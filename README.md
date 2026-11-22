# LLM Semantic Topology Research

This is the independent working repository for an experimental project
examining semantic conflict, language-model behaviour and internal
representation geometry.

> **Repository status:** active research evidence supporting the published
> [LLM Topology article](https://decrepitfilth.art/art/llm-topology).
> Experimental work, interpretation and documentation remain in development.

> **Canonical repository:** `arh789/llm_topology` became the authoritative
> project repository on 2026-11-17. The former
> `arh789/chatgpt-analysis/projects/llm-topology` subtree is retained only as
> an archival provenance source and must not receive new project work.

## Article-oriented reading path

The complete research archive remains below. For the shorter route from an
article claim to its supporting evidence, use:

1. [`ARTICLE_OUTLINE_OFFICIAL.md`](ARTICLE_OUTLINE_OFFICIAL.md) — the final
   conceptual synthesis used as the article’s content authority.
2. [`ARTICLE_EVIDENCE_INDEX.md`](ARTICLE_EVIDENCE_INDEX.md) — the current
   claim-to-measurement, code, interpretation and limitation map.
3. [`METHODOLOGY.md`](METHODOLOGY.md) — what is standard, what is distinctive
   and where interpretation begins.
4. [`REPORT_STATUS.md`](REPORT_STATUS.md) — which reports are canonical,
   exploratory or qualified by later analysis.
5. [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md) — meanings of the central R018
   and R019 fields and metrics.
6. [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — model, environment, commands,
   validation and local-only artifact boundaries.
7. [`R019_RESULT.json`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json)
   — the compact machine-readable determinism control.

## Model-interchangeable measurement pipeline

[`TSTP.md`](single_prompt_topology/TSTP.md) documents the Transformer State
Topology Pipeline extracted from R020. TSTP preserves the complete
autoregressive capture-to-network workflow while isolating architecture access
behind validated adapters. Pythia/GPT-NeoX and Qwen2 are currently supported;
the [engineering validation](single_prompt_topology/TSTP_VALIDATION.md) records
exact R020 Pythia reconciliation and a complete 52-network Qwen export test.
Semantic reconstruction remains a separate downstream task.

## Current evidence state

R015 measurement and downstream semantic reconstruction are complete for the
adjacent sensor/apartment/line/sessions region: 24 prompts, 1,392 networks,
14,796 communities, 1,344 transitions and 3,480 permutation comparisons. All
fourteen manifest components and 49 indexed artifact hashes passed
verification. Independent P1–P4 reconstruction, the R015 semantic map and the
R014–R015 comparison are now curated project evidence.

R016 then tested whether the exact native-BF16 `allenai/Olmo-3-1125-32B` base
model could serve as a larger local measurement instrument. The pinned
64-layer model completed one nine-token, no-generation instrumented forward
pass using mixed GPU, CPU and disk-backed placement. All 65 hidden states of
width 5,120 and the complete first-token logits were finite. This establishes
local single-prompt feasibility; it does not establish multi-prompt throughput
or semantic-topology output from OLMo 3 32B.

R017 completes that missing topology step for the bare-concept prompt `choke
point / collapsible barrier / spear`. The same exact OLMo revision produced 65
captured anchor states, 130 positive/negative networks, 490,114 selected token
memberships, 4,901,140 exact directed 10-NN edges, 2,007 state-local
communities and 128 adjacent-state comparisons. The evidence-linked report
reconstructs a candidate semantic map of constrained passage, deployable
obstruction, movement control and reach/piercing force. This is a successful
single-trajectory map; order and context invariance were not tested.

R018 repeats that concept set in all six input orders using one batched,
deterministically replayed OLMo 3 32B capture. It produces 780 networks,
3,081,305 selected memberships, 30,813,050 exact directed 10-NN edges, 11,872
state-local communities, 768 adjacent-state comparisons and 1,950 same-state
permutation comparisons. State 00 is exactly identical across permutations.
The measured evidence is complete and independently verified; semantic parent
reconstruction remains deliberately unstarted.

The downstream R018 reconstruction is now complete. Despite strong order and final-position effects, the six trajectories reconverge onto a strict 6/6 late semantic core comprising **constraint / requirement**, **structural configuration**, **dynamic path geometry** and **collapse / adjustment**. The result is recorded in the R018 semantic reconstruction, structured map and final HTML analysis; literal spear/attack semantics do not survive as strict late invariants.
 The initial completeness check
exposed and preserved a validator defect—physical text lines were counted
instead of logical CSV records—then passed after a validation-only correction
that did not rerun or alter the measurements.

The package contains a research design, one behavioural case mapping, an
executed model playground, one successful single-prompt hidden-state capture
from Pythia 6.9B, one successful paired whole-prompt Qwen topology run, one
successful six-permutation bare-concept Qwen topology run, one successful
four-probe overlapping-context Qwen topology run, one successful native-BF16
OLMo 3 32B feasibility run, one successful OLMo 3 32B semantic-map run, five
earlier measured derived analyses and two completed interpretive runs. R002 created the
full-vocabulary static-basis
score matrix; R003 tested an unnecessarily gated boundary policy; R004 retains
the full-curve upper and lower elbow cutoffs at all states without that
acceptance gate; R005 constructs exact static embedding relationship networks
for those populations; and R008 exports 66 separate positive/negative networks
in complete and ChatGPT-readable forms after two documented failed attempts.
R009 applies a fixed descriptive taxonomy to all 792 state-local R008
communities across 33 states and passes its structural completeness check. R010
independently reconstructs candidate latent parent structures at every state,
tracks their cross-state evolution and compares that semantic trajectory with
R008's measured topology. R010 Phase D then operationalises separate geometric,
partition and semantic curvature measures plus a coherence-difficulty score.
R011 then attempted to establish a quantised CPU/RAM capture path for matched
whole-prompt perturbations. It failed before model loading: the installed
llama.cpp binding exposes no per-layer hidden-state API, and the tested TorchAO
fallback did not supply a usable x86 CPU int4 path. The failure is retained as
runtime-readiness evidence; no R011 semantic result exists.
R012 corrected that runtime choice by using Transformers BF16 models on the
RTX 4090. After an initially incomplete capture-only checkpoint, it completed
the intended generalised pipeline for Qwen2.5-7B-Instruct: 116 positive/negative
networks, 1,181 state-local communities, 112 adjacent-state comparisons and 58
same-state paired-prompt comparisons. The smallest paired membership and edge
Jaccards both occurred at final State 28 on the negative side (0.773731 and
0.558323). Complete measured exports are available for downstream ChatGPT
semantic analysis; R012 itself adds no semantic labels or GRD/SDA roles.
R013 removes the synthesis shell and assistant prefix, captures a controlled
newline anchor after all six orderings of the same three bare concepts, and
reuses the R012 measurement method unchanged. It produces 348 networks, 3,654
state-local communities, 336 adjacent-state comparisons and 870 matched-state
permutation-pair comparisons. The smallest cross-order membership and edge
Jaccards were 0.320201 and 0.125235. Separate token and edge support evidence
identifies the structures present in 1/6 through 6/6 permutations without
semantically interpreting them.
R014 extends that exact method to four overlapping concept triplets and all 24
within-triplet orders. It produces 1,392 networks, 14,686 state-local
communities, 1,344 adjacent-state comparisons and 3,480 within-probe
permutation comparisons. The complete measured exports support independent
semantic reconstruction of each probe before any cross-probe parent or
relation matching. R014 itself does not infer the local semantic map.
R015 moves the same 24-prompt design into adjacent semantic space, then adds
independent probe reconstruction and an explicit R014–R015 parent/relation
comparison. R016 changes only the model-feasibility question: it proves that
OLMo 3 32B Base can expose every required hidden state locally for one short
prompt without quantisation or response generation. R017 uses that exact
backend for a complete single-prompt projection, cutoff, graph, community and
semantic-map run. R018 uses the same model and measurement method for the full
six-permutation order test, ending at semantic-free, ChatGPT-readable evidence.
R019 independently repeats three balanced cyclic permutations three times and
establishes a zero measured repeat noise floor: hidden states, vocabulary
scores, next-token logits, cutoffs, edges and seeded communities are exact
across identical repeats, while concept order produces substantial divergence.
For article use, the current R018 interpretation boundary is the later,
conservative MA-0114 conclusion recorded in [`REPORT_STATUS.md`](REPORT_STATUS.md):
higher-order semantic families survive permutation more clearly than their
relations, so R018 supports a perturbation-stable semantic basis more strongly
than one fixed invariant graph.

R005 found greater nearest-neighbour density and positive/negative segregation
than a size-matched random null at all 33 states, but its communities also
contain tokenizer and morphological structure. R009 records model-generated
candidate identities for those communities; R010 adds state-local generative
interpretations and a cross-state synthesis rather than new measurements. Its
Phase-C comparison finds partial, non-reducible correspondence between semantic
change and measured topology. Phase D finds that difficult-to-compress states
tend to be followed by repartitioning and supports selective compression plus
re-differentiation rather than conflict elimination. These are single-prompt,
operational measurements and interpretations: they do not establish SDA-3
roles, manifold curvature, a generally optimal layer, causal mechanisms or
cross-prompt generality. Model weights remain in the shared cache under `D:\AI`
and are not versioned here.

## Reading order

1. [`META_ANALYSIS.md`](META_ANALYSIS.md) — the append-only chronological
   record, agent usage instructions, interpretations and methodological
   decisions.
2. [`PROJECT_HANDOVER.md`](PROJECT_HANDOVER.md) — the governing research
   objective, questions, epistemic distinctions and proposed phases.
3. [`ZOMBIE_CASE_STUDY.md`](ZOMBIE_CASE_STUDY.md) — how an existing
   ChatGPT zombie-survival interrogation relates to the proposed research,
   including limitations and a candidate controlled stimulus.
4. [`ARTICLE_OUTLINE_OFFICIAL.md`](ARTICLE_OUTLINE_OFFICIAL.md) — the article’s
   governing conceptual synthesis and human-learning framework.
5. [`pythia_prompt_playground.ipynb`](pythia_prompt_playground.ipynb) — an
   executed interactive comparison surface for Pythia 410M, 6.9B and 12B.
6. [`single_prompt_topology/README.md`](single_prompt_topology/README.md) — the
   proof-of-concept pipeline, output contract and interpretation boundary.
7. [`single_prompt_topology/runs/R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2/manifest.json)
   — the selected successful baseline and artifact index.
8. [`single_prompt_topology/runs/R002_lithium-static-basis-cutoff-feasibility__20261112T083025Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R002_lithium-static-basis-cutoff-feasibility__20261112T083025Z_pythia-6.9b_52ff8f97c2/manifest.json)
   — the successful full-vocabulary score analysis reused by R003.
9. [`single_prompt_topology/R003_PLAN.md`](single_prompt_topology/R003_PLAN.md)
   — the preregistered contract and execution record for the score-region
   boundary reanalysis.
10. [`single_prompt_topology/runs/R003_lithium-score-region-boundaries__20261112T090711Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R003_lithium-score-region-boundaries__20261112T090711Z_pythia-6.9b_52ff8f97c2/manifest.json)
    — the successful R003 lineage, method, component status and artifact index.
11. [`single_prompt_topology/R004_PLAN.md`](single_prompt_topology/R004_PLAN.md)
    — the pre-run contract and execution record for the ungated full-curve
    cutoff analysis.
12. [`single_prompt_topology/runs/R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2/manifest.json)
    — the successful R004 lineage, validation record and artifact index.
13. [`single_prompt_topology/R005_PLAN.md`](single_prompt_topology/R005_PLAN.md)
    — the preregistered contract and execution record for the cutoff-population
    static-topology baseline.
14. [`single_prompt_topology/runs/R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2/manifest.json)
    — the successful R005 lineage, component status and artifact index.
15. [`single_prompt_topology/R006_PLAN.md`](single_prompt_topology/R006_PLAN.md)
    and [`single_prompt_topology/R007_PLAN.md`](single_prompt_topology/R007_PLAN.md)
    — the preserved failed-attempt contracts and failure records.
16. [`single_prompt_topology/R008_PLAN.md`](single_prompt_topology/R008_PLAN.md)
    — the successful corrected split-network contract and execution record.
17. [`single_prompt_topology/runs/R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2/manifest.json`](single_prompt_topology/runs/R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2/manifest.json)
    — the successful R008 artifact index and validation record.
18. [`single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_ANALYSIS_PROTOCOL.md`](single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_ANALYSIS_PROTOCOL.md)
    — the locked descriptive-classification contract and interpretation
    boundaries for the external ChatGPT analysis.
19. [`single_prompt_topology/runs/R009_lithium-community-semantic-classification/`](single_prompt_topology/runs/R009_lithium-community-semantic-classification/)
    — all 33 state-local community-classification files.
20. [`single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_COMPLETENESS_VERIFICATION.md)
    — the exactly-once count, schema and protocol-boundary verification.
21. [`single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_SUMMARY.html`](single_prompt_topology/runs/R009_lithium-community-semantic-classification/R009_SUMMARY.html)
    — a self-contained interactive summary of the 792 state-local community
    classifications and their top ten graph-degree representative tokens
    across all 33 transformer states.
22. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_ANALYSIS_PROTOCOL.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_ANALYSIS_PROTOCOL.md)
    — the locked independent-state parent-inference protocol and contamination
    controls.
23. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_LAYERWISE_COMMUNITY_PARENT_MAP.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_LAYERWISE_COMMUNITY_PARENT_MAP.md)
    — a concise map of the state-local community dispositions and candidate
    parent structures.
24. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_COMPLETENESS_VERIFICATION.md)
    — the final 33-state, 792-community accounting, coverage and isolation
    verification.
25. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_STRUCTURAL_EVOLUTION.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_STRUCTURAL_EVOLUTION.md)
    — the cross-state correspondence families, structural epochs and semantic
    transition record.
26. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_INSIGHTS.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_INSIGHTS.md)
    — an expanded interpretive account of the ontology-to-procedure trajectory
    inferred from Phase B.
27. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_SEMANTIC_TOPOLOGY_COMPARISON.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_SEMANTIC_TOPOLOGY_COMPARISON.md)
    — the comparison between the inferred semantic trajectory and R008's
    measured membership, edge, community and modularity changes.
28. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/PHASE_D_TASK.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/PHASE_D_TASK.md)
    — the initial curvature and coherence task definition.
29. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_PROTOCOL.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_PROTOCOL.md)
    — the frozen operational definitions and measurement procedure.
30. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_RESULTS.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_RESULTS.md)
    — the state/transition measurements and quantitative results.
31. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_CONFLICT_RESOLUTION_REPORT.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_CONFLICT_RESOLUTION_REPORT.md)
    — the final Phase-D conflict-resolution interpretation and limitations.
32. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_INSIGHTS.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_INSIGHTS.md)
    — the canonical Phase-A insight summary.
33. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_INSIGHTS.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_INSIGHTS.md)
    — the canonical Phase-C insight summary.
34. [`single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_D_INSIGHTS.md`](single_prompt_topology/runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_D_INSIGHTS.md)
    — the canonical Phase-D insight summary.
35. [`single_prompt_topology/R011_PLAN.md`](single_prompt_topology/R011_PLAN.md)
    — the locked whole-prompt paired-perturbation capture contract.
36. [`single_prompt_topology/runs/R011_whole-prompt-semantic-perturbation-feasibility/R011_RUNTIME_READINESS.md`](single_prompt_topology/runs/R011_whole-prompt-semantic-perturbation-feasibility/R011_RUNTIME_READINESS.md)
    — the failed quantised CPU runtime decision and exact stop boundary.
37. [`single_prompt_topology/R012_PLAN.md`](single_prompt_topology/R012_PLAN.md)
    — the corrected generalised paired whole-prompt topology contract.
38. [`single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_CAPTURE_REPORT.md`](single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_CAPTURE_REPORT.md)
    — the validated 0.5B and 7B capture checkpoint.
39. [`single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_MEASUREMENT_REPORT.md)
    — the completed network/community measurement and factual findings.
40. [`single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/chatgpt_layer_packets.md`](single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/chatgpt_layer_packets.md)
    — all 29 states, both prompts and both sectors in a readable analytical packet.
41. [`single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R012_qwen-whole-prompt-paired-capture/R012_COMPLETENESS_VERIFICATION.md)
    — exact coverage and integrity verification.
