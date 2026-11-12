from __future__ import annotations

import gc
import hashlib
import json
import os
import platform
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import safetensors
import torch
import torch.nn.functional as F
import transformers
from huggingface_hub import snapshot_download
from safetensors import safe_open
from safetensors.torch import load_file, save_file
from transformers import AutoConfig, AutoTokenizer


RUN_NUMBER = "R002"
RUN_NAME = "lithium-static-basis-cutoff-feasibility"
SOURCE_RUN_ID = (
    "R001_lithium-initial-output-inspection__"
    "20261112T063540Z_pythia-6.9b_52ff8f97c2"
)

EXPECTED_HF_HOME = Path(r"D:\AI\cache\huggingface").resolve()
EXPECTED_HF_HUB_CACHE = (EXPECTED_HF_HOME / "hub").resolve()
EMBEDDING_WEIGHT_NAME = "gpt_neox.embed_in.weight"
SCORE_CHUNK_SIZE = 8192

WINDOW_SPECS = (
    ("full", 1.00),
    ("top_10pct", 0.10),
    ("top_5pct", 0.05),
    ("top_2pct", 0.02),
    ("top_1pct", 0.01),
)
CONSENSUS_WINDOWS = {"top_10pct", "top_5pct", "top_2pct", "top_1pct"}
VIABLE_MIN_SUPPORT = 3
VIABLE_MAX_RELATIVE_MAD = 0.20
VIABLE_MIN_STRENGTH = 0.08
WEAK_MIN_SUPPORT = 2
WEAK_MAX_RELATIVE_MAD = 0.40
WEAK_MIN_STRENGTH = 0.04

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUNS_DIR = PIPELINE_DIR / "runs"
SOURCE_RUN_DIR = RUNS_DIR / SOURCE_RUN_ID


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def artifact_record(path: Path) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "sha256": sha256_file(path)}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_run_identity() -> None:
    if not re.fullmatch(r"R\d{3}", RUN_NUMBER):
        raise ValueError("RUN_NUMBER must use the form RNNN.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", RUN_NAME):
        raise ValueError("RUN_NAME must use lowercase kebab-case.")
    existing = sorted(path.name for path in RUNS_DIR.glob(f"{RUN_NUMBER}_*"))
    if existing:
        raise RuntimeError(
            f"{RUN_NUMBER} is already assigned to {existing[0]}. "
            "Run numbers are never reused."
        )


def validate_cache_configuration() -> None:
    hf_home = os.environ.get("HF_HOME")
    hub_cache = os.environ.get("HF_HUB_CACHE")
    if not hf_home or not hub_cache:
        raise RuntimeError("HF_HOME and HF_HUB_CACHE must be configured.")
    if Path(hf_home).resolve() != EXPECTED_HF_HOME:
        raise RuntimeError(f"HF_HOME must resolve to {EXPECTED_HF_HOME}.")
    if Path(hub_cache).resolve() != EXPECTED_HF_HUB_CACHE:
        raise RuntimeError(f"HF_HUB_CACHE must resolve to {EXPECTED_HF_HUB_CACHE}.")


def state_metadata(state_count: int, layer_count: int) -> pd.DataFrame:
    if state_count != layer_count + 1:
        raise ValueError(
            f"Expected {layer_count + 1} captured states for {layer_count} blocks; "
            f"found {state_count}."
        )

    records = []
    for state_index in range(state_count):
        if state_index == 0:
            state_type = "input_embedding"
            block_index = None
            state_label = "input_embedding"
        elif state_index == state_count - 1:
            state_type = "final_normalized_output"
            block_index = layer_count - 1
            state_label = f"final_norm_after_block_{layer_count - 1}"
        else:
            state_type = "block_output"
            block_index = state_index - 1
            state_label = f"block_{block_index:02d}_output"
        records.append(
            {
                "state_index": state_index,
                "state_type": state_type,
                "block_index": block_index,
                "state_label": state_label,
            }
        )
    return pd.DataFrame(records)


def classify_token(
    token_id: int,
    raw_token: str,
    decoded_token: str,
    special_token_ids: set[int],
    target_token_id: int,
    target_text: str,
) -> tuple[str, bool]:
    target_normalized = target_text.strip().casefold()
    decoded_normalized = decoded_token.strip().casefold()
    is_lexical_variant = (
        token_id != target_token_id
        and len(decoded_normalized) >= 2
        and (
            decoded_normalized in target_normalized
            or target_normalized in decoded_normalized
        )
    )

    if token_id == target_token_id:
        token_class = "exact_target"
    elif is_lexical_variant:
        token_class = "target_lexical_variant"
    elif token_id in special_token_ids:
        token_class = "special"
    elif not decoded_token.strip():
        token_class = "whitespace"
    elif not any(character.isalnum() for character in decoded_token):
        token_class = "punctuation_or_symbol"
    elif raw_token.startswith("Ġ"):
        token_class = "word_initial"
    else:
        token_class = "continuation_or_standalone"
    return token_class, is_lexical_variant


