"""Local-model integration tests for the two initial TSTP adapters.

These tests are intentionally skipped when CUDA or the canonical local model
snapshots are unavailable. They never download model files.
"""

from __future__ import annotations

import gc
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import torch
from safetensors.torch import load_file
from transformers import AutoModelForCausalLM, AutoTokenizer

import r020_pythia_generation_topology as r020
from topology_core import TopologySettings, state_label
from tstp.adapters import get_adapter
from tstp.capture import generate_capture
from tstp_engine import Context, capture, load_context, load_model


PIPELINE_DIR = Path(__file__).resolve().parent
R020_DIR = PIPELINE_DIR / "runs" / "R020_pythia-70m-representation-output-contrast"
R020_CONFIG = R020_DIR / "run_config.json"
R020_CAPTURE = R020_DIR / "local_raw_capture" / "primary_capture.safetensors"
QWEN_SNAPSHOT = Path(
    r"D:\AI\cache\huggingface\hub\models--Qwen--Qwen2.5-0.5B-Instruct\snapshots\7ae557604adf67be50417f59c2c2f167def9a775"
)


@unittest.skipUnless(torch.cuda.is_available(), "CUDA required")
class LocalModelIntegrationTests(unittest.TestCase):
    def tearDown(self) -> None:
        gc.collect()
        torch.cuda.empty_cache()

    @unittest.skipUnless(
        R020_CONFIG.is_file() and R020_CAPTURE.is_file(),
        "Frozen R020 configuration and local capture required",
    )
    def test_pythia_adapter_reproduces_r020_capture_exactly(self) -> None:
        context = load_context(R020_CONFIG)
        r020.set_deterministic_runtime(int(context.config["topology"]["random_seed"]))
        model, tokenizer = load_model(context)
        try:
            observed = capture(context, model, tokenizer)
            expected = load_file(str(R020_CAPTURE), device="cpu")
            for name in (
                "decision_states",
                "decision_logits",
                "full_sequence_states",
                "post_generation_logits",
            ):
                self.assertTrue(torch.equal(observed[name], expected[name]), name)
            prompt_record = json.loads(
                (R020_DIR / "prompt_records.json").read_text(encoding="utf-8")
            )
            self.assertEqual(observed["generated_ids"], prompt_record["generated_token_ids"])
        finally:
            del model, tokenizer

    @unittest.skipUnless(QWEN_SNAPSHOT.is_dir(), "Cached Qwen 0.5B snapshot required")
    def test_qwen_adapter_captures_raw_blocks_and_final_norm(self) -> None:
        tokenizer = AutoTokenizer.from_pretrained(QWEN_SNAPSHOT, local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained(
            QWEN_SNAPSHOT,
            local_files_only=True,
            dtype=torch.bfloat16,
            attn_implementation="eager",
            trust_remote_code=False,
        ).to("cuda:0")
        model.eval()
        adapter = get_adapter("qwen2")
        try:
            observed = generate_capture(
                model,
                tokenizer,
                adapter,
                "Question: Why would a city build a bridge across a river?\nAnswer:",
                device="cuda:0",
                max_new_tokens=1,
                add_special_tokens=False,
            )
            expected_states = int(model.config.num_hidden_layers) + 2
            self.assertEqual(observed["decision_states"].shape[0], 1)
            self.assertEqual(observed["decision_states"].shape[1], expected_states)
            self.assertEqual(
                observed["decision_states"].shape[2], int(model.config.hidden_size)
            )
            self.assertTrue(torch.isfinite(observed["decision_states"]).all())
            self.assertTrue(torch.isfinite(observed["decision_logits"]).all())
        finally:
            del model, tokenizer

    @unittest.skipUnless(
        os.environ.get("TSTP_FULL_INTEGRATION") == "1",
        "Set TSTP_FULL_INTEGRATION=1 for the measured Qwen topology test",
    )
    @unittest.skipUnless(QWEN_SNAPSHOT.is_dir(), "Cached Qwen 0.5B snapshot required")
    def test_qwen_adapter_reaches_measured_network_exports(self) -> None:
        tokenizer = AutoTokenizer.from_pretrained(QWEN_SNAPSHOT, local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained(
            QWEN_SNAPSHOT,
            local_files_only=True,
            dtype=torch.bfloat16,
            attn_implementation="eager",
            trust_remote_code=False,
        ).to("cuda:0")
        model.eval()
        adapter = get_adapter("qwen2")
        prompt = "Question: Why would a city build a bridge across a river?\nAnswer:"
        layer_count = int(model.config.num_hidden_layers)
        state_count = layer_count + 2
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            raw_dir = run_dir / "local_raw_capture"
            controls_dir = run_dir / "controls"
            raw_dir.mkdir()
            controls_dir.mkdir()
            config = {
                "run_id": "TSTP_qwen2_engineering_validation",
                "run_number": 0,
                "model": {
                    "id": "Qwen/Qwen2.5-0.5B-Instruct",
                    "revision": "7ae557604adf67be50417f59c2c2f167def9a775",
                    "device": "cuda:0",
                },
                "prompt": {
                    "text": prompt,
                    "utf8_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                },
                "generation": {"max_new_tokens": 1},
                "capture": {
                    "reconciliation_absolute_tolerance": 1e-5,
                    "reconciliation_relative_tolerance": 1e-5,
                    "reconciliation_min_cosine_similarity": 0.99999,
                    "reconciliation_required_top_token_overlap": 12,
                },
                "topology": {
                    "top_tokens_per_sector": 12,
                    "random_seed": 20261122,
                },
                "controls": {"shuffle_seed": 20261122},
            }
            settings = TopologySettings(
                state_count=state_count,
                layer_count=layer_count,
                k_neighbors=10,
                knn_batch_size=512,
                random_seed=20261122,
                louvain_resolution=1.0,
                device="cuda:0",
            )
            context = Context(
                config_path=run_dir / "run_config.json",
                config=config,
                run_dir=run_dir,
                raw_dir=raw_dir,
                controls_dir=controls_dir,
                snapshot_dir=QWEN_SNAPSHOT,
                manifest_path=run_dir / "manifest.json",
                settings=settings,
                state_labels=tuple(
                    state_label(index, settings) for index in range(state_count)
                ),
                adapter=adapter,
            )
            try:
                primary = generate_capture(
                    model,
                    tokenizer,
                    adapter,
                    prompt,
                    device="cuda:0",
                    max_new_tokens=1,
                )
                replay = generate_capture(
                    model,
                    tokenizer,
                    adapter,
                    prompt,
                    device="cuda:0",
                    max_new_tokens=1,
                )
                validation = r020.write_capture_artifacts(
                    context, tokenizer, primary, replay
                )
                self.assertTrue(validation["replay"]["decision_states_exact"])
                normalized, memberships, vocabulary = r020.project_and_select(
                    context, model, tokenizer, primary, replay
                )
                network_details, export_details = r020.construct_networks(
                    context, normalized, memberships, vocabulary
                )
                self.assertEqual(network_details["network_count"], state_count * 2)
                self.assertEqual(export_details["chatgpt_networks"], state_count * 2)
                for name in (
                    "network_index.csv",
                    "community_nodes.csv",
                    "community_edges.csv",
                    "chatgpt_community_networks.json",
                    "chatgpt_layer_packets.md",
                ):
                    self.assertTrue((run_dir / name).is_file(), name)
                del normalized, memberships, vocabulary, primary, replay
            finally:
                del model, tokenizer


if __name__ == "__main__":
    unittest.main()
