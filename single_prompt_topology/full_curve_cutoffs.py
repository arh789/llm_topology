from __future__ import annotations

import argparse
import hashlib
import json
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
from safetensors.numpy import load_file


RUN_NUMBER = "R004"
RUN_NAME = "lithium-full-curve-cutoffs"
SOURCE_RUN_ID = (
    "R002_lithium-static-basis-cutoff-feasibility__"
    "20261112T083025Z_pythia-6.9b_52ff8f97c2"
)
CORRECTS_RUN_ID = (
    "R003_lithium-score-region-boundaries__"
    "20261112T090711Z_pythia-6.9b_52ff8f97c2"
)
EXPECTED_ULTIMATE_SOURCE_RUN_ID = (
    "R001_lithium-initial-output-inspection__"
    "20261112T063540Z_pythia-6.9b_52ff8f97c2"
)
EXPECTED_PROMPT_SHA256 = (
    "52ff8f97c22b72506ca9b7acfb9be4450726157f1a31c6a4ce3e112380cd7bf7"
)
EXPECTED_TARGET_TOKEN_ID = 27747
EXPECTED_SCORE_SHAPE = (33, 50277)
BOUNDARY_BAND_SIZE = 50
SELECTED_STATES = (0, 8, 16, 24, 32)

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUNS_DIR = PIPELINE_DIR / "runs"
SOURCE_RUN_DIR = RUNS_DIR / SOURCE_RUN_ID
PLAN_PATH = PIPELINE_DIR / "R004_PLAN.md"
REQUIRED_SOURCE_ARTIFACTS = (
    "vocabulary_scores.safetensors",
    "vocabulary_tokens.csv",
    "state_metadata.csv",
)

REGION_CODE_TO_LABEL = {
    -1: "negative_tail",
    0: "central_body",
    1: "positive_head",
    2: "excluded_exact_target",
}


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


def elbow_candidate(sorted_values: np.ndarray) -> dict[str, float | int]:
    values = np.asarray(sorted_values, dtype=np.float64)
    if values.ndim != 1 or values.size < 5:
        raise ValueError("Elbow input must be a one-dimensional array of at least 5 values.")
    if not np.isfinite(values).all():
        raise ValueError("Elbow input contains non-finite values.")
    if np.any(np.diff(values) > np.finfo(np.float64).eps * 16):
        raise ValueError("Elbow input must be sorted in descending order.")

    score_range = float(values[0] - values[-1])
    if score_range <= np.finfo(np.float64).eps:
        raise ValueError("Elbow input has no usable score range.")

    x = np.linspace(0.0, 1.0, values.size, dtype=np.float64)
    normalized_scores = (values - values[-1]) / score_range
    deviation = (1.0 - x) - normalized_scores
    elbow_index = int(np.argmax(deviation))
    strength = float(deviation[elbow_index])
    if elbow_index < 1 or elbow_index >= values.size - 1 or strength <= 0.0:
        raise ValueError("The full distribution did not produce a valid interior elbow.")

    gaps = values[:-1] - values[1:]
    positive_gaps = gaps[gaps > 0]
    baseline_gap = float(np.median(positive_gaps)) if positive_gaps.size else 0.0
    score_gap = float(gaps[elbow_index])
    return {
        "cutoff_rank": elbow_index + 1,
        "cutoff_score": float(values[elbow_index]),
        "elbow_strength": strength,
        "score_gap_after": score_gap,
        "gap_ratio": score_gap / baseline_gap if baseline_gap > 0 else np.nan,
    }


def local_slope_diagnostic(
    sorted_values: np.ndarray,
    cutoff_rank: int,
) -> tuple[float, float, float]:
    values = np.asarray(sorted_values, dtype=np.float64)
    boundary_index = cutoff_rank - 1
    gaps = values[:-1] - values[1:]
    before = gaps[max(0, boundary_index - BOUNDARY_BAND_SIZE) : boundary_index]
    after = gaps[
        boundary_index : min(gaps.size, boundary_index + BOUNDARY_BAND_SIZE)
    ]
    before = before[before >= 0]
    after = after[after >= 0]
    if before.size == 0 or after.size == 0:
        return np.nan, np.nan, np.nan
    before_median = float(np.median(before))
    after_median = float(np.median(after))
    ratio = before_median / after_median if after_median > 0 else np.nan
    return before_median, after_median, ratio


