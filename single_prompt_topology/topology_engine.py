"""Configuration-driven measurement engine for R018 and later topology runs."""

from __future__ import annotations

import csv
import gc
import gzip
import hashlib
import itertools
import json
import shutil
import sys
import time
import traceback
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import psutil
import torch
import torch.nn.functional as F
from accelerate import infer_auto_device_map, init_empty_weights
from safetensors import safe_open
from safetensors.torch import save_file
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

from topology_core import (
    TopologySettings,
    analyze_network,
    best_community_matches,
    classify_token,
    compare_state_data,
    elbow_candidate,
    state_label,
    visible_token,
)


PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
CONFIG_SCHEMA_VERSION = 1
MANIFEST_SCHEMA_VERSION = 3
SIDES = ("positive_head", "negative_tail")

MEASUREMENT_COMPONENTS = (
    "configuration_lock",
    "environment_preflight",
    "model_identity",
    "prompt_preflight",
    "batched_capture",
    "deterministic_replay",
    "projection_and_cutoffs",
    "networks_and_communities",
    "within_prompt_transitions",
    "pairwise_permutation_comparisons",
    "permutation_invariance",
    "measured_exports",
    "completeness_validation",
    "resource_cleanup",
)


@dataclass(frozen=True)
class RunContext:
    config_path: Path
    config: dict[str, Any]
    plan_path: Path
    run_dir: Path
    manifest_path: Path
    snapshot_dir: Path
    offload_dir: Path
    prompt_ids: tuple[str, ...]
    settings: TopologySettings


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
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


def _require(mapping: dict[str, Any], key: str, where: str) -> Any:
    if key not in mapping:
        raise ValueError(f"Missing required configuration field: {where}.{key}")
    return mapping[key]


def _analysis_required(config: dict[str, Any]) -> bool:
    return bool(config.get("analysis", {}).get("required", True))


def _post_measurement_run_status(config: dict[str, Any]) -> str:
    if _analysis_required(config):
        return "awaiting_semantic_analysis"
    return "measurement_complete"


def _measurement_report_names(config: dict[str, Any]) -> tuple[str, str]:
    prefix = f"R{int(config['run_number']):03d}"
    reports = config.get("reports", {})
    verification = str(
        reports.get(
            "measurement_completeness",
            f"{prefix}_MEASUREMENT_COMPLETENESS_VERIFICATION.md",
        )
    )
    measurement = str(
        reports.get("measurement_report", f"{prefix}_MEASUREMENT_REPORT.md")
    )
    for name in (verification, measurement):
        if Path(name).name != name or not name.endswith(".md"):
            raise ValueError("Report names must be Markdown filenames without directories.")
    return verification, measurement


def load_and_validate_config(config_path: Path) -> RunContext:
    config_path = config_path.resolve()
    config = load_json(config_path)
    if config.get("schema_version") != CONFIG_SCHEMA_VERSION:
        raise ValueError(
            f"Expected configuration schema {CONFIG_SCHEMA_VERSION}; "
            f"found {config.get('schema_version')!r}."
        )
    run_id = str(_require(config, "run_id", "root"))
    run_number = int(_require(config, "run_number", "root"))
    if not run_id.startswith(f"R{run_number:03d}_"):
        raise ValueError("run_id and run_number do not agree.")
    analysis = config.get("analysis", {})
    if not isinstance(analysis, dict):
        raise ValueError("analysis must be an object when supplied.")
    if "required" in analysis and not isinstance(analysis["required"], bool):
        raise ValueError("analysis.required must be a boolean.")
    reports = config.get("reports", {})
    if not isinstance(reports, dict):
        raise ValueError("reports must be an object when supplied.")
    _measurement_report_names(config)
    plan_path = (PIPELINE_DIR / str(_require(config, "plan_path", "root"))).resolve()
    run_dir = (PIPELINE_DIR / str(_require(config, "output_directory", "root"))).resolve()
    if not plan_path.is_file():
        raise FileNotFoundError(f"Locked plan is missing: {plan_path}")
    expected_runs_root = (PIPELINE_DIR / "runs").resolve()
    if run_dir.parent != expected_runs_root:
        raise ValueError("output_directory must be a direct child of runs/.")
    if run_dir.name != run_id:
        raise ValueError("output_directory name must equal run_id.")

    model = _require(config, "model", "root")
    capture = _require(config, "capture", "root")
    measurement = _require(config, "measurement", "root")
    expected = _require(config, "expected", "root")
    concepts = _require(config, "concepts", "root")
    prompts = _require(config, "prompts", "root")
    if not isinstance(prompts, list) or not prompts:
        raise ValueError("prompts must be a non-empty list.")
    prompt_ids = tuple(str(_require(item, "prompt_id", "prompt")) for item in prompts)
    if len(set(prompt_ids)) != len(prompt_ids):
        raise ValueError("Prompt IDs must be unique.")
    if int(expected["prompt_count"]) != len(prompts):
        raise ValueError("Expected prompt_count does not match prompts.")
    anchor_text = str(capture["anchor_text"])
    if anchor_text != "\n":
        raise ValueError("Schema v1 supports the locked newline anchor only.")
    if capture.get("chat_template_used") or capture.get("response_generation"):
        raise ValueError("Topology measurement must not use chat templates or generation.")
    if capture.get("add_special_tokens"):
        raise ValueError("Topology measurement must not add special tokens.")
    if int(capture["batch_size"]) < 1:
        raise ValueError("batch_size must be positive.")
    if not capture.get("deterministic_replay"):
        raise ValueError("Schema v1 requires deterministic replay.")

    for prompt in prompts:
        prompt_id = str(prompt["prompt_id"])
        order = list(prompt["concept_order"])
        if sorted(order) != sorted(concepts):
            raise ValueError(f"{prompt_id}: concept_order is not a complete permutation.")
        expected_text = "".join(f"{concepts[key]}{anchor_text}" for key in order)
        if prompt["raw_text"] != expected_text:
            raise ValueError(f"{prompt_id}: raw_text does not match concept_order.")
        if prompt.get("permutation") != "".join(order):
            raise ValueError(f"{prompt_id}: permutation label does not match concept_order.")
        if not prompt.get("comparison_group"):
            raise ValueError(f"{prompt_id}: comparison_group is required.")

    expected_layers = int(model["expected_layers"])
    expected_states = int(model["expected_states"])
    if expected_states != expected_layers + 1:
        raise ValueError("expected_states must equal expected_layers + 1.")
    sectors = tuple(measurement["sectors"])
    if sectors != SIDES:
        raise ValueError(f"Sectors must remain {SIDES!r}.")
    prompt_count = len(prompts)
    pair_count = sum(
        len(list(itertools.combinations(group, 2)))
        for group in _comparison_groups(config).values()
    )
    calculated = {
        "network_count": prompt_count * expected_states * len(SIDES),
        "within_prompt_transition_rows": prompt_count
        * (expected_states - 1)
        * len(SIDES),
        "pairwise_permutation_rows": pair_count * expected_states * len(SIDES),
        "invariance_summary_rows": expected_states
        * len(SIDES)
        * 2
        * prompt_count,
        "hidden_state_pair_rows": pair_count * expected_states,
    }
    for key, value in calculated.items():
        if int(expected[key]) != value:
            raise ValueError(f"Expected {key}={value}; configuration says {expected[key]}.")

    snapshot_dir = Path(str(model["snapshot_directory"])).resolve()
    offload_dir = Path(str(model["offload_directory"])).resolve()
    if not snapshot_dir.is_dir():
        raise FileNotFoundError(f"Cached model snapshot is missing: {snapshot_dir}")
    if snapshot_dir.name != str(model["revision"]):
        raise ValueError("Snapshot directory does not end in the locked revision.")
    settings = TopologySettings(
        state_count=expected_states,
        layer_count=expected_layers,
        k_neighbors=int(measurement["k_neighbors"]),
        knn_batch_size=int(measurement["knn_batch_size"]),
        random_seed=int(measurement["random_seed"]),
        louvain_resolution=float(measurement["louvain_resolution"]),
    )
    if settings.k_neighbors != 10:
        raise ValueError("Schema v1 preserves the exact 10-NN method.")
    return RunContext(
        config_path=config_path,
        config=config,
        plan_path=plan_path,
        run_dir=run_dir,
        manifest_path=run_dir / "manifest.json",
        snapshot_dir=snapshot_dir,
        offload_dir=offload_dir,
        prompt_ids=prompt_ids,
        settings=settings,
    )


