"""Generate the self-contained R009 descriptive community summary report."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR_NAME = "R009_lithium-community-semantic-classification"
R008_DIR_NAME = (
    "R008_lithium-chatgpt-readable-split-networks-validated-retry__"
    "20261112T200904Z_pythia-6.9b_52ff8f97c2"
)
SOURCE_COMMIT = "49a4b0a2e0ed4eb831c9ba85311ebf093631022c"
TAXONOMY = [
    "semantic/topic",
    "lexical/morphological",
    "named-entity",
    "numeric",
    "formatting/tokenizer",
    "mixed",
    "unclear",
]
CONFIDENCES = ["High", "Moderate", "Low"]
ROW_PATTERN = re.compile(
    r"^\| (C\d+) \| (\d+) \| (.*?) \| "
    r"(semantic/topic|lexical/morphological|named-entity|numeric|"
    r"formatting/tokenizer|mixed|unclear) \| "
    r"(High|Moderate|Low) \| (.*) \|$",
    re.MULTILINE,
)
HEADER_PATTERN = re.compile(r"^# R009 State (\d+) — (.+)$", re.MULTILINE)


def friendly_state_name(index: int) -> str:
    if index == 0:
        return "Input embedding"
    if index == 32:
        return "Final normalisation after Block 31"
    return f"Block {index - 1} output"


def extract_section(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        raise ValueError(f"Missing section boundary: {start!r} / {end!r}")
    return text.split(start, 1)[1].split(end, 1)[0]


def parse_rows(section: str, state_index: int, side: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for match in ROW_PATTERN.finditer(section):
        community_id, size, identity, structure_type, confidence, evidence = match.groups()
        rows.append(
            {
                "state": state_index,
                "state_name": friendly_state_name(state_index),
                "side": side,
                "community_id": community_id,
                "community_number": int(community_id[1:]),
                "size": int(size),
                "identity": identity,
                "structure_type": structure_type,
                "confidence": confidence,
                "evidence": evidence,
            }
        )
    return rows


def parse_state_file(path: Path) -> tuple[dict[str, object], list[dict[str, object]]]:
    text = path.read_text(encoding="utf-8")
    header = HEADER_PATTERN.search(text)
    if not header:
        raise ValueError(f"Could not parse state header in {path}")
    state_index = int(header.group(1))
    positive = extract_section(
        text, "## Positive-head communities", "### Positive-head type count"
    )
    negative = extract_section(
        text, "## Negative-tail communities", "### Negative-tail type count"
    )
    rows = parse_rows(positive, state_index, "positive_head")
    rows.extend(parse_rows(negative, state_index, "negative_tail"))
    state = {
        "index": state_index,
        "name": friendly_state_name(state_index),
        "source_heading": header.group(2),
        "file": path.name,
        "positive_count": sum(row["side"] == "positive_head" for row in rows),
        "negative_count": sum(row["side"] == "negative_tail" for row in rows),
    }
    state["total_count"] = state["positive_count"] + state["negative_count"]
    return state, rows


def load_r008_top_tokens(path: Path) -> dict[tuple[int, str, int], dict[str, object]]:
    source = json.loads(path.read_text(encoding="utf-8"))
    networks = source.get("networks", [])
    if len(networks) != 66:
        raise ValueError(f"Expected 66 R008 networks, found {len(networks)}")

    records: dict[tuple[int, str, int], dict[str, object]] = {}
    for network in networks:
        state_index = int(network["state_index"])
        side = str(network["side"])
        for community in network["communities"]:
            community_id = int(community["community_id"])
            key = (state_index, side, community_id)
            if key in records:
                raise ValueError(f"Duplicate R008 community key: {key}")
            representatives = [str(token) for token in community["representative_tokens"]]
            if len(representatives) < 10:
                raise ValueError(
                    f"R008 community {key} has only {len(representatives)} representatives"
                )
            records[key] = {
                "size": int(community["community_size"]),
                "top_tokens": representatives[:10],
            }

    if len(records) != 792:
        raise ValueError(f"Expected 792 R008 community records, found {len(records)}")
    return records


def build_payload(run_dir: Path, community_networks_path: Path) -> dict[str, object]:
    states: list[dict[str, object]] = []
    communities: list[dict[str, object]] = []
    for path in sorted(run_dir.glob("STATE_*.md")):
        state, rows = parse_state_file(path)
        states.append(state)
        communities.extend(rows)

    states.sort(key=lambda item: int(item["index"]))
    communities.sort(
        key=lambda item: (
            int(item["state"]),
            0 if item["side"] == "positive_head" else 1,
            int(item["community_number"]),
        )
    )

    state_indices = [int(state["index"]) for state in states]
    if state_indices != list(range(33)):
        raise ValueError(f"Expected states 0..32, found {state_indices}")
    if len(communities) != 792:
        raise ValueError(f"Expected 792 communities, found {len(communities)}")

    side_counts = Counter(str(row["side"]) for row in communities)
    if side_counts != Counter({"positive_head": 392, "negative_tail": 400}):
        raise ValueError(f"Unexpected side totals: {side_counts}")

    for state in states:
        state_rows = [row for row in communities if row["state"] == state["index"]]
        for side in ("positive_head", "negative_tail"):
            side_rows = [row for row in state_rows if row["side"] == side]
            ids = [int(row["community_number"]) for row in side_rows]
            if ids != list(range(len(ids))):
                raise ValueError(
                    f"Non-contiguous IDs at state {state['index']} side {side}: {ids}"
                )

    top_tokens_by_key = load_r008_top_tokens(community_networks_path)
    for row in communities:
        key = (
            int(row["state"]),
            str(row["side"]),
            int(row["community_number"]),
        )
        source = top_tokens_by_key.get(key)
        if source is None:
            raise ValueError(f"No R008 representative-token record for {key}")
        if int(source["size"]) != int(row["size"]):
            raise ValueError(
                f"Community-size mismatch for {key}: "
                f"R008={source['size']} R009={row['size']}"
            )
        row["top_tokens"] = source["top_tokens"]

    return {
        "source_commit": SOURCE_COMMIT,
        "run": "R009",
        "run_name": "lithium-community-semantic-classification",
        "measurement_source": R008_DIR_NAME,
        "top_tokens_source": community_networks_path.name,
        "top_tokens_basis": (
            "First 10 R008 representative tokens, ranked by descending degree "
            "within the state-side community graph, with token ID as tie-breaker."
        ),
        "taxonomy": TAXONOMY,
        "confidences": CONFIDENCES,
        "states": states,
        "communities": communities,
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>R009 Community Summary</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: light-dark(#f4f6f8, #11161c);
      --surface: light-dark(#ffffff, #182029);
      --surface-2: light-dark(#eef2f5, #202a35);
      --text: light-dark(#17212b, #edf3f8);
      --muted: light-dark(#5d6b78, #aebbc6);
      --border: light-dark(#d7dee5, #34414d);
      --accent: light-dark(#225ea8, #69a8e8);
      --positive: light-dark(#176b57, #61c4a7);
      --negative: light-dark(#a34538, #ef8d80);
      --semantic: light-dark(#2563a6, #61a7e8);
      --lexical: light-dark(#ad5a17, #ed9b57);
      --named: light-dark(#7252a4, #aa8bd8);
      --numeric: light-dark(#277d47, #6cc78d);
      --formatting: light-dark(#a13c52, #e27a90);
      --mixed: light-dark(#8a6a13, #d8b94e);
      --unclear: light-dark(#68737e, #a8b2bb);
      --shadow: 0 8px 26px light-dark(rgba(23, 33, 43, .08), rgba(0, 0, 0, .24));
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }
    a { color: var(--accent); }
    code {
      padding: .08rem .28rem;
      border-radius: .28rem;
      background: var(--surface-2);
      color: inherit;
      font-size: .92em;
    }
    .hero {
      padding: 3rem clamp(1rem, 4vw, 4rem) 2.4rem;
      background:
        radial-gradient(circle at 12% 20%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 34%),
        radial-gradient(circle at 86% 15%, color-mix(in srgb, var(--positive) 13%, transparent), transparent 32%),
        var(--surface);
      border-bottom: 1px solid var(--border);
    }
    .hero-inner, main, footer { max-width: 1440px; margin: 0 auto; }
    .eyebrow {
      color: var(--accent);
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .11em;
      text-transform: uppercase;
    }
    h1 { max-width: 920px; margin: .4rem 0 .65rem; font-size: clamp(2rem, 4.5vw, 4rem); line-height: 1.05; }
    h2 { margin: 0 0 .45rem; font-size: clamp(1.35rem, 2.4vw, 2rem); }
    h3 { margin: 0 0 .35rem; font-size: 1.05rem; }
    p { margin: 0; }
    .lede { max-width: 880px; color: var(--muted); font-size: 1.05rem; }
    .provenance { margin-top: 1rem; color: var(--muted); font-size: .88rem; }
    main { padding: 2rem clamp(1rem, 4vw, 4rem) 4rem; }
    section { margin-top: 2.4rem; }
    section:first-child { margin-top: 0; }
    .section-intro { max-width: 900px; color: var(--muted); margin-bottom: 1rem; }
    .kpis { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: .9rem; }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: .85rem;
      box-shadow: var(--shadow);
    }
    .kpi { padding: 1rem 1.1rem; }
    .kpi-label { color: var(--muted); font-size: .78rem; text-transform: uppercase; letter-spacing: .06em; }
    .kpi-value { margin-top: .2rem; font-size: 1.8rem; font-weight: 720; font-variant-numeric: tabular-nums; }
    .kpi-note { margin-top: .15rem; color: var(--muted); font-size: .82rem; }
    .boundary {
      margin-top: 1rem;
      padding: 1rem 1.1rem;
      border-left: 4px solid var(--accent);
      background: color-mix(in srgb, var(--accent) 8%, var(--surface));
      border-radius: .45rem;
    }
    .boundary strong { display: block; margin-bottom: .2rem; }
    .chart-panel { padding: 1rem; overflow: hidden; }
    #count-chart { width: 100%; height: auto; min-height: 260px; display: block; }
    .chart-legend { display: flex; flex-wrap: wrap; gap: 1rem; margin-top: .5rem; color: var(--muted); font-size: .85rem; }
    .legend-item { display: inline-flex; align-items: center; gap: .4rem; }
    .legend-mark { width: 1rem; height: .22rem; border-radius: 1rem; background: currentColor; }
    .positive { color: var(--positive); }
    .negative { color: var(--negative); }
    .controls {
      display: grid;
      grid-template-columns: minmax(210px, 2fr) repeat(4, minmax(135px, 1fr)) auto;
      gap: .75rem;
      align-items: end;
      margin: 1rem 0;
    }
    label { display: grid; gap: .3rem; color: var(--muted); font-size: .78rem; font-weight: 650; }
    input, select, button {
      min-height: 2.55rem;
      border: 1px solid var(--border);
      border-radius: .45rem;
      background: var(--surface);
      color: var(--text);
      font: inherit;
    }
    input, select { width: 100%; padding: .55rem .65rem; }
    button { padding: .55rem .8rem; cursor: pointer; }
    button:hover { border-color: var(--accent); }
    button:focus-visible, input:focus-visible, select:focus-visible { outline: 3px solid color-mix(in srgb, var(--accent) 35%, transparent); outline-offset: 2px; }
    .table-wrap { width: 100%; overflow-x: auto; border: 1px solid var(--border); border-radius: .7rem; background: var(--surface); }
    table { width: 100%; border-collapse: collapse; font-size: .88rem; }
    th, td { padding: .66rem .7rem; border-bottom: 1px solid var(--border); text-align: left; vertical-align: top; }
    th { background: var(--surface-2); color: var(--muted); font-size: .75rem; letter-spacing: .025em; text-transform: uppercase; position: sticky; top: 0; z-index: 1; }
    tbody tr:last-child td { border-bottom: 0; }
    tbody tr:hover { background: color-mix(in srgb, var(--accent) 5%, transparent); }
    .num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
    .nowrap { white-space: nowrap; }
    .token-list { display: flex; flex-wrap: wrap; gap: .22rem .32rem; min-width: 300px; }
    .token-list code { white-space: nowrap; }
    .evidence { min-width: 330px; color: var(--muted); }
    .community-table-wrap { overflow-x: hidden; }
    .community-table { table-layout: fixed; }
    .community-table th, .community-table td {
      padding: .6rem .5rem;
      overflow-wrap: anywhere;
    }
    .community-table .token-list { min-width: 0; }
    .community-table .token-list code { white-space: normal; overflow-wrap: anywhere; }
    .community-table .evidence { min-width: 0; }
    .community-table .badge { white-space: normal; }
    .badge {
      display: inline-flex;
      align-items: center;
      max-width: 100%;
      padding: .18rem .48rem;
      border-radius: 999px;
      background: color-mix(in srgb, currentColor 12%, transparent);
      color: var(--muted);
      font-size: .76rem;
      line-height: 1.3;
      white-space: nowrap;
    }
    .badge-positive { color: var(--positive); }
    .badge-negative { color: var(--negative); }
    .type-semantic { color: var(--semantic); }
    .type-lexical { color: var(--lexical); }
    .type-named { color: var(--named); }
    .type-numeric { color: var(--numeric); }
    .type-formatting { color: var(--formatting); }
    .type-mixed { color: var(--mixed); }
    .type-unclear { color: var(--unclear); }
    .result-bar, .pagination { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin: .7rem 0; color: var(--muted); font-size: .86rem; }
    .pagination-controls { display: flex; gap: .45rem; align-items: center; }
    .pagination button { min-height: 2.2rem; padding: .35rem .65rem; }
    button:disabled { opacity: .45; cursor: not-allowed; }
    .heat-controls { width: min(250px, 100%); margin: 1rem 0 .75rem; }
    .heatmap td:not(:first-child):not(:last-child) { text-align: center; padding: .25rem; }
    .heat-cell { width: 100%; min-width: 2.35rem; min-height: 2.15rem; border: 0; border-radius: .28rem; padding: .25rem; font-variant-numeric: tabular-nums; font-weight: 700; }
    .heat-cell.type-semantic { background: color-mix(in srgb, var(--semantic) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-lexical { background: color-mix(in srgb, var(--lexical) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-named { background: color-mix(in srgb, var(--named) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-numeric { background: color-mix(in srgb, var(--numeric) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-formatting { background: color-mix(in srgb, var(--formatting) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-mixed { background: color-mix(in srgb, var(--mixed) var(--heat), var(--surface)); color: var(--text); }
    .heat-cell.type-unclear { background: color-mix(in srgb, var(--unclear) var(--heat), var(--surface)); color: var(--text); }
    .taxonomy-legend { display: flex; flex-wrap: wrap; gap: .55rem .9rem; margin-top: .75rem; }
    details { border-top: 1px solid var(--border); background: var(--surface); }
    details:last-child { border-bottom: 1px solid var(--border); }
    summary { display: flex; flex-wrap: wrap; align-items: center; gap: .55rem; padding: .85rem .9rem; cursor: pointer; font-weight: 700; }
    summary:hover { background: var(--surface-2); }
    .state-counts { margin-left: auto; color: var(--muted); font-size: .82rem; font-weight: 500; }
    .state-content { padding: 0 .9rem 1rem; }
    .state-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    .state-table th, .state-table td { padding: .48rem .55rem; }
    .state-type-row { display: flex; flex-wrap: wrap; gap: .4rem; margin: .2rem 0 .7rem; }
    .method-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    .method-card { padding: 1rem; }
    .method-card ul { margin: .55rem 0 0; padding-left: 1.15rem; }
    footer { padding: 1.2rem clamp(1rem, 4vw, 4rem) 3rem; color: var(--muted); font-size: .8rem; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }
    @media (max-width: 1000px) {
      .kpis { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .controls { grid-template-columns: repeat(3, minmax(0, 1fr)); }
      .controls .search-field { grid-column: span 2; }
      .state-grid, .method-grid { grid-template-columns: 1fr; }
    }
    @media (max-width: 650px) {
      .hero { padding-top: 2rem; }
      .kpis, .controls { grid-template-columns: 1fr; }
      .controls .search-field { grid-column: auto; }
      .result-bar, .pagination { align-items: flex-start; flex-direction: column; }
      .state-counts { width: 100%; margin-left: 0; }
      th, td { padding: .55rem; }
    }
    @media print {
      body { background: #fff; color: #111; }
      .controls, .pagination, .heat-controls { display: none !important; }
      .card, .table-wrap { box-shadow: none; }
      details { break-inside: avoid; }
    }
  </style>
</head>
<body>
  <header class="hero">
    <div class="hero-inner">
      <div class="eyebrow">R009 · descriptive community classification</div>
      <h1>Community identities across transformer depth</h1>
      <p class="lede">A self-contained summary of every state-local community identified from the input embedding through final normalisation. Explore the fixed taxonomy, compare positive and negative populations, or inspect all 792 classifications.</p>
      <p class="provenance">Measurement source: <code>R008</code> · Interpretation model: <code>GPT-5.6 Sol</code> · Imported source commit: <code>__SOURCE_COMMIT__</code></p>
    </div>
  </header>

  <main>
    <section aria-labelledby="overview-title">
      <h2 id="overview-title">Scope</h2>
      <p class="section-intro">Counts refer to state-local Louvain community instances. A token may recur across states, and equal community IDs in different states do not imply continuity.</p>
      <div class="kpis" id="kpis"></div>
      <div class="boundary">
        <strong>Interpretation boundary</strong>
        This report aggregates R009's candidate identities. It does not establish semantic coherence, match communities across states, assign SDA-3 roles, identify an optimal layer, or measure curvature.
      </div>
    </section>

    <section aria-labelledby="counts-title">
      <h2 id="counts-title">Community count by state</h2>
      <p class="section-intro">Positive-head and negative-tail populations were classified independently at each recorded state.</p>
      <div class="chart-panel card">
        <svg id="count-chart" viewBox="0 0 1120 320" role="img" aria-labelledby="count-chart-title count-chart-desc">
          <title id="count-chart-title">Positive and negative community counts by state</title>
          <desc id="count-chart-desc">Two lines compare the number of positive-head and negative-tail communities across 33 states.</desc>
        </svg>
        <div class="chart-legend" aria-hidden="true">
          <span class="legend-item positive"><span class="legend-mark"></span>Positive head</span>
          <span class="legend-item negative"><span class="legend-mark"></span>Negative tail</span>
        </div>
      </div>
    </section>

    <section aria-labelledby="heat-title">
      <h2 id="heat-title">Structure-type composition</h2>
      <p class="section-intro">The heatmap shows counts under R009's fixed taxonomy. Select a cell to open the matching communities in the explorer.</p>
      <div class="heat-controls">
        <label for="heat-side">Population
          <select id="heat-side">
            <option value="all">Both sides</option>
            <option value="positive_head">Positive head</option>
            <option value="negative_tail">Negative tail</option>
          </select>
        </label>
      </div>
      <div class="table-wrap"><table class="heatmap" id="heatmap"></table></div>
      <div class="taxonomy-legend" id="taxonomy-legend"></div>
    </section>

    <section id="explorer" aria-labelledby="explorer-title">
      <h2 id="explorer-title">Community explorer</h2>
      <p class="section-intro">Search broad identities, top tokens and supporting evidence, or filter by state, side, structure type and confidence. Top tokens are the first ten R008 representatives, ranked by within-community graph degree.</p>
      <div class="controls">
        <label class="search-field" for="search">Search
          <input id="search" type="search" placeholder="e.g. chemistry, names, numeric, formatting">
        </label>
        <label for="state-filter">State
          <select id="state-filter"><option value="all">All states</option></select>
        </label>
        <label for="side-filter">Side
          <select id="side-filter">
            <option value="all">Both sides</option>
            <option value="positive_head">Positive head</option>
            <option value="negative_tail">Negative tail</option>
          </select>
        </label>
        <label for="type-filter">Structure type
          <select id="type-filter"><option value="all">All types</option></select>
        </label>
        <label for="confidence-filter">Confidence
          <select id="confidence-filter"><option value="all">All levels</option></select>
        </label>
        <button type="button" id="reset">Reset</button>
      </div>
      <div class="result-bar"><span id="result-count" aria-live="polite"></span><span>50 rows per page</span></div>
      <div class="table-wrap community-table-wrap">
        <table class="community-table">
          <colgroup>
            <col style="width:10%">
            <col style="width:9%">
            <col style="width:6.5%">
            <col style="width:4.5%">
            <col style="width:13.5%">
            <col style="width:22%">
            <col style="width:11%">
            <col style="width:8%">
            <col style="width:15.5%">
          </colgroup>
          <thead><tr><th>State</th><th>Side</th><th>Community</th><th class="num">Size</th><th>Broad identity</th><th>Top 10 tokens</th><th>Structure type</th><th>Confidence</th><th>Evidence</th></tr></thead>
          <tbody id="community-body"></tbody>
        </table>
      </div>
      <div class="pagination">
        <span id="page-status"></span>
        <div class="pagination-controls">
          <button type="button" id="previous">Previous</button>
          <button type="button" id="next">Next</button>
        </div>
      </div>
    </section>

    <section aria-labelledby="layers-title">
      <h2 id="layers-title">State-by-state community summaries</h2>
      <p class="section-intro">Open any state to inspect every broad identity on both sides. These are state-local classifications; the layout does not imply cross-state matching.</p>
      <div id="state-summaries"></div>
    </section>

    <section aria-labelledby="method-title">
      <h2 id="method-title">Evidence and limits</h2>
      <div class="method-grid">
        <div class="method-card card">
          <h3>What is represented</h3>
          <ul>
            <li>33 recorded states from input embedding to final normalisation.</li>
            <li>392 positive-head and 400 negative-tail community instances.</li>
            <li>Broad identity, top 10 graph-degree representatives, structure type, confidence and concise evidence for every community.</li>
          </ul>
        </div>
        <div class="method-card card">
          <h3>What remains unresolved</h3>
          <ul>
            <li>Whether each label describes a genuinely coherent semantic structure.</li>
            <li>Which communities correspond across states despite changing local IDs.</li>
            <li>Whether any stable roles map to C, S, A, HCU or E.</li>
            <li>Which states expose those relationships most clearly.</li>
          </ul>
        </div>
      </div>
    </section>
  </main>

  <footer>Generated from the 33 R009 state Markdown files. The report is a descriptive aggregation, not a new measurement or a cross-state semantic synthesis.</footer>

  <script id="r009-data" type="application/json">__DATA__</script>
  <script>
    (() => {
      'use strict';
      const payload = JSON.parse(document.getElementById('r009-data').textContent);
      const rows = payload.communities;
      const states = payload.states;
      const taxonomy = payload.taxonomy;
      const confidences = payload.confidences;
      const pageSize = 50;
      let page = 1;

      const typeClass = {
        'semantic/topic': 'type-semantic',
        'lexical/morphological': 'type-lexical',
        'named-entity': 'type-named',
        'numeric': 'type-numeric',
        'formatting/tokenizer': 'type-formatting',
        'mixed': 'type-mixed',
        'unclear': 'type-unclear'
      };

      const escapeHtml = (value) => String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#039;');

      const formatInline = (value) => escapeHtml(value).replace(/`([^`]+)`/g, '<code>$1</code>');
      const tokenList = (tokens) => `<div class="token-list">${tokens.map((token) => `<code>${escapeHtml(token)}</code>`).join('')}</div>`;
      const sideLabel = (side) => side === 'positive_head' ? 'Positive head' : 'Negative tail';
      const stateCode = (index) => `State ${String(index).padStart(2, '0')}`;
      const countBy = (items, key) => items.reduce((acc, item) => {
        acc[item[key]] = (acc[item[key]] || 0) + 1;
        return acc;
      }, {});

      function renderKpis() {
        const sides = countBy(rows, 'side');
        const highConfidence = rows.filter((row) => row.confidence === 'High').length;
        const cards = [
          ['Recorded states', states.length, 'Input embedding + 31 block outputs + final norm'],
          ['Community instances', rows.length, 'Every R008 community classified exactly once'],
          ['Positive / negative', `${sides.positive_head} / ${sides.negative_tail}`, 'Separate state-local populations'],
          ['High-confidence labels', highConfidence, `${Math.round(highConfidence / rows.length * 100)}% of classifications`]
        ];
        document.getElementById('kpis').innerHTML = cards.map(([label, value, note]) => `
          <div class="kpi card"><div class="kpi-label">${label}</div><div class="kpi-value">${value}</div><div class="kpi-note">${note}</div></div>
        `).join('');
      }

      function svgElement(name, attributes = {}) {
        const element = document.createElementNS('http://www.w3.org/2000/svg', name);
        Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
        return element;
      }

      function renderCountChart() {
        const svg = document.getElementById('count-chart');
        [...svg.children].filter((child) => !['title', 'desc'].includes(child.tagName)).forEach((child) => child.remove());
        const width = 1120, height = 320;
        const margin = { top: 24, right: 90, bottom: 48, left: 44 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;
        const maximum = Math.max(...states.flatMap((state) => [state.positive_count, state.negative_count]));
        const yMax = Math.ceil(maximum / 5) * 5;
        const x = (index) => margin.left + (index / (states.length - 1)) * innerWidth;
        const y = (value) => margin.top + innerHeight - (value / yMax) * innerHeight;
        const styles = getComputedStyle(document.documentElement);
        const border = styles.getPropertyValue('--border').trim();
        const muted = styles.getPropertyValue('--muted').trim();
        const positive = styles.getPropertyValue('--positive').trim();
        const negative = styles.getPropertyValue('--negative').trim();

        for (let value = 0; value <= yMax; value += 5) {
          svg.appendChild(svgElement('line', { x1: margin.left, x2: width - margin.right, y1: y(value), y2: y(value), stroke: border, 'stroke-width': 1 }));
          const label = svgElement('text', { x: margin.left - 10, y: y(value) + 4, fill: muted, 'font-size': 12, 'text-anchor': 'end' });
          label.textContent = value;
          svg.appendChild(label);
        }
        states.forEach((state, index) => {
          if (index % 4 !== 0 && index !== states.length - 1) return;
          const label = svgElement('text', { x: x(index), y: height - 18, fill: muted, 'font-size': 12, 'text-anchor': 'middle' });
          label.textContent = String(state.index).padStart(2, '0');
          svg.appendChild(label);
        });
        const axisLabel = svgElement('text', { x: margin.left + innerWidth / 2, y: height - 2, fill: muted, 'font-size': 12, 'text-anchor': 'middle' });
        axisLabel.textContent = 'Recorded state';
        svg.appendChild(axisLabel);

        const series = [
          { key: 'positive_count', label: 'Positive head', color: positive },
          { key: 'negative_count', label: 'Negative tail', color: negative }
        ];
        series.forEach((item) => {
          const points = states.map((state, index) => `${x(index)},${y(state[item.key])}`).join(' ');
          svg.appendChild(svgElement('polyline', { points, fill: 'none', stroke: item.color, 'stroke-width': 3, 'stroke-linejoin': 'round', 'stroke-linecap': 'round' }));
          states.forEach((state, index) => {
            const circle = svgElement('circle', { cx: x(index), cy: y(state[item.key]), r: 4, fill: item.color, stroke: styles.getPropertyValue('--surface').trim(), 'stroke-width': 2, tabindex: 0 });
            const title = svgElement('title');
            title.textContent = `${stateCode(state.index)} · ${item.label}: ${state[item.key]} communities`;
            circle.appendChild(title);
            svg.appendChild(circle);
          });
          const end = states[states.length - 1];
          const label = svgElement('text', { x: width - margin.right + 10, y: y(end[item.key]) + 4, fill: item.color, 'font-size': 12, 'font-weight': 700 });
          label.textContent = end[item.key];
          svg.appendChild(label);
        });
      }

      function renderLegend() {
        document.getElementById('taxonomy-legend').innerHTML = taxonomy.map((type) => `
          <span class="badge ${typeClass[type]}">${escapeHtml(type)}</span>
        `).join('');
      }

      function renderHeatmap() {
        const side = document.getElementById('heat-side').value;
        const filtered = side === 'all' ? rows : rows.filter((row) => row.side === side);
        const counts = new Map();
        let maxCount = 1;
        states.forEach((state) => {
          const stateRows = filtered.filter((row) => row.state === state.index);
          taxonomy.forEach((type) => {
            const count = stateRows.filter((row) => row.structure_type === type).length;
            counts.set(`${state.index}|${type}`, count);
            maxCount = Math.max(maxCount, count);
          });
        });
        const header = `<thead><tr><th>State</th>${taxonomy.map((type) => `<th>${escapeHtml(type)}</th>`).join('')}<th class="num">Total</th></tr></thead>`;
        const body = states.map((state) => {
          const cells = taxonomy.map((type) => {
            const count = counts.get(`${state.index}|${type}`) || 0;
            const heat = Math.round(10 + (count / maxCount) * 58);
            return `<td><button type="button" class="heat-cell ${typeClass[type]}" style="--heat:${heat}%" data-state="${state.index}" data-type="${escapeHtml(type)}" aria-label="${stateCode(state.index)}, ${type}, ${count} communities">${count}</button></td>`;
          }).join('');
          const total = taxonomy.reduce((sum, type) => sum + (counts.get(`${state.index}|${type}`) || 0), 0);
          return `<tr><td class="nowrap"><strong>${stateCode(state.index)}</strong><br><span class="text-muted">${escapeHtml(state.name)}</span></td>${cells}<td class="num"><strong>${total}</strong></td></tr>`;
        }).join('');
        const table = document.getElementById('heatmap');
        table.innerHTML = header + `<tbody>${body}</tbody>`;
        table.querySelectorAll('.heat-cell').forEach((button) => button.addEventListener('click', () => {
          document.getElementById('state-filter').value = button.dataset.state;
          document.getElementById('type-filter').value = button.dataset.type;
          document.getElementById('side-filter').value = side;
          document.getElementById('search').value = '';
          document.getElementById('confidence-filter').value = 'all';
          page = 1;
          renderExplorer();
          document.getElementById('explorer').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }));
      }

      function populateFilters() {
        const stateSelect = document.getElementById('state-filter');
        states.forEach((state) => stateSelect.insertAdjacentHTML('beforeend', `<option value="${state.index}">${stateCode(state.index)} · ${escapeHtml(state.name)}</option>`));
        const typeSelect = document.getElementById('type-filter');
        taxonomy.forEach((type) => typeSelect.insertAdjacentHTML('beforeend', `<option value="${escapeHtml(type)}">${escapeHtml(type)}</option>`));
        const confidenceSelect = document.getElementById('confidence-filter');
        confidences.forEach((confidence) => confidenceSelect.insertAdjacentHTML('beforeend', `<option value="${confidence}">${confidence}</option>`));
      }

      function filteredRows() {
        const query = document.getElementById('search').value.trim().toLocaleLowerCase();
        const state = document.getElementById('state-filter').value;
        const side = document.getElementById('side-filter').value;
        const type = document.getElementById('type-filter').value;
        const confidence = document.getElementById('confidence-filter').value;
        return rows.filter((row) => {
          if (state !== 'all' && String(row.state) !== state) return false;
          if (side !== 'all' && row.side !== side) return false;
          if (type !== 'all' && row.structure_type !== type) return false;
          if (confidence !== 'all' && row.confidence !== confidence) return false;
          if (!query) return true;
          return `${row.identity} ${row.top_tokens.join(' ')} ${row.evidence} ${row.community_id} ${row.state_name}`.toLocaleLowerCase().includes(query);
        });
      }

      function renderExplorer() {
        const matches = filteredRows();
        const pageCount = Math.max(1, Math.ceil(matches.length / pageSize));
        page = Math.min(page, pageCount);
        const start = (page - 1) * pageSize;
        const visible = matches.slice(start, start + pageSize);
        document.getElementById('result-count').textContent = `${matches.length} matching communities`;
        document.getElementById('page-status').textContent = `Page ${page} of ${pageCount}`;
        document.getElementById('previous').disabled = page <= 1;
        document.getElementById('next').disabled = page >= pageCount;
        document.getElementById('community-body').innerHTML = visible.map((row) => `
          <tr>
            <td><strong>${stateCode(row.state)}</strong><br><span class="text-muted">${escapeHtml(row.state_name)}</span></td>
            <td><span class="badge ${row.side === 'positive_head' ? 'badge-positive' : 'badge-negative'}">${sideLabel(row.side)}</span></td>
            <td><code>${row.community_id}</code></td>
            <td class="num">${row.size.toLocaleString()}</td>
            <td>${escapeHtml(row.identity)}</td>
            <td>${tokenList(row.top_tokens)}</td>
            <td><span class="badge ${typeClass[row.structure_type]}">${escapeHtml(row.structure_type)}</span></td>
            <td>${escapeHtml(row.confidence)}</td>
            <td class="evidence">${formatInline(row.evidence)}</td>
          </tr>
        `).join('') || '<tr><td colspan="9">No communities match the current filters.</td></tr>';
      }

      function typeSummary(items) {
        const counts = countBy(items, 'structure_type');
        return taxonomy.filter((type) => counts[type]).map((type) => `<span class="badge ${typeClass[type]}">${escapeHtml(type)} · ${counts[type]}</span>`).join('');
      }

      function stateTable(items) {
        return `<div class="table-wrap"><table class="state-table"><thead><tr><th>Community</th><th class="num">Size</th><th>Broad identity</th><th>Top 10 tokens</th><th>Type</th><th>Confidence</th></tr></thead><tbody>${items.map((row) => `
          <tr><td><code>${row.community_id}</code></td><td class="num">${row.size.toLocaleString()}</td><td>${escapeHtml(row.identity)}</td><td>${tokenList(row.top_tokens)}</td><td><span class="badge ${typeClass[row.structure_type]}">${escapeHtml(row.structure_type)}</span></td><td>${escapeHtml(row.confidence)}</td></tr>
        `).join('')}</tbody></table></div>`;
      }

      function renderStateContent(details, state) {
        if (details.dataset.rendered) return;
        const stateRows = rows.filter((row) => row.state === state.index);
        const positive = stateRows.filter((row) => row.side === 'positive_head');
        const negative = stateRows.filter((row) => row.side === 'negative_tail');
        details.querySelector('.state-content').innerHTML = `
          <div class="state-grid">
            <div><h3 class="positive">Positive head · ${positive.length}</h3><div class="state-type-row">${typeSummary(positive)}</div>${stateTable(positive)}</div>
            <div><h3 class="negative">Negative tail · ${negative.length}</h3><div class="state-type-row">${typeSummary(negative)}</div>${stateTable(negative)}</div>
          </div>`;
        details.dataset.rendered = 'true';
      }

      function renderStateSummaries() {
        const container = document.getElementById('state-summaries');
        states.forEach((state) => {
          const details = document.createElement('details');
          details.innerHTML = `<summary><span>${stateCode(state.index)} · ${escapeHtml(state.name)}</span><span class="state-counts">${state.positive_count} positive · ${state.negative_count} negative · ${state.total_count} total</span></summary><div class="state-content"></div>`;
          details.addEventListener('toggle', () => { if (details.open) renderStateContent(details, state); });
          container.appendChild(details);
        });
      }

      function resetFilters() {
        ['state-filter', 'side-filter', 'type-filter', 'confidence-filter'].forEach((id) => { document.getElementById(id).value = 'all'; });
        document.getElementById('search').value = '';
        page = 1;
        renderExplorer();
      }

      renderKpis();
      renderCountChart();
      renderLegend();
      populateFilters();
      renderHeatmap();
      renderExplorer();
      renderStateSummaries();

      document.getElementById('heat-side').addEventListener('change', renderHeatmap);
      ['search', 'state-filter', 'side-filter', 'type-filter', 'confidence-filter'].forEach((id) => {
        document.getElementById(id).addEventListener(id === 'search' ? 'input' : 'change', () => { page = 1; renderExplorer(); });
      });
      document.getElementById('reset').addEventListener('click', resetFilters);
      document.getElementById('previous').addEventListener('click', () => { if (page > 1) { page -= 1; renderExplorer(); document.getElementById('explorer').scrollIntoView({ block: 'start' }); } });
      document.getElementById('next').addEventListener('click', () => { const count = Math.ceil(filteredRows().length / pageSize); if (page < count) { page += 1; renderExplorer(); document.getElementById('explorer').scrollIntoView({ block: 'start' }); } });
      window.addEventListener('beforeprint', () => document.querySelectorAll('#state-summaries details').forEach((details, index) => { details.open = true; renderStateContent(details, states[index]); }));
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', renderCountChart);
    })();
  </script>
</body>
</html>
'''


def render_report(payload: dict[str, object]) -> str:
    data = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")
    return (
        HTML_TEMPLATE.replace("__SOURCE_COMMIT__", SOURCE_COMMIT)
        .replace("__DATA__", data)
    )


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=script_dir / "runs" / RUN_DIR_NAME,
        help="R009 directory containing STATE_*.md files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output HTML path (defaults to RUN_DIR/R009_SUMMARY.html)",
    )
    parser.add_argument(
        "--community-networks",
        type=Path,
        default=(
            script_dir
            / "runs"
            / R008_DIR_NAME
            / "chatgpt_community_networks.json"
        ),
        help="R008 compact community-network JSON containing representative tokens",
    )
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    output = (args.output or run_dir / "R009_SUMMARY.html").resolve()
    payload = build_payload(run_dir, args.community_networks.resolve())
    output.write_text(render_report(payload), encoding="utf-8", newline="\n")
    side_counts = Counter(str(row["side"]) for row in payload["communities"])
    print(
        json.dumps(
            {
                "output": str(output),
                "bytes": output.stat().st_size,
                "states": len(payload["states"]),
                "communities": len(payload["communities"]),
                "positive_head": side_counts["positive_head"],
                "negative_tail": side_counts["negative_tail"],
                "communities_with_top_10_tokens": sum(
                    len(row["top_tokens"]) == 10
                    for row in payload["communities"]
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
