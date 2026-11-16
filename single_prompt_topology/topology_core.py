"""Model-independent semantic-topology calculations with explicit settings.

This module preserves the R012-R017 measurement method while removing the
module-global configuration used by the historical runners.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass

import networkx as nx
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import adjusted_rand_score


@dataclass(frozen=True)
class TopologySettings:
    state_count: int
    layer_count: int
    k_neighbors: int = 10
    knn_batch_size: int = 512
    random_seed: int = 20261115
    louvain_resolution: float = 1.0
    device: str = "cuda"


def state_label(state_index: int, settings: TopologySettings) -> str:
    if not 0 <= state_index < settings.state_count:
        raise ValueError(f"State index {state_index} is out of range.")
    if state_index == 0:
        return "input_embedding"
    if state_index == settings.state_count - 1:
        return f"final_norm_after_block_{settings.layer_count - 1}"
    return f"block_{state_index - 1}_output"


def visible_token(value: object) -> str:
    text = str(value)
    return (
        text.replace(" ", "␠")
        .replace("\n", "␤")
        .replace("\r", "␍")
        .replace("\t", "⇥")
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


def elbow_candidate(sorted_values: np.ndarray) -> dict[str, float | int | None]:
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
    settings: TopologySettings,
) -> tuple[np.ndarray, np.ndarray]:
    if token_ids.ndim != 1 or token_ids.size <= settings.k_neighbors:
        raise ValueError("Selected population must exceed the neighbour count.")
    ids = torch.as_tensor(token_ids, dtype=torch.long, device=settings.device)
    with torch.inference_mode():
        selected = normalized_embeddings.index_select(0, ids)
        all_positions: list[torch.Tensor] = []
        all_values: list[torch.Tensor] = []
        for start in range(0, token_ids.size, settings.knn_batch_size):
            stop = min(start + settings.knn_batch_size, token_ids.size)
            similarities = selected[start:stop] @ selected.transpose(0, 1)
            local_rows = torch.arange(stop - start, device=settings.device)
            similarities[local_rows, torch.arange(start, stop, device=settings.device)] = -torch.inf
            values, positions = torch.topk(
                similarities,
                k=settings.k_neighbors,
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
    settings: TopologySettings,
) -> tuple[list[set[int]], dict[int, int]]:
    seed = settings.random_seed + state_index * 2 + side_index
    communities = nx.community.louvain_communities(
        graph,
        weight=None,
        resolution=settings.louvain_resolution,
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
    **identity: object,
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
    records: list[dict] = []
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


def compare_state_data(source: dict, target: dict) -> dict[str, float | int | None]:
    shared = source["membership"] & target["membership"]
    ordered = sorted(shared)
    source_labels = [source["community_by_token"][token] for token in ordered]
    target_labels = [target["community_by_token"][token] for token in ordered]
    ari = float(adjusted_rand_score(source_labels, target_labels)) if ordered else None
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
    prompt_id: str,
    prompt_index: int,
    state_index: int,
    side: str,
    side_index: int,
    state_tokens: pd.DataFrame,
    normalized_embeddings: torch.Tensor,
    vocabulary_size: int,
    settings: TopologySettings,
) -> tuple[dict, pd.DataFrame, pd.DataFrame, list[dict], list[dict], dict, dict]:
    del prompt_index  # Retained in the explicit interface for stable caller identity.
    label = state_label(state_index, settings)
    state_tokens = state_tokens.sort_values("token_id", kind="stable").reset_index(drop=True)
    token_ids = state_tokens["token_id"].to_numpy(dtype=np.int64, copy=True)
    positions, scores = exact_knn(normalized_embeddings, token_ids, settings)
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
        graph, state_index, side_index, settings
    )
    if set(community_by_token) != set(map(int, token_ids)):
        raise RuntimeError("Community mapping does not cover the network population.")
    components = list(nx.connected_components(graph))
    metric = {
        "prompt_id": prompt_id,
        "state_index": state_index,
        "state_label": label,
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
        "community_modularity": float(nx.community.modularity(graph, communities, weight=None)),
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
            "prompt_id": prompt_id,
            "state_index": state_index,
            "state_label": label,
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
            "prompt_id": prompt_id,
            "state_index": state_index,
            "state_label": label,
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
                "prompt_id": prompt_id,
                "state_index": state_index,
                "state_label": label,
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
                    key: value
                    for key, value in record.items()
                    if key not in {"prompt_id", "state_index", "state_label", "side"}
                }
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
        "prompt_id": prompt_id,
        "state_index": state_index,
        "state_label": label,
        "side": side,
        "metrics": {
            key: value
            for key, value in metric.items()
            if key not in {"prompt_id", "state_index", "state_label", "side"}
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
