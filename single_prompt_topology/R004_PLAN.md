# R004 pre-run plan: lithium full-curve cutoffs

- Registration status: `executed successfully — see execution record below`
- Plan timestamp: `2026-11-12T20:26:46+11:00`
- Timezone: `Australia/Sydney`
- Run number: `R004`
- Neutral run name: `lithium-full-curve-cutoffs`
- Expected run-directory prefix: `R004_lithium-full-curve-cutoffs__`
- Source run:
  `R002_lithium-static-basis-cutoff-feasibility__20261112T083025Z_pythia-6.9b_52ff8f97c2`
- Corrects the cutoff-use policy in:
  `R003_lithium-score-region-boundaries__20261112T090711Z_pythia-6.9b_52ff8f97c2`
- Ultimate capture source:
  `R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2`

## Question

What upper and lower elbow cutoffs are obtained at every recorded state when
the complete target-removed score distribution is analysed directly, and what
token regions result when those cutoffs are used without an additional
acceptance or rejection gate?

## Method

R004 is a CPU-only reanalysis of the verified R002 score matrix. For every
state it will:

1. Remove the exact target token.
2. Rank all remaining scores from highest to lowest and calculate one upper
   elbow using maximum normalized deviation below the endpoint chord.
3. Rank the same scores from lowest to highest, negate them so the sequence is
   descending by anti-alignment magnitude, and calculate one lower elbow using
   the same method.
4. Save both elbow ranks and scores unconditionally.
5. Assign exactly the first `upper_cutoff_rank` tokens to `positive_head` and
   exactly the first `lower_cutoff_rank` tokens from the negative end to
   `negative_tail`. All other retained tokens form `central_body`.
6. Regenerate boundary-token inspection rows, complete tail membership and
   layer-wise region trajectories.

R004 has no sign-restricted recalculation, agreement tolerance, stability
class, accepted/rejected status or blank cutoff field. Elbow strength and local
slope ratio are descriptive measurements only and cannot remove a cutoff.

## Success criteria

- The R002 source manifest and every required source artifact pass identity,
  size and SHA-256 validation.
- All 33 states receive one valid upper and one valid lower cutoff.
- Region counts reconcile exactly with the 50,276 target-removed tokens at
  every state.
- Every required output is non-empty and recorded in a successful manifest
  with its size and SHA-256 hash.

## Interpretation boundary

The regions measure compatibility between one contextual target vector and the
static input-embedding basis. The calculated cutoffs are geometric elbows, not
validated semantic boundaries. Negative cosine means anti-alignment under this
measurement, not statistical, predictive or causal suppression.

## Outputs

- `manifest.json`
- `cutoffs.csv`
- `cutoff_tokens.csv`
- `tail_tokens.csv.gz`
- `token_region_trajectories.csv.gz`
- `figures/cutoff_overview.png`
- `figures/score_regions_selected_states.png`

## Production command

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\full_curve_cutoffs.py
```

## Out of scope

R004 does not run the transformer, load model weights, recalculate the R002
score matrix, introduce another prompt or model, test semantic enrichment,
perform topic modelling, or claim that a geometric elbow is semantically
optimal.

## Execution record

- Run ID:
  `R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2`
- Started: `2026-11-12T09:27:01.306888+00:00`
- Completed: `2026-11-12T09:27:13.162542+00:00`
- Status: `successful`
- Required components: `5 successful of 5`
- Source artifacts: `3 of 3 hash-validated`
- Output artifacts: `6 of 6 independently hash-validated`
- Upper cutoffs: `33 of 33 calculated and used`
- Lower cutoffs: `33 of 33 calculated and used`
- Model forward executed: `false`
- Model weights loaded: `false`
- Source score matrix recalculated: `false`

R004 produced 191,872 tail-membership rows and 804,012 trajectory rows for
24,364 union tokens. Its cutoff ranks exactly match R003's full-distribution
candidate ranks; R004 changes their use by removing the secondary acceptance
gate and assigning membership by exact rank.

The manifest's `pre_run_plan_sha256` records this file as it existed when the
run began. The execution record above was appended after successful completion.
