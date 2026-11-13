# R010 Phase A completeness verification

## Verification status

**OVERALL STATUS: FAIL — REPAIR REQUIRED BEFORE PHASE B**

The Phase-A corpus is mechanically complete and internally reconciled, but it
does not yet satisfy R010's mandatory state-isolation control.

Exactly two state reconstructions explicitly record incidental semantic-source
exposure to the following state:

- **State 06** — State 07 `community_nodes.csv` rows were returned in two
  retrieval responses after the requested State 06 range overran. The State 06
  file records that State 07 evidence was **not used** in inference.
- **State 07** — part of the State 08 layer packet was returned when a
  programmatic section trim failed. The State 07 file records that State 08
  evidence was **not used** in inference.

Non-use prevents an analytical dependency, but the R010 contamination control
is stricter: during Phase A the analysis must not inspect semantic content from
another state. Both state files explicitly record a strict source-isolation
breach. Therefore Phase A cannot receive a strict PASS until States 06 and 07
are independently rerun without cross-state source exposure and the
completeness verification is repeated.

Phase B remains blocked.

## Scope

This verification inspected the frozen R010 Phase-A state files only for
completeness, accounting, protocol compliance and recorded procedural
integrity. It did **not** compare parent identities across states and did not
infer persistence, strengthening, weakening, split, merge, appearance,
disappearance, side change or any other Phase-B trajectory relation.

Source corpus:

- R010 protocol: `R010_ANALYSIS_PROTOCOL.md`
- R010 state reconstructions: State 00 through State 32
- R009 authoritative completeness record:
  `R009_COMPLETENESS_VERIFICATION.md`

## File completeness

Expected R010 Phase-A state files: **33**

Observed state files:

- State 00: input embedding
- States 01–31: block 0 through block 30 outputs
- State 32: final normalisation after block 31

Result: **33 / 33 present**

Missing state files: **0**

Duplicate state indices: **0**

Unexpected State 33/raw block-31 file: **0**

## Community completeness

The community disposition tables were parsed independently from the per-state
verification claims.

R010 disposition-table rows:

- States 00–10: **279**
- States 11–21: **263**
- States 22–32: **250**
- **Total: 792**

R009 authoritative community population:

- positive-head: **392**
- negative-tail: **400**
- **Total: 792**

Result: **792 / 792 community instances accounted for**

Within every state:

- disposition-table row count equals the state's claimed community count;
- each side/community identifier is unique;
- duplicate primary dispositions = **0**;
- unassigned communities = **0**;
- each community has exactly one recognised primary disposition.

Community accounting result: **PASS**

## Node accounting

For every state, the community sizes in the disposition table were summed
independently by side and compared with the committed state verification.

States with positive-node mismatch: **0**

States with negative-node mismatch: **0**

States with total node-accounting mismatch: **0**

Node accounting result: **PASS**

## Parent identifier verification

For each state and side, parent identifiers were derived from the primary
community dispositions and checked for state-local contiguity.

Required forms:

- positive: `P+0, P+1, ...`
- negative: `P-0, P-1, ...`

States with non-contiguous positive parent identifiers: **0**

States with non-contiguous negative parent identifiers: **0**

Cross-state identity continuity was **not** inferred from matching local IDs.

Parent identifier result: **PASS**

## Parent coverage verification

For every retained parent in all 33 state files, the following were
recalculated directly from the community disposition table:

1. primary child node count;
2. side-relative coverage;
3. semantic-eligible coverage, excluding `formal-substrate` and `unclear`.

Reported percentages were accepted only within rounding tolerance.

Parents with primary-node mismatch: **0**

Parents with side-relative coverage mismatch: **0**

Parents with semantic-eligible coverage mismatch: **0**

Coverage result: **PASS**

## Population-disposition verification

Every state uses the exclusive primary dispositions defined by the protocol:

- `parent:<parent-id>`
- `formal-substrate`
- `irreducible-semantic`
- `mixed-unresolved`
- `unclear`

Because primary assignment is exclusive, retained-parent coverage is
non-overlapping. Secondary links were not counted as primary coverage.

