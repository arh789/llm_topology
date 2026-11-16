"""Focused tests for the configuration-driven topology engine."""

from __future__ import annotations

import csv
import gzip
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F

import r012_semantic_topology as historical
from topology_core import (
    TopologySettings,
    analyze_network,
    elbow_candidate,
    exact_knn,
    state_label,
)
from topology_engine import (
    RunContext,
    _analysis_required,
    _count_gzip_rows,
    _measurement_report_names,
    _post_measurement_run_status,
    final_non_padding_indices,
    load_and_validate_config,
    write_measured_reports,
)


PIPELINE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = (
    PIPELINE_DIR
    / "run_configs"
    / "R018_olmo3-choke-point-barrier-spear-permutations.json"
)


class ConfigurationTests(unittest.TestCase):
    def test_r018_configuration_validation_does_not_change_run_presence(self) -> None:
        configured_run = (
            PIPELINE_DIR
            / "runs"
            / "R018_olmo3-choke-point-barrier-spear-permutation-topology"
        )
        existed_before = configured_run.exists()
        context = load_and_validate_config(CONFIG_PATH)
        self.assertEqual(context.prompt_ids, ("ABC", "ACB", "BAC", "BCA", "CAB", "CBA"))
        self.assertEqual(context.config["expected"]["network_count"], 780)
        self.assertEqual(context.run_dir.exists(), existed_before)

    def test_semantic_analysis_is_required_by_default(self) -> None:
        config = {"run_number": 19}
        self.assertTrue(_analysis_required(config))
        self.assertEqual(
            _post_measurement_run_status(config), "awaiting_semantic_analysis"
        )
        self.assertEqual(
            _measurement_report_names(config),
            (
                "R019_MEASUREMENT_COMPLETENESS_VERIFICATION.md",
                "R019_MEASUREMENT_REPORT.md",
            ),
        )

    def test_measurement_only_run_can_explicitly_opt_out(self) -> None:
        config = {"run_number": 19, "analysis": {"required": False}}
        self.assertFalse(_analysis_required(config))
        self.assertEqual(_post_measurement_run_status(config), "measurement_complete")

    def test_state_labels_cover_input_blocks_and_final_norm(self) -> None:
        settings = TopologySettings(state_count=65, layer_count=64)
        self.assertEqual(state_label(0, settings), "input_embedding")
        self.assertEqual(state_label(1, settings), "block_0_output")
        self.assertEqual(state_label(63, settings), "block_62_output")
        self.assertEqual(state_label(64, settings), "final_norm_after_block_63")


class AnchorTests(unittest.TestCase):
    def test_variable_length_right_padding(self) -> None:
        mask = torch.tensor([[1, 1, 1, 0], [1, 1, 1, 1]], dtype=torch.long)
        self.assertTrue(torch.equal(final_non_padding_indices(mask), torch.tensor([2, 3])))

    def test_left_or_gapped_padding_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            final_non_padding_indices(torch.tensor([[1, 0, 1]], dtype=torch.long))


