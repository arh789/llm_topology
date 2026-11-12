from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from safetensors.torch import load_file

from generate_cutoff_inspection_html import (
    SOURCE_RUN_DIR,
    TARGET_TOKEN_ID,
    load_json,
    validate_source_artifact,
)


OUTPUT_DIR = Path(__file__).resolve().parent / "reports" / "R002_cutoff_score_curves_png"
OVERVIEW_PATH = OUTPUT_DIR / "R002_cutoff_score_curves_overview.png"

CANDIDATE_COLORS = {
    "full": "#6c757d",
    "top_10pct": "#e76f51",
    "top_5pct": "#f4a261",
    "top_2pct": "#2a9d8f",
    "top_1pct": "#264653",
}


def safe_filename(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def load_inputs() -> tuple[np.ndarray, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    manifest = load_json(SOURCE_RUN_DIR / "manifest.json")
    if manifest.get("status") != "successful":
        raise RuntimeError("R002 manifest is not successful.")

    score_path = validate_source_artifact(manifest, "vocabulary_scores.safetensors")
    states_path = validate_source_artifact(manifest, "state_metadata.csv")
    candidates_path = validate_source_artifact(manifest, "cutoff_candidates.csv")
    summary_path = validate_source_artifact(manifest, "cutoff_summary.csv")

    scores = load_file(score_path)["cosine_scores"].numpy()
    states = pd.read_csv(states_path).set_index("state_index")
    candidates = pd.read_csv(candidates_path)
    summary = pd.read_csv(summary_path)
    summary = summary[summary["variant"] == "exact_target_removed"].set_index(
        "state_index"
    )
    return scores, states, candidates, summary


def ranked_scores(scores: np.ndarray, state_index: int) -> np.ndarray:
    token_ids = np.arange(scores.shape[1], dtype=np.int64)
    retained_ids = token_ids[token_ids != TARGET_TOKEN_ID]
    state_scores = scores[state_index, retained_ids]
    order = np.argsort(-state_scores, kind="stable")
    return state_scores[order]


def state_candidates(candidates: pd.DataFrame, state_index: int) -> pd.DataFrame:
    return candidates[
        (candidates["state_index"] == state_index)
        & (candidates["variant"] == "exact_target_removed")
        & candidates["candidate_valid"]
    ]


def plot_state(
    sorted_scores: np.ndarray,
    candidates: pd.DataFrame,
    state_index: int,
    state_label: str,
    cutoff_status: str,
    output_path: Path,
) -> None:
    ranks = np.arange(1, sorted_scores.size + 1)
    figure, axis = plt.subplots(figsize=(14, 7), dpi=160)
    axis.plot(ranks, sorted_scores, color="#2563eb", linewidth=1.35)

    for candidate in candidates.itertuples(index=False):
        label = f"{candidate.window_label}: rank {int(candidate.elbow_rank):,}"
        axis.scatter(
            candidate.elbow_rank,
            candidate.elbow_score,
            color=CANDIDATE_COLORS[candidate.window_label],
            edgecolor="white",
            linewidth=0.8,
            marker="D",
            s=58,
            zorder=3,
            label=label,
        )

    axis.axhline(0, color="#9ca3af", linewidth=0.8)
    axis.set_title(
        f"State {state_index}: {state_label} — classification: {cutoff_status}",
        loc="left",
    )
    axis.set_xlabel("Vocabulary rank (exact target removed; linear scale)")
    axis.set_ylabel("Cosine similarity to static input embedding")
    axis.grid(True, color="#e5e7eb", linewidth=0.7)
    axis.set_xlim(1, sorted_scores.size)
    axis.legend(loc="upper right", fontsize=8, frameon=False)
    figure.tight_layout()
    figure.savefig(output_path, bbox_inches="tight")
    plt.close(figure)


def plot_overview(
    score_rows: list[np.ndarray],
    states: pd.DataFrame,
    candidates: pd.DataFrame,
) -> None:
    figure, axes = plt.subplots(6, 6, figsize=(24, 20), dpi=160)
    flat_axes = axes.ravel()

    for state_index, sorted_scores in enumerate(score_rows):
        axis = flat_axes[state_index]
        ranks = np.arange(1, sorted_scores.size + 1)
        axis.plot(ranks, sorted_scores, color="#2563eb", linewidth=0.85)
        for candidate in state_candidates(candidates, state_index).itertuples(index=False):
            axis.scatter(
                candidate.elbow_rank,
                candidate.elbow_score,
                color=CANDIDATE_COLORS[candidate.window_label],
                marker="D",
                s=15,
                zorder=3,
            )
        axis.axhline(0, color="#9ca3af", linewidth=0.5)
        axis.grid(True, color="#e5e7eb", linewidth=0.45)
        axis.set_title(
            f"{state_index}: {states.loc[state_index, 'state_label']}",
            fontsize=9,
            loc="left",
        )
        axis.tick_params(axis="both", labelsize=7)
        axis.set_xlim(1, sorted_scores.size)

    for axis in flat_axes[len(score_rows) :]:
        axis.axis("off")

    figure.suptitle(
        "R002 ranked static-input-basis cosine curves — exact target removed",
        fontsize=18,
    )
    figure.supxlabel("Vocabulary rank (linear scale)")
    figure.supylabel("Cosine similarity")
    figure.tight_layout(rect=(0.025, 0.025, 1, 0.975))
    figure.savefig(OVERVIEW_PATH, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    scores, states, candidates, summary = load_inputs()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    score_rows: list[np.ndarray] = []

    for state_index in range(scores.shape[0]):
        sorted_scores = ranked_scores(scores, state_index)
        score_rows.append(sorted_scores)
        state_label = str(states.loc[state_index, "state_label"])
        cutoff_status = str(summary.loc[state_index, "cutoff_status"])
        output_path = OUTPUT_DIR / (
            f"state-{state_index:02d}_{safe_filename(state_label)}.png"
        )
        plot_state(
            sorted_scores,
            state_candidates(candidates, state_index),
            state_index,
            state_label,
            cutoff_status,
            output_path,
        )

    plot_overview(score_rows, states, candidates)
    print(f"Created {len(score_rows)} state PNGs and 1 overview in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
