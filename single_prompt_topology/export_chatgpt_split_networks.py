from __future__ import annotations

import argparse
import gc
import gzip
import hashlib
import json
import math
import os
import platform
import re
import time
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
from huggingface_hub import snapshot_download
from safetensors import safe_open
from sklearn.metrics import adjusted_rand_score
from transformers import AutoTokenizer


RUN_NUMBER = "R008"
RUN_NAME = "lithium-chatgpt-readable-split-networks-validated-retry"
SOURCE_R005_RUN_ID = (
    "R005_lithium-cutoff-population-topology-baseline__"
    "20261112T095944Z_pythia-6.9b_52ff8f97c2"
)
SOURCE_R004_RUN_ID = (
    "R004_lithium-full-curve-cutoffs__"
    "20261112T092701Z_pythia-6.9b_52ff8f97c2"
)
EXPECTED_ULTIMATE_SOURCE_RUN_ID = (
    "R001_lithium-initial-output-inspection__"
    "20261112T063540Z_pythia-6.9b_52ff8f97c2"
)
EXPECTED_PROMPT_SHA256 = (
    "52ff8f97c22b72506ca9b7acfb9be4450726157f1a31c6a4ce3e112380cd7bf7"
)
EXPECTED_TARGET_TOKEN_ID = 27747
EXPECTED_STATE_COUNT = 33
EXPECTED_NETWORK_COUNT = 66
EXPECTED_TRANSITION_ROWS = 64
EXPECTED_VOCABULARY_SIZE = 50277
EXPECTED_NODE_ROWS = 191872
EXPECTED_COMBINED_EDGE_ROWS = 1918720
EXPECTED_MODEL_REVISION = "c0e3eee36dc47af0c49f361c74cfe459c09f7f23"

EXPECTED_HF_HOME = Path(r"D:\AI\cache\huggingface").resolve()
EXPECTED_HF_HUB_CACHE = (EXPECTED_HF_HOME / "hub").resolve()
EMBEDDING_WEIGHT_NAME = "gpt_neox.embed_in.weight"

K_NEIGHBORS = 10
RANDOM_SEED = 20261112
LOUVAIN_RESOLUTION = 1.0
SIDES = ("positive_head", "negative_tail")

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUNS_DIR = PIPELINE_DIR / "runs"
SOURCE_R005_DIR = RUNS_DIR / SOURCE_R005_RUN_ID
SOURCE_R004_DIR = RUNS_DIR / SOURCE_R004_RUN_ID
PLAN_PATH = PIPELINE_DIR / "R008_PLAN.md"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def artifact_record(path: Path) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def visible_token(value: object) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
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


def jaccard(left: set, right: set) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def add_component_success(manifest: dict, component: str, started: float) -> None:
    manifest["components"][component] = {
        "status": "successful",
        "completed_at": utc_now_iso(),
        "seconds": time.perf_counter() - started,
    }


def validate_run_identity() -> None:
    if not re.fullmatch(r"R\d{3}", RUN_NUMBER):
        raise ValueError("RUN_NUMBER must use the form RNNN.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", RUN_NAME):
        raise ValueError("RUN_NAME must use lowercase kebab-case.")
    existing = sorted(path.name for path in RUNS_DIR.glob(f"{RUN_NUMBER}_*"))
    if existing:
        raise RuntimeError(
            f"{RUN_NUMBER} is already assigned to {existing[0]}. "
            "Run numbers are never reused."
        )


def validate_cache_configuration() -> None:
    hf_home = os.environ.get("HF_HOME")
    hub_cache = os.environ.get("HF_HUB_CACHE")
    if not hf_home or not hub_cache:
        raise RuntimeError("HF_HOME and HF_HUB_CACHE must be configured.")
    if Path(hf_home).resolve() != EXPECTED_HF_HOME:
        raise RuntimeError(f"HF_HOME must resolve to {EXPECTED_HF_HOME}.")
    if Path(hub_cache).resolve() != EXPECTED_HF_HUB_CACHE:
        raise RuntimeError(f"HF_HUB_CACHE must resolve to {EXPECTED_HF_HUB_CACHE}.")


def exact_knn(
    normalized_embeddings: torch.Tensor,
    token_ids: np.ndarray,
    k: int,
) -> tuple[np.ndarray, np.ndarray]:
    if token_ids.ndim != 1 or token_ids.size <= k:
        raise ValueError("The selected population must be one-dimensional and exceed k.")
    ids_tensor = torch.as_tensor(
        token_ids,
        dtype=torch.long,
        device=normalized_embeddings.device,
    )
    with torch.inference_mode():
        selected = normalized_embeddings.index_select(0, ids_tensor)
        similarities = selected @ selected.transpose(0, 1)
        similarities.fill_diagonal_(-torch.inf)
        values, positions = torch.topk(
            similarities,
            k=k,
            dim=1,
            largest=True,
            sorted=True,
        )
        neighbor_positions = positions.cpu().numpy().astype(np.int32, copy=False)
        neighbor_scores = values.cpu().numpy().astype(np.float32, copy=False)
    del ids_tensor, selected, similarities, values, positions
    return neighbor_positions, neighbor_scores


def directed_arrays(
    token_ids: np.ndarray,
    neighbor_positions: np.ndarray,
    neighbor_scores: np.ndarray,
) -> dict[str, np.ndarray]:
    population_size, k = neighbor_positions.shape
    if neighbor_scores.shape != neighbor_positions.shape:
        raise ValueError("Neighbour positions and scores have different shapes.")
    source_ids = np.repeat(token_ids, k)
    target_ids = token_ids[neighbor_positions.reshape(-1)]
    scores = neighbor_scores.reshape(-1)
    ranks = np.tile(np.arange(1, k + 1, dtype=np.int16), population_size)
    if np.any(source_ids == target_ids):
        raise RuntimeError("A self-edge survived exact k-nearest-neighbour exclusion.")
    keys = source_ids.astype(np.int64) * EXPECTED_VOCABULARY_SIZE + target_ids
    reverse_keys = target_ids.astype(np.int64) * EXPECTED_VOCABULARY_SIZE + source_ids
    reciprocal = np.isin(reverse_keys, keys, assume_unique=True)
    return {
        "source_ids": source_ids,
        "target_ids": target_ids,
        "scores": scores,
        "ranks": ranks,
        "reciprocal": reciprocal,
    }


