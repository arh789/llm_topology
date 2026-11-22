"""Model-independent intermediate-state and autoregressive capture."""

from __future__ import annotations

import hashlib
from typing import Any

import torch
import torch.nn.functional as F

from .adapters import ArchitectureAdapter


class BlockRecorder:
    """Capture the raw output of every transformer block through hooks."""

    def __init__(self, model: Any, adapter: ArchitectureAdapter) -> None:
        adapter.validate_model(model)
        self.outputs: list[torch.Tensor | None] = [None] * len(adapter.blocks(model))
        self.handles = []
        for index, layer in enumerate(adapter.blocks(model)):
            self.handles.append(layer.register_forward_hook(self._hook(index)))

    def _hook(self, index: int):
        def record(_module: Any, _inputs: Any, output: Any) -> None:
            tensor = output[0] if isinstance(output, (tuple, list)) else output
            if not isinstance(tensor, torch.Tensor):
                raise TypeError(f"Block {index} did not return a tensor state.")
            self.outputs[index] = tensor.detach()

        return record

    def clear(self) -> None:
        self.outputs = [None] * len(self.outputs)

    def close(self) -> None:
        for handle in self.handles:
            handle.remove()
        self.handles.clear()


def _state_agreement(left: torch.Tensor, right: torch.Tensor) -> bool:
    if torch.equal(left, right):
        return True
    if left.dtype in (torch.float16, torch.bfloat16) or right.dtype in (
        torch.float16,
        torch.bfloat16,
    ):
        return bool(torch.allclose(left.float(), right.float(), atol=1e-5, rtol=1e-5))
    return False


