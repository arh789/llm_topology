"""Capture 24 controlled overlapping-context anchor trajectories for R015."""

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

from r015_config import (
    ANCHOR_TEXT,
    LOCAL_PERMUTATIONS,
    MODEL_ID,
    MODEL_REVISION,
    PROBE_PROMPT_IDS,
    PROBES,
    PROMPT_IDS,
    PROMPT_SPECS,
    RUN_ID,
)

HF_HOME = Path(r"D:\AI\cache\huggingface")
HF_HUB_CACHE = HF_HOME / "hub"

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
        anchor_records: dict[str, dict[str, Any]] = {}
        for prompt_id in PROMPT_IDS:
            prompt = str(PROMPT_SPECS[prompt_id]["raw_prompt"])
            encoded = tokenizer(
                prompt,
                return_tensors="pt",
                add_special_tokens=False,
            )
            input_ids = encoded["input_ids"][0].tolist()
            decoded_tokens = tokenizer.convert_ids_to_tokens(input_ids)
            if not input_ids or int(input_ids[-1]) != anchor_token_id:
                raise RuntimeError(
                    f"{prompt_id}: final token is not the candidate anchor."
                )
            if not prompt.endswith(ANCHOR_TEXT):
                raise RuntimeError(
                    f"{prompt_id}: raw input does not end with the anchor."
                )
            encoded_prompts[prompt_id] = encoded
            anchor_records[prompt_id] = {
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
            final_anchor_matches_all_prompts=True,
            input_token_counts={
                prompt_id: record["input_token_count"]
                for prompt_id, record in anchor_records.items()
            },
        )

        current_component = "primary_capture"
        update_component(
            current_component,
            "running",
            started_at=utc_now(),
            probe_count=len(PROBES),
            prompt_count=len(PROMPT_IDS),
            permutations_per_probe=len(LOCAL_PERMUTATIONS),
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

        for prompt_id in PROMPT_IDS:
            spec = PROMPT_SPECS[prompt_id]
            encoded = encoded_prompts[prompt_id]
            input_ids = encoded["input_ids"][0].tolist()
            decoded_tokens = tokenizer.convert_ids_to_tokens(input_ids)

            capture_started = time.perf_counter()
            first = capture_final_position(model, encoded, torch)
            capture_timings[prompt_id] = time.perf_counter() - capture_started

            replay_started = time.perf_counter()
            replay = capture_final_position(model, encoded, torch)
            replay_timings[prompt_id] = time.perf_counter() - replay_started

            if tuple(first.shape) != (state_count, hidden_width):
                raise RuntimeError(
                    f"{prompt_id}: expected {(state_count, hidden_width)}, "
                    f"received {tuple(first.shape)}."
                )
            if not torch.isfinite(first.float()).all():
                raise RuntimeError(
                    f"{prompt_id}: capture contains non-finite values."
                )
            if not torch.equal(first, replay):
                raise RuntimeError(f"{prompt_id}: deterministic replay differs.")

            trajectory_path = OUTPUT_DIR / f"{prompt_id}_hidden_states.safetensors"
            save_file({"hidden_states": first}, str(trajectory_path))
            trajectories[prompt_id] = first
            concept_order = list(spec["concept_order"])
            prompt_records[prompt_id] = {
                "prompt_id": prompt_id,
                "probe_id": spec["probe_id"],
                "local_permutation": spec["local_permutation"],
                "probe_concept_keys": list(spec["probe_concept_keys"]),
                "probe_concepts": list(spec["probe_concepts"]),
                "concept_key_order": list(spec["concept_key_order"]),
                "position_1": concept_order[0],
                "position_2": concept_order[1],
                "position_3": concept_order[2],
                "raw_prompt": spec["raw_prompt"],
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
            del replay, encoded_prompts[prompt_id]
            print(
                f"R015 capture {prompt_id}: {list(first.shape)}, "
                f"{capture_timings[prompt_id]:.3f}s + replay "
                f"{replay_timings[prompt_id]:.3f}s.",
                flush=True,
            )

        update_component(
            current_component,
            "successful",
            completed_at=utc_now(),
            probe_count=len(PROBES),
            prompt_count=len(trajectories),
            permutations_per_probe=len(LOCAL_PERMUTATIONS),
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
        reference = trajectories[PROMPT_IDS[0]]
        for prompt_id in PROMPT_IDS[1:]:
            if not torch.equal(reference[0], trajectories[prompt_id][0]):
                raise RuntimeError(
                    f"State 00 differs between {PROMPT_IDS[0]} and {prompt_id}."
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
                    "probe_id",
                    "source_prompt_id",
                    "target_prompt_id",
                    "source_local_permutation",
                    "target_local_permutation",
                    "state_index",
                    "state_label",
                    "cosine_similarity",
                    "l2_distance",
                    "exact_equal",
                ]
            )
            pair_count = 0
            for probe_id, prompt_ids in PROBE_PROMPT_IDS.items():
                for source_id, target_id in itertools.combinations(prompt_ids, 2):
                    pair_count += 1
                    source = trajectories[source_id].float()
                    target = trajectories[target_id].float()
                    cosine = torch.nn.functional.cosine_similarity(
                        source, target, dim=1
                    )
                    l2 = torch.linalg.vector_norm(source - target, dim=1)
                    exact = torch.all(
                        trajectories[source_id] == trajectories[target_id], dim=1
                    )
                    for state_index in range(state_count):
                        cosine_value = float(cosine[state_index])
                        l2_value = float(l2[state_index])
                        writer.writerow(
                            [
                                probe_id,
                                source_id,
                                target_id,
                                PROMPT_SPECS[source_id]["local_permutation"],
                                PROMPT_SPECS[target_id]["local_permutation"],
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
                                "probe_id": probe_id,
                                "source": source_id,
                                "target": target_id,
                                "state_index": state_index,
                            }
                        if l2_value > maximum_l2:
                            maximum_l2 = l2_value
                            maximum_l2_identity = {
                                "probe_id": probe_id,
                                "source": source_id,
                                "target": target_id,
                                "state_index": state_index,
                            }

        write_json(OUTPUT_DIR / "prompt_records.json", prompt_records)
        validation = {
            "status": "successful",
            "probe_count": len(PROBES),
            "prompt_count": len(PROMPT_IDS),
            "permutations_per_probe": len(LOCAL_PERMUTATIONS),
            "prompt_ids": list(PROMPT_IDS),
            "probe_prompt_ids": {
                probe_id: list(prompt_ids)
                for probe_id, prompt_ids in PROBE_PROMPT_IDS.items()
            },
            "state_count": state_count,
            "hidden_width": hidden_width,
            "all_finite": True,
            "deterministic_replay_exact": True,
            "anchor_text": "\\n",
            "anchor_single_token": True,
            "anchor_token_id": anchor_token_id,
            "anchor_token": anchor_token,
            "anchor_matches_all_prompts": True,
            "state_00_exact_equal_all_prompts": True,
            "input_token_counts": {
                prompt_id: prompt_records[prompt_id]["input_token_count"]
                for prompt_id in PROMPT_IDS
            },
            "within_probe_pair_count": pair_count,
            "pair_state_metric_rows": pair_count * state_count,
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
            state_00_exact_equal_all_prompts=True,
            deterministic_replay_exact=True,
            all_finite=True,
            pair_state_metric_rows=pair_count * state_count,
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
