"""Measure and validate R017 OLMo 3 semantic topology for one bare-concept prompt."""

from __future__ import annotations

import argparse
import gc
import gzip
import hashlib
import json
import shutil
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import networkx as nx
import numpy as np
import pandas as pd
import psutil
import torch
import torch.nn.functional as F
from accelerate import infer_auto_device_map, init_empty_weights
from safetensors import safe_open
from safetensors.torch import save_file
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

import r012_semantic_topology as topology


RUN_ID = "R017_olmo3-choke-point-barrier-spear-semantic-map"
MODEL_ID = "allenai/Olmo-3-1125-32B"
MODEL_REVISION = "c2b61dae89a1ad10e4ad5653d0e46b590902607b"
PROMPT = "choke point\ncollapsible barrier\nspear\n"
EXPECTED_LAYERS = 64
STATE_COUNT = EXPECTED_LAYERS + 1
HIDDEN_WIDTH = 5_120
SIDES = ("positive_head", "negative_tail")
K_NEIGHBORS = 10
EXPECTED_NETWORKS = STATE_COUNT * len(SIDES)
EXPECTED_TRANSITIONS = (STATE_COUNT - 1) * len(SIDES)
GPU_LIMIT = "18GiB"
CPU_LIMIT = "28GiB"
MAX_MEMORY = {0: GPU_LIMIT, "cpu": CPU_LIMIT}
EMBEDDING_KEY = "model.embed_tokens.weight"

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
PLAN_PATH = PIPELINE_DIR / "R017_PLAN.md"
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
MANIFEST_PATH = RUN_DIR / "manifest.json"
CAPTURE_PATH = RUN_DIR / "anchor_hidden_states.safetensors"
PROMPT_RECORD_PATH = RUN_DIR / "prompt_record.json"
DEVICE_MAP_PATH = RUN_DIR / "device_map.json"
SCORES_PATH = RUN_DIR / "vocabulary_scores.safetensors"
MEASURED_REPORT_PATH = RUN_DIR / "R017_MEASURED_REPORT.md"
SEMANTIC_REPORT_PATH = RUN_DIR / "R017_SEMANTIC_MAP_REPORT.html"
VERIFICATION_PATH = RUN_DIR / "R017_COMPLETENESS_VERIFICATION.md"
SNAPSHOT_DIR = (
    Path(r"D:\AI\cache\huggingface\hub\models--allenai--Olmo-3-1125-32B")
    / "snapshots"
    / MODEL_REVISION
)
OFFLOAD_DIR = Path(r"D:\AI\cache\offload\R017_olmo3-32b")

REQUIRED_COMPONENTS = (
    "plan_lock",
    "environment_preflight",
    "model_capture",
    "projection_and_cutoffs",
    "networks_and_communities",
    "adjacent_transitions",
    "measured_exports",
    "completeness_validation",
    "semantic_interpretation",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def memory_snapshot() -> dict[str, object]:
    virtual = psutil.virtual_memory()
    process = psutil.Process()
    snapshot: dict[str, object] = {
        "physical_ram_available_bytes": int(virtual.available),
        "process_rss_bytes": int(process.memory_info().rss),
        "cache_drive_free_bytes": int(shutil.disk_usage(SNAPSHOT_DIR.anchor).free),
    }
    if torch.cuda.is_available():
        free_bytes, total_bytes = torch.cuda.mem_get_info()
        snapshot.update(
            {
                "gpu_name": torch.cuda.get_device_name(0),
                "gpu_total_bytes": int(total_bytes),
                "gpu_free_bytes": int(free_bytes),
                "gpu_allocated_bytes": int(torch.cuda.memory_allocated()),
                "gpu_reserved_bytes": int(torch.cuda.memory_reserved()),
            }
        )
    return snapshot


def state_label(index: int) -> str:
    if index == 0:
        return "input_embedding"
    if index == STATE_COUNT - 1:
        return "final_norm_after_block_63"
    return f"block_{index - 1}_output"


def artifact(path: Path, tracked_by_git: bool = True) -> dict[str, object]:
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "tracked_by_git": tracked_by_git,
    }


