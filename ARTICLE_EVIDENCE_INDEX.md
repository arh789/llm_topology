# Article Claim–Evidence Index

Status: private working index, current through R019 on 2026-11-17.

This file is the shortest route from a proposed article claim to the evidence
that supports it. Relative links are intentional while the repository remains
private. At publication, they should be resolved against one frozen commit or
release tag rather than mutable `main`.

## Evidence levels

| Level | Meaning |
|---|---|
| **Measured** | Direct model capture or pipeline output. |
| **Derived** | Deterministic calculation from measured outputs. |
| **Interpreted** | Semantic identity, parent structure or explanatory synthesis assigned after measurement. |
| **Proposed** | Practical or causal implication not yet experimentally demonstrated. |

The article should never cite an interpreted artifact as though it were a
direct model measurement.

## Current article-level conclusion

The strongest supported conclusion is:

> Changing the order of the same concepts deterministically changes
> intermediate hidden states, vocabulary neighbourhoods and graph topology.
> Repeated identical prompts produce an exact measured noise floor in the
> tested local setup. Higher-order semantic families appear more stable across
> permutations than individual tokens, edges, communities or relations, but
> one invariant parent-relation graph has not yet been established.

## C1 — A large open base model can be instrumented locally

**Claim.** A pinned OLMo 3 32B Base model can expose all 65 required states and
the first-token logits for one short prompt on the local RTX 4090 system using
GPU, CPU and disk-backed placement.

- **Measured:** [R016 feasibility report](single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/R016_FEASIBILITY_REPORT.md)
  and [manifest](single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/manifest.json).
- **Protocol:** [R016 plan](single_prompt_topology/R016_PLAN.md).
- **Code:** [`r016_olmo3_32b_feasibility.py`](single_prompt_topology/r016_olmo3_32b_feasibility.py).
- **Boundary:** feasibility for a short, no-generation forward pass; not
  multi-prompt throughput or semantic validity.

## C2 — The observed order effect is deterministic, not sampling noise

**Claim.** Three sequential executions of each tested permutation produced
identical hidden states, vocabulary scores, final logits, cutoff memberships,
edges and seeded communities, while different concept orders diverged.

- **Measured summary:** [R019 result](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json)
  and [measurement report](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md).
- **Layerwise evidence:** [`divergence_by_state.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/divergence_by_state.csv),
  [hidden-state comparisons](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_hidden_state_metrics.csv),
  [vocabulary-score comparisons](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_vocabulary_score_metrics.csv),
  [next-token distribution comparisons](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_next_token_distribution_metrics.csv)
  and [topology comparisons](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_topology_metrics.csv).
- **Protocol and code:** [R019 plan](single_prompt_topology/R019_PLAN.md),
  [configuration](single_prompt_topology/run_configs/R019_olmo3-order-repeatability-control.json)
  and [`r019_repeatability_control.py`](single_prompt_topology/r019_repeatability_control.py).
- **Verification:** [R019 completeness verification](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_COMPLETENESS_VERIFICATION.md).
- **Boundary:** deterministic for this model, hardware, software path and
  no-generation experiment; not a universal determinism claim.

## C3 — Order-conditioned differentiation is followed by late reconvergence

**Claim.** The same concept set forms sharply different early and middle
representations depending on order and final position, then becomes
substantially more similar in late states.

- **Measured:** [R018 hidden-state comparisons](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_hidden_state_metrics.csv),
  [permutation comparisons](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_permutation_comparisons.csv)
  and [permutation invariance](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/permutation_invariance.csv).
- **Control:** R019's [divergence summary](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/divergence_by_state.csv).
- **Measured report:** [R018 measurement report](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_MEASUREMENT_REPORT.md).
- **Boundary:** reconvergence is similarity recovery, not proof that the six
  internal states become identical or semantically equivalent.

## C4 — Parent families are more stable than lower-level topology

**Claim.** Tokens, exact edges and community partitions remain strongly
order-conditioned, while independently reconstructed higher-order semantic
families recur more consistently.

- **Measured substrate:** [community nodes](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/community_nodes.csv),
  [community edges](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/community_edges.csv)
  and [permutation invariance](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/permutation_invariance.csv).
- **Run-level interpretation:** [R018 semantic reconstruction](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md)
  and [structured map](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP.json).
- **Current article-level qualification:** [MA-0114](META_ANALYSIS.md#ma-0114--chatgpt-revised-r018-semantic-analysis)
  concludes that the semantic basis is more stable than the relations between
  its parents.
- **Boundary:** parent identities are post-measurement semantic
  reconstructions. Their recurrence is evidence for a candidate learned
  semantic basis, not direct observation of physical parent nodes in the
  transformer.

## C5 — Some higher-order structure persists across changed context

**Claim.** The Qwen experiments recover recurring parent structures across
concept order, changed third-concept context and an adjacent semantic region.

- **Order perturbation:** [R013 plan](single_prompt_topology/R013_PLAN.md) and
  [measurement report](single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/R013_MEASUREMENT_REPORT.md).
- **Context perturbation:** [R014 plan](single_prompt_topology/R014_PLAN.md) and
  [measurement report](single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/R014_MEASUREMENT_REPORT.md).
- **Adjacent-region replication:** [R015 plan](single_prompt_topology/R015_PLAN.md),
  [measurement report](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_MEASUREMENT_REPORT.md)
  and [R014–R015 comparison](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R014_R015_COMPARISON.md).
- **Boundary:** this supports local continuity under the selected
  perturbations; it does not establish a global training-data topology.

## C6 — Measurement and interpretation were deliberately separated

**Claim.** The pipeline records model-derived evidence before semantic
classification and preserves validation failures rather than silently
repairing results.

- **Method:** [`METHODOLOGY.md`](METHODOLOGY.md).
- **Lifecycle control:** [R018 lifecycle verification](single_prompt_topology/R018_LIFECYCLE_UPDATE_VERIFICATION.md).
- **Validation recovery:** [R018 validation recovery](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_VALIDATION_RECOVERY.md)
  and [machine-readable record](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/validation_recovery.json).
- **Research history:** [`META_ANALYSIS.md`](META_ANALYSIS.md).
- **Boundary:** separation reduces interpretive contamination; it does not
  make model-generated semantic labels ground truth.

## Claims that remain proposed

The article may motivate these ideas, but should not present them as results:

- topology-guided prompt intervention improves answer quality;
- negative cosine establishes suppression;
- reconstructed parents are causal mechanisms;
- a specific training document or source can be recovered;
- the present local maps generalise to arbitrary topics or models;
- one transformer layer is universally optimal for semantic analysis.

## Figure provenance rule

Every published figure should state:

```text
source run
+ source CSV/JSON
+ generating code
+ model revision
+ commit or release tag
+ measured/derived/interpreted label
```

No public URL is assigned yet. Publication identifiers are deferred until the
private repository reaches its final state.
