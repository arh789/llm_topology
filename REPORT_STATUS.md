# Report Status and Canonicality

Status: private article-facing register, current through R019 on 2026-11-17.

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

## Earlier run status

| Run | Article-facing status | Proper use |
|---|---|---|
| R013 | Canonical Qwen order-perturbation measurement; downstream interpretation remains model- and probe-specific. | Establish that low-level topology is order-sensitive and parent families appeared more stable. |
| R014 | Canonical Qwen context-perturbation measurement plus local-map reconstruction. | Test recurrence under changed third-concept context. |
| R015 | Canonical adjacent-region replication and R014–R015 comparison. | Support local continuity with deformation, not a global map. |
| R016 | Canonical OLMo 3 32B feasibility result. | Establish local instrumentability only. |
| R017 | Exploratory single-order OLMo semantic map. | Motivate R018; never use as invariance evidence. |
| R018 | Canonical six-order measurement; interpretation qualified as above. | Order conditioning, divergence/reconvergence and candidate stable parent families. |
| R019 | Canonical repeatability control. | Exclude runtime/sampling noise as the tested explanation for order divergence. |

## Source-collection status

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