def initialize_manifest() -> dict[str, Any]:
    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"Missing locked plan: {PLAN_PATH}")
    if not SNAPSHOT_DIR.is_dir():
        raise FileNotFoundError(f"Missing cached model snapshot: {SNAPSHOT_DIR}")
    if not torch.cuda.is_available():
        raise RuntimeError("R017 requires the RTX 4090 CUDA device.")
    if MANIFEST_PATH.exists():
        previous = load_json(MANIFEST_PATH)
        if previous.get("status") == "successful":
            raise RuntimeError("R017 is already successful; refusing to overwrite it.")
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    components = {name: {"status": "pending"} for name in REQUIRED_COMPONENTS}
    components["plan_lock"] = {
        "status": "successful",
        "completed_at": started,
        "sha256": sha256_file(PLAN_PATH),
    }
    components["environment_preflight"] = {
        "status": "successful",
        "completed_at": started,
        "python": sys.version,
        "torch": torch.__version__,
        "cuda": torch.version.cuda,
        "memory_before": memory_snapshot(),
    }
    manifest: dict[str, Any] = {
        "schema_version": 1,
        "run_id": RUN_ID,
        "status": "running",
        "started_at": started,
        "completed_at": None,
        "failure_details": None,
        "objective": (
            "Measure the layerwise semantic topology formed by choke point, "
            "collapsible barrier and spear, then report its semantic map."
        ),
        "model": {
            "id": MODEL_ID,
            "revision": MODEL_REVISION,
            "precision": "bfloat16",
            "quantized": False,
        },
        "prompt": {
            "text": PROMPT,
            "capture_position": "final newline anchor",
            "chat_template_used": False,
            "generation_executed": False,
        },
        "expected": {
            "states": STATE_COUNT,
            "networks": EXPECTED_NETWORKS,
            "adjacent_transitions": EXPECTED_TRANSITIONS,
        },
        "required_components": list(REQUIRED_COMPONENTS),
        "components": components,
        "artifacts": {},
        "interpretation_boundary": (
            "Measurements end at state-local graph communities and transitions. "
            "Semantic parents and relations are post-measurement interpretations."
        ),
    }
    write_json(MANIFEST_PATH, manifest)
    return manifest


def update_component(manifest: dict[str, Any], name: str, started: float, **details: object) -> None:
    manifest["components"][name] = {
        "status": "successful",
        "completed_at": utc_now(),
        "seconds": time.perf_counter() - started,
        **details,
    }
    write_json(MANIFEST_PATH, manifest)


def fail_run(component: str, error: BaseException) -> None:
    if not MANIFEST_PATH.exists():
        return
    manifest = load_json(MANIFEST_PATH)
    manifest["status"] = "failed"
    manifest["completed_at"] = utc_now()
    manifest["failure_details"] = {
        "component": component,
        "error_type": type(error).__name__,
        "message": str(error),
        "traceback": traceback.format_exc(),
        "memory_at_failure": memory_snapshot(),
    }
    manifest["components"][component] = {
        "status": "failed",
        "completed_at": utc_now(),
        "error_type": type(error).__name__,
        "message": str(error),
    }
    write_json(MANIFEST_PATH, manifest)


def configure_topology_helpers() -> None:
    topology.STATE_COUNT = STATE_COUNT
    topology.HIDDEN_WIDTH = HIDDEN_WIDTH
    topology.K_NEIGHBORS = K_NEIGHBORS
    topology.KNN_BATCH_SIZE = 512
    topology.RANDOM_SEED = 20261115
    topology.state_label = state_label


