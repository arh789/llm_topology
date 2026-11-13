"""Complete R012 from validated Qwen trajectories to measured topology exports."""

from __future__ import annotations

import gc
import gzip
import hashlib
import json
import math
import platform
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
import safetensors
import sklearn
import torch
import torch.nn.functional as F
import transformers
from safetensors import safe_open
from safetensors.torch import save_file
from sklearn.metrics import adjusted_rand_score
from transformers import AutoTokenizer


RUN_ID = "R012_qwen-whole-prompt-paired-capture"
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
MODEL_REVISION = "a09a35458c702b33eeacc393d103063234e8bc28"
EMBEDDING_KEY = "model.embed_tokens.weight"
PROMPTS = ("baseline", "variation")
SIDES = ("positive_head", "negative_tail")
STATE_COUNT = 29
HIDDEN_WIDTH = 3584
K_NEIGHBORS = 10
LOUVAIN_RESOLUTION = 1.0
RANDOM_SEED = 20261113
EXPECTED_NETWORKS = 116
EXPECTED_TRANSITIONS = 112
EXPECTED_PAIRED_COMPARISONS = 58
KNN_BATCH_SIZE = 1024

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
CAPTURE_DIR = RUN_DIR / "primary_7b_bf16"
PLAN_PATH = PIPELINE_DIR / "R012_PLAN.md"
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


def artifact_record(path: Path) -> dict:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False),
        encoding="utf-8",
    )


def write_manifest(manifest: dict) -> None:
    write_json(MANIFEST_PATH, manifest)


def complete_component(manifest: dict, name: str, started: float, **values) -> None:
    manifest["components"][name] = {
        "status": "successful",
        "completed_at": utc_now(),
        "seconds": time.perf_counter() - started,
        **values,
    }
    write_manifest(manifest)


def visible_token(value: object) -> str:
    if value is None:
        return "<empty>"
    text = str(value)
    if not text:
        return "<empty>"
    return (
        text.replace(" ", "␠")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )


def classify_token(token_id: int, decoded: str, special_ids: set[int]) -> str:
    if token_id in special_ids:
        return "special"
    stripped = decoded.strip()
    if not stripped:
        return "whitespace"
    if stripped.isalpha():
        return "alphabetic"
    if stripped.isnumeric():
        return "numeric"
    if all(not character.isalnum() for character in stripped):
        return "punctuation"
    return "mixed"


def state_label(state_index: int) -> str:
    if state_index == 0:
        return "input_embedding"
    if state_index == STATE_COUNT - 1:
        return "final_norm_after_block_27"
    return f"block_{state_index - 1}_output"


def elbow_candidate(sorted_values: np.ndarray) -> dict:
    values = np.asarray(sorted_values, dtype=np.float64)
    if values.ndim != 1 or values.size < 5:
        raise ValueError("Elbow input must be one-dimensional with at least 5 values.")
    if not np.isfinite(values).all():
        raise ValueError("Elbow input contains non-finite values.")
    if np.any(np.diff(values) > np.finfo(np.float64).eps * 16):
        raise ValueError("Elbow input must be descending.")
    score_range = float(values[0] - values[-1])
    if score_range <= np.finfo(np.float64).eps:
        raise ValueError("Elbow input has no usable score range.")
    x = np.linspace(0.0, 1.0, values.size, dtype=np.float64)
    normalized = (values - values[-1]) / score_range
    deviation = (1.0 - x) - normalized
    elbow_index = int(np.argmax(deviation))
    strength = float(deviation[elbow_index])
    if elbow_index < 1 or elbow_index >= values.size - 1 or strength <= 0.0:
        raise ValueError("Full distribution did not produce a valid interior elbow.")
    gaps = values[:-1] - values[1:]
    positive_gaps = gaps[gaps > 0]
    baseline_gap = float(np.median(positive_gaps)) if positive_gaps.size else 0.0
    score_gap = float(gaps[elbow_index])
    return {
        "cutoff_rank": elbow_index + 1,
        "cutoff_score": float(values[elbow_index]),
        "elbow_strength": strength,
        "score_gap_after": score_gap,
        "gap_ratio": score_gap / baseline_gap if baseline_gap > 0 else None,
    }


def jaccard(left: set, right: set) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def exact_knn(
    normalized_embeddings: torch.Tensor,
    token_ids: np.ndarray,
    k: int,
) -> tuple[np.ndarray, np.ndarray]:
    if token_ids.ndim != 1 or token_ids.size <= k:
        raise ValueError("Selected population must be one-dimensional and exceed k.")
    ids = torch.as_tensor(token_ids, dtype=torch.long, device="cuda")
    with torch.inference_mode():
        selected = normalized_embeddings.index_select(0, ids)
        all_positions: list[torch.Tensor] = []
        all_values: list[torch.Tensor] = []
        for start in range(0, token_ids.size, KNN_BATCH_SIZE):
            stop = min(start + KNN_BATCH_SIZE, token_ids.size)
            similarities = selected[start:stop] @ selected.transpose(0, 1)
            local_rows = torch.arange(stop - start, device="cuda")
            similarities[local_rows, torch.arange(start, stop, device="cuda")] = -torch.inf
            values, positions = torch.topk(
                similarities,
                k=k,
                dim=1,
                largest=True,
                sorted=True,
            )
            all_positions.append(positions.cpu())
            all_values.append(values.cpu())
            del similarities, values, positions
        positions_np = torch.cat(all_positions).numpy().astype(np.int32, copy=False)
        values_np = torch.cat(all_values).numpy().astype(np.float32, copy=False)
    del ids, selected, all_positions, all_values
    return positions_np, values_np


