# R003 pre-run plan: lithium score-region boundaries

- Registration status: `planned — housekeeping complete; implementation and execution not started`
- Current execution status: `successful — see execution record below`
- Plan timestamp: `2026-11-12T20:00:33+11:00`
- Timezone: `Australia/Sydney`
- Run number: `R003`
- Neutral run name: `lithium-score-region-boundaries`
- Expected run-directory prefix: `R003_lithium-score-region-boundaries__`
- Source run: `R002_lithium-static-basis-cutoff-feasibility__20261112T083025Z_pythia-6.9b_52ff8f97c2`
- Ultimate capture source: `R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2`
- Model identity inherited from R002: `EleutherAI/pythia-6.9b`
- Prompt SHA-256 inherited from R002:
  `52ff8f97c22b72506ca9b7acfb9be4450726157f1a31c6a4ce3e112380cd7bf7`
- Target token inherited from R002: token ID `27747`, decoded target ` lithium`

## Inferred question

For each recorded state, can the complete ranked cosine distribution define
reproducible upper and lower score thresholds that separate a high-compatibility
token population, a central background population and an anti-aligned token
population, and are those populations useful for tracking changes in the
static-input-basis compatibility of the contextual `lithium` representation?

## Source reuse and provenance

R003 is a derived CPU reanalysis of R002. It must validate the R002 manifest and
reuse these hashed artifacts wherever possible:

- `vocabulary_scores.safetensors`
- `vocabulary_tokens.csv`
- `state_metadata.csv`
- `cutoff_candidates.csv`
- `cutoff_summary.csv`

R003 must not execute a transformer forward pass, download or load model
weights, recalculate the `[33, 50277]` vocabulary score matrix, or alter R002.
The exact target token remains excluded from boundary calculation. R002's
full-curve, target-removed upper-elbow candidates are source measurements, not
values to be silently recomputed under a changed method.

## Planned calculation

For every recorded state:

1. Load and hash-validate the R002 vocabulary scores and token metadata.
2. Remove token ID `27747` and rank the remaining scores in descending order.
3. Reuse R002's valid `exact_target_removed` / `full` elbow as the primary
   upper-boundary candidate.
4. Apply the same maximum-normalized-chord-deviation calculation to only the
   scores greater than zero as an upper-boundary endpoint-sensitivity check.
5. Rank tokens by anti-alignment magnitude (`-cosine_score`) from the most
   negative score upward and calculate a full-distribution lower candidate.
6. Repeat the lower calculation using only scores below zero as its
   endpoint-sensitivity check.
7. Convert accepted elbow ranks into the original cosine-score thresholds.
8. Assign each token to `positive_head`, `central_body` or `negative_tail`.
9. Track region membership and boundary crossings across states without
   treating them as causal effects or evolving pairwise vocabulary geometry.

The sign boundary is used only to construct sensitivity checks. It is not a
claim that zero cosine is a statistical, predictive or causal threshold.

## Predeclared boundary decisions

Upper and lower boundaries are judged independently at each state.

A boundary is `accepted_geometric` when:

- both its full-distribution and sign-restricted candidates are valid interior
  elbows; and
- their relative rank difference, divided by their median rank, is at most
  `0.20`.

A boundary is `rejected_unstable` when either candidate is invalid or their
relative rank difference exceeds `0.20`. Elbow strength, local slope change and
boundary-token composition must be reported as diagnostics but will not be
used to move a boundary after inspection.

Each state receives one of these region results:

- `accepted_two_boundaries`
- `accepted_upper_only`
- `accepted_lower_only`
- `rejected_unstable`

Semantic coherence is a qualitative follow-on observation in R003, not a gate
that can convert an unstable geometric boundary into an accepted one.

## Successful outcome

R003 succeeds operationally when it completes every required component,
records a manifest with artifact hashes and produces the predeclared outputs.
A positive analytical outcome is one or two reproducible geometric boundaries
at most states, together with inspectable token populations and layer-wise
membership changes. A clear, documented rejection of the boundaries is also a
successful scientific result if the method ran as specified.

## Unsuccessful or inconclusive outcome

The analytical result is inconclusive when boundary locations are dominated by
the selected endpoint, sign-restricted and full candidates disagree beyond the
predeclared tolerance, or no interior elbow is available. The run itself is
unsuccessful if source validation fails, required outputs are absent, artifact
hashes are incomplete or an exception leaves any required component
unfinished.

## Out-of-scope indicators

Stop and record scope drift if R003 begins to require:

- another prompt, topic, model or transformer forward pass;
- topic modelling, clustering, graph-community detection or dimensionality
  reduction;
- output-logit, tuned-lens, attention, ablation or causal-suppression analysis;
- manual per-layer threshold adjustment after viewing token identities;
- centering, whitening or alternative embedding bases as part of the primary
  result;
- a claim that negative cosine means predictive or causal suppression; or
- a claim that R002 contains evolving pairwise contextual representations for
  all vocabulary tokens.

Centering, whitening and alternative cutoff algorithms may be proposed as
future sensitivity studies, but they are not part of R003.

## Planned output contract

The R003 run directory must contain:

- `manifest.json` — lineage, method, environment, component status and hashes;
- `region_boundaries.csv` — upper and lower candidates, agreement metrics,
  thresholds, strengths, population sizes and decisions for every state;
- `boundary_tokens.csv` — the 50 tokens immediately inside and outside each
  calculated boundary for inspection;
- `tail_tokens.csv.gz` — all positive-head and negative-tail memberships;
- `token_region_trajectories.csv.gz` — region and score trajectories for the
  union of tokens entering either tail at any state;
- `figures/region_boundaries_overview.png` — all state-level boundary ranks and
  decisions;
- `figures/score_regions_selected_states.png` — states 0, 8, 16, 24 and 32 with
  both boundaries overlaid; and
- any failure record required by the existing manifest discipline.

No R003 run directory exists at the end of this housekeeping phase. The next
authorized phase is implementation followed by validation, then execution.

## Execution record

- Run ID:
  `R003_lithium-score-region-boundaries__20261112T090711Z_pythia-6.9b_52ff8f97c2`
- Started: `2026-11-12T09:07:11.145737+00:00`
- Completed: `2026-11-12T09:07:20.569152+00:00`
- Status: `successful`
- Required components: `5 successful of 5`
- Source artifacts: `5 of 5 hash-validated`
- Output artifacts: `6 of 6 independently hash-validated`
- Model forward executed: `false`
- Model weights loaded: `false`
- Source score matrix recalculated: `false`

The pre-run method and decision thresholds above were not changed after result
inspection. Upper boundaries were accepted at 32 of 33 states and lower
boundaries at 29 of 33 states. Twenty-eight states accepted both boundaries,
four accepted only the upper boundary and one accepted only the lower boundary.
These are geometric decisions in the static input-embedding basis, not semantic
topic boundaries or evidence of token suppression.
