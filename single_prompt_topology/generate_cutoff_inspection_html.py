from __future__ import annotations

import hashlib
import html
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.io import to_html
from safetensors.torch import load_file


SOURCE_RUN_ID = (
    "R002_lithium-static-basis-cutoff-feasibility__"
    "20261112T083025Z_pythia-6.9b_52ff8f97c2"
)
TARGET_TOKEN_ID = 27747
EXACT_UPPER_TAIL_RANKS = 5000
LOG_SAMPLED_REMAINDER_POINTS = 1000

PIPELINE_DIR = Path(__file__).resolve().parent
SOURCE_RUN_DIR = PIPELINE_DIR / "runs" / SOURCE_RUN_ID
REPORTS_DIR = PIPELINE_DIR / "reports"
OUTPUT_PATH = REPORTS_DIR / "R002_cutoff_score_curves.html"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_source_artifact(run_manifest: dict, relative_path: str) -> Path:
    expected = run_manifest["artifacts"][relative_path]
    path = SOURCE_RUN_DIR / relative_path
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.stat().st_size != expected["bytes"]:
        raise RuntimeError(f"Artifact size mismatch: {relative_path}")
    if sha256_file(path) != expected["sha256"]:
        raise RuntimeError(f"Artifact hash mismatch: {relative_path}")
    return path


def display_indices(point_count: int) -> np.ndarray:
    exact_count = min(EXACT_UPPER_TAIL_RANKS, point_count)
    exact = np.arange(exact_count, dtype=np.int64)
    if exact_count == point_count:
        return exact
    remainder = np.geomspace(
        exact_count + 1,
        point_count,
        num=LOG_SAMPLED_REMAINDER_POINTS,
    )
    remainder = np.unique(np.rint(remainder).astype(np.int64) - 1)
    return np.unique(np.concatenate([exact, remainder]))


def format_optional(value: object, digits: int = 4) -> str:
    if pd.isna(value):
        return "not available"
    if isinstance(value, (float, np.floating)):
        return f"{float(value):.{digits}f}"
    return str(value)


