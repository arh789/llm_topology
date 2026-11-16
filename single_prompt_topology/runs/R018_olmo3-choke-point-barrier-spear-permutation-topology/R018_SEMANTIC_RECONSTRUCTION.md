# R018 semantic reconstruction

## Strongest result

R018 supports **higher-order semantic reconstitution under prompt-order perturbation**.

The six permutations do not preserve one literal semantic map. Instead, the final concept controls the strongest early literal branch, the trajectories diverge through the middle layers, and they then reconverge sharply near the end.

The lowest common late structure supported across all six permutations is:

```text
CONSTRAINT / REQUIREMENT
STRUCTURAL CONFIGURATION
DYNAMIC PATH GEOMETRY
COLLAPSE / ADJUSTMENT
```

Literal `spear`, attack/interception, route and intersection structure do **not** survive as 6/6 late invariants and are excluded from the core map.

## Quantitative trajectory

State 00 is identical across all six prompts.

The strongest final-position effect occurs at State 03:

- mean membership Jaccard, same final concept: 0.729285
- mean membership Jaccard, different final concept: 0.353508
- difference: 0.375777

Cross-order divergence is strongest around the middle of the network trajectory:

- State 18 mean membership Jaccard: 0.240937
- State 18 mean edge Jaccard: 0.084986
- minimum mean hidden-state cosine occurs at State 15: 0.712484

The trajectories then reconverge:

- State 64 mean membership Jaccard: 0.663480
- State 64 mean edge Jaccard: 0.426391
- State 64 mean hidden-state cosine: 0.969007
- State 64 same-final membership Jaccard: 0.704703
- State 64 different-final membership Jaccard: 0.653175
- final-position gap falls to 0.051529

At State 64, 2,610 of 6,619 positive-sector tokens (39.43%) and 2,785 of 6,847 negative-sector tokens (40.67%) occur in all six permutations. Exact edge invariance is lower: 9,719 of 68,034 positive edges (14.29%) and 10,685 of 69,777 negative edges (15.31%) occur in all six.

## Independent permutation reconstructions

The following descriptions were reconstructed from each permutation's measured communities before cross-permutation alignment. They preserve the strong order-conditioned literal branch rather than forcing one common ontology.

| Prompt | Early literal branch | Late recurrent structure |
| --- | --- | --- |
| ABC | weapon / blade / spear / stabbing | requirements and limitations; variables and trajectories; implementations/modules; collapse/adjustment |
| ACB | walls / boundary / barrier / entrance / restriction | structures and variables; conditions/requirements; movement/separation/curves; collapse/adjustment |
| BAC | sword / knife / blade / spear / weapon | infrastructure/deployment; requirements; trajectories/velocity/curves; adjustment/collapse |
| BCA | limits / constraints / bottleneck / location / position | configuration/transformation; requirements; variables/velocity/rectangles; collapse |
| CAB | roads / pathways / entrance / barrier | infrastructure/configuration; requirements/parameters; trajectories/curves/velocities; merging/collapse |
| CBA | point / location / direction / position | configuration/parameters/modules; requirements/limitations; trajectories/velocities/curves; merging/collapse |

The early branches group by **final concept**:

```text
spear final       -> weapon / blade / piercing vocabulary
barrier final     -> wall / boundary / restriction / passage vocabulary
choke-point final -> point / location / bottleneck / limit vocabulary
```

This is measured positional conditioning, not an invariant semantic parent.

## Cross-permutation invariant parents

### N1 — Constraint / Requirement

Late 6/6 support includes:

`require`, `requires`, `requirements`, `limitations`, `dependencies`, `constraints`, `conditions`, `shortcomings`.

This family is strongest in States 62–64 and is recovered in every permutation.

### N2 — Structural Configuration

Late 6/6 support includes:

`configuration`, `infrastructure`, `modules`, `interfaces`, `installations`, `structures`, `architectures`, `projects`.

This family becomes especially explicit in the final states.

### N3 — Dynamic Path Geometry

Late 6/6 support includes:

`point`, `approach`, `flow`, `trajectory`, `curve`, `velocity` and closely related speed/rectangle terms.

It is strongest before the final normalisation state, particularly States 56–63.

### N4 — Collapse / Adjustment

The stem `collaps-` occurs in late positive communities for **all six permutations at every State 56–63**.

It is repeatedly accompanied by `normalization`, `adjustment`, `tweak`, `merging`, `restructuring`, `transformation` and related change operators.

## Minimum semantic map

```text
             STRUCTURAL CONFIGURATION
                      |
                      | recurrent coupling
                      |
             CONSTRAINT / REQUIREMENT
                      |
                      | recurrent coupling
                      |
              COLLAPSE / ADJUSTMENT
                      |
                      | recurrent coupling
                      |
             DYNAMIC PATH GEOMETRY
       point / approach / flow / trajectory
              curve / velocity
```

The lines denote recurrent semantic association and community coupling. They do not claim causal direction.

## Relation evidence

### Constraint / Requirement ↔ Structural Configuration

At State 64 the relevant families are directly connected or fused in all six permutations. Representative measured positive-sector intercommunity evidence:

- ABC: C0–C6 = 365 edges; C0–C7 = 408; C6–C7 = 326
- ACB: C5–C7 = 326 edges
- BAC: C2–C4 = 501 edges
- BCA: C3–C5 = 502 edges
- CAB: C2–C9 = 338 edges; C4–C9 = 212
- CBA: C0–C6 = 520 edges

### Collapse / Adjustment ↔ Dynamic Path Geometry

The relation is strongest around State 63, where trajectories, curves, velocities and points repeatedly neighbour or fuse with normalisation, adjustment, merging and collapse:

- ABC: relevant C6–C12 = 139 edges; C2–C12 = 199
- ACB: C9–C13 = 63; C10–C13 = 43
- BAC: C6–C7 = 215
- BCA: dynamic/change terms fuse within C0 and connect to C4 with 509 edges
- CAB: C10–C13 = 47; C9–C10 = 156
- CBA: dynamic/change terms fuse within C7; C7–C10 = 215

### Constraint / Requirement ↔ Collapse / Adjustment

This relation is frequently represented by same-community fusion rather than a stable one-to-one intercommunity edge: late communities repeatedly combine `requires`, `creates`, `removes`, `increases`, `normalization`, `adjustments`, `merging` or `collaps-`. It is therefore retained as a recurrent association, not a directional relation.

## What does not survive

These structures are not strict late 6/6 invariants:

- exact `spear`: 0/6 late support in States 56–64
- attack/interception vocabulary: 2/6 late support
- intersection: 1/6 late support
- route/pathway/road vocabulary: 0/6 late support
- deployment: 5/6 late support

They remain useful evidence about order-conditioned trajectories but are excluded from the invariant core.

## State 00 control

State 00 is exactly identical across all permutations and contains generic vocabulary-basis communities such as system/information, common verbs, punctuation and code/formatting structures.

The four-family late organisation above is not present as the same organised topology at State 00. The result is therefore not reducible to the shared newline embedding baseline.

## Abstraction control

The reconstruction deliberately stops at the lowest common structures that recur across all six orders.

It does **not** promote the evidence into a broader tactical, causal or narrative system. In particular, the disappearance of literal spear/attack semantics from the 6/6 late invariant prevents a defensible claim that the common map is fundamentally an attack/interception architecture.

## Conclusion

R018 demonstrates a three-stage trajectory:

```text
FINAL-POSITION CONDITIONING
          ↓
MIDDLE-LAYER DIVERGENCE
          ↓
LATE HIGHER-ORDER RECONVERGENCE
```

The stable object is not a literal ordering of the supplied concepts. It is a more abstract but still traceable structural schema coupling **constraints, configuration, dynamic path geometry and collapse/adjustment**.

This supports the project's central hypothesis at the level tested by R018: lower-level representations are strongly order-dependent while a higher-order semantic topology reconstitutes across the perturbation.