def symmetrized_edges(arrays: dict[str, np.ndarray]) -> pd.DataFrame:
    frame = pd.DataFrame(
        {
            "token_a": np.minimum(arrays["source_ids"], arrays["target_ids"]),
            "token_b": np.maximum(arrays["source_ids"], arrays["target_ids"]),
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


def build_graph(token_ids: np.ndarray, edges: pd.DataFrame) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(map(int, token_ids))
    graph.add_edges_from(
        (
            int(row.token_a),
            int(row.token_b),
            {"cosine_similarity": float(row.max_cosine_similarity)},
        )
        for row in edges.itertuples(index=False)
    )
    return graph


def louvain_communities(
    graph: nx.Graph,
    state_index: int,
    side: str,
) -> tuple[list[set[int]], dict[int, int]]:
    side_offset = 0 if side == "positive_head" else 1
    communities = nx.community.louvain_communities(
        graph,
        weight=None,
        resolution=LOUVAIN_RESOLUTION,
        seed=RANDOM_SEED + state_index * 2 + side_offset,
    )
    communities = sorted(
        (set(map(int, community)) for community in communities),
        key=lambda community: (-len(community), min(community)),
    )
    mapping: dict[int, int] = {}
    for community_id, community in enumerate(communities):
        for token_id in community:
            mapping[token_id] = community_id
    return communities, mapping


def analyze_network(
    state_index: int,
    state_type: str,
    state_label: str,
    side: str,
    state_tokens: pd.DataFrame,
    normalized_embeddings: torch.Tensor,
) -> tuple[
    dict,
    pd.DataFrame,
    pd.DataFrame,
    list[dict],
    list[dict],
    dict,
]:
    state_tokens = state_tokens.sort_values("token_id", kind="stable").reset_index(
        drop=True
    )
    token_ids = state_tokens["token_id"].to_numpy(dtype=np.int64, copy=True)
    positions, scores = exact_knn(normalized_embeddings, token_ids, K_NEIGHBORS)
    arrays = directed_arrays(token_ids, positions, scores)
    undirected_edges = symmetrized_edges(arrays)
    graph = build_graph(token_ids, undirected_edges)
    communities, community_by_token = louvain_communities(
        graph,
        state_index,
        side,
    )
    components = list(nx.connected_components(graph))
    modularity = nx.community.modularity(graph, communities, weight=None)

    metric_record = {
        "state_index": state_index,
        "state_type": state_type,
        "state_label": state_label,
        "side": side,
        "population_size": int(token_ids.size),
        "directed_edge_count": int(arrays["scores"].size),
        "undirected_edge_count": int(graph.number_of_edges()),
        "mean_knn_cosine": float(np.mean(arrays["scores"])),
        "median_knn_cosine": float(np.median(arrays["scores"])),
        "minimum_knn_cosine": float(np.min(arrays["scores"])),
        "maximum_knn_cosine": float(np.max(arrays["scores"])),
        "reciprocal_edge_fraction": float(np.mean(arrays["reciprocal"])),
        "connected_component_count": int(len(components)),
        "largest_component_fraction": float(
            max(len(component) for component in components) / token_ids.size
        ),
        "average_clustering": float(nx.average_clustering(graph)),
        "community_count": int(len(communities)),
        "community_modularity": float(modularity),
        "mean_target_cosine": float(state_tokens["cosine_score"].mean()),
        "minimum_target_cosine": float(state_tokens["cosine_score"].min()),
        "maximum_target_cosine": float(state_tokens["cosine_score"].max()),
    }

    community_sizes = {
        community_id: len(community)
        for community_id, community in enumerate(communities)
    }
    node_frame = state_tokens.copy()
    node_frame["side"] = side
    node_frame["display_token"] = node_frame["decoded_token"].map(visible_token)
    node_frame["community_id"] = node_frame["token_id"].map(community_by_token)
    node_frame["community_size"] = node_frame["community_id"].map(community_sizes)
    node_frame["undirected_degree"] = node_frame["token_id"].map(dict(graph.degree()))
    node_frame = node_frame[
        [
            "state_index",
            "state_type",
            "state_label",
            "side",
            "token_id",
            "raw_token",
            "decoded_token",
            "display_token",
            "token_class",
            "is_target_lexical_variant",
            "cosine_score",
            "rank_from_high",
            "rank_from_low",
            "community_id",
            "community_size",
            "undirected_degree",
        ]
    ]

    edge_frame = pd.DataFrame(
        {
            "state_index": state_index,
            "state_type": state_type,
            "state_label": state_label,
            "side": side,
            "source_token_id": arrays["source_ids"],
            "target_token_id": arrays["target_ids"],
            "neighbor_rank": arrays["ranks"],
            "cosine_similarity": arrays["scores"],
            "reciprocal": arrays["reciprocal"],
        }
    )

    indexed = state_tokens.set_index("token_id", drop=False)
    degree_by_token = dict(graph.degree())
    community_records: list[dict] = []
    compact_communities: list[dict] = []
    for community_id, community in enumerate(communities):
        node_ids = sorted(community)
        representatives = sorted(
            node_ids,
            key=lambda token_id: (-degree_by_token[token_id], token_id),
        )[:12]
        extreme_ascending = side == "negative_tail"
        extreme_ids = (
            indexed.loc[node_ids]
            .reset_index(drop=True)
            .sort_values(
                ["cosine_score", "token_id"],
                ascending=[extreme_ascending, True],
                kind="stable",
            )
            .head(12)["token_id"]
            .astype(int)
            .tolist()
        )
        representative_tokens = [
            visible_token(indexed.loc[token_id, "decoded_token"])
            for token_id in representatives
        ]
        extreme_tokens = [
            visible_token(indexed.loc[token_id, "decoded_token"])
            for token_id in extreme_ids
        ]
        class_counts = {
            str(key): int(value)
            for key, value in indexed.loc[node_ids, "token_class"]
            .value_counts()
            .sort_index()
            .items()
        }
        induced = graph.subgraph(node_ids)
        boundary_edges = sum(
            1
            for node_id in node_ids
            for neighbor_id in graph.neighbors(node_id)
            if community_by_token[int(neighbor_id)] != community_id
        )
        record = {
            "state_index": state_index,
            "state_type": state_type,
            "state_label": state_label,
            "side": side,
            "community_id": community_id,
            "community_size": len(node_ids),
            "internal_edge_count": int(induced.number_of_edges()),
            "boundary_edge_count": int(boundary_edges),
            "mean_degree": float(
                np.mean([degree_by_token[token_id] for token_id in node_ids])
            ),
            "mean_target_cosine": float(
                indexed.loc[node_ids, "cosine_score"].mean()
            ),
            "minimum_target_cosine": float(
                indexed.loc[node_ids, "cosine_score"].min()
            ),
            "maximum_target_cosine": float(
                indexed.loc[node_ids, "cosine_score"].max()
            ),
            "representative_token_ids": " ".join(map(str, representatives)),
            "representative_tokens": " | ".join(representative_tokens),
            "most_extreme_token_ids": " ".join(map(str, extreme_ids)),
            "most_extreme_tokens": " | ".join(extreme_tokens),
            "token_class_counts": json.dumps(
                class_counts,
                sort_keys=True,
                ensure_ascii=False,
            ),
        }
        community_records.append(record)
        compact_communities.append(
            {
                "community_id": community_id,
                "community_size": len(node_ids),
                "internal_edge_count": int(induced.number_of_edges()),
                "boundary_edge_count": int(boundary_edges),
                "mean_degree": record["mean_degree"],
                "mean_target_cosine": record["mean_target_cosine"],
                "minimum_target_cosine": record["minimum_target_cosine"],
                "maximum_target_cosine": record["maximum_target_cosine"],
                "representative_tokens": representative_tokens,
                "most_extreme_tokens": extreme_tokens,
                "token_class_counts": class_counts,
            }
        )

    community_edge_frame = undirected_edges.copy()
    community_edge_frame["community_a"] = community_edge_frame["token_a"].map(
        community_by_token
    )
    community_edge_frame["community_b"] = community_edge_frame["token_b"].map(
        community_by_token
    )
    community_edge_frame = community_edge_frame.loc[
        community_edge_frame["community_a"]
        != community_edge_frame["community_b"]
    ].copy()
    compact_edges: list[dict] = []
    community_edge_records: list[dict] = []
    if not community_edge_frame.empty:
        community_edge_frame[["community_a", "community_b"]] = np.sort(
            community_edge_frame[["community_a", "community_b"]].to_numpy(),
            axis=1,
        )
        grouped = (
            community_edge_frame.groupby(
                ["community_a", "community_b"],
                as_index=False,
                sort=True,
            )
            .agg(
                token_edge_count=("max_cosine_similarity", "size"),
                mean_cosine_similarity=("max_cosine_similarity", "mean"),
                maximum_cosine_similarity=("max_cosine_similarity", "max"),
            )
            .reset_index(drop=True)
        )
        for row in grouped.itertuples(index=False):
            record = {
                "state_index": state_index,
                "state_type": state_type,
                "state_label": state_label,
                "side": side,
                "community_a": int(row.community_a),
                "community_b": int(row.community_b),
                "token_edge_count": int(row.token_edge_count),
                "mean_cosine_similarity": float(row.mean_cosine_similarity),
                "maximum_cosine_similarity": float(row.maximum_cosine_similarity),
            }
            community_edge_records.append(record)
            compact_edges.append(
                {
                    "community_a": record["community_a"],
                    "community_b": record["community_b"],
                    "token_edge_count": record["token_edge_count"],
                    "mean_cosine_similarity": record["mean_cosine_similarity"],
                    "maximum_cosine_similarity": record[
                        "maximum_cosine_similarity"
                    ],
                }
            )

    compact = {
        "state_index": state_index,
        "state_type": state_type,
        "state_label": state_label,
        "side": side,
        "metrics": {
            key: value
            for key, value in metric_record.items()
            if key not in {"state_index", "state_type", "state_label", "side"}
        },
        "communities": compact_communities,
        "intercommunity_edges": compact_edges,
    }
    state_data = {
        "membership": set(map(int, token_ids)),
        "edges": set(
            zip(
                undirected_edges["token_a"].astype(int),
                undirected_edges["token_b"].astype(int),
                strict=True,
            )
        ),
        "community_by_token": community_by_token,
        "state_label": state_label,
        "undirected_edges": undirected_edges,
    }
    del positions, scores, arrays, graph
    return (
        metric_record,
        node_frame,
        edge_frame,
        community_records,
        community_edge_records,
        {"compact": compact, "state_data": state_data},
    )


def count_gzip_csv_rows(path: Path) -> int:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return max(sum(1 for _ in handle) - 1, 0)


def run_self_tests() -> None:
    embeddings = F.normalize(
        torch.tensor(
            [
                [1.0, 0.0, 0.0],
                [0.9, 0.1, 0.0],
                [0.8, 0.2, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.9, 0.1],
                [0.0, 0.8, 0.2],
            ],
            dtype=torch.float32,
        ),
        p=2,
        dim=1,
    )
    token_ids = np.arange(6, dtype=np.int64)
    positions, scores = exact_knn(embeddings, token_ids, 2)
    arrays = directed_arrays(token_ids, positions, scores)
    edges = symmetrized_edges(arrays)
    graph = build_graph(token_ids, edges)
    communities, mapping = louvain_communities(graph, 0, "positive_head")
    assert positions.shape == (6, 2)
    assert arrays["source_ids"].size == 12
    assert not np.any(arrays["source_ids"] == arrays["target_ids"])
    assert len(mapping) == 6
    assert sum(len(community) for community in communities) == 6
    assert jaccard({1, 2}, {2, 3}) == 1 / 3
    print("R008 synthetic self-tests passed.")


def main() -> None:
    validate_run_identity()
    validate_cache_configuration()
    if not SOURCE_R004_DIR.is_dir() or not SOURCE_R005_DIR.is_dir():
        raise FileNotFoundError("Required R004 or R005 source run is absent.")
    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"R008 pre-run plan not found: {PLAN_PATH}")

    r004_manifest_path = SOURCE_R004_DIR / "manifest.json"
    r005_manifest_path = SOURCE_R005_DIR / "manifest.json"
    r004_manifest = load_json(r004_manifest_path)
    r005_manifest = load_json(r005_manifest_path)
    model_id = r005_manifest["model"]["id"]
    model_revision = r005_manifest["model"]["revision"]
    prompt_hash = r005_manifest["input"]["prompt_sha256"]
    model_slug = model_id.rsplit("/", 1)[-1]

    started_at = datetime.now(timezone.utc)
    technical_id = (
        f"{started_at.strftime('%Y%m%dT%H%M%SZ')}_"
        f"{model_slug}_{prompt_hash[:10]}"
    )
    run_id = f"{RUN_NUMBER}_{RUN_NAME}__{technical_id}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    manifest_path = run_dir / "manifest.json"
    pipeline_path = Path(__file__).resolve()
    required_components = [
        "source_validation",
        "embedding_load",
        "split_networks",
        "transitions_and_bridges",
        "chatgpt_exports",
        "validation",
    ]
    manifest = {
        "run_number": RUN_NUMBER,
        "run_name": RUN_NAME,
        "run_id": run_id,
        "technical_id": technical_id,
        "source_run": SOURCE_R005_RUN_ID,
        "membership_source_run": SOURCE_R004_RUN_ID,
        "ultimate_source_run": r005_manifest.get("ultimate_source_run"),
        "status": "running",
        "started_at": started_at.isoformat(),
        "completed_at": None,
        "required_components": required_components,
        "components": {name: {"status": "pending"} for name in required_components},
        "model": {
            "id": model_id,
            "revision": model_revision,
            "model_forward_executed": False,
            "full_model_loaded": False,
            "embedding_weight_loaded": True,
            "embedding_weight": EMBEDDING_WEIGHT_NAME,
            "source_score_matrix_recalculated": False,
        },
        "input": r005_manifest["input"],
        "pipeline": {
            "script": str(pipeline_path.relative_to(PROJECT_DIR)),
            "script_sha256": sha256_file(pipeline_path),
            "pre_run_plan": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
            "pre_run_plan_sha256": sha256_file(PLAN_PATH),
        },
        "environment": {
            "python": platform.python_version(),
            "torch": torch.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "networkx": nx.__version__,
            "scikit_learn": sklearn.__version__,
            "transformers": transformers.__version__,
            "safetensors": safetensors.__version__,
            "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "hf_home": str(EXPECTED_HF_HOME),
            "hf_hub_cache": str(EXPECTED_HF_HUB_CACHE),
        },
        "method": {
            "basis": "static Pythia input embeddings",
            "metric": "cosine_similarity",
            "knn_k": K_NEIGHBORS,
            "primary_network_count": EXPECTED_NETWORK_COUNT,
            "primary_network_definition": (
                "separate exact directed 10-nearest-neighbour graphs inside each "
                "state-side population"
            ),
            "undirected_graph": "edge retained when either directed relation exists",
            "undirected_graph_weighting": "unweighted for topology and communities",
            "community_algorithm": "NetworkX Louvain",
            "community_resolution": LOUVAIN_RESOLUTION,
            "cross_side_definition": (
                "cross-region directed relations retained from R005 combined "
                "10-nearest-neighbour graphs; not exhaustive cross-side similarity"
            ),
            "interpretation_boundary": (
                "Layer-wise differences arise from changing R004 membership inside "
                "one fixed static embedding topology. Positive means target-relative "
                "alignment and negative means anti-alignment. Neither establishes a "
                "topic, suppression, contradiction, exclusion or curvature."
            ),
        },
        "source_manifests": {
            "R004": {
                "path": str(r004_manifest_path.relative_to(PROJECT_DIR)).replace(
                    "\\", "/"
                ),
                "sha256": sha256_file(r004_manifest_path),
            },
            "R005": {
                "path": str(r005_manifest_path.relative_to(PROJECT_DIR)).replace(
                    "\\", "/"
                ),
                "sha256": sha256_file(r005_manifest_path),
            },
        },
        "source_artifacts": {},
        "artifacts": {},
        "results": {},
    }

    def write_manifest() -> None:
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    write_manifest()
    current_component = "source_validation"
    try:
        component_started = time.perf_counter()
        if r004_manifest.get("status") != "successful":
            raise RuntimeError("R004 source manifest is not successful.")
        if r005_manifest.get("status") != "successful":
            raise RuntimeError("R005 source manifest is not successful.")
        if r004_manifest.get("run_id") != SOURCE_R004_RUN_ID:
            raise RuntimeError("R004 source identity does not match the plan.")
        if r005_manifest.get("run_id") != SOURCE_R005_RUN_ID:
            raise RuntimeError("R005 source identity does not match the plan.")
        if r005_manifest.get("source_run") != SOURCE_R004_RUN_ID:
            raise RuntimeError("R005 does not identify the planned R004 source.")
        if (
            r005_manifest.get("ultimate_source_run")
            != EXPECTED_ULTIMATE_SOURCE_RUN_ID
        ):
            raise RuntimeError("Ultimate source identity does not match the plan.")
        if prompt_hash != EXPECTED_PROMPT_SHA256:
            raise RuntimeError("Prompt hash does not match the plan.")
        if int(r005_manifest["input"]["target_token_id"]) != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("Target token does not match the plan.")
        if model_revision != EXPECTED_MODEL_REVISION:
            raise RuntimeError("Model revision does not match the plan.")

        source_specs = [
            (
                "R004/cutoffs.csv",
                SOURCE_R004_DIR / "cutoffs.csv",
                r004_manifest["artifacts"]["cutoffs.csv"],
            ),
            (
                "R004/tail_tokens.csv.gz",
                SOURCE_R004_DIR / "tail_tokens.csv.gz",
                r004_manifest["artifacts"]["tail_tokens.csv.gz"],
            ),
            (
                "R005/knn_edges.csv.gz",
                SOURCE_R005_DIR / "knn_edges.csv.gz",
                r005_manifest["artifacts"]["knn_edges.csv.gz"],
            ),
        ]
        for key, path, expected in source_specs:
            if not path.is_file():
                raise FileNotFoundError(f"Missing source artifact: {path}")
            if path.stat().st_size != expected["bytes"]:
                raise RuntimeError(f"Source artifact size mismatch: {key}")
            if sha256_file(path) != expected["sha256"]:
                raise RuntimeError(f"Source artifact hash mismatch: {key}")
            manifest["source_artifacts"][key] = expected

        cutoffs = pd.read_csv(SOURCE_R004_DIR / "cutoffs.csv")
        tails = pd.read_csv(SOURCE_R004_DIR / "tail_tokens.csv.gz")
        if len(cutoffs) != EXPECTED_STATE_COUNT:
            raise RuntimeError("R004 cutoffs do not cover all 33 states.")
        if len(tails) != EXPECTED_NODE_ROWS:
            raise RuntimeError("R004 tail membership row count does not match.")
        if tails.duplicated(["state_index", "token_id"]).any():
            raise RuntimeError("R004 tail memberships contain duplicate state-token rows.")
        if set(tails["region"].unique()) != set(SIDES):
            raise RuntimeError("R004 tail memberships contain an unexpected region.")
        if (tails["token_id"] == EXPECTED_TARGET_TOKEN_ID).any():
            raise RuntimeError("The exact target appears in R004 membership.")
        observed_counts = (
            tails.groupby(["state_index", "region"]).size().unstack(fill_value=0)
        )
        observed_counts = observed_counts.reindex(
            range(EXPECTED_STATE_COUNT),
            fill_value=0,
        )
        if not np.array_equal(
            observed_counts["positive_head"].to_numpy(),
            cutoffs["positive_head_count"].to_numpy(),
        ):
            raise RuntimeError("Positive membership counts do not reconcile.")
        if not np.array_equal(
            observed_counts["negative_tail"].to_numpy(),
            cutoffs["negative_tail_count"].to_numpy(),
        ):
            raise RuntimeError("Negative membership counts do not reconcile.")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "validated_source_artifact_count": len(source_specs),
                "state_count": EXPECTED_STATE_COUNT,
                "tail_membership_rows": len(tails),
            }
        )
        write_manifest()
        print("R008 source validation complete.", flush=True)

        current_component = "embedding_load"
        component_started = time.perf_counter()
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        snapshot_path = Path(
            snapshot_download(
                model_id,
                revision=model_revision,
                cache_dir=EXPECTED_HF_HUB_CACHE,
                local_files_only=True,
            )
        )
        tokenizer = AutoTokenizer.from_pretrained(snapshot_path, local_files_only=True)
        if len(tokenizer) != EXPECTED_VOCABULARY_SIZE:
            raise RuntimeError("Cached tokenizer vocabulary size does not match.")
        index_path = snapshot_path / "model.safetensors.index.json"
        index_data = load_json(index_path)
        shard_name = index_data["weight_map"].get(EMBEDDING_WEIGHT_NAME)
        if not shard_name:
            raise KeyError(f"Embedding weight not found: {EMBEDDING_WEIGHT_NAME}")
        shard_path = snapshot_path / shard_name
        with safe_open(shard_path, framework="pt", device="cpu") as handle:
            embedding_matrix = handle.get_tensor(EMBEDDING_WEIGHT_NAME)
        embedding_matrix = embedding_matrix[:EXPECTED_VOCABULARY_SIZE]
        if tuple(embedding_matrix.shape) != (EXPECTED_VOCABULARY_SIZE, 4096):
            raise RuntimeError("Embedding matrix has an unexpected shape.")
        if not torch.isfinite(embedding_matrix).all():
            raise RuntimeError("Embedding matrix contains non-finite values.")
        row_norms = torch.linalg.vector_norm(embedding_matrix.float(), dim=1)
        if torch.any(row_norms == 0):
            raise RuntimeError("Embedding matrix contains a zero-norm row.")
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if device.type != "cuda":
            raise RuntimeError("R008 exact split-network run requires CUDA.")
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        normalized_embeddings = F.normalize(
            embedding_matrix.to(device=device, dtype=torch.float32),
            p=2,
            dim=1,
        )
        del embedding_matrix, row_norms
        gc.collect()
        if not torch.isfinite(normalized_embeddings).all():
            raise RuntimeError("Normalized embeddings contain non-finite values.")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "embedding_shape": list(normalized_embeddings.shape),
                "embedding_dtype": str(normalized_embeddings.dtype),
                "embedding_shard": shard_name,
                "embedding_shard_bytes": shard_path.stat().st_size,
                "safetensors_index_sha256": sha256_file(index_path),
            }
        )
        write_manifest()
        print(
            f"R008 embedding load complete: {tuple(normalized_embeddings.shape)} on {device}.",
            flush=True,
        )

        index_path_out = run_dir / "network_index.csv"
        nodes_path = run_dir / "nodes.csv.gz"
        edges_path = run_dir / "edges.csv.gz"
        communities_path = run_dir / "community_nodes.csv"
        community_edges_path = run_dir / "community_edges.csv"
        transitions_path = run_dir / "state_transitions.csv"
        persistent_path = run_dir / "persistent_edges.csv.gz"
        cross_path = run_dir / "cross_side_edges.csv.gz"
        json_path = run_dir / "chatgpt_community_networks.json"
        packets_path = run_dir / "chatgpt_layer_packets.md"
        findings_path = run_dir / "findings.md"

        current_component = "split_networks"
        component_started = time.perf_counter()
        network_records: list[dict] = []
        community_records: list[dict] = []
        community_edge_records: list[dict] = []
        compact_networks: list[dict] = []
        transition_records: list[dict] = []
        previous_by_side: dict[str, dict] = {}
        persistent_accumulator: dict[
            tuple[str, int, int], list[float | int]
        ] = {}
        node_rows_written = 0
        edge_rows_written = 0

        with gzip.open(
            nodes_path,
            "wt",
            encoding="utf-8",
            newline="",
        ) as node_handle, gzip.open(
            edges_path,
            "wt",
            encoding="utf-8",
            newline="",
        ) as edge_handle:
            for state_index in range(EXPECTED_STATE_COUNT):
                state_row = cutoffs.loc[
                    cutoffs["state_index"] == state_index
                ].iloc[0]
                state_type = str(state_row["state_type"])
                state_label = str(state_row["state_label"])
                for side in SIDES:
                    network_started = time.perf_counter()
                    state_tokens = tails.loc[
                        (tails["state_index"] == state_index)
                        & (tails["region"] == side)
                    ].copy()
                    (
                        metric_record,
                        node_frame,
                        edge_frame,
                        state_communities,
                        state_community_edges,
                        auxiliary,
                    ) = analyze_network(
                        state_index,
                        state_type,
                        state_label,
                        side,
                        state_tokens,
                        normalized_embeddings,
                    )
                    node_frame.to_csv(
                        node_handle,
                        index=False,
                        header=node_rows_written == 0,
                    )
                    edge_frame.to_csv(
                        edge_handle,
                        index=False,
                        header=edge_rows_written == 0,
                    )
                    node_rows_written += len(node_frame)
                    edge_rows_written += len(edge_frame)
                    network_records.append(metric_record)
                    community_records.extend(state_communities)
                    community_edge_records.extend(state_community_edges)
                    compact_networks.append(auxiliary["compact"])

                    current = auxiliary["state_data"]
                    previous = previous_by_side.get(side)
                    if previous is not None:
                        shared_tokens = previous["membership"] & current["membership"]
                        previous_labels = [
                            previous["community_by_token"][token_id]
                            for token_id in sorted(shared_tokens)
                        ]
                        current_labels = [
                            current["community_by_token"][token_id]
                            for token_id in sorted(shared_tokens)
                        ]
                        retained_edges = previous["edges"] & current["edges"]
                        transition_records.append(
                            {
                                "side": side,
                                "previous_state_index": state_index - 1,
                                "current_state_index": state_index,
                                "previous_state_label": previous["state_label"],
                                "current_state_label": state_label,
                                "shared_token_count": len(shared_tokens),
                                "membership_jaccard": jaccard(
                                    previous["membership"],
                                    current["membership"],
                                ),
                                "previous_edge_count": len(previous["edges"]),
                                "current_edge_count": len(current["edges"]),
                                "retained_edge_count": len(retained_edges),
                                "new_edge_count": len(
                                    current["edges"] - previous["edges"]
                                ),
                                "disappeared_edge_count": len(
                                    previous["edges"] - current["edges"]
                                ),
                                "edge_jaccard": jaccard(
                                    previous["edges"],
                                    current["edges"],
                                ),
                                "community_adjusted_rand": float(
                                    adjusted_rand_score(
                                        previous_labels,
                                        current_labels,
                                    )
                                ),
                            }
                        )
                    previous_by_side[side] = {
                        key: value
                        for key, value in current.items()
                        if key != "undirected_edges"
                    }

                    for row in current["undirected_edges"].itertuples(index=False):
                        token_a = int(row.token_a)
                        token_b = int(row.token_b)
                        similarity = float(row.max_cosine_similarity)
                        key = (side, token_a, token_b)
                        value = persistent_accumulator.get(key)
                        if value is None:
                            value = [0, 0.0, -math.inf, 0]
                            persistent_accumulator[key] = value
                        value[0] = int(value[0]) + 1
                        value[1] = float(value[1]) + similarity
                        value[2] = max(float(value[2]), similarity)
                        value[3] = int(value[3]) | (1 << state_index)

                    print(
                        f"R008 state {state_index:02d}/32 {side} complete "
                        f"({len(node_frame)} nodes, "
                        f"{time.perf_counter() - network_started:.1f}s).",
                        flush=True,
                    )

        network_index = pd.DataFrame(network_records).sort_values(
            ["state_index", "side"]
        )
        network_index.to_csv(index_path_out, index=False)
        community_nodes = pd.DataFrame(community_records).sort_values(
            ["state_index", "side", "community_id"]
        )
        community_nodes.to_csv(communities_path, index=False)
        community_edges = pd.DataFrame(community_edge_records).sort_values(
            ["state_index", "side", "community_a", "community_b"]
        )
        community_edges.to_csv(community_edges_path, index=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "primary_network_count": len(network_index),
                "node_rows": node_rows_written,
                "directed_edge_rows": edge_rows_written,
                "community_rows": len(community_nodes),
                "intercommunity_edge_rows": len(community_edges),
            }
        )
        write_manifest()

        current_component = "transitions_and_bridges"
        component_started = time.perf_counter()
        transitions = pd.DataFrame(transition_records).sort_values(
            ["side", "current_state_index"]
        )
        transitions.to_csv(transitions_path, index=False)

        token_metadata = (
            tails.sort_values(["token_id", "state_index"], kind="stable")
            .drop_duplicates("token_id")
            .set_index("token_id", drop=False)
        )
        persistent_records: list[dict] = []
        for (side, token_a, token_b), values in persistent_accumulator.items():
            state_count = int(values[0])
            if state_count < 2:
                continue
            state_mask = int(values[3])
            state_indices = [
                index
                for index in range(EXPECTED_STATE_COUNT)
                if state_mask & (1 << index)
            ]
            persistent_records.append(
                {
                    "side": side,
                    "token_a": token_a,
                    "token_a_decoded": token_metadata.loc[token_a, "decoded_token"],
                    "token_a_display": visible_token(
                        token_metadata.loc[token_a, "decoded_token"]
                    ),
                    "token_b": token_b,
                    "token_b_decoded": token_metadata.loc[token_b, "decoded_token"],
                    "token_b_display": visible_token(
                        token_metadata.loc[token_b, "decoded_token"]
                    ),
                    "state_count": state_count,
                    "state_fraction": state_count / EXPECTED_STATE_COUNT,
                    "first_state_index": state_indices[0],
                    "last_state_index": state_indices[-1],
                    "state_indices": " ".join(map(str, state_indices)),
                    "mean_cosine_similarity": float(values[1]) / state_count,
                    "maximum_cosine_similarity": float(values[2]),
                }
            )
        persistent_edges = pd.DataFrame(persistent_records)
        if persistent_edges.empty:
            raise RuntimeError("No split-network edge appeared in two or more states.")
        persistent_edges = persistent_edges.sort_values(
            [
                "state_count",
                "mean_cosine_similarity",
                "side",
                "token_a",
                "token_b",
            ],
            ascending=[False, False, True, True, True],
        )
        persistent_edges.to_csv(persistent_path, index=False, compression="gzip")

        cross_chunks: list[pd.DataFrame] = []
        combined_edge_rows = 0
        source_edge_path = SOURCE_R005_DIR / "knn_edges.csv.gz"
        for chunk in pd.read_csv(source_edge_path, chunksize=250000):
            combined_edge_rows += len(chunk)
            selected = chunk.loc[chunk["region_pair"] == "cross_region"].copy()
            if not selected.empty:
                cross_chunks.append(selected)
        if combined_edge_rows != EXPECTED_COMBINED_EDGE_ROWS:
            raise RuntimeError("R005 combined edge row count does not reconcile.")
        if not cross_chunks:
            raise RuntimeError("R005 contains no cross-region directed edges.")
        cross_edges = pd.concat(cross_chunks, ignore_index=True)
        display_by_token = {
            int(token_id): visible_token(decoded)
            for token_id, decoded in zip(
                token_metadata["token_id"],
                token_metadata["decoded_token"],
                strict=True,
            )
        }
        cross_edges["source_display_token"] = cross_edges["source_token_id"].map(
            display_by_token
        )
        cross_edges["target_display_token"] = cross_edges["target_token_id"].map(
            display_by_token
        )
        cross_edges = cross_edges[
            [
                "state_index",
                "state_type",
                "state_label",
                "source_token_id",
                "source_display_token",
                "target_token_id",
                "target_display_token",
                "neighbor_rank",
                "cosine_similarity",
                "source_region",
                "target_region",
                "reciprocal",
            ]
        ].sort_values(
            ["state_index", "source_token_id", "neighbor_rank"],
            kind="stable",
        )
        cross_edges.to_csv(cross_path, index=False, compression="gzip")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "adjacent_transition_rows": len(transitions),
                "persistent_edge_rows": len(persistent_edges),
                "cross_side_directed_edge_rows": len(cross_edges),
                "validated_r005_combined_edge_rows": combined_edge_rows,
            }
        )
        write_manifest()

        current_component = "chatgpt_exports"
        component_started = time.perf_counter()
        compact_document = {
            "schema_version": 1,
            "run_id": run_id,
            "network_count": len(compact_networks),
            "state_count": EXPECTED_STATE_COUNT,
            "sides": list(SIDES),
            "stable_join_key": "token_id",
            "community_identity": (
                "community_id is local to one state and side and is not a "
                "persistent semantic identity"
            ),
            "cross_side_evidence": (
                "See cross_side_edges.csv.gz for cross-region directed relations "
                "retained from R005 combined 10-nearest-neighbour graphs."
            ),
            "interpretation_boundary": manifest["method"][
                "interpretation_boundary"
            ],
            "networks": compact_networks,
        }
        json_path.write_text(
            json.dumps(compact_document, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        packet_lines = [
            "# R008 ChatGPT layer packets",
            "",
            "These packets summarize all 66 split community networks. The JSON and "
            "CSV artifacts contain the complete compact and token-level evidence.",
            "",
            "Interpretation boundary: positive_head means high target-relative cosine "
            "alignment and negative_tail means geometric anti-alignment. Community "
            "partitions are not established topics. Negative membership does not by "
            "itself establish suppression, contradiction or exclusion.",
            "",
        ]
        compact_by_key = {
            (int(network["state_index"]), str(network["side"])): network
            for network in compact_networks
        }
        for state_index in range(EXPECTED_STATE_COUNT):
            state_label = str(
                network_index.loc[
                    network_index["state_index"] == state_index,
                    "state_label",
                ].iloc[0]
            )
            packet_lines.extend(
                [
                    f"## State {state_index}: {state_label}",
                    "",
                ]
            )
            for side in SIDES:
                network = compact_by_key[(state_index, side)]
                metrics = network["metrics"]
                packet_lines.extend(
                    [
                        f"### {side}",
                        "",
                        f"- Nodes: {metrics['population_size']}",
                        f"- Directed 10-NN edges: {metrics['directed_edge_count']}",
                        f"- Undirected edges: {metrics['undirected_edge_count']}",
                        f"- Mean 10-NN cosine: {metrics['mean_knn_cosine']:.6f}",
                        f"- Communities: {metrics['community_count']}",
                        f"- Modularity: {metrics['community_modularity']:.6f}",
                        "",
                        "Largest communities:",
                        "",
                    ]
                )
                largest = sorted(
                    network["communities"],
                    key=lambda item: (
                        -int(item["community_size"]),
                        int(item["community_id"]),
                    ),
                )[:8]
                for community in largest:
                    representatives = ", ".join(
                        community["representative_tokens"][:8]
                    )
                    extremes = ", ".join(community["most_extreme_tokens"][:5])
                    packet_lines.append(
                        f"- C{community['community_id']} "
                        f"(n={community['community_size']}): "
                        f"representatives [{representatives}]; "
                        f"target-extreme [{extremes}]; "
                        f"token classes {community['token_class_counts']}"
                    )
                packet_lines.extend(["", "Strongest intercommunity connections:", ""])
                strongest = sorted(
                    network["intercommunity_edges"],
                    key=lambda item: (
                        -int(item["token_edge_count"]),
                        -float(item["mean_cosine_similarity"]),
                    ),
                )[:10]
                if strongest:
                    for edge in strongest:
                        packet_lines.append(
                            f"- C{edge['community_a']} to C{edge['community_b']}: "
                            f"{edge['token_edge_count']} token edges; "
                            f"mean cosine {edge['mean_cosine_similarity']:.6f}"
                        )
                else:
                    packet_lines.append("- No intercommunity edges.")
                packet_lines.append("")

            state_cross = cross_edges.loc[
                cross_edges["state_index"] == state_index
            ].nlargest(10, "cosine_similarity")
            packet_lines.extend(
                [
                    "### Secondary cross-side relations from R005",
                    "",
                ]
            )
            if state_cross.empty:
                packet_lines.append("- None retained by the combined graph.")
            else:
                for row in state_cross.itertuples(index=False):
                    packet_lines.append(
                        f"- {row.source_display_token} ({row.source_region}) to "
                        f"{row.target_display_token} ({row.target_region}): "
                        f"cosine {float(row.cosine_similarity):.6f}, "
                        f"combined-neighbour rank {int(row.neighbor_rank)}"
                    )
            packet_lines.append("")
        packets_path.write_text("\n".join(packet_lines) + "\n", encoding="utf-8")

        side_summaries = {}
        for side in SIDES:
            side_networks = network_index.loc[network_index["side"] == side]
            side_transitions = transitions.loc[transitions["side"] == side]
            side_summaries[side] = {
                "population_min": int(side_networks["population_size"].min()),
                "population_max": int(side_networks["population_size"].max()),
                "community_min": int(side_networks["community_count"].min()),
                "community_max": int(side_networks["community_count"].max()),
                "modularity_min": float(
                    side_networks["community_modularity"].min()
                ),
                "modularity_max": float(
                    side_networks["community_modularity"].max()
                ),
                "median_membership_jaccard": float(
                    side_transitions["membership_jaccard"].median()
                ),
                "median_edge_jaccard": float(
                    side_transitions["edge_jaccard"].median()
                ),
                "median_community_ari": float(
                    side_transitions["community_adjusted_rand"].median()
                ),
            }

        findings_lines = [
            "# R008 findings: ChatGPT-readable split networks",
            "",
            "## Direct observations",
            "",
            f"- All {EXPECTED_NETWORK_COUNT} planned primary networks were produced: "
            "one positive-head and one negative-tail network at each of 33 states.",
            f"- The complete export contains {node_rows_written:,} node-state rows and "
            f"{edge_rows_written:,} directed within-side 10-nearest-neighbour edges.",
            f"- The secondary R005 bridge table contains {len(cross_edges):,} directed "
            "cross-side relations retained by the earlier combined graphs.",
        ]
        for side in SIDES:
            values = side_summaries[side]
            findings_lines.extend(
                [
                    f"- {side} population size ranged from "
                    f"{values['population_min']:,} to {values['population_max']:,}; "
                    f"community count ranged from {values['community_min']} to "
                    f"{values['community_max']}; modularity ranged from "
                    f"{values['modularity_min']:.4f} to "
                    f"{values['modularity_max']:.4f}.",
                    f"- {side} median adjacent-state membership Jaccard was "
                    f"{values['median_membership_jaccard']:.4f}, median edge Jaccard "
                    f"was {values['median_edge_jaccard']:.4f}, and median community "
                    f"adjusted Rand index was {values['median_community_ari']:.4f}.",
                ]
            )
        findings_lines.extend(
            [
                "",
                "## Supported conclusion",
                "",
                "The R004 positive and negative populations can now be reconstructed "
                "and inspected as separate static-embedding relationship networks at "
                "every recorded state. Compact community-level exports make those "
                "networks accessible for external semantic interpretation while the "
                "complete tables preserve the measured evidence.",
                "",
                "## Limitations",
                "",
                "- The static vocabulary geometry is fixed. Layer-wise changes come "
                "from changing target-relative membership, not contextual movement of "
                "every selected vocabulary token.",
                "- Community representatives can expose lexical, morphological and "
                "tokenizer structure; they are not automatic topic labels.",
                "- Cross-side relations are only those retained by R005's combined "
                "10-nearest-neighbour graphs and are not an exhaustive bipartite graph.",
                "- Positive alignment does not establish semantic centrality, and "
                "negative anti-alignment does not establish suppression or exclusion.",
                "- R008 does not test coherence, semantic conflict or curvature density.",
            ]
        )
        findings_path.write_text(
            "\n".join(findings_lines) + "\n",
            encoding="utf-8",
        )
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "compact_json_network_count": len(compact_networks),
                "layer_packet_state_count": EXPECTED_STATE_COUNT,
                "findings_report_written": True,
            }
        )
        write_manifest()

        current_component = "validation"
        component_started = time.perf_counter()
        artifact_paths = [
            index_path_out,
            nodes_path,
            edges_path,
            communities_path,
            community_edges_path,
            transitions_path,
            persistent_path,
            cross_path,
            json_path,
            packets_path,
            findings_path,
        ]
        if len(network_index) != EXPECTED_NETWORK_COUNT:
            raise RuntimeError("Network index does not contain all 66 networks.")
        expected_pairs = {
            (state_index, side)
            for state_index in range(EXPECTED_STATE_COUNT)
            for side in SIDES
        }
        actual_pairs = set(
            zip(
                network_index["state_index"].astype(int),
                network_index["side"].astype(str),
                strict=True,
            )
        )
        if actual_pairs != expected_pairs:
            raise RuntimeError("Network index state-side coverage is incomplete.")
        if node_rows_written != EXPECTED_NODE_ROWS:
            raise RuntimeError("In-memory node row count does not reconcile.")
        persisted_node_rows = sum(
            len(chunk)
            for chunk in pd.read_csv(
                nodes_path,
                usecols=["state_index"],
                chunksize=50000,
            )
        )
        if persisted_node_rows != EXPECTED_NODE_ROWS:
            raise RuntimeError("Persisted node row count does not reconcile.")
        expected_edges = EXPECTED_NODE_ROWS * K_NEIGHBORS
        if edge_rows_written != expected_edges:
            raise RuntimeError("In-memory directed edge count does not reconcile.")
        if count_gzip_csv_rows(edges_path) != expected_edges:
            raise RuntimeError("Persisted directed edge count does not reconcile.")
        if not (
            network_index["directed_edge_count"]
            == network_index["population_size"] * K_NEIGHBORS
        ).all():
            raise RuntimeError("A primary network has the wrong edge count.")
        if len(transitions) != EXPECTED_TRANSITION_ROWS:
            raise RuntimeError("Transition output does not contain 64 rows.")
        if not (
            transitions.groupby("side").size().reindex(SIDES).to_numpy() == 32
        ).all():
            raise RuntimeError("Each side must contain 32 adjacent transitions.")
        if len(compact_networks) != EXPECTED_NETWORK_COUNT:
            raise RuntimeError("Compact JSON source does not cover all networks.")
        persisted_json = load_json(json_path)
        if len(persisted_json["networks"]) != EXPECTED_NETWORK_COUNT:
            raise RuntimeError("Persisted compact JSON does not cover all networks.")
        finite_network_columns = [
            "mean_knn_cosine",
            "median_knn_cosine",
            "minimum_knn_cosine",
            "maximum_knn_cosine",
            "reciprocal_edge_fraction",
            "largest_component_fraction",
            "average_clustering",
            "community_modularity",
            "mean_target_cosine",
            "minimum_target_cosine",
            "maximum_target_cosine",
        ]
        if not np.isfinite(
            network_index[finite_network_columns].to_numpy()
        ).all():
            raise RuntimeError("Network metrics contain non-finite values.")
        if not np.isfinite(
            transitions[
                [
                    "membership_jaccard",
                    "edge_jaccard",
                    "community_adjusted_rand",
                ]
            ].to_numpy()
        ).all():
            raise RuntimeError("Transition metrics contain non-finite values.")
        if len(cross_edges) == 0:
            raise RuntimeError("Cross-side bridge export is empty.")
        for path in artifact_paths:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"Required R008 artifact is absent or empty: {path}")

        torch.cuda.synchronize()
        peak_gpu_bytes = int(torch.cuda.max_memory_allocated())
        manifest["artifacts"] = {
            str(path.relative_to(run_dir)).replace("\\", "/"): artifact_record(path)
            for path in artifact_paths
        }
        manifest["results"] = {
            "state_count": EXPECTED_STATE_COUNT,
            "side_count": len(SIDES),
            "primary_network_count": len(network_index),
            "valid_vocabulary_size": EXPECTED_VOCABULARY_SIZE,
            "knn_k": K_NEIGHBORS,
            "node_rows": node_rows_written,
            "directed_edge_rows": edge_rows_written,
            "community_rows": len(community_nodes),
            "intercommunity_edge_rows": len(community_edges),
            "transition_rows": len(transitions),
            "persistent_edge_rows": len(persistent_edges),
            "cross_side_directed_edge_rows": len(cross_edges),
            "compact_json_network_count": len(compact_networks),
            "side_summaries": side_summaries,
            "peak_gpu_memory_bytes": peak_gpu_bytes,
        }
        add_component_success(manifest, current_component, component_started)
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now_iso()
        write_manifest()

        print(f"Run:                    {run_id}", flush=True)
        print(f"Status:                 {manifest['status']}", flush=True)
        print(f"Primary networks:       {len(network_index)}", flush=True)
        print(f"Node rows:              {node_rows_written}", flush=True)
        print(f"Directed edge rows:     {edge_rows_written}", flush=True)
        print(f"Cross-side edge rows:   {len(cross_edges)}", flush=True)
        print(f"Peak GPU memory:        {peak_gpu_bytes / 1024**3:.2f} GiB", flush=True)
        print(f"Output:                 {run_dir}", flush=True)
    except Exception as error:
        manifest["status"] = "failed"
        manifest["completed_at"] = utc_now_iso()
        manifest["components"][current_component] = {
            "status": "failed",
            "completed_at": utc_now_iso(),
            "error_type": type(error).__name__,
            "error": str(error),
        }
        write_manifest()
        raise
    finally:
        if "normalized_embeddings" in locals():
            del normalized_embeddings
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="R008 ChatGPT-readable split-network export"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run synthetic validation without creating an R008 run directory.",
    )
    arguments = parser.parse_args()
    if arguments.self_test:
        run_self_tests()
    else:
        main()
