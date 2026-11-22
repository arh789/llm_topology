"""R020 tiny-model autoregressive representation/output contrast.

This runner captures every transformer boundary for every greedy next-token
decision, projects those states into the fixed input-embedding vocabulary,
constructs the established cutoff populations and token networks, and stops
before semantic interpretation.
"""

from __future__ import annotations

import argparse
import copy
import csv
import gc
import gzip
import hashlib
import json
import math
import os
import platform
import sys
import time
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import networkx as nx
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from safetensors.torch import save_file
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

import topology_core as topology


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
SIDES = ("positive_head", "negative_tail")
COMPONENTS = (
    "model_identity",
    "primary_capture",
    "deterministic_replay",
    "projection_and_cutoffs",
    "networks_and_communities",
    "shuffled_control",
    "measured_exports",
    "resource_cleanup",
    "completeness_validation",
)


@dataclass(frozen=True)
class Context:
    config_path: Path
    config: dict[str, Any]
    run_dir: Path
    raw_dir: Path
    controls_dir: Path
    snapshot_dir: Path
    manifest_path: Path
    settings: topology.TopologySettings
    state_labels: tuple[str, ...]


class BlockRecorder:
    def __init__(self, model: Any) -> None:
        self.outputs: list[torch.Tensor | None] = [None] * len(model.gpt_neox.layers)
        self.handles = []
        for index, layer in enumerate(model.gpt_neox.layers):
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


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
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


def safe_decode(tokenizer: Any, token_id: int) -> str:
    if not 0 <= token_id < len(tokenizer):
        return f"<padded_token_{token_id}>"
    return tokenizer.decode(
        [token_id],
        skip_special_tokens=False,
        clean_up_tokenization_spaces=False,
    )


def raw_token(tokenizer: Any, token_id: int) -> str:
    if not 0 <= token_id < len(tokenizer):
        return f"<padded_token_{token_id}>"
    return str(tokenizer.convert_ids_to_tokens([token_id])[0])


def memory_snapshot() -> dict[str, object]:
    payload: dict[str, object] = {
        "timestamp": utc_now(),
        "cuda_available": torch.cuda.is_available(),
    }
    if torch.cuda.is_available():
        free, total = torch.cuda.mem_get_info()
        payload.update(
            {
                "cuda_device": torch.cuda.get_device_name(0),
                "cuda_free_bytes": int(free),
                "cuda_total_bytes": int(total),
                "cuda_allocated_bytes": int(torch.cuda.memory_allocated()),
                "cuda_reserved_bytes": int(torch.cuda.memory_reserved()),
                "cuda_peak_allocated_bytes": int(torch.cuda.max_memory_allocated()),
            }
        )
    return payload


def set_deterministic_runtime(seed: int) -> None:
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.manual_seed(seed)
    np.random.seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.set_float32_matmul_precision("highest")


def load_context(config_path: Path) -> Context:
    config_path = config_path.resolve()
    config = load_json(config_path)
    if int(config.get("run_number", -1)) != 20:
        raise ValueError("R020 runner requires run_number 20.")
    if config.get("run_id") != "R020_pythia-70m-representation-output-contrast":
        raise ValueError("Unexpected R020 run identity.")
    run_dir = (PROJECT_ROOT / str(config["run_directory"])).resolve()
    if config_path.parent != run_dir:
        raise ValueError("run_config.json must reside in the configured run directory.")
    prompt = str(config["prompt"]["text"])
    if sha256_bytes(prompt.encode("utf-8")) != config["prompt"]["utf8_sha256"]:
        raise ValueError("Prompt UTF-8 hash does not match the configuration.")
    if config["prompt"].get("chat_template_used"):
        raise ValueError("R020 does not permit a chat template.")
    if config["prompt"].get("add_special_tokens"):
        raise ValueError("R020 does not permit added special tokens.")
    if config["generation"].get("do_sample"):
        raise ValueError("R020 requires deterministic greedy decoding.")
    if config["generation"].get("use_cache"):
        raise ValueError("R020 requires inspectable full-prefix forwards.")
    if int(config["generation"]["max_new_tokens"]) != 32:
        raise ValueError("R020 is locked to at most 32 generated tokens.")
    minimum_cosine = float(
        config["capture"]["reconciliation_min_cosine_similarity"]
    )
    if not 0.0 < minimum_cosine <= 1.0:
        raise ValueError("The full-sequence cosine threshold must be in (0, 1].")
    required_overlap = int(
        config["capture"]["reconciliation_required_top_token_overlap"]
    )
    configured_top_count = int(config["topology"]["top_tokens_per_sector"])
    if required_overlap != configured_top_count:
        raise ValueError(
            "R020 requires the complete configured top-token set to reconcile."
        )
    model = config["model"]
    snapshot_dir = Path(str(model["snapshot_path"])).resolve()
    if not snapshot_dir.is_dir():
        raise FileNotFoundError(f"Frozen model snapshot is missing: {snapshot_dir}")
    if not (snapshot_dir / "model.safetensors").is_file():
        raise FileNotFoundError("Frozen model weights are missing.")
    model_config = AutoConfig.from_pretrained(snapshot_dir, local_files_only=True)
    if model_config.architectures != [str(model["architecture"])]:
        raise RuntimeError(f"Unexpected architecture: {model_config.architectures}")
    layer_count = int(model_config.num_hidden_layers)
    hidden_width = int(model_config.hidden_size)
    if layer_count != int(model["expected_layer_count"]):
        raise RuntimeError("Model layer count differs from the frozen contract.")
    if hidden_width != int(model["expected_hidden_width"]):
        raise RuntimeError("Model hidden width differs from the frozen contract.")
    state_count = layer_count + 2
    if state_count != int(config["capture"]["expected_state_count"]):
        raise RuntimeError("Recorded-state count differs from the frozen contract.")
    device = str(model["device"])
    if device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("The frozen CUDA device is unavailable.")
    settings = topology.TopologySettings(
        state_count=state_count,
        layer_count=layer_count,
        k_neighbors=int(config["topology"]["k_neighbors"]),
        knn_batch_size=int(config["topology"]["knn_batch_size"]),
        random_seed=int(config["topology"]["random_seed"]),
        louvain_resolution=float(config["topology"]["louvain_resolution"]),
        device=device,
    )
    labels = tuple(topology.state_label(index, settings) for index in range(state_count))
    return Context(
        config_path=config_path,
        config=config,
        run_dir=run_dir,
        raw_dir=run_dir / "local_raw_capture",
        controls_dir=run_dir / "controls",
        snapshot_dir=snapshot_dir,
        manifest_path=run_dir / "manifest.json",
        settings=settings,
        state_labels=labels,
    )


def initialize_manifest(context: Context) -> dict[str, Any]:
    if context.manifest_path.exists():
        raise FileExistsError("R020 manifest already exists; refusing to overwrite the run.")
    allowed = {
        "hypothesis.md",
        "R020_RUN_METHODOLOGY.md",
        "R020_VALIDATION_AMENDMENT.md",
        "run_config.json",
    }
    unexpected = [
        path.name
        for path in context.run_dir.iterdir()
        if path.name not in allowed
    ]
    if unexpected:
        raise FileExistsError(f"Stale R020 output exists: {sorted(unexpected)}")
    context.raw_dir.mkdir(parents=True, exist_ok=False)
    context.controls_dir.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema_version": 1,
        "run_id": context.config["run_id"],
        "run_number": 20,
        "started_at": utc_now(),
        "run_status": "running",
        "measurement_status": "running",
        "analysis_required": True,
        "analysis_status": "not_started",
        "config": {
            "relative_path": "run_config.json",
            "sha256": sha256_file(context.config_path),
        },
        "model": context.config["model"],
        "prompt_sha256": context.config["prompt"]["utf8_sha256"],
        "required_components": list(COMPONENTS),
        "components": {name: {"status": "pending"} for name in COMPONENTS},
        "failure_details": None,
        "fallbacks": [
            {
                "name": "revision_pinned_local_model",
                "used": True,
                "reason": "The ordinary Hugging Face cache path could not create Windows symlinks; the immutable snapshot was downloaded to the canonical pinned-model store.",
                "snapshot_path": str(context.snapshot_dir),
            }
        ],
    }
    write_json(context.manifest_path, manifest)
    return manifest


def update_component(
    context: Context,
    name: str,
    started_at: str,
    started: float,
    **details: object,
) -> None:
    manifest = load_json(context.manifest_path)
    manifest["components"][name] = {
        "status": "successful",
        "started_at": started_at,
        "completed_at": utc_now(),
        "elapsed_seconds": time.perf_counter() - started,
        **details,
    }
    write_json(context.manifest_path, manifest)


def fail_measurement(context: Context, component: str, error: BaseException) -> None:
    if context.manifest_path.exists():
        manifest = load_json(context.manifest_path)
        manifest["run_status"] = "measurement_failed"
        manifest["measurement_status"] = "measurement_failed"
        manifest["analysis_status"] = "not_started"
        manifest["failed_at"] = utc_now()
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
        write_json(context.manifest_path, manifest)


def load_model(context: Context) -> tuple[Any, Any]:
    tokenizer = AutoTokenizer.from_pretrained(context.snapshot_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        context.snapshot_dir,
        local_files_only=True,
        dtype=torch.float32,
    )
    model.to(str(context.config["model"]["device"]))
    model.eval()
    if type(model).__name__ != context.config["model"]["architecture"]:
        raise RuntimeError(f"Loaded unexpected model class: {type(model).__name__}")
    if len(model.gpt_neox.layers) != context.settings.layer_count:
        raise RuntimeError("Loaded transformer-block count changed.")
    embedding = model.get_input_embeddings().weight
    output = model.get_output_embeddings().weight
    if tuple(embedding.shape) != (
        int(context.config["model"]["expected_embedding_rows"]),
        context.settings.layer_count * 0 + int(context.config["model"]["expected_hidden_width"]),
    ):
        raise RuntimeError(f"Unexpected input embedding shape: {tuple(embedding.shape)}")
    if tuple(output.shape) != tuple(embedding.shape):
        raise RuntimeError("Output head shape differs from the input embedding shape.")
    return model, tokenizer