42. [`METHODOLOGY.md`](METHODOLOGY.md)
    — the methodological division between standard analytical tools and the project's distinctive semantic-topology machinery.
43. [`single_prompt_topology/R013_PLAN.md`](single_prompt_topology/R013_PLAN.md)
    — the locked bare-concept six-permutation measurement contract.
44. [`single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/R013_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/R013_MEASUREMENT_REPORT.md)
    — the completed R013 measurement coverage and factual structural findings.
45. [`single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/chatgpt_layer_packets.md`](single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/chatgpt_layer_packets.md)
    — all six permutations, 29 states and both sectors in a readable analytical packet.
46. [`single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/chatgpt_community_networks.json`](single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/chatgpt_community_networks.json)
    — the complete compact measured network package for downstream semantic analysis.
47. [`single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/R013_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R013_qwen-bare-concept-permutation-topology/R013_COMPLETENESS_VERIFICATION.md)
    — exact capture, network, comparison, invariance and referential-integrity verification.
48. [`single_prompt_topology/R014_PLAN.md`](single_prompt_topology/R014_PLAN.md)
    — the locked four-probe overlapping-context measurement contract.
49. [`single_prompt_topology/R014_CONCEPT_SELECTION_EVIDENCE.md`](single_prompt_topology/R014_CONCEPT_SELECTION_EVIDENCE.md)
    — the measured R013 evidence supporting the four concrete R014 concepts.