def directed_arrays(
    token_ids: np.ndarray,
    positions: np.ndarray,
    similarities: np.ndarray,
    vocabulary_size: int,
) -> dict[str, np.ndarray]:
    population_size, k = positions.shape
    source = np.repeat(token_ids, k)
    target = token_ids[positions.reshape(-1)]
    scores = similarities.reshape(-1)
    ranks = np.tile(np.arange(1, k + 1, dtype=np.int16), population_size)
    if np.any(source == target):
        raise RuntimeError("Self-edge survived exact kNN exclusion.")
    keys = source.astype(np.int64) * vocabulary_size + target
    reverse = target.astype(np.int64) * vocabulary_size + source
    reciprocal = np.isin(reverse, keys, assume_unique=False)
    return {
        "source": source,
        "target": target,
        "scores": scores,
        "ranks": ranks,
        "reciprocal": reciprocal,
    }


def symmetrize(arrays: dict[str, np.ndarray]) -> pd.DataFrame:
    frame = pd.DataFrame(
        {
            "token_a": np.minimum(arrays["source"], arrays["target"]),
            "token_b": np.maximum(arrays["source"], arrays["target"]),
            "cosine_similarity": arrays["scores"],
        }
    )
    return (
        frame.groupby(["token_a", "token_b"], as_index=False, sort=True)
        .agg(
            max_cosine_similarity=("cosine_similarity", "max"),
            mean_cosine_similarity=("cosine_similarity", "mean"),
            directed_occurrences=("cosine_similarity", "size"),
        )
        .reset_index(drop=True)
    )


def louvain_partition(
    graph: nx.Graph,
    state_index: int,
    side_index: int,
) -> tuple[list[set[int]], dict[int, int]]:
    # The seed depends only on the state/side analysis slot. Identical graphs
    # from different prompts must therefore receive identical partitions.
    seed = RANDOM_SEED + state_index * 2 + side_index
    communities = nx.community.louvain_communities(
        graph,
        weight=None,
        resolution=LOUVAIN_RESOLUTION,
        seed=seed,
    )
    ordered = sorted(
        (set(map(int, community)) for community in communities),
        key=lambda community: (-len(community), min(community)),
    )
    mapping = {
        token_id: community_id
        for community_id, community in enumerate(ordered)
        for token_id in community
    }
    return ordered, mapping


def best_community_matches(
    comparison_type: str,
    side: str,
    source: dict,
    target: dict,
    **identity,
) -> list[dict]:
    pair_counts: Counter = Counter()
    for token_id in source["membership"] & target["membership"]:
        pair_counts[
            (
                source["community_by_token"][token_id],
                target["community_by_token"][token_id],
            )
        ] += 1
    target_sizes = Counter(target["community_by_token"].values())
    source_sizes = Counter(source["community_by_token"].values())
    records = []
    for source_id in sorted(source_sizes):
        candidates = [
            (overlap, target_id)
            for (candidate_source, target_id), overlap in pair_counts.items()
            if candidate_source == source_id
        ]
        if candidates:
            overlap, target_id = max(candidates, key=lambda item: (item[0], -item[1]))
            union = source_sizes[source_id] + target_sizes[target_id] - overlap
            target_value: int | None = int(target_id)
            target_size: int | None = int(target_sizes[target_id])
            overlap_value = int(overlap)
            overlap_jaccard: float | None = overlap / union
        else:
            target_value = None
            target_size = None
            overlap_value = 0
            overlap_jaccard = None
        records.append(
            {
                "comparison_type": comparison_type,
                "side": side,
                **identity,
                "source_community_id": int(source_id),
                "source_community_size": int(source_sizes[source_id]),
                "best_target_community_id": target_value,
                "best_target_community_size": target_size,
                "shared_token_count": overlap_value,
                "source_retained_fraction": overlap_value / source_sizes[source_id],
                "community_jaccard": overlap_jaccard,
            }
        )
    return records


def compare_state_data(source: dict, target: dict) -> dict:
    shared = source["membership"] & target["membership"]
    ordered = sorted(shared)
    source_labels = [source["community_by_token"][token] for token in ordered]
    target_labels = [target["community_by_token"][token] for token in ordered]
    ari = (
        float(adjusted_rand_score(source_labels, target_labels))
        if ordered
        else None
    )
    return {
        "shared_token_count": len(shared),
        "membership_jaccard": jaccard(source["membership"], target["membership"]),
        "source_edge_count": len(source["edges"]),
        "target_edge_count": len(target["edges"]),
        "retained_edge_count": len(source["edges"] & target["edges"]),
        "new_edge_count": len(target["edges"] - source["edges"]),
        "disappeared_edge_count": len(source["edges"] - target["edges"]),
        "edge_jaccard": jaccard(source["edges"], target["edges"]),
        "community_adjusted_rand": ari,
    }


