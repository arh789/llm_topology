"""Capture six controlled bare-concept anchor trajectories for R013."""

from __future__ import annotations

import csv
import gc
import hashlib
import itertools
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RUN_ID = "R013_qwen-bare-concept-permutation-topology"
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
MODEL_REVISION = "a09a35458c702b33eeacc393d103063234e8bc28"
HF_HOME = Path(r"D:\AI\cache\huggingface")
HF_HUB_CACHE = HF_HOME / "hub"
ANCHOR_TEXT = "\n"
CONCEPTS = {
    "A": "electro pink",
    "B": "curvature density",
    "C": "Tokyo nightlife",
}
PERMUTATIONS = ("ABC", "ACB", "BAC", "BCA", "CAB", "CBA")
PROMPTS = {
    label: "".join(f"{CONCEPTS[key]}\n" for key in label)
    for label in PERMUTATIONS
}

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
OUTPUT_DIR = RUN_DIR / "primary_7b_bf16"
MANIFEST_PATH = RUN_DIR / "manifest.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def write_manifest(manifest: dict) -> None:
    write_json(MANIFEST_PATH, manifest)


def update_component(name: str, status: str, **values: Any) -> None:
    manifest = load_manifest()
    manifest["components"][name] = {
        "status": status,
        **values,
    }
    write_manifest(manifest)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def configure_cache() -> None:
    expected_home = HF_HOME.resolve()
    expected_hub = HF_HUB_CACHE.resolve()
    configured_home = Path(os.environ.get("HF_HOME", str(HF_HOME))).resolve()
    configured_hub = Path(os.environ.get("HF_HUB_CACHE", str(HF_HUB_CACHE))).resolve()
    if configured_home != expected_home or configured_hub != expected_hub:
        raise RuntimeError(
            "Model cache must resolve to D:\\AI\\cache\\huggingface and its hub."
        )
    os.environ["HF_HOME"] = str(HF_HOME)
    os.environ["HF_HUB_CACHE"] = str(HF_HUB_CACHE)
    os.environ["TRANSFORMERS_CACHE"] = str(HF_HUB_CACHE)
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"


def capture_final_position(model: Any, encoded: dict[str, Any], torch: Any) -> Any:
    device_inputs = {key: value.to("cuda:0") for key, value in encoded.items()}
    with torch.inference_mode():
        outputs = model(
            **device_inputs,
            output_hidden_states=True,
            use_cache=False,
            return_dict=True,
        )
    if outputs.hidden_states is None:
        raise RuntimeError("Model returned no hidden states.")
    trajectory = torch.stack(
        [state[0, -1, :].detach().to("cpu") for state in outputs.hidden_states]
    ).contiguous()
    del outputs, device_inputs
    return trajectory


def state_label(state_index: int, state_count: int, layer_count: int) -> str:
    if state_index == 0:
        return "input_embedding"
    if state_index == state_count - 1:
        return f"final_norm_after_block_{layer_count - 1}"
    return f"block_{state_index - 1}_output"