def forward_capture(
    model: Any,
    recorder: BlockRecorder,
    input_ids: torch.Tensor,
    full_sequence: bool,
) -> tuple[torch.Tensor, torch.Tensor]:
    recorder.clear()
    with torch.inference_mode():
        output = model(
            input_ids=input_ids,
            output_hidden_states=True,
            use_cache=False,
            return_dict=True,
        )
    standard = output.hidden_states
    if standard is None or len(standard) != len(model.gpt_neox.layers) + 1:
        raise RuntimeError("The standard hidden-state tuple has unexpected coverage.")
    if any(value is None for value in recorder.outputs):
        raise RuntimeError("At least one raw transformer-block output was not captured.")
    raw_blocks = [value for value in recorder.outputs if value is not None]
    for index in range(len(raw_blocks) - 1):
        if not torch.equal(raw_blocks[index], standard[index + 1]):
            raise RuntimeError(f"Raw block {index} disagrees with the standard state tuple.")
    with torch.inference_mode():
        recomputed_final = model.gpt_neox.final_layer_norm(raw_blocks[-1])
    if not torch.equal(recomputed_final, standard[-1]):
        maximum = float((recomputed_final - standard[-1]).abs().max())
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
    del output, standard, raw_blocks, state_tensors, recomputed_final
    return states, logits


def generate_capture(
    context: Context,
    model: Any,
    tokenizer: Any,
    prompt_text: str,
    max_new_tokens: int,
) -> dict[str, Any]:
    encoded = tokenizer(
        prompt_text,
        return_tensors="pt",
        add_special_tokens=False,
        return_token_type_ids=False,
    )
    prompt_ids = encoded["input_ids"][0].tolist()
    if not prompt_ids:
        raise RuntimeError("Prompt tokenization is empty.")
    input_ids = encoded["input_ids"].to(str(context.config["model"]["device"]))
    recorder = BlockRecorder(model)
    decision_states: list[torch.Tensor] = []
    decision_logits: list[torch.Tensor] = []
    generated_ids: list[int] = []
    trace_rows: list[dict[str, object]] = []
    top_logit_rows: list[dict[str, object]] = []
    stop_reason = "max_new_tokens"
    eos_id = tokenizer.eos_token_id
    try:
        for decision_index in range(max_new_tokens):
            states, logits = forward_capture(model, recorder, input_ids, full_sequence=False)
            if tuple(states.shape) != (
                context.settings.state_count,
                int(context.config["model"]["expected_hidden_width"]),
            ):
                raise RuntimeError(f"Unexpected decision-state shape: {tuple(states.shape)}")
            probabilities = torch.softmax(logits.double(), dim=0)
            selected_id = int(torch.argmax(logits).item())
            selected_probability = float(probabilities[selected_id])
            log_probabilities = torch.log_softmax(logits.double(), dim=0)
            entropy = float(-(probabilities * log_probabilities).sum())
            top_count = min(100, logits.numel())
            top_values, top_ids = torch.topk(logits, k=top_count, largest=True, sorted=True)
            prefix_ids = input_ids[0].detach().cpu().tolist()
            trace_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "prefix_token_count": len(prefix_ids),
                    "prefix_utf8_sha256": sha256_bytes(
                        tokenizer.decode(prefix_ids, clean_up_tokenization_spaces=False).encode("utf-8")
                    ),
                    "decision_position": len(prefix_ids) - 1,
                    "decision_token_id": int(prefix_ids[-1]),
                    "decision_token": raw_token(tokenizer, int(prefix_ids[-1])),
                    "decision_decoded_token": safe_decode(tokenizer, int(prefix_ids[-1])),
                    "selected_token_id": selected_id,
                    "selected_token": raw_token(tokenizer, selected_id),
                    "selected_decoded_token": safe_decode(tokenizer, selected_id),
                    "selected_logit": float(logits[selected_id]),
                    "selected_probability": selected_probability,
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
                        "raw_token": raw_token(tokenizer, int(token_id)),
                        "decoded_token": safe_decode(tokenizer, int(token_id)),
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
            model, recorder, input_ids, full_sequence=True
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


def tensor_pair_metrics(source: torch.Tensor, target: torch.Tensor) -> dict[str, object]:
    if tuple(source.shape) != tuple(target.shape):
        return {
            "shape_equal": False,
            "exact_equal": False,
            "max_absolute_difference": None,
            "l2_distance": None,
            "cosine_similarity": None,
        }
    source64 = source.double().reshape(-1)
    target64 = target.double().reshape(-1)
    difference = source64 - target64
    return {
        "shape_equal": True,
        "exact_equal": bool(torch.equal(source, target)),
        "max_absolute_difference": float(difference.abs().max()),
        "l2_distance": float(torch.linalg.vector_norm(difference)),
        "cosine_similarity": float(F.cosine_similarity(source64, target64, dim=0)),
    }


def model_metadata(context: Context, model: Any, tokenizer: Any) -> dict[str, Any]:
    import huggingface_hub
    import safetensors
    import sklearn
    import transformers

    files = {}
    for path in sorted(context.snapshot_dir.iterdir()):
        if path.is_file():
            files[path.name] = {
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
    return {
        "schema_version": 1,
        "recorded_at": utc_now(),
        "model_id": context.config["model"]["id"],
        "revision": context.config["model"]["revision"],
        "snapshot_path": str(context.snapshot_dir),
        "architecture": type(model).__name__,
        "transformer_block_class": type(model.gpt_neox.layers[0]).__name__,
        "layer_count": len(model.gpt_neox.layers),
        "recorded_state_count": context.settings.state_count,
        "state_labels": list(context.state_labels),
        "hidden_width": int(model.config.hidden_size),
        "input_embedding_shape": list(model.get_input_embeddings().weight.shape),
        "output_embedding_shape": list(model.get_output_embeddings().weight.shape),
        "input_output_embeddings_tied": bool(
            model.get_input_embeddings().weight.data_ptr()
            == model.get_output_embeddings().weight.data_ptr()
        ),
        "tokenizer_class": type(tokenizer).__name__,
        "tokenizer_length": len(tokenizer),
        "tokenizer_special_ids": list(map(int, tokenizer.all_special_ids)),
        "files": files,
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "safetensors": safetensors.__version__,
            "huggingface_hub": huggingface_hub.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "networkx": nx.__version__,
            "sklearn": sklearn.__version__,
            "cuda": torch.version.cuda,
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        },
        "acquisition_fallback": {
            "used": True,
            "primary_failure": "Windows symlink privilege prevented ordinary Hugging Face snapshot pointers.",
            "fallback": "Immutable revision-pinned local_dir snapshot in D:/AI/models.",
        },
    }


def capture_pair_rows(
    context: Context,
    primary: dict[str, Any],
    replay: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, object]]:
    hidden_rows: list[dict[str, object]] = []
    logit_rows: list[dict[str, object]] = []
    common_steps = min(
        int(primary["decision_states"].shape[0]),
        int(replay["decision_states"].shape[0]),
    )
    for decision_index in range(common_steps):
        for state_index, label in enumerate(context.state_labels):
            hidden_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "state_index": state_index,
                    "state_label": label,
                    **tensor_pair_metrics(
                        primary["decision_states"][decision_index, state_index],
                        replay["decision_states"][decision_index, state_index],
                    ),
                }
            )
        logit_rows.append(
            {
                "decision_index": decision_index,
                "generated_token_index": decision_index + 1,
                **tensor_pair_metrics(
                    primary["decision_logits"][decision_index],
                    replay["decision_logits"][decision_index],
                ),
            }
        )
    reconciliation_rows: list[dict[str, object]] = []
    absolute = float(context.config["capture"]["reconciliation_absolute_tolerance"])
    relative = float(context.config["capture"]["reconciliation_relative_tolerance"])
    minimum_cosine = float(
        context.config["capture"]["reconciliation_min_cosine_similarity"]
    )
    prompt_length = len(primary["prompt_ids"])
    for decision_index in range(int(primary["decision_states"].shape[0])):
        position = prompt_length + decision_index - 1
        for state_index, label in enumerate(context.state_labels):
            decision = primary["decision_states"][decision_index, state_index]
            final_sequence = primary["full_sequence_states"][state_index, position]
            metrics = tensor_pair_metrics(decision, final_sequence)
            elementwise = bool(
                torch.allclose(
                    decision,
                    final_sequence,
                    atol=absolute,
                    rtol=relative,
                )
            )
            directional = bool(
                metrics["cosine_similarity"] is not None
                and float(metrics["cosine_similarity"]) >= minimum_cosine
            )
            reconciliation_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "sequence_position": position,
                    "state_index": state_index,
                    "state_label": label,
                    "elementwise_within_tolerance": elementwise,
                    "directionally_within_tolerance": directional,
                    "within_tolerance": directional,
                    **metrics,
                }
            )
    summary = {
        "primary_generated_token_count": len(primary["generated_ids"]),
        "replay_generated_token_count": len(replay["generated_ids"]),
        "generated_token_ids_exact": primary["generated_ids"] == replay["generated_ids"],
        "decision_states_exact": bool(
            torch.equal(primary["decision_states"], replay["decision_states"])
        ) if primary["decision_states"].shape == replay["decision_states"].shape else False,
        "decision_logits_exact": bool(
            torch.equal(primary["decision_logits"], replay["decision_logits"])
        ) if primary["decision_logits"].shape == replay["decision_logits"].shape else False,
        "full_sequence_states_exact": bool(
            torch.equal(primary["full_sequence_states"], replay["full_sequence_states"])
        ) if primary["full_sequence_states"].shape == replay["full_sequence_states"].shape else False,
        "all_final_sequence_elementwise_reconciliations_within_tolerance": bool(
            all(row["elementwise_within_tolerance"] for row in reconciliation_rows)
        ),
        "all_final_sequence_directional_reconciliations_within_tolerance": bool(
            all(row["directionally_within_tolerance"] for row in reconciliation_rows)
        ),
        "all_final_sequence_reconciliations_within_tolerance": bool(
            all(row["within_tolerance"] for row in reconciliation_rows)
        ),
        "minimum_required_cosine_similarity": minimum_cosine,
    }
    return (
        pd.DataFrame(hidden_rows),
        pd.DataFrame(logit_rows),
        pd.DataFrame(reconciliation_rows),
        summary,
    )


