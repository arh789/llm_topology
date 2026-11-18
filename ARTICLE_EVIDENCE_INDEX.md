# Article Claim–Evidence Index

Status: private working index, current through R020 on 2026-11-19.

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

Two complementary research findings now govern the article. The R013–R019
findings below remain in force; R020 adds a distinct test of recoverable
semantic information against generated expression.

**R013–R019 — structural sensitivity and recurrence:**

> Changing the order of the same concepts deterministically changes
> intermediate hidden states, vocabulary neighbourhoods and graph topology.
> Repeated identical prompts produce an exact measured noise floor in the
> tested local setup. Higher-order semantic families appear more stable across
> permutations than individual tokens, edges, communities or relations, but
> one invariant parent-relation graph has not yet been established.

**R020 — semantic availability, integration and expression:** A small model
generated a circular and unsuccessful answer even though measured networks
allowed reconstruction of recurring candidate relations among settlements,
movement/routes, crossings, built environments and inhabitants. Those relations
are intermittent; a consistently integrated hypothesis and a causal explanation
of the failure have not been established. The human usefulness judgement is
pending. See C7–C9 and [R020's final conclusion](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_FINAL_CONCLUSION.md).

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

## C7 — R020 makes internal associations inspectable despite an unsuccessful answer

**Claim.** Pythia 70M produced a circular, repeated response to the simple
question about why a city would build a bridge across a river. The same run
captured internal representations for every next-token decision, allowing the
output to be compared with measured representational networks.

- **Measured:** [R020 measurement report](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_MEASUREMENT_REPORT.md),
  [manifest](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/manifest.json),
  [generation trace](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/generation_trace.csv)
  and [completeness verification](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_COMPLETENESS_VERIFICATION.md).
- **Coverage:** 32 generated-token decisions, eight recorded states and two
  cosine sectors per decision: **512 networks** and **6,944 state-local
  communities**.
- **Protocol and correction:** [R020 run methodology](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_RUN_METHODOLOGY.md)
  and [validation amendment](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_VALIDATION_AMENDMENT.md).
- **Generated response and comparison:** [R020 generation-wide analysis](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md).
- **Boundary:** An unsuccessful continuation and measurable associations
  establish a representation–output contrast, not the usefulness of those
  associations, their relevance throughout generation or a causal explanation
  for the output. The frozen measurement report describes the status *before*
  the downstream semantic analyses were produced.

## C8 — Related semantic functions recur, but not as one continuous graph

**Claim.** Across generated-token decisions, independently evidenced
intercommunity relationships support a recurring candidate functional field
involving settlements, movement/routes, crossings, built places and inhabitants.
Its components and couplings are selectively reactivated and reorganised;
the reconstruction does not establish one uninterrupted, fully integrated
semantic hypothesis.

- **Measured substrate:** [R020 community edges](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/community_edges.csv)
  and [original network export](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/chatgpt_community_networks.json).
- **Reconstruction:** [Generation-wide hypothesis report](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md),
  [cross-generation trajectories](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_CROSS_GENERATION_HYPOTHESIS_TRAJECTORY.json)
  and [per-decision hypothesis map](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_PER_TOKEN_HYPOTHESIS_MAP.html).
- **Independent evidence reconciliation:** [R020 v3 relation audit](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_V3_INDEPENDENT_RELATION_EVIDENCE_AUDIT.md)
  checks **359/359** cited cross-community edge records, **2,353/2,353**
  cited community exemplar tokens and **359/359** normalised affinities
  against saved measured evidence, with no mismatches.
- **Qualifying result:** In the positive cosine sector at contextual states
  S01–S05, **21/32** decisions have at least one screened task-candidate
  relationship; **6/32** repeat the same relationship across multiple such
  states; **11/32** remain unresolved at the declared threshold. The most
  recurrent connections are movement/routes–settlements (**11 decisions**) and
  crossings/connections–movement/routes (**8 decisions**).
- **Boundary:** These are *interpreted* semantic functions supported by
  measured community edges, not directly observed semantic parent variables.
  Selection, thresholds and post-hoc labelling do not exhaust the available
  networks; failure to match a candidate does not prove absence.

## C9 — Semantic availability, integration and generative expression are distinct research questions

**Claim.** R020 provides evidence of semantic associations that the model's
visible answer fails to communicate, but it does **not** establish sustained
binding of city as an actor/beneficiary, bridge as a constructed means, river
as an obstacle and crossing as a purpose. A proposed integration failure is
therefore a candidate explanation, not a demonstrated mechanism.

- **Current run-level synthesis:** [R020 final conclusion](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_FINAL_CONCLUSION.md)
  and [generation-wide reconstruction](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md).
- **Audit and uncertainty:** [R020 v3 independent audit](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_V3_INDEPENDENT_RELATION_EVIDENCE_AUDIT.md).
  The targeted functional screen matches **818 of 6,944** communities, not
  every potential relation. Under that screen, **0/32** decisions have a
  qualifying task-candidate positive relation at S06–S07; the projection uses
  the *input* embedding basis while the model's input/output embeddings are
  untied, so that result does not demonstrate loss of task information.
- **Interpretive history:** [MA-0125](META_ANALYSIS.md#ma-0125--r020-final-semantic-reconstruction-project-level-contextual-conclusion)
  preserves the final R020 interpretation, while
  [MA-0126](META_ANALYSIS.md#ma-0126--core-insight-semantic-integration-as-both-research-object-and-research-method-failure-mode)
  offers the project-level hypothesis that the research process can itself
  encounter failures of semantic integration. MA-0126 is *methodological
  interpretation*, not a newly measured model mechanism.
- **Status boundary:** The first interpretation used post-hoc semantic
  categories and a label-shuffling sensitivity check, not blind semantic
  validation; one model, one prompt and a repeated continuation cannot establish
  universal behaviour. The human evaluation of whether the recovered
  relationships are **more useful** than the poor answer remains pending.
  The analysis evidence and human-utility status are separately recorded in
  [R020 analysis manifest](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_ANALYSIS_MANIFEST.json).

## Claims that remain proposed

The article may motivate these ideas, but should not present them as results:

- topology-guided prompt intervention improves answer quality;
- negative cosine establishes suppression;
- reconstructed parents are causal mechanisms;
- a specific training document or source can be recovered;
- the present local maps generalise to arbitrary topics or models;
- one transformer layer is universally optimal for semantic analysis;
- representational analysis generally produces more useful information than
  generated answers, rather than exposing additional candidate associations
  in this one test;
- a failure to bind semantic roles caused R020's circular output;
- output-proximal states lack prompt-related information merely because the
  selected input-basis projection fails to identify it;
- the human–agent methodology and Pythia 70M share an established causal
  failure mechanism, rather than a suggestive functional parallel.

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