def analyze_network(
    prompt: str,
    prompt_index: int,
    state_index: int,
    side: str,
    side_index: int,
    state_tokens: pd.DataFrame,
    normalized_embeddings: torch.Tensor,
    vocabulary_size: int,
) -> tuple[dict, pd.DataFrame, pd.DataFrame, list[dict], list[dict], dict, dict]:
    state_tokens = state_tokens.sort_values("token_id", kind="stable").reset_index(drop=True)
    token_ids = state_tokens["token_id"].to_numpy(dtype=np.int64, copy=True)
    positions, scores = exact_knn(normalized_embeddings, token_ids, K_NEIGHBORS)
    arrays = directed_arrays(token_ids, positions, scores, vocabulary_size)
    undirected = symmetrize(arrays)
    graph = nx.Graph()
    graph.add_nodes_from(map(int, token_ids))
    graph.add_edges_from(
        (
            int(row.token_a),
            int(row.token_b),
            {"cosine_similarity": float(row.max_cosine_similarity)},
        )
        for row in undirected.itertuples(index=False)
    )
    communities, community_by_token = louvain_partition(
        graph, state_index, side_index
    )
    if set(community_by_token) != set(map(int, token_ids)):
        raise RuntimeError("Community mapping does not cover the network population.")
    components = list(nx.connected_components(graph))
    metric = {
        "prompt": prompt,
        "state_index": state_index,
        "state_label": state_label(state_index),
        "side": side,
        "population_size": int(token_ids.size),
        "directed_edge_count": int(arrays["scores"].size),
        "undirected_edge_count": int(graph.number_of_edges()),
        "mean_knn_cosine": float(np.mean(arrays["scores"])),
        "median_knn_cosine": float(np.median(arrays["scores"])),
        "minimum_knn_cosine": float(np.min(arrays["scores"])),
        "maximum_knn_cosine": float(np.max(arrays["scores"])),
        "reciprocal_edge_fraction": float(np.mean(arrays["reciprocal"])),
        "connected_component_count": len(components),
        "largest_component_fraction": max(map(len, components)) / token_ids.size,
        "average_clustering": float(nx.average_clustering(graph)),
        "community_count": len(communities),
        "community_modularity": float(
            nx.community.modularity(graph, communities, weight=None)
        ),
        "mean_target_cosine": float(state_tokens["cosine_score"].mean()),
        "minimum_target_cosine": float(state_tokens["cosine_score"].min()),
        "maximum_target_cosine": float(state_tokens["cosine_score"].max()),
    }
    sizes = {community_id: len(nodes) for community_id, nodes in enumerate(communities)}
    node_frame = state_tokens.copy()
    node_frame["community_id"] = node_frame["token_id"].map(community_by_token)
    node_frame["community_size"] = node_frame["community_id"].map(sizes)
    node_frame["undirected_degree"] = node_frame["token_id"].map(dict(graph.degree()))

    edge_frame = pd.DataFrame(
        {
            "prompt": prompt,
            "state_index": state_index,
            "state_label": state_label(state_index),
            "side": side,
            "source_token_id": arrays["source"],
            "target_token_id": arrays["target"],
            "neighbor_rank": arrays["ranks"],
            "cosine_similarity": arrays["scores"],
            "reciprocal": arrays["reciprocal"],
        }
    )

    indexed = state_tokens.set_index("token_id", drop=False)
    degrees = dict(graph.degree())
    community_records: list[dict] = []
    compact_communities: list[dict] = []
    for community_id, community in enumerate(communities):
        node_ids = sorted(community)
        representatives = sorted(node_ids, key=lambda item: (-degrees[item], item))[:12]
        extremes = (
            indexed.loc[node_ids]
            .reset_index(drop=True)
            .sort_values(
                ["cosine_score", "token_id"],
                ascending=[side == "negative_tail", True],
                kind="stable",
            )
            .head(12)["token_id"]
            .astype(int)
            .tolist()
        )
        class_counts = {
            str(key): int(value)
            for key, value in indexed.loc[node_ids, "token_class"].value_counts().sort_index().items()
        }
        representative_tokens = [
            visible_token(indexed.loc[token_id, "decoded_token"])
            for token_id in representatives
        ]
        extreme_tokens = [
            visible_token(indexed.loc[token_id, "decoded_token"])
            for token_id in extremes
        ]
        induced = graph.subgraph(node_ids)
        boundary_edges = sum(
            1
            for node_id in node_ids
            for neighbor in graph.neighbors(node_id)
            if community_by_token[int(neighbor)] != community_id
        )
        record = {
            "prompt": prompt,
            "state_index": state_index,
            "state_label": state_label(state_index),
            "side": side,
            "community_id": community_id,
            "community_size": len(node_ids),
            "internal_edge_count": int(induced.number_of_edges()),
            "boundary_edge_count": int(boundary_edges),
            "mean_degree": float(np.mean([degrees[token] for token in node_ids])),
            "mean_target_cosine": float(indexed.loc[node_ids, "cosine_score"].mean()),
            "minimum_target_cosine": float(indexed.loc[node_ids, "cosine_score"].min()),
            "maximum_target_cosine": float(indexed.loc[node_ids, "cosine_score"].max()),
            "representative_token_ids": " ".join(map(str, representatives)),
            "representative_tokens": " | ".join(representative_tokens),
            "most_extreme_token_ids": " ".join(map(str, extremes)),
            "most_extreme_tokens": " | ".join(extreme_tokens),
            "token_class_counts": json.dumps(class_counts, sort_keys=True),
        }
        community_records.append(record)
        compact_communities.append(
            {
                "community_id": community_id,
                "community_size": len(node_ids),
                "internal_edge_count": record["internal_edge_count"],
                "boundary_edge_count": record["boundary_edge_count"],
                "mean_target_cosine": record["mean_target_cosine"],
                "representative_tokens": representative_tokens,
                "most_extreme_tokens": extreme_tokens,
                "token_class_counts": class_counts,
            }
        )

    between = undirected.copy()
    between["community_a"] = between["token_a"].map(community_by_token)
    between["community_b"] = between["token_b"].map(community_by_token)
    between = between.loc[between["community_a"] != between["community_b"]].copy()
    community_edge_records: list[dict] = []
    compact_edges: list[dict] = []
    if not between.empty:
        between[["community_a", "community_b"]] = np.sort(
            between[["community_a", "community_b"]].to_numpy(), axis=1
        )
        grouped = (
            between.groupby(["community_a", "community_b"], as_index=False, sort=True)
            .agg(
                token_edge_count=("max_cosine_similarity", "size"),
                mean_cosine_similarity=("max_cosine_similarity", "mean"),
                maximum_cosine_similarity=("max_cosine_similarity", "max"),
            )
            .reset_index(drop=True)
        )
        for row in grouped.itertuples(index=False):
            record = {
                "prompt": prompt,
                "state_index": state_index,
                "state_label": state_label(state_index),
                "side": side,
                "community_a": int(row.community_a),
                "community_b": int(row.community_b),
                "token_edge_count": int(row.token_edge_count),
                "mean_cosine_similarity": float(row.mean_cosine_similarity),
                "maximum_cosine_similarity": float(row.maximum_cosine_similarity),
            }
            community_edge_records.append(record)
            compact_edges.append(
                {key: value for key, value in record.items() if key not in {"prompt", "state_index", "state_label", "side"}}
            )

    state_data = {
        "membership": set(map(int, token_ids)),
        "edges": set(
            zip(
                undirected["token_a"].astype(int),
                undirected["token_b"].astype(int),
                strict=True,
            )
        ),
        "community_by_token": community_by_token,
    }
    compact = {
        "prompt": prompt,
        "state_index": state_index,
        "state_label": state_label(state_index),
        "side": side,
        "metrics": {
            key: value
            for key, value in metric.items()
            if key not in {"prompt", "state_index", "state_label", "side"}
        },
        "communities": compact_communities,
        "intercommunity_edges": compact_edges,
    }
    del positions, scores, arrays, graph, undirected, between
    return (
        metric,
        node_frame,
        edge_frame,
        community_records,
        community_edge_records,
        state_data,
        compact,
    )