def write_capture_artifacts(
    context: Context,
    tokenizer: Any,
    primary: dict[str, Any],
    replay: dict[str, Any],
) -> dict[str, object]:
    trace = pd.DataFrame(primary["trace_rows"])
    trace.to_csv(context.run_dir / "generation_trace.csv", index=False)
    pd.DataFrame(primary["top_logit_rows"]).to_csv(
        context.run_dir / "next_token_top100.csv", index=False
    )
    prompt_length = len(primary["prompt_ids"])
    alignment_rows: list[dict[str, object]] = []
    for position, token_id in enumerate(primary["full_ids"]):
        generated = position >= prompt_length
        generation_step = position - prompt_length + 1 if generated else None
        alignment_rows.append(
            {
                "sequence_position": position,
                "source": "generated" if generated else "prompt",
                "generation_step": generation_step,
                "token_id": int(token_id),
                "raw_token": raw_token(tokenizer, int(token_id)),
                "decoded_token": safe_decode(tokenizer, int(token_id)),
                "predicted_by_sequence_position": position - 1 if generated else None,
                "decision_index": generation_step - 1 if generated else None,
                "is_eos": bool(
                    tokenizer.eos_token_id is not None
                    and int(token_id) == int(tokenizer.eos_token_id)
                ),
            }
        )
    pd.DataFrame(alignment_rows).to_csv(
        context.run_dir / "token_alignment.csv", index=False
    )
    record = {
        "schema_version": 1,
        "raw_prompt": context.config["prompt"]["text"],
        "prompt_utf8_sha256": context.config["prompt"]["utf8_sha256"],
        "prompt_input_ids": primary["prompt_ids"],
        "prompt_tokens": [raw_token(tokenizer, item) for item in primary["prompt_ids"]],
        "prompt_decoded_tokens": [safe_decode(tokenizer, item) for item in primary["prompt_ids"]],
        "capture_position": len(primary["prompt_ids"]) - 1,
        "capture_token_id": int(primary["prompt_ids"][-1]),
        "capture_token": raw_token(tokenizer, int(primary["prompt_ids"][-1])),
        "generated_token_ids": primary["generated_ids"],
        "generated_tokens": [raw_token(tokenizer, item) for item in primary["generated_ids"]],
        "generated_decoded_tokens": [
            safe_decode(tokenizer, item) for item in primary["generated_ids"]
        ],
        "generated_text": primary["generated_text"],
        "stop_reason": primary["stop_reason"],
        "chat_template_used": False,
        "special_tokens_added": False,
    }
    write_json(context.run_dir / "prompt_records.json", record)
    save_file(
        {
            "decision_states": primary["decision_states"],
            "decision_logits": primary["decision_logits"],
            "full_sequence_states": primary["full_sequence_states"],
            "post_generation_logits": primary["post_generation_logits"],
        },
        str(context.raw_dir / "primary_capture.safetensors"),
        metadata={
            "run_id": context.config["run_id"],
            "model_revision": context.config["model"]["revision"],
            "prompt_sha256": context.config["prompt"]["utf8_sha256"],
        },
    )
    save_file(
        {
            "decision_states": replay["decision_states"],
            "decision_logits": replay["decision_logits"],
            "full_sequence_states": replay["full_sequence_states"],
            "post_generation_logits": replay["post_generation_logits"],
        },
        str(context.raw_dir / "replay_capture.safetensors"),
        metadata={"run_id": context.config["run_id"], "capture": "deterministic_replay"},
    )
    hidden, logits, reconciliation, summary = capture_pair_rows(context, primary, replay)
    hidden.to_csv(context.run_dir / "replay_hidden_state_metrics.csv", index=False)
    logits.to_csv(context.run_dir / "replay_logit_metrics.csv", index=False)
    reconciliation.to_csv(
        context.run_dir / "full_sequence_reconciliation.csv", index=False
    )
    capture_validation = {
        "schema_version": 1,
        "status": "successful",
        "recorded_at": utc_now(),
        "decision_state_shape": list(primary["decision_states"].shape),
        "decision_logit_shape": list(primary["decision_logits"].shape),
        "full_sequence_state_shape": list(primary["full_sequence_states"].shape),
        "state_labels": list(context.state_labels),
        "prompt_token_count": prompt_length,
        "generated_token_count": len(primary["generated_ids"]),
        "stop_reason": primary["stop_reason"],
        "replay": summary,
        "reconciliation_absolute_tolerance": context.config["capture"][
            "reconciliation_absolute_tolerance"
        ],
        "reconciliation_relative_tolerance": context.config["capture"][
            "reconciliation_relative_tolerance"
        ],
        "reconciliation_min_cosine_similarity": context.config["capture"][
            "reconciliation_min_cosine_similarity"
        ],
    }
    write_json(context.run_dir / "capture_validation.json", capture_validation)
    return capture_validation


