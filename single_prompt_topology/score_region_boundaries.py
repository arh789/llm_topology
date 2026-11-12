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


RUN_NUMBER = "R003"
RUN_NAME = "lithium-score-region-boundaries"
SOURCE_RUN_ID = (
    "R002_lithium-static-basis-cutoff-feasibility__"
    "20261112T083025Z_pythia-6.9b_52ff8f97c2"
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
AGREEMENT_TOLERANCE = 0.20
BOUNDARY_BAND_SIZE = 50
SELECTED_STATES = (0, 8, 16, 24, 32)

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUNS_DIR = PIPELINE_DIR / "runs"
SOURCE_RUN_DIR = RUNS_DIR / SOURCE_RUN_ID
REQUIRED_SOURCE_ARTIFACTS = (
    "vocabulary_scores.safetensors",
    "vocabulary_tokens.csv",
    "state_metadata.csv",
    "cutoff_candidates.csv",
    "cutoff_summary.csv",
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


def elbow_candidate(sorted_values: np.ndarray) -> dict[str, bool | float | int | None]:
    values = np.asarray(sorted_values, dtype=np.float64)
    if values.ndim != 1:
        raise ValueError("Elbow input must be one-dimensional.")
    if values.size < 5:
        return {
            "candidate_valid": False,
            "elbow_rank": None,
            "elbow_score": None,
            "elbow_strength": 0.0,
            "score_gap_after": None,
            "gap_ratio": None,
        }
    if not np.isfinite(values).all():
        raise ValueError("Elbow input contains non-finite values.")
    if np.any(np.diff(values) > np.finfo(np.float64).eps * 16):
        raise ValueError("Elbow input must be sorted in descending order.")

    score_range = float(values[0] - values[-1])
    if score_range <= np.finfo(np.float64).eps:
        return {
            "candidate_valid": False,
            "elbow_rank": None,
            "elbow_score": None,
            "elbow_strength": 0.0,
            "score_gap_after": None,
            "gap_ratio": None,
        }

    x = np.linspace(0.0, 1.0, values.size, dtype=np.float64)
    normalized_scores = (values - values[-1]) / score_range
    deviation = (1.0 - x) - normalized_scores
    elbow_index = int(np.argmax(deviation))
    strength = float(deviation[elbow_index])

    if elbow_index < 1 or elbow_index >= values.size - 1 or strength <= 0.0:
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


def boundary_agreement(
    full_candidate: dict,
    restricted_candidate: dict,
) -> tuple[str, float | None, str]:
    if not full_candidate["candidate_valid"]:
        return "rejected_unstable", None, "Full-distribution candidate is invalid."
    if not restricted_candidate["candidate_valid"]:
        return "rejected_unstable", None, "Sign-restricted candidate is invalid."

    full_rank = float(full_candidate["elbow_rank"])
    restricted_rank = float(restricted_candidate["elbow_rank"])
    median_rank = float(np.median([full_rank, restricted_rank]))
    relative_difference = abs(full_rank - restricted_rank) / median_rank
    if relative_difference <= AGREEMENT_TOLERANCE:
        return (
            "accepted_geometric",
            relative_difference,
            "Candidate ranks agree within the predeclared tolerance.",
        )
    return (
        "rejected_unstable",
        relative_difference,
        "Candidate ranks exceed the predeclared agreement tolerance.",
    )


def local_slope_diagnostic(
    sorted_values: np.ndarray,
    elbow_rank: int | None,
    band_size: int = BOUNDARY_BAND_SIZE,
) -> tuple[float | None, float | None, float | None]:
    if elbow_rank is None:
        return None, None, None
    values = np.asarray(sorted_values, dtype=np.float64)
    boundary_index = int(elbow_rank) - 1
    gaps = values[:-1] - values[1:]
    before = gaps[max(0, boundary_index - band_size) : boundary_index]
    after = gaps[boundary_index : min(gaps.size, boundary_index + band_size)]
    before = before[before >= 0]
    after = after[after >= 0]
    if before.size == 0 or after.size == 0:
        return None, None, None
    before_median = float(np.median(before))
    after_median = float(np.median(after))
    ratio = before_median / after_median if after_median > 0 else None
    return before_median, after_median, ratio


def candidate_from_r002_row(row: pd.Series) -> dict:
    valid = bool(row["candidate_valid"])
    return {
        "candidate_valid": valid,
        "elbow_rank": int(row["elbow_rank"]) if valid else None,
        "elbow_score": float(row["elbow_score"]) if valid else None,
        "elbow_strength": float(row["elbow_strength"]),
        "score_gap_after": (
            float(row["score_gap_after"])
            if valid and pd.notna(row["score_gap_after"])
            else None
        ),
        "gap_ratio": (
            float(row["gap_ratio"])
            if valid and pd.notna(row["gap_ratio"])
            else None
        ),
    }


def state_region_result(upper_decision: str, lower_decision: str) -> str:
    upper = upper_decision == "accepted_geometric"
    lower = lower_decision == "accepted_geometric"
    if upper and lower:
        return "accepted_two_boundaries"
    if upper:
        return "accepted_upper_only"
    if lower:
        return "accepted_lower_only"
    return "rejected_unstable"


def assign_regions(
    scores: np.ndarray,
    target_token_id: int,
    upper_decision: str,
    upper_threshold: float | None,
    lower_decision: str,
    lower_threshold: float | None,
) -> np.ndarray:
    codes = np.zeros(scores.size, dtype=np.int8)
    codes[target_token_id] = 2
    if upper_decision == "accepted_geometric":
        if upper_threshold is None:
            raise ValueError("Accepted upper boundary is missing its threshold.")
        codes[(scores >= upper_threshold) & (np.arange(scores.size) != target_token_id)] = 1
    if lower_decision == "accepted_geometric":
        if lower_threshold is None:
            raise ValueError("Accepted lower boundary is missing its threshold.")
        lower_mask = (scores <= lower_threshold) & (
            np.arange(scores.size) != target_token_id
        )
        if np.any((codes == 1) & lower_mask):
            raise RuntimeError("Accepted upper and lower regions overlap.")
        codes[lower_mask] = -1
    return codes


def boundary_band_records(
    *,
    state_index: int,
    state_type: str,
    state_label: str,
    boundary_kind: str,
    decision: str,
    sorted_token_ids: np.ndarray,
    sorted_original_scores: np.ndarray,
    elbow_rank: int | None,
    vocabulary: pd.DataFrame,
) -> list[dict]:
    if elbow_rank is None:
        return []
    rank = int(elbow_rank)
    inside_start = max(0, rank - BOUNDARY_BAND_SIZE)
    inside_stop = rank
    outside_start = rank
    outside_stop = min(sorted_token_ids.size, rank + BOUNDARY_BAND_SIZE)
    records: list[dict] = []
    for position in range(inside_start, inside_stop):
        token_id = int(sorted_token_ids[position])
        token = vocabulary.loc[token_id]
        records.append(
            {
                "state_index": state_index,
                "state_type": state_type,
                "state_label": state_label,
                "boundary_kind": boundary_kind,
                "boundary_decision": decision,
                "boundary_side": "inside_tail",
                "boundary_rank": rank,
                "rank_in_boundary_direction": position + 1,
                "rank_offset": position + 1 - rank,
                "token_id": token_id,
                "raw_token": token["raw_token"],
                "decoded_token": token["decoded_token"],
                "token_class": token["token_class"],
                "is_target_lexical_variant": token["is_target_lexical_variant"],
                "cosine_score": float(sorted_original_scores[position]),
            }
        )
    for position in range(outside_start, outside_stop):
        token_id = int(sorted_token_ids[position])
        token = vocabulary.loc[token_id]
        records.append(
            {
                "state_index": state_index,
                "state_type": state_type,
                "state_label": state_label,
                "boundary_kind": boundary_kind,
                "boundary_decision": decision,
                "boundary_side": "outside_tail",
                "boundary_rank": rank,
                "rank_in_boundary_direction": position + 1,
                "rank_offset": position + 1 - rank,
                "token_id": token_id,
                "raw_token": token["raw_token"],
                "decoded_token": token["decoded_token"],
                "token_class": token["token_class"],
                "is_target_lexical_variant": token["is_target_lexical_variant"],
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


def plot_boundary_overview(boundaries: pd.DataFrame, output_path: Path) -> None:
    states = boundaries["state_index"].to_numpy()
    figure, axes = plt.subplots(3, 1, figsize=(13, 12), sharex=True)

    axes[0].plot(
        states,
        boundaries["upper_full_rank"],
        marker="o",
        label="full distribution",
        color="#2563eb",
    )
    axes[0].plot(
        states,
        boundaries["upper_positive_only_rank"],
        marker="s",
        label="positive scores only",
        color="#2a9d8f",
    )
    axes[0].set_ylabel("Rank from positive end")
    axes[0].set_title("Upper-boundary candidates")
    axes[0].legend(frameon=False)

    axes[1].plot(
        states,
        boundaries["lower_full_rank"],
        marker="o",
        label="full distribution",
        color="#7c3aed",
    )
    axes[1].plot(
        states,
        boundaries["lower_negative_only_rank"],
        marker="s",
        label="negative scores only",
        color="#e76f51",
    )
    axes[1].set_ylabel("Rank from negative end")
    axes[1].set_title("Lower-boundary candidates")
    axes[1].legend(frameon=False)

    axes[2].plot(
        states,
        boundaries["positive_head_count"],
        label="positive head",
        color="#2a9d8f",
    )
    axes[2].plot(
        states,
        boundaries["central_body_count"],
        label="central body",
        color="#6b7280",
    )
    axes[2].plot(
        states,
        boundaries["negative_tail_count"],
        label="negative tail",
        color="#7c3aed",
    )
    axes[2].set_ylabel("Assigned token count")
    axes[2].set_xlabel("Recorded state index")
    axes[2].set_title("Accepted region populations")
    axes[2].legend(frameon=False, ncol=3)

    for axis in axes:
        axis.grid(True, color="#e5e7eb", linewidth=0.7)
    figure.tight_layout()
    figure.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def plot_selected_regions(
    scores: np.ndarray,
    target_token_id: int,
    boundaries: pd.DataFrame,
    output_path: Path,
) -> None:
    retained_ids = np.arange(scores.shape[1], dtype=np.int64)
    retained_ids = retained_ids[retained_ids != target_token_id]
    figure, axes = plt.subplots(2, 3, figsize=(18, 10), sharey=False)
    flat_axes = axes.ravel()

    for axis, state_index in zip(flat_axes, SELECTED_STATES):
        state_scores = scores[state_index, retained_ids]
        sorted_scores = np.sort(state_scores)[::-1]
        ranks = np.arange(1, sorted_scores.size + 1)
        row = boundaries.loc[boundaries["state_index"] == state_index].iloc[0]
        axis.plot(ranks, sorted_scores, color="#2563eb", linewidth=1.15)

        upper_rank = int(row["upper_full_rank"])
        upper_accepted = row["upper_decision"] == "accepted_geometric"
        axis.axvline(
            upper_rank,
            color="#2a9d8f",
            linestyle="-" if upper_accepted else "--",
            linewidth=1.4,
            label=f"upper {upper_rank:,} ({'accepted' if upper_accepted else 'rejected'})",
        )
        if upper_accepted:
            axis.axvspan(1, upper_rank, color="#2a9d8f", alpha=0.08)

        lower_rank = int(row["lower_full_rank"])
        lower_position_from_high = sorted_scores.size - lower_rank + 1
        lower_accepted = row["lower_decision"] == "accepted_geometric"
        axis.axvline(
            lower_position_from_high,
            color="#7c3aed",
            linestyle="-" if lower_accepted else "--",
            linewidth=1.4,
            label=(
                f"lower {lower_rank:,} from low "
                f"({'accepted' if lower_accepted else 'rejected'})"
            ),
        )
        if lower_accepted:
            axis.axvspan(
                lower_position_from_high,
                sorted_scores.size,
                color="#7c3aed",
                alpha=0.08,
            )

        axis.axhline(0, color="#9ca3af", linewidth=0.7)
        axis.set_title(
            f"State {state_index}: {row['state_label']}\n{row['region_result']}",
            loc="left",
            fontsize=10,
        )
        axis.set_xlabel("Vocabulary rank from positive end")
        axis.set_ylabel("Cosine similarity")
        axis.grid(True, color="#e5e7eb", linewidth=0.6)
        axis.legend(frameon=False, fontsize=7, loc="upper right")

    flat_axes[-1].axis("off")
    figure.suptitle(
        "R003 score regions — exact target removed, linear rank",
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
    assert candidate["candidate_valid"]
    assert 15 <= int(candidate["elbow_rank"]) <= 25

    constant = elbow_candidate(np.ones(10, dtype=np.float64))
    assert not constant["candidate_valid"]

    accepted, difference, _ = boundary_agreement(
        {"candidate_valid": True, "elbow_rank": 100},
        {"candidate_valid": True, "elbow_rank": 110},
    )
    assert accepted == "accepted_geometric"
    assert difference is not None and difference < AGREEMENT_TOLERANCE

    rejected, difference, _ = boundary_agreement(
        {"candidate_valid": True, "elbow_rank": 100},
        {"candidate_valid": True, "elbow_rank": 150},
    )
    assert rejected == "rejected_unstable"
    assert difference is not None and difference > AGREEMENT_TOLERANCE

    scores = np.array([0.8, 0.4, 0.0, -0.2, -0.7], dtype=np.float64)
    regions = assign_regions(
        scores,
        target_token_id=2,
        upper_decision="accepted_geometric",
        upper_threshold=0.4,
        lower_decision="accepted_geometric",
        lower_threshold=-0.2,
    )
    assert regions.tolist() == [1, 1, 2, -1, -1]
    print("R003 synthetic self-tests passed.")


def main() -> None:
    validate_run_identity()
    if not SOURCE_RUN_DIR.is_dir():
        raise FileNotFoundError(f"Source run not found: {SOURCE_RUN_DIR}")

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
        "boundary_analysis",
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
            "pre_run_plan": "single_prompt_topology/R003_PLAN.md",
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
            "agreement_tolerance": AGREEMENT_TOLERANCE,
            "boundary_band_size": BOUNDARY_BAND_SIZE,
            "upper_full_candidate": "reused from R002 exact_target_removed/full",
            "upper_sensitivity_candidate": "scores greater than zero only",
            "lower_full_candidate": "full distribution ranked by -cosine_score",
            "lower_sensitivity_candidate": "scores below zero ranked by -cosine_score",
            "sign_boundary_role": (
                "endpoint-sensitivity partition only; not a statistical, predictive, "
                "or causal threshold"
            ),
            "decisions": [
                "accepted_two_boundaries",
                "accepted_upper_only",
                "accepted_lower_only",
                "rejected_unstable",
            ],
            "interpretation_boundary": (
                "Regions describe layer-wise compatibility between one contextual target "
                "and static input embeddings. Negative cosine means anti-alignment, not "
                "predictive or causal suppression."
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
            raise RuntimeError("R002 ultimate source run does not match the R003 plan.")
        if prompt_hash != EXPECTED_PROMPT_SHA256:
            raise RuntimeError("R002 prompt hash does not match the R003 plan.")
        if int(source_manifest["input"]["target_token_id"]) != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("R002 target token does not match the R003 plan.")
        if tuple(source_manifest["results"]["score_matrix_shape"]) != EXPECTED_SCORE_SHAPE:
            raise RuntimeError("R002 score shape does not match the R003 plan.")

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
        candidates = pd.read_csv(SOURCE_RUN_DIR / "cutoff_candidates.csv")
        cutoff_summary = pd.read_csv(SOURCE_RUN_DIR / "cutoff_summary.csv")

        if scores.shape != EXPECTED_SCORE_SHAPE:
            raise RuntimeError(f"Unexpected score shape: {scores.shape}")
        if not np.isfinite(scores).all():
            raise RuntimeError("R002 vocabulary scores contain non-finite values.")
        if scores.min() < -1.0001 or scores.max() > 1.0001:
            raise RuntimeError("R002 cosine scores are outside the valid range.")
        if len(vocabulary) != scores.shape[1]:
            raise RuntimeError("R002 vocabulary table does not match the score width.")
        expected_ids = np.arange(scores.shape[1], dtype=np.int64)
        if not np.array_equal(vocabulary["token_id"].to_numpy(), expected_ids):
            raise RuntimeError("R002 vocabulary IDs are not contiguous score columns.")
        if len(states) != scores.shape[0]:
            raise RuntimeError("R002 state table does not match the score height.")
        if not np.array_equal(states["state_index"].to_numpy(), np.arange(scores.shape[0])):
            raise RuntimeError("R002 state indices are not contiguous.")
        if int(vocabulary["is_exact_target"].sum()) != 1:
            raise RuntimeError("R002 vocabulary table must contain one exact target.")
        exact_target_id = int(
            vocabulary.loc[vocabulary["is_exact_target"], "token_id"].iloc[0]
        )
        if exact_target_id != EXPECTED_TARGET_TOKEN_ID:
            raise RuntimeError("R002 exact target row does not match the manifest.")

        full_upper_rows = candidates[
            (candidates["variant"] == "exact_target_removed")
            & (candidates["window_label"] == "full")
        ].copy()
        if len(full_upper_rows) != scores.shape[0]:
            raise RuntimeError("R002 does not contain one reusable full elbow per state.")
        if full_upper_rows["state_index"].nunique() != scores.shape[0]:
            raise RuntimeError("R002 reusable full elbows have duplicate state indices.")
        if not full_upper_rows["candidate_valid"].all():
            raise RuntimeError("R002 contains an invalid reusable full upper elbow.")
        full_upper_rows = full_upper_rows.set_index("state_index")

        target_removed_summary = cutoff_summary[
            cutoff_summary["variant"] == "exact_target_removed"
        ]
        if len(target_removed_summary) != scores.shape[0]:
            raise RuntimeError("R002 target-removed summary has the wrong state count.")

        vocabulary = vocabulary.set_index("token_id", drop=False)
        states = states.set_index("state_index", drop=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "score_shape": list(scores.shape),
                "validated_source_artifact_count": len(REQUIRED_SOURCE_ARTIFACTS),
                "source_status": source_manifest["status"],
            }
        )
        write_manifest()

        current_component = "boundary_analysis"
        component_started = time.perf_counter()
        token_ids = np.arange(scores.shape[1], dtype=np.int64)
        retained_ids = token_ids[token_ids != EXPECTED_TARGET_TOKEN_ID]
        state_count = scores.shape[0]
        vocab_size = scores.shape[1]
        retained_count = retained_ids.size
        region_codes = np.zeros((state_count, vocab_size), dtype=np.int8)
        region_codes[:, EXPECTED_TARGET_TOKEN_ID] = 2
        rank_from_high = np.zeros((state_count, vocab_size), dtype=np.int32)
        rank_from_low = np.zeros((state_count, vocab_size), dtype=np.int32)
        boundary_records: list[dict] = []
        boundary_token_records: list[dict] = []

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

            upper_full = candidate_from_r002_row(full_upper_rows.loc[state_index])
            upper_full_rank = int(upper_full["elbow_rank"])
            actual_upper_score = float(descending_scores[upper_full_rank - 1])
            if not np.isclose(
                actual_upper_score,
                float(upper_full["elbow_score"]),
                rtol=0.0,
                atol=1e-7,
            ):
                raise RuntimeError(
                    f"R002 upper elbow score mismatch at state {state_index}."
                )

            positive_scores = descending_scores[descending_scores > 0]
            upper_positive_only = elbow_candidate(positive_scores)
            upper_decision, upper_relative_difference, upper_reason = boundary_agreement(
                upper_full,
                upper_positive_only,
            )
            upper_threshold = (
                float(upper_full["elbow_score"])
                if upper_decision == "accepted_geometric"
                else None
            )
            upper_before, upper_after, upper_slope_ratio = local_slope_diagnostic(
                descending_scores,
                upper_full_rank,
            )

            anti_alignment_full = -ascending_scores
            lower_full = elbow_candidate(anti_alignment_full)
            negative_scores = ascending_scores[ascending_scores < 0]
            lower_negative_only = elbow_candidate(-negative_scores)
            lower_decision, lower_relative_difference, lower_reason = boundary_agreement(
                lower_full,
                lower_negative_only,
            )
            lower_threshold = (
                -float(lower_full["elbow_score"])
                if lower_decision == "accepted_geometric"
                else None
            )
            lower_before, lower_after, lower_slope_ratio = local_slope_diagnostic(
                anti_alignment_full,
                int(lower_full["elbow_rank"]) if lower_full["candidate_valid"] else None,
            )

            codes = assign_regions(
                state_scores,
                EXPECTED_TARGET_TOKEN_ID,
                upper_decision,
                upper_threshold,
                lower_decision,
                lower_threshold,
            )
            region_codes[state_index] = codes
            positive_count = int(np.sum(codes == 1))
            negative_count = int(np.sum(codes == -1))
            central_count = int(np.sum(codes == 0))
            if positive_count + negative_count + central_count != retained_count:
                raise RuntimeError(f"Region counts do not reconcile at state {state_index}.")

            region_result = state_region_result(upper_decision, lower_decision)
            boundary_records.append(
                {
                    "state_index": state_index,
                    "state_type": state["state_type"],
                    "state_label": state["state_label"],
                    "valid_token_count": retained_count,
                    "positive_score_count": int(np.sum(retained_scores > 0)),
                    "zero_score_count": int(np.sum(retained_scores == 0)),
                    "negative_score_count": int(np.sum(retained_scores < 0)),
                    "upper_full_rank": upper_full_rank,
                    "upper_full_score": float(upper_full["elbow_score"]),
                    "upper_full_strength": float(upper_full["elbow_strength"]),
                    "upper_positive_only_count": int(positive_scores.size),
                    "upper_positive_only_valid": bool(
                        upper_positive_only["candidate_valid"]
                    ),
                    "upper_positive_only_rank": upper_positive_only["elbow_rank"],
                    "upper_positive_only_score": upper_positive_only["elbow_score"],
                    "upper_positive_only_strength": upper_positive_only[
                        "elbow_strength"
                    ],
                    "upper_relative_rank_difference": upper_relative_difference,
                    "upper_decision": upper_decision,
                    "upper_reason": upper_reason,
                    "upper_threshold_score": upper_threshold,
                    "upper_local_gap_before": upper_before,
                    "upper_local_gap_after": upper_after,
                    "upper_local_slope_ratio": upper_slope_ratio,
                    "lower_full_valid": bool(lower_full["candidate_valid"]),
                    "lower_full_rank": lower_full["elbow_rank"],
                    "lower_full_score": (
                        -float(lower_full["elbow_score"])
                        if lower_full["candidate_valid"]
                        else None
                    ),
                    "lower_full_strength": lower_full["elbow_strength"],
                    "lower_negative_only_count": int(negative_scores.size),
                    "lower_negative_only_valid": bool(
                        lower_negative_only["candidate_valid"]
                    ),
                    "lower_negative_only_rank": lower_negative_only["elbow_rank"],
                    "lower_negative_only_score": (
                        -float(lower_negative_only["elbow_score"])
                        if lower_negative_only["candidate_valid"]
                        else None
                    ),
                    "lower_negative_only_strength": lower_negative_only[
                        "elbow_strength"
                    ],
                    "lower_relative_rank_difference": lower_relative_difference,
                    "lower_decision": lower_decision,
                    "lower_reason": lower_reason,
                    "lower_threshold_score": lower_threshold,
                    "lower_local_gap_before": lower_before,
                    "lower_local_gap_after": lower_after,
                    "lower_local_slope_ratio": lower_slope_ratio,
                    "positive_head_count": positive_count,
                    "central_body_count": central_count,
                    "negative_tail_count": negative_count,
                    "region_result": region_result,
                }
            )

            boundary_token_records.extend(
                boundary_band_records(
                    state_index=state_index,
                    state_type=str(state["state_type"]),
                    state_label=str(state["state_label"]),
                    boundary_kind="upper",
                    decision=upper_decision,
                    sorted_token_ids=descending_ids,
                    sorted_original_scores=descending_scores,
                    elbow_rank=upper_full_rank,
                    vocabulary=vocabulary,
                )
            )
            boundary_token_records.extend(
                boundary_band_records(
                    state_index=state_index,
                    state_type=str(state["state_type"]),
                    state_label=str(state["state_label"]),
                    boundary_kind="lower",
                    decision=lower_decision,
                    sorted_token_ids=ascending_ids,
                    sorted_original_scores=ascending_scores,
                    elbow_rank=(
                        int(lower_full["elbow_rank"])
                        if lower_full["candidate_valid"]
                        else None
                    ),
                    vocabulary=vocabulary,
                )
            )

        boundaries = pd.DataFrame(boundary_records)
        boundary_tokens = pd.DataFrame(boundary_token_records)
        boundaries_path = run_dir / "region_boundaries.csv"
        boundary_tokens_path = run_dir / "boundary_tokens.csv"
        boundaries.to_csv(boundaries_path, index=False)
        boundary_tokens.to_csv(boundary_tokens_path, index=False)
        add_component_success(manifest, current_component, component_started)
        manifest["components"][current_component].update(
            {
                "state_count": state_count,
                "agreement_tolerance": AGREEMENT_TOLERANCE,
                "boundary_band_size": BOUNDARY_BAND_SIZE,
            }
        )
        write_manifest()

        current_component = "region_membership"
        component_started = time.perf_counter()
        tail_frames: list[pd.DataFrame] = []
        for state_index in range(state_count):
            selected_ids = np.flatnonzero(np.abs(region_codes[state_index]) == 1)
            if selected_ids.size == 0:
                continue
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
        tails = (
            pd.concat(tail_frames, ignore_index=True)[tail_columns]
            if tail_frames
            else pd.DataFrame(columns=tail_columns)
        )
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
                [REGION_CODE_TO_LABEL[int(code)] for code in codes],
                dtype=object,
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
        trajectories = (
            pd.concat(trajectory_frames, ignore_index=True)[trajectory_columns]
            if trajectory_frames
            else pd.DataFrame(columns=trajectory_columns)
        )
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
        overview_figure_path = figures_dir / "region_boundaries_overview.png"
        selected_figure_path = figures_dir / "score_regions_selected_states.png"
        plot_boundary_overview(boundaries, overview_figure_path)
        plot_selected_regions(
            scores,
            EXPECTED_TARGET_TOKEN_ID,
            boundaries,
            selected_figure_path,
        )
        add_component_success(manifest, current_component, component_started)
        write_manifest()

        current_component = "validation"
        component_started = time.perf_counter()
        artifact_paths = [
            boundaries_path,
            boundary_tokens_path,
            tails_path,
            trajectories_path,
            overview_figure_path,
            selected_figure_path,
        ]
        if len(boundaries) != state_count:
            raise RuntimeError("Region boundary table has the wrong state count.")
        if not (
            boundaries["positive_head_count"]
            + boundaries["central_body_count"]
            + boundaries["negative_tail_count"]
            == retained_count
        ).all():
            raise RuntimeError("Persisted region population counts do not reconcile.")
        expected_tail_rows = int(
            boundaries["positive_head_count"].sum()
            + boundaries["negative_tail_count"].sum()
        )
        if len(tails) != expected_tail_rows:
            raise RuntimeError("Tail-token rows do not match accepted population counts.")
        expected_trajectory_rows = int(union_tail_ids.size * state_count)
        if len(trajectories) != expected_trajectory_rows:
            raise RuntimeError("Trajectory rows do not cover every selected token and state.")
        if set(boundaries["region_result"]) - {
            "accepted_two_boundaries",
            "accepted_upper_only",
            "accepted_lower_only",
            "rejected_unstable",
        }:
            raise RuntimeError("Unknown region decision in boundary table.")
        for path in artifact_paths:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"Required R003 artifact is absent or empty: {path}")

        manifest["artifacts"] = {
            str(path.relative_to(run_dir)).replace("\\", "/"): artifact_record(path)
            for path in artifact_paths
        }
        result_counts = boundaries["region_result"].value_counts().sort_index()
        upper_counts = boundaries["upper_decision"].value_counts().sort_index()
        lower_counts = boundaries["lower_decision"].value_counts().sort_index()
        manifest["results"] = {
            "state_count": state_count,
            "valid_vocabulary_size": vocab_size,
            "target_removed_vocabulary_size": retained_count,
            "source_score_matrix_shape": list(scores.shape),
            "region_result_counts": {
                key: int(value) for key, value in result_counts.items()
            },
            "upper_boundary_decision_counts": {
                key: int(value) for key, value in upper_counts.items()
            },
            "lower_boundary_decision_counts": {
                key: int(value) for key, value in lower_counts.items()
            },
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
        print(f"Upper decisions:        {manifest['results']['upper_boundary_decision_counts']}")
        print(f"Lower decisions:        {manifest['results']['lower_boundary_decision_counts']}")
        print(f"Region results:         {manifest['results']['region_result_counts']}")
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
    parser = argparse.ArgumentParser(description="R003 score-region boundary analysis")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run synthetic validation without creating an R003 run directory.",
    )
    arguments = parser.parse_args()
    if arguments.self_test:
        run_self_tests()
    else:
        main()
