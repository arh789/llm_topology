"""Regression-check the generic core against one frozen R017 network."""

from __future__ import annotations

import gc
import json
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from safetensors import safe_open

from topology_core import TopologySettings, analyze_network


PIPELINE_DIR = Path(__file__).resolve().parent
RUN_DIR = (
    PIPELINE_DIR
    / "runs"
    / "R017_olmo3-choke-point-barrier-spear-semantic-map"
)
SNAPSHOT_DIR = (
    Path(r"D:\AI\cache\huggingface\hub\models--allenai--Olmo-3-1125-32B")
    / "snapshots"
    / "c2b61dae89a1ad10e4ad5653d0e46b590902607b"
)
EMBEDDING_KEY = "model.embed_tokens.weight"
VOCABULARY_SIZE = 100278


@unittest.skipUnless(torch.cuda.is_available(), "CUDA required for R017 regression")
class FrozenR017Regression(unittest.TestCase):
    def test_state_01_negative_network_matches(self) -> None:
        index = json.loads(
            (SNAPSHOT_DIR / "model.safetensors.index.json").read_text(encoding="utf-8")
        )
        shard = SNAPSHOT_DIR / index["weight_map"][EMBEDDING_KEY]
        with safe_open(str(shard), framework="pt", device="cpu") as handle:
            embeddings = handle.get_tensor(EMBEDDING_KEY)[:VOCABULARY_SIZE]
        normalized = F.normalize(embeddings.to("cuda", dtype=torch.float32), p=2, dim=1)

        memberships = pd.read_csv(RUN_DIR / "tail_tokens.csv.gz")
        state_tokens = memberships.loc[
            (memberships["state_index"] == 1)
            & (memberships["side"] == "negative_tail")
        ].rename(columns={"prompt": "prompt_id"})
        settings = TopologySettings(
            state_count=65,
            layer_count=64,
            k_neighbors=10,
            knn_batch_size=512,
            random_seed=20261115,
            louvain_resolution=1.0,
        )
        metric, nodes, _edges, communities, _community_edges, _state_data, _compact = (
            analyze_network(
                "primary",
                0,
                1,
                "negative_tail",
                1,
                state_tokens,
                normalized,
                VOCABULARY_SIZE,
                settings,
            )
        )
        expected_metric = pd.read_csv(RUN_DIR / "network_index.csv").loc[
            lambda frame: (frame["state_index"] == 1)
            & (frame["side"] == "negative_tail")
        ].iloc[0]
        for key in (
            "population_size",
            "directed_edge_count",
            "undirected_edge_count",
            "community_count",
        ):
            self.assertEqual(metric[key], int(expected_metric[key]))
        for key in (
            "community_modularity",
            "mean_knn_cosine",
            "reciprocal_edge_fraction",
        ):
            self.assertTrue(np.isclose(metric[key], float(expected_metric[key])))

        expected_nodes = pd.read_csv(RUN_DIR / "nodes.csv.gz").loc[
            lambda frame: (frame["state_index"] == 1)
            & (frame["side"] == "negative_tail"),
            ["token_id", "community_id"],
        ].sort_values("token_id")
        actual_nodes = nodes[["token_id", "community_id"]].sort_values("token_id")
        pd.testing.assert_frame_equal(
            actual_nodes.reset_index(drop=True),
            expected_nodes.reset_index(drop=True),
            check_dtype=False,
        )
        expected_communities = pd.read_csv(RUN_DIR / "community_nodes.csv").loc[
            lambda frame: (frame["state_index"] == 1)
            & (frame["side"] == "negative_tail"),
            ["community_id", "community_size", "representative_token_ids"],
        ].sort_values("community_id")
        actual_communities = pd.DataFrame(communities)[
            ["community_id", "community_size", "representative_token_ids"]
        ].sort_values("community_id")
        pd.testing.assert_frame_equal(
            actual_communities.reset_index(drop=True),
            expected_communities.reset_index(drop=True),
            check_dtype=False,
        )
        del normalized, embeddings, nodes, memberships
        gc.collect()
        torch.cuda.empty_cache()


if __name__ == "__main__":
    unittest.main()