def project_and_select(
    context: Context,
    model: Any,
    tokenizer: Any,
    primary: dict[str, Any],
    replay: dict[str, Any],
) -> tuple[
    torch.Tensor,
    dict[tuple[int, int, str], pd.DataFrame],
    dict[str, Any],
]:
    vocabulary_size = len(tokenizer)
    embedding_rows = int(model.get_input_embeddings().weight.shape[0])
    if embedding_rows < vocabulary_size:
        raise RuntimeError("Input embedding table is smaller than the tokenizer vocabulary.")
    embeddings = (
        model.get_input_embeddings().weight[:vocabulary_size]
        .detach()
        .to(device=str(context.config["model"]["device"]), dtype=torch.float32)
    )
    normalized_embeddings = F.normalize(embeddings, p=2, dim=1)
    normalized_primary = F.normalize(
        primary["decision_states"].to(normalized_embeddings.device), p=2, dim=2
    )
    with torch.inference_mode():
        primary_scores = torch.einsum(
            "dsh,vh->dsv", normalized_primary, normalized_embeddings
        ).cpu().contiguous()
    normalized_replay = F.normalize(
        replay["decision_states"].to(normalized_embeddings.device), p=2, dim=2
    )
    with torch.inference_mode():
        replay_scores = torch.einsum(
            "dsh,vh->dsv", normalized_replay, normalized_embeddings
        ).cpu().contiguous()
    prompt_length = len(primary["prompt_ids"])
    full_sequence_decision_states = torch.stack(
        [
            primary["full_sequence_states"][:, prompt_length + decision_index - 1, :]
            for decision_index in range(primary["decision_states"].shape[0])
        ],
        dim=0,
    )
    normalized_full_sequence = F.normalize(
        full_sequence_decision_states.to(normalized_embeddings.device), p=2, dim=2
    )
    with torch.inference_mode():
        full_sequence_scores = torch.einsum(
            "dsh,vh->dsv", normalized_full_sequence, normalized_embeddings
        ).cpu().contiguous()
    if not (
        torch.isfinite(primary_scores).all()
        and torch.isfinite(replay_scores).all()
        and torch.isfinite(full_sequence_scores).all()
    ):
        raise RuntimeError("Vocabulary projection contains non-finite values.")
    save_file(
        {"cosine_scores": primary_scores},
        str(context.raw_dir / "vocabulary_scores.safetensors"),
        metadata={
            "shape": json.dumps(list(primary_scores.shape)),
            "basis": "input_embedding",
        },
    )
    raw_tokens = tokenizer.convert_ids_to_tokens(list(range(vocabulary_size)))
    decoded_tokens = tokenizer.batch_decode(
        [[token_id] for token_id in range(vocabulary_size)],
        skip_special_tokens=False,
        clean_up_tokenization_spaces=False,
    )
    special_ids = set(map(int, tokenizer.all_special_ids))
    token_classes = [
        topology.classify_token(token_id, decoded_tokens[token_id], special_ids)
        for token_id in range(vocabulary_size)
    ]
    eligible = np.asarray(
        [token_id for token_id in range(vocabulary_size) if token_id not in special_ids],
        dtype=np.int64,
    )
    score_values = primary_scores.numpy()
    full_sequence_score_values = full_sequence_scores.numpy()
    top_count = int(context.config["topology"]["top_tokens_per_sector"])
    required_overlap = int(
        context.config["capture"]["reconciliation_required_top_token_overlap"]
    )
    cutoff_rows: list[dict[str, object]] = []
    top_rows: list[dict[str, object]] = []
    full_sequence_projection_rows: list[dict[str, object]] = []
    memberships: dict[tuple[int, int, str], pd.DataFrame] = {}
    all_memberships: list[pd.DataFrame] = []
    trace = primary["trace_rows"]
    for decision_index in range(primary_scores.shape[0]):
        for state_index, label in enumerate(context.state_labels):
            values = score_values[decision_index, state_index]
            full_sequence_values = full_sequence_score_values[
                decision_index, state_index
            ]
            descending = eligible[np.argsort(-values[eligible], kind="stable")]
            ascending = eligible[np.argsort(values[eligible], kind="stable")]
            full_sequence_descending = eligible[
                np.argsort(-full_sequence_values[eligible], kind="stable")
            ]
            full_sequence_ascending = eligible[
                np.argsort(full_sequence_values[eligible], kind="stable")
            ]
            primary_positive_top = descending[:required_overlap]
            primary_negative_top = ascending[:required_overlap]
            full_sequence_positive_top = full_sequence_descending[:required_overlap]
            full_sequence_negative_top = full_sequence_ascending[:required_overlap]
            positive_overlap = int(
                np.intersect1d(
                    primary_positive_top,
                    full_sequence_positive_top,
                    assume_unique=True,
                ).size
            )
            negative_overlap = int(
                np.intersect1d(
                    primary_negative_top,
                    full_sequence_negative_top,
                    assume_unique=True,
                ).size
            )
            projection_metrics = tensor_pair_metrics(
                primary_scores[decision_index, state_index, eligible],
                full_sequence_scores[decision_index, state_index, eligible],
            )
            full_sequence_projection_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "state_index": state_index,
                    "state_label": label,
                    "required_top_token_overlap": required_overlap,
                    "positive_top_token_overlap": positive_overlap,
                    "negative_top_token_overlap": negative_overlap,
                    "positive_top_token_set_exact": positive_overlap
                    == required_overlap,
                    "negative_top_token_set_exact": negative_overlap
                    == required_overlap,
                    "positive_rank_order_exact": bool(
                        np.array_equal(
                            primary_positive_top, full_sequence_positive_top
                        )
                    ),
                    "negative_rank_order_exact": bool(
                        np.array_equal(
                            primary_negative_top, full_sequence_negative_top
                        )
                    ),
                    **projection_metrics,
                }
            )
            upper = topology.elbow_candidate(values[descending])
            lower_inverse = topology.elbow_candidate(-values[ascending])
            positive_ids = descending[: int(upper["cutoff_rank"])]
            negative_ids = ascending[: int(lower_inverse["cutoff_rank"])]
            if np.intersect1d(positive_ids, negative_ids).size:
                raise RuntimeError(
                    f"Cutoff populations overlap at decision {decision_index}, state {state_index}."
                )
            if len(positive_ids) <= context.settings.k_neighbors or len(negative_ids) <= context.settings.k_neighbors:
                raise RuntimeError("A cutoff population cannot support exact 10-NN analysis.")
            cutoff_rows.append(
                {
                    "decision_index": decision_index,
                    "generated_token_index": decision_index + 1,
                    "state_index": state_index,
                    "state_label": label,
                    "eligible_vocabulary_size": len(eligible),
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
            for side, ids in (
                ("positive_head", positive_ids),
                ("negative_tail", negative_ids),
            ):
                for rank, token_id in enumerate(ids[:top_count], start=1):
                    top_rows.append(
                        {
                            "decision_index": decision_index,
                            "generated_token_index": decision_index + 1,
                            "state_index": state_index,
                            "state_label": label,
                            "side": side,
                            "rank_from_extreme": rank,
                            "token_id": int(token_id),
                            "raw_token": raw_tokens[int(token_id)],
                            "decoded_token": decoded_tokens[int(token_id)],
                            "display_token": topology.visible_token(decoded_tokens[int(token_id)]),
                            "token_class": token_classes[int(token_id)],
                            "cosine_score": float(values[int(token_id)]),
                        }
                    )
                frame = pd.DataFrame(
                    {
                        "prompt_id": f"decision_{decision_index:03d}",
                        "decision_index": decision_index,
                        "generated_token_index": decision_index + 1,
                        "state_index": state_index,
                        "state_label": label,
                        "side": side,
                        "token_id": ids,
                        "raw_token": [raw_tokens[int(item)] for item in ids],
                        "decoded_token": [decoded_tokens[int(item)] for item in ids],
                        "display_token": [
                            topology.visible_token(decoded_tokens[int(item)]) for item in ids
                        ],
                        "token_class": [token_classes[int(item)] for item in ids],
                        "cosine_score": values[ids],
                        "rank_from_extreme": np.arange(1, len(ids) + 1, dtype=np.int32),
                    }
                )
                memberships[(decision_index, state_index, side)] = frame
                all_memberships.append(frame)
    pd.DataFrame(cutoff_rows).to_csv(context.run_dir / "cutoffs.csv", index=False)
    pd.DataFrame(top_rows).to_csv(
        context.run_dir / "top_tokens_by_step_and_state.csv", index=False
    )
    pd.concat(all_memberships, ignore_index=True).to_csv(
        context.run_dir / "tail_tokens.csv.gz", index=False, compression="gzip"
    )
    score_metric_rows: list[dict[str, object]] = []
    if primary_scores.shape == replay_scores.shape:
        for decision_index in range(primary_scores.shape[0]):
            for state_index, label in enumerate(context.state_labels):
                score_metric_rows.append(
                    {
                        "decision_index": decision_index,
                        "generated_token_index": decision_index + 1,
                        "state_index": state_index,
                        "state_label": label,
                        **tensor_pair_metrics(
                            primary_scores[decision_index, state_index],
                            replay_scores[decision_index, state_index],
                        ),
                    }
                )
    pd.DataFrame(score_metric_rows).to_csv(
        context.run_dir / "replay_vocabulary_score_metrics.csv", index=False
    )
    full_sequence_projection_frame = pd.DataFrame(full_sequence_projection_rows)
    full_sequence_projection_frame.to_csv(
        context.run_dir / "full_sequence_projection_reconciliation.csv",
        index=False,
    )
    top_token_sets_exact = bool(
        full_sequence_projection_frame["positive_top_token_set_exact"].all()
        and full_sequence_projection_frame["negative_top_token_set_exact"].all()
    )
    projection_record = {
        "schema_version": 1,
        "score_shape": list(primary_scores.shape),
        "vocabulary_size": vocabulary_size,
        "embedding_rows": embedding_rows,
        "padded_embedding_rows_excluded": embedding_rows - vocabulary_size,
        "special_token_ids_excluded": sorted(special_ids),
        "eligible_vocabulary_size": len(eligible),
        "decision_token_excluded": False,
        "top_tokens_per_sector": top_count,
        "replay_score_exact": bool(torch.equal(primary_scores, replay_scores)),
        "full_sequence_reconciliation_rows": len(full_sequence_projection_frame),
        "full_sequence_required_top_token_overlap": required_overlap,
        "full_sequence_min_positive_top_token_overlap": int(
            full_sequence_projection_frame["positive_top_token_overlap"].min()
        ),
        "full_sequence_min_negative_top_token_overlap": int(
            full_sequence_projection_frame["negative_top_token_overlap"].min()
        ),
        "full_sequence_top_token_sets_exact": top_token_sets_exact,
        "full_sequence_max_absolute_score_difference": float(
            full_sequence_projection_frame["max_absolute_difference"].max()
        ),
        "full_sequence_mean_l2_score_distance": float(
            full_sequence_projection_frame["l2_distance"].mean()
        ),
        "full_sequence_min_score_cosine_similarity": float(
            full_sequence_projection_frame["cosine_similarity"].min()
        ),
    }
    write_json(context.run_dir / "projection_validation.json", projection_record)
    del (
        normalized_primary,
        normalized_replay,
        normalized_full_sequence,
        full_sequence_decision_states,
        primary_scores,
        replay_scores,
        full_sequence_scores,
        embeddings,
    )
    gc.collect()
    return normalized_embeddings, memberships, {
        "raw_tokens": raw_tokens,
        "decoded_tokens": decoded_tokens,
        "token_classes": token_classes,
        "eligible_ids": eligible,
        "vocabulary_size": vocabulary_size,
        "projection_record": projection_record,
        "trace": trace,
    }


def add_decision_identity(
    decision_index: int,
    value: Any,
) -> Any:
    if isinstance(value, pd.DataFrame):
        if "decision_index" not in value.columns:
            value.insert(1, "decision_index", decision_index)
        if "generated_token_index" not in value.columns:
            value.insert(2, "generated_token_index", decision_index + 1)
        return value
    if isinstance(value, dict):
        value["decision_index"] = decision_index
        value["generated_token_index"] = decision_index + 1
        return value
    if isinstance(value, list):
        for item in value:
            item["decision_index"] = decision_index
            item["generated_token_index"] = decision_index + 1
        return value
    raise TypeError(type(value).__name__)


def write_layer_packets(
    path: Path,
    run_id: str,
    state_labels: tuple[str, ...],
    compact_networks: list[dict[str, Any]],
    heading_suffix: str = "",
) -> None:
    lines = [
        f"# {run_id} measured generation-layer packets{heading_suffix}",
        "",
        "Positive and negative denote cosine alignment sectors. Negative does not independently establish suppression.",
        "",
    ]
    by_key = {
        (int(item["decision_index"]), int(item["state_index"]), str(item["side"])): item
        for item in compact_networks
    }
    decision_count = 1 + max(int(item["decision_index"]) for item in compact_networks)
    for decision_index in range(decision_count):
        lines.extend([f"## Generation decision {decision_index + 1:02d}", ""])
        for state_index, label in enumerate(state_labels):
            lines.extend([f"### State {state_index:02d} — {label}", ""])
            for side in SIDES:
                item = by_key[(decision_index, state_index, side)]
                metrics = item["metrics"]
                lines.extend(
                    [
                        f"#### {side}",
                        "",
                        f"- Nodes: {metrics['population_size']}",
                        f"- Communities: {metrics['community_count']}",
                        f"- Modularity: {metrics['community_modularity']:.6f}",
                        "",
                    ]
                )
                for community in item["communities"]:
                    representatives = ", ".join(community["representative_tokens"][:10])
                    extremes = ", ".join(community["most_extreme_tokens"][:6])
                    lines.append(
                        f"- C{community['community_id']} (n={community['community_size']}): "
                        f"representatives [{representatives}]; target-extreme [{extremes}]"
                    )
                lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def shuffled_control(
    context: Context,
    compact: dict[str, Any],
    community_nodes: pd.DataFrame,
    top_tokens: pd.DataFrame,
    vocabulary: dict[str, Any],
) -> dict[str, object]:
    eligible = np.asarray(vocabulary["eligible_ids"], dtype=np.int64)
    rng = np.random.default_rng(int(context.config["controls"]["shuffle_seed"]))
    shuffled_ids = rng.permutation(eligible)
    mapping = {int(source): int(target) for source, target in zip(eligible, shuffled_ids, strict=True)}
    decoded = vocabulary["decoded_tokens"]
    raw = vocabulary["raw_tokens"]
    mapping_frame = pd.DataFrame(
        {
            "source_token_id": eligible,
            "source_decoded_token": [decoded[int(item)] for item in eligible],
            "shuffled_token_id": shuffled_ids,
            "shuffled_decoded_token": [decoded[int(item)] for item in shuffled_ids],
        }
    )
    mapping_path = context.controls_dir / "shuffled_token_mapping.local.csv"
    mapping_frame.to_csv(mapping_path, index=False)

    shuffled_nodes = community_nodes.copy()
    for prefix in ("representative", "most_extreme"):
        id_column = f"{prefix}_token_ids"
        token_column = f"{prefix}_tokens"
        new_ids: list[str] = []
        new_tokens: list[str] = []
        for ids in shuffled_nodes[id_column].fillna("").astype(str):
            source_ids = [int(item) for item in ids.split() if item]
            target_ids = [mapping[item] for item in source_ids]
            new_ids.append(" ".join(map(str, target_ids)))
            new_tokens.append(
                " | ".join(topology.visible_token(decoded[item]) for item in target_ids)
            )
        shuffled_nodes[id_column] = new_ids
        shuffled_nodes[token_column] = new_tokens
    shuffled_nodes["token_class_counts"] = "{}"
    shuffled_nodes.to_csv(context.controls_dir / "shuffled_community_nodes.csv", index=False)

    shuffled_top = top_tokens.copy()
    shuffled_top["token_id"] = shuffled_top["token_id"].map(mapping)
    shuffled_top["raw_token"] = shuffled_top["token_id"].map(
        lambda item: raw[int(item)]
    )
    shuffled_top["decoded_token"] = shuffled_top["token_id"].map(
        lambda item: decoded[int(item)]
    )
    shuffled_top["display_token"] = shuffled_top["decoded_token"].map(
        topology.visible_token
    )
    shuffled_top["token_class"] = "shuffled"
    shuffled_top.to_csv(context.controls_dir / "shuffled_top_tokens.csv", index=False)

    shuffled_compact = copy.deepcopy(compact)
    shuffled_compact["control"] = {
        "type": "deterministic_global_vocabulary_label_permutation",
        "seed": int(context.config["controls"]["shuffle_seed"]),
        "mapping_sha256": sha256_file(mapping_path),
        "structure_preserved": True,
        "semantic_labels_destroyed": True,
    }
    node_index = {
        (
            int(row.decision_index),
            int(row.state_index),
            str(row.side),
            int(row.community_id),
        ): row
        for row in shuffled_nodes.itertuples(index=False)
    }
    for network in shuffled_compact["networks"]:
        for community in network["communities"]:
            row = node_index[
                (
                    int(network["decision_index"]),
                    int(network["state_index"]),
                    str(network["side"]),
                    int(community["community_id"]),
                )
            ]
            community["representative_token_ids"] = [
                int(item) for item in str(row.representative_token_ids).split() if item
            ]
            community["representative_tokens"] = str(row.representative_tokens).split(" | ")
            community["most_extreme_token_ids"] = [
                int(item) for item in str(row.most_extreme_token_ids).split() if item
            ]
            community["most_extreme_tokens"] = str(row.most_extreme_tokens).split(" | ")
            community["token_class_counts"] = {}
    control_json = context.controls_dir / "shuffled_chatgpt_community_networks.json"
    write_json(control_json, shuffled_compact)
    write_layer_packets(
        context.controls_dir / "shuffled_chatgpt_layer_packets.md",
        context.config["run_id"],
        context.state_labels,
        shuffled_compact["networks"],
        heading_suffix=" — shuffled-label control",
    )
    return {
        "mapping_rows": len(mapping_frame),
        "mapping_sha256": sha256_file(mapping_path),
        "control_networks": len(shuffled_compact["networks"]),
        "control_json_sha256": sha256_file(control_json),
    }


def construct_networks(
    context: Context,
    normalized_embeddings: torch.Tensor,
    memberships: dict[tuple[int, int, str], pd.DataFrame],
    vocabulary: dict[str, Any],
) -> tuple[dict[str, object], dict[str, object]]:
    decision_count = 1 + max(key[0] for key in memberships)
    expected_networks = decision_count * context.settings.state_count * len(SIDES)
    metrics: list[dict[str, Any]] = []
    community_rows: list[dict[str, Any]] = []
    community_edge_rows: list[dict[str, Any]] = []
    compact_networks: list[dict[str, Any]] = []
    state_transitions: list[dict[str, Any]] = []
    generation_transitions: list[dict[str, Any]] = []
    matches: list[dict[str, Any]] = []
    previous_generation: dict[tuple[int, str], dict[str, Any]] = {}
    node_count = 0
    edge_count = 0
    nodes_path = context.run_dir / "nodes.csv.gz"
    edges_path = context.run_dir / "edges.csv.gz"
    with gzip.open(nodes_path, "wt", encoding="utf-8", newline="") as node_handle, gzip.open(
        edges_path, "wt", encoding="utf-8", newline=""
    ) as edge_handle:
        for decision_index in range(decision_count):
            previous_layer: dict[str, dict[str, Any]] = {}
            for state_index in range(context.settings.state_count):
                for side_index, side in enumerate(SIDES):
                    network_started = time.perf_counter()
                    (
                        metric,
                        nodes,
                        edges,
                        communities,
                        community_edges,
                        state_data,
                        compact_network,
                    ) = topology.analyze_network(
                        f"decision_{decision_index:03d}",
                        decision_index,
                        state_index,
                        side,
                        side_index,
                        memberships[(decision_index, state_index, side)],
                        normalized_embeddings,
                        int(vocabulary["vocabulary_size"]),
                        context.settings,
                    )
                    add_decision_identity(decision_index, metric)
                    add_decision_identity(decision_index, nodes)
                    add_decision_identity(decision_index, edges)
                    add_decision_identity(decision_index, communities)
                    add_decision_identity(decision_index, community_edges)
                    add_decision_identity(decision_index, compact_network)
                    community_by_id = {
                        int(record["community_id"]): record for record in communities
                    }
                    for compact_community in compact_network["communities"]:
                        record = community_by_id[int(compact_community["community_id"])]
                        compact_community["representative_token_ids"] = [
                            int(item)
                            for item in str(record["representative_token_ids"]).split()
                            if item
                        ]
                        compact_community["most_extreme_token_ids"] = [
                            int(item)
                            for item in str(record["most_extreme_token_ids"]).split()
                            if item
                        ]
                    nodes.to_csv(node_handle, index=False, header=node_count == 0)
                    edges.to_csv(edge_handle, index=False, header=edge_count == 0)
                    node_count += len(nodes)
                    edge_count += len(edges)
                    metrics.append(metric)
                    community_rows.extend(communities)
                    community_edge_rows.extend(community_edges)
                    compact_networks.append(compact_network)
                    if side in previous_layer:
                        comparison = topology.compare_state_data(
                            previous_layer[side], state_data
                        )
                        state_transitions.append(
                            {
                                "comparison_type": "adjacent_transformer_state",
                                "decision_index": decision_index,
                                "generated_token_index": decision_index + 1,
                                "side": side,
                                "source_state_index": state_index - 1,
                                "target_state_index": state_index,
                                "source_state_label": context.state_labels[state_index - 1],
                                "target_state_label": context.state_labels[state_index],
                                **comparison,
                            }
                        )
                        matches.extend(
                            topology.best_community_matches(
                                "adjacent_transformer_state",
                                side,
                                previous_layer[side],
                                state_data,
                                source_decision_index=decision_index,
                                target_decision_index=decision_index,
                                source_state_index=state_index - 1,
                                target_state_index=state_index,
                            )
                        )
                    previous_layer[side] = state_data
                    generation_key = (state_index, side)
                    if generation_key in previous_generation:
                        comparison = topology.compare_state_data(
                            previous_generation[generation_key], state_data
                        )
                        generation_transitions.append(
                            {
                                "comparison_type": "adjacent_generation_decision",
                                "source_decision_index": decision_index - 1,
                                "target_decision_index": decision_index,
                                "source_generated_token_index": decision_index,
                                "target_generated_token_index": decision_index + 1,
                                "state_index": state_index,
                                "state_label": context.state_labels[state_index],
                                "side": side,
                                **comparison,
                            }
                        )
                        matches.extend(
                            topology.best_community_matches(
                                "adjacent_generation_decision",
                                side,
                                previous_generation[generation_key],
                                state_data,
                                source_decision_index=decision_index - 1,
                                target_decision_index=decision_index,
                                source_state_index=state_index,
                                target_state_index=state_index,
                            )
                        )
                    previous_generation[generation_key] = state_data
                    print(
                        f"{context.config['run_id']} network "
                        f"{len(metrics):03d}/{expected_networks}: "
                        f"decision {decision_index + 1:02d}, state {state_index:02d}, "
                        f"{side}, {len(nodes):,} nodes, {len(communities)} communities, "
                        f"{time.perf_counter() - network_started:.2f}s.",
                        flush=True,
                    )
    network_index = pd.DataFrame(metrics).sort_values(
        ["decision_index", "state_index", "side"], kind="stable"
    )
    community_nodes = pd.DataFrame(community_rows).sort_values(
        ["decision_index", "state_index", "side", "community_id"], kind="stable"
    )
    community_edges = pd.DataFrame(community_edge_rows).sort_values(
        ["decision_index", "state_index", "side", "community_a", "community_b"],
        kind="stable",
    )
    state_frame = pd.DataFrame(state_transitions).sort_values(
        ["decision_index", "target_state_index", "side"], kind="stable"
    )
    generation_frame = pd.DataFrame(generation_transitions)
    if generation_frame.empty:
        generation_frame = pd.DataFrame(
            columns=[
                "comparison_type",
                "source_decision_index",
                "target_decision_index",
                "source_generated_token_index",
                "target_generated_token_index",
                "state_index",
                "state_label",
                "side",
            ]
        )
    else:
        generation_frame = generation_frame.sort_values(
            ["target_decision_index", "state_index", "side"], kind="stable"
        )
    match_frame = pd.DataFrame(matches)
    network_index.to_csv(context.run_dir / "network_index.csv", index=False)
    community_nodes.to_csv(context.run_dir / "community_nodes.csv", index=False)
    community_edges.to_csv(context.run_dir / "community_edges.csv", index=False)
    state_frame.to_csv(context.run_dir / "state_transitions.csv", index=False)
    generation_frame.to_csv(context.run_dir / "generation_transitions.csv", index=False)
    match_frame.to_csv(
        context.run_dir / "community_transition_evidence.csv", index=False
    )
    compact = {
        "schema_version": 1,
        "run_id": context.config["run_id"],
        "model": {
            "id": context.config["model"]["id"],
            "revision": context.config["model"]["revision"],
        },
        "evidence_scope": "Semantic-free networks for every generation decision and recorded transformer state. Generated token identities and continuation text are intentionally omitted from this package.",
        "decision_count": decision_count,
        "state_count": context.settings.state_count,
        "state_labels": list(context.state_labels),
        "network_count": len(compact_networks),
        "sides": list(SIDES),
        "community_identity": "community_id is local to one generation decision, state and side",
        "interpretation_boundary": "Positive and negative are cosine-alignment sectors. Communities are measured graph partitions; semantic topic and parent labels are not included.",
        "within_decision_state_transitions": state_frame.to_dict(orient="records"),
        "across_decision_generation_transitions": generation_frame.to_dict(
            orient="records"
        ),
        "networks": compact_networks,
    }
    compact_path = context.run_dir / "chatgpt_community_networks.json"
    write_json(compact_path, compact)
    write_layer_packets(
        context.run_dir / "chatgpt_layer_packets.md",
        context.config["run_id"],
        context.state_labels,
        compact_networks,
    )
    top_tokens = pd.read_csv(context.run_dir / "top_tokens_by_step_and_state.csv")
    control_details = shuffled_control(
        context,
        compact,
        community_nodes,
        top_tokens,
        vocabulary,
    )
    network_details = {
        "decision_count": decision_count,
        "network_count": len(network_index),
        "selected_node_rows": node_count,
        "directed_edge_rows": edge_count,
        "community_rows": len(community_nodes),
        "intercommunity_edge_rows": len(community_edges),
        "within_decision_transition_rows": len(state_frame),
        "across_decision_transition_rows": len(generation_frame),
        "community_match_rows": len(match_frame),
        "nodes_sha256": sha256_file(nodes_path),
        "edges_sha256": sha256_file(edges_path),
    }
    export_details = {
        "chatgpt_networks": len(compact_networks),
        "chatgpt_json_sha256": sha256_file(compact_path),
        "semantic_labels_added": False,
        "generated_tokens_disclosed_in_compact_exports": False,
    }
    return network_details, {**control_details, **export_details}


def logical_csv_rows(path: Path) -> int:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        next(reader)
        return sum(1 for _ in reader)


def validate_outputs(context: Context, write_reports: bool) -> dict[str, Any]:
    trace = pd.read_csv(context.run_dir / "generation_trace.csv")
    decision_count = len(trace)
    if decision_count < 1 or decision_count > int(context.config["generation"]["max_new_tokens"]):
        raise RuntimeError("Generated-token count is outside the frozen bounds.")
    capture_validation = load_json(context.run_dir / "capture_validation.json")
    if capture_validation.get("status") != "successful":
        raise RuntimeError("Capture validation is not successful.")
    if int(capture_validation["generated_token_count"]) != decision_count:
        raise RuntimeError("Capture and trace token counts differ.")
    replay_validation = capture_validation["replay"]
    for field in (
        "generated_token_ids_exact",
        "decision_states_exact",
        "decision_logits_exact",
        "full_sequence_states_exact",
    ):
        if not bool(replay_validation[field]):
            raise RuntimeError(f"Deterministic replay failed: {field}")
    if not bool(
        replay_validation[
            "all_final_sequence_directional_reconciliations_within_tolerance"
        ]
    ):
        raise RuntimeError("Full-sequence directional reconciliation failed.")
    projection_validation = load_json(
        context.run_dir / "projection_validation.json"
    )
    if not bool(projection_validation["replay_score_exact"]):
        raise RuntimeError("Deterministic vocabulary-score replay failed.")
    if not bool(projection_validation["full_sequence_top_token_sets_exact"]):
        raise RuntimeError("Full-sequence projected top-token reconciliation failed.")
    network_index = pd.read_csv(context.run_dir / "network_index.csv")
    communities = pd.read_csv(context.run_dir / "community_nodes.csv")
    state_transitions = pd.read_csv(context.run_dir / "state_transitions.csv")
    generation_transitions = pd.read_csv(context.run_dir / "generation_transitions.csv")
    cutoffs = pd.read_csv(context.run_dir / "cutoffs.csv")
    top_tokens = pd.read_csv(context.run_dir / "top_tokens_by_step_and_state.csv")
    expected_networks = decision_count * context.settings.state_count * len(SIDES)
    expected_state_transitions = (
        decision_count * (context.settings.state_count - 1) * len(SIDES)
    )
    expected_generation_transitions = (
        (decision_count - 1) * context.settings.state_count * len(SIDES)
    )
    expected_cutoffs = decision_count * context.settings.state_count
    expected_top_rows = (
        decision_count
        * context.settings.state_count
        * len(SIDES)
        * int(context.config["topology"]["top_tokens_per_sector"])
    )
    if len(network_index) != expected_networks:
        raise RuntimeError(f"Expected {expected_networks} networks; found {len(network_index)}.")
    if network_index.duplicated(["decision_index", "state_index", "side"]).any():
        raise RuntimeError("Duplicate network identity found.")
    if not (
        network_index["directed_edge_count"]
        == network_index["population_size"] * context.settings.k_neighbors
    ).all():
        raise RuntimeError("Exact neighbour coverage failed.")
    community_totals = communities.groupby(
        ["decision_index", "state_index", "side"]
    )["community_size"].sum().sort_index()
    populations = network_index.set_index(
        ["decision_index", "state_index", "side"]
    )["population_size"].sort_index()
    if not community_totals.equals(populations):
        raise RuntimeError("Community sizes do not reconcile with network populations.")
    if len(state_transitions) != expected_state_transitions:
        raise RuntimeError("Within-decision state-transition coverage is incomplete.")
    if len(generation_transitions) != expected_generation_transitions:
        raise RuntimeError("Across-decision generation-transition coverage is incomplete.")
    if len(cutoffs) != expected_cutoffs:
        raise RuntimeError("Cutoff coverage is incomplete.")
    if len(top_tokens) != expected_top_rows:
        raise RuntimeError("Top-token coverage is incomplete.")
    required = [
        "prompt_records.json",
        "token_alignment.csv",
        "replay_hidden_state_metrics.csv",
        "replay_logit_metrics.csv",
        "replay_vocabulary_score_metrics.csv",
        "full_sequence_projection_reconciliation.csv",
        "projection_validation.json",
        "chatgpt_community_networks.json",
        "chatgpt_layer_packets.md",
        "controls/shuffled_chatgpt_community_networks.json",
        "controls/shuffled_chatgpt_layer_packets.md",
        "local_raw_capture/primary_capture.safetensors",
        "local_raw_capture/replay_capture.safetensors",
        "local_raw_capture/vocabulary_scores.safetensors",
    ]
    for relative in required:
        if not (context.run_dir / relative).is_file():
            raise FileNotFoundError(f"Required R020 artifact is missing: {relative}")
    results = {
        "generated_token_count": decision_count,
        "recorded_state_count": context.settings.state_count,
        "network_count": len(network_index),
        "selected_membership_rows": int(network_index["population_size"].sum()),
        "directed_edge_rows": int(network_index["directed_edge_count"].sum()),
        "state_local_community_count": len(communities),
        "within_decision_transition_rows": len(state_transitions),
        "across_decision_transition_rows": len(generation_transitions),
        "cutoff_rows": len(cutoffs),
        "top_token_rows": len(top_tokens),
        "node_file_logical_rows": logical_csv_rows(context.run_dir / "nodes.csv.gz"),
        "edge_file_logical_rows": logical_csv_rows(context.run_dir / "edges.csv.gz"),
        "replay_generated_tokens_exact": bool(
            capture_validation["replay"]["generated_token_ids_exact"]
        ),
        "replay_hidden_states_exact": bool(
            capture_validation["replay"]["decision_states_exact"]
        ),
        "replay_logits_exact": bool(
            capture_validation["replay"]["decision_logits_exact"]
        ),
        "full_sequence_elementwise_reconciliation_within_tolerance": bool(
            capture_validation["replay"][
                "all_final_sequence_elementwise_reconciliations_within_tolerance"
            ]
        ),
        "full_sequence_directional_reconciliation_within_tolerance": bool(
            capture_validation["replay"][
                "all_final_sequence_directional_reconciliations_within_tolerance"
            ]
        ),
        "full_sequence_top_token_sets_exact": bool(
            projection_validation["full_sequence_top_token_sets_exact"]
        ),
        "full_sequence_min_positive_top_token_overlap": int(
            projection_validation[
                "full_sequence_min_positive_top_token_overlap"
            ]
        ),
        "full_sequence_min_negative_top_token_overlap": int(
            projection_validation[
                "full_sequence_min_negative_top_token_overlap"
            ]
        ),
    }
    if results["node_file_logical_rows"] != results["selected_membership_rows"]:
        raise RuntimeError("Logical node rows do not reconcile.")
    if results["edge_file_logical_rows"] != results["directed_edge_rows"]:
        raise RuntimeError("Logical edge rows do not reconcile.")
    if write_reports:
        write_json(context.run_dir / "measurement_results.json", results)
        verification = [
            "# R020 measurement completeness verification",
            "",
            "- Measurement status: **PASS**",
            f"- Generated-token decisions: {decision_count}",
            f"- Recorded states per decision: {context.settings.state_count}",
            f"- Networks: {len(network_index)} / {expected_networks}",
            f"- Within-decision state transitions: {len(state_transitions)} / {expected_state_transitions}",
            f"- Across-decision generation transitions: {len(generation_transitions)} / {expected_generation_transitions}",
            f"- Selected token memberships: {results['selected_membership_rows']:,}",
            f"- Directed exact 10-NN edges: {results['directed_edge_rows']:,}",
            f"- State-local communities: {len(communities):,}",
            f"- Replay generated tokens exact: {results['replay_generated_tokens_exact']}",
            f"- Replay hidden states exact: {results['replay_hidden_states_exact']}",
            f"- Replay logits exact: {results['replay_logits_exact']}",
            f"- Prefix/full-sequence elementwise diagnostic: {results['full_sequence_elementwise_reconciliation_within_tolerance']}",
            f"- Prefix/full-sequence directional gate: {results['full_sequence_directional_reconciliation_within_tolerance']}",
            f"- Prefix/full-sequence positive top-token overlap: {results['full_sequence_min_positive_top_token_overlap']}/50 minimum",
            f"- Prefix/full-sequence negative top-token overlap: {results['full_sequence_min_negative_top_token_overlap']}/50 minimum",
            f"- Prefix/full-sequence top-token sets exact: {results['full_sequence_top_token_sets_exact']}",
            "- Every selected node belongs to exactly one state-local community.",
            "- Compact measured exports contain no semantic parent labels or generated-token identities.",
            "- Semantic reconstruction and topic-trajectory interpretation remain pending.",
        ]
        (context.run_dir / "R020_COMPLETENESS_VERIFICATION.md").write_text(
            "\n".join(verification) + "\n", encoding="utf-8"
        )
        report = [
            "# R020 semantic-topology measurement report",
            "",
            "## Outcome",
            "",
            "The deterministic Pythia 70M capture, replay, vocabulary projection, topology construction and shuffled-label control completed and validated.",
            "",
            "**Overall run status: awaiting semantic analysis.** The continuation has not been evaluated here, and no semantic topics or parents have been assigned.",
            "",
            "## Run identity",
            "",
            f"- Model: `{context.config['model']['id']}`",
            f"- Revision: `{context.config['model']['revision']}`",
            f"- Prompt hash: `{context.config['prompt']['utf8_sha256']}`",
            f"- Prompt tokens: {capture_validation['prompt_token_count']}",
            f"- Generated-token decisions: {decision_count}",
            f"- Stop reason: `{capture_validation['stop_reason']}`",
            f"- Recorded states per decision: {context.settings.state_count}",
            "- Generation: deterministic greedy argmax",
            "- Generated continuation: deliberately not reproduced in this semantic-free report",
            "",
            "## Coverage",
            "",
            f"- Networks: {len(network_index)}",
            f"- Selected token memberships: {results['selected_membership_rows']:,}",
            f"- Directed exact 10-NN edges: {results['directed_edge_rows']:,}",
            f"- State-local communities: {len(communities):,}",
            f"- Within-decision state transitions: {len(state_transitions)}",
            f"- Across-decision generation transitions: {len(generation_transitions)}",
            f"- Directional full-sequence reconciliation: {results['full_sequence_directional_reconciliation_within_tolerance']}",
            f"- Projected top-token-set reconciliation: {results['full_sequence_top_token_sets_exact']}",
            f"- Elementwise full-sequence diagnostic (retained, not concealed): {results['full_sequence_elementwise_reconciliation_within_tolerance']}",
            "",
            "## Interpretation boundary",
            "",
            "These outputs measure changing vocabulary neighbourhoods, graph partitions and transitions through depth and autoregressive time. They do not yet identify topics, determine whether the visible answer is useful, or establish that an internal structure caused a generated token.",
        ]
        (context.run_dir / "R020_MEASUREMENT_REPORT.md").write_text(
            "\n".join(report) + "\n", encoding="utf-8"
        )
    return results


def artifact_type(path: Path) -> str:
    if path.suffix == ".safetensors":
        return "tensor"
    if path.suffix in {".csv", ".gz"}:
        return "table"
    if path.suffix == ".json":
        return "structured_record"
    if path.suffix == ".md":
        return "report"
    if path.suffix == ".html":
        return "interactive_report"
    return "other"


def build_artifact_index(context: Context) -> dict[str, Any]:
    artifacts: dict[str, Any] = {}
    for path in sorted(context.run_dir.rglob("*")):
        if not path.is_file() or path.name in {"manifest.json", "artifact_index.json"}:
            continue
        relative = str(path.relative_to(context.run_dir)).replace("\\", "/")
        artifacts[relative] = {
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "artifact_type": artifact_type(path),
            "evidence_class": "measurement" if not relative.startswith("analysis/") else "interpretation",
            "tracked_by_git": not (
                path.suffix in {".safetensors", ".gz"}
                or ".local." in path.name
            ),
        }
    index = {
        "schema_version": 1,
        "generated_at": utc_now(),
        "run_id": context.config["run_id"],
        "run_status": "awaiting_semantic_analysis",
        "measurement_status": "measurement_successful",
        "analysis_status": "not_started",
        "self_exclusions": [
            "manifest.json changes after index creation",
            "artifact_index.json cannot hash itself",
        ],
        "artifacts": artifacts,
    }
    write_json(context.run_dir / "artifact_index.json", index)
    return index


def preflight(context: Context) -> dict[str, Any]:
    set_deterministic_runtime(int(context.config["topology"]["random_seed"]))
    model, tokenizer = load_model(context)
    print("R020 preflight: model loaded.", flush=True)
    neutral_prompt = "Technical preflight.\nAnswer:"
    recorder = BlockRecorder(model)
    try:
        encoded = tokenizer(
            neutral_prompt,
            return_tensors="pt",
            add_special_tokens=False,
            return_token_type_ids=False,
        )["input_ids"].to(str(context.config["model"]["device"]))
        states, logits = forward_capture(model, recorder, encoded, full_sequence=False)
        print("R020 preflight: transformer capture complete.", flush=True)
        selected = int(torch.argmax(logits))
        embeddings = F.normalize(
            model.get_input_embeddings().weight[: len(tokenizer)].detach().float(),
            p=2,
            dim=1,
        )
        final = F.normalize(states[-1].to(embeddings.device), p=2, dim=0)
        scores = (embeddings @ final).detach().cpu().numpy()
        print("R020 preflight: vocabulary projection complete.", flush=True)
        eligible = np.asarray(
            [item for item in range(len(tokenizer)) if item not in tokenizer.all_special_ids],
            dtype=np.int64,
        )
        descending = eligible[np.argsort(-scores[eligible], kind="stable")]
        ascending = eligible[np.argsort(scores[eligible], kind="stable")]
        upper = topology.elbow_candidate(scores[descending])
        lower = topology.elbow_candidate(-scores[ascending])
        positive = descending[: int(upper["cutoff_rank"])]
        negative = ascending[: int(lower["cutoff_rank"])]
        print(
            f"R020 preflight: cutoffs positive={len(positive):,}, negative={len(negative):,}.",
            flush=True,
        )
        if len(positive) <= context.settings.k_neighbors or len(negative) <= context.settings.k_neighbors:
            raise RuntimeError("Preflight cutoff population is too small for 10-NN.")
        raw_tokens = tokenizer.convert_ids_to_tokens(list(range(len(tokenizer))))
        decoded = tokenizer.batch_decode(
            [[item] for item in range(len(tokenizer))],
            skip_special_tokens=False,
            clean_up_tokenization_spaces=False,
        )
        print("R020 preflight: vocabulary decoding complete.", flush=True)
        classes = [
            topology.classify_token(item, decoded[item], set(tokenizer.all_special_ids))
            for item in range(len(tokenizer))
        ]
        network_counts = {}
        for side_index, (side, ids) in enumerate(
            (("positive_head", positive), ("negative_tail", negative))
        ):
            full_population_size = len(ids)
            ids = ids[: min(len(ids), 1024)]
            frame = pd.DataFrame(
                {
                    "prompt_id": "preflight",
                    "state_index": context.settings.state_count - 1,
                    "state_label": context.state_labels[-1],
                    "side": side,
                    "token_id": ids,
                    "raw_token": [raw_tokens[int(item)] for item in ids],
                    "decoded_token": [decoded[int(item)] for item in ids],
                    "display_token": [topology.visible_token(decoded[int(item)]) for item in ids],
                    "token_class": [classes[int(item)] for item in ids],
                    "cosine_score": scores[ids],
                    "rank_from_extreme": np.arange(1, len(ids) + 1),
                }
            )
            metric, *_ = topology.analyze_network(
                "preflight",
                0,
                context.settings.state_count - 1,
                side,
                side_index,
                frame,
                embeddings,
                len(tokenizer),
                context.settings,
            )
            network_counts[side] = {
                "full_cutoff_population_size": full_population_size,
                "preflight_network_population_size": metric["population_size"],
                "community_count": metric["community_count"],
            }
            print(f"R020 preflight: {side} test network complete.", flush=True)
        result = {
            "status": "PASS",
            "scientific_evidence_written": False,
            "neutral_prompt": neutral_prompt,
            "state_shape": list(states.shape),
            "logit_shape": list(logits.shape),
            "selected_token_id": selected,
            "selected_token": safe_decode(tokenizer, selected),
            "networks": network_counts,
            "memory": memory_snapshot(),
        }
    finally:
        recorder.close()
        del model, tokenizer
        gc.collect()
        torch.cuda.empty_cache()
    return result


def measure(context: Context) -> None:
    set_deterministic_runtime(int(context.config["topology"]["random_seed"]))
    initialize_manifest(context)
    component = "model_identity"
    model = None
    tokenizer = None
    normalized_embeddings = None
    try:
        started_at = utc_now()
        started = time.perf_counter()
        torch.cuda.reset_peak_memory_stats()
        model, tokenizer = load_model(context)
        metadata = model_metadata(context, model, tokenizer)
        write_json(context.run_dir / "model_metadata.json", metadata)
        update_component(
            context,
            "model_identity",
            started_at,
            started,
            revision=context.config["model"]["revision"],
            model_file_sha256=metadata["files"]["model.safetensors"]["sha256"],
            state_labels=list(context.state_labels),
            memory_after_load=memory_snapshot(),
        )

        component = "primary_capture"
        started_at = utc_now()
        started = time.perf_counter()
        primary = generate_capture(
            context,
            model,
            tokenizer,
            context.config["prompt"]["text"],
            int(context.config["generation"]["max_new_tokens"]),
        )
        update_component(
            context,
            "primary_capture",
            started_at,
            started,
            generated_token_count=len(primary["generated_ids"]),
            stop_reason=primary["stop_reason"],
            decision_state_shape=list(primary["decision_states"].shape),
            full_sequence_state_shape=list(primary["full_sequence_states"].shape),
            peak_gpu_allocated_bytes=int(torch.cuda.max_memory_allocated()),
        )

        component = "deterministic_replay"
        started_at = utc_now()
        started = time.perf_counter()
        replay = generate_capture(
            context,
            model,
            tokenizer,
            context.config["prompt"]["text"],
            int(context.config["generation"]["max_new_tokens"]),
        )
        capture_validation = write_capture_artifacts(
            context, tokenizer, primary, replay
        )
        update_component(
            context,
            "deterministic_replay",
            started_at,
            started,
            **capture_validation["replay"],
        )

        component = "projection_and_cutoffs"
        started_at = utc_now()
        started = time.perf_counter()
        normalized_embeddings, memberships, vocabulary = project_and_select(
            context, model, tokenizer, primary, replay
        )
        update_component(
            context,
            "projection_and_cutoffs",
            started_at,
            started,
            **vocabulary["projection_record"],
            cutoff_rows=len(pd.read_csv(context.run_dir / "cutoffs.csv")),
            top_token_rows=len(
                pd.read_csv(context.run_dir / "top_tokens_by_step_and_state.csv")
            ),
        )
        del primary, replay
        del model
        model = None
        gc.collect()
        torch.cuda.empty_cache()

        component = "networks_and_communities"
        started_at = utc_now()
        started = time.perf_counter()
        network_details, export_control_details = construct_networks(
            context, normalized_embeddings, memberships, vocabulary
        )
        update_component(
            context,
            "networks_and_communities",
            started_at,
            started,
            **network_details,
        )
        update_component(
            context,
            "shuffled_control",
            started_at,
            started,
            mapping_rows=export_control_details["mapping_rows"],
            mapping_sha256=export_control_details["mapping_sha256"],
            control_networks=export_control_details["control_networks"],
            control_json_sha256=export_control_details["control_json_sha256"],
        )
        update_component(
            context,
            "measured_exports",
            started_at,
            started,
            chatgpt_networks=export_control_details["chatgpt_networks"],
            chatgpt_json_sha256=export_control_details["chatgpt_json_sha256"],
            semantic_labels_added=False,
            generated_tokens_disclosed_in_compact_exports=False,
        )

        component = "resource_cleanup"
        started_at = utc_now()
        started = time.perf_counter()
        del normalized_embeddings, memberships, vocabulary, tokenizer
        normalized_embeddings = None
        tokenizer = None
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        update_component(
            context,
            "resource_cleanup",
            started_at,
            started,
            memory_after_cleanup=memory_snapshot(),
        )

        component = "completeness_validation"
        started_at = utc_now()
        started = time.perf_counter()
        results = validate_outputs(context, write_reports=True)
        update_component(
            context,
            "completeness_validation",
            started_at,
            started,
            **results,
        )
        index = build_artifact_index(context)
        manifest = load_json(context.manifest_path)
        for name in COMPONENTS:
            if manifest["components"].get(name, {}).get("status") != "successful":
                raise RuntimeError(f"Required component is not successful: {name}")
        manifest["measurement_status"] = "measurement_successful"
        manifest["analysis_status"] = "not_started"
        manifest["run_status"] = "awaiting_semantic_analysis"
        manifest["measurement_completed_at"] = utc_now()
        manifest["failure_details"] = None
        manifest["results"] = results
        manifest["artifact_index"] = {
            "relative_path": "artifact_index.json",
            "bytes": (context.run_dir / "artifact_index.json").stat().st_size,
            "sha256": sha256_file(context.run_dir / "artifact_index.json"),
            "indexed_artifact_count": len(index["artifacts"]),
        }
        write_json(context.manifest_path, manifest)
        print(
            json.dumps(
                {
                    "run_id": context.config["run_id"],
                    "run_status": manifest["run_status"],
                    "measurement_status": manifest["measurement_status"],
                    "analysis_status": manifest["analysis_status"],
                    "results": results,
                },
                indent=2,
            ),
            flush=True,
        )
    except BaseException as error:
        try:
            if model is not None:
                del model
            if tokenizer is not None:
                del tokenizer
            if normalized_embeddings is not None:
                del normalized_embeddings
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        finally:
            fail_measurement(context, component, error)
        raise


def verify(context: Context) -> dict[str, Any]:
    if not context.manifest_path.is_file():
        raise FileNotFoundError("R020 manifest is missing.")
    manifest = load_json(context.manifest_path)
    if manifest.get("measurement_status") != "measurement_successful":
        raise RuntimeError("R020 measurement is not successful.")
    index_path = context.run_dir / "artifact_index.json"
    index = load_json(index_path)
    if sha256_file(index_path) != manifest["artifact_index"]["sha256"]:
        raise RuntimeError("Artifact-index hash differs from the manifest.")
    for relative, record in index["artifacts"].items():
        path = context.run_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"Indexed artifact is missing: {relative}")
        if path.stat().st_size != int(record["bytes"]):
            raise RuntimeError(f"Indexed artifact size changed: {relative}")
        if sha256_file(path) != record["sha256"]:
            raise RuntimeError(f"Indexed artifact hash changed: {relative}")
    results = validate_outputs(context, write_reports=False)
    if results != manifest["results"]:
        raise RuntimeError("Recomputed completeness results differ from the manifest.")
    return {
        "status": "PASS",
        "run_id": context.config["run_id"],
        "run_status": manifest["run_status"],
        "measurement_status": manifest["measurement_status"],
        "analysis_status": manifest["analysis_status"],
        "artifact_count": len(index["artifacts"]),
        **results,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("validate-config", "preflight", "measure", "verify")
    )
    parser.add_argument("--config", required=True, type=Path)
    arguments = parser.parse_args()
    context = load_context(arguments.config)
    if arguments.action == "validate-config":
        print(
            json.dumps(
                {
                    "status": "valid",
                    "run_id": context.config["run_id"],
                    "model_revision": context.config["model"]["revision"],
                    "state_labels": list(context.state_labels),
                    "prompt_sha256": context.config["prompt"]["utf8_sha256"],
                    "run_directory_exists": context.run_dir.is_dir(),
                    "manifest_exists": context.manifest_path.exists(),
                },
                indent=2,
            )
        )
    elif arguments.action == "preflight":
        print(json.dumps(preflight(context), indent=2))
    elif arguments.action == "measure":
        measure(context)
    else:
        print(json.dumps(verify(context), indent=2))


if __name__ == "__main__":
    main()