def _comparison_groups(config: dict[str, Any]) -> dict[str, list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for prompt in config["prompts"]:
        groups[str(prompt["comparison_group"])].append(str(prompt["prompt_id"]))
    return dict(groups)


def memory_snapshot(path: Path) -> dict[str, object]:
    virtual = psutil.virtual_memory()
    process = psutil.Process()
    snapshot: dict[str, object] = {
        "physical_ram_available_bytes": int(virtual.available),
        "process_rss_bytes": int(process.memory_info().rss),
        "model_drive_free_bytes": int(shutil.disk_usage(path.anchor).free),
    }
    if torch.cuda.is_available():
        free_bytes, total_bytes = torch.cuda.mem_get_info()
        snapshot.update(
            {
                "gpu_name": torch.cuda.get_device_name(0),
                "gpu_total_bytes": int(total_bytes),
                "gpu_free_bytes": int(free_bytes),
                "gpu_allocated_bytes": int(torch.cuda.memory_allocated()),
                "gpu_reserved_bytes": int(torch.cuda.memory_reserved()),
            }
        )
    return snapshot


def initialize_manifest(context: RunContext) -> dict[str, Any]:
    if context.run_dir.exists():
        raise FileExistsError(
            f"Run directory already exists; refusing to overwrite or resume: {context.run_dir}"
        )
    if not torch.cuda.is_available():
        raise RuntimeError("The configured OLMo measurement requires CUDA.")
    context.run_dir.mkdir(parents=True)
    started = utc_now()
    components = {name: {"status": "pending"} for name in MEASUREMENT_COMPONENTS}
    components["configuration_lock"] = {
        "status": "successful",
        "started_at": started,
        "completed_at": started,
        "elapsed_seconds": 0.0,
        "config_sha256": sha256_file(context.config_path),
        "plan_sha256": sha256_file(context.plan_path),
    }
    components["environment_preflight"] = {
        "status": "successful",
        "started_at": started,
        "completed_at": started,
        "elapsed_seconds": 0.0,
        "python": sys.version,
        "torch": torch.__version__,
        "cuda": torch.version.cuda,
        "memory_before": memory_snapshot(context.snapshot_dir),
    }
    manifest: dict[str, Any] = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "run_id": context.config["run_id"],
        "run_number": context.config["run_number"],
        "run_status": "measurement_running",
        "measurement_status": "measurement_running",
        "analysis_required": _analysis_required(context.config),
        "analysis_status": (
            "not_started" if _analysis_required(context.config) else "not_required"
        ),
        "started_at": started,
        "measurement_completed_at": None,
        "failure_details": None,
        "objective": context.config["objective"],
        "model": context.config["model"],
        "capture": context.config["capture"],
        "prompt_definitions": context.config["prompts"],
        "expected": context.config["expected"],
        "required_components": list(MEASUREMENT_COMPONENTS),
        "components": components,
        "artifact_index": None,
        "results": {},
        "interpretation_boundary": (
            "Measurement ends at hidden states, scores, cutoffs, graph communities, "
            "transitions, permutation comparisons and support counts. Semantic parent "
            "identities and relations are not measurement outputs."
        ),
    }
    write_json(context.manifest_path, manifest)
    return manifest


def update_component(
    context: RunContext,
    name: str,
    started_at: str,
    started_perf: float,
    **details: object,
) -> None:
    manifest = load_json(context.manifest_path)
    manifest["components"][name] = {
        "status": "successful",
        "started_at": started_at,
        "completed_at": utc_now(),
        "elapsed_seconds": time.perf_counter() - started_perf,
        **details,
    }
    write_json(context.manifest_path, manifest)


def fail_measurement(context: RunContext, component: str, error: BaseException) -> None:
    if not context.manifest_path.exists():
        return
    manifest = load_json(context.manifest_path)
    failed_at = utc_now()
    manifest["run_status"] = "measurement_failed"
    manifest["measurement_status"] = "measurement_failed"
    manifest["failure_details"] = {
        "component": component,
        "error_type": type(error).__name__,
        "message": str(error),
        "traceback": traceback.format_exc(),
        "failed_at": failed_at,
        "memory_at_failure": memory_snapshot(context.snapshot_dir),
    }
    manifest["components"][component] = {
        "status": "failed",
        "completed_at": failed_at,
        "error_type": type(error).__name__,
        "message": str(error),
    }
    write_json(context.manifest_path, manifest)


def _model_identity(context: RunContext) -> dict[str, Any]:
    model = context.config["model"]
    config_path = context.snapshot_dir / "config.json"
    index_path = context.snapshot_dir / "model.safetensors.index.json"
    tokenizer_paths = [
        path
        for name in (
            "tokenizer.json",
            "tokenizer_config.json",
            "special_tokens_map.json",
            "generation_config.json",
        )
        if (path := context.snapshot_dir / name).is_file()
    ]
    if not config_path.is_file() or not index_path.is_file():
        raise FileNotFoundError("Model configuration or Safetensors index is missing.")
    auto_config = AutoConfig.from_pretrained(context.snapshot_dir, local_files_only=True)
    observed = {
        "layers": int(auto_config.num_hidden_layers),
        "hidden_width": int(auto_config.hidden_size),
        "config_sha256": sha256_file(config_path),
        "weight_index_sha256": sha256_file(index_path),
        "tokenizer_metadata": {
            path.name: sha256_file(path) for path in tokenizer_paths
        },
    }
    if observed["layers"] != int(model["expected_layers"]):
        raise RuntimeError("Model layer count does not match the locked configuration.")
    if observed["hidden_width"] != int(model["hidden_width"]):
        raise RuntimeError("Model hidden width does not match the locked configuration.")
    index = load_json(index_path)
    if model["embedding_key"] not in index.get("weight_map", {}):
        raise RuntimeError("Locked input-embedding tensor is absent from the weight index.")
    return observed


def _capture_batch(
    model: Any,
    encoded: dict[str, torch.Tensor],
    capture_indices: torch.Tensor,
    state_count: int,
) -> torch.Tensor:
    device_inputs = {name: tensor.to("cuda:0") for name, tensor in encoded.items()}
    with torch.inference_mode():
        output = model(
            **device_inputs,
            output_hidden_states=True,
            use_cache=False,
            return_dict=True,
        )
    states = output.hidden_states
    if states is None or len(states) != state_count:
        raise RuntimeError(
            f"Expected {state_count} hidden states; found {0 if states is None else len(states)}."
        )
    captured_states: list[torch.Tensor] = []
    for state in states:
        state_rows = torch.arange(capture_indices.numel(), device=state.device)
        state_indices = capture_indices.to(state.device)
        captured_states.append(
            state[state_rows, state_indices]
            .detach()
            .to(device="cpu", dtype=torch.bfloat16)
        )
    trajectories = torch.stack(captured_states, dim=1).contiguous()
    del output, states, device_inputs, captured_states
    return trajectories


def final_non_padding_indices(attention_mask: torch.Tensor) -> torch.Tensor:
    """Return the last attended index for right-padded prompt rows."""
    if attention_mask.ndim != 2 or attention_mask.shape[1] == 0:
        raise ValueError("attention_mask must be a non-empty two-dimensional tensor.")
    if not torch.all((attention_mask == 0) | (attention_mask == 1)):
        raise ValueError("attention_mask must contain only zero and one values.")
    lengths = attention_mask.sum(dim=1).to(torch.long)
    if torch.any(lengths <= 0):
        raise ValueError("Every prompt must contain at least one attended token.")
    expected = (
        torch.arange(attention_mask.shape[1], device=attention_mask.device)[None, :]
        < lengths[:, None]
    ).to(attention_mask.dtype)
    if not torch.equal(attention_mask, expected):
        raise ValueError("Schema v1 requires contiguous right padding.")
    return lengths - 1


def _prepare_prompt_batch(
    context: RunContext,
) -> tuple[Any, dict[str, torch.Tensor], torch.Tensor, dict[str, Any], int]:
    """Tokenize and validate every capture position before model weights are loaded."""
    tokenizer = AutoTokenizer.from_pretrained(context.snapshot_dir, local_files_only=True)
    tokenizer.padding_side = "right"
    if tokenizer.pad_token_id is None:
        if tokenizer.eos_token_id is None:
            raise RuntimeError("Tokenizer has neither a pad token nor an EOS token.")
        tokenizer.pad_token = tokenizer.eos_token
    if len(tokenizer) != int(context.config["model"]["usable_vocabulary_size"]):
        raise RuntimeError("Tokenizer vocabulary size does not match the locked configuration.")

    anchor_ids = tokenizer.encode(
        context.config["capture"]["anchor_text"], add_special_tokens=False
    )
    if len(anchor_ids) != 1:
        raise RuntimeError(f"Newline anchor is not one token: {anchor_ids}")
    anchor_token_id = int(anchor_ids[0])
    prompts = context.config["prompts"]
    raw_texts = [str(prompt["raw_text"]) for prompt in prompts]
    encoded_batch = tokenizer(
        raw_texts,
        return_tensors="pt",
        padding=True,
        add_special_tokens=False,
        return_token_type_ids=False,
    )
    encoded = {name: tensor for name, tensor in encoded_batch.items()}
    attention_mask = encoded["attention_mask"]
    capture_indices = final_non_padding_indices(attention_mask)
    prompt_records: dict[str, Any] = {}
    for row, prompt in enumerate(prompts):
        prompt_id = str(prompt["prompt_id"])
        capture_index = int(capture_indices[row])
        token_id = int(encoded["input_ids"][row, capture_index])
        if token_id != anchor_token_id:
            raise RuntimeError(f"{prompt_id}: capture position is not the newline anchor.")
        length = int(attention_mask[row].sum())
        input_ids = encoded["input_ids"][row, :length].tolist()
        prompt_records[prompt_id] = {
            **prompt,
            "input_ids": input_ids,
            "tokens": tokenizer.convert_ids_to_tokens(input_ids),
            "input_token_count": length,
            "capture_index": capture_index,
            "capture_token_id": token_id,
            "capture_token": tokenizer.convert_ids_to_tokens([token_id])[0],
            "padding_side": tokenizer.padding_side,
            "padded_sequence_length": int(encoded["input_ids"].shape[1]),
            "chat_template_used": False,
            "special_tokens_added": False,
            "response_generation_executed": False,
        }
    return tokenizer, encoded, capture_indices, prompt_records, anchor_token_id