def elbow_candidate(sorted_scores: np.ndarray, window_count: int) -> dict:
    window_count = min(max(int(window_count), 5), sorted_scores.size)
    values = sorted_scores[:window_count].astype(np.float64, copy=False)
    score_range = float(values[0] - values[-1])
    if not np.isfinite(score_range) or score_range <= np.finfo(np.float64).eps:
        return {
            "candidate_valid": False,
            "elbow_rank": None,
            "elbow_score": None,
            "elbow_strength": 0.0,
            "score_gap_after": None,
            "gap_ratio": None,
        }

    x = np.linspace(0.0, 1.0, window_count, dtype=np.float64)
    normalized_scores = (values - values[-1]) / score_range
    chord = 1.0 - x
    deviation = chord - normalized_scores
    elbow_index = int(np.argmax(deviation))
    strength = float(deviation[elbow_index])

    if elbow_index < 1 or elbow_index >= window_count - 1 or strength <= 0.0:
        return {
            "candidate_valid": False,
            "elbow_rank": None,
            "elbow_score": None,
            "elbow_strength": max(strength, 0.0),
            "score_gap_after": None,
            "gap_ratio": None,
        }

    gaps = values[:-1] - values[1:]
    positive_gaps = gaps[gaps > 0]
    baseline_gap = float(np.median(positive_gaps)) if positive_gaps.size else 0.0
    score_gap = float(gaps[elbow_index])
    gap_ratio = score_gap / baseline_gap if baseline_gap > 0 else None

    return {
        "candidate_valid": True,
        "elbow_rank": elbow_index + 1,
        "elbow_score": float(values[elbow_index]),
        "elbow_strength": strength,
        "score_gap_after": score_gap,
        "gap_ratio": gap_ratio,
    }


def classify_cutoff(
    support: int,
    relative_mad: float | None,
    median_strength: float | None,
    candidate_rank: int | None,
) -> tuple[str, str]:
    if candidate_rank is None or candidate_rank < 3:
        return "none", "No interior consensus elbow was available."
    if relative_mad is None or median_strength is None:
        return "none", "Insufficient valid upper-tail windows."
    if (
        support >= VIABLE_MIN_SUPPORT
        and relative_mad <= VIABLE_MAX_RELATIVE_MAD
        and median_strength >= VIABLE_MIN_STRENGTH
    ):
        return "viable", "Upper-tail elbow rank was strong and stable across windows."
    if (
        support >= WEAK_MIN_SUPPORT
        and relative_mad <= WEAK_MAX_RELATIVE_MAD
        and median_strength >= WEAK_MIN_STRENGTH
    ):
        return "weak", "An upper-tail elbow was present but did not meet the viable threshold."
    return "none", "Upper-tail elbow candidates were too weak or window-sensitive."


def add_component_success(manifest: dict, component: str, started: float) -> None:
    manifest["components"][component] = {
        "status": "successful",
        "completed_at": utc_now_iso(),
        "seconds": time.perf_counter() - started,
    }