def main() -> int:
    configure_cache()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    status_path = OUTPUT_DIR / "status.json"
    started_at = utc_now()
    started = time.perf_counter()
    current_component = "anchor_probe"
    write_json(
        status_path,
        {
            "status": "running",
            "started_at": started_at,
            "run_id": RUN_ID,
            "model_id": MODEL_ID,
            "revision": MODEL_REVISION,
        },
    )
    update_component(
        "anchor_probe",
        "running",
        started_at=started_at,
        candidate_anchor=ANCHOR_TEXT,
    )

    try:
        import torch
        import transformers
        from safetensors.torch import save_file
        from transformers import AutoModelForCausalLM, AutoTokenizer

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA is unavailable.")

        torch.manual_seed(0)
        torch.cuda.manual_seed_all(0)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        free_before, total_memory = torch.cuda.mem_get_info()

        tokenizer_started = time.perf_counter()
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_ID,
            revision=MODEL_REVISION,
            cache_dir=str(HF_HUB_CACHE),
            trust_remote_code=False,
            local_files_only=True,
        )
        tokenizer_seconds = time.perf_counter() - tokenizer_started

        anchor_ids = tokenizer(
            ANCHOR_TEXT,
            add_special_tokens=False,
        )["input_ids"]
        if len(anchor_ids) != 1:
            raise RuntimeError(
                f"Candidate newline anchor produced {len(anchor_ids)} tokens, not one."
            )
        anchor_token_id = int(anchor_ids[0])
        anchor_token = tokenizer.convert_ids_to_tokens([anchor_token_id])[0]

        encoded_prompts: dict[str, dict[str, Any]] = {}
        probe_records: dict[str, dict[str, Any]] = {}
        for label, prompt in PROMPTS.items():
            encoded = tokenizer(
                prompt,
                return_tensors="pt",
                add_special_tokens=False,
            )
            input_ids = encoded["input_ids"][0].tolist()
            decoded_tokens = tokenizer.convert_ids_to_tokens(input_ids)
            if not input_ids or int(input_ids[-1]) != anchor_token_id:
                raise RuntimeError(f"{label}: final token is not the candidate anchor.")
            if not prompt.endswith(ANCHOR_TEXT):
                raise RuntimeError(f"{label}: raw input does not end with the anchor.")
            encoded_prompts[label] = encoded
            probe_records[label] = {
                "input_token_count": len(input_ids),
                "capture_index": len(input_ids) - 1,
                "capture_token_id": int(input_ids[-1]),
                "capture_token": decoded_tokens[-1],
            }

        update_component(
            "anchor_probe",
            "successful",
            completed_at=utc_now(),
            anchor_text="\\n",
            anchor_token_id=anchor_token_id,
            anchor_token=anchor_token,
            single_token=True,
            final_anchor_matches_all_permutations=True,
            input_token_counts={
                label: record["input_token_count"]
                for label, record in probe_records.items()
            },
        )

        current_component = "primary_capture"
        update_component(
            current_component,
            "running",
            started_at=utc_now(),
            permutation_count=len(PERMUTATIONS),
        )
        model_started = time.perf_counter()
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_ID,
            revision=MODEL_REVISION,
            cache_dir=str(HF_HUB_CACHE),
            dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=False,
            attn_implementation="eager",
            local_files_only=True,
        )
        model.to("cuda:0")
        model.eval()
        model_seconds = time.perf_counter() - model_started

        hidden_width = int(model.config.hidden_size)
        layer_count = int(model.config.num_hidden_layers)
        state_count = layer_count + 1
        resolved_revision = getattr(model.config, "_commit_hash", None)
        if resolved_revision != MODEL_REVISION:
            raise RuntimeError(
                f"Resolved revision {resolved_revision!r} does not match locked revision."
            )
        if (state_count, hidden_width) != (29, 3584):
            raise RuntimeError(
                f"Expected trajectory shape (29, 3584), model reports "
                f"({state_count}, {hidden_width})."
            )

        trajectories: dict[str, Any] = {}
        prompt_records: dict[str, Any] = {}
        capture_timings: dict[str, float] = {}
        replay_timings: dict[str, float] = {}

        for label in PERMUTATIONS:
            encoded = encoded_prompts[label]
            input_ids = encoded["input_ids"][0].tolist()
            decoded_tokens = tokenizer.convert_ids_to_tokens(input_ids)

            capture_started = time.perf_counter()
            first = capture_final_position(model, encoded, torch)
            capture_timings[label] = time.perf_counter() - capture_started

            replay_started = time.perf_counter()
            replay = capture_final_position(model, encoded, torch)
            replay_timings[label] = time.perf_counter() - replay_started

            if tuple(first.shape) != (state_count, hidden_width):
                raise RuntimeError(
                    f"{label}: expected {(state_count, hidden_width)}, "
                    f"received {tuple(first.shape)}."
                )
            if not torch.isfinite(first.float()).all():
                raise RuntimeError(f"{label}: capture contains non-finite values.")
            if not torch.equal(first, replay):
                raise RuntimeError(f"{label}: deterministic replay differs.")

            trajectory_path = OUTPUT_DIR / f"{label}_hidden_states.safetensors"
            save_file({"hidden_states": first}, str(trajectory_path))
            trajectories[label] = first
            prompt_records[label] = {
                "permutation": label,
                "position_1": CONCEPTS[label[0]],
                "position_2": CONCEPTS[label[1]],
                "position_3": CONCEPTS[label[2]],
                "raw_prompt": PROMPTS[label],
                "chat_template_applied": False,
                "special_tokens_added": False,
                "input_ids": input_ids,
                "decoded_tokens": decoded_tokens,
                "input_token_count": len(input_ids),
                "capture_index": len(input_ids) - 1,
                "capture_token_id": int(input_ids[-1]),
                "capture_token": decoded_tokens[-1],
                "trajectory_file": trajectory_path.name,
                "trajectory_shape": list(first.shape),
                "trajectory_dtype": str(first.dtype),
                "deterministic_replay_exact": True,
            }
            del replay, encoded_prompts[label]
            print(
                f"R013 capture {label}: {list(first.shape)}, "
                f"{capture_timings[label]:.3f}s + replay {replay_timings[label]:.3f}s.",
                flush=True,
            )

        update_component(
            current_component,
            "successful",
            completed_at=utc_now(),
            permutation_count=len(trajectories),
            state_count=state_count,
            hidden_width=hidden_width,
            response_generation_executed=False,
        )

        current_component = "capture_validation"
        update_component(
            current_component,
            "running",
            started_at=utc_now(),
        )
        reference = trajectories[PERMUTATIONS[0]]
        for label in PERMUTATIONS[1:]:
            if not torch.equal(reference[0], trajectories[label][0]):
                raise RuntimeError(
                    f"State 00 differs between {PERMUTATIONS[0]} and {label}."
                )

        metrics_path = OUTPUT_DIR / "pairwise_hidden_state_metrics.csv"
        minimum_cosine = 1.0
        minimum_cosine_identity: dict[str, Any] | None = None
        maximum_l2 = 0.0
        maximum_l2_identity: dict[str, Any] | None = None
        with metrics_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "source_permutation",
                    "target_permutation",
                    "state_index",
                    "state_label",
                    "cosine_similarity",
                    "l2_distance",
                    "exact_equal",
                ]
            )
            for source_label, target_label in itertools.combinations(PERMUTATIONS, 2):
                source = trajectories[source_label].float()
                target = trajectories[target_label].float()
                cosine = torch.nn.functional.cosine_similarity(source, target, dim=1)
                l2 = torch.linalg.vector_norm(source - target, dim=1)
                exact = torch.all(
                    trajectories[source_label] == trajectories[target_label], dim=1
                )
                for state_index in range(state_count):
                    cosine_value = float(cosine[state_index])
                    l2_value = float(l2[state_index])
                    writer.writerow(
                        [
                            source_label,
                            target_label,
                            state_index,
                            state_label(state_index, state_count, layer_count),
                            cosine_value,
                            l2_value,
                            bool(exact[state_index]),
                        ]
                    )
                    if cosine_value < minimum_cosine:
                        minimum_cosine = cosine_value
                        minimum_cosine_identity = {
                            "source": source_label,
                            "target": target_label,
                            "state_index": state_index,
                        }
                    if l2_value > maximum_l2:
                        maximum_l2 = l2_value
                        maximum_l2_identity = {
                            "source": source_label,
                            "target": target_label,
                            "state_index": state_index,
                        }

        write_json(OUTPUT_DIR / "prompt_records.json", prompt_records)
        validation = {
            "status": "successful",
            "permutation_count": len(PERMUTATIONS),
            "permutations": list(PERMUTATIONS),
            "state_count": state_count,
            "hidden_width": hidden_width,
            "all_finite": True,
            "deterministic_replay_exact": True,
            "anchor_text": "\\n",
            "anchor_single_token": True,
            "anchor_token_id": anchor_token_id,
            "anchor_token": anchor_token,
            "anchor_matches_all_permutations": True,
            "state_00_exact_equal_all_permutations": True,
            "input_token_counts": {
                label: prompt_records[label]["input_token_count"]
                for label in PERMUTATIONS
            },
            "pair_count": 15,
            "pair_state_metric_rows": 15 * state_count,
            "minimum_cosine_similarity": minimum_cosine,
            "minimum_cosine_identity": minimum_cosine_identity,
            "maximum_l2_distance": maximum_l2,
            "maximum_l2_identity": maximum_l2_identity,
        }
        write_json(OUTPUT_DIR / "permutation_validation.json", validation)

        free_after, _ = torch.cuda.mem_get_info()
        metadata = {
            "status": "successful",
            "started_at": started_at,
            "completed_at": utc_now(),
            "run_id": RUN_ID,
            "model_id": MODEL_ID,
            "revision_requested": MODEL_REVISION,
            "revision_resolved": resolved_revision,
            "model_class": model.__class__.__name__,
            "tokenizer_class": tokenizer.__class__.__name__,
            "transformers_version": transformers.__version__,
            "torch_version": torch.__version__,
            "cuda_runtime": torch.version.cuda,
            "gpu_name": torch.cuda.get_device_name(0),
            "dtype": "torch.bfloat16",
            "layer_count": layer_count,
            "state_count": state_count,
            "hidden_width": hidden_width,
            "tokenizer_load_seconds": tokenizer_seconds,
            "model_load_seconds": model_seconds,
            "capture_seconds": capture_timings,
            "replay_seconds": replay_timings,
            "elapsed_seconds": time.perf_counter() - started,
            "gpu_total_bytes": total_memory,
            "gpu_free_before_load_bytes": free_before,
            "gpu_free_after_capture_bytes": free_after,
            "gpu_peak_allocated_bytes": torch.cuda.max_memory_allocated(),
            "gpu_peak_reserved_bytes": torch.cuda.max_memory_reserved(),
            "chat_template_applied": False,
            "response_generation_executed": False,
            "model_loaded_from_shared_cache_only": True,
        }
        write_json(OUTPUT_DIR / "run_metadata.json", metadata)

        update_component(
            current_component,
            "successful",
            completed_at=utc_now(),
            state_00_exact_equal_all_permutations=True,
            deterministic_replay_exact=True,
            all_finite=True,
            pair_state_metric_rows=15 * state_count,
        )

        del model, tokenizer, trajectories, reference
        gc.collect()
        torch.cuda.empty_cache()

        artifact_hashes: dict[str, Any] = {}
        for path in sorted(OUTPUT_DIR.iterdir()):
            if path.is_file() and path.name not in {
                "artifact_hashes.json",
                "status.json",
            }:
                artifact_hashes[path.name] = {
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
        write_json(OUTPUT_DIR / "artifact_hashes.json", artifact_hashes)
        write_json(
            status_path,
            {
                "status": "successful",
                "completed_at": utc_now(),
                "run_id": RUN_ID,
                "model_id": MODEL_ID,
                "revision": MODEL_REVISION,
                "elapsed_seconds": time.perf_counter() - started,
            },
        )
        print(json.dumps(validation, indent=2), flush=True)
        return 0
    except Exception as error:
        failure = {
            "status": "failed",
            "failed_at": utc_now(),
            "run_id": RUN_ID,
            "component": current_component,
            "model_id": MODEL_ID,
            "revision": MODEL_REVISION,
            "error_type": type(error).__name__,
            "error": str(error),
            "elapsed_seconds": time.perf_counter() - started,
        }
        write_json(OUTPUT_DIR / "failure.json", failure)
        write_json(status_path, failure)
        if MANIFEST_PATH.exists():
            manifest = load_manifest()
            manifest["status"] = "failed"
            manifest["completed_at"] = failure["failed_at"]
            manifest["failure_details"] = {
                "component": current_component,
                "error_type": type(error).__name__,
                "message": str(error),
            }
            manifest["components"][current_component] = {
                "status": "failed",
                "failed_at": failure["failed_at"],
                "error_type": type(error).__name__,
                "message": str(error),
            }
            write_manifest(manifest)
        print(json.dumps(failure, indent=2), file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
