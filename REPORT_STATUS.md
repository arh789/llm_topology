# Report Status and Canonicality

Status: private article-facing register, current through R020 on 2026-11-19.

This file does not delete or rewrite earlier interpretations. It states which
artifact should govern a current article claim when later analysis narrowed or
qualified an earlier report.

## Status terms

| Status | Meaning |
|---|---|
| **Canonical measurement** | Current factual record of captured or derived numerical evidence. |
| **Canonical control** | Current result governing a confound or repeatability question. |
| **Current article interpretation** | Most conservative project-level semantic conclusion. |
| **Run-local interpretation** | Valid record of how one run was reconstructed, but not automatically the current project conclusion. |
| **Exploratory** | Useful hypothesis generation without the controls needed for a general claim. |
| **Historical** | Preserved research history; later evidence may supersede its factual status. |

## Current governing artifacts

### R020 — canonical measurement and output contrast

- [R020 measurement report](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_MEASUREMENT_REPORT.md)
- [Measurement manifest](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/manifest.json)
- [Generation trace](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/generation_trace.csv)
- [Completeness verification](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_COMPLETENESS_VERIFICATION.md)
- [Validation amendment](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_VALIDATION_AMENDMENT.md)

The Pythia 70M run captured 32 generated-token decisions, each with eight
recorded states and two cosine sectors (512 networks, 6,944 communities).
Its deterministic continuation was circular and did not answer why a city
would build a bridge.

**Historical-status warning:** The frozen R020 measurement report says that
semantic analysis is awaiting completion. That was correct *when the
measurement report was written*. Later downstream semantic reconstruction and
auditing now exist. Do not revise the frozen measurement report to conceal
this chronology, and do not treat its earlier status as the present overall
analysis status.

### R020 — current, evidence-bounded semantic interpretation

- [R020 final conclusion](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_FINAL_CONCLUSION.md)
- [Generation-wide semantic hypothesis report](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md)
- [Independent v3 relationship-evidence audit](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_V3_INDEPENDENT_RELATION_EVIDENCE_AUDIT.md)
- [Cross-generation trajectory data](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_CROSS_GENERATION_HYPOTHESIS_TRAJECTORY.json)
- [Analysis manifest](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_ANALYSIS_MANIFEST.json)

**Current conclusion:** Candidate relations among settlements, movement/routes,
crossings, built places and inhabitants recur intermittently across the
generated response, with different community and state realisations. They do
not form one continuously maintained, fully role-bound semantic graph under
the recorded reconstruction.

The selected positive-sector screen finds qualifying question-related
relationships in 21/32 decisions at S01–S05, and repetition of the same
relation across contextual states in 6/32. Eleven decisions do not qualify
at this threshold, which is *unresolved*, not proof of absent structure.
The strongest candidate relations are movement/routes–settlements (11
decisions) and crossings–movement/routes (8 decisions).

The independent audit verifies all **359 cited intercommunity edges**,
**2,353 cited exemplar tokens** and **359 reported affinities** against
recorded evidence. This establishes the accuracy of the cited evidence
references, not unique semantic labels or exhaustive coverage: the targeted
screen selects 818 of the 6,944 communities.

**Interpretation boundary:** The output is demonstrably poor; the recovered
candidate associations are observable beyond its wording. But the evidence
does not demonstrate that a fully integrated bridge-building explanation
persisted internally, that a role-binding failure caused generation to loop,
or that human usefulness exceeds the generated response in an independently
validated sense. The analysis was not blinded. No qualifying positive task
relations at S06–S07 under the input-embedding projection is not evidence
that the output-relevant representations contain none; Pythia's input and
output embedding matrices are untied. Human usefulness evaluation is still
pending.

### R020 — project-level methodological context, not additional measurement

