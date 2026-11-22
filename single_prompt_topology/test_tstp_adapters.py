"""Contract tests for TSTP architecture adapters and state capture."""

from __future__ import annotations

import types
import unittest

import torch

from tstp.adapters import PythiaAdapter, Qwen2Adapter, adapter_names, get_adapter


class _Block(torch.nn.Module):
    def forward(self, value: torch.Tensor) -> torch.Tensor:
        return value + 1


class GPTNeoXForCausalLM:
    def __init__(self) -> None:
        self.config = types.SimpleNamespace(num_hidden_layers=2, hidden_size=4)
        self.gpt_neox = types.SimpleNamespace(
            layers=torch.nn.ModuleList([_Block(), _Block()]),
            final_layer_norm=torch.nn.LayerNorm(4),
        )
        self._input = torch.nn.Embedding(8, 4)
        self._output = torch.nn.Linear(4, 8, bias=False)

    def get_input_embeddings(self):
        return self._input

    def get_output_embeddings(self):
        return self._output


class Qwen2ForCausalLM:
    def __init__(self) -> None:
        self.config = types.SimpleNamespace(num_hidden_layers=3, hidden_size=6)
        self.model = types.SimpleNamespace(
            layers=torch.nn.ModuleList([_Block(), _Block(), _Block()]),
            norm=torch.nn.RMSNorm(6),
        )
        self._input = torch.nn.Embedding(10, 6)
        self._output = torch.nn.Linear(6, 10, bias=False)

    def get_input_embeddings(self):
        return self._input

    def get_output_embeddings(self):
        return self._output


class AdapterContractTests(unittest.TestCase):
    def test_registry_exposes_two_independent_architectures(self) -> None:
        self.assertEqual(adapter_names(), ("pythia", "qwen2"))
        self.assertIsInstance(get_adapter("pythia"), PythiaAdapter)
        self.assertIsInstance(get_adapter("qwen2"), Qwen2Adapter)

    def test_pythia_state_contract(self) -> None:
        model = GPTNeoXForCausalLM()
        adapter = get_adapter("pythia")
        adapter.validate_model(model)
        self.assertEqual(len(adapter.blocks(model)), 2)
        self.assertEqual(
            adapter.state_labels(model),
            (
                "input_embedding",
                "block_0_output",
                "block_1_output",
                "final_norm_after_block_1",
            ),
        )

    def test_qwen_state_contract(self) -> None:
        model = Qwen2ForCausalLM()
        adapter = get_adapter("qwen2")
        adapter.validate_model(model)
        self.assertEqual(len(adapter.blocks(model)), 3)
        self.assertEqual(adapter.metadata(model)["recorded_state_count"], 5)

    def test_wrong_adapter_fails_before_capture(self) -> None:
        with self.assertRaisesRegex(TypeError, "supports"):
            get_adapter("pythia").validate_model(Qwen2ForCausalLM())

    def test_unknown_adapter_is_explicit(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unsupported TSTP adapter"):
            get_adapter("unknown")


if __name__ == "__main__":
    unittest.main()
