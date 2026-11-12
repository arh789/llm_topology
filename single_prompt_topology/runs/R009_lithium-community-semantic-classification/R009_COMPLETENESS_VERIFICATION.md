# R009 Completeness Verification

## Verification scope

This file records the post-classification completeness check required by
`R009_ANALYSIS_PROTOCOL.md`.

It does **not** perform cross-state semantic synthesis, coherence analysis,
SDA-3 role assignment, optimal-layer selection, or curvature interpretation.

## Result

**PASS**

R009 satisfies the protocol's completion criteria for the first-pass
state-local semantic classification stage.

## File coverage

- Required state indices: **00–32**
- State files present: **33 / 33**
- Missing state files: **0**
- Duplicate state indices: **0**
- Protocol file present: **yes**

The R009 directory contains the protocol plus one state-classification file for
every transformer state from the input embedding through final normalisation.

## Authoritative R008 community counts

Source:
`R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2/COMMUNITY_COUNTS_BY_STATE.md`

| Side | R008 authoritative instances | R009 classified instances | Status |
|---|---:|---:|---|
| positive_head | 392 | 392 | exact |
| negative_tail | 400 | 400 | exact |
| **Total** | **792** | **792** | **exact** |

## Exactly-once verification

For every state:

- the R009 positive-head community count was compared with the authoritative
  R008 positive-head count;
- the R009 negative-tail community count was compared with the authoritative
  R008 negative-tail count;
- community IDs were required to form the complete contiguous sequence
  `C0 ... C(n-1)` on each side;
- no duplicate community IDs were accepted;
- no expected community IDs were missing.

Result:

- states with count mismatches: **0**
- states with missing community IDs: **0**
- states with duplicate community IDs: **0**
- unclassified R008 community instances: **0**
- multiply classified R008 community instances: **0**

Therefore all **792** R008 state-local community instances are represented
**exactly once** in R009.

## Per-state count reconciliation

| State | Positive | Negative | Total |
|---:|---:|---:|---:|
| 00 | 12 | 10 | 22 |
| 01 | 12 | 13 | 25 |
| 02 | 14 | 13 | 27 |
| 03 | 11 | 15 | 26 |
| 04 | 12 | 13 | 25 |
| 05 | 13 | 14 | 27 |
| 06 | 13 | 13 | 26 |
| 07 | 12 | 12 | 24 |
| 08 | 13 | 12 | 25 |
| 09 | 13 | 12 | 25 |
| 10 | 13 | 14 | 27 |
| 11 | 14 | 12 | 26 |
| 12 | 11 | 13 | 24 |
| 13 | 12 | 13 | 25 |
| 14 | 13 | 13 | 26 |
| 15 | 9 | 13 | 22 |
| 16 | 11 | 12 | 23 |
| 17 | 13 | 10 | 23 |
| 18 | 12 | 12 | 24 |
| 19 | 13 | 11 | 24 |
| 20 | 12 | 11 | 23 |
| 21 | 12 | 11 | 23 |
| 22 | 11 | 12 | 23 |
| 23 | 13 | 11 | 24 |
| 24 | 12 | 12 | 24 |
| 25 | 11 | 10 | 21 |
| 26 | 12 | 12 | 24 |
| 27 | 10 | 12 | 22 |
| 28 | 11 | 10 | 21 |
| 29 | 9 | 12 | 21 |
| 30 | 11 | 12 | 23 |
| 31 | 11 | 13 | 24 |
| 32 | 11 | 12 | 23 |
| **Total** | **392** | **400** | **792** |

Every row matches the authoritative R008 count table.

## Output-schema verification

Every community table was checked for the required columns:

- Community
- Size
- Broad identity
- Structure type
- Confidence
- Evidence

Result:

- state files with missing community tables: **0**
- state files with schema mismatch: **0**
- community rows with missing size: **0**
- community rows with missing broad identity: **0**
- community rows with missing evidence: **0**

## Taxonomy verification

Every `Structure type` value was checked against the fixed R009 taxonomy:

- `semantic/topic`
- `lexical/morphological`
- `named-entity`
- `numeric`
- `formatting/tokenizer`
- `mixed`
- `unclear`

Result:

- invalid structure-type values: **0**

## Confidence verification

Every confidence value was checked against:

- `High`
- `Moderate`
- `Low`

Result:

- invalid confidence values: **0**

## Protocol-boundary verification

The descriptive pass was checked for premature cross-state interpretation.

No state file contains an explicit classification field assigning:

- Central
- Suppressed
- Adjacent
- HCU / Highly Correlated Unrelated
- Emerging

No pre-boundary state text contains explicit comparison with previous, earlier,
later or next states, or an across-states comparison.

The files retain explicit boundary statements reserving:

- cross-state persistence and trajectory analysis;
- semantic coherence judgement;
- SDA-3 role assignment;
- optimal-layer judgement;
- curvature interpretation

for the post-verification synthesis stage.

## Verification conclusion

The R009 first-pass classification stage is complete.

```
33 states
    ↓
392 positive-head community instances
+
400 negative-tail community instances
    ↓
792 / 792 classified exactly once
    ↓
schema valid
taxonomy valid
confidence valid
protocol boundary preserved
    ↓
R009 FIRST-PASS VERIFICATION: PASS
```

A subsequent project-owner `proceed` may now begin the cross-state
synthesis/coherence/SDA-3 analysis permitted by the protocol.
