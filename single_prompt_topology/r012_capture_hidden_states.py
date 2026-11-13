"""Capture paired whole-prompt final-position trajectories from Qwen2.5."""

from __future__ import annotations

import argparse
import csv
import gc
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


HF_HOME = Path(r"D:\AI\cache\huggingface")
HF_HUB_CACHE = HF_HOME / "hub"
BASELINE_PROMPT = (
    "What structure forms from electro pink, curvature density, Tokyo nightlife?"
)
VARIATION_PROMPT = (
    "What structure forms from electro pink, Tokyo nightlife, curvature density?"
)
PROMPTS = {"baseline": BASELINE_PROMPT, "variation": VARIATION_PROMPT}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--revision", default="main")
    parser.add_argument("--stage", required=True, choices=("smoke_0_5b", "primary_7b"))
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    configure_cache()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    status_path = args.output_dir / "status.json"
    write_json(
        status_path,
        {
            "status": "running",
            "started_at": utc_now(),
            "stage": args.stage,
            "model_id": args.model_id,
            "revision_requested": args.revision,
        },
    )

    started = time.perf_counter()
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
            args.model_id,
            revision=args.revision,
            cache_dir=str(HF_HUB_CACHE),
            trust_remote_code=False,
        )
        tokenizer_seconds = time.perf_counter() - tokenizer_started
        if not getattr(tokenizer, "chat_template", None):
            raise RuntimeError("Tokenizer has no official chat template.")

        model_started = time.perf_counter()
        model = AutoModelForCausalLM.from_pretrained(
            args.model_id,
            revision=args.revision,
            cache_dir=str(HF_HUB_CACHE),
            dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=False,
            attn_implementation="eager",
        )
        model.to("cuda:0")
        model.eval()
        model_seconds = time.perf_counter() - model_started

        hidden_width = int(model.config.hidden_size)
        layer_count = int(model.config.num_hidden_layers)
        expected_state_count = layer_count + 1
        resolved_revision = getattr(model.config, "_commit_hash", None)

        trajectories: dict[str, Any] = {}
        prompt_records: dict[str, Any] = {}
        capture_timings: dict[str, float] = {}
        replay_timings: dict[str, float] = {}

        for label, prompt in PROMPTS.items():
            templated = tokenizer.apply_chat_template(
                [{"role": "user", "content": prompt}],
                tokenize=False,
                add_generation_prompt=True,
            )
            encoded = tokenizer(
                templated,
                return_tensors="pt",
                add_special_tokens=False,
            )
            input_ids = encoded["input_ids"][0].tolist()
            decoded_tokens = tokenizer.convert_ids_to_tokens(input_ids)

            capture_started = time.perf_counter()
            first = capture_final_position(model, encoded, torch)
            capture_timings[label] = time.perf_counter() - capture_started

            replay_started = time.perf_counter()
            replay = capture_final_position(model, encoded, torch)
            replay_timings[label] = time.perf_counter() - replay_started

            if tuple(first.shape) != (expected_state_count, hidden_width):
                raise RuntimeError(
                    f"{label}: expected {(expected_state_count, hidden_width)}, "
                    f"received {tuple(first.shape)}."
                )
            if not torch.isfinite(first.float()).all():
                raise RuntimeError(f"{label}: capture contains non-finite values.")
            if not torch.equal(first, replay):
                raise RuntimeError(f"{label}: deterministic replay differs.")

            trajectory_path = args.output_dir / f"{label}_hidden_states.safetensors"
            save_file({"hidden_states": first}, str(trajectory_path))
            trajectories[label] = first
            prompt_records[label] = {
                "raw_prompt": prompt,
                "templated_prompt": templated,
                "input_ids": input_ids,
                "decoded_tokens": decoded_tokens,
                "input_token_count": len(input_ids),
                "capture_index": len(input_ids) - 1,
                "capture_token_id": input_ids[-1],
                "capture_token": decoded_tokens[-1],
                "trajectory_file": trajectory_path.name,
                "trajectory_shape": list(first.shape),
                "trajectory_dtype": str(first.dtype),
                "deterministic_replay_exact": True,
            }
            del replay, encoded

        baseline = trajectories["baseline"].float()
        variation = trajectories["variation"].float()
        if baseline.shape != variation.shape:
            raise RuntimeError("Paired trajectory shapes differ.")
        if (
            prompt_records["baseline"]["capture_token_id"]
            != prompt_records["variation"]["capture_token_id"]
        ):
            raise RuntimeError("Paired prompts use different capture-token IDs.")
        if not torch.equal(trajectories["baseline"][0], trajectories["variation"][0]):
            raise RuntimeError("State 00 differs across the controlled prompt pair.")

        exact_equal_by_state = torch.all(
            trajectories["baseline"] == trajectories["variation"], dim=1
        )
        if bool(torch.all(exact_equal_by_state[1:])):
            raise RuntimeError("No post-embedding state differs across prompts.")

        cosine = torch.nn.functional.cosine_similarity(baseline, variation, dim=1)
        l2 = torch.linalg.vector_norm(baseline - variation, dim=1)
        metrics_path = args.output_dir / "layer_pair_metrics.csv"
        with metrics_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "state_index",
                    "state_label",
                    "cosine_similarity",
                    "l2_distance",
                    "exact_equal",
                ]
            )
            for state_index in range(expected_state_count):
                if state_index == 0:
                    state_label = "input_embedding"
                elif state_index == expected_state_count - 1:
                    state_label = f"final_norm_after_block_{layer_count - 1}"
                else:
                    state_label = f"block_{state_index - 1}_output"
                writer.writerow(
                    [
                        state_index,
                        state_label,
                        float(cosine[state_index]),
                        float(l2[state_index]),
                        bool(exact_equal_by_state[state_index]),
                    ]
                )

        write_json(args.output_dir / "prompt_records.json", prompt_records)
        validation = {
            "status": "successful",
            "state_count": expected_state_count,
            "hidden_width": hidden_width,
            "all_finite": True,
            "deterministic_replay_exact": True,
            "capture_token_matches": True,
            "state_00_exact_equal": True,
            "later_state_differs": True,
            "minimum_cosine_similarity": float(torch.min(cosine)),
            "minimum_cosine_state": int(torch.argmin(cosine)),
            "maximum_l2_distance": float(torch.max(l2)),
            "maximum_l2_state": int(torch.argmax(l2)),
        }
        write_json(args.output_dir / "pair_validation.json", validation)

        free_after, _ = torch.cuda.mem_get_info()
        metadata = {
            "status": "successful",
            "completed_at": utc_now(),
            "stage": args.stage,
            "model_id": args.model_id,
            "revision_requested": args.revision,
            "revision_resolved": resolved_revision,
            "model_class": model.__class__.__name__,
            "tokenizer_class": tokenizer.__class__.__name__,
            "transformers_version": transformers.__version__,
            "torch_version": torch.__version__,
            "cuda_runtime": torch.version.cuda,
            "gpu_name": torch.cuda.get_device_name(0),
            "dtype": "torch.bfloat16",
            "layer_count": layer_count,
            "state_count": expected_state_count,
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
            "response_generation_executed": False,
        }
        write_json(args.output_dir / "run_metadata.json", metadata)

        del model, tokenizer, trajectories, baseline, variation
        gc.collect()
        torch.cuda.empty_cache()

        artifact_hashes: dict[str, Any] = {}
        for path in sorted(args.output_dir.iterdir()):
            if path.is_file() and path.name not in {"artifact_hashes.json", "status.json"}:
                artifact_hashes[path.name] = {
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
        write_json(args.output_dir / "artifact_hashes.json", artifact_hashes)
        write_json(
            status_path,
            {
                "status": "successful",
                "completed_at": utc_now(),
                "stage": args.stage,
                "model_id": args.model_id,
                "revision_requested": args.revision,
                "revision_resolved": resolved_revision,
                "elapsed_seconds": time.perf_counter() - started,
            },
        )
        print(json.dumps({"status": "successful", **validation}, indent=2))
        return 0
    except Exception as error:
        failure = {
            "status": "failed",
            "failed_at": utc_now(),
            "stage": args.stage,
            "model_id": args.model_id,
            "revision_requested": args.revision,
            "error_type": type(error).__name__,
            "error": str(error),
            "elapsed_seconds": time.perf_counter() - started,
        }
        write_json(args.output_dir / "failure.json", failure)
        write_json(status_path, failure)
        print(json.dumps(failure, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