- [MA-0125](META_ANALYSIS.md#ma-0125--r020-final-semantic-reconstruction-project-level-contextual-conclusion)
  records the R020 final synthesis in the chronological project history.
- [MA-0126](META_ANALYSIS.md#ma-0126--core-insight-semantic-integration-as-both-research-object-and-research-method-failure-mode)
  identifies a possible parallel between recoverable-but-poorly-integrated
  information in the experiment and incomplete integration during agent
  analysis.

MA-0126 is a **core methodological insight**, not a measured demonstration
that ChatGPT and Pythia share a causal failure mode. The article may use it
to explain why human judgement and iterative reconstruction matter, but must
not present it as a new controlled model result.

### R019 — canonical determinism control

- [`R019_RESULT.json`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json)
- [`R019_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md)
- [`R019_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_COMPLETENESS_VERIFICATION.md)

Current conclusion: `deterministic_order_effect_confirmed`. Identical repeats
were exact at all tested levels; different orders diverged.

### R018 — canonical measurement

- [`R018_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_MEASUREMENT_REPORT.md)
- [`manifest.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/manifest.json)
- [`R018_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_COMPLETENESS_VERIFICATION.md)
- [`validation_recovery.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/validation_recovery.json)

These govern numerical claims about coverage, order effects, final-position
conditioning, divergence and late reconvergence.

### R018 — current article interpretation

The governing project-level boundary is the later
[MA-0114 revised analysis](META_ANALYSIS.md#ma-0114--chatgpt-revised-r018-semantic-analysis):

> A perturbation-stable semantic basis survives permutation, while the
> relations and emphasis between those semantic components remain strongly
> order-conditioned.

The article may therefore claim stronger stability for parent families than
for tokens, edges, communities or parent-parent relations. It should not claim
that R018 established one fixed invariant graph.

### R018 — qualified run-local interpretation

The following artifacts preserve the earlier four-parent reconstruction:

- [`R018_SEMANTIC_RECONSTRUCTION.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md)
- [`R018_SEMANTIC_MAP.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP.json)
- [`R018_FINAL_REPORT.html`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_FINAL_REPORT.html)
- [`R018_SEMANTIC_NETWORK_GRAPH_REPORT.html`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_REPORT.html)

They remain evidence of the run's reconstruction process and a candidate
higher-order map. Their recurrent edges must not be presented as the current
project-level proof of invariant parent relations because MA-0114 materially
narrows that claim.

## Run-status overview (R013–R020)

| Run | Article-facing status | Proper use |
|---|---|---|
| R013 | Canonical Qwen order-perturbation measurement; downstream interpretation remains model- and probe-specific. | Establish that low-level topology is order-sensitive and parent families appeared more stable. |
| R014 | Canonical Qwen context-perturbation measurement plus local-map reconstruction. | Test recurrence under changed third-concept context. |
| R015 | Canonical adjacent-region replication and R014–R015 comparison. | Support local continuity with deformation, not a global map. |
| R016 | Canonical OLMo 3 32B feasibility result. | Establish local instrumentability only. |
| R017 | Exploratory single-order OLMo semantic map. | Motivate R018; never use as invariance evidence. |
| R018 | Canonical six-order measurement; interpretation qualified as above. | Order conditioning, divergence/reconvergence and candidate stable parent families. |
| R019 | Canonical repeatability control. | Exclude runtime/sampling noise as the tested explanation for order divergence. |
| R020 | Canonical measurement and audited candidate semantic reconstruction; interpretation provisional; human usefulness pending. | Contrast recoverable associations with poor generation while preserving the gap between availability, integration and expression. |

## Source-collection status

[RUN_OPTIMISATION_TRAJECTORY.md](RUN_OPTIMISATION_TRAJECTORY.md) is the
project-level account of how the experimental objective evolved from R001
through R020. It is interpretive context, not a substitute for individual
run plans, manifests or measured evidence.


[`ARTICLE_OUTLINE.md`](ARTICLE_OUTLINE.md) reproduces responses verbatim and
chronologically. Some statements describe the repository state at the time of
writing—for example, that R019 had not yet been pushed. It is source material
for drafting, not a current factual register.

[`META_ANALYSIS.md`](META_ANALYSIS.md) is append-only research history. When
entries conflict, later explicitly revised entries govern the current
project-level interpretation unless a subsequent measured result overturns
them.

## Supersession rule

Do not mutate a historical run artifact merely to make it agree with a later
interpretation. Instead:

1. preserve the original artifact;
2. record the newer interpretation in the meta-analysis;
3. update this status register;
4. make the article cite both the measured substrate and the current
   interpretive boundary.
