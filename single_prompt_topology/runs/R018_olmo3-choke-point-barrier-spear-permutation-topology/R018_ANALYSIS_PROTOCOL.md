# R018 independent semantic-analysis protocol

## Current lifecycle state

The R018 measurement phase is complete and frozen.

```text
measurement_status = measurement_successful
analysis_status    = not_started
run_status         = awaiting_semantic_analysis
```

R018 is not an overall completed research run until the independent semantic
reconstruction and final analysis defined here are complete. This protocol
extends the lifecycle of R018; it does not alter the historical measurement
contract in `R018_PLAN.md`.

## Controlling project objective

Determine whether changes in a model's internal state across transformer
layers can be used to infer the higher-order semantic relationships and
topology learned from its training data. The objective is not to recover
specific training documents.

R018 tests which structures survive all six order perturbations of:

- `A = choke point`
- `B = collapsible barrier`
- `C = spear`

## Division of responsibility

```text
CODEX
measure
→ validate
→ export semantic-free evidence
→ stop

CHATGPT
inspect measured evidence
→ independently reconstruct each permutation
→ compare them
→ infer invariant parents and relations
→ construct semantic map
→ write final analysis and report
```

Codex must not supply semantic parent identities or relations. ChatGPT must
not alter the frozen measurement evidence.

## Frozen evidence

Use these as primary compact evidence:

- `../chatgpt_community_networks.json`
- `../chatgpt_layer_packets.md`
- `../network_index.csv`
- `../community_nodes.csv`
- `../community_edges.csv`
- `../state_transitions.csv`
- `../pairwise_permutation_comparisons.csv`
- `../permutation_invariance.csv`

Consult the complete compressed node, membership and edge tables only where
the compact exports are insufficient. Keep measured facts and semantic
interpretations explicitly separate.

## Required analysis sequence

### 1. Independent permutation reconstruction

Analyse `ABC`, `ACB`, `BAC`, `BCA`, `CAB` and `CBA` independently.
Complete and save each first-pass reconstruction before using the other
permutations to influence its parent identities.

For each permutation:

- identify defensible state-local semantic structures;
- reconstruct higher-order parents and relations across depth;
- distinguish positive and negative cosine sectors without equating negative
  cosine with suppression;
- record confidence, ambiguity, mixed structures and artefacts; and
- identify the minimum functional or relational architecture supported by
  the measured evidence.

### 2. Cross-permutation matching

After all six independent reconstructions exist:

- match semantically corresponding parents;
- match parent-parent relations;
- distinguish invariant, recurrent, order-conditioned and final-position-
  conditioned structures;
- preserve unmatched or unresolved structures rather than forcing alignment;
  and
- link every match to the supporting permutation, state, sector and measured
  community identifiers.

### 3. Semantic-map construction

Construct a map whose:

- nodes are higher-order semantic structures;
- edges are learned relations between those structures;
- weights or confidence fields record perturbation support and evidence
  strength; and
- provenance connects every interpreted object to measured R018 evidence.

The map must state what survives presentation-order perturbation and what
remains order-dependent.

### 4. Final analysis

The final report must directly answer:

> Which higher-order semantic structures and relations persist across
> transformer depth and controlled input-order perturbation, and what do those
> persistent structures imply about the semantic topology learned from
> training?

SDA-3 or GRD may be compared only after the empirical semantic map has been
reconstructed. They must not determine the first-pass parent identities.

## Required outputs

```text
analysis/
├── analysis_manifest.json
├── permutations/
│   ├── ABC_SEMANTIC_RECONSTRUCTION.md
│   ├── ACB_SEMANTIC_RECONSTRUCTION.md
│   ├── BAC_SEMANTIC_RECONSTRUCTION.md
│   ├── BCA_SEMANTIC_RECONSTRUCTION.md
│   ├── CAB_SEMANTIC_RECONSTRUCTION.md
│   └── CBA_SEMANTIC_RECONSTRUCTION.md
├── cross_permutation_parent_matches.csv
├── cross_permutation_relation_matches.csv
├── R018_SEMANTIC_MAP_NODES.csv
├── R018_SEMANTIC_MAP_EDGES.csv
├── R018_SEMANTIC_MAP.json
└── R018_RUN_ANALYSIS_AND_RECOMMENDATIONS.html
```

## Completion gate

R018 becomes complete only when:

1. all six independent permutation reconstructions exist;
2. cross-permutation parent and relation matching is complete;
3. the semantic-map CSV and JSON representations reconcile;
4. the final HTML report answers the controlling project objective;
5. interpretive claims retain measured-evidence provenance;
6. the analysis manifest records the analysis model and source commit;
7. `analysis_status` is changed to `complete`; and
8. `run_status` is changed to `complete`.

Until then, the correct statement is:

> Measurement complete; R018 remains incomplete pending independent semantic
> reconstruction and final analysis.
