# R010 Phase D — curvature and coherence measurement results

## Status

**PRIMARY PHASE-D MEASUREMENT PASS COMPLETE**

This report applies the frozen R010_PHASE_D_MEASUREMENT_PROTOCOL.md without changing its definitions after inspecting results.

Scores are percentile-based and range from 0 to 1. They are relative rankings within this 33-state capture, not absolute physical quantities.

## Executive result

The four quantities do not collapse onto one trajectory.

- **Geometric curvature** is highest at the two endpoint resets and is concentrated internally in the early/middle transformer.
- **Partition curvature** peaks at S16→S17 and S15→S16, with S22→S23 also very high.
- **Semantic curvature** peaks internally at S08→S09 and S26→S27.
- **Coherence difficulty** peaks at different states on each side: positive S13, negative S10, combined S09.

The central result is:

> **High curvature does not always resolve coherence difficulty. It can create, expose or resolve conflict depending on the transition.**

## Curvature rankings

### Geometric curvature — full run

| Rank | Transition | Combined | Positive | Negative |
|---:|---|---:|---:|---:|
| 1 | S00→S01 | 1.000 | 1.000 | 1.000 |
| 2 | S31→S32 | 0.866 | 0.946 | 0.785 |
| 3 | S13→S14 | 0.742 | 0.806 | 0.677 |
| 4 | S03→S04 | 0.726 | 0.645 | 0.806 |
| 5 | S08→S09 | 0.726 | 0.688 | 0.763 |
| 6 | S12→S13 | 0.710 | 0.753 | 0.667 |
| 7 | S10→S11 | 0.694 | 0.763 | 0.624 |
| 8 | S09→S10 | 0.677 | 0.645 | 0.710 |

### Partition curvature — full run

| Rank | Transition | Combined | Positive | Negative |
|---:|---|---:|---:|---:|
| 1 | S16→S17 | 0.790 | 0.782 | 0.798 |
| 2 | S00→S01 | 0.774 | 0.548 | 1.000 |
| 3 | S15→S16 | 0.694 | 0.919 | 0.468 |
| 4 | S22→S23 | 0.694 | 0.831 | 0.557 |
| 5 | S03→S04 | 0.625 | 0.532 | 0.718 |
| 6 | S10→S11 | 0.617 | 0.387 | 0.847 |
| 7 | S23→S24 | 0.605 | 0.476 | 0.734 |

### Semantic curvature — full run

| Rank | Transition | Combined | Positive | Negative |
|---:|---|---:|---:|---:|
| 1 | S08→S09 | 0.704 | 0.688 | 0.720 |
| 2 | S02→S03 | 0.672 | 0.613 | 0.731 |
| 3 | S26→S27 | 0.664 | **0.898** | 0.430 |
| 4 | S17→S18 | 0.634 | 0.742 | 0.527 |
| 5 | S01→S02 | 0.621 | 0.554 | 0.688 |
| 6 | S22→S23 | 0.581 | **0.796** | 0.366 |
| 7 | S14→S15 | 0.575 | 0.656 | 0.495 |
| 8 | S30→S31 | 0.570 | **0.720** | 0.419 |

S21→S22 is also important despite a lower combined rank: positive semantic curvature is **0.731** while positive geometric curvature is only **0.054**.

## State-local coherence difficulty

### Highest combined states

| Rank | State | Combined | Positive | Negative |
|---:|---|---:|---:|---:|
| 1 | S09 | **0.740** | 0.688 | 0.792 |
| 2 | S10 | **0.685** | 0.484 | **0.885** |
| 3 | S13 | **0.672** | **0.969** | 0.375 |
| 4 | S26 | **0.667** | **0.719** | 0.615 |
| 5 | S27 | **0.607** | 0.672 | 0.542 |
| 6 | S00 | 0.578 | 0.406 | 0.750 |
| 7 | S15 | 0.578 | 0.667 | 0.490 |
| 8 | S17 | 0.563 | 0.500 | 0.625 |
| 9 | S22 | 0.560 | **0.745** | 0.375 |
| 10 | S07 | 0.555 | 0.266 | **0.844** |

Highest positive states: S13, S22, S26, S25, S09, S12, S27, S15, S32, then S24/S29/S30.

Highest negative states: S10, S08, S07, S09, S00, S03, S04, S17, then S05/S26.

## Strongest coherence-resolution transitions

Positive resolution means the destination state has lower coherence difficulty.

### Combined

| Rank | Transition | Resolution |
|---:|---|---:|
| 1 | S10→S11 | **+0.307** |
| 2 | S27→S28 | **+0.284** |
| 3 | S13→S14 | **+0.281** |
| 4 | S17→S18 | +0.167 |
| 5 | S00→S01 | +0.161 |
| 6 | S18→S19 | +0.138 |
| 7 | S22→S23 | +0.135 |

Positive-side largest reductions:
- S13→S14: **+0.604**
- S27→S28: **+0.370**
- S22→S23: **+0.313**
- S18→S19: **+0.245**
- S09→S10: **+0.203**
- S15→S16: **+0.172**

Negative-side largest reductions:
- S10→S11: **+0.667**
- S17→S18: **+0.396**
- S00→S01: **+0.318**
- S05→S06: **+0.229**
- S27→S28: **+0.198**
- S23→S24: **+0.146**

## Transitions that increase difficulty most

Largest combined increases:

- S21→S22: **−0.224**
- S28→S29: **−0.203**
- S08→S09: **−0.201**
- S14→S15: **−0.188**
- S12→S13: **−0.169**
- S06→S07: **−0.167**