def main() -> None:
    manifest_path = SOURCE_RUN_DIR / "manifest.json"
    run_manifest = load_json(manifest_path)
    if run_manifest.get("status") != "successful":
        raise RuntimeError("R002 manifest is not successful.")

    score_path = validate_source_artifact(
        run_manifest,
        "vocabulary_scores.safetensors",
    )
    vocabulary_path = validate_source_artifact(run_manifest, "vocabulary_tokens.csv")
    states_path = validate_source_artifact(run_manifest, "state_metadata.csv")
    candidates_path = validate_source_artifact(run_manifest, "cutoff_candidates.csv")
    summary_path = validate_source_artifact(run_manifest, "cutoff_summary.csv")

    scores = load_file(score_path)["cosine_scores"].numpy()
    vocabulary = pd.read_csv(vocabulary_path).set_index("token_id")
    states = pd.read_csv(states_path).set_index("state_index")
    candidates = pd.read_csv(candidates_path)
    summary = pd.read_csv(summary_path)
    summary = summary[summary["variant"] == "exact_target_removed"].set_index(
        "state_index"
    )

    token_ids = np.arange(scores.shape[1], dtype=np.int64)
    retained_ids = token_ids[token_ids != TARGET_TOKEN_ID]
    candidate_colors = {
        "full": "#6c757d",
        "top_10pct": "#e76f51",
        "top_5pct": "#f4a261",
        "top_2pct": "#2a9d8f",
        "top_1pct": "#264653",
    }

    plot_fragments = []
    overview_rows = []
    for state_index in range(scores.shape[0]):
        state = states.loc[state_index]
        state_summary = summary.loc[state_index]
        state_scores = scores[state_index, retained_ids]
        order = np.argsort(-state_scores, kind="stable")
        sorted_scores = state_scores[order]
        sorted_ids = retained_ids[order]
        selected = display_indices(sorted_scores.size)
        selected_ids = sorted_ids[selected]
        selected_vocab = vocabulary.loc[selected_ids]

        customdata = np.column_stack(
            [
                selected_ids,
                selected_vocab["raw_token"].fillna("").astype(str),
                selected_vocab["decoded_token"].fillna("").astype(str),
                selected_vocab["token_class"].fillna("").astype(str),
            ]
        )
        figure = go.Figure()
        figure.add_trace(
            go.Scatter(
                x=selected + 1,
                y=sorted_scores[selected],
                mode="lines",
                name="ranked cosine score",
                line={"color": "#2563eb", "width": 1.5},
                customdata=customdata,
                hovertemplate=(
                    "rank=%{x:,}<br>score=%{y:.7f}<br>"
                    "token_id=%{customdata[0]}<br>"
                    "raw=%{customdata[1]}<br>decoded=%{customdata[2]}<br>"
                    "class=%{customdata[3]}<extra></extra>"
                ),
            )
        )

        state_candidates = candidates[
            (candidates["state_index"] == state_index)
            & (candidates["variant"] == "exact_target_removed")
            & candidates["candidate_valid"]
        ]
        for candidate in state_candidates.itertuples(index=False):
            figure.add_trace(
                go.Scatter(
                    x=[candidate.elbow_rank],
                    y=[candidate.elbow_score],
                    mode="markers",
                    name=candidate.window_label,
                    marker={
                        "size": 9,
                        "color": candidate_colors[candidate.window_label],
                        "symbol": "diamond",
                    },
                    hovertemplate=(
                        f"window={candidate.window_label}<br>"
                        "rank=%{x:,}<br>score=%{y:.7f}<br>"
                        f"strength={candidate.elbow_strength:.5f}<extra></extra>"
                    ),
                )
            )

        figure.update_layout(
            title={
                "text": (
                    f"State {state_index}: {state['state_label']}"
                    f" — classification: {state_summary['cutoff_status']}"
                ),
                "x": 0.02,
            },
            xaxis={
                "title": "Vocabulary rank (exact target removed)",
                "type": "linear",
                "gridcolor": "#e5e7eb",
            },
            yaxis={
                "title": "Cosine similarity to static input embedding",
                "gridcolor": "#e5e7eb",
                "zerolinecolor": "#9ca3af",
            },
            template="plotly_white",
            height=470,
            margin={"l": 75, "r": 25, "t": 75, "b": 70},
            legend={
                "orientation": "h",
                "yanchor": "bottom",
                "y": 1.01,
                "xanchor": "right",
                "x": 1,
                "font": {"size": 10},
            },
            updatemenus=[
                {
                    "type": "buttons",
                    "direction": "right",
                    "x": 0,
                    "y": 1.13,
                    "buttons": [
                        {
                            "label": "Linear rank",
                            "method": "relayout",
                            "args": [{"xaxis.type": "linear"}],
                        },
                        {
                            "label": "Log rank",
                            "method": "relayout",
                            "args": [{"xaxis.type": "log"}],
                        },
                    ],
                }
            ],
        )
        plot_fragments.append(
            to_html(
                figure,
                full_html=False,
                include_plotlyjs="inline" if state_index == 0 else False,
                config={
                    "displaylogo": False,
                    "responsive": True,
                    "scrollZoom": True,
                },
                div_id=f"state-{state_index:02d}",
            )
        )

        overview_rows.append(
            "<tr>"
            f"<td>{state_index}</td>"
            f"<td>{html.escape(str(state['state_label']))}</td>"
            f"<td>{html.escape(str(state_summary['cutoff_status']))}</td>"
            f"<td>{format_optional(state_summary['candidate_rank'], 0)}</td>"
            f"<td>{format_optional(state_summary['cutoff_score'], 6)}</td>"
            f"<td>{format_optional(state_summary['relative_rank_mad'], 4)}</td>"
            f"<td>{format_optional(state_summary['median_elbow_strength'], 4)}</td>"
            "</tr>"
        )

    generated_at = datetime.now(timezone.utc).isoformat()
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>R002 cutoff score curves</title>
  <style>
    body {{ margin: 0; background: #f3f4f6; color: #111827; font-family: Inter, Segoe UI, Arial, sans-serif; }}
    main {{ max-width: 1800px; margin: 0 auto; padding: 28px; }}
    header, section {{ background: white; border: 1px solid #d1d5db; border-radius: 10px; padding: 22px; margin-bottom: 22px; }}
    h1 {{ margin-top: 0; }}
    code {{ overflow-wrap: anywhere; }}
    .notice {{ border-left: 5px solid #2563eb; background: #eff6ff; padding: 12px 16px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(660px, 1fr)); gap: 18px; }}
    .plot-card {{ background: white; border: 1px solid #d1d5db; border-radius: 10px; padding: 8px; min-width: 0; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; }}
    th, td {{ border-bottom: 1px solid #e5e7eb; padding: 7px 9px; text-align: right; }}
    th:nth-child(2), td:nth-child(2) {{ text-align: left; }}
    @media (max-width: 760px) {{ main {{ padding: 10px; }} .grid {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
<main>
  <header>
    <h1>R002 full-vocabulary cutoff inspection</h1>
    <p><strong>Source run:</strong> <code>{html.escape(SOURCE_RUN_ID)}</code></p>
    <p><strong>Generated:</strong> <code>{generated_at}</code></p>
    <p><strong>Score artifact SHA-256:</strong> <code>{sha256_file(score_path)}</code></p>
    <div class="notice">
      Each curve ranks cosine similarity between the contextual <code>lithium</code>
      state and every valid static input embedding. The exact target token is
      removed. Ranks 1–{EXACT_UPPER_TAIL_RANKS:,} are preserved exactly; the
      remaining tail is logarithmically sampled for browser performance. Use the
      modebar to zoom, pan, inspect tokens and reset axes. Candidate elbow markers
      show the five automated analysis windows but do not establish a valid cutoff.
    </div>
    <p>The capture contains the input embedding, outputs after blocks 0–30, and
    the final layer-normalized output after block 31. The raw block-31 output is
    unavailable because the capture API replaced it with the normalized state.</p>
  </header>

  <section>
    <h2>Automated-cutoff summary</h2>
    <table>
      <thead><tr><th>State</th><th>Label</th><th>Status</th><th>Candidate rank</th><th>Score</th><th>Relative rank MAD</th><th>Median strength</th></tr></thead>
      <tbody>{''.join(overview_rows)}</tbody>
    </table>
  </section>

  <div class="grid">
    {''.join(f'<div class="plot-card">{fragment}</div>' for fragment in plot_fragments)}
  </div>
</main>
</body>
</html>
"""

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(page, encoding="utf-8")
    print(f"Created: {OUTPUT_PATH}")
    print(f"Bytes:   {OUTPUT_PATH.stat().st_size}")
    print(f"SHA256:  {sha256_file(OUTPUT_PATH)}")


if __name__ == "__main__":
    main()