class PersistenceTests(unittest.TestCase):
    def test_gzip_row_count_uses_csv_records_not_physical_lines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.csv.gz"
            with gzip.open(path, "wt", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(["token_id", "decoded_token"])
                writer.writerow([1, "ordinary"])
                writer.writerow([2, "embedded\nnewline"])
            self.assertEqual(_count_gzip_rows(path), 2)


class ReportLifecycleTests(unittest.TestCase):
    def test_measurement_report_leaves_research_run_awaiting_analysis(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            config = {
                "run_id": "R019_synthetic",
                "run_number": 19,
                "model": {"id": "synthetic/model", "revision": "test-revision"},
                "expected": {
                    "network_count": 2,
                    "within_prompt_transition_rows": 0,
                    "pairwise_permutation_rows": 0,
                    "invariance_summary_rows": 4,
                },
            }
            context = RunContext(
                config_path=run_dir / "config.json",
                config=config,
                plan_path=run_dir / "plan.md",
                run_dir=run_dir,
                manifest_path=run_dir / "manifest.json",
                snapshot_dir=run_dir,
                offload_dir=run_dir,
                prompt_ids=("ABC",),
                settings=TopologySettings(state_count=1, layer_count=0),
            )
            results = {
                "network_count": 2,
                "adjacent_transition_rows": 0,
                "pairwise_comparison_rows": 0,
                "invariance_summary_rows": 4,
                "selected_membership_rows": 20,
                "directed_edge_rows": 200,
                "community_count": 4,
                "minimum_pairwise_membership_jaccard": 1.0,
                "minimum_pairwise_edge_jaccard": 1.0,
                "mean_same_final_membership_jaccard": 1.0,
                "mean_different_final_membership_jaccard": 1.0,
            }
            write_measured_reports(context, results)
            verification = (
                run_dir / "R019_MEASUREMENT_COMPLETENESS_VERIFICATION.md"
            ).read_text(encoding="utf-8")
            report = (run_dir / "R019_MEASUREMENT_REPORT.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("measurement completeness verification", verification)
            self.assertIn("awaiting_semantic_analysis", verification)
            self.assertIn("Overall run status: awaiting semantic analysis", report)
            self.assertNotIn("R018", report)


class MethodCompatibilityTests(unittest.TestCase):
    def test_elbow_matches_historical_function(self) -> None:
        values = np.array([1.0, 0.92, 0.85, 0.62, 0.40, 0.31, 0.25, 0.20])
        self.assertEqual(elbow_candidate(values), historical.elbow_candidate(values))

    @unittest.skipUnless(torch.cuda.is_available(), "CUDA required for exact kNN")
    def test_exact_knn_matches_historical_function(self) -> None:
        generator = torch.Generator(device="cpu").manual_seed(7)
        embeddings = F.normalize(torch.randn(40, 16, generator=generator), p=2, dim=1).cuda()
        token_ids = np.arange(24, dtype=np.int64)
        settings = TopologySettings(
            state_count=3,
            layer_count=2,
            k_neighbors=10,
            knn_batch_size=historical.KNN_BATCH_SIZE,
        )
        new_positions, new_values = exact_knn(embeddings, token_ids, settings)
        old_positions, old_values = historical.exact_knn(
            embeddings, token_ids, historical.K_NEIGHBORS
        )
        np.testing.assert_array_equal(new_positions, old_positions)
        np.testing.assert_array_equal(new_values, old_values)

    @unittest.skipUnless(torch.cuda.is_available(), "CUDA required for network test")
    def test_network_partition_matches_historical_function(self) -> None:
        generator = torch.Generator(device="cpu").manual_seed(11)
        embeddings = F.normalize(torch.randn(48, 20, generator=generator), p=2, dim=1).cuda()
        token_ids = np.arange(30, dtype=np.int64)
        frame = pd.DataFrame(
            {
                "prompt": "synthetic",
                "state_index": 1,
                "state_label": "block_0_output",
                "side": "positive_head",
                "token_id": token_ids,
                "raw_token": [f"t{item}" for item in token_ids],
                "decoded_token": [f"t{item}" for item in token_ids],
                "display_token": [f"t{item}" for item in token_ids],
                "token_class": ["alphabetic"] * len(token_ids),
                "cosine_score": np.linspace(0.9, 0.2, len(token_ids)),
                "rank_from_extreme": np.arange(1, len(token_ids) + 1),
            }
        )
        historical_result = historical.analyze_network(
            "synthetic", 0, 1, "positive_head", 0, frame, embeddings, 48
        )
        new_frame = frame.rename(columns={"prompt": "prompt_id"})
        settings = TopologySettings(
            state_count=historical.STATE_COUNT,
            layer_count=historical.STATE_COUNT - 1,
            k_neighbors=historical.K_NEIGHBORS,
            knn_batch_size=historical.KNN_BATCH_SIZE,
            random_seed=historical.RANDOM_SEED,
            louvain_resolution=historical.LOUVAIN_RESOLUTION,
        )
        new_result = analyze_network(
            "synthetic", 0, 1, "positive_head", 0, new_frame, embeddings, 48, settings
        )
        old_nodes, old_edges = historical_result[1], historical_result[2]
        new_nodes, new_edges = new_result[1], new_result[2]
        np.testing.assert_array_equal(
            old_nodes["community_id"].to_numpy(), new_nodes["community_id"].to_numpy()
        )
        np.testing.assert_array_equal(
            old_edges[["source_token_id", "target_token_id", "neighbor_rank"]].to_numpy(),
            new_edges[["source_token_id", "target_token_id", "neighbor_rank"]].to_numpy(),
        )
        np.testing.assert_array_equal(
            old_edges["cosine_similarity"].to_numpy(),
            new_edges["cosine_similarity"].to_numpy(),
        )


if __name__ == "__main__":
    unittest.main()