Several are high-curvature transitions. Curvature can therefore be a conflict-producing or conflict-exposing step, not only a resolution step.

## Association analysis

Spearman associations are exploratory and descriptive.

### Combined, internal transitions only

| Relation | Geometric | Partition | Semantic |
|---|---:|---:|---:|
| curvature → destination difficulty | ρ = 0.137 | ρ = 0.088 | **ρ = 0.320** |
| source difficulty → next curvature | ρ = 0.243 | **ρ = 0.502** | ρ = 0.233 |
| curvature → coherence resolution | ρ = 0.005 | ρ = 0.287 | ρ = −0.137 |

The strongest relationship is:

> **A difficult state tends to be followed by community repartitioning.**

### Positive side, internal transitions

| Relation | Geometric | Partition | Semantic |
|---|---:|---:|---:|
| curvature → destination difficulty | −0.097 | 0.206 | **0.373** |
| source difficulty → next curvature | −0.089 | 0.105 | **0.288** |
| curvature → resolution | −0.039 | −0.131 | −0.047 |

### Negative side, internal transitions

| Relation | Geometric | Partition | Semantic |
|---|---:|---:|---:|
| curvature → destination difficulty | 0.267 | 0.139 | **0.421** |
| source difficulty → next curvature | 0.353 | 0.369 | **0.487** |
| curvature → resolution | 0.086 | 0.106 | 0.063 |

The negative side shows the clearest conflict-response relationship.

## Candidate curvature-density composite

The largest equal-weight point composites are:

1. S00→S01 — 0.783
2. S31→S32 — 0.633
3. S12→S13 — 0.615
4. S08→S09 — 0.615
5. S16→S17 — 0.612
6. S01→S02 — 0.606
7. S02→S03 — 0.605

The highest three-transition local density occurs in the very early transformer, followed by the S08–S10 and S12–S17 regions.

### Judgement

**Do not use one curvature-density score as the primary explanatory variable.**

It obscures S21→S22, where geometry is extremely stable but semantic curvature and conflict are high. The three curvature dimensions should remain separate.

## Full combined transition table

| From | To | Geometric | Partition | Semantic | Composite | Coherence resolution |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1.000 | 0.774 | 0.575 | 0.783 | +0.161 |
| 1 | 2 | 0.645 | 0.552 | 0.621 | 0.606 | −0.013 |
| 2 | 3 | 0.554 | 0.589 | 0.672 | 0.605 | −0.104 |
| 3 | 4 | 0.726 | 0.625 | 0.298 | 0.550 | +0.081 |
| 4 | 5 | 0.516 | 0.500 | 0.427 | 0.481 | −0.039 |
| 5 | 6 | 0.468 | 0.343 | 0.460 | 0.423 | +0.104 |
| 6 | 7 | 0.430 | 0.375 | 0.374 | 0.393 | −0.167 |
| 7 | 8 | 0.634 | 0.484 | 0.562 | 0.560 | +0.016 |
| 8 | 9 | 0.726 | 0.415 | 0.704 | 0.615 | −0.201 |
| 9 | 10 | 0.677 | 0.569 | 0.441 | 0.562 | +0.055 |
| 10 | 11 | 0.694 | 0.617 | 0.427 | 0.579 | **+0.307** |
| 11 | 12 | 0.640 | 0.496 | 0.352 | 0.496 | −0.125 |
| 12 | 13 | 0.710 | 0.569 | 0.567 | 0.615 | −0.169 |
| 13 | 14 | 0.742 | 0.500 | 0.513 | 0.585 | **+0.281** |
| 14 | 15 | 0.538 | 0.464 | 0.575 | 0.526 | −0.188 |
| 15 | 16 | 0.393 | 0.694 | 0.548 | 0.545 | +0.044 |
| 16 | 17 | 0.478 | **0.790** | 0.567 | 0.612 | −0.029 |
| 17 | 18 | 0.462 | 0.589 | 0.634 | 0.562 | +0.167 |
| 18 | 19 | 0.328 | 0.315 | 0.406 | 0.349 | +0.138 |
| 19 | 20 | 0.360 | 0.266 | 0.481 | 0.369 | −0.146 |
| 20 | 21 | 0.172 | 0.125 | 0.320 | 0.206 | +0.068 |
| 21 | 22 | **0.048** | 0.399 | 0.554 | 0.334 | **−0.224** |
| 22 | 23 | 0.328 | 0.694 | 0.581 | 0.534 | +0.135 |
| 23 | 24 | 0.543 | 0.605 | 0.444 | 0.530 | −0.008 |
| 24 | 25 | 0.129 | 0.512 | 0.476 | 0.372 | −0.117 |
| 25 | 26 | 0.462 | 0.504 | 0.484 | 0.483 | −0.117 |
| 26 | 27 | **0.210** | 0.560 | **0.664** | 0.478 | +0.060 |
| 27 | 28 | 0.344 | 0.544 | 0.478 | 0.456 | **+0.284** |
| 28 | 29 | 0.403 | 0.480 | 0.446 | 0.443 | **−0.203** |
| 29 | 30 | 0.349 | 0.310 | 0.317 | 0.326 | −0.021 |
| 30 | 31 | 0.425 | 0.169 | **0.570** | 0.388 | +0.034 |
| 31 | 32 | **0.866** | 0.573 | 0.460 | 0.633 | −0.018 |

## Interpretation boundary

These scores do not measure literal differential-geometric curvature or conscious uncertainty.

They describe abrupt change and compression resistance in the measured/inferred representation.
