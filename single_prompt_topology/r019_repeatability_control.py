"""R019 order-versus-repeatability control for the OLMo 3 32B topology pipeline.

The run captures one balanced three-permutation batch in three sequential
forward passes, then compares variation within identical prompts against
variation caused by concept order. No token is generated or sampled.
"""

from __future__ import annotations

import argparse
import gc
import itertools
import json
import math
import shutil
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from accelerate import infer_auto_device_map, init_empty_weights
from safetensors import safe_open
from safetensors.torch import save_file
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

from topology_core import (
    TopologySettings,
    analyze_network,
    classify_token,
    compare_state_data,
    elbow_candidate,
    state_label,
    visible_token,
)
from topology_engine import (
    _model_identity,
    _prepare_prompt_batch,
    load_and_validate_config,
    memory_snapshot,
    sha256_file,
    write_json,
)


PIPELINE_DIR = Path(__file__).resolve().parent
SIDES = ("positive_head", "negative_tail")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def observation_specs(context: Any) -> list[dict[str, Any]]:
    repeats = int(context.config["capture"]["repeat_count"])
    records: list[dict[str, Any]] = []
    for repeat_index in range(1, repeats + 1):
        for prompt_index, prompt in enumerate(context.config["prompts"]):
            permutation = str(prompt["permutation"])
            records.append(
                {
                    "observation_index": len(records),
                    "observation_id": f"{permutation}_R{repeat_index}",
                    "prompt_index": prompt_index,
                    "prompt_id": str(prompt["prompt_id"]),
                    "permutation": permutation,
                    "repeat_index": repeat_index,
                    "concept_order": list(prompt["concept_order"]),
                    "raw_text": str(prompt["raw_text"]),
                }
            )
    return records


def pair_specs(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for source, target in itertools.combinations(observations, 2):
        same_permutation = source["permutation"] == target["permutation"]
        pairs.append(
            {
                "source_index": int(source["observation_index"]),
                "target_index": int(target["observation_index"]),
                "source_observation_id": source["observation_id"],
                "target_observation_id": target["observation_id"],
                "source_permutation": source["permutation"],
                "target_permutation": target["permutation"],
                "source_repeat_index": int(source["repeat_index"]),
                "target_repeat_index": int(target["repeat_index"]),
                "same_repeat_index": source["repeat_index"]
                == target["repeat_index"],
                "comparison_type": (
                    "within_prompt_repeat" if same_permutation else "between_order"
                ),
            }
        )
    return pairs


def initialize_run(context: Any) -> dict[str, Any]:
    if context.run_dir.exists():
        raise FileExistsError(
            f"Run directory already exists; refusing to overwrite: {context.run_dir}"
        )
    if not torch.cuda.is_available():
        raise RuntimeError("R019 requires CUDA.")
    if int(context.config["capture"].get("repeat_count", 0)) != 3:
        raise ValueError("R019 requires exactly three sequential captures.")
    if tuple(context.prompt_ids) != ("ABC", "BCA", "CAB"):
        raise ValueError("R019 requires the locked balanced cyclic permutations.")

    context.run_dir.mkdir(parents=True)
    shutil.copy2(context.config_path, context.run_dir / "run_config.json")
    shutil.copy2(context.plan_path, context.run_dir / "R019_PLAN.md")
    manifest = {
        "schema_version": 1,
        "run_id": context.config["run_id"],
        "run_number": context.config["run_number"],
        "run_status": "measurement_running",
        "started_at": utc_now(),
        "completed_at": None,
        "objective": context.config["objective"],
        "model": context.config["model"],
        "capture": context.config["capture"],
        "measurement": context.config["measurement"],
        "expected": context.config["expected"],
        "components": {},
        "failure": None,
        "result": None,
        "artifact_index": None,
        "interpretation_boundary": (
            "R019 measures repeat and order divergence. It does not reconstruct "
            "semantic parents or interpret their meaning."
        ),
    }
    write_json(context.run_dir / "manifest.json", manifest)
    return manifest


def update_component(
    context: Any,
    component: str,
    started_at: str,
    started_perf: float,
    **details: object,
) -> None:
    manifest_path = context.run_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["components"][component] = {
        "status": "successful",
        "started_at": started_at,
        "completed_at": utc_now(),
        "elapsed_seconds": time.perf_counter() - started_perf,
        **details,
    }
    write_json(manifest_path, manifest)


def fail_run(context: Any, component: str, error: BaseException) -> None:
    manifest_path = context.run_dir / "manifest.json"
    if not manifest_path.exists():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["run_status"] = "measurement_failed"
    manifest["completed_at"] = utc_now()
    manifest["failure"] = {
        "component": component,
        "error_type": type(error).__name__,
        "message": str(error),
        "traceback": traceback.format_exc(),
    }
    write_json(manifest_path, manifest)


def capture_once(
    model: Any,
    encoded: dict[str, torch.Tensor],
    capture_indices: torch.Tensor,
    state_count: int,
) -> tuple[torch.Tensor, torch.Tensor]:
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
            f"Expected {state_count} hidden states; found "
            f"{0 if states is None else len(states)}."
        )
    state_rows = torch.arange(capture_indices.numel())
    captured: list[torch.Tensor] = []
    for state in states:
        rows = state_rows.to(state.device)
        indices = capture_indices.to(state.device)
        captured.append(
            state[rows, indices].detach().to(device="cpu", dtype=torch.bfloat16)
        )
    logits = output.logits
    logit_rows = state_rows.to(logits.device)
    logit_indices = capture_indices.to(logits.device)
    final_logits = (
        logits[logit_rows, logit_indices]
        .detach()
        .to(device="cpu", dtype=torch.bfloat16)
        .contiguous()
    )
    trajectories = torch.stack(captured, dim=1).contiguous()
    del output, states, logits, device_inputs, captured
    return trajectories, final_logits


