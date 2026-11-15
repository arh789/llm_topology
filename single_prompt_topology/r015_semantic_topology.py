"""Convert validated R015 trajectories into within-probe topology evidence."""

from __future__ import annotations

import csv
import gc
import gzip
import hashlib
import itertools
import json
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import safetensors
import sklearn
import torch
import torch.nn.functional as F
import transformers
from safetensors import safe_open
from safetensors.torch import save_file
from transformers import AutoTokenizer

from r015_config import (
    LOCAL_PERMUTATIONS,
    MODEL_ID,
    MODEL_REVISION,
    PROBE_PROMPT_IDS,
    PROBES,
    PROMPT_IDS,
    PROMPT_SPECS,
    RUN_ID,
)
from r012_semantic_topology import (
    K_NEIGHBORS,
    analyze_network,
    best_community_matches,
    classify_token,
    compare_state_data,
    elbow_candidate,
    state_label,
    visible_token,
)


EMBEDDING_KEY = "model.embed_tokens.weight"
SIDES = ("positive_head", "negative_tail")
STATE_COUNT = 29
HIDDEN_WIDTH = 3584
EXPECTED_NETWORKS = 1392
EXPECTED_TRANSITIONS = 1344
EXPECTED_PAIRWISE_COMPARISONS = 3480
EXPECTED_INVARIANCE_SUMMARY_ROWS = 2784

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
CAPTURE_DIR = RUN_DIR / "primary_7b_bf16"
PLAN_PATH = PIPELINE_DIR / "R015_PLAN.md"
CONCEPT_EVIDENCE_PATH = PIPELINE_DIR / "R015_CONCEPT_SELECTION_EVIDENCE.md"
MANIFEST_PATH = RUN_DIR / "manifest.json"
SNAPSHOT_DIR = Path(
    r"D:\AI\cache\huggingface\hub\models--Qwen--Qwen2.5-7B-Instruct"
) / "snapshots" / MODEL_REVISION


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def artifact_record(path: Path) -> dict[str, Any]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def write_manifest(manifest: dict[str, Any]) -> None:
    write_json(MANIFEST_PATH, manifest)


def complete_component(
    manifest: dict[str, Any],
    name: str,
    started: float,
    **values: Any,
) -> None:
    manifest["components"][name] = {
        "status": "successful",
        "completed_at": utc_now(),
        "seconds": time.perf_counter() - started,
        **values,
    }
    write_manifest(manifest)