def forward_capture(
    model: Any,
    adapter: ArchitectureAdapter,
    recorder: BlockRecorder,
    input_ids: torch.Tensor,
    *,
    full_sequence: bool,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Capture input, every raw block output, final norm and output logits."""

    recorder.clear()
    with torch.inference_mode():
        output = model(
            input_ids=input_ids,
            output_hidden_states=True,
            use_cache=False,
            return_dict=True,
        )
    standard = output.hidden_states
    blocks = adapter.blocks(model)
    if standard is None or len(standard) != len(blocks) + 1:
        found = 0 if standard is None else len(standard)
        raise RuntimeError(
            f"Expected {len(blocks) + 1} standard hidden states; found {found}."
        )
    if any(value is None for value in recorder.outputs):
        raise RuntimeError("At least one raw transformer-block output was not captured.")
    raw_blocks = [value for value in recorder.outputs if value is not None]

    # Hugging Face causal decoders normally expose pre-layer states plus the
    # final-normalised state. Raw block hooks make the final block boundary
    # explicit and allow every earlier boundary to be reconciled independently.
    for index in range(len(raw_blocks) - 1):
        if not _state_agreement(raw_blocks[index], standard[index + 1]):
            raise RuntimeError(
                f"Raw block {index} disagrees with the standard hidden-state tuple."
            )
    with torch.inference_mode():
        recomputed_final = adapter.final_norm(model)(raw_blocks[-1])
    if not _state_agreement(recomputed_final, standard[-1]):
        maximum = float((recomputed_final.float() - standard[-1].float()).abs().max())
        raise RuntimeError(f"Final-normalisation capture mismatch: {maximum}")

    state_tensors = [standard[0], *raw_blocks, standard[-1]]
    if full_sequence:
        states = torch.stack(
            [value[0].detach().to(device="cpu", dtype=torch.float32) for value in state_tensors]
        ).contiguous()
        logits = output.logits[0].detach().to(device="cpu", dtype=torch.float32).contiguous()
    else:
        states = torch.stack(
            [value[0, -1].detach().to(device="cpu", dtype=torch.float32) for value in state_tensors]
        ).contiguous()
        logits = output.logits[0, -1].detach().to(device="cpu", dtype=torch.float32).contiguous()
    if not torch.isfinite(states).all() or not torch.isfinite(logits).all():
        raise RuntimeError("A captured state or logit is non-finite.")
    return states, logits


def _decode(tokenizer: Any, token_id: int) -> str:
    return tokenizer.decode(
        [token_id],
        skip_special_tokens=False,
        clean_up_tokenization_spaces=False,
    )


def _raw_token(tokenizer: Any, token_id: int) -> str:
    return str(tokenizer.convert_ids_to_tokens([token_id])[0])


def generate_capture(
    model: Any,
    tokenizer: Any,
    adapter: ArchitectureAdapter,
    prompt_text: str,
    *,
    device: str,
    max_new_tokens: int,
    add_special_tokens: bool = False,
) -> dict[str, Any]:
    """Greedily generate and capture every layer for every token decision."""

    if max_new_tokens < 1:
        raise ValueError("max_new_tokens must be positive.")
    encoded = tokenizer(
        prompt_text,
        return_tensors="pt",
        add_special_tokens=add_special_tokens,
        return_token_type_ids=False,
    )
    prompt_ids = encoded["input_ids"][0].tolist()
    if not prompt_ids:
        raise RuntimeError("Prompt tokenization is empty.")
    input_ids = encoded["input_ids"].to(device)
    recorder = BlockRecorder(model, adapter)
    decision_states: list[torch.Tensor] = []
    decision_logits: list[torch.Tensor] = []
    generated_ids: list[int] = []
    trace_rows: list[dict[str, object]] = []
    top_logit_rows: list[dict[str, object]] = []
    stop_reason = "max_new_tokens"
    eos_id = tokenizer.eos_token_id
    try:
        for decision_index in range(max_new_tokens):
            states, logits = forward_capture(
                model, adapter, recorder, input_ids, full_sequence=False
            )
            expected_shape = (
                len(adapter.blocks(model)) + 2,
                int(model.config.hidden_size),
            )
            if tuple(states.shape) != expected_shape:
                raise RuntimeError(f"Unexpected decision-state shape: {tuple(states.shape)}")
            probabilities = torch.softmax(logits.double(), dim=0)
            selected_id = int(torch.argmax(logits).item())
            log_probabilities = torch.log_softmax(logits.double(), dim=0)
            entropy = float(-(probabilities * log_probabilities).sum())
            top_count = min(100, logits.numel())
            top_values, top_ids = torch.topk(logits, k=top_count, largest=True, sorted=True)
            prefix_ids = input_ids[0].detach().cpu().tolist()
            prefix_text = tokenizer.decode(prefix_ids, clean_up_tokenization_spaces=False)
            trace_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "prefix_token_count": len(prefix_ids),
                    "prefix_utf8_sha256": hashlib.sha256(prefix_text.encode("utf-8")).hexdigest(),
                    "decision_position": len(prefix_ids) - 1,
                    "decision_token_id": int(prefix_ids[-1]),
                    "decision_token": _raw_token(tokenizer, int(prefix_ids[-1])),
                    "decision_decoded_token": _decode(tokenizer, int(prefix_ids[-1])),
                    "selected_token_id": selected_id,
                    "selected_token": _raw_token(tokenizer, selected_id),
                    "selected_decoded_token": _decode(tokenizer, selected_id),
                    "selected_logit": float(logits[selected_id]),
                    "selected_probability": float(probabilities[selected_id]),
                    "selected_rank": 1,
                    "distribution_entropy_nats": entropy,
                    "is_eos": bool(eos_id is not None and selected_id == int(eos_id)),
                }
            )
            for rank, (token_id, value) in enumerate(
                zip(top_ids.tolist(), top_values.tolist(), strict=True), start=1
            ):
                top_logit_rows.append(
                    {
                        "decision_index": decision_index,
                        "generated_token_index": decision_index + 1,
                        "rank": rank,
                        "token_id": int(token_id),
                        "raw_token": _raw_token(tokenizer, int(token_id)),
                        "decoded_token": _decode(tokenizer, int(token_id)),
                        "logit": float(value),
                        "probability": float(probabilities[int(token_id)]),
                    }
                )
            decision_states.append(states)
            decision_logits.append(logits)
            generated_ids.append(selected_id)
            addition = torch.tensor([[selected_id]], dtype=torch.long, device=input_ids.device)
            input_ids = torch.cat([input_ids, addition], dim=1)
            if eos_id is not None and selected_id == int(eos_id):
                stop_reason = "eos"
                break
        full_states, final_logits = forward_capture(
            model, adapter, recorder, input_ids, full_sequence=True
        )
    finally:
        recorder.close()
    if not decision_states:
        raise RuntimeError("Generation produced no decision record.")
    return {
        "prompt_ids": prompt_ids,
        "generated_ids": generated_ids,
        "full_ids": input_ids[0].detach().cpu().tolist(),
        "decision_states": torch.stack(decision_states).contiguous(),
        "decision_logits": torch.stack(decision_logits).contiguous(),
        "full_sequence_states": full_states,
        "post_generation_logits": final_logits,
        "trace_rows": trace_rows,
        "top_logit_rows": top_logit_rows,
        "stop_reason": stop_reason,
        "generated_text": tokenizer.decode(
            generated_ids,
            skip_special_tokens=False,
            clean_up_tokenization_spaces=False,
        ),
    }