50. [`single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/R014_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/R014_MEASUREMENT_REPORT.md)
    — the completed R014 measurement coverage and factual structural findings.
51. [`single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/chatgpt_layer_packets.md`](single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/chatgpt_layer_packets.md)
    — all four probes, 24 prompts, 29 states and both sectors in a readable analytical packet.
52. [`single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/chatgpt_community_networks.json`](single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/chatgpt_community_networks.json)
    — the complete compact measured network package for downstream independent semantic reconstruction.
53. [`single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/R014_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R014_qwen-overlapping-context-semantic-map/R014_COMPLETENESS_VERIFICATION.md)
    — exact network, transition, comparison, invariance and export verification.
54. [`single_prompt_topology/R015_PLAN.md`](single_prompt_topology/R015_PLAN.md)
    — the frozen adjacent-neighbourhood replication contract.
55. [`single_prompt_topology/R015_CONCEPT_SELECTION_EVIDENCE.md`](single_prompt_topology/R015_CONCEPT_SELECTION_EVIDENCE.md)
    — measured R014 evidence supporting sensor, apartment, line and sessions as neighbouring replacements.
56. [`single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_MEASUREMENT_REPORT.md)
    — the completed and validated 24-prompt R015 measurement.
57. [`single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_PROBE_RECONSTRUCTIONS.md`](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_PROBE_RECONSTRUCTIONS.md)
    — independent P1-P4 semantic reconstruction before R014 alignment.
58. [`single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_SEMANTIC_MAP.json`](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_SEMANTIC_MAP.json)
    — the completed R015 local semantic-neighbourhood map.
59. [`single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R014_R015_COMPARISON.md`](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R014_R015_COMPARISON.md)
    — parent, relation, held-out and deformation comparison between R014 and R015.
60. [`single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_RUN_ANALYSIS_AND_RECOMMENDATIONS.html`](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R015_RUN_ANALYSIS_AND_RECOMMENDATIONS.html)
    — human-readable R015 findings and next-experiment recommendation.
61. [`single_prompt_topology/R016_PLAN.md`](single_prompt_topology/R016_PLAN.md)
    — the locked native-BF16 OLMo 3 32B local feasibility contract.
62. [`single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/R016_FEASIBILITY_REPORT.md`](single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/R016_FEASIBILITY_REPORT.md)
    — the measured device placement, memory, timing, capture and cleanup result.
63. [`single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/manifest.json`](single_prompt_topology/runs/R016_olmo3-32b-local-bf16-feasibility/manifest.json)
    — the successful component record, artifact hashes, transport reassessment
    and cache-cleanup evidence.
64. [`single_prompt_topology/R017_PLAN.md`](single_prompt_topology/R017_PLAN.md)
    — the locked OLMo 3 32B single-prompt topology and reporting contract.
65. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_MEASURED_REPORT.md`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_MEASURED_REPORT.md)
    — the completed 65-state measurement summary.
66. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_REPORT.html`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_REPORT.html)
    — the evidence-linked semantic map and report-standardisation candidates.
67. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/manifest.json`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/manifest.json)
    — the successful component record and hashes for curated R017 evidence.
68. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_REPORTING_RULES.md`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_REPORTING_RULES.md)
    — the R014/R015-derived reporting rules adapted to single-trajectory evidence.
69. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_RECONSTRUCTION.md`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_RECONSTRUCTION.md)
    — the independent downstream parent and relation reconstruction.
70. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_NODES.csv`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_NODES.csv)
    — structured R017 parent nodes with trajectory support and confidence.
71. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_EDGES.csv`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP_EDGES.csv)
    — structured parent relations with evidence scope and caveats.
72. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP.json`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_MAP.json)
    — machine-readable single-trajectory semantic map and invariance status.
73. [`single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_RUN_ANALYSIS_AND_RECOMMENDATIONS.html`](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_RUN_ANALYSIS_AND_RECOMMENDATIONS.html)
    — canonical R017 analysis, limitations and next-experiment recommendation.
74. [`single_prompt_topology/R018_PLAN.md`](single_prompt_topology/R018_PLAN.md)
    — the locked OLMo 3 32B six-permutation measurement contract.
75. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_MEASUREMENT_REPORT.md)
    — the semantic-free measured coverage and comparison summary.
76. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_COMPLETENESS_VERIFICATION.md)
    — the reconciled structural completeness record.
77. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/validation_recovery.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/validation_recovery.json)
    — the original validation failure, corrected logical-record check and
    hashes proving that measured evidence was not re-executed or changed.
78. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_ANALYSIS_PROTOCOL.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_ANALYSIS_PROTOCOL.md)
    — the independent semantic-reconstruction contract and overall R018
    completion gate.
79. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/analysis/analysis_manifest.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/analysis/analysis_manifest.json)
    — the append-only analysis status, required outputs and frozen measurement
    provenance.
80. [`single_prompt_topology/R018_LIFECYCLE_UPDATE_VERIFICATION.md`](single_prompt_topology/R018_LIFECYCLE_UPDATE_VERIFICATION.md)
    — the implemented lifecycle correction and passing unit/regression test
    record.
81. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md)
    — the independent six-permutation reconstruction and invariant-parent
    derivation.
82. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP_NODES.csv`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP_NODES.csv)
    — the structured invariant and contextual semantic parents.
83. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP_EDGES.csv`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP_EDGES.csv)
    — the evidence-linked higher-order parent relations.
84. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP.json)
    — the machine-readable completed R018 semantic topology.
85. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_RUN_ANALYSIS_AND_RECOMMENDATIONS.html`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_RUN_ANALYSIS_AND_RECOMMENDATIONS.html)
    — the final R018 human-readable analysis and recommendations.
86. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_DATA.json`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_DATA.json)
    — the provenance-linked intermediate semantic-network dataset.
87. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_REPORT.html`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_REPORT.html)
    — the rendered intermediate-resolution R018 semantic network.
88. [`single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_FINAL_REPORT.html`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_FINAL_REPORT.html)
    — the canonical integrated R018 final report.
89. [`single_prompt_topology/R019_PLAN.md`](single_prompt_topology/R019_PLAN.md)
    — the locked three-permutation, three-repeat reproducibility-control contract.
90. [`single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md)
    — the measured repeat noise floor and between-order divergence summary.
91. [`single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json)
    — the machine-readable conclusion and strongest divergence cases.
92. [`single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_COMPLETENESS_VERIFICATION.md`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_COMPLETENESS_VERIFICATION.md)
    — the expected-coverage reconciliation for all repeat and order comparisons.

## Provenance