def support_records(
    probe_id: str,
    prompt_ids: tuple[str, ...],
    state_index: int,
    side: str,
    state_data: dict[tuple[str, str], dict[str, Any]],
    decoded_tokens: list[str],
    token_writer: csv.DictWriter,
    edge_writer: csv.DictWriter,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    token_counts: Counter[int] = Counter()
    token_prompts: defaultdict[int, list[str]] = defaultdict(list)
    edge_counts: Counter[tuple[int, int]] = Counter()
    edge_prompts: defaultdict[tuple[int, int], list[str]] = defaultdict(list)

    for prompt_id in prompt_ids:
        data = state_data[(prompt_id, side)]
        for token_id in data["membership"]:
            token_counts[int(token_id)] += 1
            token_prompts[int(token_id)].append(prompt_id)
        for edge in data["edges"]:
            normalized = (int(edge[0]), int(edge[1]))
            edge_counts[normalized] += 1
            edge_prompts[normalized].append(prompt_id)

    for token_id in sorted(token_counts):
        prompt_support = token_prompts[token_id]
        token_writer.writerow(
            {
                "probe_id": probe_id,
                "state_index": state_index,
                "state_label": state_label(state_index),
                "side": side,
                "token_id": token_id,
                "decoded_token": visible_token(decoded_tokens[token_id]),
                "support_count": token_counts[token_id],
                "prompt_ids": "|".join(prompt_support),
                "local_permutations": "|".join(
                    str(PROMPT_SPECS[item]["local_permutation"])
                    for item in prompt_support
                ),
            }
        )
    for token_a, token_b in sorted(edge_counts):
        prompt_support = edge_prompts[(token_a, token_b)]
        edge_writer.writerow(
            {
                "probe_id": probe_id,
                "state_index": state_index,
                "state_label": state_label(state_index),
                "side": side,
                "token_a": token_a,
                "token_b": token_b,
                "support_count": edge_counts[(token_a, token_b)],
                "prompt_ids": "|".join(prompt_support),
                "local_permutations": "|".join(
                    str(PROMPT_SPECS[item]["local_permutation"])
                    for item in prompt_support
                ),
            }
        )

    rows: list[dict[str, Any]] = []
    token_distribution = Counter(token_counts.values())
    edge_distribution = Counter(edge_counts.values())
    for item_type, distribution, total in (
        ("token", token_distribution, len(token_counts)),
        ("edge", edge_distribution, len(edge_counts)),
    ):
        for support_count in range(1, len(prompt_ids) + 1):
            item_count = int(distribution.get(support_count, 0))
            rows.append(
                {
                    "probe_id": probe_id,
                    "state_index": state_index,
                    "state_label": state_label(state_index),
                    "side": side,
                    "item_type": item_type,
                    "support_count": support_count,
                    "item_count": item_count,
                    "total_unique_items": total,
                    "fraction_of_unique_items": item_count / total if total else 0.0,
                }
            )
    return rows, {
        "unique_tokens": len(token_counts),
        "six_of_six_tokens": int(token_distribution.get(6, 0)),
        "unique_edges": len(edge_counts),
        "six_of_six_edges": int(edge_distribution.get(6, 0)),
    }

def main() -> None:
    started_at = utc_now()
    started_perf = time.perf_counter()
    manifest = load_json(MANIFEST_PATH)
    if manifest.get("run_id") != RUN_ID:
        raise RuntimeError("R015 manifest identity mismatch.")
    if manifest.get("status") != "running":
        raise RuntimeError("R015 must be running before topology execution.")
    current_component = "projection_and_cutoffs"

    try:
        if (
            not PLAN_PATH.is_file()
            or not CONCEPT_EVIDENCE_PATH.is_file()
            or not SNAPSHOT_DIR.is_dir()
        ):
            raise FileNotFoundError(
                "R015 plan, concept evidence or cached Qwen snapshot is missing."
            )
        if manifest["model"]["id"] != MODEL_ID:
            raise RuntimeError("Manifest model does not match the locked backend.")

        capture_hashes = load_json(CAPTURE_DIR / "artifact_hashes.json")
        required_capture_names = [
            *(f"{prompt_id}_hidden_states.safetensors" for prompt_id in PROMPT_IDS),
            "prompt_records.json",
            "run_metadata.json",
            "permutation_validation.json",
            "pairwise_hidden_state_metrics.csv",
        ]
        for name in required_capture_names:
            path = CAPTURE_DIR / name
            expected = capture_hashes[name]
            if (
                path.stat().st_size != expected["bytes"]
                or sha256_file(path) != expected["sha256"]
            ):
                raise RuntimeError(f"Capture artifact failed validation: {name}")
        validation = load_json(CAPTURE_DIR / "permutation_validation.json")
        if validation.get("status") != "successful":
            raise RuntimeError("Capture validation is not successful.")
        if not validation.get("state_00_exact_equal_all_prompts"):
            raise RuntimeError("Capture validation did not establish State 00 equality.")

        model_index = load_json(SNAPSHOT_DIR / "model.safetensors.index.json")
        shard_name = model_index["weight_map"].get(EMBEDDING_KEY)
        if not shard_name:
            raise KeyError(f"Missing embedding tensor: {EMBEDDING_KEY}")
        tokenizer = AutoTokenizer.from_pretrained(
            SNAPSHOT_DIR,
            local_files_only=True,
            trust_remote_code=False,
        )
        vocabulary_size = len(tokenizer)
        special_ids = set(map(int, tokenizer.all_special_ids))
        raw_tokens = tokenizer.convert_ids_to_tokens(list(range(vocabulary_size)))
        decoded_tokens = [
            tokenizer.decode(
                [token_id],
                skip_special_tokens=False,
                clean_up_tokenization_spaces=False,
            )
            for token_id in range(vocabulary_size)
        ]
        token_classes = [
            classify_token(token_id, decoded_tokens[token_id], special_ids)
            for token_id in range(vocabulary_size)
        ]

        prompt_records = load_json(CAPTURE_DIR / "prompt_records.json")
        capture_token_ids = {
            int(prompt_records[prompt_id]["capture_token_id"])
            for prompt_id in PROMPT_IDS
        }
        if len(capture_token_ids) != 1:
            raise RuntimeError("Captures do not share one anchor-token ID.")
        capture_token_id = capture_token_ids.pop()

        trajectories: list[torch.Tensor] = []
        for prompt_id in PROMPT_IDS:
            with safe_open(
                str(CAPTURE_DIR / f"{prompt_id}_hidden_states.safetensors"),
                framework="pt",
                device="cpu",
            ) as handle:
                tensor = handle.get_tensor("hidden_states").float()
            if tuple(tensor.shape) != (STATE_COUNT, HIDDEN_WIDTH):
                raise RuntimeError(
                    f"Unexpected {prompt_id} trajectory shape: {tuple(tensor.shape)}"
                )
            trajectories.append(tensor)
        hidden_states = torch.stack(trajectories)
        if not torch.isfinite(hidden_states).all():
            raise RuntimeError("Hidden states contain non-finite values.")
        if not all(
            torch.equal(hidden_states[0, 0], hidden_states[index, 0])
            for index in range(1, len(PROMPT_IDS))
        ):
            raise RuntimeError("State 00 equality failed during topology reload.")

        with safe_open(
            str(SNAPSHOT_DIR / shard_name), framework="pt", device="cpu"
        ) as handle:
            embedding_matrix = handle.get_tensor(EMBEDDING_KEY)
        full_embedding_rows = int(embedding_matrix.shape[0])
        if embedding_matrix.ndim != 2 or embedding_matrix.shape[1] != HIDDEN_WIDTH:
            raise RuntimeError(
                f"Unexpected embedding shape: {tuple(embedding_matrix.shape)}"
            )
        if full_embedding_rows < vocabulary_size:
            raise RuntimeError("Embedding table has fewer rows than usable token IDs.")
        embedding_matrix = embedding_matrix[:vocabulary_size]

        if not torch.cuda.is_available():
            raise RuntimeError("R015 exact topology execution requires CUDA.")
        device = torch.device("cuda")
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        normalized_embeddings = F.normalize(
            embedding_matrix.to(device=device, dtype=torch.float32), p=2, dim=1
        )
        normalized_states = F.normalize(
            hidden_states.to(device=device, dtype=torch.float32), p=2, dim=2
        )
        with torch.inference_mode():
            scores_tensor = torch.einsum(
                "psd,vd->psv", normalized_states, normalized_embeddings
            ).cpu().contiguous()
        if not torch.isfinite(scores_tensor).all():
            raise RuntimeError("Vocabulary score tensor contains non-finite values.")
        scores_path = RUN_DIR / "vocabulary_scores.safetensors"
        save_file(
            {"cosine_scores": scores_tensor},
            str(scores_path),
            metadata={
                "prompt_ids": ",".join(PROMPT_IDS),
                "probe_ids": ",".join(PROBES),
                "state_count": str(STATE_COUNT),
                "vocabulary_size": str(vocabulary_size),
                "excluded_capture_token_id": str(capture_token_id),
            },
        )
        del normalized_states, hidden_states, trajectories, embedding_matrix
        gc.collect()

        eligible_ids = np.arange(vocabulary_size, dtype=np.int64)
        eligible_ids = eligible_ids[eligible_ids != capture_token_id]
        scores = scores_tensor.numpy()
        cutoff_records: list[dict[str, Any]] = []
        membership_frames: list[pd.DataFrame] = []
        membership_by_key: dict[tuple[str, int, str], pd.DataFrame] = {}
        for prompt_index, prompt_id in enumerate(PROMPT_IDS):
            spec = PROMPT_SPECS[prompt_id]
            for state_index in range(STATE_COUNT):
                state_scores = scores[prompt_index, state_index]
                descending = eligible_ids[
                    np.argsort(-state_scores[eligible_ids], kind="stable")
                ]
                ascending = eligible_ids[
                    np.argsort(state_scores[eligible_ids], kind="stable")
                ]
                upper = elbow_candidate(state_scores[descending])
                lower_inverted = elbow_candidate(-state_scores[ascending])
                upper_rank = int(upper["cutoff_rank"])
                lower_rank = int(lower_inverted["cutoff_rank"])
                positive_ids = descending[:upper_rank]
                negative_ids = ascending[:lower_rank]
                if np.intersect1d(positive_ids, negative_ids).size:
                    raise RuntimeError(
                        f"Cutoff populations overlap at {prompt_id} State {state_index}."
                    )
                cutoff_records.append(
                    {
                        "prompt_id": prompt_id,
                        "probe_id": spec["probe_id"],
                        "local_permutation": spec["local_permutation"],
                        "state_index": state_index,
                        "state_label": state_label(state_index),
                        "eligible_vocabulary_size": len(eligible_ids),
                        "excluded_capture_token_id": capture_token_id,
                        "upper_cutoff_rank": upper_rank,
                        "upper_cutoff_score": upper["cutoff_score"],
                        "upper_elbow_strength": upper["elbow_strength"],
                        "upper_score_gap_after": upper["score_gap_after"],
                        "upper_gap_ratio": upper["gap_ratio"],
                        "lower_cutoff_rank": lower_rank,
                        "lower_cutoff_score": -float(lower_inverted["cutoff_score"]),
                        "lower_elbow_strength": lower_inverted["elbow_strength"],
                        "lower_score_gap_after": lower_inverted["score_gap_after"],
                        "lower_gap_ratio": lower_inverted["gap_ratio"],
                        "positive_head_count": upper_rank,
                        "negative_tail_count": lower_rank,
                        "central_body_count": len(eligible_ids) - upper_rank - lower_rank,
                        "positive_head_fraction": upper_rank / len(eligible_ids),
                        "negative_tail_fraction": lower_rank / len(eligible_ids),
                    }
                )
                for side, token_ids in (
                    ("positive_head", positive_ids),
                    ("negative_tail", negative_ids),
                ):
                    frame = pd.DataFrame(
                        {
                            "prompt_id": prompt_id,
                            "probe_id": spec["probe_id"],
                            "local_permutation": spec["local_permutation"],
                            "state_index": state_index,
                            "state_label": state_label(state_index),
                            "side": side,
                            "token_id": token_ids,
                            "raw_token": [raw_tokens[token] for token in token_ids],
                            "decoded_token": [decoded_tokens[token] for token in token_ids],
                            "display_token": [
                                visible_token(decoded_tokens[token]) for token in token_ids
                            ],
                            "token_class": [token_classes[token] for token in token_ids],
                            "cosine_score": state_scores[token_ids],
                            "rank_from_extreme": np.arange(
                                1, len(token_ids) + 1, dtype=np.int32
                            ),
                        }
                    )
                    membership_by_key[(prompt_id, state_index, side)] = frame
                    membership_frames.append(frame)

        cutoffs = pd.DataFrame(cutoff_records).sort_values(
            ["probe_id", "local_permutation", "state_index"], kind="stable"
        )
        if len(cutoffs) != len(PROMPT_IDS) * STATE_COUNT:
            raise RuntimeError("Cutoff table has incomplete prompt-state coverage.")
        cutoffs.to_csv(RUN_DIR / "cutoffs.csv", index=False)
        tails = pd.concat(membership_frames, ignore_index=True)
        tails.to_csv(RUN_DIR / "tail_tokens.csv.gz", index=False, compression="gzip")
        complete_component(
            manifest,
            current_component,
            started_perf,
            score_shape=list(scores.shape),
            vocabulary_size=vocabulary_size,
            excluded_capture_token_id=capture_token_id,
            cutoff_rows=len(cutoffs),
            membership_rows=len(tails),
            embedding_shard=shard_name,
            full_embedding_rows=full_embedding_rows,
            usable_tokenizer_rows=vocabulary_size,
            padded_embedding_rows_excluded=full_embedding_rows - vocabulary_size,
            model_forward_executed=False,
        )
        print(
            f"R015 projection and cutoffs complete: {len(tails):,} memberships.",
            flush=True,
        )

        current_component = "split_networks_and_communities"
        component_started = time.perf_counter()
        network_records: list[dict[str, Any]] = []
        community_records: list[dict[str, Any]] = []
        community_edge_records: list[dict[str, Any]] = []
        compact_networks: list[dict[str, Any]] = []
        transition_records: list[dict[str, Any]] = []
        pairwise_records: list[dict[str, Any]] = []
        community_match_records: list[dict[str, Any]] = []
        invariance_records: list[dict[str, Any]] = []
        invariant_core_counts: dict[tuple[int, str], dict[str, int]] = {}
        previous: dict[tuple[str, str], dict[str, Any]] = {}
        node_rows = 0
        edge_rows = 0
        token_support_rows = 0
        edge_support_rows = 0

        nodes_path = RUN_DIR / "nodes.csv.gz"
        edges_path = RUN_DIR / "edges.csv.gz"
        token_support_path = RUN_DIR / "token_permutation_support.csv.gz"
        edge_support_path = RUN_DIR / "edge_permutation_support.csv.gz"
        with (
            gzip.open(nodes_path, "wt", encoding="utf-8", newline="") as node_handle,
            gzip.open(edges_path, "wt", encoding="utf-8", newline="") as edge_handle,
            gzip.open(
                token_support_path, "wt", encoding="utf-8", newline=""
            ) as token_support_handle,
            gzip.open(
                edge_support_path, "wt", encoding="utf-8", newline=""
            ) as edge_support_handle,
        ):
            token_writer = csv.DictWriter(
                token_support_handle,
                fieldnames=[
                    "probe_id",
                    "state_index",
                    "state_label",
                    "side",
                    "token_id",
                    "decoded_token",
                    "support_count",
                    "prompt_ids",
                    "local_permutations",
                ],
            )
            edge_writer = csv.DictWriter(
                edge_support_handle,
                fieldnames=[
                    "probe_id",
                    "state_index",
                    "state_label",
                    "side",
                    "token_a",
                    "token_b",
                    "support_count",
                    "prompt_ids",
                    "local_permutations",
                ],
            )
            token_writer.writeheader()
            edge_writer.writeheader()

            for state_index in range(STATE_COUNT):
                current_state: dict[tuple[str, str], dict[str, Any]] = {}
                for prompt_index, prompt_id in enumerate(PROMPT_IDS):
                    spec = PROMPT_SPECS[prompt_id]
                    probe_id = str(spec["probe_id"])
                    local_permutation = str(spec["local_permutation"])
                    for side_index, side in enumerate(SIDES):
                        network_started = time.perf_counter()
                        state_tokens = membership_by_key[
                            (prompt_id, state_index, side)
                        ]
                        (
                            metric,
                            node_frame,
                            edge_frame,
                            communities,
                            community_edges,
                            state_data,
                            compact,
                        ) = analyze_network(
                            prompt_id,
                            prompt_index,
                            state_index,
                            side,
                            side_index,
                            state_tokens,
                            normalized_embeddings,
                            vocabulary_size,
                        )
                        metric["prompt_id"] = metric.pop("prompt")
                        metric["probe_id"] = probe_id
                        metric["local_permutation"] = local_permutation
                        node_frame = node_frame.rename(columns={"prompt": "prompt_id"})
                        node_frame["probe_id"] = probe_id
                        node_frame["local_permutation"] = local_permutation
                        edge_frame["prompt_id"] = edge_frame.pop("prompt")
                        edge_frame["probe_id"] = probe_id
                        edge_frame["local_permutation"] = local_permutation
                        for record in communities:
                            record["prompt_id"] = record.pop("prompt")
                            record["probe_id"] = probe_id
                            record["local_permutation"] = local_permutation
                        for record in community_edges:
                            record["prompt_id"] = record.pop("prompt")
                            record["probe_id"] = probe_id
                            record["local_permutation"] = local_permutation
                        compact["prompt_id"] = compact.pop("prompt")
                        compact["probe_id"] = probe_id
                        compact["local_permutation"] = local_permutation

                        node_frame.to_csv(
                            node_handle, index=False, header=node_rows == 0
                        )
                        edge_frame.to_csv(
                            edge_handle, index=False, header=edge_rows == 0
                        )
                        node_rows += len(node_frame)
                        edge_rows += len(edge_frame)
                        network_records.append(metric)
                        community_records.extend(communities)
                        community_edge_records.extend(community_edges)
                        compact_networks.append(compact)
                        current_state[(prompt_id, side)] = state_data

                        prior = previous.get((prompt_id, side))
                        if prior is not None:
                            comparison = compare_state_data(prior, state_data)
                            transition_records.append(
                                {
                                    "probe_id": probe_id,
                                    "prompt_id": prompt_id,
                                    "local_permutation": local_permutation,
                                    "side": side,
                                    "previous_state_index": state_index - 1,
                                    "current_state_index": state_index,
                                    "previous_state_label": state_label(state_index - 1),
                                    "current_state_label": state_label(state_index),
                                    **comparison,
                                }
                            )
                            community_match_records.extend(
                                best_community_matches(
                                    "adjacent_state",
                                    side,
                                    prior,
                                    state_data,
                                    probe_id=probe_id,
                                    prompt_id=prompt_id,
                                    local_permutation=local_permutation,
                                    source_prompt_id=prompt_id,
                                    target_prompt_id=prompt_id,
                                    source_state_index=state_index - 1,
                                    target_state_index=state_index,
                                )
                            )
                        previous[(prompt_id, side)] = state_data
                        print(
                            f"R015 network {len(network_records):04d}/"
                            f"{EXPECTED_NETWORKS}: {prompt_id} State "
                            f"{state_index:02d} {side}, {len(node_frame):,} nodes, "
                            f"{len(communities)} communities, "
                            f"{time.perf_counter() - network_started:.1f}s.",
                            flush=True,
                        )

                for probe_id, prompt_ids in PROBE_PROMPT_IDS.items():
                    for side in SIDES:
                        for source_id, target_id in itertools.combinations(
                            prompt_ids, 2
                        ):
                            source_data = current_state[(source_id, side)]
                            target_data = current_state[(target_id, side)]
                            comparison = compare_state_data(source_data, target_data)
                            pairwise_records.append(
                                {
                                    "probe_id": probe_id,
                                    "source_prompt_id": source_id,
                                    "target_prompt_id": target_id,
                                    "source_local_permutation": PROMPT_SPECS[source_id][
                                        "local_permutation"
                                    ],
                                    "target_local_permutation": PROMPT_SPECS[target_id][
                                        "local_permutation"
                                    ],
                                    "state_index": state_index,
                                    "state_label": state_label(state_index),
                                    "side": side,
                                    **comparison,
                                }
                            )
                            community_match_records.extend(
                                best_community_matches(
                                    "within_probe_permutation_pair",
                                    side,
                                    source_data,
                                    target_data,
                                    probe_id=probe_id,
                                    source_prompt_id=source_id,
                                    target_prompt_id=target_id,
                                    source_local_permutation=PROMPT_SPECS[source_id][
                                        "local_permutation"
                                    ],
                                    target_local_permutation=PROMPT_SPECS[target_id][
                                        "local_permutation"
                                    ],
                                    source_state_index=state_index,
                                    target_state_index=state_index,
                                )
                            )

                        summary_rows, core_counts = support_records(
                            probe_id,
                            prompt_ids,
                            state_index,
                            side,
                            current_state,
                            decoded_tokens,
                            token_writer,
                            edge_writer,
                        )
                        invariance_records.extend(summary_rows)
                        invariant_core_counts[(probe_id, state_index, side)] = (
                            core_counts
                        )
                        token_support_rows += core_counts["unique_tokens"]
                        edge_support_rows += core_counts["unique_edges"]

        network_index = pd.DataFrame(network_records).sort_values(
            ["state_index", "probe_id", "local_permutation", "side"],
            kind="stable",
        )
        community_nodes = pd.DataFrame(community_records).sort_values(
            ["state_index", "probe_id", "local_permutation", "side", "community_id"],
            kind="stable",
        )
        community_edges = pd.DataFrame(community_edge_records).sort_values(
            [
                "state_index",
                "probe_id",
                "local_permutation",
                "side",
                "community_a",
                "community_b",
            ],
            kind="stable",
        )
        transitions = pd.DataFrame(transition_records).sort_values(
            ["probe_id", "local_permutation", "side", "current_state_index"],
            kind="stable",
        )
        pairwise = pd.DataFrame(pairwise_records).sort_values(
            [
                "state_index",
                "probe_id",
                "side",
                "source_local_permutation",
                "target_local_permutation",
            ],
            kind="stable",
        )
        invariance = pd.DataFrame(invariance_records).sort_values(
            ["state_index", "probe_id", "side", "item_type", "support_count"],
            kind="stable",
        )
        community_matches = pd.DataFrame(community_match_records)
        network_index.to_csv(RUN_DIR / "network_index.csv", index=False)
        community_nodes.to_csv(RUN_DIR / "community_nodes.csv", index=False)
        community_edges.to_csv(RUN_DIR / "community_edges.csv", index=False)
        transitions.to_csv(RUN_DIR / "state_transitions.csv", index=False)
        pairwise.to_csv(
            RUN_DIR / "pairwise_permutation_comparisons.csv", index=False
        )
        invariance.to_csv(RUN_DIR / "permutation_invariance.csv", index=False)
        community_matches.to_csv(
            RUN_DIR / "community_transition_evidence.csv", index=False
        )
        complete_component(
            manifest,
            current_component,
            component_started,
            network_count=len(network_index),
            node_rows=node_rows,
            directed_edge_rows=edge_rows,
            community_rows=len(community_nodes),
            intercommunity_edge_rows=len(community_edges),
        )

        current_component = "within_prompt_transitions"
        component_started = time.perf_counter()
        if len(transitions) != EXPECTED_TRANSITIONS:
            raise RuntimeError(
                f"Expected {EXPECTED_TRANSITIONS} transitions, found {len(transitions)}."
            )
        complete_component(
            manifest,
            current_component,
            component_started,
            transition_rows=len(transitions),
            minimum_membership_jaccard=float(transitions["membership_jaccard"].min()),
            minimum_edge_jaccard=float(transitions["edge_jaccard"].min()),
        )

        current_component = "within_probe_permutation_comparisons"
        component_started = time.perf_counter()
        if len(pairwise) != EXPECTED_PAIRWISE_COMPARISONS:
            raise RuntimeError(
                f"Expected {EXPECTED_PAIRWISE_COMPARISONS} pairwise rows, "
                f"found {len(pairwise)}."
            )
        complete_component(
            manifest,
            current_component,
            component_started,
            pairwise_comparison_rows=len(pairwise),
            minimum_membership_jaccard=float(pairwise["membership_jaccard"].min()),
            minimum_edge_jaccard=float(pairwise["edge_jaccard"].min()),
        )

        current_component = "within_probe_invariance"
        component_started = time.perf_counter()
        if len(invariance) != EXPECTED_INVARIANCE_SUMMARY_ROWS:
            raise RuntimeError(
                f"Expected {EXPECTED_INVARIANCE_SUMMARY_ROWS} invariance summary rows, "
                f"found {len(invariance)}."
            )
        complete_component(
            manifest,
            current_component,
            component_started,
            summary_rows=len(invariance),
            token_support_rows=token_support_rows,
            edge_support_rows=edge_support_rows,
            support_levels=list(range(1, 7)),
            token_and_edge_support_separate=True,
        )

        current_component = "chatgpt_exports"
        component_started = time.perf_counter()
        compact_document = {
            "schema_version": 1,
            "run_id": RUN_ID,
            "model": {"id": MODEL_ID, "revision": MODEL_REVISION},
            "probe_records": {
                probe_id: {
                    "concept_keys": list(PROBES[probe_id]),
                    "concepts": [
                        PROMPT_SPECS[prompt_ids[0]]["probe_concepts"][index]
                        for index in range(3)
                    ],
                    "prompt_ids": list(prompt_ids),
                }
                for probe_id, prompt_ids in PROBE_PROMPT_IDS.items()
            },
            "prompt_records": {
                prompt_id: {
                    "probe_id": prompt_records[prompt_id]["probe_id"],
                    "local_permutation": prompt_records[prompt_id][
                        "local_permutation"
                    ],
                    "raw_prompt": prompt_records[prompt_id]["raw_prompt"],
                    "position_1": prompt_records[prompt_id]["position_1"],
                    "position_2": prompt_records[prompt_id]["position_2"],
                    "position_3": prompt_records[prompt_id]["position_3"],
                    "capture_index": prompt_records[prompt_id]["capture_index"],
                    "capture_token_id": prompt_records[prompt_id]["capture_token_id"],
                }
                for prompt_id in PROMPT_IDS
            },
            "network_count": len(compact_networks),
            "state_count": STATE_COUNT,
            "sides": list(SIDES),
            "stable_join_key": "token_id",
            "community_identity": (
                "community_id is local to one prompt, state and side"
            ),
            "interpretation_boundary": (
                "Positive and negative denote anchor-state cosine alignment and "
                "anti-alignment in the fixed input-embedding basis. Communities are "
                "measured partitions, not semantic topics, parents, cross-probe map "
                "nodes/edges, SDA/GRD roles, coherence claims or curvature claims."
            ),
            "within_prompt_transitions": transitions.to_dict(orient="records"),
            "within_probe_permutation_comparisons": pairwise.to_dict(
                orient="records"
            ),
            "within_probe_invariance_summary": invariance.to_dict(
                orient="records"
            ),
            "networks": compact_networks,
        }
        write_json(RUN_DIR / "chatgpt_community_networks.json", compact_document)

        compact_by_key = {
            (item["state_index"], item["prompt_id"], item["side"]): item
            for item in compact_networks
        }
        packet_lines = [
            "# R015 ChatGPT layer packets",
            "",
            "This file describes all 1,392 measured probe/prompt/state/side "
            "networks. It contains no semantic topic or parent labels.",
            "",
            "Positive and negative mean cosine alignment and anti-alignment with "
            "the evolving final-anchor state. Negative does not establish "
            "suppression, contradiction or exclusion.",
            "",
            "Token and edge support are counted independently across the six "
            "permutations within each probe. Community IDs are local and are not "
            "matched here as persistent semantic entities.",
            "",
            "Each probe must be reconstructed independently before cross-probe "
            "parent or relation matching.",
            "",
        ]
        for state_index in range(STATE_COUNT):
            packet_lines.extend(
                [f"## State {state_index:02d} — {state_label(state_index)}", ""]
            )
            state_pairs = pairwise.loc[pairwise["state_index"] == state_index]
            for probe_id, prompt_ids in PROBE_PROMPT_IDS.items():
                concepts = ", ".join(
                    str(item)
                    for item in PROMPT_SPECS[prompt_ids[0]]["probe_concepts"]
                )
                packet_lines.extend(
                    [f"### Probe {probe_id} — {concepts}", ""]
                )
                probe_pairs = state_pairs.loc[
                    state_pairs["probe_id"] == probe_id
                ]
                for side in SIDES:
                    side_pairs = probe_pairs.loc[probe_pairs["side"] == side]
                    core = invariant_core_counts[(probe_id, state_index, side)]
                    packet_lines.extend(
                        [
                            f"#### {side} within-probe measurement",
                            "",
                            f"- Membership Jaccard: min "
                            f"{side_pairs['membership_jaccard'].min():.6f}; mean "
                            f"{side_pairs['membership_jaccard'].mean():.6f}; max "
                            f"{side_pairs['membership_jaccard'].max():.6f}",
                            f"- Edge Jaccard: min "
                            f"{side_pairs['edge_jaccard'].min():.6f}; mean "
                            f"{side_pairs['edge_jaccard'].mean():.6f}; max "
                            f"{side_pairs['edge_jaccard'].max():.6f}",
                            f"- Community ARI: min "
                            f"{side_pairs['community_adjusted_rand'].min():.6f}; "
                            f"mean "
                            f"{side_pairs['community_adjusted_rand'].mean():.6f}; "
                            f"max "
                            f"{side_pairs['community_adjusted_rand'].max():.6f}",
                            f"- Tokens in 6/6 permutations: "
                            f"{core['six_of_six_tokens']} of "
                            f"{core['unique_tokens']} unique",
                            f"- Edges in 6/6 permutations: "
                            f"{core['six_of_six_edges']} of "
                            f"{core['unique_edges']} unique",
                            "",
                        ]
                    )

                for prompt_id in prompt_ids:
                    local_permutation = prompt_records[prompt_id][
                        "local_permutation"
                    ]
                    packet_lines.extend(
                        [
                            f"#### Prompt {prompt_id} — permutation "
                            f"{local_permutation}",
                            "",
                            f"Input: "
                            f"`{visible_token(prompt_records[prompt_id]['raw_prompt'])}`",
                            "",
                        ]
                    )
                    for side in SIDES:
                        network = compact_by_key[(state_index, prompt_id, side)]
                        metrics = network["metrics"]
                        packet_lines.extend(
                            [
                                f"##### {side}",
                                "",
                                f"- Nodes: {metrics['population_size']}",
                                f"- Directed 10-NN edges: "
                                f"{metrics['directed_edge_count']}",
                                f"- Undirected edges: "
                                f"{metrics['undirected_edge_count']}",
                                f"- Communities: {metrics['community_count']}",
                                f"- Modularity: "
                                f"{metrics['community_modularity']:.6f}",
                                "",
                                "All communities:",
                                "",
                            ]
                        )
                        for community in network["communities"]:
                            representatives = ", ".join(
                                community["representative_tokens"][:10]
                            )
                            extremes = ", ".join(
                                community["most_extreme_tokens"][:6]
                            )
                            packet_lines.append(
                                f"- C{community['community_id']} "
                                f"(n={community['community_size']}): "
                                f"representatives [{representatives}]; "
                                f"target-extreme [{extremes}]; classes "
                                f"{community['token_class_counts']}"
                            )
                        packet_lines.extend(
                            ["", "Strongest intercommunity connections:", ""]
                        )
                        strongest = sorted(
                            network["intercommunity_edges"],
                            key=lambda item: (
                                -int(item["token_edge_count"]),
                                -float(item["mean_cosine_similarity"]),
                            ),
                        )[:15]
                        if strongest:
                            for edge in strongest:
                                packet_lines.append(
                                    f"- C{edge['community_a']} to "
                                    f"C{edge['community_b']}: "
                                    f"{edge['token_edge_count']} token edges; "
                                    f"mean cosine "
                                    f"{edge['mean_cosine_similarity']:.6f}"
                                )
                        else:
                            packet_lines.append("- None")
                        packet_lines.append("")
        (RUN_DIR / "chatgpt_layer_packets.md").write_text(
            "\n".join(packet_lines), encoding="utf-8"
        )
        complete_component(
            manifest,
            current_component,
            component_started,
            json_networks=len(compact_networks),
            markdown_state_sections=STATE_COUNT,
            semantic_labels_added=False,
        )

        current_component = "completeness_validation"
        component_started = time.perf_counter()
        if len(network_index) != EXPECTED_NETWORKS:
            raise RuntimeError(
                f"Expected {EXPECTED_NETWORKS} networks, found {len(network_index)}."
            )
        if network_index.duplicated(
            ["prompt_id", "state_index", "side"]
        ).any():
            raise RuntimeError("Duplicate network identity found.")
        if pairwise.duplicated(
            [
                "probe_id",
                "source_prompt_id",
                "target_prompt_id",
                "state_index",
                "side",
            ]
        ).any():
            raise RuntimeError("Duplicate pairwise comparison identity found.")
        expected_node_rows = int(network_index["population_size"].sum())
        expected_edge_rows = int(network_index["directed_edge_count"].sum())
        if node_rows != expected_node_rows or edge_rows != expected_edge_rows:
            raise RuntimeError("Streamed node or edge rows do not reconcile.")
        if not (
            network_index["directed_edge_count"]
            == network_index["population_size"] * K_NEIGHBORS
        ).all():
            raise RuntimeError("One or more networks lack exact 10-NN coverage.")
        community_size_totals = community_nodes.groupby(
            ["prompt_id", "state_index", "side"]
        )["community_size"].sum()
        population_totals = network_index.set_index(
            ["prompt_id", "state_index", "side"]
        )["population_size"]
        if not community_size_totals.equals(population_totals.sort_index()):
            raise RuntimeError("Community sizes do not reconcile with populations.")
        state_zero = pairwise.loc[pairwise["state_index"] == 0]
        if len(state_zero) != 120 or not (
            np.allclose(state_zero["membership_jaccard"], 1.0)
            and np.allclose(state_zero["edge_jaccard"], 1.0)
            and np.allclose(state_zero["community_adjusted_rand"], 1.0)
        ):
            raise RuntimeError("State 00 topology is not identical across all pairs.")
        for probe_id in PROBES:
            for side in SIDES:
                for item_type in ("token", "edge"):
                    state_zero_distribution = invariance.loc[
                        (invariance["probe_id"] == probe_id)
                        & (invariance["state_index"] == 0)
                        & (invariance["side"] == side)
                        & (invariance["item_type"] == item_type)
                    ]
                    non_six = state_zero_distribution.loc[
                        state_zero_distribution["support_count"] < 6,
                        "item_count",
                    ].sum()
                    if int(non_six) != 0:
                        raise RuntimeError(
                            f"State 00 {probe_id} {side} {item_type} support "
                            "is not entirely 6/6."
                        )
        if compact_document["network_count"] != EXPECTED_NETWORKS:
            raise RuntimeError("ChatGPT JSON network count is incomplete.")

        verification_path = RUN_DIR / "R015_COMPLETENESS_VERIFICATION.md"
        verification_path.write_text(
            "\n".join(
                [
                    "# R015 completeness verification",
                    "",
                    "- Status: PASS",
                    f"- Networks: {len(network_index)} / {EXPECTED_NETWORKS}",
                    f"- Within-prompt transitions: {len(transitions)} / {EXPECTED_TRANSITIONS}",
                    f"- Within-probe permutation comparisons: {len(pairwise)} / {EXPECTED_PAIRWISE_COMPARISONS}",
                    f"- Invariance summary rows: {len(invariance)} / {EXPECTED_INVARIANCE_SUMMARY_ROWS}",
                    f"- Selected token memberships: {node_rows:,}",
                    f"- Directed exact 10-NN edges: {edge_rows:,}",
                    f"- State-local communities: {len(community_nodes):,}",
                    f"- Item-level token-support rows: {token_support_rows:,}",
                    f"- Item-level edge-support rows: {edge_support_rows:,}",
                    "- Every network and pairwise identity is unique.",
                    "- Every selected node belongs to exactly one community.",
                    "- Every network has exactly 10 directed neighbours per node.",
                    "- State 00 topology is identical across all 60 within-probe pairs on both sides.",
                    "- State 00 tokens and edges all have 6/6 support within every probe.",
                    "- ChatGPT JSON contains all 1,392 networks.",
                    "- Semantic labels and SDA/GRD roles were not added.",
                ]
            ),
            encoding="utf-8",
        )
        complete_component(
            manifest,
            current_component,
            component_started,
            networks_verified=len(network_index),
            nodes_verified=node_rows,
            directed_edges_verified=edge_rows,
            communities_verified=len(community_nodes),
            state_zero_all_pairs_identity_verified=True,
            token_support_rows_verified=token_support_rows,
            edge_support_rows_verified=edge_support_rows,
        )

        current_component = "run_report"
        component_started = time.perf_counter()
        cutoff_summary = cutoffs[["positive_head_count", "negative_tail_count"]]
        min_pair_row = pairwise.loc[pairwise["membership_jaccard"].idxmin()]
        min_edge_pair_row = pairwise.loc[pairwise["edge_jaccard"].idxmin()]
        min_transition_row = transitions.loc[
            transitions["membership_jaccard"].idxmin()
        ]
        final_core_lines: list[str] = []
        for probe_id in PROBES:
            positive = invariant_core_counts[
                (probe_id, STATE_COUNT - 1, "positive_head")
            ]
            negative = invariant_core_counts[
                (probe_id, STATE_COUNT - 1, "negative_tail")
            ]
            final_core_lines.extend(
                [
                    f"- {probe_id} final positive 6/6 core: "
                    f"{positive['six_of_six_tokens']:,} tokens and "
                    f"{positive['six_of_six_edges']:,} edges.",
                    f"- {probe_id} final negative 6/6 core: "
                    f"{negative['six_of_six_tokens']:,} tokens and "
                    f"{negative['six_of_six_edges']:,} edges.",
                ]
            )

        report_path = RUN_DIR / "R015_MEASUREMENT_REPORT.md"
        report_lines = [
            "# R015 overlapping-context topology measurement report",
            "",
            "## Outcome",
            "",
            "R015 completed the controlled four-probe, 24-prompt measurement "
            "pipeline. Every overlapping concept triplet was measured in six "
            "orders at the same final newline anchor. The trajectories were "
            "projected into the fixed input-embedding vocabulary, divided by the "
            "locked full-curve elbows, converted into 1,392 exact split networks, "
            "partitioned into state-local communities and compared within each "
            "probe across depth and order.",
            "",
            "No chat template, assistant prefix or response generation was used. "
            "No semantic topic labels, parent nodes, cross-probe map nodes/edges, "
            "SDA roles, GRD roles, coherence claims or semantic-curvature claims "
            "were inferred.",
            "",
            "## Coverage",
            "",
            f"- Probes: {len(PROBES)}",
            f"- Prompts: {len(PROMPT_IDS)}",
            f"- Networks: {len(network_index)}",
            f"- Selected token memberships: {node_rows:,}",
            f"- Directed 10-NN edges: {edge_rows:,}",
            f"- State-local communities: {len(community_nodes):,}",
            f"- Within-prompt adjacent-state comparisons: {len(transitions)}",
            f"- Within-probe same-state permutation comparisons: {len(pairwise)}",
            f"- Item-level token-support rows: {token_support_rows:,}",
            f"- Item-level edge-support rows: {edge_support_rows:,}",
            "",
            "## Measured findings",
            "",
            f"- Positive populations ranged from "
            f"{int(cutoff_summary['positive_head_count'].min()):,} to "
            f"{int(cutoff_summary['positive_head_count'].max()):,} tokens "
            f"(median {cutoff_summary['positive_head_count'].median():,.0f}).",
            f"- Negative populations ranged from "
            f"{int(cutoff_summary['negative_tail_count'].min()):,} to "
            f"{int(cutoff_summary['negative_tail_count'].max()):,} tokens "
            f"(median {cutoff_summary['negative_tail_count'].median():,.0f}).",
            f"- The smallest within-probe membership Jaccard was "
            f"{min_pair_row.membership_jaccard:.6f} for "
            f"{min_pair_row.source_prompt_id} vs "
            f"{min_pair_row.target_prompt_id}, State "
            f"{int(min_pair_row.state_index):02d}, {min_pair_row.side}.",
            f"- The smallest within-probe edge Jaccard was "
            f"{min_edge_pair_row.edge_jaccard:.6f} for "
            f"{min_edge_pair_row.source_prompt_id} vs "
            f"{min_edge_pair_row.target_prompt_id}, State "
            f"{int(min_edge_pair_row.state_index):02d}, "
            f"{min_edge_pair_row.side}.",
            f"- The largest adjacent-state membership reorganisation "
            f"(Jaccard {min_transition_row.membership_jaccard:.6f}) occurred "
            f"for {min_transition_row.prompt_id} {min_transition_row.side}, "
            f"State {int(min_transition_row.previous_state_index):02d} → "
            f"{int(min_transition_row.current_state_index):02d}.",
            *final_core_lines,
            f"- Community counts ranged from "
            f"{int(network_index['community_count'].min())} to "
            f"{int(network_index['community_count'].max())} per network.",
            "- State 00 topology was identical across all prompts; subsequent "
            "differences arise only after contextual processing.",
            "",
            "These are measured structural results. Every probe must be "
            "semantically reconstructed independently before cross-probe parent "
            "or relation matching. Whether a local semantic map is supported is "
            "a downstream analytical question.",
        ]
        report_path.write_text("\n".join(report_lines), encoding="utf-8")
        complete_component(
            manifest,
            current_component,
            component_started,
            path=str(report_path.relative_to(PROJECT_DIR)).replace("\\", "/"),
        )
        output_names = [
            "vocabulary_scores.safetensors",
            "cutoffs.csv",
            "tail_tokens.csv.gz",
            "network_index.csv",
            "nodes.csv.gz",
            "edges.csv.gz",
            "community_nodes.csv",
            "community_edges.csv",
            "state_transitions.csv",
            "pairwise_permutation_comparisons.csv",
            "permutation_invariance.csv",
            "token_permutation_support.csv.gz",
            "edge_permutation_support.csv.gz",
            "community_transition_evidence.csv",
            "chatgpt_community_networks.json",
            "chatgpt_layer_packets.md",
            "R015_COMPLETENESS_VERIFICATION.md",
            "R015_MEASUREMENT_REPORT.md",
        ]
        manifest["artifacts"].update(
            {name: artifact_record(RUN_DIR / name) for name in output_names}
        )
        manifest["pipeline"] = {
            "orchestrator": "single_prompt_topology/r015_run.py",
            "capture_script": "single_prompt_topology/r015_capture_hidden_states.py",
            "topology_script": "single_prompt_topology/r015_semantic_topology.py",
            "topology_script_sha256": sha256_file(Path(__file__).resolve()),
            "plan": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
            "plan_sha256": sha256_file(PLAN_PATH),
            "concept_selection_evidence": str(
                CONCEPT_EVIDENCE_PATH.relative_to(PROJECT_DIR)
            ).replace("\\", "/"),
            "concept_selection_evidence_sha256": sha256_file(
                CONCEPT_EVIDENCE_PATH
            ),
            "prompt_config": "single_prompt_topology/r015_config.py",
            "prompt_config_sha256": sha256_file(
                PIPELINE_DIR / "r015_config.py"
            ),
            "measurement_functions_reused_from": (
                "single_prompt_topology/r012_semantic_topology.py"
            ),
            "model_backend": "direct Qwen Transformers capture artifacts",
            "downstream_analysis": (
                "independent semantic reconstruction per probe, followed by "
                "cross-probe parent and relation matching"
            ),
        }
        manifest["results"] = {
            "network_count": len(network_index),
            "selected_membership_rows": node_rows,
            "directed_edge_rows": edge_rows,
            "community_count": len(community_nodes),
            "adjacent_transition_rows": len(transitions),
            "pairwise_comparison_rows": len(pairwise),
            "invariance_summary_rows": len(invariance),
            "token_support_rows": token_support_rows,
            "edge_support_rows": edge_support_rows,
            "minimum_within_probe_membership_jaccard": float(
                pairwise["membership_jaccard"].min()
            ),
            "minimum_within_probe_edge_jaccard": float(
                pairwise["edge_jaccard"].min()
            ),
            "final_six_of_six_cores": {
                probe_id: {
                    side: invariant_core_counts[
                        (probe_id, STATE_COUNT - 1, side)
                    ]
                    for side in SIDES
                }
                for probe_id in PROBES
            },
        }
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now()
        manifest["failure_details"] = None
        manifest["execution_attempts"][-1].update(
            {
                "status": "successful",
                "completed_at": manifest["completed_at"],
                "seconds": time.perf_counter() - started_perf,
            }
        )
        write_manifest(manifest)

        artifact_index = {
            "generated_at": utc_now(),
            "run_id": RUN_ID,
            "manifest_status": "successful",
            "artifacts": {
                str(path.relative_to(RUN_DIR)).replace("\\", "/"): artifact_record(
                    path
                )
                for path in sorted(RUN_DIR.rglob("*"))
                if path.is_file()
                and path.name not in {
                    "artifact_index.json",
                    "R015_EXECUTION_LOG.md",
                }
            },
            "excluded_mutable_log": "R015_EXECUTION_LOG.md",
        }
        write_json(RUN_DIR / "artifact_index.json", artifact_index)
        print(
            f"R015 complete: {len(network_index)} networks, "
            f"{len(community_nodes):,} communities, "
            f"{time.perf_counter() - started_perf:.1f}s.",
            flush=True,
        )

    except Exception as error:
        manifest = load_json(MANIFEST_PATH)
        manifest["status"] = "failed"
        manifest["completed_at"] = utc_now()
        manifest["failure_details"] = {
            "component": current_component,
            "error_type": type(error).__name__,
            "message": str(error),
        }
        manifest["components"].setdefault(current_component, {})
        manifest["components"][current_component].update(
            {
                "status": "failed",
                "failed_at": manifest["completed_at"],
                "error_type": type(error).__name__,
                "message": str(error),
            }
        )
        if manifest.get("execution_attempts"):
            manifest["execution_attempts"][-1].update(
                {
                    "status": "failed",
                    "completed_at": manifest["completed_at"],
                    "component": current_component,
                    "error_type": type(error).__name__,
                    "message": str(error),
                }
            )
        write_manifest(manifest)
        raise


if __name__ == "__main__":
    main()
