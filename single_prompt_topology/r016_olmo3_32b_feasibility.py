"""Test native-BF16 OLMo 3 32B local instrumented-forward feasibility."""

from __future__ import annotations

import gc
import hashlib
import json
import shutil
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psutil
import torch
from accelerate import infer_auto_device_map, init_empty_weights
from huggingface_hub import HfApi, snapshot_download
from safetensors.torch import save_file
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "allenai/Olmo-3-1125-32B"
MODEL_REVISION = "c2b61dae89a1ad10e4ad5653d0e46b590902607b"
EXPECTED_REPOSITORY_BYTES = 64_476_978_123
EXPECTED_LAYERS = 64
EXPECTED_HIDDEN_WIDTH = 5_120
EXPECTED_STATES = EXPECTED_LAYERS + 1
PROMPT = "laser\ncity\nspatial field\n"
GPU_LIMIT = "18GiB"
CPU_LIMIT = "28GiB"
MAX_MEMORY = {0: GPU_LIMIT, "cpu": CPU_LIMIT}

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUN_ID = "R016_olmo3-32b-local-bf16-feasibility"
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
PLAN_PATH = PIPELINE_DIR / "R016_PLAN.md"
MANIFEST_PATH = RUN_DIR / "manifest.json"
DEVICE_MAP_PATH = RUN_DIR / "device_map.json"
VALIDATION_PATH = RUN_DIR / "capture_validation.json"
REPORT_PATH = RUN_DIR / "R016_FEASIBILITY_REPORT.md"
CAPTURE_PATH = RUN_DIR / "anchor_hidden_states.safetensors"
CACHE_DIR = Path(r"D:\AI\cache\huggingface\hub")
OFFLOAD_DIR = Path(r"D:\AI\cache\offload\R016_olmo3-32b")

