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

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
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
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score
from transformers import AutoTokenizer


RUN_NUMBER = "R005"
RUN_NAME = "lithium-cutoff-population-topology-baseline"
SOURCE_RUN_ID = (
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
EXPECTED_VOCABULARY_SIZE = 50277
EXPECTED_TAIL_ROWS = 191872
EXPECTED_MODEL_REVISION = "c0e3eee36dc47af0c49f361c74cfe459c09f7f23"

EXPECTED_HF_HOME = Path(r"D:\AI\cache\huggingface").resolve()
EXPECTED_HF_HUB_CACHE = (EXPECTED_HF_HOME / "hub").resolve()
EMBEDDING_WEIGHT_NAME = "gpt_neox.embed_in.weight"

K_NEIGHBORS = 10
RANDOM_REPLICATES = 20
RANDOM_SEED = 20261112
LOUVAIN_RESOLUTION = 1.0
SELECTED_FIGURE_STATES = (0, 8, 16, 24, 32)
COMPARISON_METRICS = (
    "mean_knn_cosine",
    "same_region_edge_fraction",
    "reciprocal_edge_fraction",
)

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUNS_DIR = PIPELINE_DIR / "runs"
SOURCE_RUN_DIR = RUNS_DIR / SOURCE_RUN_ID
PLAN_PATH = PIPELINE_DIR / "R005_PLAN.md"
REQUIRED_SOURCE_ARTIFACTS = ("cutoffs.csv", "tail_tokens.csv.gz")


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


def add_component_success(manifest: dict, component: str, started: float) -> None:
    manifest["components"][component] = {
        "status": "successful",
        "completed_at": utc_now_iso(),
        "seconds": time.perf_counter() - started,
    }


def jaccard(left: set, right: set) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


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


def exact_knn(
    normalized_embeddings: torch.Tensor,
    token_ids: np.ndarray,
    k: int,
) -> tuple[np.ndarray, np.ndarray]:
    if token_ids.ndim != 1 or token_ids.size <= k:
        raise ValueError("The selected population must be one-dimensional and exceed k.")
    device = normalized_embeddings.device
    ids_tensor = torch.as_tensor(token_ids, dtype=torch.long, device=device)
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


def directed_edge_arrays(
    token_ids: np.ndarray,
    regions: np.ndarray,
    neighbor_positions: np.ndarray,
    neighbor_scores: np.ndarray,
) -> dict[str, np.ndarray]:
    population_size, k = neighbor_positions.shape
    if neighbor_scores.shape != neighbor_positions.shape:
        raise ValueError("Neighbour positions and scores have different shapes.")
    source_ids = np.repeat(token_ids, k)
    target_ids = token_ids[neighbor_positions.reshape(-1)]
    source_regions = np.repeat(regions, k)
    target_regions = regions[neighbor_positions.reshape(-1)]
    scores = neighbor_scores.reshape(-1)
    ranks = np.tile(np.arange(1, k + 1, dtype=np.int16), population_size)

    if np.any(source_ids == target_ids):
        raise RuntimeError("A self-relation survived exact k-nearest-neighbour exclusion.")
    directed_keys = source_ids.astype(np.int64) * EXPECTED_VOCABULARY_SIZE + target_ids
    reverse_keys = target_ids.astype(np.int64) * EXPECTED_VOCABULARY_SIZE + source_ids
    reciprocal = np.isin(reverse_keys, directed_keys, assume_unique=True)

    positive_positive = (source_regions == "positive_head") & (
        target_regions == "positive_head"
    )
    negative_negative = (source_regions == "negative_tail") & (
        target_regions == "negative_tail"
    )
    region_pair = np.full(source_ids.size, "cross_region", dtype=object)
    region_pair[positive_positive] = "positive_positive"
    region_pair[negative_negative] = "negative_negative"

    return {
        "source_ids": source_ids,
        "target_ids": target_ids,
        "source_regions": source_regions,
        "target_regions": target_regions,
        "scores": scores,
        "ranks": ranks,
        "reciprocal": reciprocal,
        "region_pair": region_pair,
    }


def symmetrized_edges(arrays: dict[str, np.ndarray]) -> pd.DataFrame:
    source_ids = arrays["source_ids"]
    target_ids = arrays["target_ids"]
    frame = pd.DataFrame(
        {
            "token_a": np.minimum(source_ids, target_ids),
            "token_b": np.maximum(source_ids, target_ids),
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


def build_graph(
    token_ids: np.ndarray,
    regions: np.ndarray,
    edges: pd.DataFrame,
) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(
        (int(token_id), {"region": str(region)})
        for token_id, region in zip(token_ids, regions, strict=True)
    )
    graph.add_edges_from(
        (
            int(row.token_a),
            int(row.token_b),
            {"cosine_similarity": float(row.max_cosine_similarity)},
        )
        for row in edges.itertuples(index=False)
    )
    return graph


def sorted_louvain_communities(graph: nx.Graph, state_index: int) -> list[set[int]]:
    communities = nx.community.louvain_communities(
        graph,
        weight=None,
        resolution=LOUVAIN_RESOLUTION,
        seed=RANDOM_SEED + state_index,
    )
    return sorted(
        (set(int(token_id) for token_id in community) for community in communities),
        key=lambda community: (-len(community), min(community)),
    )


def graph_and_community_metrics(
    graph: nx.Graph,
    communities: list[set[int]],
    token_ids: np.ndarray,
    regions: np.ndarray,
    arrays: dict[str, np.ndarray],
) -> tuple[dict[str, float | int], dict[int, int]]:
    components = list(nx.connected_components(graph))
    community_by_token: dict[int, int] = {}
    for community_id, community in enumerate(communities):
        for token_id in community:
            community_by_token[token_id] = community_id

    community_labels = np.array(
        [community_by_token[int(token_id)] for token_id in token_ids], dtype=np.int32
    )
    region_labels = (regions == "positive_head").astype(np.int8)
    pair_types = arrays["region_pair"]
    directed_edge_count = int(arrays["scores"].size)
    metrics: dict[str, float | int] = {
        "population_size": int(token_ids.size),
        "directed_edge_count": directed_edge_count,
        "undirected_edge_count": int(graph.number_of_edges()),
        "mean_knn_cosine": float(np.mean(arrays["scores"])),
        "median_knn_cosine": float(np.median(arrays["scores"])),
        "minimum_knn_cosine": float(np.min(arrays["scores"])),
        "maximum_knn_cosine": float(np.max(arrays["scores"])),
        "same_region_edge_fraction": float(np.mean(pair_types != "cross_region")),
        "positive_positive_edge_fraction": float(
            np.mean(pair_types == "positive_positive")
        ),
        "negative_negative_edge_fraction": float(
            np.mean(pair_types == "negative_negative")
        ),
        "cross_region_edge_fraction": float(np.mean(pair_types == "cross_region")),
        "reciprocal_edge_fraction": float(np.mean(arrays["reciprocal"])),
        "connected_component_count": int(len(components)),
        "largest_component_fraction": float(
            max(len(component) for component in components) / token_ids.size
        ),
        "average_clustering": float(nx.average_clustering(graph)),
        "community_count": int(len(communities)),
        "community_modularity": float(
            nx.community.modularity(graph, communities, weight=None)
        ),
        "community_region_nmi": float(
            normalized_mutual_info_score(region_labels, community_labels)
        ),
    }
    return metrics, community_by_token


def random_graph_metrics(
    regions: np.ndarray,
    arrays: dict[str, np.ndarray],
) -> dict[str, float]:
    pair_types = arrays["region_pair"]
    return {
        "mean_knn_cosine": float(np.mean(arrays["scores"])),
        "median_knn_cosine": float(np.median(arrays["scores"])),
        "same_region_edge_fraction": float(np.mean(pair_types != "cross_region")),
        "positive_positive_edge_fraction": float(
            np.mean(pair_types == "positive_positive")
        ),
        "negative_negative_edge_fraction": float(
            np.mean(pair_types == "negative_negative")
        ),
        "cross_region_edge_fraction": float(np.mean(pair_types == "cross_region")),
        "reciprocal_edge_fraction": float(np.mean(arrays["reciprocal"])),
    }


def community_outputs(
    state_index: int,
    state_type: str,
    state_label: str,
    graph: nx.Graph,
    communities: list[set[int]],
    community_by_token: dict[int, int],
    state_tokens: pd.DataFrame,
) -> tuple[pd.DataFrame, list[dict], nx.Graph, dict[int, str]]:
    indexed = state_tokens.set_index("token_id", drop=False)
    community_sizes = {index: len(nodes) for index, nodes in enumerate(communities)}
    assignments = state_tokens.copy()
    assignments["state_index"] = state_index
    assignments["state_type"] = state_type
    assignments["state_label"] = state_label
    assignments["community_id"] = assignments["token_id"].map(community_by_token)
    assignments["community_size"] = assignments["community_id"].map(community_sizes)
    assignment_columns = [
        "state_index",
        "state_type",
        "state_label",
        "token_id",
        "raw_token",
        "decoded_token",
        "token_class",
        "is_target_lexical_variant",
        "region",
        "cosine_score",
        "community_id",
        "community_size",
    ]
    assignments = assignments[assignment_columns]

    summary_records: list[dict] = []
    labels: dict[int, str] = {}
    community_graph = nx.Graph()
    for community_id, nodes in enumerate(communities):
        node_ids = sorted(nodes)
        positive_count = sum(
            str(indexed.loc[token_id, "region"]) == "positive_head"
            for token_id in node_ids
        )
        degrees = graph.degree(node_ids)
        ranked_ids = sorted(
            node_ids,
            key=lambda token_id: (-int(degrees[token_id]), token_id),
        )
        representative_ids = ranked_ids[:12]
        representatives = [
            visible_token(indexed.loc[token_id, "decoded_token"])
            for token_id in representative_ids
        ]
        induced = graph.subgraph(node_ids)
        representative_text = " | ".join(representatives)
        summary_records.append(
            {
                "state_index": state_index,
                "state_type": state_type,
                "state_label": state_label,
                "community_id": community_id,
                "community_size": len(node_ids),
                "positive_head_count": positive_count,
                "negative_tail_count": len(node_ids) - positive_count,
                "positive_head_fraction": positive_count / len(node_ids),
                "internal_edge_count": induced.number_of_edges(),
                "mean_degree": float(
                    np.mean([graph.degree(token_id) for token_id in node_ids])
                ),
                "representative_token_ids": " ".join(map(str, representative_ids)),
                "representative_tokens": representative_text,
            }
        )
        community_graph.add_node(
            community_id,
            size=len(node_ids),
            positive_fraction=positive_count / len(node_ids),
        )
        labels[community_id] = f"C{community_id}\n" + " ".join(representatives[:2])

    for token_a, token_b in graph.edges():
        community_a = community_by_token[int(token_a)]
        community_b = community_by_token[int(token_b)]
        if community_a == community_b:
            continue
        if community_graph.has_edge(community_a, community_b):
            community_graph[community_a][community_b]["weight"] += 1
        else:
            community_graph.add_edge(community_a, community_b, weight=1)

    return assignments, summary_records, community_graph, labels


def update_persistent_edges(
    accumulator: dict[tuple[int, int], list[float | int]],
    state_index: int,
    edges: pd.DataFrame,
    region_by_token: dict[int, str],
) -> None:
    for row in edges.itertuples(index=False):
        token_a = int(row.token_a)
        token_b = int(row.token_b)
        similarity = float(row.max_cosine_similarity)
        region_a = region_by_token[token_a]
        region_b = region_by_token[token_b]
        pair_index = 2 if region_a != region_b else (0 if region_a == "positive_head" else 1)
        key = (token_a, token_b)
        value = accumulator.get(key)
        if value is None:
            value = [0, 0.0, -math.inf, 0, 0, 0, 0]
            accumulator[key] = value
        value[0] = int(value[0]) + 1
        value[1] = float(value[1]) + similarity
        value[2] = max(float(value[2]), similarity)
        value[3] = int(value[3]) | (1 << state_index)
        value[4 + pair_index] = int(value[4 + pair_index]) + 1


def plot_topology_vs_random(
    comparisons: pd.DataFrame,
    state_labels: dict[int, str],
    output_path: Path,
) -> None:
    display_metrics = (
        ("mean_knn_cosine", "Mean 10-NN cosine"),
        ("same_region_edge_fraction", "Same-region directed-edge fraction"),
        ("reciprocal_edge_fraction", "Reciprocal directed-edge fraction"),
    )
    figure, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=True)
    for axis, (metric, label) in zip(axes, display_metrics, strict=True):
        rows = comparisons.loc[comparisons["metric"] == metric].sort_values(
            "state_index"
        )
        x = rows["state_index"].to_numpy()
        axis.fill_between(
            x,
            rows["random_q025"],
            rows["random_q975"],
            color="#adb5bd",
            alpha=0.35,
            label="Random 2.5–97.5%",
        )
        axis.plot(x, rows["random_mean"], color="#6c757d", label="Random mean")
        axis.plot(
            x,
            rows["observed"],
            color="#d1495b",
            marker="o",
            markersize=3,
            linewidth=1.5,
            label="R004 population",
        )
        axis.set_ylabel(label)
        axis.grid(alpha=0.25)
        axis.legend(loc="best")
    axes[-1].set_xlabel("Recorded state index")
    axes[-1].set_xticks(
        list(state_labels),
        [str(index) for index in state_labels],
    )
    figure.suptitle("R005 observed cutoff populations versus size-matched random populations")
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_transition_stability(transitions: pd.DataFrame, output_path: Path) -> None:
    figure, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    x = transitions["current_state_index"].to_numpy()
    axes[0].plot(x, transitions["combined_membership_jaccard"], label="Combined")
    axes[0].plot(x, transitions["positive_membership_jaccard"], label="Positive")
    axes[0].plot(x, transitions["negative_membership_jaccard"], label="Negative")
    axes[0].set_ylabel("Membership Jaccard")
    axes[0].set_ylim(0, 1)
    axes[0].legend(loc="best")
    axes[0].grid(alpha=0.25)

    axes[1].plot(x, transitions["edge_jaccard"], label="Edge Jaccard")
    axes[1].plot(x, transitions["community_adjusted_rand"], label="Community ARI")
    axes[1].plot(x, transitions["shared_token_region_agreement"], label="Region agreement")
    axes[1].set_ylabel("Adjacent-state stability")
    axes[1].set_xlabel("Current recorded state index")
    axes[1].set_ylim(-0.1, 1)
    axes[1].legend(loc="best")
    axes[1].grid(alpha=0.25)
    figure.suptitle("R005 adjacent-state membership, relationship and community stability")
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_selected_community_networks(
    plot_records: list[dict],
    output_path: Path,
) -> None:
    figure, axes = plt.subplots(1, len(plot_records), figsize=(26, 6))
    for axis, record in zip(axes, plot_records, strict=True):
        graph: nx.Graph = record["graph"]
        labels: dict[int, str] = record["labels"]
        positions = nx.spring_layout(
            graph,
            seed=RANDOM_SEED + int(record["state_index"]),
            weight="weight",
            iterations=100,
        )
        nodes = list(graph.nodes())
        node_sizes = [90 + 25 * math.sqrt(graph.nodes[node]["size"]) for node in nodes]
        node_colors = [graph.nodes[node]["positive_fraction"] for node in nodes]
        edge_weights = [math.log1p(graph[u][v]["weight"]) * 0.35 for u, v in graph.edges()]
        nx.draw_networkx_edges(
            graph,
            positions,
            ax=axis,
            width=edge_weights,
            alpha=0.25,
            edge_color="#495057",
        )
        nx.draw_networkx_nodes(
            graph,
            positions,
            ax=axis,
            node_size=node_sizes,
            node_color=node_colors,
            cmap="coolwarm",
            vmin=0,
            vmax=1,
            linewidths=0.5,
            edgecolors="#343a40",
        )
        largest = sorted(nodes, key=lambda node: -graph.nodes[node]["size"])[:8]
        nx.draw_networkx_labels(
            graph,
            positions,
            labels={node: labels[node] for node in largest},
            font_size=6,
            ax=axis,
        )
        axis.set_title(f"State {record['state_index']}\n{record['state_label']}")
        axis.axis("off")
    scalar = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(0, 1))
    scalar.set_array([])
    figure.colorbar(
        scalar,
        ax=axes.ravel().tolist(),
        shrink=0.65,
        label="Community positive-head fraction",
    )
    figure.suptitle(
        "R005 community-level networks; labels show the eight largest communities"
    )
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def count_gzip_csv_rows(path: Path) -> int:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        return max(sum(1 for _ in handle) - 1, 0)


def run_self_tests() -> None:
    embeddings = torch.tensor(
        [
            [1.0, 0.0, 0.0],
            [0.9, 0.1, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.9, 0.1],
            [0.0, 0.0, 1.0],
        ],
        dtype=torch.float32,
    )
    embeddings = F.normalize(embeddings, p=2, dim=1)
    token_ids = np.arange(5, dtype=np.int64)
    regions = np.array(
        ["positive_head", "positive_head", "negative_tail", "negative_tail", "negative_tail"],
        dtype=object,
    )
    positions, scores = exact_knn(embeddings, token_ids, 2)
    arrays = directed_edge_arrays(token_ids, regions, positions, scores)
    assert positions.shape == (5, 2)
    assert arrays["source_ids"].size == 10
    assert not np.any(arrays["source_ids"] == arrays["target_ids"])
    edges = symmetrized_edges(arrays)
    graph = build_graph(token_ids, regions, edges)
    communities = sorted_louvain_communities(graph, 0)
    metrics, mapping = graph_and_community_metrics(
        graph, communities, token_ids, regions, arrays
    )
    assert int(metrics["directed_edge_count"]) == 10
    assert len(mapping) == 5
    assert jaccard({1, 2}, {2, 3}) == 1 / 3
    print("R005 synthetic self-tests passed.")


def main() -> None:
    validate_run_identity()
    validate_cache_configuration()
    if not SOURCE_RUN_DIR.is_dir():
        raise FileNotFoundError(f"Source run not found: {SOURCE_RUN_DIR}")
    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"R005 pre-run plan not found: {PLAN_PATH}")

    source_manifest_path = SOURCE_RUN_DIR / "manifest.json"
    source_manifest = load_json(source_manifest_path)
    model_id = source_manifest["model"]["id"]
    model_revision = source_manifest["model"]["revision"]
    prompt_hash = source_manifest["input"]["prompt_sha256"]
    model_slug = model_id.rsplit("/", 1)[-1]

    started_at = datetime.now(timezone.utc)
    technical_id = (
        f"{started_at.strftime('%Y%m%dT%H%M%SZ')}_"
        f"{model_slug}_{prompt_hash[:10]}"
    )
    run_id = f"{RUN_NUMBER}_{RUN_NAME}__{technical_id}"
    run_dir = RUNS_DIR / run_id
    figures_dir = run_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=False)

    manifest_path = run_dir / "manifest.json"
    pipeline_path = Path(__file__).resolve()
    required_components = [
        "source_validation",
        "embedding_load",
        "observed_graphs",
        "random_baselines",
        "transition_analysis",
        "communities_and_figures",
        "validation",
    ]
    manifest = {
        "run_number": RUN_NUMBER,
        "run_name": RUN_NAME,
        "run_id": run_id,
        "technical_id": technical_id,
        "source_run": SOURCE_RUN_ID,
        "ultimate_source_run": source_manifest.get("ultimate_source_run"),
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
        "input": source_manifest["input"],
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
            "matplotlib": matplotlib.__version__,
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
            "knn_algorithm": "exact full selected-population matrix",
            "directed_graph": "each selected token points to its 10 nearest selected tokens",
            "undirected_graph": "edge retained when either directed relation exists",
            "undirected_graph_weighting": "unweighted for topology and communities",
            "community_algorithm": "NetworkX Louvain",
            "community_resolution": LOUVAIN_RESOLUTION,
            "random_replicates_per_state": RANDOM_REPLICATES,
            "random_seed": RANDOM_SEED,
            "random_baseline": (
                "sampled without replacement from the exact-target-removed vocabulary; "
                "positive, negative and total counts match each observed state"
            ),
            "selected_figure_states": list(SELECTED_FIGURE_STATES),
            "interpretation_boundary": (
                "Layer-wise changes arise from changing R004 membership inside one fixed "
                "static embedding topology. Communities are geometric graph partitions, "
                "not established topics. The null controls population size only."
            ),
        },
        "source_manifest": {
            "path": str(source_manifest_path.relative_to(PROJECT_DIR)).replace("\\", "/"),
            "sha256": sha256_file(source_manifest_path),
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
        if source_manifest.get("status") != "successful":
            raise RuntimeError("R004 source manifest is not successful.")
        if source_manifest.get("run_id") != SOURCE_RUN_ID:
            raise RuntimeError("R004 source manifest identity does not match the plan.")
        if source_manifest.get("ultimate_source_run") != EXPECTED_ULTIMATE_SOURCE_RUN_ID:
            raise RuntimeError("R004 ultimate source run does not match the plan.")
        if prompt_hash != EXPECTED_PROMPT_SHA256:
            raise RuntimeError("R004 prompt hash does not match the plan.")
        if int(source_manifest["input"]["target_token_id"]) != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("R004 target token does not match the plan.")
        if model_revision != EXPECTED_MODEL_REVISION:
            raise RuntimeError("R004 model revision does not match the plan.")
        if int(source_manifest["results"]["state_count"]) != EXPECTED_STATE_COUNT:
            raise RuntimeError("R004 state count does not match the plan.")
        if int(source_manifest["results"]["valid_vocabulary_size"]) != EXPECTED_VOCABULARY_SIZE:
            raise RuntimeError("R004 vocabulary size does not match the plan.")

        for relative_path in REQUIRED_SOURCE_ARTIFACTS:
            expected = source_manifest["artifacts"][relative_path]
            source_path = SOURCE_RUN_DIR / relative_path
            if not source_path.is_file():
                raise FileNotFoundError(f"Missing R004 source artifact: {source_path}")
            if source_path.stat().st_size != expected["bytes"]:
                raise RuntimeError(f"R004 artifact size mismatch: {relative_path}")
            if sha256_file(source_path) != expected["sha256"]:
                raise RuntimeError(f"R004 artifact hash mismatch: {relative_path}")
            manifest["source_artifacts"][relative_path] = expected

        cutoffs = pd.read_csv(SOURCE_RUN_DIR / "cutoffs.csv")
        tails = pd.read_csv(SOURCE_RUN_DIR / "tail_tokens.csv.gz")
        if len(cutoffs) != EXPECTED_STATE_COUNT:
            raise RuntimeError("R004 cutoff table does not contain all 33 states.")
        if len(tails) != EXPECTED_TAIL_ROWS:
            raise RuntimeError("R004 tail-membership row count does not match the plan.")
        if tails.duplicated(["state_index", "token_id"]).any():
            raise RuntimeError("R004 tail memberships contain duplicate state-token rows.")
        if set(tails["region"].unique()) != {"positive_head", "negative_tail"}:
            raise RuntimeError("R004 tail memberships contain an unexpected region.")
        if (tails["token_id"] == EXPECTED_TARGET_TOKEN_ID).any():
            raise RuntimeError("The exact target token appears in R004 tail membership.")
        observed_counts = tails.groupby(["state_index", "region"]).size().unstack(fill_value=0)
        observed_counts = observed_counts.reindex(range(EXPECTED_STATE_COUNT), fill_value=0)
        if not np.array_equal(
            observed_counts["positive_head"].to_numpy(),
            cutoffs["positive_head_count"].to_numpy(),
        ):
            raise RuntimeError("R004 positive-head counts do not reconcile.")
        if not np.array_equal(
            observed_counts["negative_tail"].to_numpy(),
            cutoffs["negative_tail_count"].to_numpy(),
        ):
            raise RuntimeError("R004 negative-tail counts do not reconcile.")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "validated_source_artifact_count": len(REQUIRED_SOURCE_ARTIFACTS),
                "state_count": EXPECTED_STATE_COUNT,
                "tail_membership_rows": len(tails),
            }
        )
        write_manifest()
        print("R005 source validation complete.", flush=True)

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
            raise RuntimeError("Cached tokenizer vocabulary size does not match R004.")
        index_path = snapshot_path / "model.safetensors.index.json"
        index_data = load_json(index_path)
        shard_name = index_data["weight_map"].get(EMBEDDING_WEIGHT_NAME)
        if not shard_name:
            raise KeyError(f"Embedding weight not found: {EMBEDDING_WEIGHT_NAME}")
        shard_path = snapshot_path / shard_name
        with safe_open(shard_path, framework="pt", device="cpu") as handle:
            embedding_matrix = handle.get_tensor(EMBEDDING_WEIGHT_NAME)
        if embedding_matrix.shape[0] < EXPECTED_VOCABULARY_SIZE:
            raise RuntimeError("Embedding matrix has fewer rows than the tokenizer.")
        embedding_matrix = embedding_matrix[:EXPECTED_VOCABULARY_SIZE]
        if embedding_matrix.ndim != 2 or embedding_matrix.shape[1] != 4096:
            raise RuntimeError("Embedding matrix has an unexpected shape.")
        if not torch.isfinite(embedding_matrix).all():
            raise RuntimeError("Embedding matrix contains non-finite values.")
        row_norms = torch.linalg.vector_norm(embedding_matrix.float(), dim=1)
        if torch.any(row_norms == 0):
            raise RuntimeError("Embedding matrix contains a zero-norm row.")

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if device.type != "cuda":
            raise RuntimeError("R005 exact graph run requires the configured CUDA GPU.")
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        normalized_embeddings = F.normalize(
            embedding_matrix.to(device=device, dtype=torch.float32), p=2, dim=1
        )
        del embedding_matrix, row_norms
        gc.collect()
        if not torch.isfinite(normalized_embeddings).all():
            raise RuntimeError("Normalized embedding matrix contains non-finite values.")
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
            f"R005 embedding load complete: {tuple(normalized_embeddings.shape)} on {device}.",
            flush=True,
        )

        state_metrics_path = run_dir / "state_topology_metrics.csv"
        random_path = run_dir / "random_baseline_metrics.csv"
        comparison_path = run_dir / "observed_vs_random.csv"
        edges_path = run_dir / "knn_edges.csv.gz"
        assignments_path = run_dir / "community_assignments.csv.gz"
        community_summary_path = run_dir / "community_summary.csv"
        transitions_path = run_dir / "state_transitions.csv"
        persistent_path = run_dir / "persistent_edges.csv.gz"
        findings_path = run_dir / "findings.md"
        topology_figure_path = figures_dir / "topology_vs_random.png"
        transitions_figure_path = figures_dir / "transition_stability.png"
        communities_figure_path = figures_dir / "selected_state_community_networks.png"

        current_component = "observed_graphs"
        component_started = time.perf_counter()
        state_metrics_records: list[dict] = []
        community_summary_records: list[dict] = []
        transition_records: list[dict] = []
        persistent_accumulator: dict[tuple[int, int], list[float | int]] = {}
        plot_records: list[dict] = []
        previous: dict | None = None
        edge_rows_written = 0
        assignment_rows_written = 0

        with gzip.open(edges_path, "wt", encoding="utf-8", newline="") as edge_handle, gzip.open(
            assignments_path, "wt", encoding="utf-8", newline=""
        ) as assignment_handle:
            for state_index in range(EXPECTED_STATE_COUNT):
                state_started = time.perf_counter()
                state_row = cutoffs.loc[cutoffs["state_index"] == state_index].iloc[0]
                state_tokens = (
                    tails.loc[tails["state_index"] == state_index]
                    .sort_values("token_id", kind="stable")
                    .reset_index(drop=True)
                )
                token_ids = state_tokens["token_id"].to_numpy(dtype=np.int64)
                regions = state_tokens["region"].to_numpy(dtype=object)
                expected_population = int(state_row["combined_tail_count"])
                if token_ids.size != expected_population:
                    raise RuntimeError(
                        f"State {state_index} population does not match R004 cutoff counts."
                    )
                positions, scores = exact_knn(normalized_embeddings, token_ids, K_NEIGHBORS)
                arrays = directed_edge_arrays(token_ids, regions, positions, scores)
                sym_edges = symmetrized_edges(arrays)
                graph = build_graph(token_ids, regions, sym_edges)
                communities = sorted_louvain_communities(graph, state_index)
                graph_metrics, community_by_token = graph_and_community_metrics(
                    graph, communities, token_ids, regions, arrays
                )
                graph_metrics.update(
                    {
                        "state_index": state_index,
                        "state_type": str(state_row["state_type"]),
                        "state_label": str(state_row["state_label"]),
                        "positive_head_count": int(
                            np.sum(regions == "positive_head")
                        ),
                        "negative_tail_count": int(
                            np.sum(regions == "negative_tail")
                        ),
                    }
                )
                state_metrics_records.append(graph_metrics)

                edge_frame = pd.DataFrame(
                    {
                        "state_index": state_index,
                        "state_type": str(state_row["state_type"]),
                        "state_label": str(state_row["state_label"]),
                        "source_token_id": arrays["source_ids"],
                        "target_token_id": arrays["target_ids"],
                        "neighbor_rank": arrays["ranks"],
                        "cosine_similarity": arrays["scores"],
                        "source_region": arrays["source_regions"],
                        "target_region": arrays["target_regions"],
                        "region_pair": arrays["region_pair"],
                        "reciprocal": arrays["reciprocal"],
                    }
                )
                edge_frame.to_csv(
                    edge_handle,
                    index=False,
                    header=edge_rows_written == 0,
                )
                edge_rows_written += len(edge_frame)

                assignments, summaries, community_graph, plot_labels = community_outputs(
                    state_index,
                    str(state_row["state_type"]),
                    str(state_row["state_label"]),
                    graph,
                    communities,
                    community_by_token,
                    state_tokens,
                )
                assignments.to_csv(
                    assignment_handle,
                    index=False,
                    header=assignment_rows_written == 0,
                )
                assignment_rows_written += len(assignments)
                community_summary_records.extend(summaries)

                region_by_token = dict(
                    zip(token_ids.tolist(), regions.tolist(), strict=True)
                )
                update_persistent_edges(
                    persistent_accumulator,
                    state_index,
                    sym_edges,
                    region_by_token,
                )

                selected_set = set(map(int, token_ids))
                positive_set = set(
                    map(int, token_ids[regions == "positive_head"])
                )
                negative_set = set(
                    map(int, token_ids[regions == "negative_tail"])
                )
                edge_set = set(
                    zip(
                        sym_edges["token_a"].astype(int),
                        sym_edges["token_b"].astype(int),
                        strict=True,
                    )
                )
                if previous is not None:
                    shared_tokens = selected_set & previous["selected_set"]
                    previous_labels = [
                        previous["community_by_token"][token_id]
                        for token_id in sorted(shared_tokens)
                    ]
                    current_labels = [
                        community_by_token[token_id]
                        for token_id in sorted(shared_tokens)
                    ]
                    region_agreement = np.mean(
                        [
                            previous["region_by_token"][token_id]
                            == region_by_token[token_id]
                            for token_id in shared_tokens
                        ]
                    )
                    retained_edges = previous["edge_set"] & edge_set
                    transition_records.append(
                        {
                            "previous_state_index": state_index - 1,
                            "current_state_index": state_index,
                            "previous_state_label": previous["state_label"],
                            "current_state_label": str(state_row["state_label"]),
                            "shared_token_count": len(shared_tokens),
                            "combined_membership_jaccard": jaccard(
                                previous["selected_set"], selected_set
                            ),
                            "positive_membership_jaccard": jaccard(
                                previous["positive_set"], positive_set
                            ),
                            "negative_membership_jaccard": jaccard(
                                previous["negative_set"], negative_set
                            ),
                            "shared_token_region_agreement": float(region_agreement),
                            "previous_edge_count": len(previous["edge_set"]),
                            "current_edge_count": len(edge_set),
                            "retained_edge_count": len(retained_edges),
                            "new_edge_count": len(edge_set - previous["edge_set"]),
                            "disappeared_edge_count": len(
                                previous["edge_set"] - edge_set
                            ),
                            "edge_jaccard": jaccard(previous["edge_set"], edge_set),
                            "community_adjusted_rand": float(
                                adjusted_rand_score(previous_labels, current_labels)
                            ),
                        }
                    )
                previous = {
                    "state_label": str(state_row["state_label"]),
                    "selected_set": selected_set,
                    "positive_set": positive_set,
                    "negative_set": negative_set,
                    "edge_set": edge_set,
                    "community_by_token": community_by_token,
                    "region_by_token": region_by_token,
                }
                if state_index in SELECTED_FIGURE_STATES:
                    plot_records.append(
                        {
                            "state_index": state_index,
                            "state_label": str(state_row["state_label"]),
                            "graph": community_graph,
                            "labels": plot_labels,
                        }
                    )
                del positions, scores, arrays, sym_edges, graph, edge_frame, assignments
                print(
                    f"R005 observed state {state_index:02d}/32 complete "
                    f"({token_ids.size} tokens, {time.perf_counter() - state_started:.1f}s).",
                    flush=True,
                )

        state_metrics = pd.DataFrame(state_metrics_records).sort_values("state_index")
        state_metrics.to_csv(state_metrics_path, index=False)
        community_summary = pd.DataFrame(community_summary_records).sort_values(
            ["state_index", "community_id"]
        )
        community_summary.to_csv(community_summary_path, index=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "state_count": len(state_metrics),
                "directed_edge_rows": edge_rows_written,
                "community_assignment_rows": assignment_rows_written,
                "community_rows": len(community_summary),
            }
        )
        write_manifest()

        current_component = "random_baselines"
        component_started = time.perf_counter()
        rng = np.random.default_rng(RANDOM_SEED)
        valid_ids = np.delete(
            np.arange(EXPECTED_VOCABULARY_SIZE, dtype=np.int64),
            EXPECTED_TARGET_TOKEN_ID,
        )
        random_records: list[dict] = []
        for state_index in range(EXPECTED_STATE_COUNT):
            state_started = time.perf_counter()
            observed = state_metrics.loc[
                state_metrics["state_index"] == state_index
            ].iloc[0]
            positive_count = int(observed["positive_head_count"])
            negative_count = int(observed["negative_tail_count"])
            population_size = positive_count + negative_count
            random_regions = np.array(
                ["positive_head"] * positive_count
                + ["negative_tail"] * negative_count,
                dtype=object,
            )
            for replicate in range(RANDOM_REPLICATES):
                random_ids = rng.choice(
                    valid_ids,
                    size=population_size,
                    replace=False,
                    shuffle=True,
                )
                positions, scores = exact_knn(
                    normalized_embeddings, random_ids, K_NEIGHBORS
                )
                arrays = directed_edge_arrays(
                    random_ids, random_regions, positions, scores
                )
                metrics = random_graph_metrics(random_regions, arrays)
                metrics.update(
                    {
                        "state_index": state_index,
                        "state_label": str(observed["state_label"]),
                        "replicate": replicate,
                        "seed": RANDOM_SEED,
                        "population_size": population_size,
                        "positive_head_count": positive_count,
                        "negative_tail_count": negative_count,
                    }
                )
                random_records.append(metrics)
                del positions, scores, arrays
            print(
                f"R005 random baseline state {state_index:02d}/32 complete "
                f"({RANDOM_REPLICATES} replicates, {time.perf_counter() - state_started:.1f}s).",
                flush=True,
            )

        random_metrics = pd.DataFrame(random_records).sort_values(
            ["state_index", "replicate"]
        )
        random_metrics.to_csv(random_path, index=False)
        comparison_records: list[dict] = []
        for state_index in range(EXPECTED_STATE_COUNT):
            observed = state_metrics.loc[
                state_metrics["state_index"] == state_index
            ].iloc[0]
            baseline = random_metrics.loc[random_metrics["state_index"] == state_index]
            for metric in COMPARISON_METRICS:
                values = baseline[metric].to_numpy(dtype=float)
                observed_value = float(observed[metric])
                random_mean = float(np.mean(values))
                random_std = float(np.std(values, ddof=1))
                comparison_records.append(
                    {
                        "state_index": state_index,
                        "state_label": str(observed["state_label"]),
                        "metric": metric,
                        "observed": observed_value,
                        "random_mean": random_mean,
                        "random_std": random_std,
                        "random_q025": float(np.quantile(values, 0.025)),
                        "random_q975": float(np.quantile(values, 0.975)),
                        "observed_minus_random_mean": observed_value - random_mean,
                        "z_score": (
                            (observed_value - random_mean) / random_std
                            if random_std > 0
                            else np.nan
                        ),
                        "empirical_p_greater_equal": float(
                            (1 + np.sum(values >= observed_value))
                            / (RANDOM_REPLICATES + 1)
                        ),
                    }
                )
        comparisons = pd.DataFrame(comparison_records)
        comparisons.to_csv(comparison_path, index=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "replicates_per_state": RANDOM_REPLICATES,
                "random_population_rows": len(random_metrics),
                "comparison_rows": len(comparisons),
            }
        )
        write_manifest()

        current_component = "transition_analysis"
        component_started = time.perf_counter()
        transitions = pd.DataFrame(transition_records).sort_values(
            "current_state_index"
        )
        transitions.to_csv(transitions_path, index=False)

        token_metadata = (
            tails.sort_values(["token_id", "state_index"], kind="stable")
            .drop_duplicates("token_id")
            .set_index("token_id", drop=False)
        )
        persistent_records: list[dict] = []
        for (token_a, token_b), values in persistent_accumulator.items():
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
                    "token_a": token_a,
                    "token_a_decoded": token_metadata.loc[token_a, "decoded_token"],
                    "token_b": token_b,
                    "token_b_decoded": token_metadata.loc[token_b, "decoded_token"],
                    "state_count": state_count,
                    "state_fraction": state_count / EXPECTED_STATE_COUNT,
                    "first_state_index": state_indices[0],
                    "last_state_index": state_indices[-1],
                    "state_indices": " ".join(map(str, state_indices)),
                    "mean_cosine_similarity": float(values[1]) / state_count,
                    "maximum_cosine_similarity": float(values[2]),
                    "positive_positive_state_count": int(values[4]),
                    "negative_negative_state_count": int(values[5]),
                    "cross_region_state_count": int(values[6]),
                }
            )
        persistent_edges = pd.DataFrame(persistent_records)
        if persistent_edges.empty:
            raise RuntimeError("No relationship appeared in at least two states.")
        persistent_edges = persistent_edges.sort_values(
            ["state_count", "mean_cosine_similarity", "token_a", "token_b"],
            ascending=[False, False, True, True],
        )
        persistent_edges.to_csv(persistent_path, index=False, compression="gzip")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "adjacent_transition_rows": len(transitions),
                "persistent_edge_rows": len(persistent_edges),
                "minimum_persistent_state_count": 2,
            }
        )
        write_manifest()

        current_component = "communities_and_figures"
        component_started = time.perf_counter()
        state_labels = dict(
            zip(
                state_metrics["state_index"].astype(int),
                state_metrics["state_label"].astype(str),
                strict=True,
            )
        )
        plot_topology_vs_random(comparisons, state_labels, topology_figure_path)
        plot_transition_stability(transitions, transitions_figure_path)
        plot_selected_community_networks(plot_records, communities_figure_path)

        similarity_comparison = comparisons.loc[
            comparisons["metric"] == "mean_knn_cosine"
        ].copy()
        same_region_comparison = comparisons.loc[
            comparisons["metric"] == "same_region_edge_fraction"
        ].copy()
        strongest_similarity = similarity_comparison.loc[
            similarity_comparison["observed_minus_random_mean"].idxmax()
        ]
        weakest_similarity = similarity_comparison.loc[
            similarity_comparison["observed_minus_random_mean"].idxmin()
        ]
        strongest_separation = same_region_comparison.loc[
            same_region_comparison["observed_minus_random_mean"].idxmax()
        ]
        top_persistent = persistent_edges.head(10)
        top_relationship_lines = [
            (
                f"- `{visible_token(row.token_a_decoded)}` ↔ "
                f"`{visible_token(row.token_b_decoded)}`: {int(row.state_count)}/33 "
                f"states, mean cosine {float(row.mean_cosine_similarity):.4f}."
            )
            for row in top_persistent.itertuples(index=False)
        ]
        findings_text = "\n".join(
            [
                "# R005 findings: cutoff-population topology baseline",
                "",
                "## Direct observations",
                "",
                f"- All {EXPECTED_STATE_COUNT} R004 populations produced exact "
                f"{K_NEIGHBORS}-nearest-neighbour graphs.",
                f"- Observed mean nearest-neighbour cosine exceeded the 97.5th "
                f"percentile of the size-matched random baseline at "
                f"{int((similarity_comparison['observed'] > similarity_comparison['random_q975']).sum())} "
                f"of {EXPECTED_STATE_COUNT} states.",
                f"- Observed same-region edge fraction exceeded the random 97.5th "
                f"percentile at "
                f"{int((same_region_comparison['observed'] > same_region_comparison['random_q975']).sum())} "
                f"of {EXPECTED_STATE_COUNT} states.",
                f"- The largest mean-neighbour-cosine excess occurred at state "
                f"{int(strongest_similarity['state_index'])} "
                f"(`{strongest_similarity['state_label']}`): "
                f"{float(strongest_similarity['observed_minus_random_mean']):.6f}.",
                f"- The smallest mean-neighbour-cosine excess occurred at state "
                f"{int(weakest_similarity['state_index'])} "
                f"(`{weakest_similarity['state_label']}`): "
                f"{float(weakest_similarity['observed_minus_random_mean']):.6f}.",
                f"- The largest same-region-edge excess occurred at state "
                f"{int(strongest_separation['state_index'])} "
                f"(`{strongest_separation['state_label']}`): "
                f"{float(strongest_separation['observed_minus_random_mean']):.6f}.",
                f"- Median adjacent-state combined membership Jaccard was "
                f"{float(transitions['combined_membership_jaccard'].median()):.4f}; "
                f"median edge Jaccard was {float(transitions['edge_jaccard'].median()):.4f}; "
                f"median community adjusted Rand index was "
                f"{float(transitions['community_adjusted_rand'].median()):.4f}.",
                f"- Louvain community count ranged from "
                f"{int(state_metrics['community_count'].min())} to "
                f"{int(state_metrics['community_count'].max())}; modularity ranged "
                f"from {float(state_metrics['community_modularity'].min()):.4f} to "
                f"{float(state_metrics['community_modularity'].max()):.4f}.",
                f"- {len(persistent_edges):,} undirected relationships appeared "
                "in at least two states.",
                "",
                "## Most persistent observed relationships",
                "",
                *top_relationship_lines,
                "",
                "## Supported conclusion",
                "",
                "R004's selected populations can be tested as relationship networks. "
                "Differences from the size-matched null establish geometric organization "
                "relative to that null; they do not establish semantic topics, contextual "
                "evolution of every vocabulary token, an optimal layer or causal conflict.",
                "",
                "## Limitations",
                "",
                "- The input-embedding geometry is fixed across all states; only selected "
                "membership changes.",
                "- The null controls positive, negative and total population sizes only. "
                "It does not control token class, morphology, frequency or score rank.",
                "- Louvain communities are state-local geometric partitions. Community IDs "
                "are not persistent topic identities.",
                "- Twenty null replicates give a minimum one-sided empirical p-value of "
                "1/21 ≈ 0.0476 and are suitable only for this proof of concept.",
            ]
        )
        findings_path.write_text(findings_text + "\n", encoding="utf-8")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "selected_figure_states": list(SELECTED_FIGURE_STATES),
                "figure_count": 3,
                "findings_report_written": True,
            }
        )
        write_manifest()

        current_component = "validation"
        component_started = time.perf_counter()
        artifact_paths = [
            state_metrics_path,
            random_path,
            comparison_path,
            edges_path,
            assignments_path,
            community_summary_path,
            transitions_path,
            persistent_path,
            findings_path,
            topology_figure_path,
            transitions_figure_path,
            communities_figure_path,
        ]
        if len(state_metrics) != EXPECTED_STATE_COUNT:
            raise RuntimeError("State topology metrics do not cover all states.")
        if len(random_metrics) != EXPECTED_STATE_COUNT * RANDOM_REPLICATES:
            raise RuntimeError("Random baseline does not have the required row count.")
        if len(comparisons) != EXPECTED_STATE_COUNT * len(COMPARISON_METRICS):
            raise RuntimeError("Observed-versus-random table has the wrong row count.")
        if len(transitions) != EXPECTED_STATE_COUNT - 1:
            raise RuntimeError("Transition table does not cover all adjacent states.")
        expected_edge_rows = int(state_metrics["population_size"].sum()) * K_NEIGHBORS
        if edge_rows_written != expected_edge_rows:
            raise RuntimeError("In-memory directed edge count does not reconcile.")
        if count_gzip_csv_rows(edges_path) != expected_edge_rows:
            raise RuntimeError("Persisted directed edge count does not reconcile.")
        if assignment_rows_written != EXPECTED_TAIL_ROWS:
            raise RuntimeError("In-memory community assignment count does not reconcile.")
        persisted_assignment_rows = len(
            pd.read_csv(assignments_path, usecols=["state_index"])
        )
        if persisted_assignment_rows != EXPECTED_TAIL_ROWS:
            raise RuntimeError("Persisted community assignment count does not reconcile.")
        if not (
            state_metrics["directed_edge_count"]
            == state_metrics["population_size"] * K_NEIGHBORS
        ).all():
            raise RuntimeError("A state graph has the wrong directed edge count.")
        finite_state_columns = [
            "mean_knn_cosine",
            "same_region_edge_fraction",
            "reciprocal_edge_fraction",
            "largest_component_fraction",
            "average_clustering",
            "community_modularity",
            "community_region_nmi",
        ]
        if not np.isfinite(state_metrics[finite_state_columns].to_numpy()).all():
            raise RuntimeError("State topology metrics contain non-finite values.")
        if not np.isfinite(
            random_metrics[list(COMPARISON_METRICS)].to_numpy()
        ).all():
            raise RuntimeError("Random baseline metrics contain non-finite values.")
        if not np.isfinite(
            comparisons[
                [
                    "observed",
                    "random_mean",
                    "random_std",
                    "random_q025",
                    "random_q975",
                    "z_score",
                    "empirical_p_greater_equal",
                ]
            ].to_numpy()
        ).all():
            raise RuntimeError("Observed-versus-random metrics contain non-finite values.")
        for path in artifact_paths:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"Required R005 artifact is absent or empty: {path}")

        torch.cuda.synchronize()
        peak_gpu_bytes = int(torch.cuda.max_memory_allocated())
        manifest["artifacts"] = {
            str(path.relative_to(run_dir)).replace("\\", "/"): artifact_record(path)
            for path in artifact_paths
        }
        manifest["results"] = {
            "state_count": EXPECTED_STATE_COUNT,
            "valid_vocabulary_size": EXPECTED_VOCABULARY_SIZE,
            "knn_k": K_NEIGHBORS,
            "observed_population_rows": EXPECTED_TAIL_ROWS,
            "directed_edge_rows": edge_rows_written,
            "community_assignment_rows": assignment_rows_written,
            "community_summary_rows": len(community_summary),
            "random_baseline_rows": len(random_metrics),
            "comparison_rows": len(comparisons),
            "transition_rows": len(transitions),
            "persistent_edge_rows": len(persistent_edges),
            "states_above_random_similarity_q975": int(
                (
                    similarity_comparison["observed"]
                    > similarity_comparison["random_q975"]
                ).sum()
            ),
            "states_above_random_same_region_q975": int(
                (
                    same_region_comparison["observed"]
                    > same_region_comparison["random_q975"]
                ).sum()
            ),
            "median_adjacent_membership_jaccard": float(
                transitions["combined_membership_jaccard"].median()
            ),
            "median_adjacent_edge_jaccard": float(
                transitions["edge_jaccard"].median()
            ),
            "median_adjacent_community_ari": float(
                transitions["community_adjusted_rand"].median()
            ),
            "peak_gpu_memory_bytes": peak_gpu_bytes,
        }
        add_component_success(manifest, current_component, component_started)
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now_iso()
        write_manifest()

        print(f"Run:                    {run_id}", flush=True)
        print(f"Status:                 {manifest['status']}", flush=True)
        print(f"Source run:             {SOURCE_RUN_ID}", flush=True)
        print(f"Observed graph states:  {len(state_metrics)}", flush=True)
        print(f"Directed edge rows:     {edge_rows_written}", flush=True)
        print(f"Random baseline rows:   {len(random_metrics)}", flush=True)
        print(f"Persistent edges:       {len(persistent_edges)}", flush=True)
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
        description="R005 cutoff-population static-topology baseline"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run synthetic validation without creating an R005 run directory.",
    )
    arguments = parser.parse_args()
    if arguments.self_test:
        run_self_tests()
    else:
        main()