def assign_regions_by_rank(
    vocabulary_size: int,
    target_token_id: int,
    descending_ids: np.ndarray,
    ascending_ids: np.ndarray,
    upper_cutoff_rank: int,
    lower_cutoff_rank: int,
) -> np.ndarray:
    codes = np.zeros(vocabulary_size, dtype=np.int8)
    codes[target_token_id] = 2
    positive_ids = descending_ids[:upper_cutoff_rank]
    negative_ids = ascending_ids[:lower_cutoff_rank]
    if np.intersect1d(positive_ids, negative_ids).size:
        raise RuntimeError("The upper and lower cutoff regions overlap.")
    codes[positive_ids] = 1
    codes[negative_ids] = -1
    return codes


def boundary_band_records(
    *,
    state_index: int,
    state_type: str,
    state_label: str,
    cutoff_kind: str,
    sorted_token_ids: np.ndarray,
    sorted_original_scores: np.ndarray,
    cutoff_rank: int,
    vocabulary: pd.DataFrame,
) -> list[dict]:
    records: list[dict] = []
    for side, start, stop in (
        ("inside_tail", max(0, cutoff_rank - BOUNDARY_BAND_SIZE), cutoff_rank),
        (
            "outside_tail",
            cutoff_rank,
            min(sorted_token_ids.size, cutoff_rank + BOUNDARY_BAND_SIZE),
        ),
    ):
        for position in range(start, stop):
            token_id = int(sorted_token_ids[position])
            token = vocabulary.loc[token_id]
            records.append(
                {
                    "state_index": state_index,
                    "state_type": state_type,
                    "state_label": state_label,
                    "cutoff_kind": cutoff_kind,
                    "cutoff_side": side,
                    "cutoff_rank": cutoff_rank,
                    "rank_in_cutoff_direction": position + 1,
                    "rank_offset": position + 1 - cutoff_rank,
                    "token_id": token_id,
                    "raw_token": token["raw_token"],
                    "decoded_token": token["decoded_token"],
                    "token_class": token["token_class"],
                    "is_target_lexical_variant": token[
                        "is_target_lexical_variant"
                    ],
                    "cosine_score": float(sorted_original_scores[position]),
                }
            )
    return records


def add_component_success(manifest: dict, component: str, started: float) -> None:
    manifest["components"][component] = {
        "status": "successful",
        "completed_at": utc_now_iso(),
        "seconds": time.perf_counter() - started,
    }