def capture_states(manifest: dict[str, Any]) -> None:
    started = time.perf_counter()
    config = AutoConfig.from_pretrained(SNAPSHOT_DIR, local_files_only=True)
    if config.num_hidden_layers != EXPECTED_LAYERS or config.hidden_size != HIDDEN_WIDTH:
        raise RuntimeError(
            f"Unexpected model shape: {config.num_hidden_layers} layers, "
            f"width {config.hidden_size}."
        )
    with init_empty_weights():
        empty_model = AutoModelForCausalLM.from_config(config, dtype=torch.bfloat16)
    no_split = list(getattr(empty_model, "_no_split_modules", None) or ["Olmo3DecoderLayer"])
    device_map = infer_auto_device_map(
        empty_model,
        max_memory=MAX_MEMORY,
        no_split_module_classes=no_split,
        dtype=torch.bfloat16,
        offload_buffers=True,
        fallback_allocation=True,
    )
    del empty_model
    gc.collect()
    if "disk" not in {str(value) for value in device_map.values()}:
        raise RuntimeError("Locked placement unexpectedly contains no disk-backed modules.")
    write_json(
        DEVICE_MAP_PATH,
        {
            "model": MODEL_ID,
            "revision": MODEL_REVISION,
            "max_memory": MAX_MEMORY,
            "device_map": {str(key): str(value) for key, value in device_map.items()},
        },
    )

    OFFLOAD_DIR.mkdir(parents=True, exist_ok=True)
    model = AutoModelForCausalLM.from_pretrained(
        SNAPSHOT_DIR,
        revision=MODEL_REVISION,
        dtype=torch.bfloat16,
        device_map=device_map,
        max_memory=MAX_MEMORY,
        offload_folder=OFFLOAD_DIR,
        offload_state_dict=True,
        offload_buffers=True,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(SNAPSHOT_DIR, local_files_only=True)
    anchor_ids = tokenizer.encode("\n", add_special_tokens=False)
    if len(anchor_ids) != 1:
        raise RuntimeError(f"Newline anchor is not one token: {anchor_ids}")
    encoded = tokenizer(
        PROMPT,
        return_tensors="pt",
        add_special_tokens=False,
        return_token_type_ids=False,
    )
    if int(encoded["input_ids"][0, -1]) != anchor_ids[0]:
        raise RuntimeError("Final prompt token is not the newline anchor.")
    prompt_record = {
        "raw_prompt": PROMPT,
        "input_ids": encoded["input_ids"][0].tolist(),
        "tokens": tokenizer.convert_ids_to_tokens(encoded["input_ids"][0].tolist()),
        "capture_index": int(encoded["input_ids"].shape[1] - 1),
        "capture_token_id": int(anchor_ids[0]),
        "chat_template_used": False,
        "special_tokens_added": False,
        "response_generation_executed": False,
    }
    write_json(PROMPT_RECORD_PATH, prompt_record)
    encoded = {name: tensor.to("cuda:0") for name, tensor in encoded.items()}
    torch.cuda.reset_peak_memory_stats()
    with torch.inference_mode():
        output = model(
            **encoded,
            output_hidden_states=True,
            use_cache=False,
            return_dict=True,
        )
    torch.cuda.synchronize()
    states = output.hidden_states
    if states is None or len(states) != STATE_COUNT:
        raise RuntimeError(f"Expected {STATE_COUNT} hidden states; found {0 if states is None else len(states)}.")
    anchors = torch.stack(
        [state[0, -1].detach().to(device="cpu", dtype=torch.bfloat16) for state in states]
    ).contiguous()
    if tuple(anchors.shape) != (STATE_COUNT, HIDDEN_WIDTH):
        raise RuntimeError(f"Unexpected capture shape: {tuple(anchors.shape)}")
    if not torch.isfinite(anchors.float()).all():
        raise RuntimeError("Captured anchor states contain non-finite values.")
    save_file(
        {"anchor_hidden_states": anchors},
        str(CAPTURE_PATH),
        metadata={
            "model_id": MODEL_ID,
            "revision": MODEL_REVISION,
            "prompt": PROMPT,
            "anchor_token_id": str(anchor_ids[0]),
        },
    )
    details = {
        "input_tokens": len(prompt_record["input_ids"]),
        "anchor_token_id": anchor_ids[0],
        "capture_shape": list(anchors.shape),
        "peak_gpu_allocated_bytes": int(torch.cuda.max_memory_allocated()),
        "memory_after_forward": memory_snapshot(),
        "device_map_sha256": sha256_file(DEVICE_MAP_PATH),
        "capture_sha256": sha256_file(CAPTURE_PATH),
    }
    del output, states, anchors, encoded, model
    gc.collect()
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    update_component(manifest, "model_capture", started, **details)


def project_and_select(manifest: dict[str, Any]) -> tuple[torch.Tensor, dict[tuple[int, str], pd.DataFrame], AutoTokenizer]:
    started = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(SNAPSHOT_DIR, local_files_only=True)
    vocabulary_size = len(tokenizer)
    special_ids = set(map(int, tokenizer.all_special_ids))
    raw_tokens = tokenizer.convert_ids_to_tokens(list(range(vocabulary_size)))
    decoded_tokens = [
        tokenizer.decode([token_id], skip_special_tokens=False, clean_up_tokenization_spaces=False)
        for token_id in range(vocabulary_size)
    ]
    token_classes = [
        topology.classify_token(token_id, decoded_tokens[token_id], special_ids)
        for token_id in range(vocabulary_size)
    ]
    prompt_record = load_json(PROMPT_RECORD_PATH)
    capture_token_id = int(prompt_record["capture_token_id"])

    index = load_json(SNAPSHOT_DIR / "model.safetensors.index.json")
    shard_name = index["weight_map"].get(EMBEDDING_KEY)
    if not shard_name:
        raise KeyError(f"Missing embedding tensor: {EMBEDDING_KEY}")
    with safe_open(str(SNAPSHOT_DIR / shard_name), framework="pt", device="cpu") as handle:
        embeddings = handle.get_tensor(EMBEDDING_KEY)
    if embeddings.ndim != 2 or embeddings.shape[1] != HIDDEN_WIDTH:
        raise RuntimeError(f"Unexpected embedding matrix shape: {tuple(embeddings.shape)}")
    if embeddings.shape[0] < vocabulary_size:
        raise RuntimeError("Embedding table is smaller than the tokenizer vocabulary.")
    embeddings = embeddings[:vocabulary_size]
    with safe_open(str(CAPTURE_PATH), framework="pt", device="cpu") as handle:
        states = handle.get_tensor("anchor_hidden_states").float()
    if tuple(states.shape) != (STATE_COUNT, HIDDEN_WIDTH):
        raise RuntimeError(f"Unexpected saved trajectory shape: {tuple(states.shape)}")

    normalized_embeddings = F.normalize(embeddings.to("cuda", dtype=torch.float32), p=2, dim=1)
    normalized_states = F.normalize(states.to("cuda", dtype=torch.float32), p=2, dim=1)
    with torch.inference_mode():
        score_tensor = (normalized_states @ normalized_embeddings.transpose(0, 1)).cpu().contiguous()
    if not torch.isfinite(score_tensor).all():
        raise RuntimeError("Vocabulary projection contains non-finite values.")
    save_file(
        {"cosine_scores": score_tensor},
        str(SCORES_PATH),
        metadata={
            "state_count": str(STATE_COUNT),
            "vocabulary_size": str(vocabulary_size),
            "excluded_capture_token_id": str(capture_token_id),
        },
    )
    del normalized_states, states, embeddings
    gc.collect()

    eligible = np.arange(vocabulary_size, dtype=np.int64)
    eligible = eligible[eligible != capture_token_id]
    scores = score_tensor.numpy()
    cutoff_rows: list[dict[str, object]] = []
    memberships: dict[tuple[int, str], pd.DataFrame] = {}
    all_memberships: list[pd.DataFrame] = []
    for state_index in range(STATE_COUNT):
        values = scores[state_index]
        descending = eligible[np.argsort(-values[eligible], kind="stable")]
        ascending = eligible[np.argsort(values[eligible], kind="stable")]
        upper = topology.elbow_candidate(values[descending])
        lower_inverse = topology.elbow_candidate(-values[ascending])
        positive_ids = descending[: int(upper["cutoff_rank"])]
        negative_ids = ascending[: int(lower_inverse["cutoff_rank"])]
        if np.intersect1d(positive_ids, negative_ids).size:
            raise RuntimeError(f"Positive and negative populations overlap at state {state_index}.")
        cutoff_rows.append(
            {
                "state_index": state_index,
                "state_label": state_label(state_index),
                "eligible_vocabulary_size": len(eligible),
                "excluded_capture_token_id": capture_token_id,
                "upper_cutoff_rank": len(positive_ids),
                "upper_cutoff_score": float(upper["cutoff_score"]),
                "upper_elbow_strength": float(upper["elbow_strength"]),
                "lower_cutoff_rank": len(negative_ids),
                "lower_cutoff_score": -float(lower_inverse["cutoff_score"]),
                "lower_elbow_strength": float(lower_inverse["elbow_strength"]),
                "positive_head_fraction": len(positive_ids) / len(eligible),
                "negative_tail_fraction": len(negative_ids) / len(eligible),
            }
        )
        for side, ids in (("positive_head", positive_ids), ("negative_tail", negative_ids)):
            frame = pd.DataFrame(
                {
                    "prompt": "primary",
                    "state_index": state_index,
                    "state_label": state_label(state_index),
                    "side": side,
                    "token_id": ids,
                    "raw_token": [raw_tokens[item] for item in ids],
                    "decoded_token": [decoded_tokens[item] for item in ids],
                    "display_token": [topology.visible_token(decoded_tokens[item]) for item in ids],
                    "token_class": [token_classes[item] for item in ids],
                    "cosine_score": values[ids],
                    "rank_from_extreme": np.arange(1, len(ids) + 1, dtype=np.int32),
                }
            )
            memberships[(state_index, side)] = frame
            all_memberships.append(frame)

    cutoffs = pd.DataFrame(cutoff_rows)
    tails = pd.concat(all_memberships, ignore_index=True)
    cutoffs.to_csv(RUN_DIR / "cutoffs.csv", index=False)
    tails.to_csv(RUN_DIR / "tail_tokens.csv.gz", index=False, compression="gzip")
    update_component(
        manifest,
        "projection_and_cutoffs",
        started,
        score_shape=list(score_tensor.shape),
        vocabulary_size=vocabulary_size,
        cutoff_rows=len(cutoffs),
        membership_rows=len(tails),
        embedding_shard=shard_name,
        capture_token_id=capture_token_id,
    )
    return normalized_embeddings, memberships, tokenizer


def construct_networks(
    manifest: dict[str, Any],
    normalized_embeddings: torch.Tensor,
    memberships: dict[tuple[int, str], pd.DataFrame],
    vocabulary_size: int,
) -> None:
    started = time.perf_counter()
    metrics: list[dict] = []
    community_rows: list[dict] = []
    community_edge_rows: list[dict] = []
    compact_networks: list[dict] = []
    transitions: list[dict] = []
    matches: list[dict] = []
    previous: dict[str, dict] = {}
    node_count = 0
    edge_count = 0
    nodes_path = RUN_DIR / "nodes.csv.gz"
    edges_path = RUN_DIR / "edges.csv.gz"
    with gzip.open(nodes_path, "wt", encoding="utf-8", newline="") as node_handle, gzip.open(
        edges_path, "wt", encoding="utf-8", newline=""
    ) as edge_handle:
        for state_index in range(STATE_COUNT):
            for side_index, side in enumerate(SIDES):
                network_started = time.perf_counter()
                (
                    metric,
                    nodes,
                    edges,
                    communities,
                    community_edges,
                    state_data,
                    compact,
                ) = topology.analyze_network(
                    "primary",
                    0,
                    state_index,
                    side,
                    side_index,
                    memberships[(state_index, side)],
                    normalized_embeddings,
                    vocabulary_size,
                )
                nodes.to_csv(node_handle, index=False, header=node_count == 0)
                edges.to_csv(edge_handle, index=False, header=edge_count == 0)
                node_count += len(nodes)
                edge_count += len(edges)
                metrics.append(metric)
                community_rows.extend(communities)
                community_edge_rows.extend(community_edges)
                compact_networks.append(compact)
                if side in previous:
                    comparison = topology.compare_state_data(previous[side], state_data)
                    transitions.append(
                        {
                            "side": side,
                            "previous_state_index": state_index - 1,
                            "current_state_index": state_index,
                            "previous_state_label": state_label(state_index - 1),
                            "current_state_label": state_label(state_index),
                            **comparison,
                        }
                    )
                    matches.extend(
                        topology.best_community_matches(
                            "adjacent_state",
                            side,
                            previous[side],
                            state_data,
                            prompt="primary",
                            source_prompt="primary",
                            target_prompt="primary",
                            source_state_index=state_index - 1,
                            target_state_index=state_index,
                        )
                    )
                previous[side] = state_data
                print(
                    f"R017 network {len(metrics):03d}/{EXPECTED_NETWORKS}: state "
                    f"{state_index:02d} {side}, {len(nodes):,} nodes, "
                    f"{len(communities)} communities, "
                    f"{time.perf_counter() - network_started:.1f}s.",
                    flush=True,
                )

    network_index = pd.DataFrame(metrics).sort_values(["state_index", "side"], kind="stable")
    community_nodes = pd.DataFrame(community_rows).sort_values(
        ["state_index", "side", "community_id"], kind="stable"
    )
    community_edges = pd.DataFrame(community_edge_rows).sort_values(
        ["state_index", "side", "community_a", "community_b"], kind="stable"
    )
    transition_frame = pd.DataFrame(transitions).sort_values(
        ["current_state_index", "side"], kind="stable"
    )
    match_frame = pd.DataFrame(matches)
    network_index.to_csv(RUN_DIR / "network_index.csv", index=False)
    community_nodes.to_csv(RUN_DIR / "community_nodes.csv", index=False)
    community_edges.to_csv(RUN_DIR / "community_edges.csv", index=False)
    transition_frame.to_csv(RUN_DIR / "state_transitions.csv", index=False)
    match_frame.to_csv(RUN_DIR / "community_transition_evidence.csv", index=False)
    update_component(
        manifest,
        "networks_and_communities",
        started,
        network_count=len(network_index),
        selected_node_rows=node_count,
        directed_edge_rows=edge_count,
        community_rows=len(community_nodes),
        intercommunity_edge_rows=len(community_edges),
    )
    transition_started = time.perf_counter()
    if len(transition_frame) != EXPECTED_TRANSITIONS:
        raise RuntimeError(f"Expected {EXPECTED_TRANSITIONS} transitions; found {len(transition_frame)}.")
    update_component(
        manifest,
        "adjacent_transitions",
        transition_started,
        transition_rows=len(transition_frame),
        minimum_membership_jaccard=float(transition_frame["membership_jaccard"].min()),
        minimum_edge_jaccard=float(transition_frame["edge_jaccard"].min()),
    )

    export_started = time.perf_counter()
    compact = {
        "schema_version": 1,
        "run_id": RUN_ID,
        "model": {"id": MODEL_ID, "revision": MODEL_REVISION},
        "prompt_record": load_json(PROMPT_RECORD_PATH),
        "state_count": STATE_COUNT,
        "network_count": len(compact_networks),
        "sides": list(SIDES),
        "community_identity": "community_id is local to one state and side",
        "interpretation_boundary": (
            "Positive and negative are cosine alignment sectors. Communities are "
            "measured graph partitions; semantic parent labels are not included."
        ),
        "within_prompt_transitions": transition_frame.to_dict(orient="records"),
        "networks": compact_networks,
    }
    write_json(RUN_DIR / "chatgpt_community_networks.json", compact)
    packet_lines = [
        "# R017 measured layer packets",
        "",
        "Positive and negative denote alignment and anti-alignment with the evolving final-newline state. Negative does not independently establish suppression.",
        "",
    ]
    by_key = {(item["state_index"], item["side"]): item for item in compact_networks}
    for state_index in range(STATE_COUNT):
        packet_lines.extend([f"## State {state_index:02d} — {state_label(state_index)}", ""])
        for side in SIDES:
            item = by_key[(state_index, side)]
            item_metrics = item["metrics"]
            packet_lines.extend(
                [
                    f"### {side}",
                    "",
                    f"- Nodes: {item_metrics['population_size']}",
                    f"- Communities: {item_metrics['community_count']}",
                    f"- Modularity: {item_metrics['community_modularity']:.6f}",
                    "",
                ]
            )
            for community in item["communities"]:
                reps = ", ".join(community["representative_tokens"][:10])
                extremes = ", ".join(community["most_extreme_tokens"][:6])
                packet_lines.append(
                    f"- C{community['community_id']} (n={community['community_size']}): "
                    f"representatives [{reps}]; target-extreme [{extremes}]"
                )
            packet_lines.append("")
    (RUN_DIR / "chatgpt_layer_packets.md").write_text(
        "\n".join(packet_lines).rstrip() + "\n", encoding="utf-8"
    )
    update_component(
        manifest,
        "measured_exports",
        export_started,
        json_networks=len(compact_networks),
        markdown_state_sections=STATE_COUNT,
        semantic_labels_added=False,
    )


def validate_measurement(manifest: dict[str, Any]) -> None:
    started = time.perf_counter()
    network_index = pd.read_csv(RUN_DIR / "network_index.csv")
    communities = pd.read_csv(RUN_DIR / "community_nodes.csv")
    transitions = pd.read_csv(RUN_DIR / "state_transitions.csv")
    if len(network_index) != EXPECTED_NETWORKS:
        raise RuntimeError(f"Expected {EXPECTED_NETWORKS} networks; found {len(network_index)}.")
    if network_index.duplicated(["state_index", "side"]).any():
        raise RuntimeError("Duplicate state/side network identity found.")
    if not (network_index["directed_edge_count"] == network_index["population_size"] * K_NEIGHBORS).all():
        raise RuntimeError("Exact 10-neighbour coverage failed.")
    totals = communities.groupby(["state_index", "side"])["community_size"].sum().sort_index()
    populations = network_index.set_index(["state_index", "side"])["population_size"].sort_index()
    if not totals.equals(populations):
        raise RuntimeError("Community sizes do not reconcile with network populations.")
    if len(transitions) != EXPECTED_TRANSITIONS:
        raise RuntimeError("Adjacent transition coverage is incomplete.")
    VERIFY = [
        "# R017 completeness verification",
        "",
        "- Measurement status: **PASS**",
        f"- Networks: {len(network_index)} / {EXPECTED_NETWORKS}",
        f"- Adjacent transitions: {len(transitions)} / {EXPECTED_TRANSITIONS}",
        f"- Selected token memberships: {int(network_index['population_size'].sum()):,}",
        f"- Directed exact 10-NN edges: {int(network_index['directed_edge_count'].sum()):,}",
        f"- State-local communities: {len(communities):,}",
        "- Every state/side network identity is unique.",
        "- Every selected node belongs to exactly one state-local community.",
        "- Every network has exactly 10 directed neighbours per node.",
        "- Semantic parent labels were not added to the measured exports.",
        "- Final semantic interpretation remains pending.",
    ]
    VERIFICATION_PATH.write_text("\n".join(VERIFY) + "\n", encoding="utf-8")
    MEASURED_REPORT_PATH.write_text(
        "\n".join(
            [
                "# R017 measured topology report",
                "",
                "- Measurement status: **complete and validated**",
                f"- Model: `{MODEL_ID}` at `{MODEL_REVISION}`",
                "- Prompt: `choke point\\ncollapsible barrier\\nspear\\n`",
                f"- Captured states: {STATE_COUNT}",
                f"- Measured networks: {EXPECTED_NETWORKS}",
                f"- Adjacent transition rows: {EXPECTED_TRANSITIONS}",
                "- Response generation: not executed",
                "- Semantic interpretation: pending",
                "",
                "The measured exports contain cosine-sector populations, exact 10-NN graphs, state-local Louvain communities and adjacent-state comparisons. They do not contain imposed topic, GRD or SDA-3 labels.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    update_component(
        manifest,
        "completeness_validation",
        started,
        networks_verified=len(network_index),
        transitions_verified=len(transitions),
        communities_verified=len(communities),
    )


def measure() -> None:
    configure_topology_helpers()
    manifest = initialize_manifest()
    component = "model_capture"
    try:
        capture_states(manifest)
        manifest = load_json(MANIFEST_PATH)
        component = "projection_and_cutoffs"
        embeddings, memberships, tokenizer = project_and_select(manifest)
        manifest = load_json(MANIFEST_PATH)
        component = "networks_and_communities"
        construct_networks(manifest, embeddings, memberships, len(tokenizer))
        del embeddings, memberships
        gc.collect()
        torch.cuda.empty_cache()
        manifest = load_json(MANIFEST_PATH)
        component = "completeness_validation"
        validate_measurement(manifest)
        manifest = load_json(MANIFEST_PATH)
        manifest["status"] = "running"
        manifest["measurement_completed_at"] = utc_now()
        manifest["next_required_component"] = "semantic_interpretation"
        write_json(MANIFEST_PATH, manifest)
        print(json.dumps({"status": "measurement_complete", "manifest": str(MANIFEST_PATH)}), flush=True)
    except BaseException as error:
        fail_run(component, error)
        raise


def finalize() -> None:
    if not MANIFEST_PATH.is_file():
        raise FileNotFoundError("R017 manifest is missing.")
    manifest = load_json(MANIFEST_PATH)
    if manifest.get("status") not in {"running", "successful"}:
        raise RuntimeError(f"R017 cannot be finalized from status {manifest.get('status')}.")
    for name in REQUIRED_COMPONENTS[:-1]:
        if manifest["components"].get(name, {}).get("status") != "successful":
            raise RuntimeError(f"Required component is not successful: {name}")
    if not SEMANTIC_REPORT_PATH.is_file():
        raise FileNotFoundError(f"Semantic report is missing: {SEMANTIC_REPORT_PATH}")
    report_text = SEMANTIC_REPORT_PATH.read_text(encoding="utf-8")
    for required in (
        "Strongest supported result",
        "Measured development through depth",
        "Parent structures",
        "Semantic map",
        "Evidence and limitations",
        "Report standardisation candidates",
    ):
        if required not in report_text:
            raise RuntimeError(f"Semantic report is missing required section: {required}")
    started = time.perf_counter()
    update_component(
        manifest,
        "semantic_interpretation",
        started,
        report=SEMANTIC_REPORT_PATH.name,
        report_sha256=sha256_file(SEMANTIC_REPORT_PATH),
        measurement_interpretation_boundary_stated=True,
    )
    manifest = load_json(MANIFEST_PATH)
    manifest["status"] = "successful"
    manifest["completed_at"] = utc_now()
    manifest["failure_details"] = None
    manifest["next_required_component"] = None
    artifact_names = (
        "prompt_record.json",
        "device_map.json",
        "anchor_hidden_states.safetensors",
        "vocabulary_scores.safetensors",
        "cutoffs.csv",
        "network_index.csv",
        "community_nodes.csv",
        "community_edges.csv",
        "state_transitions.csv",
        "community_transition_evidence.csv",
        "chatgpt_community_networks.json",
        "chatgpt_layer_packets.md",
        "R017_MEASURED_REPORT.md",
        "R017_COMPLETENESS_VERIFICATION.md",
        "R017_SEMANTIC_MAP_REPORT.html",
    )
    manifest["artifacts"] = {
        name: artifact(RUN_DIR / name, tracked_by_git=not name.endswith(".safetensors"))
        for name in artifact_names
    }
    write_json(MANIFEST_PATH, manifest)
    print(json.dumps({"status": "successful", "manifest": str(MANIFEST_PATH)}), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("measure", "finalize"))
    arguments = parser.parse_args()
    if arguments.action == "measure":
        measure()
    else:
        finalize()


if __name__ == "__main__":
    main()