States with duplicate primary assignments: **0**

States with unassigned communities: **0**

Population-disposition result: **PASS**

## Anti-vacuity and alternatives

Every retained parent must have an exclusion boundary.

For all 33 state files, the number of recorded exclusion boundaries was checked
against the number of retained parents.

States missing a retained-parent exclusion boundary: **0**

Every state file contains an `Alternative reconstruction` section. Across the
corpus, every retained parent whose confidence contains `Moderate` or `Low`
occurs in a state with an explicit alternative reconstruction.

Anti-vacuity/alternative result: **PASS**

## Phase-A interpretation boundaries

Every state verification was checked for the required zero-claim boundaries.

States with cross-state continuity claims: **0**

States with SDA-3 role assignments: **0**

States with optimal-layer claims: **0**

States with curvature claims: **0**

No Phase-B trajectory synthesis was performed during this verification.

Interpretation-boundary result: **PASS**

## State-isolation integrity

### State 06 — FAIL

The State 06 reconstruction explicitly records that the final requested State
06 source range returned some State 07 community rows. The later-state rows
were not used, but semantic content from another state was exposed during the
State 06 reconstruction.

Protocol requirement violated:

> During Phase A, the analysis of State N must be independent of inferred R010
> structures for every other state, and semantic content from other states must
> not be inspected as evidence during construction.

State 06 analytical dependence on State 07: **none recorded**

State 06 procedural source-isolation breach: **yes**

Disposition: **clean rerun required**

### State 07 — FAIL

The State 07 reconstruction explicitly records that a failed packet-section
trim returned part of the State 08 packet. The State 08 content was not used,
but semantic content from the next state was exposed during State 07
construction.

State 07 analytical dependence on State 08: **none recorded**

State 07 procedural source-isolation breach: **yes**

Disposition: **clean rerun required**

### All other states

No other recorded strict source-isolation breach was found in the Phase-A state
corpus.

State-isolation result: **FAIL — States 06 and 07 require repair**

## Completion-criteria matrix

| Criterion | Result | Evidence |
|---|---|---|
| All 33 state files exist | PASS | 33 / 33 |
| Every community has one primary disposition | PASS | 792 / 792 |
| All R009 community instances accounted for | PASS | 792 / 792 |
| Primary node coverage reconciles | PASS | 0 mismatches |
| Side-relative coverage reconciles | PASS | 0 mismatches |
| Semantic-eligible coverage reconciles | PASS | 0 mismatches |
| Parent IDs state-local and contiguous | PASS | 0 violations |
| Every retained parent has exclusion boundary | PASS | 0 violations |
| Moderate/Low structures have alternatives where material | PASS | explicit alternatives present |
| No cross-state evolution inferred | PASS | 0 claims |
| No SDA-3 role assigned | PASS | 0 assignments |
| No optimal-layer claim | PASS | 0 claims |
| No curvature claim | PASS | 0 claims |
| Mandatory Phase-A state isolation preserved | **FAIL** | State 06, State 07 |

## Repair prescription

Phase B must **not** begin.

The minimum repair sequence is:

1. independently rerun **State 06 — Block 5 output** using only State 06
   R009/R008 semantic evidence;
2. independently rerun **State 07 — Block 6 output** using only State 07
   R009/R008 semantic evidence;
3. replace the contaminated State 06 and State 07 R010 files with the clean
   reconstructions;
4. repeat R010 Phase-A completeness verification;
5. begin Phase B only if the repeated verification passes.

The clean reruns must not inspect the existing State 06/07 R010 parent
reconstructions while constructing the replacement hypotheses; the reconstruction
should be regenerated from R008/R009 evidence and only compared for file
replacement after the new state-local hypothesis is frozen.

No other state requires rerun on the evidence found in this verification.

## Boundary

This artifact is a **Phase-A verification record**, not a Phase-B synthesis.

No parent correspondence across states has been inferred. No trajectory,
coherence, SDA-3, optimal-layer or curvature conclusion is made here.

**Final Phase-A verification result: FAIL — repair States 06 and 07, then
reverify.**