def main() -> None:
    started_at = utc_now()
    started_perf = time.perf_counter()
    manifest = load_json(MANIFEST_PATH)
    if manifest.get("run_id") != RUN_ID:
        raise RuntimeError("R012 manifest identity mismatch.")
    if manifest.get("status") not in {"running", "failed"}:
        raise RuntimeError("R012 must be running or failed before analysis execution.")
    manifest["status"] = "running"
    manifest["completed_at"] = None
    manifest["failure_details"] = None
    manifest.setdefault("analysis_attempts", []).append(
        {"started_at": started_at, "status": "running"}
    )
    write_manifest(manifest)
    current_component = "projection_and_cutoffs"

    try:
        if not PLAN_PATH.is_file() or not SNAPSHOT_DIR.is_dir():
            raise FileNotFoundError("R012 plan or cached Qwen snapshot is missing.")
        if manifest["models"]["primary"]["id"] != MODEL_ID:
            raise RuntimeError("Manifest primary model does not match the locked backend.")
        hash_manifest = load_json(CAPTURE_DIR / "artifact_hashes.json")
        for name in (
            "baseline_hidden_states.safetensors",
            "variation_hidden_states.safetensors",
            "prompt_records.json",
            "run_metadata.json",
            "pair_validation.json",
        ):
            path = CAPTURE_DIR / name
            expected = hash_manifest[name]
            if path.stat().st_size != expected["bytes"] or sha256_file(path) != expected["sha256"]:
                raise RuntimeError(f"Capture artifact failed validation: {name}")
        validation = load_json(CAPTURE_DIR / "pair_validation.json")
        if validation.get("status") != "successful":
            raise RuntimeError("Primary capture validation is not successful.")

        model_index_path = SNAPSHOT_DIR / "model.safetensors.index.json"
        model_index = load_json(model_index_path)
        shard_name = model_index["weight_map"].get(EMBEDDING_KEY)
        if not shard_name:
            raise KeyError(f"Missing embedding tensor: {EMBEDDING_KEY}")
        tokenizer = AutoTokenizer.from_pretrained(SNAPSHOT_DIR, local_files_only=True)
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
        capture_token_id = int(prompt_records["baseline"]["capture_token_id"])
        if capture_token_id != int(prompt_records["variation"]["capture_token_id"]):
            raise RuntimeError("Paired captures use different target-position tokens.")

        trajectories = []
        for prompt in PROMPTS:
            with safe_open(
                str(CAPTURE_DIR / f"{prompt}_hidden_states.safetensors"),
                framework="pt",
                device="cpu",
            ) as handle:
                tensor = handle.get_tensor("hidden_states").float()
            if tuple(tensor.shape) != (STATE_COUNT, HIDDEN_WIDTH):
                raise RuntimeError(f"Unexpected {prompt} trajectory shape: {tuple(tensor.shape)}")
            trajectories.append(tensor)
        hidden_states = torch.stack(trajectories)
        if not torch.isfinite(hidden_states).all():
            raise RuntimeError("Hidden states contain non-finite values.")

        shard_path = SNAPSHOT_DIR / shard_name
        with safe_open(str(shard_path), framework="pt", device="cpu") as handle:
            embedding_matrix = handle.get_tensor(EMBEDDING_KEY)
        full_embedding_rows = int(embedding_matrix.shape[0])
        if embedding_matrix.ndim != 2 or embedding_matrix.shape[1] != HIDDEN_WIDTH:
            raise RuntimeError(
                f"Unexpected embedding shape: {tuple(embedding_matrix.shape)}"
            )
        if full_embedding_rows < vocabulary_size:
            raise RuntimeError(
                "Embedding table has fewer rows than the tokenizer's usable ID range."
            )
        # Qwen pads the model embedding table beyond the tokenizer's usable IDs.
        # Those unaddressable rows are not vocabulary tokens and are excluded.
        embedding_matrix = embedding_matrix[:vocabulary_size]
        if not torch.cuda.is_available():
            raise RuntimeError("R012 exact topology execution requires CUDA.")
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
                "prompts": "baseline,variation",
                "state_count": str(STATE_COUNT),
                "vocabulary_size": str(vocabulary_size),
                "excluded_from_cutoff_token_id": str(capture_token_id),
            },
        )
        del normalized_states, hidden_states, trajectories, embedding_matrix
        gc.collect()

        eligible_ids = np.arange(vocabulary_size, dtype=np.int64)
        eligible_ids = eligible_ids[eligible_ids != capture_token_id]
        scores = scores_tensor.numpy()
        cutoff_records: list[dict] = []
        membership_frames: list[pd.DataFrame] = []
        membership_by_key: dict[tuple[str, int, str], pd.DataFrame] = {}
        for prompt_index, prompt in enumerate(PROMPTS):
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
                    raise RuntimeError(f"Cutoff populations overlap at {prompt} state {state_index}.")
                cutoff_records.append(
                    {
                        "prompt": prompt,
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
                    rank_order = np.arange(1, len(token_ids) + 1, dtype=np.int32)
                    frame = pd.DataFrame(
                        {
                            "prompt": prompt,
                            "state_index": state_index,
                            "state_label": state_label(state_index),
                            "side": side,
                            "token_id": token_ids,
                            "raw_token": [raw_tokens[token] for token in token_ids],
                            "decoded_token": [decoded_tokens[token] for token in token_ids],
                            "display_token": [visible_token(decoded_tokens[token]) for token in token_ids],
                            "token_class": [token_classes[token] for token in token_ids],
                            "cosine_score": state_scores[token_ids],
                            "rank_from_extreme": rank_order,
                        }
                    )
                    membership_by_key[(prompt, state_index, side)] = frame
                    membership_frames.append(frame)

        cutoffs = pd.DataFrame(cutoff_records).sort_values(["prompt", "state_index"])
        if len(cutoffs) != len(PROMPTS) * STATE_COUNT:
            raise RuntimeError("Cutoff table has incomplete prompt-state coverage.")
        cutoffs_path = RUN_DIR / "cutoffs.csv"
        cutoffs.to_csv(cutoffs_path, index=False)
        tails = pd.concat(membership_frames, ignore_index=True)
        tails_path = RUN_DIR / "tail_tokens.csv.gz"
        tails.to_csv(tails_path, index=False, compression="gzip")
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
            f"R012 projection and cutoffs complete: {len(tails):,} selected memberships.",
            flush=True,
        )

        current_component = "split_networks_and_communities"
        component_started = time.perf_counter()
        network_records: list[dict] = []
        community_records: list[dict] = []
        community_edge_records: list[dict] = []
        compact_networks: list[dict] = []
        transition_records: list[dict] = []
        paired_records: list[dict] = []
        community_match_records: list[dict] = []
        previous: dict[tuple[str, str], dict] = {}
        node_rows = 0
        edge_rows = 0
        nodes_path = RUN_DIR / "nodes.csv.gz"
        edges_path = RUN_DIR / "edges.csv.gz"
        with gzip.open(nodes_path, "wt", encoding="utf-8", newline="") as node_handle, gzip.open(
            edges_path, "wt", encoding="utf-8", newline=""
        ) as edge_handle:
            for state_index in range(STATE_COUNT):
                current_state: dict[tuple[str, str], dict] = {}
                for prompt_index, prompt in enumerate(PROMPTS):
                    for side_index, side in enumerate(SIDES):
                        network_started = time.perf_counter()
                        state_tokens = membership_by_key[(prompt, state_index, side)]
                        (
                            metric,
                            node_frame,
                            edge_frame,
                            communities,
                            community_edges,
                            state_data,
                            compact,
                        ) = analyze_network(
                            prompt,
                            prompt_index,
                            state_index,
                            side,
                            side_index,
                            state_tokens,
                            normalized_embeddings,
                            vocabulary_size,
                        )
                        node_frame.to_csv(node_handle, index=False, header=node_rows == 0)
                        edge_frame.to_csv(edge_handle, index=False, header=edge_rows == 0)
                        node_rows += len(node_frame)
                        edge_rows += len(edge_frame)
                        network_records.append(metric)
                        community_records.extend(communities)
                        community_edge_records.extend(community_edges)
                        compact_networks.append(compact)
                        current_state[(prompt, side)] = state_data

                        prior = previous.get((prompt, side))
                        if prior is not None:
                            comparison = compare_state_data(prior, state_data)
                            transition_records.append(
                                {
                                    "prompt": prompt,
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
                                    prompt=prompt,
                                    source_prompt=prompt,
                                    target_prompt=prompt,
                                    source_state_index=state_index - 1,
                                    target_state_index=state_index,
                                )
                            )
                        previous[(prompt, side)] = state_data
                        print(
                            f"R012 network {len(network_records):03d}/{EXPECTED_NETWORKS}: "
                            f"{prompt} state {state_index:02d} {side}, "
                            f"{len(node_frame):,} nodes, {len(communities)} communities, "
                            f"{time.perf_counter() - network_started:.1f}s.",
                            flush=True,
                        )

                for side in SIDES:
                    baseline = current_state[("baseline", side)]
                    variation = current_state[("variation", side)]
                    comparison = compare_state_data(baseline, variation)
                    paired_records.append(
                        {
                            "state_index": state_index,
                            "state_label": state_label(state_index),
                            "side": side,
                            **comparison,
                        }
                    )
                    community_match_records.extend(
                        best_community_matches(
                            "paired_prompt",
                            side,
                            baseline,
                            variation,
                            prompt=None,
                            source_prompt="baseline",
                            target_prompt="variation",
                            source_state_index=state_index,
                            target_state_index=state_index,
                        )
                    )

        network_index = pd.DataFrame(network_records).sort_values(
            ["state_index", "prompt", "side"], kind="stable"
        )
        community_nodes = pd.DataFrame(community_records).sort_values(
            ["state_index", "prompt", "side", "community_id"], kind="stable"
        )
        community_edges = pd.DataFrame(community_edge_records).sort_values(
            ["state_index", "prompt", "side", "community_a", "community_b"],
            kind="stable",
        )
        transitions = pd.DataFrame(transition_records).sort_values(
            ["prompt", "side", "current_state_index"], kind="stable"
        )
        paired = pd.DataFrame(paired_records).sort_values(
            ["state_index", "side"], kind="stable"
        )
        community_matches = pd.DataFrame(community_match_records)
        network_index.to_csv(RUN_DIR / "network_index.csv", index=False)
        community_nodes.to_csv(RUN_DIR / "community_nodes.csv", index=False)
        community_edges.to_csv(RUN_DIR / "community_edges.csv", index=False)
        transitions.to_csv(RUN_DIR / "state_transitions.csv", index=False)
        paired.to_csv(RUN_DIR / "paired_state_comparisons.csv", index=False)
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
            raise RuntimeError(f"Expected {EXPECTED_TRANSITIONS} transitions, found {len(transitions)}.")
        complete_component(
            manifest,
            current_component,
            component_started,
            transition_rows=len(transitions),
            minimum_membership_jaccard=float(transitions["membership_jaccard"].min()),
            minimum_edge_jaccard=float(transitions["edge_jaccard"].min()),
        )

        current_component = "paired_prompt_comparisons"
        component_started = time.perf_counter()
        if len(paired) != EXPECTED_PAIRED_COMPARISONS:
            raise RuntimeError(
                f"Expected {EXPECTED_PAIRED_COMPARISONS} paired comparisons, found {len(paired)}."
            )
        complete_component(
            manifest,
            current_component,
            component_started,
            paired_comparison_rows=len(paired),
            minimum_membership_jaccard=float(paired["membership_jaccard"].min()),
            minimum_edge_jaccard=float(paired["edge_jaccard"].min()),
        )

        current_component = "chatgpt_exports"
        component_started = time.perf_counter()
        compact_document = {
            "schema_version": 1,
            "run_id": RUN_ID,
            "model": {"id": MODEL_ID, "revision": MODEL_REVISION},
            "prompt_records": {
                prompt: {
                    "raw_prompt": prompt_records[prompt]["raw_prompt"],
                    "capture_index": prompt_records[prompt]["capture_index"],
                    "capture_token_id": prompt_records[prompt]["capture_token_id"],
                }
                for prompt in PROMPTS
            },
            "network_count": len(compact_networks),
            "state_count": STATE_COUNT,
            "sides": list(SIDES),
            "stable_join_key": "token_id",
            "community_identity": "community_id is local to one prompt, state and side",
            "interpretation_boundary": (
                "Positive and negative denote target-state cosine alignment and "
                "anti-alignment in the fixed input-embedding basis. Communities are "
                "measured graph partitions, not established semantic topics, GRD roles "
                "or SDA-3 categories."
            ),
            "within_prompt_transitions": transitions.to_dict(orient="records"),
            "paired_prompt_comparisons": paired.to_dict(orient="records"),
            "networks": compact_networks,
        }
        json_path = RUN_DIR / "chatgpt_community_networks.json"
        write_json(json_path, compact_document)

        compact_by_key = {
            (item["state_index"], item["prompt"], item["side"]): item
            for item in compact_networks
        }
        paired_by_key = {
            (int(row.state_index), str(row.side)): row
            for row in paired.itertuples(index=False)
        }
        packet_lines = [
            "# R012 ChatGPT layer packets",
            "",
            "This file describes all 116 measured prompt/state/side networks. "
            "It contains no semantic topic labels.",
            "",
            "Positive and negative mean cosine alignment and anti-alignment with "
            "the evolving whole-prompt final-position state. Negative does not by "
            "itself establish suppression, contradiction or exclusion.",
            "",
        ]
        for state_index in range(STATE_COUNT):
            packet_lines.extend(
                [f"## State {state_index:02d} — {state_label(state_index)}", ""]
            )
            for side in SIDES:
                comparison = paired_by_key[(state_index, side)]
                packet_lines.append(
                    f"Paired {side}: membership Jaccard "
                    f"{comparison.membership_jaccard:.6f}; edge Jaccard "
                    f"{comparison.edge_jaccard:.6f}; shared tokens "
                    f"{comparison.shared_token_count}."
                )
            packet_lines.append("")
            for prompt in PROMPTS:
                packet_lines.extend(
                    [
                        f"### {prompt}",
                        "",
                        f"Prompt: `{prompt_records[prompt]['raw_prompt']}`",
                        "",
                    ]
                )
                for side in SIDES:
                    network = compact_by_key[(state_index, prompt, side)]
                    metrics = network["metrics"]
                    packet_lines.extend(
                        [
                            f"#### {side}",
                            "",
                            f"- Nodes: {metrics['population_size']}",
                            f"- Directed 10-NN edges: {metrics['directed_edge_count']}",
                            f"- Undirected edges: {metrics['undirected_edge_count']}",
                            f"- Communities: {metrics['community_count']}",
                            f"- Modularity: {metrics['community_modularity']:.6f}",
                            "",
                            "All communities:",
                            "",
                        ]
                    )
                    for community in network["communities"]:
                        representatives = ", ".join(community["representative_tokens"][:10])
                        extremes = ", ".join(community["most_extreme_tokens"][:6])
                        packet_lines.append(
                            f"- C{community['community_id']} (n={community['community_size']}): "
                            f"representatives [{representatives}]; target-extreme "
                            f"[{extremes}]; classes {community['token_class_counts']}"
                        )
                    packet_lines.extend(["", "Strongest intercommunity connections:", ""])
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
                                f"- C{edge['community_a']} to C{edge['community_b']}: "
                                f"{edge['token_edge_count']} token edges; mean cosine "
                                f"{edge['mean_cosine_similarity']:.6f}"
                            )
                    else:
                        packet_lines.append("- None")
                    packet_lines.append("")
        packets_path = RUN_DIR / "chatgpt_layer_packets.md"
        packets_path.write_text("\n".join(packet_lines), encoding="utf-8")
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
            raise RuntimeError(f"Expected {EXPECTED_NETWORKS} networks, found {len(network_index)}.")
        if network_index.duplicated(["prompt", "state_index", "side"]).any():
            raise RuntimeError("Duplicate network identity found.")
        expected_node_rows = int(network_index["population_size"].sum())
        expected_edge_rows = int(network_index["directed_edge_count"].sum())
        if node_rows != expected_node_rows or edge_rows != expected_edge_rows:
            raise RuntimeError("Streamed node or edge rows do not reconcile with network index.")
        if not (network_index["directed_edge_count"] == network_index["population_size"] * K_NEIGHBORS).all():
            raise RuntimeError("One or more networks do not contain exact 10-NN coverage.")
        community_size_totals = community_nodes.groupby(
            ["prompt", "state_index", "side"]
        )["community_size"].sum()
        population_totals = network_index.set_index(
            ["prompt", "state_index", "side"]
        )["population_size"]
        if not community_size_totals.equals(population_totals.sort_index()):
            raise RuntimeError("Community sizes do not reconcile with network populations.")
        state_zero = paired.loc[paired["state_index"] == 0]
        if not (
            np.allclose(state_zero["membership_jaccard"], 1.0)
            and np.allclose(state_zero["edge_jaccard"], 1.0)
            and np.allclose(state_zero["community_adjusted_rand"], 1.0)
        ):
            raise RuntimeError("Identical State 00 inputs did not produce identical topology.")
        if compact_document["network_count"] != EXPECTED_NETWORKS:
            raise RuntimeError("ChatGPT JSON network count is incomplete.")

        verification_path = RUN_DIR / "R012_COMPLETENESS_VERIFICATION.md"
        verification_path.write_text(
            "\n".join(
                [
                    "# R012 completeness verification",
                    "",
                    "- Status: PASS",
                    f"- Networks: {len(network_index)} / {EXPECTED_NETWORKS}",
                    f"- Within-prompt adjacent transitions: {len(transitions)} / {EXPECTED_TRANSITIONS}",
                    f"- Paired-prompt same-state comparisons: {len(paired)} / {EXPECTED_PAIRED_COMPARISONS}",
                    f"- Selected token memberships: {node_rows:,}",
                    f"- Directed exact 10-NN edges: {edge_rows:,}",
                    f"- State-local communities: {len(community_nodes):,}",
                    "- Every network identity is unique.",
                    "- Every selected node belongs to exactly one community.",
                    "- Every network has exactly 10 directed neighbours per node.",
                    "- State 00 topology is identical across the paired prompts.",
                    "- ChatGPT JSON contains all 116 networks.",
                    "- Semantic labels and GRD/SDA roles were not added.",
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
            state_zero_pair_identity_verified=True,
        )

        current_component = "run_report"
        component_started = time.perf_counter()
        cutoff_summary = cutoffs[["positive_head_count", "negative_tail_count"]]
        min_pair_row = paired.loc[paired["membership_jaccard"].idxmin()]
        min_edge_pair_row = paired.loc[paired["edge_jaccard"].idxmin()]
        min_transition_row = transitions.loc[transitions["membership_jaccard"].idxmin()]
        report_path = RUN_DIR / "R012_MEASUREMENT_REPORT.md"
        report_path.write_text(
            "\n".join(
                [
                    "# R012 whole-prompt semantic-topology measurement report",
                    "",
                    "## Outcome",
                    "",
                    "R012 completed the intended generalised measured pipeline. The validated Qwen hidden-state trajectories were projected into the fixed input-embedding vocabulary, divided by full-curve elbows, converted into 116 exact split networks, partitioned into state-local communities, compared through depth and compared across the paired prompts.",
                    "",
                    "The model was not re-run and no response token was generated. No semantic topic labels, parent nodes, GRD roles or SDA-3 roles were inferred.",
                    "",
                    "## Coverage",
                    "",
                    f"- Networks: {len(network_index)}",
                    f"- Selected token memberships: {node_rows:,}",
                    f"- Directed 10-NN edges: {edge_rows:,}",
                    f"- State-local communities: {len(community_nodes):,}",
                    f"- Adjacent-state comparisons: {len(transitions)}",
                    f"- Same-state paired-prompt comparisons: {len(paired)}",
                    "",
                    "## Measured findings",
                    "",
                    f"- Positive populations ranged from {int(cutoff_summary['positive_head_count'].min()):,} to {int(cutoff_summary['positive_head_count'].max()):,} tokens (median {cutoff_summary['positive_head_count'].median():,.0f}).",
                    f"- Negative populations ranged from {int(cutoff_summary['negative_tail_count'].min()):,} to {int(cutoff_summary['negative_tail_count'].max()):,} tokens (median {cutoff_summary['negative_tail_count'].median():,.0f}).",
                    f"- The smallest paired-prompt membership Jaccard was {min_pair_row.membership_jaccard:.6f} at State {int(min_pair_row.state_index):02d} on {min_pair_row.side}.",
                    f"- The smallest paired-prompt edge Jaccard was {min_edge_pair_row.edge_jaccard:.6f} at State {int(min_edge_pair_row.state_index):02d} on {min_edge_pair_row.side}.",
                    f"- The largest adjacent membership reorganisation (lowest Jaccard {min_transition_row.membership_jaccard:.6f}) occurred for {min_transition_row.prompt} {min_transition_row.side}, State {int(min_transition_row.previous_state_index):02d} → {int(min_transition_row.current_state_index):02d}.",
                    f"- Community counts ranged from {int(network_index['community_count'].min())} to {int(network_index['community_count'].max())} per network.",
                    "- State 00 was structurally identical across prompts, as required by the identical capture-position input embedding; later differences therefore arise after contextual processing.",
                    "",
                    "These are measured structural results. Their semantic meaning is intentionally deferred to downstream ChatGPT analysis using the JSON, Markdown and CSV exports.",
                    "",
                    "## Method boundary",
                    "",
                    "The Qwen model is the first validated backend for the minimal capture contract. Vocabulary projection, cutoff calculation, networks, communities and comparisons are model-independent once trajectories, input embeddings and vocabulary are supplied.",
                ]
            ),
            encoding="utf-8",
        )
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
            "paired_state_comparisons.csv",
            "community_transition_evidence.csv",
            "chatgpt_community_networks.json",
            "chatgpt_layer_packets.md",
            "R012_COMPLETENESS_VERIFICATION.md",
            "R012_MEASUREMENT_REPORT.md",
        ]
        manifest["artifacts"].update(
            {name: artifact_record(RUN_DIR / name) for name in output_names}
        )
        manifest["pipeline"] = {
            "script": str(Path(__file__).resolve().relative_to(PROJECT_DIR)).replace("\\", "/"),
            "script_sha256": sha256_file(Path(__file__).resolve()),
            "plan": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
            "plan_sha256": sha256_file(PLAN_PATH),
            "model_backend": "direct Qwen Transformers capture artifacts",
            "downstream_analysis": "model-independent",
        }
        manifest["results"] = {
            "network_count": len(network_index),
            "selected_membership_rows": node_rows,
            "directed_edge_rows": edge_rows,
            "community_count": len(community_nodes),
            "adjacent_transition_rows": len(transitions),
            "paired_comparison_rows": len(paired),
            "minimum_paired_membership_jaccard": float(paired["membership_jaccard"].min()),
            "minimum_paired_edge_jaccard": float(paired["edge_jaccard"].min()),
        }
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now()
        manifest["failure_details"] = None
        manifest["operational_notes"]["semantic_topology_pipeline_status"] = "successful"
        manifest["operational_notes"]["model_forward_reexecuted"] = False
        manifest["analysis_attempts"][-1].update(
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
                str(path.relative_to(RUN_DIR)).replace("\\", "/"): artifact_record(path)
                for path in sorted(RUN_DIR.rglob("*"))
                if path.is_file() and path.name != "artifact_index.json"
            },
        }
        write_json(RUN_DIR / "artifact_index.json", artifact_index)
        print(
            f"R012 complete: {len(network_index)} networks, {len(community_nodes):,} "
            f"communities, {time.perf_counter() - started_perf:.1f}s.",
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
        manifest.setdefault("components", {}).setdefault(current_component, {})
        manifest["components"][current_component].update(
            {
                "status": "failed",
                "failed_at": manifest["completed_at"],
                "error_type": type(error).__name__,
                "message": str(error),
            }
        )
        if manifest.get("analysis_attempts"):
            manifest["analysis_attempts"][-1].update(
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
