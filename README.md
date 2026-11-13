# LLM Semantic Topology Research

This is the independent working repository for an experimental project
examining semantic conflict, language-model behaviour and internal
representation geometry.

## Current evidence state

The package contains a research design, one behavioural case mapping, an
executed model playground, one successful single-prompt hidden-state capture
from Pythia 6.9B, five successful measured derived analyses and two completed
interpretive runs. R002 created the full-vocabulary static-basis
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
4. [`ANALYSIS_BRIEF.md`](ANALYSIS_BRIEF.md) — bounded questions for ChatGPT to
   analyse using the two preceding documents.
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