- The project handover was supplied by the project owner on 2026-11-12.
- The behavioural case is the public page
  [Zombie Survival by ChatGPT — Why the AI Lies (and How to Stop It)](https://decrepitfilth.art/art/zombie-survival-chatgpt-why-the-ai-lies-and-how-to-stop-it),
  inspected on 2026-11-12.
- The case-study mapping was prepared from the handover and the published page.

Selected, documented snapshots may be published separately to the private
`chatgpt-analysis` repository for external analysis. R009 was authored there
by external ChatGPT and imported byte-for-byte at remote commit `49a4b0a`.
R010 was also authored externally in the private parent repository. Its final
Phase-A verification passed at remote commit `28e3653`; Phase B was added at
`a62646f`, Phase C at `3f82f28`, and the expanded Phase-B insights artifact was
finalised at `11bc912`. A Phase-D task definition was added at `3711712`. The
Phase-D measurement results and final report were completed at `96041ea` and
`4e5541d`. Canonical Phase-A, Phase-C and Phase-D insight summaries were added
through remote head `44adff3`. The complete 48-file package was imported
byte-for-byte from that head.
GitHub may temporarily lead while external analysis is active, so its history
must be fetched and reconciled before later edits or pushes. This repository
remains the authoritative project working copy after that reconciliation.

## First experiment: Pythia prompt playground

[`pythia_prompt_playground.ipynb`](pythia_prompt_playground.ipynb)
provides a dropdown for switching between `EleutherAI/pythia-410m`,
`EleutherAI/pythia-6.9b` and `EleutherAI/pythia-12b` without editing the
notebook. Pythia 12B is selected by default for the current fit test. Its BF16
weights nearly fill a 24 GiB GPU, so 6.9B remains the practical fallback. The
editable prompt cell returns the generated continuation and records the seed,
sampling settings, token counts, latency and peak GPU memory.

To reproduce the notebooks in a fresh Windows environment:

1. Install Python 3.11 or later.
2. Create and activate a project environment:

   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```

3. Install a CUDA-enabled PyTorch build using the command generated by the
   [official PyTorch selector](https://pytorch.org/get-started/locally/).
4. Install the notebook dependencies and launch JupyterLab:

   ```powershell
   python -m pip install jupyterlab "transformers>=4.48" safetensors ipywidgets
   python -m jupyter lab
   ```

The first loading run for each choice downloads its checkpoint from Hugging
Face. All three Pythia models are base next-token models, not instruction-tuned
assistants, so the notebook deliberately evaluates completions rather than
chat behaviour.

The notebook verifies that `HF_HOME` is `D:\AI\cache\huggingface` and
`HF_HUB_CACHE` is `D:\AI\cache\huggingface\hub` before loading anything. It
stops before a download if the shared model-cache configuration is missing or
points elsewhere.

## Second experiment: single-prompt layer topology

[`single_prompt_topology/single_prompt_topology.ipynb`](single_prompt_topology/single_prompt_topology.ipynb)
captures every prompt-token hidden state across all 33 Pythia 6.9B layer
outputs for one fixed lithium-market prompt. It compares the target token's
static input-embedding neighbours, contextual prompt-token relationships and
final next-token predictions without treating those three measurements as
equivalent.

The committed baseline completed successfully using exact model revision
`c0e3eee36dc47af0c49f361c74cfe459c09f7f23`. It captured a
`[33, 19, 4096]` BF16 tensor, used 12.79 GiB peak GPU memory and records hashes
for every generated artifact in its manifest. Future run directories remain
ignored until they are deliberately reviewed and selected for publication.

R002 reused that capture to calculate a verified `[33, 50277]` matrix of
contextual-target compatibility scores against the static input-embedding
vocabulary. R003 reused those scores without loading the model or using the GPU,
but added a secondary acceptance gate that was later identified as unnecessary.
R004 removes that gate, calculates and uses one upper and one lower full-curve
elbow at all 33 states, and assigns membership by exact cutoff rank. Semantic
usefulness remains unestablished.

R005 loads only the exact cached input-embedding weight and constructs an exact
directed 10-nearest-neighbour graph for every R004 population. It compares each
state with 20 deterministic size-matched random populations, records
state-local Louvain communities and tracks membership, edge and community
stability across adjacent states. Mean nearest-neighbour cosine and same-region
edge fraction exceeded the random 97.5th percentile at all 33 states. Because
the null controls size only and the population is selected along the same
target-relative axis used to define positive and negative tails, this establishes
geometric organization relative to that null, not semantic topic validity.

R006 failed before its first network because of an ambiguous temporary pandas
index. R007 rebuilt all 66 networks and exports but failed closed when physical
gzip lines were incorrectly used to count CSV records containing embedded
newlines. R008 reran the full workflow and validated those records with a CSV
parser. It exports separate positive-head and negative-tail token graphs,
community-level networks, transition evidence, a secondary R005 cross-side
table and compact JSON and Markdown packets for ChatGPT. The split exports make
the existing measurements easier to interpret; they do not validate topics,
suppression, coherence or curvature.

## Interpretation boundary

Keep these levels separate throughout analysis:

- observable model responses;
- researcher interpretations of those responses;
- model-generated explanations of its own behaviour;
- measured internal representations;
- causal conclusions supported by interventions.

Only the first three are present in the behavioural case. The proposed project
is intended to measure the fourth and test the fifth.