def hidden_pair_metrics(
    flat_hidden: torch.Tensor,
    pairs: list[dict[str, Any]],
    settings: TopologySettings,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    values = flat_hidden.float()
    for pair in pairs:
        source = values[pair["source_index"]]
        target = values[pair["target_index"]]
        cosine = F.cosine_similarity(source, target, dim=1)
        difference = source - target
        l2 = torch.linalg.vector_norm(difference, dim=1)
        maximum = difference.abs().amax(dim=1)
        exact = torch.all(
            flat_hidden[pair["source_index"]]
            == flat_hidden[pair["target_index"]],
            dim=1,
        )
        for state_index in range(settings.state_count):
            is_exact = bool(exact[state_index])
            rows.append(
                {
                    **{key: value for key, value in pair.items() if not key.endswith("_index") or key in {"source_repeat_index", "target_repeat_index"}},
                    "state_index": state_index,
                    "state_label": state_label(state_index, settings),
                    "cosine_similarity": 1.0 if is_exact else float(cosine[state_index]),
                    "cosine_distance": 0.0
                    if is_exact
                    else max(0.0, 1.0 - float(cosine[state_index])),
                    "l2_distance": 0.0 if is_exact else float(l2[state_index]),
                    "maximum_absolute_difference": 0.0
                    if is_exact
                    else float(maximum[state_index]),
                    "exact_equal": is_exact,
                }
            )
    return pd.DataFrame(rows)


def jensen_shannon_from_logits(source: torch.Tensor, target: torch.Tensor) -> float:
    source_log = F.log_softmax(source.float(), dim=0)
    target_log = F.log_softmax(target.float(), dim=0)
    mixture_log = torch.logaddexp(source_log, target_log) - math.log(2.0)
    source_probability = source_log.exp()
    target_probability = target_log.exp()
    value = 0.5 * (
        torch.sum(source_probability * (source_log - mixture_log))
        + torch.sum(target_probability * (target_log - mixture_log))
    )
    return float(value)


def set_jaccard(source: set[int], target: set[int]) -> float:
    union = source | target
    return len(source & target) / len(union) if union else 1.0


def logit_pair_metrics(
    flat_logits: torch.Tensor,
    pairs: list[dict[str, Any]],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    values = flat_logits.float()
    for pair in pairs:
        source = values[pair["source_index"]]
        target = values[pair["target_index"]]
        difference = source - target
        is_exact = bool(
            torch.equal(
                flat_logits[pair["source_index"]],
                flat_logits[pair["target_index"]],
            )
        )
        source_top = set(map(int, torch.topk(source, k=100).indices.tolist()))
        target_top = set(map(int, torch.topk(target, k=100).indices.tolist()))
        rows.append(
            {
                **{key: value for key, value in pair.items() if key not in {"source_index", "target_index"}},
                "cosine_similarity": 1.0 if is_exact else float(
                    F.cosine_similarity(source[None, :], target[None, :], dim=1)[0]
                ),
                "l2_distance": 0.0
                if is_exact
                else float(torch.linalg.vector_norm(difference)),
                "maximum_absolute_difference": 0.0
                if is_exact
                else float(difference.abs().max()),
                "exact_equal": is_exact,
                "jensen_shannon_divergence": 0.0
                if is_exact
                else jensen_shannon_from_logits(source, target),
                "top_100_token_jaccard": 1.0
                if is_exact
                else set_jaccard(source_top, target_top),
            }
        )
    return pd.DataFrame(rows)


def capture_model(
    context: Any,
    observations: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
) -> tuple[torch.Tensor, torch.Tensor, int]:
    component_started_at = utc_now()
    component_started = time.perf_counter()
    identity = _model_identity(context)
    tokenizer, encoded, capture_indices, prompt_records, anchor_token_id = (
        _prepare_prompt_batch(context)
    )
    write_json(context.run_dir / "prompt_records.json", prompt_records)
    write_json(
        context.run_dir / "observation_records.json",
        {record["observation_id"]: record for record in observations},
    )

    model_config = AutoConfig.from_pretrained(context.snapshot_dir, local_files_only=True)
    with init_empty_weights():
        empty_model = AutoModelForCausalLM.from_config(
            model_config, dtype=torch.bfloat16
        )
    no_split = list(
        getattr(empty_model, "_no_split_modules", None) or ["Olmo3DecoderLayer"]
    )
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

    repeat_states: list[torch.Tensor] = []
    repeat_logits: list[torch.Tensor] = []
    repeat_seconds: list[float] = []
    torch.cuda.reset_peak_memory_stats()
    for repeat_index in range(1, int(context.config["capture"]["repeat_count"]) + 1):
        started = time.perf_counter()
        states, logits = capture_once(
            model, encoded, capture_indices, context.settings.state_count
        )
        torch.cuda.synchronize()
        repeat_states.append(states)
        repeat_logits.append(logits)
        repeat_seconds.append(time.perf_counter() - started)
        print(
            f"R019 captured repeat {repeat_index}/3 in {repeat_seconds[-1]:.2f}s.",
            flush=True,
        )

    hidden = torch.stack(repeat_states, dim=0).contiguous()
    logits = torch.stack(repeat_logits, dim=0).contiguous()
    expected_hidden = (
        3,
        len(context.prompt_ids),
        context.settings.state_count,
        int(context.config["model"]["hidden_width"]),
    )
    if tuple(hidden.shape) != expected_hidden:
        raise RuntimeError(f"Unexpected repeated hidden-state shape: {tuple(hidden.shape)}")
    if not torch.isfinite(hidden.float()).all() or not torch.isfinite(logits.float()).all():
        raise RuntimeError("Captured hidden states or logits contain non-finite values.")

    flat_hidden = hidden.reshape(
        -1, context.settings.state_count, int(context.config["model"]["hidden_width"])
    )
    flat_logits = logits.reshape(-1, logits.shape[-1])
    hidden_metrics = hidden_pair_metrics(flat_hidden, pairs, context.settings)
    logit_metrics = logit_pair_metrics(flat_logits, pairs)
    hidden_metrics.to_csv(
        context.run_dir / "pairwise_hidden_state_metrics.csv", index=False
    )
    logit_metrics.to_csv(
        context.run_dir / "pairwise_next_token_distribution_metrics.csv", index=False
    )
    save_file(
        {
            "anchor_hidden_state_repeats": hidden,
            "final_next_token_logits": logits,
        },
        str(context.run_dir / "repeat_capture.safetensors"),
        metadata={
            "model_id": context.config["model"]["id"],
            "revision": context.config["model"]["revision"],
            "prompt_ids": ",".join(context.prompt_ids),
            "repeat_count": "3",
            "anchor_token_id": str(anchor_token_id),
        },
    )
    within_hidden = hidden_metrics.loc[
        hidden_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    within_logits = logit_metrics.loc[
        logit_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    validation = {
        "status": "successful",
        "identity": identity,
        "repeat_count": 3,
        "prompt_count": len(context.prompt_ids),
        "observation_count": len(observations),
        "hidden_shape": list(hidden.shape),
        "logit_shape": list(logits.shape),
        "all_finite": True,
        "anchor_token_id": anchor_token_id,
        "within_repeat_hidden_exact_all_states": bool(
            within_hidden["exact_equal"].all()
        ),
        "within_repeat_logits_exact": bool(within_logits["exact_equal"].all()),
        "repeat_seconds": repeat_seconds,
        "peak_gpu_allocated_bytes": int(torch.cuda.max_memory_allocated()),
    }
    write_json(context.run_dir / "capture_validation.json", validation)
    update_component(
        context,
        "sequential_capture",
        component_started_at,
        component_started,
        **validation,
        memory_after_capture=memory_snapshot(context.snapshot_dir),
    )

    del model, tokenizer, encoded, capture_indices, repeat_states, repeat_logits
    gc.collect()
    torch.cuda.empty_cache()
    torch.cuda.synchronize()
    return hidden, logits, anchor_token_id


def score_pair_metrics(
    scores: torch.Tensor,
    pairs: list[dict[str, Any]],
    settings: TopologySettings,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for pair in pairs:
        source = scores[pair["source_index"]]
        target = scores[pair["target_index"]]
        cosine = F.cosine_similarity(source, target, dim=1)
        difference = source - target
        rmse = torch.sqrt(torch.mean(difference.square(), dim=1))
        maximum = difference.abs().amax(dim=1)
        exact = torch.all(source == target, dim=1)
        for state_index in range(settings.state_count):
            is_exact = bool(exact[state_index])
            rows.append(
                {
                    **{key: value for key, value in pair.items() if key not in {"source_index", "target_index"}},
                    "state_index": state_index,
                    "state_label": state_label(state_index, settings),
                    "cosine_similarity": 1.0 if is_exact else float(cosine[state_index]),
                    "cosine_distance": 0.0
                    if is_exact
                    else max(0.0, 1.0 - float(cosine[state_index])),
                    "rmse": 0.0 if is_exact else float(rmse[state_index]),
                    "maximum_absolute_difference": 0.0
                    if is_exact
                    else float(maximum[state_index]),
                    "exact_equal": is_exact,
                }
            )
    return pd.DataFrame(rows)


def project_and_select(
    context: Any,
    hidden: torch.Tensor,
    observations: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
    anchor_token_id: int,
) -> tuple[
    torch.Tensor,
    torch.Tensor,
    dict[tuple[int, int, str], np.ndarray],
    list[str],
    list[str],
    list[str],
    int,
]:
    started_at = utc_now()
    started = time.perf_counter()
    tokenizer = AutoTokenizer.from_pretrained(context.snapshot_dir, local_files_only=True)
    vocabulary_size = len(tokenizer)
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

    index = json.loads(
        (context.snapshot_dir / "model.safetensors.index.json").read_text(
            encoding="utf-8"
        )
    )
    embedding_key = context.config["model"]["embedding_key"]
    shard_name = index["weight_map"].get(embedding_key)
    if not shard_name:
        raise KeyError(f"Missing embedding tensor: {embedding_key}")
    with safe_open(
        str(context.snapshot_dir / shard_name), framework="pt", device="cpu"
    ) as handle:
        embeddings = handle.get_tensor(embedding_key)
    embeddings = embeddings[:vocabulary_size]
    normalized_embeddings = F.normalize(
        embeddings.to("cuda", dtype=torch.float32), p=2, dim=1
    )
    flat_hidden = hidden.reshape(
        len(observations),
        context.settings.state_count,
        int(context.config["model"]["hidden_width"]),
    )
    normalized_states = F.normalize(
        flat_hidden.to("cuda", dtype=torch.float32), p=2, dim=2
    )
    with torch.inference_mode():
        scores = torch.einsum(
            "osd,vd->osv", normalized_states, normalized_embeddings
        ).cpu().contiguous()
    if not torch.isfinite(scores).all():
        raise RuntimeError("Vocabulary projection contains non-finite values.")
    save_file(
        {"cosine_score_repeats": scores},
        str(context.run_dir / "vocabulary_score_repeats.safetensors"),
        metadata={
            "observation_ids": ",".join(
                str(record["observation_id"]) for record in observations
            ),
            "state_count": str(context.settings.state_count),
            "vocabulary_size": str(vocabulary_size),
            "excluded_capture_token_id": str(anchor_token_id),
        },
    )
    score_metrics = score_pair_metrics(scores, pairs, context.settings)
    score_metrics.to_csv(
        context.run_dir / "pairwise_vocabulary_score_metrics.csv", index=False
    )

    eligible_ids = np.arange(vocabulary_size, dtype=np.int64)
    eligible_ids = eligible_ids[eligible_ids != anchor_token_id]
    score_values = scores.numpy()
    memberships: dict[tuple[int, int, str], np.ndarray] = {}
    cutoff_rows: list[dict[str, Any]] = []
    for observation in observations:
        observation_index = int(observation["observation_index"])
        for state_index in range(context.settings.state_count):
            state_scores = score_values[observation_index, state_index]
            descending = eligible_ids[
                np.argsort(-state_scores[eligible_ids], kind="stable")
            ]
            ascending = eligible_ids[
                np.argsort(state_scores[eligible_ids], kind="stable")
            ]
            positive = elbow_candidate(state_scores[descending])
            negative_inverted = elbow_candidate(-state_scores[ascending])
            positive_count = int(positive["cutoff_rank"])
            negative_count = int(negative_inverted["cutoff_rank"])
            positive_ids = descending[:positive_count].copy()
            negative_ids = ascending[:negative_count].copy()
            if np.intersect1d(positive_ids, negative_ids).size:
                raise RuntimeError(
                    f"Cutoff populations overlap at {observation['observation_id']} "
                    f"State {state_index}."
                )
            memberships[(observation_index, state_index, "positive_head")] = (
                positive_ids
            )
            memberships[(observation_index, state_index, "negative_tail")] = (
                negative_ids
            )
            cutoff_rows.append(
                {
                    "observation_id": observation["observation_id"],
                    "permutation": observation["permutation"],
                    "repeat_index": observation["repeat_index"],
                    "state_index": state_index,
                    "state_label": state_label(state_index, context.settings),
                    "eligible_vocabulary_size": len(eligible_ids),
                    "excluded_capture_token_id": anchor_token_id,
                    "upper_cutoff_rank": positive_count,
                    "upper_cutoff_score": positive["cutoff_score"],
                    "upper_elbow_strength": positive["elbow_strength"],
                    "lower_cutoff_rank": negative_count,
                    "lower_cutoff_score": -float(negative_inverted["cutoff_score"]),
                    "lower_elbow_strength": negative_inverted["elbow_strength"],
                    "positive_head_count": positive_count,
                    "negative_tail_count": negative_count,
                    "central_body_count": len(eligible_ids)
                    - positive_count
                    - negative_count,
                }
            )
    cutoffs = pd.DataFrame(cutoff_rows)
    cutoffs.to_csv(context.run_dir / "cutoffs.csv", index=False)

    within_scores = score_metrics.loc[
        score_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    update_component(
        context,
        "projection_and_cutoffs",
        started_at,
        started,
        score_shape=list(scores.shape),
        cutoff_rows=len(cutoffs),
        membership_population_count=len(memberships),
        within_repeat_scores_exact_all_states=bool(
            within_scores["exact_equal"].all()
        ),
        embedding_shard=shard_name,
    )
    del normalized_states, flat_hidden, embeddings, tokenizer
    gc.collect()
    return (
        normalized_embeddings,
        scores,
        memberships,
        raw_tokens,
        decoded_tokens,
        token_classes,
        vocabulary_size,
    )


def construct_repeat_networks(
    context: Any,
    observations: list[dict[str, Any]],
    pairs: list[dict[str, Any]],
    normalized_embeddings: torch.Tensor,
    scores: torch.Tensor,
    memberships: dict[tuple[int, int, str], np.ndarray],
    raw_tokens: list[str],
    decoded_tokens: list[str],
    token_classes: list[str],
    vocabulary_size: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    started_at = utc_now()
    started = time.perf_counter()
    score_values = scores.numpy()
    network_rows: list[dict[str, Any]] = []
    pair_rows: list[dict[str, Any]] = []
    completed = 0
    expected_networks = int(context.config["expected"]["repeat_network_count"])

    for state_index in range(context.settings.state_count):
        current: dict[tuple[int, str], dict[str, Any]] = {}
        for observation in observations:
            observation_index = int(observation["observation_index"])
            for side_index, side in enumerate(SIDES):
                token_ids = memberships[(observation_index, state_index, side)]
                state_scores = score_values[observation_index, state_index]
                frame = pd.DataFrame(
                    {
                        "observation_id": observation["observation_id"],
                        "state_index": state_index,
                        "state_label": state_label(state_index, context.settings),
                        "side": side,
                        "token_id": token_ids,
                        "raw_token": [raw_tokens[token_id] for token_id in token_ids],
                        "decoded_token": [
                            decoded_tokens[token_id] for token_id in token_ids
                        ],
                        "display_token": [
                            visible_token(decoded_tokens[token_id])
                            for token_id in token_ids
                        ],
                        "token_class": [
                            token_classes[token_id] for token_id in token_ids
                        ],
                        "cosine_score": state_scores[token_ids],
                        "rank_from_extreme": np.arange(
                            1, len(token_ids) + 1, dtype=np.int32
                        ),
                    }
                )
                (
                    metric,
                    _node_frame,
                    _edge_frame,
                    _communities,
                    _community_edges,
                    state_data,
                    _compact,
                ) = analyze_network(
                    str(observation["observation_id"]),
                    observation_index,
                    state_index,
                    side,
                    side_index,
                    frame,
                    normalized_embeddings,
                    vocabulary_size,
                    context.settings,
                )
                metric.update(
                    {
                        "permutation": observation["permutation"],
                        "repeat_index": observation["repeat_index"],
                    }
                )
                network_rows.append(metric)
                current[(observation_index, side)] = state_data
                completed += 1
                if completed % 15 == 0 or completed == expected_networks:
                    print(
                        f"R019 network {completed}/{expected_networks}: "
                        f"{observation['observation_id']} State {state_index:02d} "
                        f"{side}.",
                        flush=True,
                    )
                del (
                    frame,
                    _node_frame,
                    _edge_frame,
                    _communities,
                    _community_edges,
                    _compact,
                )

        for pair in pairs:
            for side in SIDES:
                comparison = compare_state_data(
                    current[(pair["source_index"], side)],
                    current[(pair["target_index"], side)],
                )
                pair_rows.append(
                    {
                        **{
                            key: value
                            for key, value in pair.items()
                            if key not in {"source_index", "target_index"}
                        },
                        "state_index": state_index,
                        "state_label": state_label(state_index, context.settings),
                        "side": side,
                        **comparison,
                    }
                )

    network_index = pd.DataFrame(network_rows).sort_values(
        ["state_index", "prompt_id", "side"], kind="stable"
    )
    topology_pairs = pd.DataFrame(pair_rows).sort_values(
        ["state_index", "side", "source_observation_id", "target_observation_id"],
        kind="stable",
    )
    network_index.to_csv(context.run_dir / "network_index.csv", index=False)
    topology_pairs.to_csv(
        context.run_dir / "pairwise_topology_metrics.csv", index=False
    )
    update_component(
        context,
        "repeat_networks_and_comparisons",
        started_at,
        started,
        network_count=len(network_index),
        topology_pair_rows=len(topology_pairs),
    )
    return network_index, topology_pairs


def summarize_divergence(
    context: Any,
    hidden_metrics: pd.DataFrame,
    score_metrics: pd.DataFrame,
    logit_metrics: pd.DataFrame,
    topology_metrics: pd.DataFrame,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for state_index in range(context.settings.state_count):
        hidden_state = hidden_metrics.loc[hidden_metrics["state_index"] == state_index]
        score_state = score_metrics.loc[score_metrics["state_index"] == state_index]
        hidden_within = hidden_state.loc[
            hidden_state["comparison_type"] == "within_prompt_repeat"
        ]
        hidden_between = hidden_state.loc[
            hidden_state["comparison_type"] == "between_order"
        ]
        score_within = score_state.loc[
            score_state["comparison_type"] == "within_prompt_repeat"
        ]
        score_between = score_state.loc[
            score_state["comparison_type"] == "between_order"
        ]
        row: dict[str, Any] = {
            "state_index": state_index,
            "state_label": state_label(state_index, context.settings),
            "within_hidden_max_cosine_distance": float(
                hidden_within["cosine_distance"].max()
            ),
            "between_order_mean_hidden_cosine_distance": float(
                hidden_between["cosine_distance"].mean()
            ),
            "between_order_max_hidden_cosine_distance": float(
                hidden_between["cosine_distance"].max()
            ),
            "within_score_max_rmse": float(score_within["rmse"].max()),
            "between_order_mean_score_rmse": float(score_between["rmse"].mean()),
            "between_order_max_score_rmse": float(score_between["rmse"].max()),
        }
        for side in SIDES:
            topology_state = topology_metrics.loc[
                (topology_metrics["state_index"] == state_index)
                & (topology_metrics["side"] == side)
            ]
            within = topology_state.loc[
                topology_state["comparison_type"] == "within_prompt_repeat"
            ]
            between = topology_state.loc[
                topology_state["comparison_type"] == "between_order"
            ]
            prefix = "positive" if side == "positive_head" else "negative"
            row[f"within_{prefix}_minimum_membership_jaccard"] = float(
                within["membership_jaccard"].min()
            )
            row[f"between_order_{prefix}_mean_membership_jaccard"] = float(
                between["membership_jaccard"].mean()
            )
            row[f"between_order_{prefix}_minimum_membership_jaccard"] = float(
                between["membership_jaccard"].min()
            )
            row[f"within_{prefix}_minimum_edge_jaccard"] = float(
                within["edge_jaccard"].min()
            )
            row[f"between_order_{prefix}_mean_edge_jaccard"] = float(
                between["edge_jaccard"].mean()
            )
            row[f"between_order_{prefix}_minimum_edge_jaccard"] = float(
                between["edge_jaccard"].min()
            )
            row[f"within_{prefix}_minimum_community_ari"] = float(
                within["community_adjusted_rand"].min()
            )
            row[f"between_order_{prefix}_mean_community_ari"] = float(
                between["community_adjusted_rand"].mean()
            )
        rows.append(row)
    by_state = pd.DataFrame(rows)
    by_state.to_csv(context.run_dir / "divergence_by_state.csv", index=False)

    within_hidden = hidden_metrics.loc[
        hidden_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    between_hidden = hidden_metrics.loc[
        (hidden_metrics["comparison_type"] == "between_order")
        & (hidden_metrics["state_index"] > 0)
    ]
    within_scores = score_metrics.loc[
        score_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    between_scores = score_metrics.loc[
        (score_metrics["comparison_type"] == "between_order")
        & (score_metrics["state_index"] > 0)
    ]
    within_logits = logit_metrics.loc[
        logit_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    between_logits = logit_metrics.loc[
        logit_metrics["comparison_type"] == "between_order"
    ]
    within_topology = topology_metrics.loc[
        topology_metrics["comparison_type"] == "within_prompt_repeat"
    ]
    between_topology = topology_metrics.loc[
        (topology_metrics["comparison_type"] == "between_order")
        & (topology_metrics["state_index"] > 0)
    ]

    worst_hidden = between_hidden.loc[between_hidden["cosine_similarity"].idxmin()]
    worst_score = between_scores.loc[between_scores["rmse"].idxmax()]
    worst_membership = between_topology.loc[
        between_topology["membership_jaccard"].idxmin()
    ]
    worst_edge = between_topology.loc[between_topology["edge_jaccard"].idxmin()]
    worst_logits = between_logits.loc[
        between_logits["jensen_shannon_divergence"].idxmax()
    ]

    repeat_hidden_exact = bool(within_hidden["exact_equal"].all())
    repeat_scores_exact = bool(within_scores["exact_equal"].all())
    repeat_logits_exact = bool(within_logits["exact_equal"].all())
    repeat_topology_exact = bool(
        np.allclose(within_topology["membership_jaccard"], 1.0)
        and np.allclose(within_topology["edge_jaccard"], 1.0)
        and np.allclose(within_topology["community_adjusted_rand"], 1.0)
    )
    order_effect_detected = bool(
        (~between_hidden["exact_equal"]).any()
        and (between_logits["jensen_shannon_divergence"] > 0).any()
        and (between_topology["membership_jaccard"] < 1).any()
    )
    repeat_exact = (
        repeat_hidden_exact
        and repeat_scores_exact
        and repeat_logits_exact
        and repeat_topology_exact
    )
    if repeat_exact and order_effect_detected:
        conclusion = "deterministic_order_effect_confirmed"
    elif order_effect_detected:
        conclusion = "order_effect_detected_above_nonzero_repeat_variation"
    else:
        conclusion = "order_effect_not_resolved_from_repeat_variation"

    summary = {
        "conclusion": conclusion,
        "repeat_noise_floor": {
            "hidden_exact_all_states": repeat_hidden_exact,
            "vocabulary_scores_exact_all_states": repeat_scores_exact,
            "next_token_logits_exact": repeat_logits_exact,
            "topology_exact_all_states_and_sides": repeat_topology_exact,
            "maximum_hidden_cosine_distance": float(
                within_hidden["cosine_distance"].max()
            ),
            "maximum_score_rmse": float(within_scores["rmse"].max()),
            "maximum_next_token_js_divergence": float(
                within_logits["jensen_shannon_divergence"].max()
            ),
            "minimum_membership_jaccard": float(
                within_topology["membership_jaccard"].min()
            ),
            "minimum_edge_jaccard": float(within_topology["edge_jaccard"].min()),
            "minimum_community_ari": float(
                within_topology["community_adjusted_rand"].min()
            ),
        },
        "order_effect": {
            "detected": order_effect_detected,
            "minimum_hidden_cosine_similarity": float(
                worst_hidden["cosine_similarity"]
            ),
            "maximum_score_rmse": float(worst_score["rmse"]),
            "maximum_next_token_js_divergence": float(
                worst_logits["jensen_shannon_divergence"]
            ),
            "minimum_membership_jaccard": float(
                worst_membership["membership_jaccard"]
            ),
            "minimum_edge_jaccard": float(worst_edge["edge_jaccard"]),
            "worst_hidden_case": {
                "source": worst_hidden["source_observation_id"],
                "target": worst_hidden["target_observation_id"],
                "state_index": int(worst_hidden["state_index"]),
                "state_label": worst_hidden["state_label"],
            },
            "worst_score_case": {
                "source": worst_score["source_observation_id"],
                "target": worst_score["target_observation_id"],
                "state_index": int(worst_score["state_index"]),
                "state_label": worst_score["state_label"],
            },
            "worst_membership_case": {
                "source": worst_membership["source_observation_id"],
                "target": worst_membership["target_observation_id"],
                "state_index": int(worst_membership["state_index"]),
                "state_label": worst_membership["state_label"],
                "side": worst_membership["side"],
            },
            "worst_edge_case": {
                "source": worst_edge["source_observation_id"],
                "target": worst_edge["target_observation_id"],
                "state_index": int(worst_edge["state_index"]),
                "state_label": worst_edge["state_label"],
                "side": worst_edge["side"],
            },
            "worst_next_token_case": {
                "source": worst_logits["source_observation_id"],
                "target": worst_logits["target_observation_id"],
            },
        },
        "interpretation": (
            "The measured order effect is compared against repeated deterministic "
            "forward passes. No generated token or sampled trajectory contributed "
            "to any comparison."
        ),
    }
    write_json(context.run_dir / "R019_RESULT.json", summary)
    return by_state, summary


def validate_counts(
    context: Any,
    hidden_metrics: pd.DataFrame,
    score_metrics: pd.DataFrame,
    logit_metrics: pd.DataFrame,
    network_index: pd.DataFrame,
    topology_metrics: pd.DataFrame,
) -> dict[str, Any]:
    expected = context.config["expected"]
    checks = {
        "hidden_pair_rows": len(hidden_metrics)
        == int(expected["repeat_pair_state_rows"]),
        "score_pair_rows": len(score_metrics)
        == int(expected["repeat_pair_state_rows"]),
        "logit_pair_rows": len(logit_metrics) == math.comb(9, 2),
        "network_rows": len(network_index)
        == int(expected["repeat_network_count"]),
        "topology_pair_rows": len(topology_metrics)
        == int(expected["repeat_topology_pair_rows"]),
        "within_hidden_rows": int(
            (hidden_metrics["comparison_type"] == "within_prompt_repeat").sum()
        )
        == int(expected["within_repeat_pair_state_rows"]),
        "between_hidden_rows": int(
            (hidden_metrics["comparison_type"] == "between_order").sum()
        )
        == int(expected["between_order_pair_state_rows"]),
        "within_topology_rows": int(
            (topology_metrics["comparison_type"] == "within_prompt_repeat").sum()
        )
        == int(expected["within_repeat_topology_rows"]),
        "between_topology_rows": int(
            (topology_metrics["comparison_type"] == "between_order").sum()
        )
        == int(expected["between_order_topology_rows"]),
    }
    if not all(checks.values()):
        raise RuntimeError(f"R019 completeness checks failed: {checks}")
    return checks


def render_reports(
    context: Any,
    summary: dict[str, Any],
    checks: dict[str, Any],
) -> None:
    repeat = summary["repeat_noise_floor"]
    order = summary["order_effect"]
    measurement_report = f"""# R019 order-versus-repeatability measurement report

## Result

`{summary['conclusion']}`

R019 executed three sequential forward passes for each of the balanced cyclic
permutations `ABC`, `BCA` and `CAB`. No response was generated and no token was
sampled.

## Measured repeat noise floor

- Hidden states exact across identical repeats at all 65 states: `{repeat['hidden_exact_all_states']}`
- Full-vocabulary score vectors exact across repeats: `{repeat['vocabulary_scores_exact_all_states']}`
- Final next-token logits exact across repeats: `{repeat['next_token_logits_exact']}`
- Cutoff membership, 10-NN edges and seeded Louvain partitions exact across repeats: `{repeat['topology_exact_all_states_and_sides']}`
- Maximum within-repeat hidden cosine distance: `{repeat['maximum_hidden_cosine_distance']:.12g}`
- Maximum within-repeat vocabulary-score RMSE: `{repeat['maximum_score_rmse']:.12g}`
- Maximum within-repeat next-token Jensen-Shannon divergence: `{repeat['maximum_next_token_js_divergence']:.12g}`
- Minimum within-repeat membership Jaccard: `{repeat['minimum_membership_jaccard']:.12g}`
- Minimum within-repeat edge Jaccard: `{repeat['minimum_edge_jaccard']:.12g}`
- Minimum within-repeat community ARI: `{repeat['minimum_community_ari']:.12g}`

## Measured order divergence

- Order effect detected after State 00: `{order['detected']}`
- Minimum between-order hidden cosine similarity: `{order['minimum_hidden_cosine_similarity']:.9f}`
- Maximum between-order vocabulary-score RMSE: `{order['maximum_score_rmse']:.9f}`
- Maximum between-order next-token Jensen-Shannon divergence: `{order['maximum_next_token_js_divergence']:.9f}`
- Minimum between-order cutoff-membership Jaccard: `{order['minimum_membership_jaccard']:.9f}`
- Minimum between-order 10-NN edge Jaccard: `{order['minimum_edge_jaccard']:.9f}`

The strongest hidden-state divergence occurred for
`{order['worst_hidden_case']['source']}` versus
`{order['worst_hidden_case']['target']}` at State
`{order['worst_hidden_case']['state_index']:02d}`
(`{order['worst_hidden_case']['state_label']}`).

## Conclusion boundary

This result determines whether R018's permutation differences exceed the
measured repeat noise floor. It does not identify semantic parents or explain
what the order-conditioned structures mean.

The final token seed is irrelevant to this experiment because there was no
sampling. The fixed random seed applies only to deterministic graph-community
bookkeeping.
"""
    (context.run_dir / "R019_MEASUREMENT_REPORT.md").write_text(
        measurement_report, encoding="utf-8"
    )
    verification = "# R019 completeness verification\n\n"
    verification += "All required coverage checks passed.\n\n"
    for name, passed in checks.items():
        verification += f"- `{name}`: `{passed}`\n"
    verification += "\nThe run is measurement-complete and requires no semantic analysis.\n"
    (context.run_dir / "R019_COMPLETENESS_VERIFICATION.md").write_text(
        verification, encoding="utf-8"
    )


def build_artifact_index(context: Any) -> list[dict[str, Any]]:
    artifacts: list[dict[str, Any]] = []
    for path in sorted(context.run_dir.iterdir(), key=lambda item: item.name):
        if not path.is_file() or path.name in {"manifest.json", "artifact_index.json"}:
            continue
        artifacts.append(
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    write_json(context.run_dir / "artifact_index.json", {"artifacts": artifacts})
    return artifacts


def refresh_derived_outputs(context: Any) -> dict[str, Any]:
    """Normalize exact-pair diagnostic roundoff and rebuild derived summaries."""
    started_at = utc_now()
    started = time.perf_counter()
    hidden_metrics = pd.read_csv(
        context.run_dir / "pairwise_hidden_state_metrics.csv"
    )
    score_metrics = pd.read_csv(
        context.run_dir / "pairwise_vocabulary_score_metrics.csv"
    )
    logit_metrics = pd.read_csv(
        context.run_dir / "pairwise_next_token_distribution_metrics.csv"
    )
    network_index = pd.read_csv(context.run_dir / "network_index.csv")
    topology_metrics = pd.read_csv(
        context.run_dir / "pairwise_topology_metrics.csv"
    )

    for frame, zero_columns in (
        (
            hidden_metrics,
            ("cosine_distance", "l2_distance", "maximum_absolute_difference"),
        ),
        (
            score_metrics,
            ("cosine_distance", "rmse", "maximum_absolute_difference"),
        ),
        (
            logit_metrics,
            (
                "l2_distance",
                "maximum_absolute_difference",
                "jensen_shannon_divergence",
            ),
        ),
    ):
        exact = frame["exact_equal"].astype(bool)
        frame.loc[exact, "cosine_similarity"] = 1.0
        for column in zero_columns:
            frame.loc[exact, column] = 0.0
    exact_logits = logit_metrics["exact_equal"].astype(bool)
    logit_metrics.loc[exact_logits, "top_100_token_jaccard"] = 1.0

    hidden_metrics.to_csv(
        context.run_dir / "pairwise_hidden_state_metrics.csv", index=False
    )
    score_metrics.to_csv(
        context.run_dir / "pairwise_vocabulary_score_metrics.csv", index=False
    )
    logit_metrics.to_csv(
        context.run_dir / "pairwise_next_token_distribution_metrics.csv", index=False
    )
    _by_state, summary = summarize_divergence(
        context,
        hidden_metrics,
        score_metrics,
        logit_metrics,
        topology_metrics,
    )
    checks = validate_counts(
        context,
        hidden_metrics,
        score_metrics,
        logit_metrics,
        network_index,
        topology_metrics,
    )
    render_reports(context, summary, checks)
    artifacts = build_artifact_index(context)
    manifest_path = context.run_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["result"] = summary
    manifest["components"]["derived_metric_normalization"] = {
        "status": "successful",
        "started_at": started_at,
        "completed_at": utc_now(),
        "elapsed_seconds": time.perf_counter() - started,
        "reason": (
            "Exact-equal tensor pairs are assigned mathematically exact zero "
            "distance/divergence instead of retaining cosine or softmax roundoff."
        ),
        "artifact_count": len(artifacts),
    }
    write_json(manifest_path, manifest)
    return summary


def measure(context: Any) -> None:
    initialize_run(context)
    component = "initialization"
    try:
        observations = observation_specs(context)
        pairs = pair_specs(observations)
        component = "sequential_capture"
        hidden, logits, anchor_token_id = capture_model(
            context, observations, pairs
        )
        component = "projection_and_cutoffs"
        (
            normalized_embeddings,
            scores,
            memberships,
            raw_tokens,
            decoded_tokens,
            token_classes,
            vocabulary_size,
        ) = project_and_select(
            context,
            hidden,
            observations,
            pairs,
            anchor_token_id,
        )
        component = "repeat_networks_and_comparisons"
        network_index, topology_metrics = construct_repeat_networks(
            context,
            observations,
            pairs,
            normalized_embeddings,
            scores,
            memberships,
            raw_tokens,
            decoded_tokens,
            token_classes,
            vocabulary_size,
        )
        component = "summarization"
        hidden_metrics = pd.read_csv(
            context.run_dir / "pairwise_hidden_state_metrics.csv"
        )
        score_metrics = pd.read_csv(
            context.run_dir / "pairwise_vocabulary_score_metrics.csv"
        )
        logit_metrics = pd.read_csv(
            context.run_dir / "pairwise_next_token_distribution_metrics.csv"
        )
        summary_started_at = utc_now()
        summary_started = time.perf_counter()
        _by_state, summary = summarize_divergence(
            context,
            hidden_metrics,
            score_metrics,
            logit_metrics,
            topology_metrics,
        )
        checks = validate_counts(
            context,
            hidden_metrics,
            score_metrics,
            logit_metrics,
            network_index,
            topology_metrics,
        )
        render_reports(context, summary, checks)
        update_component(
            context,
            "summarization_and_validation",
            summary_started_at,
            summary_started,
            conclusion=summary["conclusion"],
            completeness_checks=checks,
        )

        component = "artifact_index"
        index_started_at = utc_now()
        index_started = time.perf_counter()
        artifacts = build_artifact_index(context)
        update_component(
            context,
            "artifact_index",
            index_started_at,
            index_started,
            artifact_count=len(artifacts),
        )
        manifest_path = context.run_dir / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["run_status"] = "measurement_complete"
        manifest["completed_at"] = utc_now()
        manifest["result"] = summary
        manifest["artifact_index"] = "artifact_index.json"
        write_json(manifest_path, manifest)
        print(json.dumps(summary, indent=2), flush=True)
    except BaseException as error:
        fail_run(context, component, error)
        raise
    finally:
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def verify_existing(context: Any) -> dict[str, Any]:
    required = (
        "manifest.json",
        "capture_validation.json",
        "pairwise_hidden_state_metrics.csv",
        "pairwise_vocabulary_score_metrics.csv",
        "pairwise_next_token_distribution_metrics.csv",
        "pairwise_topology_metrics.csv",
        "network_index.csv",
        "divergence_by_state.csv",
        "R019_RESULT.json",
        "R019_MEASUREMENT_REPORT.md",
        "R019_COMPLETENESS_VERIFICATION.md",
        "artifact_index.json",
    )
    missing = [name for name in required if not (context.run_dir / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing R019 artifacts: {missing}")
    manifest = json.loads(
        (context.run_dir / "manifest.json").read_text(encoding="utf-8")
    )
    if manifest.get("run_status") != "measurement_complete":
        raise RuntimeError(f"R019 status is {manifest.get('run_status')!r}.")
    artifact_index = json.loads(
        (context.run_dir / "artifact_index.json").read_text(encoding="utf-8")
    )["artifacts"]
    hash_failures: list[str] = []
    for record in artifact_index:
        artifact_path = context.run_dir / str(record["path"])
        if not artifact_path.is_file():
            hash_failures.append(f"missing:{record['path']}")
        elif artifact_path.stat().st_size != int(record["bytes"]):
            hash_failures.append(f"size:{record['path']}")
        elif sha256_file(artifact_path) != str(record["sha256"]):
            hash_failures.append(f"sha256:{record['path']}")
    if hash_failures:
        raise RuntimeError(f"R019 artifact-index verification failed: {hash_failures}")
    result = json.loads(
        (context.run_dir / "R019_RESULT.json").read_text(encoding="utf-8")
    )
    return {
        "status": "verified",
        "run_id": context.config["run_id"],
        "conclusion": result["conclusion"],
        "required_artifacts": len(required),
        "indexed_artifacts_verified": len(artifact_index),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("validate-config", "measure", "refresh-derived", "verify")
    )
    parser.add_argument("--config", required=True, type=Path)
    arguments = parser.parse_args()
    context = load_and_validate_config(arguments.config)
    if arguments.action == "validate-config":
        print(
            json.dumps(
                {
                    "status": "valid",
                    "run_id": context.config["run_id"],
                    "prompts": list(context.prompt_ids),
                    "repeat_count": context.config["capture"]["repeat_count"],
                    "expected": context.config["expected"],
                },
                indent=2,
            )
        )
    elif arguments.action == "measure":
        measure(context)
    elif arguments.action == "refresh-derived":
        print(json.dumps(refresh_derived_outputs(context), indent=2))
    else:
        print(json.dumps(verify_existing(context), indent=2))


if __name__ == "__main__":
    main()
