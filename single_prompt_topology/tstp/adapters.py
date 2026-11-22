"""Architecture adapters for Transformer State Topology Pipeline captures.

Adapters expose only the model-specific objects required by the common
capture and topology workflow. They do not perform semantic interpretation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any

import torch


class ArchitectureAdapter(ABC):
    """Minimal contract required by the model-independent TSTP runner."""

    name: str
    architecture_names: tuple[str, ...]

    def supports(self, model: Any) -> bool:
        return type(model).__name__ in self.architecture_names

    def validate_model(self, model: Any) -> None:
        if not self.supports(model):
            expected = ", ".join(self.architecture_names)
            raise TypeError(
                f"Adapter {self.name!r} supports [{expected}], not "
                f"{type(model).__name__!r}."
            )
        blocks = self.blocks(model)
        if not blocks:
            raise RuntimeError(f"Adapter {self.name!r} found no transformer blocks.")
        if len(blocks) != int(model.config.num_hidden_layers):
            raise RuntimeError(
                f"Adapter {self.name!r} found {len(blocks)} blocks but the model "
                f"configuration declares {model.config.num_hidden_layers}."
            )
        if self.final_norm(model) is None:
            raise RuntimeError(f"Adapter {self.name!r} found no final normalisation.")
        if model.get_input_embeddings() is None:
            raise RuntimeError(f"Adapter {self.name!r} found no input embeddings.")
        if model.get_output_embeddings() is None:
            raise RuntimeError(f"Adapter {self.name!r} found no output embeddings.")

    @abstractmethod
    def blocks(self, model: Any) -> Sequence[torch.nn.Module]:
        """Return transformer blocks in forward order."""

    @abstractmethod
    def final_norm(self, model: Any) -> torch.nn.Module:
        """Return the module applied after the final raw transformer block."""

    def state_labels(self, model: Any) -> tuple[str, ...]:
        block_count = len(self.blocks(model))
        return (
            "input_embedding",
            *(f"block_{index}_output" for index in range(block_count)),
            f"final_norm_after_block_{block_count - 1}",
        )

    def metadata(self, model: Any) -> dict[str, object]:
        blocks = self.blocks(model)
        return {
            "adapter": self.name,
            "architecture": type(model).__name__,
            "transformer_block_class": type(blocks[0]).__name__,
            "layer_count": len(blocks),
            "recorded_state_count": len(blocks) + 2,
            "state_labels": list(self.state_labels(model)),
            "hidden_width": int(model.config.hidden_size),
            "input_embedding_shape": list(model.get_input_embeddings().weight.shape),
            "output_embedding_shape": list(model.get_output_embeddings().weight.shape),
        }


class PythiaAdapter(ArchitectureAdapter):
    name = "pythia"
    architecture_names = ("GPTNeoXForCausalLM",)

    def blocks(self, model: Any) -> Sequence[torch.nn.Module]:
        return model.gpt_neox.layers

    def final_norm(self, model: Any) -> torch.nn.Module:
        return model.gpt_neox.final_layer_norm


class Qwen2Adapter(ArchitectureAdapter):
    name = "qwen2"
    architecture_names = ("Qwen2ForCausalLM",)

    def blocks(self, model: Any) -> Sequence[torch.nn.Module]:
        return model.model.layers

    def final_norm(self, model: Any) -> torch.nn.Module:
        return model.model.norm


_ADAPTERS: dict[str, ArchitectureAdapter] = {
    adapter.name: adapter for adapter in (PythiaAdapter(), Qwen2Adapter())
}


def adapter_names() -> tuple[str, ...]:
    return tuple(sorted(_ADAPTERS))


def get_adapter(name: str) -> ArchitectureAdapter:
    try:
        return _ADAPTERS[name]
    except KeyError as error:
        available = ", ".join(adapter_names())
        raise ValueError(
            f"Unsupported TSTP adapter {name!r}. Available adapters: {available}."
        ) from error