def capture_hidden_states(context: RunContext) -> None:
    identity_started_at = utc_now()
    identity_started = time.perf_counter()
    identity = _model_identity(context)
    update_component(
        context,
        "model_identity",
        identity_started_at,
        identity_started,
        **identity,
    )

    preflight_started_at = utc_now()
    preflight_started = time.perf_counter()
    tokenizer, encoded, capture_indices, prompt_records, anchor_token_id = (
        _prepare_prompt_batch(context)
    )
    write_json(context.run_dir / "prompt_records.json", prompt_records)
    update_component(
        context,
        "prompt_preflight",
        preflight_started_at,
        preflight_started,
        prompt_count=len(context.prompt_ids),
        anchor_token_id=anchor_token_id,
        input_token_counts={
            prompt_id: int(record["input_token_count"])
            for prompt_id, record in prompt_records.items()
        },
        validated_before_model_load=True,
    )

    started_at = utc_now()
    started = time.perf_counter()
    model_config = AutoConfig.from_pretrained(context.snapshot_dir, local_files_only=True)
    with init_empty_weights():
        empty_model = AutoModelForCausalLM.from_config(model_config, dtype=torch.bfloat16)
    no_split = list(getattr(empty_model, "_no_split_modules", None) or ["Olmo3DecoderLayer"])
    max_memory = {
        0: context.config["model"]["gpu_memory_limit"],
        "cpu": context.config["model"]["cpu_memory_limit"],
    }
    device_map = infer_auto_device_map(
        empty_model,
        max_memory=max_memory,
        no_split_module_classes=no_split,
        dtype=torch.bfloat16,
        offload_buffers=True,
        fallback_allocation=True,
    )
    del empty_model
    gc.collect()
    if "disk" not in {str(value) for value in device_map.values()}:
        raise RuntimeError("Locked OLMo placement unexpectedly contains no disk modules.")
    write_json(
        context.run_dir / "device_map.json",
        {
            "model": context.config["model"]["id"],
            "revision": context.config["model"]["revision"],
            "max_memory": max_memory,
            "device_map": {str(key): str(value) for key, value in device_map.items()},
        },
    )

    context.offload_dir.mkdir(parents=True, exist_ok=True)
    torch.manual_seed(0)
    torch.cuda.manual_seed_all(0)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    model = AutoModelForCausalLM.from_pretrained(
        context.snapshot_dir,
        revision=context.config["model"]["revision"],
        dtype=torch.bfloat16,
        device_map=device_map,
        max_memory=max_memory,
        offload_folder=context.offload_dir,
        offload_state_dict=True,
        offload_buffers=True,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model.eval()
    attention_mask = encoded["attention_mask"]

    torch.cuda.reset_peak_memory_stats()
    first_started = time.perf_counter()
    first = _capture_batch(
        model,
        encoded,
        capture_indices,
        context.settings.state_count,
    )
    torch.cuda.synchronize()
    first_seconds = time.perf_counter() - first_started
    replay_started = time.perf_counter()
    replay = _capture_batch(
        model,
        encoded,
        capture_indices,
        context.settings.state_count,
    )
    torch.cuda.synchronize()
    replay_seconds = time.perf_counter() - replay_started
    expected_shape = (
        len(context.prompt_ids),
        context.settings.state_count,
        int(context.config["model"]["hidden_width"]),
    )
    if tuple(first.shape) != expected_shape:
        raise RuntimeError(f"Unexpected capture shape: {tuple(first.shape)}")
    if not torch.isfinite(first.float()).all():
        raise RuntimeError("Captured trajectories contain non-finite values.")
    deterministic_exact = bool(torch.equal(first, replay))
    if not deterministic_exact:
        raise RuntimeError("Deterministic batch replay differs from the first capture.")
    if not all(torch.equal(first[0, 0], first[index, 0]) for index in range(1, len(context.prompt_ids))):
        raise RuntimeError("State 00 differs across permutations.")
    capture_path = context.run_dir / "anchor_hidden_states.safetensors"
    save_file(
        {"anchor_hidden_states": first},
        str(capture_path),
        metadata={
            "model_id": context.config["model"]["id"],
            "revision": context.config["model"]["revision"],
            "prompt_ids": ",".join(context.prompt_ids),
            "anchor_token_id": str(anchor_token_id),
        },
    )

    pair_rows: list[dict[str, Any]] = []
    for group_name, group_prompt_ids in _comparison_groups(context.config).items():
        for source_id, target_id in itertools.combinations(group_prompt_ids, 2):
            source_index = context.prompt_ids.index(source_id)
            target_index = context.prompt_ids.index(target_id)
            source = first[source_index].float()
            target = first[target_index].float()
            cosine = F.cosine_similarity(source, target, dim=1)
            l2 = torch.linalg.vector_norm(source - target, dim=1)
            exact = torch.all(first[source_index] == first[target_index], dim=1)
            for state_index in range(context.settings.state_count):
                pair_rows.append(
                    {
                        "comparison_group": group_name,
                        "source_prompt_id": source_id,
                        "target_prompt_id": target_id,
                        "state_index": state_index,
                        "state_label": state_label(state_index, context.settings),
                        "cosine_similarity": float(cosine[state_index]),
                        "l2_distance": float(l2[state_index]),
                        "exact_equal": bool(exact[state_index]),
                    }
                )
    pd.DataFrame(pair_rows).to_csv(
        context.run_dir / "pairwise_hidden_state_metrics.csv", index=False
    )
    validation = {
        "status": "successful",
        "prompt_count": len(context.prompt_ids),
        "prompt_ids": list(context.prompt_ids),
        "state_count": context.settings.state_count,
        "hidden_width": int(context.config["model"]["hidden_width"]),
        "all_finite": True,
        "deterministic_replay_exact": deterministic_exact,
        "anchor_token_id": anchor_token_id,
        "anchor_matches_all_prompts": True,
        "state_00_exact_equal_all_prompts": True,
        "pair_state_metric_rows": len(pair_rows),
    }
    write_json(context.run_dir / "capture_validation.json", validation)
    update_component(
        context,
        "batched_capture",
        started_at,
        started,
        prompt_count=len(context.prompt_ids),
        capture_shape=list(first.shape),
        capture_seconds=first_seconds,
        replay_seconds=replay_seconds,
        peak_gpu_allocated_bytes=int(torch.cuda.max_memory_allocated()),
        memory_after_capture=memory_snapshot(context.snapshot_dir),
    )
    replay_component_started_at = utc_now()
    replay_component_started = time.perf_counter()
    update_component(
        context,
        "deterministic_replay",
        replay_component_started_at,
        replay_component_started,
        exact_equal=deterministic_exact,
        pair_state_metric_rows=len(pair_rows),
        state_00_exact_equal_all_prompts=True,
    )

    cleanup_started_at = utc_now()
    cleanup_started = time.perf_counter()
    del model, tokenizer, encoded, attention_mask, capture_indices, first, replay
    gc.collect()
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    update_component(
        context,
        "resource_cleanup",
        cleanup_started_at,
        cleanup_started,
        phase="post_capture",
        offload_directory=str(context.offload_dir),
        memory_after_cleanup=memory_snapshot(context.snapshot_dir),
    )


def project_and_select(
    context: RunContext,
) -> tuple[
    torch.Tensor,
    dict[tuple[str, int, str], pd.DataFrame],
    list[str],
    int,
]:
    started_at = utc_now()
    started = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(context.snapshot_dir, local_files_only=True)
    vocabulary_size = len(tokenizer)
    if vocabulary_size != int(context.config["model"]["usable_vocabulary_size"]):
        raise RuntimeError("Tokenizer vocabulary size changed after capture.")
    special_ids = set(map(int, tokenizer.all_special_ids))
    raw_tokens = tokenizer.convert_ids_to_tokens(list(range(vocabulary_size)))
    decoded_tokens = [
        tokenizer.decode(
            [token_id],
            skip_special_tokens=False,
            clean_up_tokenization_spaces=False,
        )
        for token_id in range(vocabulary_size)
    ]
    token_classes = [
        classify_token(token_id, decoded_tokens[token_id], special_ids)
        for token_id in range(vocabulary_size)
    ]
    prompt_records = load_json(context.run_dir / "prompt_records.json")
    capture_token_ids = {
        int(prompt_records[prompt_id]["capture_token_id"])
        for prompt_id in context.prompt_ids
    }
    if len(capture_token_ids) != 1:
        raise RuntimeError("Prompts do not share one capture-token ID.")
    capture_token_id = capture_token_ids.pop()

    index = load_json(context.snapshot_dir / "model.safetensors.index.json")
    embedding_key = context.config["model"]["embedding_key"]
    shard_name = index["weight_map"].get(embedding_key)
    if not shard_name:
        raise KeyError(f"Missing embedding tensor: {embedding_key}")
    with safe_open(
        str(context.snapshot_dir / shard_name), framework="pt", device="cpu"
    ) as handle:
        embeddings = handle.get_tensor(embedding_key)
    hidden_width = int(context.config["model"]["hidden_width"])
    if embeddings.ndim != 2 or embeddings.shape[1] != hidden_width:
        raise RuntimeError(f"Unexpected embedding matrix shape: {tuple(embeddings.shape)}")
    full_embedding_rows = int(embeddings.shape[0])
    if full_embedding_rows < vocabulary_size:
        raise RuntimeError("Embedding table is smaller than the tokenizer vocabulary.")
    embeddings = embeddings[:vocabulary_size]
    with safe_open(
        str(context.run_dir / "anchor_hidden_states.safetensors"),
        framework="pt",
        device="cpu",
    ) as handle:
        hidden_states = handle.get_tensor("anchor_hidden_states").float()
    expected_shape = (
        len(context.prompt_ids),
        context.settings.state_count,
        hidden_width,
    )
    if tuple(hidden_states.shape) != expected_shape:
        raise RuntimeError(f"Unexpected saved trajectory shape: {tuple(hidden_states.shape)}")

    normalized_embeddings = F.normalize(
        embeddings.to("cuda", dtype=torch.float32), p=2, dim=1
    )
    normalized_states = F.normalize(
        hidden_states.to("cuda", dtype=torch.float32), p=2, dim=2
    )
    with torch.inference_mode():
        score_tensor = torch.einsum(
            "psd,vd->psv", normalized_states, normalized_embeddings
        ).cpu().contiguous()
    if not torch.isfinite(score_tensor).all():
        raise RuntimeError("Vocabulary projection contains non-finite values.")
    save_file(
        {"cosine_scores": score_tensor},
        str(context.run_dir / "vocabulary_scores.safetensors"),
        metadata={
            "prompt_ids": ",".join(context.prompt_ids),
            "state_count": str(context.settings.state_count),
            "vocabulary_size": str(vocabulary_size),
            "excluded_capture_token_id": str(capture_token_id),
        },
    )
    del normalized_states, hidden_states, embeddings
    gc.collect()

    eligible_ids = np.arange(vocabulary_size, dtype=np.int64)
    eligible_ids = eligible_ids[eligible_ids != capture_token_id]
    scores = score_tensor.numpy()
    cutoff_records: list[dict[str, Any]] = []
    membership_frames: list[pd.DataFrame] = []
    membership_by_key: dict[tuple[str, int, str], pd.DataFrame] = {}
    for prompt_index, prompt_id in enumerate(context.prompt_ids):
        for state_index in range(context.settings.state_count):
            state_scores = scores[prompt_index, state_index]
            descending = eligible_ids[
                np.argsort(-state_scores[eligible_ids], kind="stable")
            ]
            ascending = eligible_ids[
                np.argsort(state_scores[eligible_ids], kind="stable")
            ]
            upper = elbow_candidate(state_scores[descending])
            lower_inverted = elbow_candidate(-state_scores[ascending])
            upper_rank = int(upper["cutoff_rank"])
            lower_rank = int(lower_inverted["cutoff_rank"])
            positive_ids = descending[:upper_rank]
            negative_ids = ascending[:lower_rank]
            if np.intersect1d(positive_ids, negative_ids).size:
                raise RuntimeError(
                    f"Cutoff populations overlap at {prompt_id} State {state_index}."
                )
            cutoff_records.append(
                {
                    "prompt_id": prompt_id,
                    "state_index": state_index,
                    "state_label": state_label(state_index, context.settings),
                    "eligible_vocabulary_size": len(eligible_ids),
                    "excluded_capture_token_id": capture_token_id,
                    "upper_cutoff_rank": upper_rank,
                    "upper_cutoff_score": upper["cutoff_score"],
                    "upper_elbow_strength": upper["elbow_strength"],
                    "upper_score_gap_after": upper["score_gap_after"],
                    "upper_gap_ratio": upper["gap_ratio"],
                    "lower_cutoff_rank": lower_rank,
                    "lower_cutoff_score": -float(lower_inverted["cutoff_score"]),
                    "lower_elbow_strength": lower_inverted["elbow_strength"],
                    "lower_score_gap_after": lower_inverted["score_gap_after"],
                    "lower_gap_ratio": lower_inverted["gap_ratio"],
                    "positive_head_count": upper_rank,
                    "negative_tail_count": lower_rank,
                    "central_body_count": len(eligible_ids) - upper_rank - lower_rank,
                    "positive_head_fraction": upper_rank / len(eligible_ids),
                    "negative_tail_fraction": lower_rank / len(eligible_ids),
                }
            )
            for side, token_ids in (
                ("positive_head", positive_ids),
                ("negative_tail", negative_ids),
            ):
                frame = pd.DataFrame(
                    {
                        "prompt_id": prompt_id,
                        "state_index": state_index,
                        "state_label": state_label(state_index, context.settings),
                        "side": side,
                        "token_id": token_ids,
                        "raw_token": [raw_tokens[token] for token in token_ids],
                        "decoded_token": [decoded_tokens[token] for token in token_ids],
                        "display_token": [
                            visible_token(decoded_tokens[token]) for token in token_ids
                        ],
                        "token_class": [token_classes[token] for token in token_ids],
                        "cosine_score": state_scores[token_ids],
                        "rank_from_extreme": np.arange(
                            1, len(token_ids) + 1, dtype=np.int32
                        ),
                    }
                )
                membership_by_key[(prompt_id, state_index, side)] = frame
                membership_frames.append(frame)

    cutoffs = pd.DataFrame(cutoff_records).sort_values(
        ["prompt_id", "state_index"], kind="stable"
    )
    expected_cutoffs = len(context.prompt_ids) * context.settings.state_count
    if len(cutoffs) != expected_cutoffs:
        raise RuntimeError(
            f"Expected {expected_cutoffs} cutoff rows; found {len(cutoffs)}."
        )
    cutoffs.to_csv(context.run_dir / "cutoffs.csv", index=False)
    tails = pd.concat(membership_frames, ignore_index=True)
    tails.to_csv(
        context.run_dir / "tail_tokens.csv.gz", index=False, compression="gzip"
    )
    update_component(
        context,
        "projection_and_cutoffs",
        started_at,
        started,
        score_shape=list(score_tensor.shape),
        vocabulary_size=vocabulary_size,
        full_embedding_rows=full_embedding_rows,
        padded_embedding_rows_excluded=full_embedding_rows - vocabulary_size,
        excluded_capture_token_id=capture_token_id,
        cutoff_rows=len(cutoffs),
        membership_rows=len(tails),
        embedding_shard=shard_name,
    )
    del score_tensor, scores, tails, membership_frames
    gc.collect()
    return normalized_embeddings, membership_by_key, decoded_tokens, vocabulary_size


def _support_records(
    comparison_group: str,
    prompt_ids: list[str],
    state_index: int,
    side: str,
    state_data: dict[tuple[str, str], dict[str, Any]],
    decoded_tokens: list[str],
    token_writer: csv.DictWriter,
    edge_writer: csv.DictWriter,
    settings: TopologySettings,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    token_counts: Counter[int] = Counter()
    token_prompts: defaultdict[int, list[str]] = defaultdict(list)
    edge_counts: Counter[tuple[int, int]] = Counter()
    edge_prompts: defaultdict[tuple[int, int], list[str]] = defaultdict(list)
    for prompt_id in prompt_ids:
        data = state_data[(prompt_id, side)]
        for token_id in data["membership"]:
            token_counts[int(token_id)] += 1
            token_prompts[int(token_id)].append(prompt_id)
        for edge in data["edges"]:
            normalized = (int(edge[0]), int(edge[1]))
            edge_counts[normalized] += 1
            edge_prompts[normalized].append(prompt_id)
    for token_id in sorted(token_counts):
        token_writer.writerow(
            {
                "comparison_group": comparison_group,
                "state_index": state_index,
                "state_label": state_label(state_index, settings),
                "side": side,
                "token_id": token_id,
                "decoded_token": visible_token(decoded_tokens[token_id]),
                "support_count": token_counts[token_id],
                "prompt_ids": "|".join(token_prompts[token_id]),
            }
        )
    for token_a, token_b in sorted(edge_counts):
        edge_writer.writerow(
            {
                "comparison_group": comparison_group,
                "state_index": state_index,
                "state_label": state_label(state_index, settings),
                "side": side,
                "token_a": token_a,
                "token_b": token_b,
                "support_count": edge_counts[(token_a, token_b)],
                "prompt_ids": "|".join(edge_prompts[(token_a, token_b)]),
            }
        )
    rows: list[dict[str, Any]] = []
    token_distribution = Counter(token_counts.values())
    edge_distribution = Counter(edge_counts.values())
    for item_type, distribution, total in (
        ("token", token_distribution, len(token_counts)),
        ("edge", edge_distribution, len(edge_counts)),
    ):
        for support_count in range(1, len(prompt_ids) + 1):
            item_count = int(distribution.get(support_count, 0))
            rows.append(
                {
                    "comparison_group": comparison_group,
                    "state_index": state_index,
                    "state_label": state_label(state_index, settings),
                    "side": side,
                    "item_type": item_type,
                    "support_count": support_count,
                    "item_count": item_count,
                    "total_unique_items": total,
                    "fraction_of_unique_items": item_count / total if total else 0.0,
                }
            )
    return rows, {
        "unique_tokens": len(token_counts),
        "all_prompt_tokens": int(token_distribution.get(len(prompt_ids), 0)),
        "unique_edges": len(edge_counts),
        "all_prompt_edges": int(edge_distribution.get(len(prompt_ids), 0)),
    }


def construct_networks(
    context: RunContext,
    normalized_embeddings: torch.Tensor,
    memberships: dict[tuple[str, int, str], pd.DataFrame],
    decoded_tokens: list[str],
    vocabulary_size: int,
) -> dict[str, Any]:
    started_at = utc_now()
    started = time.perf_counter()
    groups = _comparison_groups(context.config)
    prompt_specs = {
        str(prompt["prompt_id"]): prompt for prompt in context.config["prompts"]
    }
    network_records: list[dict[str, Any]] = []
    community_records: list[dict[str, Any]] = []
    community_edge_records: list[dict[str, Any]] = []
    compact_networks: list[dict[str, Any]] = []
    transition_records: list[dict[str, Any]] = []
    pairwise_records: list[dict[str, Any]] = []
    community_match_records: list[dict[str, Any]] = []
    invariance_records: list[dict[str, Any]] = []
    invariant_core_counts: dict[tuple[str, int, str], dict[str, int]] = {}
    previous: dict[tuple[str, str], dict[str, Any]] = {}
    node_rows = 0
    edge_rows = 0
    token_support_rows = 0
    edge_support_rows = 0

    nodes_path = context.run_dir / "nodes.csv.gz"
    edges_path = context.run_dir / "edges.csv.gz"
    token_support_path = context.run_dir / "token_permutation_support.csv.gz"
    edge_support_path = context.run_dir / "edge_permutation_support.csv.gz"
    with (
        gzip.open(nodes_path, "wt", encoding="utf-8", newline="") as node_handle,
        gzip.open(edges_path, "wt", encoding="utf-8", newline="") as edge_handle,
        gzip.open(token_support_path, "wt", encoding="utf-8", newline="") as token_handle,
        gzip.open(edge_support_path, "wt", encoding="utf-8", newline="") as edge_support_handle,
    ):
        token_writer = csv.DictWriter(
            token_handle,
            fieldnames=[
                "comparison_group",
                "state_index",
                "state_label",
                "side",
                "token_id",
                "decoded_token",
                "support_count",
                "prompt_ids",
            ],
        )
        edge_writer = csv.DictWriter(
            edge_support_handle,
            fieldnames=[
                "comparison_group",
                "state_index",
                "state_label",
                "side",
                "token_a",
                "token_b",
                "support_count",
                "prompt_ids",
            ],
        )
        token_writer.writeheader()
        edge_writer.writeheader()

        for state_index in range(context.settings.state_count):
            current_state: dict[tuple[str, str], dict[str, Any]] = {}
            for prompt_index, prompt_id in enumerate(context.prompt_ids):
                for side_index, side in enumerate(SIDES):
                    network_started = time.perf_counter()
                    (
                        metric,
                        node_frame,
                        edge_frame,
                        communities,
                        community_edges,
                        state_data,
                        compact,
                    ) = analyze_network(
                        prompt_id,
                        prompt_index,
                        state_index,
                        side,
                        side_index,
                        memberships[(prompt_id, state_index, side)],
                        normalized_embeddings,
                        vocabulary_size,
                        context.settings,
                    )
                    node_frame.to_csv(node_handle, index=False, header=node_rows == 0)
                    edge_frame.to_csv(edge_handle, index=False, header=edge_rows == 0)
                    node_rows += len(node_frame)
                    edge_rows += len(edge_frame)
                    network_records.append(metric)
                    community_records.extend(communities)
                    community_edge_records.extend(community_edges)
                    compact_networks.append(compact)
                    current_state[(prompt_id, side)] = state_data

                    prior = previous.get((prompt_id, side))
                    if prior is not None:
                        comparison = compare_state_data(prior, state_data)
                        transition_records.append(
                            {
                                "prompt_id": prompt_id,
                                "side": side,
                                "previous_state_index": state_index - 1,
                                "current_state_index": state_index,
                                "previous_state_label": state_label(
                                    state_index - 1, context.settings
                                ),
                                "current_state_label": state_label(
                                    state_index, context.settings
                                ),
                                **comparison,
                            }
                        )
                        community_match_records.extend(
                            best_community_matches(
                                "adjacent_state",
                                side,
                                prior,
                                state_data,
                                prompt_id=prompt_id,
                                source_prompt_id=prompt_id,
                                target_prompt_id=prompt_id,
                                source_state_index=state_index - 1,
                                target_state_index=state_index,
                            )
                        )
                    previous[(prompt_id, side)] = state_data
                    print(
                        f"{context.config['run_id']} network "
                        f"{len(network_records):03d}/{context.config['expected']['network_count']}: "
                        f"{prompt_id} State {state_index:02d} {side}, "
                        f"{len(node_frame):,} nodes, {len(communities)} communities, "
                        f"{time.perf_counter() - network_started:.1f}s.",
                        flush=True,
                    )

            for group_name, group_prompt_ids in groups.items():
                for side in SIDES:
                    for source_id, target_id in itertools.combinations(
                        group_prompt_ids, 2
                    ):
                        source_data = current_state[(source_id, side)]
                        target_data = current_state[(target_id, side)]
                        comparison = compare_state_data(source_data, target_data)
                        source_order = list(prompt_specs[source_id]["concept_order"])
                        target_order = list(prompt_specs[target_id]["concept_order"])
                        pairwise_records.append(
                            {
                                "comparison_group": group_name,
                                "source_prompt_id": source_id,
                                "target_prompt_id": target_id,
                                "source_first_concept": source_order[0],
                                "target_first_concept": target_order[0],
                                "source_final_concept": source_order[-1],
                                "target_final_concept": target_order[-1],
                                "same_first_concept": source_order[0] == target_order[0],
                                "same_final_concept": source_order[-1] == target_order[-1],
                                "reverse_order": source_order == list(reversed(target_order)),
                                "state_index": state_index,
                                "state_label": state_label(state_index, context.settings),
                                "side": side,
                                **comparison,
                            }
                        )
                        community_match_records.extend(
                            best_community_matches(
                                "prompt_pair",
                                side,
                                source_data,
                                target_data,
                                comparison_group=group_name,
                                source_prompt_id=source_id,
                                target_prompt_id=target_id,
                                source_state_index=state_index,
                                target_state_index=state_index,
                            )
                        )
                    summary_rows, core_counts = _support_records(
                        group_name,
                        group_prompt_ids,
                        state_index,
                        side,
                        current_state,
                        decoded_tokens,
                        token_writer,
                        edge_writer,
                        context.settings,
                    )
                    invariance_records.extend(summary_rows)
                    invariant_core_counts[(group_name, state_index, side)] = core_counts
                    token_support_rows += core_counts["unique_tokens"]
                    edge_support_rows += core_counts["unique_edges"]

    network_index = pd.DataFrame(network_records).sort_values(
        ["state_index", "prompt_id", "side"], kind="stable"
    )
    community_nodes = pd.DataFrame(community_records).sort_values(
        ["state_index", "prompt_id", "side", "community_id"], kind="stable"
    )
    community_edges = pd.DataFrame(community_edge_records).sort_values(
        ["state_index", "prompt_id", "side", "community_a", "community_b"],
        kind="stable",
    )
    transitions = pd.DataFrame(transition_records).sort_values(
        ["prompt_id", "side", "current_state_index"], kind="stable"
    )
    pairwise = pd.DataFrame(pairwise_records).sort_values(
        ["state_index", "side", "source_prompt_id", "target_prompt_id"],
        kind="stable",
    )
    invariance = pd.DataFrame(invariance_records).sort_values(
        ["comparison_group", "state_index", "side", "item_type", "support_count"],
        kind="stable",
    )
    community_matches = pd.DataFrame(community_match_records)
    network_index.to_csv(context.run_dir / "network_index.csv", index=False)
    community_nodes.to_csv(context.run_dir / "community_nodes.csv", index=False)
    community_edges.to_csv(context.run_dir / "community_edges.csv", index=False)
    transitions.to_csv(context.run_dir / "state_transitions.csv", index=False)
    pairwise.to_csv(
        context.run_dir / "pairwise_permutation_comparisons.csv", index=False
    )
    invariance.to_csv(context.run_dir / "permutation_invariance.csv", index=False)
    community_matches.to_csv(
        context.run_dir / "community_transition_evidence.csv", index=False
    )
    update_component(
        context,
        "networks_and_communities",
        started_at,
        started,
        network_count=len(network_index),
        selected_node_rows=node_rows,
        directed_edge_rows=edge_rows,
        community_rows=len(community_nodes),
        intercommunity_edge_rows=len(community_edges),
    )

    transition_started_at = utc_now()
    transition_started = time.perf_counter()
    expected_transitions = int(
        context.config["expected"]["within_prompt_transition_rows"]
    )
    if len(transitions) != expected_transitions:
        raise RuntimeError(
            f"Expected {expected_transitions} transitions; found {len(transitions)}."
        )
    update_component(
        context,
        "within_prompt_transitions",
        transition_started_at,
        transition_started,
        transition_rows=len(transitions),
        minimum_membership_jaccard=float(transitions["membership_jaccard"].min()),
        minimum_edge_jaccard=float(transitions["edge_jaccard"].min()),
    )

    pair_started_at = utc_now()
    pair_started = time.perf_counter()
    expected_pairs = int(context.config["expected"]["pairwise_permutation_rows"])
    if len(pairwise) != expected_pairs:
        raise RuntimeError(
            f"Expected {expected_pairs} pairwise rows; found {len(pairwise)}."
        )
    update_component(
        context,
        "pairwise_permutation_comparisons",
        pair_started_at,
        pair_started,
        pairwise_comparison_rows=len(pairwise),
        minimum_membership_jaccard=float(pairwise["membership_jaccard"].min()),
        minimum_edge_jaccard=float(pairwise["edge_jaccard"].min()),
    )

    invariance_started_at = utc_now()
    invariance_started = time.perf_counter()
    expected_invariance = int(context.config["expected"]["invariance_summary_rows"])
    if len(invariance) != expected_invariance:
        raise RuntimeError(
            f"Expected {expected_invariance} invariance rows; found {len(invariance)}."
        )
    update_component(
        context,
        "permutation_invariance",
        invariance_started_at,
        invariance_started,
        summary_rows=len(invariance),
        token_support_rows=token_support_rows,
        edge_support_rows=edge_support_rows,
        token_and_edge_support_separate=True,
    )

    export_started_at = utc_now()
    export_started = time.perf_counter()
    prompt_records = load_json(context.run_dir / "prompt_records.json")
    compact_document = {
        "schema_version": 2,
        "run_id": context.config["run_id"],
        "model": {
            "id": context.config["model"]["id"],
            "revision": context.config["model"]["revision"],
        },
        "prompt_records": prompt_records,
        "comparison_groups": groups,
        "network_count": len(compact_networks),
        "state_count": context.settings.state_count,
        "sides": list(SIDES),
        "stable_join_key": "token_id",
        "community_identity": "community_id is local to one prompt, state and side",
        "interpretation_boundary": (
            "Positive and negative denote anchor-state cosine alignment and "
            "anti-alignment in the fixed input-embedding basis. Communities are "
            "measured partitions, not semantic topics or parent structures."
        ),
        "within_prompt_transitions": transitions.to_dict(orient="records"),
        "pairwise_permutation_comparisons": pairwise.to_dict(orient="records"),
        "permutation_invariance_summary": invariance.to_dict(orient="records"),
        "networks": compact_networks,
    }
    write_json(context.run_dir / "chatgpt_community_networks.json", compact_document)

    compact_by_key = {
        (item["state_index"], item["prompt_id"], item["side"]): item
        for item in compact_networks
    }
    packet_lines = [
        f"# {context.config['run_id']} measured layer packets",
        "",
        f"This file describes all {len(compact_networks)} measured prompt/state/side networks.",
        "It contains no inferred semantic topic or parent labels.",
        "",
        "Positive and negative mean cosine alignment and anti-alignment with the evolving final-newline state. Negative does not establish suppression.",
        "",
    ]
    primary_group = next(iter(groups))
    for state_index in range(context.settings.state_count):
        packet_lines.extend(
            [f"## State {state_index:02d} — {state_label(state_index, context.settings)}", ""]
        )
        state_pairs = pairwise.loc[pairwise["state_index"] == state_index]
        for side in SIDES:
            side_pairs = state_pairs.loc[state_pairs["side"] == side]
            core = invariant_core_counts[(primary_group, state_index, side)]
            packet_lines.extend(
                [
                    f"### {side} cross-permutation measurement",
                    "",
                    f"- Membership Jaccard: min {side_pairs['membership_jaccard'].min():.6f}; mean {side_pairs['membership_jaccard'].mean():.6f}; max {side_pairs['membership_jaccard'].max():.6f}",
                    f"- Edge Jaccard: min {side_pairs['edge_jaccard'].min():.6f}; mean {side_pairs['edge_jaccard'].mean():.6f}; max {side_pairs['edge_jaccard'].max():.6f}",
                    f"- Community ARI: min {side_pairs['community_adjusted_rand'].min():.6f}; mean {side_pairs['community_adjusted_rand'].mean():.6f}; max {side_pairs['community_adjusted_rand'].max():.6f}",
                    f"- Tokens in all prompts: {core['all_prompt_tokens']} of {core['unique_tokens']} unique",
                    f"- Edges in all prompts: {core['all_prompt_edges']} of {core['unique_edges']} unique",
                    "",
                ]
            )
        for prompt_id in context.prompt_ids:
            packet_lines.extend(
                [
                    f"### Prompt {prompt_id}",
                    "",
                    f"Input: `{visible_token(prompt_records[prompt_id]['raw_text'])}`",
                    "",
                ]
            )
            for side in SIDES:
                network = compact_by_key[(state_index, prompt_id, side)]
                metrics = network["metrics"]
                packet_lines.extend(
                    [
                        f"#### {side}",
                        "",
                        f"- Nodes: {metrics['population_size']}",
                        f"- Directed 10-NN edges: {metrics['directed_edge_count']}",
                        f"- Communities: {metrics['community_count']}",
                        f"- Modularity: {metrics['community_modularity']:.6f}",
                        "",
                        "All communities:",
                        "",
                    ]
                )
                for community in network["communities"]:
                    representatives = ", ".join(community["representative_tokens"][:10])
                    extremes = ", ".join(community["most_extreme_tokens"][:6])
                    packet_lines.append(
                        f"- C{community['community_id']} (n={community['community_size']}): "
                        f"representatives [{representatives}]; target-extreme [{extremes}]"
                    )
                packet_lines.extend(["", "Strongest intercommunity connections:", ""])
                strongest = sorted(
                    network["intercommunity_edges"],
                    key=lambda item: (
                        -int(item["token_edge_count"]),
                        -float(item["mean_cosine_similarity"]),
                    ),
                )[:15]
                if strongest:
                    for edge in strongest:
                        packet_lines.append(
                            f"- C{edge['community_a']} to C{edge['community_b']}: "
                            f"{edge['token_edge_count']} token edges; mean cosine "
                            f"{edge['mean_cosine_similarity']:.6f}"
                        )
                else:
                    packet_lines.append("- None")
                packet_lines.append("")
    (context.run_dir / "chatgpt_layer_packets.md").write_text(
        "\n".join(packet_lines).rstrip() + "\n", encoding="utf-8"
    )
    update_component(
        context,
        "measured_exports",
        export_started_at,
        export_started,
        json_networks=len(compact_networks),
        markdown_state_sections=context.settings.state_count,
        semantic_labels_added=False,
    )
    return {
        "network_index": network_index,
        "community_nodes": community_nodes,
        "community_edges": community_edges,
        "transitions": transitions,
        "pairwise": pairwise,
        "invariance": invariance,
        "node_rows": node_rows,
        "edge_rows": edge_rows,
        "token_support_rows": token_support_rows,
        "edge_support_rows": edge_support_rows,
        "invariant_core_counts": invariant_core_counts,
    }


def _count_gzip_rows(path: Path) -> int:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as handle:
        records = csv.reader(handle)
        if next(records, None) is None:
            return 0
        return sum(1 for _ in records)


def validate_measurement_files(context: RunContext) -> dict[str, Any]:
    expected = context.config["expected"]
    network_index = pd.read_csv(context.run_dir / "network_index.csv")
    communities = pd.read_csv(context.run_dir / "community_nodes.csv")
    community_edges = pd.read_csv(context.run_dir / "community_edges.csv")
    transitions = pd.read_csv(context.run_dir / "state_transitions.csv")
    pairwise = pd.read_csv(context.run_dir / "pairwise_permutation_comparisons.csv")
    invariance = pd.read_csv(context.run_dir / "permutation_invariance.csv")
    cutoffs = pd.read_csv(context.run_dir / "cutoffs.csv")
    hidden_pairs = pd.read_csv(context.run_dir / "pairwise_hidden_state_metrics.csv")
    capture_validation = load_json(context.run_dir / "capture_validation.json")

    if len(network_index) != int(expected["network_count"]):
        raise RuntimeError("Network coverage is incomplete.")
    network_key = ["prompt_id", "state_index", "side"]
    if network_index.duplicated(network_key).any():
        raise RuntimeError("Duplicate prompt/state/side network identity found.")
    if not (
        network_index["directed_edge_count"]
        == network_index["population_size"] * context.settings.k_neighbors
    ).all():
        raise RuntimeError("Exact 10-neighbour coverage failed.")
    expected_network_keys = {
        (prompt_id, state_index, side)
        for prompt_id in context.prompt_ids
        for state_index in range(context.settings.state_count)
        for side in SIDES
    }
    actual_network_keys = set(
        network_index[network_key].itertuples(index=False, name=None)
    )
    if actual_network_keys != expected_network_keys:
        raise RuntimeError("Network identities do not equal the expected Cartesian product.")

    community_totals = communities.groupby(network_key)["community_size"].sum().sort_index()
    population_totals = network_index.set_index(network_key)["population_size"].sort_index()
    if not community_totals.equals(population_totals):
        raise RuntimeError("Community sizes do not reconcile with network populations.")
    valid_communities = set(
        communities[[*network_key, "community_id"]].itertuples(index=False, name=None)
    )
    for row in community_edges.itertuples(index=False):
        prefix = (row.prompt_id, int(row.state_index), row.side)
        if (*prefix, int(row.community_a)) not in valid_communities:
            raise RuntimeError("Intercommunity edge references an invalid source community.")
        if (*prefix, int(row.community_b)) not in valid_communities:
            raise RuntimeError("Intercommunity edge references an invalid target community.")

    if len(transitions) != int(expected["within_prompt_transition_rows"]):
        raise RuntimeError("Within-prompt transition coverage is incomplete.")
    if transitions.duplicated(["prompt_id", "current_state_index", "side"]).any():
        raise RuntimeError("Duplicate within-prompt transition identity found.")
    for row in transitions.itertuples(index=False):
        source_key = (row.prompt_id, int(row.previous_state_index), row.side)
        target_key = (row.prompt_id, int(row.current_state_index), row.side)
        if source_key not in actual_network_keys or target_key not in actual_network_keys:
            raise RuntimeError("Transition references a missing network.")

    if len(pairwise) != int(expected["pairwise_permutation_rows"]):
        raise RuntimeError("Pairwise permutation coverage is incomplete.")
    pair_key = ["source_prompt_id", "target_prompt_id", "state_index", "side"]
    if pairwise.duplicated(pair_key).any():
        raise RuntimeError("Duplicate pairwise permutation identity found.")
    for row in pairwise.itertuples(index=False):
        source_key = (row.source_prompt_id, int(row.state_index), row.side)
        target_key = (row.target_prompt_id, int(row.state_index), row.side)
        if source_key not in actual_network_keys or target_key not in actual_network_keys:
            raise RuntimeError("Pairwise comparison references a missing network.")
    state_zero = pairwise.loc[pairwise["state_index"] == 0]
    expected_state_zero = sum(
        len(list(itertools.combinations(prompt_ids, 2)))
        for prompt_ids in _comparison_groups(context.config).values()
    ) * len(SIDES)
    if len(state_zero) != expected_state_zero or not (
        np.allclose(state_zero["membership_jaccard"], 1.0)
        and np.allclose(state_zero["edge_jaccard"], 1.0)
        and np.allclose(state_zero["community_adjusted_rand"], 1.0)
    ):
        raise RuntimeError("State 00 topology is not identical across all permutations.")

    if len(invariance) != int(expected["invariance_summary_rows"]):
        raise RuntimeError("Permutation-invariance coverage is incomplete.")
    if len(cutoffs) != len(context.prompt_ids) * context.settings.state_count:
        raise RuntimeError("Cutoff coverage is incomplete.")
    if len(hidden_pairs) != int(expected["hidden_state_pair_rows"]):
        raise RuntimeError("Hidden-state pair coverage is incomplete.")
    if capture_validation.get("status") != "successful":
        raise RuntimeError("Capture validation is not successful.")
    if not capture_validation.get("deterministic_replay_exact"):
        raise RuntimeError("Deterministic replay was not exact.")
    if not capture_validation.get("state_00_exact_equal_all_prompts"):
        raise RuntimeError("State 00 hidden states are not equal across prompts.")

    expected_nodes = int(network_index["population_size"].sum())
    expected_edges = int(network_index["directed_edge_count"].sum())
    node_rows = _count_gzip_rows(context.run_dir / "nodes.csv.gz")
    edge_rows = _count_gzip_rows(context.run_dir / "edges.csv.gz")
    tail_rows = _count_gzip_rows(context.run_dir / "tail_tokens.csv.gz")
    if node_rows != expected_nodes or tail_rows != expected_nodes:
        raise RuntimeError("Node or membership row counts do not reconcile.")
    if edge_rows != expected_edges:
        raise RuntimeError("Directed edge rows do not reconcile.")
    compact = load_json(context.run_dir / "chatgpt_community_networks.json")
    if int(compact.get("network_count", -1)) != int(expected["network_count"]):
        raise RuntimeError("ChatGPT JSON network count is incomplete.")

    return {
        "network_count": len(network_index),
        "selected_membership_rows": expected_nodes,
        "directed_edge_rows": expected_edges,
        "community_count": len(communities),
        "intercommunity_edge_rows": len(community_edges),
        "adjacent_transition_rows": len(transitions),
        "pairwise_comparison_rows": len(pairwise),
        "invariance_summary_rows": len(invariance),
        "minimum_pairwise_membership_jaccard": float(
            pairwise["membership_jaccard"].min()
        ),
        "minimum_pairwise_edge_jaccard": float(pairwise["edge_jaccard"].min()),
        "mean_same_final_membership_jaccard": float(
            pairwise.loc[pairwise["same_final_concept"], "membership_jaccard"].mean()
        ),
        "mean_different_final_membership_jaccard": float(
            pairwise.loc[~pairwise["same_final_concept"], "membership_jaccard"].mean()
        ),
        "state_zero_pair_identity_verified": True,
        "deterministic_replay_exact": True,
        "node_rows_counted": node_rows,
        "edge_rows_counted": edge_rows,
    }


def write_measured_reports(context: RunContext, results: dict[str, Any]) -> None:
    run_status = _post_measurement_run_status(context.config)
    analysis_required = _analysis_required(context.config)
    verification_name, measurement_report_name = _measurement_report_names(
        context.config
    )
    run_number = int(context.config["run_number"])
    verification_lines = [
        f"# {context.config['run_id']} measurement completeness verification",
        "",
        "- Measurement status: **PASS**",
        f"- Overall run status after measurement: **{run_status}**",
        f"- Networks: {results['network_count']} / {context.config['expected']['network_count']}",
        f"- Within-prompt transitions: {results['adjacent_transition_rows']} / {context.config['expected']['within_prompt_transition_rows']}",
        f"- Same-state permutation comparisons: {results['pairwise_comparison_rows']} / {context.config['expected']['pairwise_permutation_rows']}",
        f"- Invariance summary rows: {results['invariance_summary_rows']} / {context.config['expected']['invariance_summary_rows']}",
        f"- Selected token memberships: {results['selected_membership_rows']:,}",
        f"- Directed exact 10-NN edges: {results['directed_edge_rows']:,}",
        f"- State-local communities: {results['community_count']:,}",
        "- Every expected network and comparison identity exists exactly once.",
        "- Every selected node belongs to exactly one state-local community.",
        "- Every network has exactly ten directed neighbours per node.",
        "- Intercommunity edges, transitions and pairwise comparisons reference valid measured objects.",
        "- State 00 hidden states and topology are identical across all permutations.",
        "- Deterministic batch replay is exactly equal.",
        "- Measured exports contain no semantic parent labels.",
    ]
    (context.run_dir / verification_name).write_text(
        "\n".join(verification_lines) + "\n", encoding="utf-8"
    )
    report_lines = [
        f"# R{run_number:03d} semantic-topology measurement report",
        "",
        "## Outcome",
        "",
        f"Measurement complete for `{context.config['run_id']}`. The report contains measured structural evidence only.",
        "",
        (
            "**Overall run status: awaiting semantic analysis.** Independent semantic "
            "reconstruction and final analysis remain required before the research run "
            "is complete."
            if analysis_required
            else "**Overall run status: measurement complete.** No semantic-analysis phase is required by this run configuration."
        ),
        "",
        "## Run identity",
        "",
        f"- Model: `{context.config['model']['id']}`",
        f"- Revision: `{context.config['model']['revision']}`",
        f"- Prompts: {len(context.prompt_ids)}",
        f"- Recorded states per prompt: {context.settings.state_count}",
        "- Capture position: final newline token",
        "- Response generation: not executed",
        "- Deterministic replay: exact",
        "",
        "## Coverage",
        "",
        f"- Networks: {results['network_count']}",
        f"- Selected token memberships: {results['selected_membership_rows']:,}",
        f"- Directed 10-NN edges: {results['directed_edge_rows']:,}",
        f"- State-local communities: {results['community_count']:,}",
        f"- Adjacent-state comparisons: {results['adjacent_transition_rows']}",
        f"- Same-state permutation comparisons: {results['pairwise_comparison_rows']}",
        "",
        "## Measured comparison summary",
        "",
        f"- Minimum cross-permutation membership Jaccard: {results['minimum_pairwise_membership_jaccard']:.6f}",
        f"- Minimum cross-permutation edge Jaccard: {results['minimum_pairwise_edge_jaccard']:.6f}",
        f"- Mean membership Jaccard for pairs sharing the final concept: {results['mean_same_final_membership_jaccard']:.6f}",
        f"- Mean membership Jaccard for pairs with different final concepts: {results['mean_different_final_membership_jaccard']:.6f}",
        "",
        "These measurements test order and final-position association. They do not identify semantic parents or establish what the measured differences mean.",
        "",
        "## Interpretation boundary",
        "",
        "The measured outputs end at tokens, scores, networks, state-local communities, transitions and permutation comparisons. Any parent structures, relations or semantic maps must be reconstructed independently downstream.",
    ]
    (context.run_dir / measurement_report_name).write_text(
        "\n".join(report_lines) + "\n", encoding="utf-8"
    )


def _artifact_type(path: Path) -> str:
    name = path.name
    if name.endswith(".safetensors"):
        return "tensor"
    if name.endswith(".csv") or name.endswith(".csv.gz"):
        return "table"
    if name.endswith(".json"):
        return "structured_record"
    if name.endswith(".md"):
        return "report"
    return "other"


def build_artifact_index(context: RunContext) -> dict[str, Any]:
    artifacts: dict[str, Any] = {}
    for path in sorted(context.run_dir.rglob("*")):
        if not path.is_file() or path.name in {"manifest.json", "artifact_index.json"}:
            continue
        relative = str(path.relative_to(context.run_dir)).replace("\\", "/")
        artifacts[relative] = {
            "relative_path": relative,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "artifact_type": _artifact_type(path),
            "evidence_class": "measurement",
            "tracked_by_git": not (
                path.name.endswith(".safetensors") or path.name.endswith(".gz")
            ),
        }
    index = {
        "schema_version": 1,
        "generated_at": utc_now(),
        "run_id": context.config["run_id"],
        "run_status": _post_measurement_run_status(context.config),
        "measurement_status": "measurement_successful",
        "self_exclusions": [
            "manifest.json changes after index creation",
            "artifact_index.json cannot hash itself",
        ],
        "artifacts": artifacts,
    }
    write_json(context.run_dir / "artifact_index.json", index)
    return index


def measure(context: RunContext) -> None:
    initialize_manifest(context)
    (context.run_dir / "run_config.json").write_text(
        json.dumps(context.config, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    (context.run_dir / context.plan_path.name).write_text(
        context.plan_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    current_component = "model_identity"
    try:
        capture_hidden_states(context)
        current_component = "projection_and_cutoffs"
        embeddings, memberships, decoded_tokens, vocabulary_size = project_and_select(
            context
        )
        current_component = "networks_and_communities"
        construct_networks(
            context,
            embeddings,
            memberships,
            decoded_tokens,
            vocabulary_size,
        )
        del embeddings, memberships, decoded_tokens
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.synchronize()

        cleanup_started_at = utc_now()
        cleanup_started = time.perf_counter()
        update_component(
            context,
            "resource_cleanup",
            cleanup_started_at,
            cleanup_started,
            phase="final",
            offload_directory=str(context.offload_dir),
            memory_after_cleanup=memory_snapshot(context.snapshot_dir),
        )

        current_component = "completeness_validation"
        validation_started_at = utc_now()
        validation_started = time.perf_counter()
        results = validate_measurement_files(context)
        write_measured_reports(context, results)
        update_component(
            context,
            "completeness_validation",
            validation_started_at,
            validation_started,
            **results,
        )
        index = build_artifact_index(context)
        manifest = load_json(context.manifest_path)
        for name in MEASUREMENT_COMPONENTS:
            if manifest["components"].get(name, {}).get("status") != "successful":
                raise RuntimeError(f"Required component is not successful: {name}")
        manifest["measurement_status"] = "measurement_successful"
        manifest["analysis_required"] = _analysis_required(context.config)
        manifest["analysis_status"] = (
            "not_started" if _analysis_required(context.config) else "not_required"
        )
        manifest["run_status"] = _post_measurement_run_status(context.config)
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
                    "run_status": manifest["run_status"],
                    "measurement_status": "measurement_successful",
                    "analysis_status": manifest["analysis_status"],
                    "run_id": context.config["run_id"],
                    "results": results,
                },
                indent=2,
            ),
            flush=True,
        )
    except BaseException as error:
        try:
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        finally:
            fail_measurement(context, current_component, error)
        raise


def recover_validation(context: RunContext) -> dict[str, Any]:
    """Recover only a failed completeness check without changing measured evidence."""
    if not context.run_dir.is_dir() or not context.manifest_path.is_file():
        raise FileNotFoundError(f"Run directory or manifest is missing: {context.run_dir}")
    manifest = load_json(context.manifest_path)
    failure = manifest.get("failure_details") or {}
    if manifest.get("measurement_status") != "measurement_failed":
        raise RuntimeError("Validation recovery requires a measurement_failed manifest.")
    if failure.get("component") != "completeness_validation":
        raise RuntimeError("Validation recovery is limited to completeness-validation failures.")
    for name in MEASUREMENT_COMPONENTS:
        if name == "completeness_validation":
            continue
        if manifest["components"].get(name, {}).get("status") != "successful":
            raise RuntimeError(f"Upstream component is not successful: {name}")

    failed_manifest_path = context.run_dir / "manifest.failed_validation.json"
    recovery_path = context.run_dir / "validation_recovery.json"
    if failed_manifest_path.exists() or recovery_path.exists():
        raise FileExistsError("A validation-recovery record already exists; refusing to repeat it.")
    write_json(failed_manifest_path, manifest)

    protected_paths = [
        path
        for path in sorted(context.run_dir.iterdir())
        if path.is_file()
        and path.name
        not in {
            "manifest.json",
            "manifest.failed_validation.json",
            "validation_recovery.json",
            "artifact_index.json",
        }
    ]
    protected_hashes = {
        path.name: {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in protected_paths
    }
    started_at = utc_now()
    started = time.perf_counter()
    results = validate_measurement_files(context)
    write_measured_reports(context, results)
    recovery_record = {
        "schema_version": 1,
        "run_id": context.config["run_id"],
        "recovered_at": utc_now(),
        "scope": "completeness_validation_only",
        "measurement_reexecuted": False,
        "measurement_artifacts_modified": False,
        "original_failure_manifest": failed_manifest_path.name,
        "original_failure": failure,
        "defect": (
            "The original validator counted physical gzip text lines. Quoted CSV "
            "token fields can contain embedded newline characters, so physical lines "
            "are not logical CSV records."
        ),
        "correction": (
            "Count logical records with csv.reader while preserving every measured "
            "artifact byte-for-byte."
        ),
        "protected_measurement_artifacts": protected_hashes,
        "validated_results": results,
    }
    write_json(recovery_path, recovery_record)
    recovery_report_name = f"R{int(context.config['run_number']):03d}_VALIDATION_RECOVERY.md"
    (context.run_dir / recovery_report_name).write_text(
        "\n".join(
            [
                f"# {context.config['run_id']} validation recovery",
                "",
                "The measured evidence was not rerun or changed. The initial final check failed because it counted physical text lines in gzip CSV files; quoted token fields may contain embedded newline characters.",
                "",
                "The corrected check counts logical CSV records. It reconciled all selected nodes, directed edges, communities, transitions, pairwise comparisons and invariance records. The original failed manifest is preserved as `manifest.failed_validation.json`, and SHA-256 hashes of the pre-existing measured artifacts are recorded in `validation_recovery.json`.",
                "",
                "Semantic interpretation remains `not_started`.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    update_component(
        context,
        "completeness_validation",
        started_at,
        started,
        recovery=True,
        measurement_reexecuted=False,
        original_failure_manifest=failed_manifest_path.name,
        **results,
    )
    index = build_artifact_index(context)
    manifest = load_json(context.manifest_path)
    for name in MEASUREMENT_COMPONENTS:
        if manifest["components"].get(name, {}).get("status") != "successful":
            raise RuntimeError(f"Required component is not successful after recovery: {name}")
    manifest.setdefault("validation_history", []).append(
        {
            "status": "failed_then_recovered",
            "original_failure_manifest": failed_manifest_path.name,
            "recovery_record": recovery_path.name,
            "original_failure": failure,
        }
    )
    manifest["measurement_status"] = "measurement_successful"
    manifest["analysis_required"] = _analysis_required(context.config)
    manifest["analysis_status"] = (
        "not_started" if _analysis_required(context.config) else "not_required"
    )
    manifest["run_status"] = _post_measurement_run_status(context.config)
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
    return {
        "run_status": manifest["run_status"],
        "measurement_status": "measurement_successful",
        "analysis_status": manifest["analysis_status"],
        "validation_recovery": True,
        "run_id": context.config["run_id"],
        "results": results,
    }


def verify(context: RunContext) -> dict[str, Any]:
    if not context.run_dir.is_dir() or not context.manifest_path.is_file():
        raise FileNotFoundError(f"Run directory or manifest is missing: {context.run_dir}")
    manifest = load_json(context.manifest_path)
    if manifest.get("run_id") != context.config["run_id"]:
        raise RuntimeError("Manifest run identity does not match the configuration.")
    if manifest.get("measurement_status") != "measurement_successful":
        raise RuntimeError("Standalone verification requires a successful measurement.")
    index_path = context.run_dir / "artifact_index.json"
    index = load_json(index_path)
    if sha256_file(index_path) != manifest["artifact_index"]["sha256"]:
        raise RuntimeError("Artifact-index hash does not match the manifest.")
    for relative, record in index["artifacts"].items():
        path = context.run_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"Indexed artifact is missing: {relative}")
        if path.stat().st_size != int(record["bytes"]):
            raise RuntimeError(f"Indexed artifact size changed: {relative}")
        if sha256_file(path) != record["sha256"]:
            raise RuntimeError(f"Indexed artifact hash changed: {relative}")
    results = validate_measurement_files(context)
    for key, value in results.items():
        recorded = manifest["results"].get(key)
        if isinstance(value, float):
            if not np.isclose(value, recorded, equal_nan=True):
                raise RuntimeError(f"Recomputed result changed: {key}")
        elif value != recorded:
            raise RuntimeError(f"Recomputed result changed: {key}")
    return {
        "status": "PASS",
        "run_id": context.config["run_id"],
        "run_status": manifest.get(
            "run_status", _post_measurement_run_status(context.config)
        ),
        "measurement_status": manifest["measurement_status"],
        "analysis_status": manifest.get(
            "analysis_status",
            "not_started" if _analysis_required(context.config) else "not_required",
        ),
        "artifact_count": len(index["artifacts"]),
        **results,
    }