def plot_cutoff_overview(cutoffs: pd.DataFrame, output_path: Path) -> None:
    states = cutoffs["state_index"].to_numpy()
    figure, axes = plt.subplots(2, 1, figsize=(13, 9), sharex=True)
    axes[0].plot(
        states,
        cutoffs["upper_cutoff_rank"],
        marker="o",
        color="#2563eb",
        label="upper cutoff rank",
    )
    axes[0].plot(
        states,
        cutoffs["lower_cutoff_rank"],
        marker="o",
        color="#7c3aed",
        label="lower cutoff rank from negative end",
    )
    axes[0].set_ylabel("Included-token rank")
    axes[0].set_title("Full-curve elbow cutoffs")
    axes[0].legend(frameon=False)

    axes[1].plot(
        states,
        cutoffs["positive_head_count"],
        color="#2a9d8f",
        label="positive head",
    )
    axes[1].plot(
        states,
        cutoffs["central_body_count"],
        color="#6b7280",
        label="central body",
    )
    axes[1].plot(
        states,
        cutoffs["negative_tail_count"],
        color="#7c3aed",
        label="negative tail",
    )
    axes[1].set_xlabel("Recorded state index")
    axes[1].set_ylabel("Assigned token count")
    axes[1].set_title("Unconditionally assigned regions")
    axes[1].legend(frameon=False, ncol=3)
    for axis in axes:
        axis.grid(True, color="#e5e7eb", linewidth=0.7)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_selected_regions(
    scores: np.ndarray,
    target_token_id: int,
    cutoffs: pd.DataFrame,
    output_path: Path,
) -> None:
    retained_ids = np.arange(scores.shape[1], dtype=np.int64)
    retained_ids = retained_ids[retained_ids != target_token_id]
    figure, axes = plt.subplots(2, 3, figsize=(18, 10))
    flat_axes = axes.ravel()
    for axis, state_index in zip(flat_axes, SELECTED_STATES):
        sorted_scores = np.sort(scores[state_index, retained_ids])[::-1]
        ranks = np.arange(1, sorted_scores.size + 1)
        row = cutoffs.loc[cutoffs["state_index"] == state_index].iloc[0]
        upper_rank = int(row["upper_cutoff_rank"])
        lower_rank = int(row["lower_cutoff_rank"])
        lower_position_from_high = sorted_scores.size - lower_rank + 1
        axis.plot(ranks, sorted_scores, color="#2563eb", linewidth=1.1)
        axis.axvspan(1, upper_rank, color="#2a9d8f", alpha=0.10)
        axis.axvline(
            upper_rank,
            color="#2a9d8f",
            linewidth=1.4,
            label=f"upper cutoff {upper_rank:,}",
        )
        axis.axvspan(
            lower_position_from_high,
            sorted_scores.size,
            color="#7c3aed",
            alpha=0.10,
        )
        axis.axvline(
            lower_position_from_high,
            color="#7c3aed",
            linewidth=1.4,
            label=f"lower cutoff {lower_rank:,} from low",
        )
        axis.axhline(0, color="#9ca3af", linewidth=0.7)
        axis.set_title(
            f"State {state_index}: {row['state_label']}",
            loc="left",
            fontsize=10,
        )
        axis.set_xlabel("Vocabulary rank from positive end")
        axis.set_ylabel("Cosine similarity")
        axis.grid(True, color="#e5e7eb", linewidth=0.6)
        axis.legend(frameon=False, fontsize=8, loc="upper right")
    flat_axes[-1].axis("off")
    figure.suptitle(
        "R004 full-curve score regions — exact target removed, linear rank",
        fontsize=16,
    )
    figure.tight_layout(rect=(0, 0, 1, 0.97))
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def run_self_tests() -> None:
    synthetic = np.concatenate(
        [
            np.linspace(1.0, 0.55, 20, endpoint=True),
            np.linspace(0.549, 0.50, 80, endpoint=True),
        ]
    )
    candidate = elbow_candidate(synthetic)
    assert 15 <= int(candidate["cutoff_rank"]) <= 25
    codes = assign_regions_by_rank(
        vocabulary_size=7,
        target_token_id=3,
        descending_ids=np.array([0, 1, 2, 4, 5, 6]),
        ascending_ids=np.array([6, 5, 4, 2, 1, 0]),
        upper_cutoff_rank=2,
        lower_cutoff_rank=2,
    )
    assert codes.tolist() == [1, 1, 0, 2, 0, -1, -1]
    print("R004 synthetic self-tests passed.")