REQUIRED_COMPONENTS = (
    "plan_lock",
    "environment_preflight",
    "model_metadata_lock",
    "snapshot_download",
    "device_map_preflight",
    "model_load",
    "instrumented_forward",
    "capture_validation",
    "resource_cleanup",
    "feasibility_decision",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def json_safe(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, torch.device):
        return str(value)
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    return value


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(json_safe(payload), indent=2, ensure_ascii=False, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def memory_snapshot() -> dict[str, object]:
    virtual = psutil.virtual_memory()
    disk = shutil.disk_usage(CACHE_DIR.anchor)
    process = psutil.Process()
    snapshot: dict[str, object] = {
        "physical_ram_total_bytes": int(virtual.total),
        "physical_ram_available_bytes": int(virtual.available),
        "physical_ram_used_bytes": int(virtual.used),
        "process_rss_bytes": int(process.memory_info().rss),
        "cache_drive_total_bytes": int(disk.total),
        "cache_drive_free_bytes": int(disk.free),
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


def load_manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def save_manifest(manifest: dict[str, object]) -> None:
    write_json(MANIFEST_PATH, manifest)


def set_component(name: str, status: str, **details: object) -> None:
    manifest = load_manifest()
    components = manifest["components"]
    assert isinstance(components, dict)
    components[name] = {
        "status": status,
        "completed_at": utc_now(),
        **details,
    }
    save_manifest(manifest)


def initialize_manifest() -> None:
    import accelerate
    import safetensors
    import transformers

    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"Missing locked plan: {PLAN_PATH}")
    if not torch.cuda.is_available():
        raise RuntimeError("R016 requires the RTX 4090 CUDA device.")
    previous_attempts: list[dict[str, object]] = []
    if MANIFEST_PATH.exists():
        previous = load_manifest()
        if previous.get("status") == "successful":
            raise RuntimeError("R016 is already successful; refusing to overwrite it.")
        previous_attempts = list(previous.get("attempt_history", []))
        previous_attempts.append(
            {
                "status": previous.get("status"),
                "started_at": previous.get("started_at"),
                "completed_at": previous.get("completed_at"),
                "failure_details": previous.get("failure_details"),
            }
        )

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    started_at = utc_now()
    components = {name: {"status": "pending"} for name in REQUIRED_COMPONENTS}
    components["plan_lock"] = {
        "status": "successful",
        "completed_at": started_at,
        "path": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
        "sha256": sha256_file(PLAN_PATH),
    }
    components["environment_preflight"] = {
        "status": "successful",
        "completed_at": started_at,
        "python": sys.version,
        "executable": sys.executable,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "accelerate": accelerate.__version__,
        "safetensors": safetensors.__version__,
        "memory_before": memory_snapshot(),
        "gpu_limit": GPU_LIMIT,
        "cpu_limit": CPU_LIMIT,
        "cache_dir": str(CACHE_DIR),
        "offload_dir": str(OFFLOAD_DIR),
    }
    manifest: dict[str, object] = {
        "schema_version": 1,
        "run_id": RUN_ID,
        "status": "running",
        "started_at": started_at,
        "completed_at": None,
        "failure_details": None,
        "objective": (
            "Determine whether the exact native-BF16 OLMo 3 32B Base model can "
            "complete one local instrumented final-anchor forward pass."
        ),
        "model": {
            "id": MODEL_ID,
            "revision": MODEL_REVISION,
            "precision": "bfloat16",
            "quantized": False,
            "expected_repository_bytes": EXPECTED_REPOSITORY_BYTES,
        },
        "prompt": {
            "text": PROMPT,
            "capture_position": "final newline anchor",
            "chat_template_used": False,
            "generation_executed": False,
        },
        "expected": {
            "transformer_layers": EXPECTED_LAYERS,
            "hidden_width": EXPECTED_HIDDEN_WIDTH,
            "hidden_states": EXPECTED_STATES,
        },
        "required_components": list(REQUIRED_COMPONENTS),
        "components": components,
        "artifacts": {},
        "attempt_history": previous_attempts,
        "interpretation_boundary": (
            "R016 tests local native-BF16 model loading and one instrumented "
            "forward pass only; topology construction and semantic interpretation "
            "are excluded."
        ),
    }
    save_manifest(manifest)


def fail_run(stage: str, error: BaseException) -> None:
    if not MANIFEST_PATH.exists():
        return
    manifest = load_manifest()
    completed_at = utc_now()
    manifest["status"] = "failed"
    manifest["completed_at"] = completed_at
    manifest["failure_details"] = {
        "component": stage,
        "error_type": type(error).__name__,
        "message": str(error),
        "traceback": traceback.format_exc(),
        "memory_at_failure": memory_snapshot(),
    }
    components = manifest["components"]
    assert isinstance(components, dict)
    components[stage] = {
        "status": "failed",
        "completed_at": completed_at,
        "error_type": type(error).__name__,
        "message": str(error),
    }
    save_manifest(manifest)
    write_report(manifest)


def write_report(manifest: dict[str, object]) -> None:
    status = manifest.get("status", "unknown")
    components = manifest.get("components", {})
    failure = manifest.get("failure_details")
    lines = [
        "# R016 OLMo 3 32B local BF16 feasibility report",
        "",
        f"- Status: **{status}**",
        f"- Model: `{MODEL_ID}`",
        f"- Revision: `{MODEL_REVISION}`",
        "- Precision: native BF16",
        f"- Placement caps: CUDA `{GPU_LIMIT}`; CPU `{CPU_LIMIT}`; remainder on disk",
        "- Response generation: **not executed**",
        "",
        "## Component results",
        "",
    ]
    if isinstance(components, dict):
        for name in REQUIRED_COMPONENTS:
            component = components.get(name, {})
            component_status = (
                component.get("status", "missing")
                if isinstance(component, dict)
                else "invalid"
            )
            lines.append(f"- `{name}`: `{component_status}`")
    if failure:
        lines.extend(
            [
                "",
                "## Failure",
                "",
                f"- Component: `{failure.get('component')}`",
                f"- Error: `{failure.get('error_type')}: {failure.get('message')}`",
            ]
        )
    elif status == "successful":
        lines.extend(
            [
                "",
                "## Decision",
                "",
                (
                    "OLMo 3 32B Base is locally feasible for the project's "
                    "instrumented first-token-prediction capture workload under "
                    "the measured mixed GPU/CPU/disk placement."
                ),
            ]
        )
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    stage = "initialization"
    model = None
    outputs = None
    started = time.perf_counter()
    try:
        initialize_manifest()

        stage = "model_metadata_lock"
        metadata_started = time.perf_counter()
        model_info = HfApi().model_info(
            MODEL_ID,
            revision=MODEL_REVISION,
            files_metadata=True,
        )
        repository_bytes = sum(item.size or 0 for item in model_info.siblings)
        if model_info.sha != MODEL_REVISION:
            raise RuntimeError(
                f"Resolved revision {model_info.sha} does not match {MODEL_REVISION}."
            )
        if repository_bytes != EXPECTED_REPOSITORY_BYTES:
            raise RuntimeError(
                f"Repository size {repository_bytes} does not match "
                f"{EXPECTED_REPOSITORY_BYTES}."
            )
        set_component(
            stage,
            "successful",
            resolved_revision=model_info.sha,
            repository_bytes=repository_bytes,
            sibling_files=len(model_info.siblings),
            seconds=time.perf_counter() - metadata_started,
        )

        stage = "snapshot_download"
        download_started = time.perf_counter()
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        snapshot_path = Path(
            snapshot_download(
                repo_id=MODEL_ID,
                revision=MODEL_REVISION,
                cache_dir=CACHE_DIR,
                allow_patterns=[
                    "config.json",
                    "generation_config.json",
                    "merges.txt",
                    "model-*.safetensors",
                    "model.safetensors.index.json",
                    "special_tokens_map.json",
                    "tokenizer.json",
                    "tokenizer_config.json",
                    "vocab.json",
                ],
                max_workers=1,
            )
        )
        if not snapshot_path.is_dir():
            raise RuntimeError("snapshot_download returned a missing directory.")
        weight_shards = sorted(snapshot_path.glob("model-*.safetensors"))
        if len(weight_shards) != 14:
            raise RuntimeError(f"Expected 14 weight shards; found {len(weight_shards)}.")
        set_component(
            stage,
            "successful",
            snapshot_path=str(snapshot_path),
            weight_shards=len(weight_shards),
            seconds=time.perf_counter() - download_started,
            memory_after=memory_snapshot(),
        )

        stage = "device_map_preflight"
        map_started = time.perf_counter()
        config = AutoConfig.from_pretrained(snapshot_path, local_files_only=True)
        if config.num_hidden_layers != EXPECTED_LAYERS:
            raise RuntimeError(
                f"Expected {EXPECTED_LAYERS} layers; config has "
                f"{config.num_hidden_layers}."
            )
        if config.hidden_size != EXPECTED_HIDDEN_WIDTH:
            raise RuntimeError(
                f"Expected hidden width {EXPECTED_HIDDEN_WIDTH}; config has "
                f"{config.hidden_size}."
            )
        with init_empty_weights():
            empty_model = AutoModelForCausalLM.from_config(
                config,
                dtype=torch.bfloat16,
            )
        no_split_modules = list(
            getattr(empty_model, "_no_split_modules", None)
            or ["Olmo3DecoderLayer"]
        )
        device_map = infer_auto_device_map(
            empty_model,
            max_memory=MAX_MEMORY,
            no_split_module_classes=no_split_modules,
            dtype=torch.bfloat16,
            offload_buffers=True,
            fallback_allocation=True,
        )
        del empty_model
        gc.collect()
        placements: dict[str, int] = {}
        for placement in device_map.values():
            key = str(placement)
            placements[key] = placements.get(key, 0) + 1
        if "disk" not in placements:
            raise RuntimeError(
                "The locked 18 GiB GPU / 28 GiB CPU limits unexpectedly produced "
                "no disk placement; feasibility configuration has drifted."
            )
        write_json(
            DEVICE_MAP_PATH,
            {
                "model": MODEL_ID,
                "revision": MODEL_REVISION,
                "dtype": "bfloat16",
                "max_memory": MAX_MEMORY,
                "no_split_module_classes": no_split_modules,
                "placement_counts": placements,
                "device_map": device_map,
            },
        )
        set_component(
            stage,
            "successful",
            placements=placements,
            device_map_path=str(DEVICE_MAP_PATH.relative_to(PROJECT_DIR)).replace(
                "\\", "/"
            ),
            device_map_sha256=sha256_file(DEVICE_MAP_PATH),
            seconds=time.perf_counter() - map_started,
        )

        stage = "model_load"
        load_started = time.perf_counter()
        OFFLOAD_DIR.mkdir(parents=True, exist_ok=True)
        torch.cuda.reset_peak_memory_stats()
        model = AutoModelForCausalLM.from_pretrained(
            snapshot_path,
            revision=MODEL_REVISION,
            dtype=torch.bfloat16,
            device_map=device_map,
            max_memory=MAX_MEMORY,
            offload_folder=OFFLOAD_DIR,
            offload_state_dict=True,
            offload_buffers=True,
            low_cpu_mem_usage=True,
            local_files_only=True,
        )
        model.eval()
        resolved_map = getattr(model, "hf_device_map", device_map)
        set_component(
            stage,
            "successful",
            seconds=time.perf_counter() - load_started,
            resolved_device_map=json_safe(resolved_map),
            memory_after=memory_snapshot(),
            peak_gpu_allocated_bytes=int(torch.cuda.max_memory_allocated()),
            peak_gpu_reserved_bytes=int(torch.cuda.max_memory_reserved()),
        )

        stage = "instrumented_forward"
        tokenizer = AutoTokenizer.from_pretrained(snapshot_path, local_files_only=True)
        anchor_ids = tokenizer.encode("\n", add_special_tokens=False)
        if len(anchor_ids) != 1:
            raise RuntimeError(f"Newline anchor is not one token: {anchor_ids}")
        inputs = tokenizer(
            PROMPT,
            return_tensors="pt",
            add_special_tokens=False,
            return_token_type_ids=False,
        )
        if int(inputs["input_ids"][0, -1]) != anchor_ids[0]:
            raise RuntimeError("Final prompt token is not the newline anchor.")
        input_device = torch.device("cuda:0")
        inputs = {name: tensor.to(input_device) for name, tensor in inputs.items()}
        torch.cuda.reset_peak_memory_stats()
        forward_started = time.perf_counter()
        with torch.inference_mode():
            outputs = model(
                **inputs,
                output_hidden_states=True,
                use_cache=False,
                return_dict=True,
            )
        torch.cuda.synchronize()
        forward_seconds = time.perf_counter() - forward_started
        set_component(
            stage,
            "successful",
            seconds=forward_seconds,
            input_tokens=int(inputs["input_ids"].shape[1]),
            anchor_token_id=anchor_ids[0],
            hidden_states_returned=len(outputs.hidden_states or ()),
            logits_shape=list(outputs.logits.shape),
            response_generation_executed=False,
            memory_after=memory_snapshot(),
            peak_gpu_allocated_bytes=int(torch.cuda.max_memory_allocated()),
            peak_gpu_reserved_bytes=int(torch.cuda.max_memory_reserved()),
        )

        stage = "capture_validation"
        validation_started = time.perf_counter()
        hidden_states = outputs.hidden_states
        if hidden_states is None or len(hidden_states) != EXPECTED_STATES:
            count = 0 if hidden_states is None else len(hidden_states)
            raise RuntimeError(f"Expected {EXPECTED_STATES} hidden states; found {count}.")
        anchor_vectors = []
        state_shapes = []
        for index, state in enumerate(hidden_states):
            state_shapes.append(list(state.shape))
            if state.shape[-1] != EXPECTED_HIDDEN_WIDTH:
                raise RuntimeError(
                    f"State {index} width {state.shape[-1]} != "
                    f"{EXPECTED_HIDDEN_WIDTH}."
                )
            anchor = state[0, -1].detach().to(device="cpu", dtype=torch.bfloat16)
            if not torch.isfinite(anchor.float()).all():
                raise RuntimeError(f"State {index} contains non-finite values.")
            anchor_vectors.append(anchor.contiguous())
        capture = torch.stack(anchor_vectors)
        logits = outputs.logits[0, -1].detach().to(device="cpu", dtype=torch.float32)
        if not torch.isfinite(logits).all():
            raise RuntimeError("First-token logits contain non-finite values.")
        top_values, top_indices = torch.topk(logits, k=10)
        top_tokens = tokenizer.convert_ids_to_tokens(top_indices.tolist())
        save_file(
            {"anchor_hidden_states": capture},
            str(CAPTURE_PATH),
            metadata={
                "model_id": MODEL_ID,
                "revision": MODEL_REVISION,
                "prompt": PROMPT,
                "anchor_token_id": str(anchor_ids[0]),
                "response_generation_executed": "false",
            },
        )
        validation = {
            "status": "successful",
            "model_id": MODEL_ID,
            "revision": MODEL_REVISION,
            "precision": "bfloat16",
            "prompt": PROMPT,
            "input_ids": inputs["input_ids"][0].detach().cpu().tolist(),
            "anchor_token_id": anchor_ids[0],
            "hidden_states": len(hidden_states),
            "hidden_width": int(capture.shape[1]),
            "capture_shape": list(capture.shape),
            "all_hidden_states_finite": True,
            "logits_shape": list(logits.shape),
            "all_logits_finite": True,
            "top_10_next_tokens": [
                {
                    "token_id": int(token_id),
                    "token": token,
                    "logit": float(value),
                }
                for token_id, token, value in zip(
                    top_indices.tolist(), top_tokens, top_values.tolist(), strict=True
                )
            ],
            "state_shapes": state_shapes,
            "response_generation_executed": False,
        }
        write_json(VALIDATION_PATH, validation)
        set_component(
            stage,
            "successful",
            seconds=time.perf_counter() - validation_started,
            validation_path=str(VALIDATION_PATH.relative_to(PROJECT_DIR)).replace(
                "\\", "/"
            ),
            validation_sha256=sha256_file(VALIDATION_PATH),
            capture_path=str(CAPTURE_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
            capture_bytes=CAPTURE_PATH.stat().st_size,
            capture_sha256=sha256_file(CAPTURE_PATH),
        )

        stage = "resource_cleanup"
        cleanup_started = time.perf_counter()
        del outputs, hidden_states, anchor_vectors, capture, logits, inputs, model
        outputs = None
        model = None
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        set_component(
            stage,
            "successful",
            seconds=time.perf_counter() - cleanup_started,
            memory_after=memory_snapshot(),
            offload_cache_preserved=True,
        )

        stage = "feasibility_decision"
        set_component(
            stage,
            "successful",
            decision="locally_feasible",
            basis=(
                "The exact native-BF16 model completed one instrumented "
                "forward pass with all expected hidden states and finite logits."
            ),
        )
        manifest = load_manifest()
        completed_at = utc_now()
        manifest["status"] = "successful"
        manifest["completed_at"] = completed_at
        manifest["failure_details"] = None
        manifest["total_seconds"] = time.perf_counter() - started
        manifest["artifacts"] = {
            "device_map.json": {
                "bytes": DEVICE_MAP_PATH.stat().st_size,
                "sha256": sha256_file(DEVICE_MAP_PATH),
            },
            "capture_validation.json": {
                "bytes": VALIDATION_PATH.stat().st_size,
                "sha256": sha256_file(VALIDATION_PATH),
            },
            "anchor_hidden_states.safetensors": {
                "bytes": CAPTURE_PATH.stat().st_size,
                "sha256": sha256_file(CAPTURE_PATH),
                "tracked_by_git": False,
            },
        }
        save_manifest(manifest)
        write_report(manifest)
        manifest = load_manifest()
        artifacts = manifest["artifacts"]
        assert isinstance(artifacts, dict)
        artifacts[REPORT_PATH.name] = {
            "bytes": REPORT_PATH.stat().st_size,
            "sha256": sha256_file(REPORT_PATH),
        }
        save_manifest(manifest)
        print(json.dumps({"status": "successful", "manifest": str(MANIFEST_PATH)}))
        return 0
    except BaseException as error:
        try:
            if outputs is not None:
                del outputs
            if model is not None:
                del model
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        finally:
            fail_run(stage, error)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