def main() -> None:
    validate_run_identity()
    validate_cache_configuration()
    if not SOURCE_RUN_DIR.is_dir():
        raise FileNotFoundError(f"Source run not found: {SOURCE_RUN_DIR}")

    source_manifest_path = SOURCE_RUN_DIR / "manifest.json"
    source_manifest = load_json(source_manifest_path)
    model_id = source_manifest["model"]["id"]
    model_revision = source_manifest["model"]["resolved_revision"]
    prompt_hash = source_manifest["input"]["prompt_sha256"]
    model_slug = model_id.rsplit("/", 1)[-1]

    started_at = datetime.now(timezone.utc)
    technical_id = (
        f"{started_at.strftime('%Y%m%dT%H%M%SZ')}_"
        f"{model_slug}_{prompt_hash[:10]}"
    )
    run_id = f"{RUN_NUMBER}_{RUN_NAME}__{technical_id}"
    run_dir = RUNS_DIR / run_id
    figures_dir = run_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=False)

    manifest_path = run_dir / "manifest.json"
    pipeline_path = Path(__file__).resolve()
    required_components = [
        "source_validation",
        "static_basis_scores",
        "cutoff_analysis",
        "contextual_diagnostic",
        "validation",
    ]
    manifest = {
        "run_number": RUN_NUMBER,
        "run_name": RUN_NAME,
        "run_id": run_id,
        "technical_id": technical_id,
        "source_run": SOURCE_RUN_ID,
        "status": "running",
        "started_at": started_at.isoformat(),
        "completed_at": None,
        "required_components": required_components,
        "components": {name: {"status": "pending"} for name in required_components},
        "model": {
            "id": model_id,
            "revision": model_revision,
            "model_forward_executed": False,
            "embedding_weight": EMBEDDING_WEIGHT_NAME,
        },
        "input": {
            "prompt": source_manifest["input"]["prompt"],
            "prompt_sha256": prompt_hash,
            "target_text": source_manifest["input"]["target_text"],
            "target_token_id": source_manifest["input"]["target_token_id"],
            "target_position": source_manifest["input"]["target_position"],
        },
        "pipeline": {
            "script": str(pipeline_path.relative_to(PROJECT_DIR)),
            "script_sha256": sha256_file(pipeline_path),
        },
        "environment": {
            "python": platform.python_version(),
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "safetensors": safetensors.__version__,
            "pandas": pd.__version__,
            "matplotlib": matplotlib.__version__,
            "device": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
            "hf_home": str(EXPECTED_HF_HOME),
            "hf_hub_cache": str(EXPECTED_HF_HUB_CACHE),
        },
        "method": {
            "static_basis_metric": "cosine_similarity",
            "valid_vocabulary_definition": "token IDs from 0 through len(tokenizer)-1",
            "cutoff_algorithm": "maximum normalized deviation below endpoint chord",
            "window_specs": [
                {"label": label, "fraction": fraction}
                for label, fraction in WINDOW_SPECS
            ],
            "consensus_windows": sorted(CONSENSUS_WINDOWS),
            "classification": {
                "viable": {
                    "minimum_support": VIABLE_MIN_SUPPORT,
                    "maximum_relative_mad": VIABLE_MAX_RELATIVE_MAD,
                    "minimum_median_strength": VIABLE_MIN_STRENGTH,
                },
                "weak": {
                    "minimum_support": WEAK_MIN_SUPPORT,
                    "maximum_relative_mad": WEAK_MAX_RELATIVE_MAD,
                    "minimum_median_strength": WEAK_MIN_STRENGTH,
                },
                "none": "all other cases",
            },
            "variants": ["all_tokens", "exact_target_removed"],
            "state_semantics": {
                "state_0": "input embedding presented to block 0",
                "intermediate_states": "outputs after transformer blocks 0 through 30",
                "state_32": "final layer-normalized output after block 31",
                "raw_block_31_output_available": False,
            },
            "interpretation_boundary": (
                "Scores measure compatibility between a contextual target state and "
                "the static input-embedding basis; they are not contextual relations "
                "among the full vocabulary."
            ),
        },
        "artifacts": {},
        "results": {},
    }

    def write_manifest() -> None:
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    write_manifest()
    current_component = "source_validation"

    try:
        component_started = time.perf_counter()
        if source_manifest.get("status") != "successful":
            raise RuntimeError("Source run manifest is not successful.")
        for relative_path, expected in source_manifest["artifacts"].items():
            source_path = SOURCE_RUN_DIR / relative_path
            if not source_path.is_file():
                raise FileNotFoundError(f"Missing source artifact: {source_path}")
            if source_path.stat().st_size != expected["bytes"]:
                raise RuntimeError(f"Source artifact size mismatch: {relative_path}")
            if sha256_file(source_path) != expected["sha256"]:
                raise RuntimeError(f"Source artifact hash mismatch: {relative_path}")

        hidden_states = load_file(SOURCE_RUN_DIR / "hidden_states.safetensors")[
            "hidden_states"
        ]
        source_tokens = pd.read_csv(SOURCE_RUN_DIR / "tokens.csv")
        target_position = int(source_manifest["input"]["target_position"])
        target_token_id = int(source_manifest["input"]["target_token_id"])
        if hidden_states.ndim != 3:
            raise ValueError(f"Expected a 3D hidden-state tensor; found {hidden_states.shape}.")
        if target_position >= hidden_states.shape[1]:
            raise ValueError("Target position is outside the captured token dimension.")
        recorded_target = source_tokens.loc[
            source_tokens["position"] == target_position, "token_id"
        ]
        if recorded_target.empty or int(recorded_target.iloc[0]) != target_token_id:
            raise ValueError("Source token table does not match the manifest target.")
        add_component_success(manifest, current_component, component_started)
        write_manifest()

        current_component = "static_basis_scores"
        component_started = time.perf_counter()
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        snapshot_path = Path(
            snapshot_download(
                model_id,
                revision=model_revision,
                cache_dir=EXPECTED_HF_HUB_CACHE,
                local_files_only=True,
            )
        )
        config = AutoConfig.from_pretrained(
            snapshot_path,
            local_files_only=True,
        )
        tokenizer = AutoTokenizer.from_pretrained(
            snapshot_path,
            local_files_only=True,
        )
        index_path = snapshot_path / "model.safetensors.index.json"
        index_data = load_json(index_path)
        shard_name = index_data["weight_map"].get(EMBEDDING_WEIGHT_NAME)
        if not shard_name:
            raise KeyError(f"Embedding weight not found: {EMBEDDING_WEIGHT_NAME}")
        shard_path = snapshot_path / shard_name
        with safe_open(shard_path, framework="pt", device="cpu") as handle:
            embedding_matrix = handle.get_tensor(EMBEDDING_WEIGHT_NAME)

        valid_vocab_size = len(tokenizer)
        if valid_vocab_size > embedding_matrix.shape[0]:
            raise ValueError("Tokenizer contains more IDs than the embedding matrix.")
        embedding_matrix = embedding_matrix[:valid_vocab_size]
        state_table = state_metadata(hidden_states.shape[0], int(config.num_hidden_layers))

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if device.type == "cuda":
            torch.cuda.empty_cache()
            torch.cuda.reset_peak_memory_stats()
        target_states = hidden_states[:, target_position, :].to(device=device, dtype=torch.float32)
        target_states = F.normalize(target_states, p=2, dim=1)
        score_matrix = torch.empty(
            (hidden_states.shape[0], valid_vocab_size),
            dtype=torch.float32,
            device="cpu",
        )
        with torch.inference_mode():
            for start in range(0, valid_vocab_size, SCORE_CHUNK_SIZE):
                end = min(start + SCORE_CHUNK_SIZE, valid_vocab_size)
                embedding_chunk = embedding_matrix[start:end].to(
                    device=device,
                    dtype=torch.float32,
                )
                embedding_chunk = F.normalize(embedding_chunk, p=2, dim=1)
                score_matrix[:, start:end] = (
                    target_states @ embedding_chunk.transpose(0, 1)
                ).cpu()
                del embedding_chunk

        scores_path = run_dir / "vocabulary_scores.safetensors"
        save_file(
            {"cosine_scores": score_matrix.contiguous()},
            scores_path,
            metadata={
                "metric": "cosine_similarity",
                "basis": EMBEDDING_WEIGHT_NAME,
                "source_run": SOURCE_RUN_ID,
            },
        )

        token_ids = np.arange(valid_vocab_size, dtype=np.int64)
        raw_tokens = tokenizer.convert_ids_to_tokens(token_ids.tolist())
        decoded_tokens = [
            tokenizer.decode([int(token_id)], clean_up_tokenization_spaces=False)
            for token_id in token_ids
        ]
        special_token_ids = set(tokenizer.all_special_ids)
        token_classes = []
        lexical_variant_flags = []
        for token_id, raw_token, decoded_token in zip(
            token_ids,
            raw_tokens,
            decoded_tokens,
            strict=True,
        ):
            token_class, is_variant = classify_token(
                int(token_id),
                raw_token,
                decoded_token,
                special_token_ids,
                target_token_id,
                source_manifest["input"]["target_text"],
            )
            token_classes.append(token_class)
            lexical_variant_flags.append(is_variant)
        vocabulary_table = pd.DataFrame(
            {
                "token_id": token_ids,
                "raw_token": raw_tokens,
                "decoded_token": decoded_tokens,
                "token_class": token_classes,
                "is_exact_target": token_ids == target_token_id,
                "is_target_lexical_variant": lexical_variant_flags,
            }
        )
        vocabulary_path = run_dir / "vocabulary_tokens.csv"
        vocabulary_table.to_csv(vocabulary_path, index=False, lineterminator="\n")
        state_table_path = run_dir / "state_metadata.csv"
        state_table.to_csv(state_table_path, index=False, lineterminator="\n")

        peak_gpu_gib = (
            torch.cuda.max_memory_allocated() / 1024**3 if device.type == "cuda" else 0.0
        )
        del embedding_matrix, target_states
        if device.type == "cuda":
            torch.cuda.empty_cache()
        gc.collect()
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "score_shape": list(score_matrix.shape),
                "score_dtype": str(score_matrix.dtype),
                "embedding_rows_total": int(config.vocab_size),
                "valid_vocabulary_size": valid_vocab_size,
                "padded_rows_excluded": int(config.vocab_size - valid_vocab_size),
                "device": str(device),
                "peak_gpu_memory_gib": peak_gpu_gib,
            }
        )
        write_manifest()

        current_component = "cutoff_analysis"
        component_started = time.perf_counter()
        scores_numpy = score_matrix.numpy()
        state_lookup = state_table.set_index("state_index").to_dict("index")
        candidate_records = []
        summary_records = []
        sorted_cache: dict[tuple[int, str], tuple[np.ndarray, np.ndarray]] = {}

        for state_index in range(scores_numpy.shape[0]):
            state_info = state_lookup[state_index]
            for variant in ("all_tokens", "exact_target_removed"):
                if variant == "all_tokens":
                    variant_ids = token_ids
                else:
                    variant_ids = token_ids[token_ids != target_token_id]
                variant_scores = scores_numpy[state_index, variant_ids]
                order = np.argsort(-variant_scores, kind="stable")
                sorted_scores = variant_scores[order]
                sorted_ids = variant_ids[order]
                sorted_cache[(state_index, variant)] = (sorted_scores, sorted_ids)

                state_candidates = []
                for window_label, window_fraction in WINDOW_SPECS:
                    window_count = (
                        sorted_scores.size
                        if window_fraction == 1.0
                        else max(50, round(sorted_scores.size * window_fraction))
                    )
                    candidate = elbow_candidate(sorted_scores, window_count)
                    record = {
                        "state_index": state_index,
                        "state_type": state_info["state_type"],
                        "state_label": state_info["state_label"],
                        "variant": variant,
                        "window_label": window_label,
                        "window_fraction": window_fraction,
                        "window_count": min(window_count, sorted_scores.size),
                        **candidate,
                    }
                    candidate_records.append(record)
                    state_candidates.append(record)

                upper_candidates = [
                    record
                    for record in state_candidates
                    if record["window_label"] in CONSENSUS_WINDOWS
                    and record["candidate_valid"]
                ]
                ranks = np.array(
                    [record["elbow_rank"] for record in upper_candidates],
                    dtype=np.float64,
                )
                strengths = np.array(
                    [record["elbow_strength"] for record in upper_candidates],
                    dtype=np.float64,
                )
                if ranks.size:
                    consensus_rank = max(1, int(round(float(np.median(ranks)))))
                    rank_mad = float(np.median(np.abs(ranks - np.median(ranks))))
                    relative_mad = rank_mad / float(np.median(ranks))
                    tolerance = max(5.0, 0.25 * consensus_rank)
                    support = int(np.sum(np.abs(ranks - consensus_rank) <= tolerance))
                    median_strength = float(np.median(strengths))
                    cutoff_score = float(sorted_scores[consensus_rank - 1])
                    score_gap_after = (
                        float(
                            sorted_scores[consensus_rank - 1]
                            - sorted_scores[consensus_rank]
                        )
                        if consensus_rank < sorted_scores.size
                        else None
                    )
                else:
                    consensus_rank = None
                    rank_mad = None
                    relative_mad = None
                    support = 0
                    median_strength = None
                    cutoff_score = None
                    score_gap_after = None

                cutoff_status, classification_reason = classify_cutoff(
                    support,
                    relative_mad,
                    median_strength,
                    consensus_rank,
                )
                full_candidate = next(
                    record
                    for record in state_candidates
                    if record["window_label"] == "full"
                )
                summary_records.append(
                    {
                        "state_index": state_index,
                        "state_type": state_info["state_type"],
                        "state_label": state_info["state_label"],
                        "variant": variant,
                        "cutoff_status": cutoff_status,
                        "classification_reason": classification_reason,
                        "candidate_rank": consensus_rank,
                        "cutoff_score": cutoff_score,
                        "score_gap_after": score_gap_after,
                        "upper_window_valid_count": len(upper_candidates),
                        "consensus_support": support,
                        "rank_mad": rank_mad,
                        "relative_rank_mad": relative_mad,
                        "median_elbow_strength": median_strength,
                        "full_curve_elbow_rank": full_candidate["elbow_rank"],
                        "full_curve_elbow_score": full_candidate["elbow_score"],
                        "full_curve_elbow_strength": full_candidate[
                            "elbow_strength"
                        ],
                        "accepted_neighbor_count": (
                            consensus_rank if cutoff_status in {"viable", "weak"} else 0
                        ),
                    }
                )

        cutoff_candidates = pd.DataFrame(candidate_records)
        cutoff_summary = pd.DataFrame(summary_records)
        candidates_path = run_dir / "cutoff_candidates.csv"
        summary_path = run_dir / "cutoff_summary.csv"
        cutoff_candidates.to_csv(candidates_path, index=False, lineterminator="\n")
        cutoff_summary.to_csv(summary_path, index=False, lineterminator="\n")

        accepted_frames = []
        preview_frames = []
        active_sets: dict[int, set[int]] = {}
        primary_summary = cutoff_summary[
            cutoff_summary["variant"] == "exact_target_removed"
        ].copy()
        for row in primary_summary.itertuples(index=False):
            sorted_scores, sorted_ids = sorted_cache[
                (int(row.state_index), "exact_target_removed")
            ]
            candidate_rank = int(row.candidate_rank) if pd.notna(row.candidate_rank) else 0
            preview_count = min(50, candidate_rank or 50, sorted_ids.size)
            preview_ids = sorted_ids[:preview_count]
            preview_frames.append(
                pd.DataFrame(
                    {
                        "state_index": int(row.state_index),
                        "state_type": row.state_type,
                        "state_label": row.state_label,
                        "cutoff_status": row.cutoff_status,
                        "candidate_rank": candidate_rank or None,
                        "rank": np.arange(1, preview_count + 1),
                        "token_id": preview_ids,
                        "score": sorted_scores[:preview_count],
                        "raw_token": np.asarray(raw_tokens, dtype=object)[preview_ids],
                        "decoded_token": np.asarray(decoded_tokens, dtype=object)[preview_ids],
                        "token_class": np.asarray(token_classes, dtype=object)[preview_ids],
                        "is_target_lexical_variant": np.asarray(
                            lexical_variant_flags,
                            dtype=bool,
                        )[preview_ids],
                    }
                )
            )
            if row.cutoff_status in {"viable", "weak"} and candidate_rank > 0:
                accepted_ids = sorted_ids[:candidate_rank]
                active_sets[int(row.state_index)] = set(int(value) for value in accepted_ids)
                accepted_frames.append(
                    pd.DataFrame(
                        {
                            "state_index": int(row.state_index),
                            "state_type": row.state_type,
                            "state_label": row.state_label,
                            "cutoff_status": row.cutoff_status,
                            "cutoff_score": row.cutoff_score,
                            "rank": np.arange(1, candidate_rank + 1),
                            "token_id": accepted_ids,
                            "score": sorted_scores[:candidate_rank],
                            "raw_token": np.asarray(raw_tokens, dtype=object)[accepted_ids],
                            "decoded_token": np.asarray(decoded_tokens, dtype=object)[
                                accepted_ids
                            ],
                            "token_class": np.asarray(token_classes, dtype=object)[accepted_ids],
                            "is_target_lexical_variant": np.asarray(
                                lexical_variant_flags,
                                dtype=bool,
                            )[accepted_ids],
                        }
                    )
                )
            else:
                active_sets[int(row.state_index)] = set()

        candidate_neighbors = (
            pd.concat(accepted_frames, ignore_index=True)
            if accepted_frames
            else pd.DataFrame(
                columns=[
                    "state_index",
                    "state_type",
                    "state_label",
                    "cutoff_status",
                    "cutoff_score",
                    "rank",
                    "token_id",
                    "score",
                    "raw_token",
                    "decoded_token",
                    "token_class",
                    "is_target_lexical_variant",
                ]
            )
        )
        preview_neighbors = pd.concat(preview_frames, ignore_index=True)
        accepted_path = run_dir / "candidate_neighbors.csv.gz"
        preview_path = run_dir / "candidate_neighbors_preview.csv"
        candidate_neighbors.to_csv(
            accepted_path,
            index=False,
            compression="gzip",
            lineterminator="\n",
        )
        preview_neighbors.to_csv(preview_path, index=False, lineterminator="\n")

        overlap_records = []
        for state_index in range(scores_numpy.shape[0] - 1):
            current_set = active_sets[state_index]
            next_set = active_sets[state_index + 1]
            union = current_set | next_set
            intersection = current_set & next_set
            overlap_records.append(
                {
                    "from_state": state_index,
                    "to_state": state_index + 1,
                    "from_size": len(current_set),
                    "to_size": len(next_set),
                    "intersection_size": len(intersection),
                    "union_size": len(union),
                    "jaccard": len(intersection) / len(union) if union else np.nan,
                }
            )
        overlap_table = pd.DataFrame(overlap_records)
        overlap_path = run_dir / "neighbor_overlap.csv"
        overlap_table.to_csv(overlap_path, index=False, lineterminator="\n")

        if not candidate_neighbors.empty:
            trajectory_table = (
                candidate_neighbors.groupby(
                    [
                        "token_id",
                        "raw_token",
                        "decoded_token",
                        "token_class",
                        "is_target_lexical_variant",
                    ],
                    dropna=False,
                )
                .agg(
                    first_active_state=("state_index", "min"),
                    last_active_state=("state_index", "max"),
                    active_state_count=("state_index", "nunique"),
                    best_rank=("rank", "min"),
                    maximum_score=("score", "max"),
                    mean_score=("score", "mean"),
                )
                .reset_index()
                .sort_values(
                    ["active_state_count", "best_rank"],
                    ascending=[False, True],
                )
            )
        else:
            trajectory_table = pd.DataFrame(
                columns=[
                    "token_id",
                    "raw_token",
                    "decoded_token",
                    "token_class",
                    "is_target_lexical_variant",
                    "first_active_state",
                    "last_active_state",
                    "active_state_count",
                    "best_rank",
                    "maximum_score",
                    "mean_score",
                ]
            )
        trajectory_path = run_dir / "neighbor_trajectories.csv"
        trajectory_table.to_csv(trajectory_path, index=False, lineterminator="\n")

        status_counts = (
            primary_summary["cutoff_status"].value_counts().sort_index().to_dict()
        )
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "primary_variant": "exact_target_removed",
                "status_counts": {key: int(value) for key, value in status_counts.items()},
                "candidate_neighbor_rows": int(len(candidate_neighbors)),
            }
        )
        write_manifest()

        current_component = "contextual_diagnostic"
        component_started = time.perf_counter()
        hidden_float = hidden_states.to(dtype=torch.float32)
        contextual_normalized = F.normalize(hidden_float, p=2, dim=2)
        contextual_scores = torch.matmul(
            contextual_normalized,
            contextual_normalized.transpose(1, 2),
        )
        contextual_path = run_dir / "contextual_prompt_similarity.safetensors"
        save_file(
            {"cosine_scores": contextual_scores.contiguous()},
            contextual_path,
            metadata={
                "metric": "cosine_similarity",
                "scope": "tokens observed in the single source prompt",
                "source_run": SOURCE_RUN_ID,
            },
        )

        contextual_records = []
        for state_index in range(contextual_scores.shape[0]):
            state_info = state_lookup[state_index]
            for position_a in range(contextual_scores.shape[1]):
                for position_b in range(position_a + 1, contextual_scores.shape[2]):
                    token_a = source_tokens.iloc[position_a]
                    token_b = source_tokens.iloc[position_b]
                    contextual_records.append(
                        {
                            "state_index": state_index,
                            "state_type": state_info["state_type"],
                            "state_label": state_info["state_label"],
                            "position_a": position_a,
                            "token_id_a": int(token_a["token_id"]),
                            "decoded_token_a": token_a["decoded_token"],
                            "position_b": position_b,
                            "token_id_b": int(token_b["token_id"]),
                            "decoded_token_b": token_b["decoded_token"],
                            "cosine_similarity": float(
                                contextual_scores[
                                    state_index,
                                    position_a,
                                    position_b,
                                ]
                            ),
                        }
                    )
        contextual_table = pd.DataFrame(contextual_records)
        contextual_table_path = run_dir / "contextual_prompt_relationships.csv"
        contextual_table.to_csv(
            contextual_table_path,
            index=False,
            lineterminator="\n",
        )
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "matrix_shape": list(contextual_scores.shape),
                "relationship_rows": int(len(contextual_table)),
                "interpretation_boundary": (
                    "Prompt-local contextual diagnostic; not a controlled semantic "
                    "token population and not evidence of topic recovery."
                ),
            }
        )
        write_manifest()

        primary_summary = primary_summary.sort_values("state_index")
        status_color = {"viable": "#2a9d8f", "weak": "#e9c46a", "none": "#e76f51"}

        figure, axes = plt.subplots(3, 1, figsize=(11, 12), sharex=True)
        colors = [status_color[value] for value in primary_summary["cutoff_status"]]
        axes[0].bar(primary_summary["state_index"], primary_summary["candidate_rank"], color=colors)
        axes[0].set_ylabel("Candidate elbow rank")
        axes[0].set_title("Target-removed cutoff candidates by recorded state")
        axes[1].plot(
            primary_summary["state_index"],
            primary_summary["cutoff_score"],
            marker="o",
            linewidth=1,
        )
        axes[1].set_ylabel("Cosine cutoff score")
        axes[2].plot(
            primary_summary["state_index"],
            primary_summary["relative_rank_mad"],
            marker="o",
            label="relative rank MAD",
        )
        axes[2].axhline(VIABLE_MAX_RELATIVE_MAD, color="#2a9d8f", linestyle="--", label="viable limit")
        axes[2].axhline(WEAK_MAX_RELATIVE_MAD, color="#e9c46a", linestyle="--", label="weak limit")
        axes[2].set_ylabel("Window sensitivity")
        axes[2].set_xlabel("Recorded state index")
        axes[2].legend()
        figure.tight_layout()
        cutoff_figure_path = figures_dir / "cutoff_overview.png"
        figure.savefig(cutoff_figure_path, dpi=180)
        plt.close(figure)

        selected_states = [0, 8, 16, 24, 31, 32]
        figure, axes = plt.subplots(2, 3, figsize=(16, 9), sharey=True)
        for axis, state_index in zip(axes.flat, selected_states, strict=True):
            sorted_scores, _ = sorted_cache[(state_index, "exact_target_removed")]
            ranks = np.arange(1, sorted_scores.size + 1)
            row = primary_summary.loc[primary_summary["state_index"] == state_index].iloc[0]
            axis.plot(ranks, sorted_scores, linewidth=1)
            axis.set_xscale("log")
            if pd.notna(row["candidate_rank"]):
                axis.axvline(int(row["candidate_rank"]), color=status_color[row["cutoff_status"]], linestyle="--")
            axis.set_title(f"{row['state_label']} ({row['cutoff_status']})")
            axis.set_xlabel("Vocabulary rank (log scale)")
            axis.grid(alpha=0.2)
        axes[0, 0].set_ylabel("Cosine similarity")
        axes[1, 0].set_ylabel("Cosine similarity")
        figure.tight_layout()
        curves_figure_path = figures_dir / "score_curves_selected_states.png"
        figure.savefig(curves_figure_path, dpi=180)
        plt.close(figure)

        figure, axis = plt.subplots(figsize=(11, 4.5))
        axis.plot(
            overlap_table["to_state"],
            overlap_table["jaccard"],
            marker="o",
        )
        axis.set_xlabel("Destination state index")
        axis.set_ylabel("Jaccard overlap")
        axis.set_ylim(0, 1)
        axis.set_title("Accepted-neighbour overlap between consecutive states")
        axis.grid(alpha=0.25)
        figure.tight_layout()
        overlap_figure_path = figures_dir / "neighbor_overlap.png"
        figure.savefig(overlap_figure_path, dpi=180)
        plt.close(figure)

        labels = [
            f"{int(row.position)}:{str(row.decoded_token).strip() or str(row.raw_token)}"
            for row in source_tokens.itertuples(index=False)
        ]
        contextual_states = [0, 16, 31, 32]
        figure, axes = plt.subplots(2, 2, figsize=(16, 14))
        image = None
        for axis, state_index in zip(axes.flat, contextual_states, strict=True):
            image = axis.imshow(
                contextual_scores[state_index].numpy(),
                vmin=-1,
                vmax=1,
                cmap="coolwarm",
            )
            axis.set_title(state_lookup[state_index]["state_label"])
            axis.set_xticks(range(len(labels)), labels, rotation=90, fontsize=7)
            axis.set_yticks(range(len(labels)), labels, fontsize=7)
        figure.colorbar(image, ax=axes.ravel().tolist(), shrink=0.7, label="Cosine similarity")
        contextual_figure_path = figures_dir / "contextual_prompt_similarity.png"
        figure.savefig(contextual_figure_path, dpi=180, bbox_inches="tight")
        plt.close(figure)

        current_component = "validation"
        component_started = time.perf_counter()
        artifact_paths = [
            scores_path,
            vocabulary_path,
            state_table_path,
            candidates_path,
            summary_path,
            accepted_path,
            preview_path,
            overlap_path,
            trajectory_path,
            contextual_path,
            contextual_table_path,
            cutoff_figure_path,
            curves_figure_path,
            overlap_figure_path,
            contextual_figure_path,
        ]
        loaded_scores = load_file(scores_path)["cosine_scores"]
        loaded_contextual = load_file(contextual_path)["cosine_scores"]
        if tuple(loaded_scores.shape) != tuple(score_matrix.shape):
            raise RuntimeError("Persisted vocabulary score matrix has the wrong shape.")
        if tuple(loaded_contextual.shape) != tuple(contextual_scores.shape):
            raise RuntimeError("Persisted contextual matrix has the wrong shape.")
        if not torch.isfinite(loaded_scores).all():
            raise RuntimeError("Vocabulary score matrix contains non-finite values.")
        if loaded_scores.min() < -1.0001 or loaded_scores.max() > 1.0001:
            raise RuntimeError("Vocabulary cosine scores are outside the valid range.")
        if len(cutoff_summary) != hidden_states.shape[0] * 2:
            raise RuntimeError("Cutoff summary does not contain both variants for every state.")
        if len(contextual_table) != hidden_states.shape[0] * 171:
            raise RuntimeError("Contextual relationship table has the wrong row count.")

        manifest["artifacts"] = {
            str(path.relative_to(run_dir)).replace("\\", "/"): artifact_record(path)
            for path in artifact_paths
        }
        primary_counts = (
            primary_summary["cutoff_status"].value_counts().sort_index().to_dict()
        )
        all_token_counts = (
            cutoff_summary.loc[
                cutoff_summary["variant"] == "all_tokens",
                "cutoff_status",
            ]
            .value_counts()
            .sort_index()
            .to_dict()
        )
        manifest["results"] = {
            "state_count": int(hidden_states.shape[0]),
            "valid_vocabulary_size": valid_vocab_size,
            "score_matrix_shape": list(score_matrix.shape),
            "target_removed_cutoff_status_counts": {
                key: int(value) for key, value in primary_counts.items()
            },
            "all_token_cutoff_status_counts": {
                key: int(value) for key, value in all_token_counts.items()
            },
            "accepted_candidate_neighbor_rows": int(len(candidate_neighbors)),
            "contextual_prompt_matrix_shape": list(contextual_scores.shape),
        }
        add_component_success(manifest, current_component, component_started)
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now_iso()
        write_manifest()

        print(f"Run:                {run_id}")
        print(f"Status:             {manifest['status']}")
        print(f"Source run:         {SOURCE_RUN_ID}")
        print(f"Vocabulary scores:  {tuple(score_matrix.shape)}")
        print(f"Target-removed:     {manifest['results']['target_removed_cutoff_status_counts']}")
        print(f"All tokens:         {manifest['results']['all_token_cutoff_status_counts']}")
        print(f"Output:             {run_dir}")
    except Exception as error:
        manifest["status"] = "failed"
        manifest["completed_at"] = utc_now_iso()
        manifest["components"][current_component] = {
            "status": "failed",
            "completed_at": utc_now_iso(),
            "error_type": type(error).__name__,
            "error": str(error),
        }
        write_manifest()
        raise


if __name__ == "__main__":
    main()