def main() -> None:
    validate_run_identity()
    if not SOURCE_RUN_DIR.is_dir():
        raise FileNotFoundError(f"Source run not found: {SOURCE_RUN_DIR}")
    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"R004 pre-run plan not found: {PLAN_PATH}")

    source_manifest_path = SOURCE_RUN_DIR / "manifest.json"
    source_manifest = load_json(source_manifest_path)
    model_id = source_manifest["model"]["id"]
    model_revision = source_manifest["model"]["revision"]
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
        "cutoff_calculation",
        "region_membership",
        "figures",
        "validation",
    ]
    manifest = {
        "run_number": RUN_NUMBER,
        "run_name": RUN_NAME,
        "run_id": run_id,
        "technical_id": technical_id,
        "source_run": SOURCE_RUN_ID,
        "corrects_run": CORRECTS_RUN_ID,
        "ultimate_source_run": source_manifest.get("source_run"),
        "status": "running",
        "started_at": started_at.isoformat(),
        "completed_at": None,
        "required_components": required_components,
        "components": {name: {"status": "pending"} for name in required_components},
        "model": {
            "id": model_id,
            "revision": model_revision,
            "model_forward_executed": False,
            "model_weights_loaded": False,
            "source_score_matrix_recalculated": False,
        },
        "input": source_manifest["input"],
        "pipeline": {
            "script": str(pipeline_path.relative_to(PROJECT_DIR)),
            "script_sha256": sha256_file(pipeline_path),
            "pre_run_plan": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace(
                "\\", "/"
            ),
            "pre_run_plan_sha256": sha256_file(PLAN_PATH),
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "matplotlib": matplotlib.__version__,
            "safetensors": safetensors.__version__,
            "device": "cpu",
        },
        "method": {
            "metric": "cosine_similarity from the reused R002 score matrix",
            "algorithm": "maximum normalized deviation below endpoint chord",
            "exact_target_removed": True,
            "upper_cutoff": "complete score distribution ranked descending",
            "lower_cutoff": (
                "complete score distribution ranked ascending and negated for "
                "descending anti-alignment magnitude"
            ),
            "membership_rule": "exact rank membership from each distribution end",
            "secondary_acceptance_gate": None,
            "agreement_tolerance": None,
            "sign_restricted_candidates": False,
            "boundary_band_size": BOUNDARY_BAND_SIZE,
            "interpretation_boundary": (
                "Cutoffs are geometric elbows in static-input-basis compatibility, "
                "not validated semantic boundaries. Negative cosine means "
                "anti-alignment, not predictive or causal suppression."
            ),
        },
        "source_artifacts": {},
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
            raise RuntimeError("R002 source manifest is not successful.")
        if source_manifest.get("run_id") != SOURCE_RUN_ID:
            raise RuntimeError("R002 source manifest run identity does not match.")
        if source_manifest.get("source_run") != EXPECTED_ULTIMATE_SOURCE_RUN_ID:
            raise RuntimeError("R002 ultimate source run does not match the R004 plan.")
        if prompt_hash != EXPECTED_PROMPT_SHA256:
            raise RuntimeError("R002 prompt hash does not match the R004 plan.")
        if int(source_manifest["input"]["target_token_id"]) != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("R002 target token does not match the R004 plan.")
        if tuple(source_manifest["results"]["score_matrix_shape"]) != EXPECTED_SCORE_SHAPE:
            raise RuntimeError("R002 score shape does not match the R004 plan.")

        for relative_path in REQUIRED_SOURCE_ARTIFACTS:
            expected = source_manifest["artifacts"][relative_path]
            source_path = SOURCE_RUN_DIR / relative_path
            if not source_path.is_file():
                raise FileNotFoundError(f"Missing R002 source artifact: {source_path}")
            if source_path.stat().st_size != expected["bytes"]:
                raise RuntimeError(f"R002 artifact size mismatch: {relative_path}")
            if sha256_file(source_path) != expected["sha256"]:
                raise RuntimeError(f"R002 artifact hash mismatch: {relative_path}")
            manifest["source_artifacts"][relative_path] = expected

        scores = load_file(SOURCE_RUN_DIR / "vocabulary_scores.safetensors")[
            "cosine_scores"
        ]
        vocabulary = pd.read_csv(SOURCE_RUN_DIR / "vocabulary_tokens.csv")
        states = pd.read_csv(SOURCE_RUN_DIR / "state_metadata.csv")
        if scores.shape != EXPECTED_SCORE_SHAPE or not np.isfinite(scores).all():
            raise RuntimeError("R002 score matrix failed shape or finite-value validation.")
        if scores.min() < -1.0001 or scores.max() > 1.0001:
            raise RuntimeError("R002 cosine scores are outside the valid range.")
        if len(vocabulary) != scores.shape[1] or len(states) != scores.shape[0]:
            raise RuntimeError("R002 metadata dimensions do not match the score matrix.")
        expected_ids = np.arange(scores.shape[1], dtype=np.int64)
        if not np.array_equal(vocabulary["token_id"].to_numpy(), expected_ids):
            raise RuntimeError("R002 vocabulary IDs are not contiguous score columns.")
        if not np.array_equal(states["state_index"].to_numpy(), np.arange(scores.shape[0])):
            raise RuntimeError("R002 state indices are not contiguous.")
        if int(vocabulary["is_exact_target"].sum()) != 1:
            raise RuntimeError("R002 vocabulary table must contain one exact target.")
        exact_target_id = int(
            vocabulary.loc[vocabulary["is_exact_target"], "token_id"].iloc[0]
        )
        if exact_target_id != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("R002 exact target row does not match the manifest.")
        vocabulary = vocabulary.set_index("token_id", drop=False)
        states = states.set_index("state_index", drop=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "score_shape": list(scores.shape),
                "validated_source_artifact_count": len(REQUIRED_SOURCE_ARTIFACTS),
            }
        )
        write_manifest()

        current_component = "cutoff_calculation"
        component_started = time.perf_counter()
        token_ids = np.arange(scores.shape[1], dtype=np.int64)
        retained_ids = token_ids[token_ids != EXPECTED_TARGET_TOKEN_ID]
        state_count, vocabulary_size = scores.shape
        retained_count = retained_ids.size
        region_codes = np.zeros((state_count, vocabulary_size), dtype=np.int8)
        region_codes[:, EXPECTED_TARGET_TOKEN_ID] = 2
        rank_from_high = np.zeros((state_count, vocabulary_size), dtype=np.int32)
        rank_from_low = np.zeros((state_count, vocabulary_size), dtype=np.int32)
        cutoff_records: list[dict] = []
        cutoff_token_records: list[dict] = []

        for state_index in range(state_count):
            state = states.loc[state_index]
            state_scores = scores[state_index]
            retained_scores = state_scores[retained_ids]
            descending_order = np.argsort(-retained_scores, kind="stable")
            descending_ids = retained_ids[descending_order]
            descending_scores = retained_scores[descending_order]
            ascending_order = np.argsort(retained_scores, kind="stable")
            ascending_ids = retained_ids[ascending_order]
            ascending_scores = retained_scores[ascending_order]
            rank_from_high[state_index, descending_ids] = np.arange(
                1, retained_count + 1, dtype=np.int32
            )
            rank_from_low[state_index, ascending_ids] = np.arange(
                1, retained_count + 1, dtype=np.int32
            )

            upper = elbow_candidate(descending_scores)
            lower = elbow_candidate(-ascending_scores)
            upper_rank = int(upper["cutoff_rank"])
            lower_rank = int(lower["cutoff_rank"])
            upper_before, upper_after, upper_slope_ratio = local_slope_diagnostic(
                descending_scores, upper_rank
            )
            lower_before, lower_after, lower_slope_ratio = local_slope_diagnostic(
                -ascending_scores, lower_rank
            )
            codes = assign_regions_by_rank(
                vocabulary_size,
                EXPECTED_TARGET_TOKEN_ID,
                descending_ids,
                ascending_ids,
                upper_rank,
                lower_rank,
            )
            region_codes[state_index] = codes
            positive_count = int(np.sum(codes == 1))
            negative_count = int(np.sum(codes == -1))
            central_count = int(np.sum(codes == 0))
            if positive_count + central_count + negative_count != retained_count:
                raise RuntimeError(f"Region counts do not reconcile at state {state_index}.")

            cutoff_records.append(
                {
                    "state_index": state_index,
                    "state_type": state["state_type"],
                    "state_label": state["state_label"],
                    "valid_token_count": retained_count,
                    "upper_cutoff_rank": upper_rank,
                    "upper_cutoff_score": float(upper["cutoff_score"]),
                    "upper_elbow_strength": float(upper["elbow_strength"]),
                    "upper_score_gap_after": float(upper["score_gap_after"]),
                    "upper_gap_ratio": float(upper["gap_ratio"]),
                    "upper_local_gap_before": upper_before,
                    "upper_local_gap_after": upper_after,
                    "upper_local_slope_ratio": upper_slope_ratio,
                    "lower_cutoff_rank": lower_rank,
                    "lower_cutoff_score": -float(lower["cutoff_score"]),
                    "lower_elbow_strength": float(lower["elbow_strength"]),
                    "lower_score_gap_after": float(lower["score_gap_after"]),
                    "lower_gap_ratio": float(lower["gap_ratio"]),
                    "lower_local_gap_before": lower_before,
                    "lower_local_gap_after": lower_after,
                    "lower_local_slope_ratio": lower_slope_ratio,
                    "positive_head_count": positive_count,
                    "positive_head_percent": positive_count / retained_count * 100,
                    "central_body_count": central_count,
                    "central_body_percent": central_count / retained_count * 100,
                    "negative_tail_count": negative_count,
                    "negative_tail_percent": negative_count / retained_count * 100,
                    "combined_tail_count": positive_count + negative_count,
                    "combined_tail_percent": (
                        (positive_count + negative_count) / retained_count * 100
                    ),
                }
            )
            cutoff_token_records.extend(
                boundary_band_records(
                    state_index=state_index,
                    state_type=str(state["state_type"]),
                    state_label=str(state["state_label"]),
                    cutoff_kind="upper",
                    sorted_token_ids=descending_ids,
                    sorted_original_scores=descending_scores,
                    cutoff_rank=upper_rank,
                    vocabulary=vocabulary,
                )
            )
            cutoff_token_records.extend(
                boundary_band_records(
                    state_index=state_index,
                    state_type=str(state["state_type"]),
                    state_label=str(state["state_label"]),
                    cutoff_kind="lower",
                    sorted_token_ids=ascending_ids,
                    sorted_original_scores=ascending_scores,
                    cutoff_rank=lower_rank,
                    vocabulary=vocabulary,
                )
            )

        cutoffs = pd.DataFrame(cutoff_records)
        cutoff_tokens = pd.DataFrame(cutoff_token_records)
        cutoffs_path = run_dir / "cutoffs.csv"
        cutoff_tokens_path = run_dir / "cutoff_tokens.csv"
        cutoffs.to_csv(cutoffs_path, index=False)
        cutoff_tokens.to_csv(cutoff_tokens_path, index=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "state_count": state_count,
                "upper_cutoffs_calculated": int(cutoffs["upper_cutoff_rank"].notna().sum()),
                "lower_cutoffs_calculated": int(cutoffs["lower_cutoff_rank"].notna().sum()),
                "secondary_acceptance_gate": False,
            }
        )
        write_manifest()

        current_component = "region_membership"
        component_started = time.perf_counter()
        tail_frames: list[pd.DataFrame] = []
        for state_index in range(state_count):
            selected_ids = np.flatnonzero(np.abs(region_codes[state_index]) == 1)
            frame = vocabulary.loc[selected_ids].copy()
            codes = region_codes[state_index, selected_ids]
            frame.insert(0, "state_index", state_index)
            frame.insert(1, "state_type", states.loc[state_index, "state_type"])
            frame.insert(2, "state_label", states.loc[state_index, "state_label"])
            frame["region"] = [REGION_CODE_TO_LABEL[int(code)] for code in codes]
            frame["cosine_score"] = scores[state_index, selected_ids]
            frame["rank_from_high"] = rank_from_high[state_index, selected_ids]
            frame["rank_from_low"] = rank_from_low[state_index, selected_ids]
            tail_frames.append(frame.reset_index(drop=True))

        tail_columns = [
            "state_index",
            "state_type",
            "state_label",
            "token_id",
            "raw_token",
            "decoded_token",
            "token_class",
            "is_exact_target",
            "is_target_lexical_variant",
            "region",
            "cosine_score",
            "rank_from_high",
            "rank_from_low",
        ]
        tails = pd.concat(tail_frames, ignore_index=True)[tail_columns]
        tails_path = run_dir / "tail_tokens.csv.gz"
        tails.to_csv(tails_path, index=False, compression="gzip")

        union_tail_ids = np.flatnonzero(
            np.any(np.abs(region_codes) == 1, axis=0)
        ).astype(np.int64)
        trajectory_frames: list[pd.DataFrame] = []
        previous_labels: np.ndarray | None = None
        for state_index in range(state_count):
            codes = region_codes[state_index, union_tail_ids]
            labels = np.array(
                [REGION_CODE_TO_LABEL[int(code)] for code in codes], dtype=object
            )
            frame = vocabulary.loc[union_tail_ids].copy()
            frame.insert(0, "state_index", state_index)
            frame.insert(1, "state_type", states.loc[state_index, "state_type"])
            frame.insert(2, "state_label", states.loc[state_index, "state_label"])
            frame["region"] = labels
            frame["cosine_score"] = scores[state_index, union_tail_ids]
            frame["rank_from_high"] = rank_from_high[state_index, union_tail_ids]
            frame["rank_from_low"] = rank_from_low[state_index, union_tail_ids]
            if previous_labels is None:
                frame["previous_region"] = ""
                frame["region_changed"] = False
            else:
                frame["previous_region"] = previous_labels
                frame["region_changed"] = labels != previous_labels
            trajectory_frames.append(frame.reset_index(drop=True))
            previous_labels = labels.copy()

        trajectory_columns = tail_columns + ["previous_region", "region_changed"]
        trajectories = pd.concat(trajectory_frames, ignore_index=True)[
            trajectory_columns
        ]
        trajectories_path = run_dir / "token_region_trajectories.csv.gz"
        trajectories.to_csv(trajectories_path, index=False, compression="gzip")
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "tail_membership_rows": int(len(tails)),
                "trajectory_token_count": int(union_tail_ids.size),
                "trajectory_rows": int(len(trajectories)),
            }
        )
        write_manifest()

        current_component = "figures"
        component_started = time.perf_counter()
        overview_figure_path = figures_dir / "cutoff_overview.png"
        selected_figure_path = figures_dir / "score_regions_selected_states.png"
        plot_cutoff_overview(cutoffs, overview_figure_path)
        plot_selected_regions(
            scores,
            EXPECTED_TARGET_TOKEN_ID,
            cutoffs,
            selected_figure_path,
        )
        add_component_success(manifest, current_component, component_started)
        write_manifest()

        current_component = "validation"
        component_started = time.perf_counter()
        artifact_paths = [
            cutoffs_path,
            cutoff_tokens_path,
            tails_path,
            trajectories_path,
            overview_figure_path,
            selected_figure_path,
        ]
        if len(cutoffs) != state_count:
            raise RuntimeError("Cutoff table has the wrong state count.")
        if cutoffs[["upper_cutoff_rank", "lower_cutoff_rank"]].isna().any().any():
            raise RuntimeError("A state is missing an upper or lower cutoff.")
        if not (cutoffs["positive_head_count"] == cutoffs["upper_cutoff_rank"]).all():
            raise RuntimeError("Positive-head membership does not match cutoff ranks.")
        if not (cutoffs["negative_tail_count"] == cutoffs["lower_cutoff_rank"]).all():
            raise RuntimeError("Negative-tail membership does not match cutoff ranks.")
        if not (
            cutoffs["positive_head_count"]
            + cutoffs["central_body_count"]
            + cutoffs["negative_tail_count"]
            == retained_count
        ).all():
            raise RuntimeError("Persisted region population counts do not reconcile.")
        expected_tail_rows = int(cutoffs["combined_tail_count"].sum())
        if len(tails) != expected_tail_rows:
            raise RuntimeError("Tail-token rows do not match cutoff population counts.")
        if len(cutoff_tokens) != state_count * 2 * BOUNDARY_BAND_SIZE * 2:
            raise RuntimeError("Cutoff-token inspection table has the wrong row count.")
        expected_trajectory_rows = int(union_tail_ids.size * state_count)
        if len(trajectories) != expected_trajectory_rows:
            raise RuntimeError("Trajectory rows do not cover every selected token and state.")
        for path in artifact_paths:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"Required R004 artifact is absent or empty: {path}")

        manifest["artifacts"] = {
            str(path.relative_to(run_dir)).replace("\\", "/"): artifact_record(path)
            for path in artifact_paths
        }
        manifest["results"] = {
            "state_count": state_count,
            "valid_vocabulary_size": vocabulary_size,
            "target_removed_vocabulary_size": retained_count,
            "source_score_matrix_shape": list(scores.shape),
            "upper_cutoffs_calculated": state_count,
            "lower_cutoffs_calculated": state_count,
            "states_with_two_cutoffs": state_count,
            "tail_membership_rows": int(len(tails)),
            "trajectory_token_count": int(union_tail_ids.size),
            "trajectory_rows": int(len(trajectories)),
        }
        add_component_success(manifest, current_component, component_started)
        manifest["status"] = "successful"
        manifest["completed_at"] = utc_now_iso()
        write_manifest()

        print(f"Run:                    {run_id}")
        print(f"Status:                 {manifest['status']}")
        print(f"Source run:             {SOURCE_RUN_ID}")
        print(f"Score matrix reused:    {tuple(scores.shape)}")
        print(f"Upper cutoffs:          {state_count}/{state_count}")
        print(f"Lower cutoffs:          {state_count}/{state_count}")
        print(f"Tail membership rows:   {len(tails)}")
        print(f"Trajectory tokens:      {union_tail_ids.size}")
        print(f"Output:                 {run_dir}")
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
    parser = argparse.ArgumentParser(
        description="R004 unconditional full-curve cutoff analysis"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run synthetic validation without creating an R004 run directory.",
    )
    arguments = parser.parse_args()
    if arguments.self_test:
        run_self_tests()
    else:
        main()
