# Single-prompt semantic topology

This proof of concept measures how one target token changes across every layer
of Pythia 6.9B for one fixed prompt. It separates three forms of evidence:

- static neighbours in the input embedding matrix;
- contextual relationships among the prompt tokens across layers;
- the final next-token probability distribution.

The initial capture pipeline is intentionally contained in
`single_prompt_topology.ipynb`. The derived full-vocabulary cutoff analysis is
contained in `full_vocabulary_cutoff.py`; the R005 relationship baseline is in
`cutoff_population_topology.py`. Topic modelling, multi-model comparisons and
causal interventions remain outside the proof-of-concept scope.

## Before running

Shut down the kernel used by `pythia_prompt_playground.ipynb` if Pythia 12B is
still loaded. The notebook fails before creating a run when less than 14 GiB of
GPU memory is free.

Open `single_prompt_topology.ipynb`, restart the kernel, and run all cells in
order. Pythia 6.9B is loaded from the shared Hugging Face cache under `D:\AI`.

## R002 derived cutoff analysis

`full_vocabulary_cutoff.py` reuses the successful R001 hidden states. It loads
only Pythia's cached input embedding matrix, calculates the target token's
cosine similarity to every valid vocabulary token at every recorded state,
tests elbow stability across several analysis windows, and creates the full
prompt-token contextual similarity matrices as a diagnostic. It does not run
another transformer forward pass.

From the project root, the verified local production command is:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\full_vocabulary_cutoff.py
```

The cutoff classifications are heuristic feasibility assessments. A result of
`none` is a valid outcome. Static-basis compatibility must not be interpreted
as a contextual relationship network over the entire vocabulary.

For manual curve inspection, generate the self-contained interactive HTML
report with:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\generate_cutoff_inspection_html.py
```

The resulting `reports/R002_cutoff_score_curves.html` contains one zoomable
line plot for every recorded state. It preserves ranks 1–5,000 exactly, samples
only the far tail, displays token identity and score on hover, and overlays the
automated window-specific elbow candidates without treating them as accepted
cutoffs.

## R003 score-region boundary analysis

R003 is reserved under the neutral name `lithium-score-region-boundaries`.
Its pre-run contract and execution record are in [`R003_PLAN.md`](R003_PLAN.md).
The successful run reused R002's verified `[33, 50277]` score matrix and token
metadata. It did not load the model, use the GPU or execute another transformer
forward pass.

The analysis treats the positive head, central body and negative tail as
separate geometric regions. It tests one upper and one lower boundary per
state, retains R002's full-curve upper elbow instead of recalculating it, and
uses sign-restricted calculations only as predeclared endpoint-sensitivity
checks. Negative cosine remains geometric anti-alignment, not evidence of
predictive downweighting or causal suppression.

The successful production execution used:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\score_region_boundaries.py
```

Its manifest is at
`runs/R003_lithium-score-region-boundaries__20261112T090711Z_pythia-6.9b_52ff8f97c2/manifest.json`.
Upper boundaries were accepted at 32 of 33 states and lower boundaries at 29 of
33 states. The accepted populations are geometric regions only; token inspection
did not establish a semantic transition at the boundaries.

## R004 full-curve cutoff analysis

R004 corrects R003's cutoff-use policy without changing the underlying score
matrix or elbow algorithm. Its contract and execution record are in
[`R004_PLAN.md`](R004_PLAN.md), and the implementation is
`full_curve_cutoffs.py`.

For every state, R004 calculates one upper elbow from the complete descending
score distribution and one lower elbow from the complete distribution ordered
by anti-alignment magnitude. Both cutoffs are saved and used unconditionally.
There is no sign-restricted candidate, agreement tolerance, accepted/rejected
classification or blank cutoff field. Region membership uses exact rank, so the
number of included tokens equals the cutoff rank even when scores are tied.

The verified production command is:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\full_curve_cutoffs.py
```

The successful run is
`runs/R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2/`.
It calculated and used both cutoffs at all 33 states, producing 191,872
tail-membership rows and trajectories for 24,364 union tokens. R004 supersedes
R003 for primary cutoff membership; R003 remains the historical record of the
discarded acceptance policy.

## R005 cutoff-population topology baseline

R005 reuses R004's exact positive-head and negative-tail memberships and loads
only the exact cached Pythia input-embedding weight. Its preregistered contract
and execution record are in [`R005_PLAN.md`](R005_PLAN.md), and the
implementation is `cutoff_population_topology.py`.

For each of the 33 states, it calculates an exact directed cosine
10-nearest-neighbour graph among the selected tokens, symmetrizes it for graph
metrics and state-local Louvain communities, and compares the observed graph
with 20 deterministic size-matched random populations. It also records
adjacent-state membership, edge and community stability. The transformer is not
run and R002's score matrix is not recalculated.

The verified production command is:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\cutoff_population_topology.py
```

The successful run is
`runs/R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2/`.
It produced 1,918,720 directed edges and 660 random-baseline rows. Mean
nearest-neighbour cosine and same-region edge fraction exceeded the random
97.5th percentile at all 33 states. The median adjacent-state population
Jaccard was 0.7561, edge Jaccard was 0.5307 and state-local community adjusted
Rand index was 0.3827.

These results establish organization relative to a size-only random null. They
do not establish topics or validate the elbow as a semantic boundary. The
strong positive/negative separation is partly expected because both populations
were selected from opposite ends of their projection onto the same contextual
target vector. The community representatives also expose lexical,
morphological and tokenizer structure.

## R008 ChatGPT-readable split networks

R006 and R007 are preserved failed attempts. R006 failed before the first
network because of an ambiguous temporary pandas index. R007 completed every
analysis and export component but failed final validation because physical
gzip lines were incorrectly treated as CSV rows even though tokenizer fields
can contain embedded newlines. Neither failed run supplies accepted result
artifacts.

R008 reruns the complete workflow from the validated R004 and R005 sources.
For every recorded state it calculates separate exact directed 10-nearest-
neighbour graphs inside the positive-head and negative-tail populations. It
produces 66 primary graphs, state-side-local Louvain communities, separate
transition statistics, persistent within-side edges and a secondary table of
cross-side relations retained by R005's earlier combined graphs.

The complete token-level evidence is in `nodes.csv.gz` and `edges.csv.gz`. The
small `community_nodes.csv`, `community_edges.csv` and
`chatgpt_community_networks.json` artifacts let ChatGPT reconstruct all 66
community-level networks, while `chatgpt_layer_packets.md` provides a readable
state-by-state inspection surface.

The verified production command is:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\export_chatgpt_split_networks.py
```

The successful run is
`runs/R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2/`.
It contains 191,872 node-state rows, 1,918,720 directed within-side edges,
792 community rows, 4,384 intercommunity edges and 604,515 secondary cross-side
relations. These remain static-embedding networks selected by a moving
contextual target representation.

## R009 state-local semantic classification

R009 is an interpretive analysis of R008 rather than another measured pipeline
run. It does not run Pythia, recalculate scores, alter cutoffs or change the
R008 communities. Its locked contract is
[`R009_ANALYSIS_PROTOCOL.md`](runs/R009_lithium-community-semantic-classification/R009_ANALYSIS_PROTOCOL.md).

External ChatGPT classified every state-local community independently under a
fixed descriptive taxonomy, producing one self-contained Markdown file for
each of the 33 recorded states. The
[`R009_COMPLETENESS_VERIFICATION.md`](runs/R009_lithium-community-semantic-classification/R009_COMPLETENESS_VERIFICATION.md)
check reports 392 positive-head and 400 negative-tail instances, for all 792
R008 communities exactly once with valid schemas, taxonomy values and
confidence values.

[`R009_SUMMARY.html`](runs/R009_lithium-community-semantic-classification/R009_SUMMARY.html)
is the self-contained interactive R009 summary. It aggregates every
classification across all 33 states, shows positive/negative community counts,
provides a taxonomy heatmap, supports filtering and search, and preserves a
complete state-by-state table. Every community includes its top 10 R008
representative tokens, ranked by descending degree within that state-side
community graph with token ID as the tie-breaker. The report is generated from
the 33 state Markdown files and R008 `chatgpt_community_networks.json` with:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\generate_r009_summary.py
```

The report is a descriptive index, not cross-state semantic synthesis. It does
not normalize broad-identity labels, infer that similarly named communities
persist across states, judge coherence or assign SDA-3 roles.

The R009 labels are model-generated interpretations of measured R008
communities, not new measurements or proof of semantic coherence. No
cross-state synthesis, SDA-3 role assignment, optimal-layer judgement or
curvature interpretation has yet been performed. The text-only package was
imported byte-for-byte from `chatgpt-analysis` commit `49a4b0a`.

## R010 state-local latent structure reconstruction

R010 is a second interpretive analysis rather than a measured pipeline run. Its
locked contract is
[`R010_ANALYSIS_PROTOCOL.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_ANALYSIS_PROTOCOL.md).
For each state, external ChatGPT independently inferred the minimum plausible
set of higher-order parent structures that could account for the observed R009
communities. Positive and negative populations were analysed separately before
cross-side relations were considered, and state-local parent identifiers carry
no cross-state continuity meaning.

The package contains 33 frozen state reconstructions. The final
[`R010_PHASE_A_COMPLETENESS_VERIFICATION.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_COMPLETENESS_VERIFICATION.md)
accounts for all 392 positive-head and 400 negative-tail communities exactly
once, reports zero node or parent-coverage mismatches and records clean isolated
reruns for States 06, 07, 23 and 24. Its result is **PASS**. The concise
[`R010_LAYERWISE_COMMUNITY_PARENT_MAP.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_LAYERWISE_COMMUNITY_PARENT_MAP.md)
indexes the resulting state-local dispositions and parents.

R010 Phase A is interpretive evidence built from R008 and R009. Phase B's
[`R010_PHASE_B_STRUCTURAL_EVOLUTION.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_STRUCTURAL_EVOLUTION.md)
infers cross-state correspondence families and a non-monotonic trajectory: the
positive side remains plastic around an increasingly abstract
operational/inquiry/process spine, while the negative side stabilises earlier
around control/characterisation/adverse change and authority/territorial order.
The later
[`R010_PHASE_B_INSIGHTS.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_B_INSIGHTS.md)
expands that interpretation as a progression from ontology through operators
and functional dependencies to a final procedure-like organisation.

Phase C's
[`R010_PHASE_C_SEMANTIC_TOPOLOGY_COMPARISON.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_SEMANTIC_TOPOLOGY_COMPARISON.md)
compares that semantic trajectory with R008's measured topology. It identifies
global resets, community re-partitioning and semantic abstraction over stable
geometry. The comparison does not assign SDA-3 roles, select an optimal layer
or infer curvature/coherence. The later
[`PHASE_D_TASK.md`](runs/R010_lithium-layerwise-latent-generative-structure/phase_d/PHASE_D_TASK.md)
was implemented through a frozen
[`R010_PHASE_D_MEASUREMENT_PROTOCOL.md`](runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_PROTOCOL.md),
quantitative
[`R010_PHASE_D_MEASUREMENT_RESULTS.md`](runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_MEASUREMENT_RESULTS.md)
and final
[`R010_PHASE_D_CONFLICT_RESOLUTION_REPORT.md`](runs/R010_lithium-layerwise-latent-generative-structure/phase_d/R010_PHASE_D_CONFLICT_RESOLUTION_REPORT.md).
Phase D keeps geometric, partition and semantic curvature separate and finds
that high coherence difficulty tends to precede community repartitioning. It
supports conflict resolution by selective compression, functional-role
assignment and re-differentiation rather than wholesale elimination. These
results remain specific to the current prompt and operational definitions. The
canonical
[`R010_PHASE_A_INSIGHTS.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_A_INSIGHTS.md),
[`R010_PHASE_C_INSIGHTS.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_C_INSIGHTS.md)
and
[`R010_PHASE_D_INSIGHTS.md`](runs/R010_lithium-layerwise-latent-generative-structure/R010_PHASE_D_INSIGHTS.md)
provide concise phase-level summaries. The complete 48-file package was
imported byte-for-byte from private `chatgpt-analysis` head `44adff3`.

## R011 whole-prompt perturbation feasibility

R011 reserves the first measured cross-prompt experiment under the neutral name
`whole-prompt-semantic-perturbation-feasibility`. Its locked contract is
[`R011_PLAN.md`](R011_PLAN.md). The planned pair uses one fixed Qwen chat shell
and changes only the order of `curvature density` and `Tokyo nightlife`, while
capturing the final assistant-prefix position at every transformer state.

The run failed at runtime readiness before any model was loaded. The installed
`llama-cpp-python 0.3.34` interface exposes final embeddings but no per-layer
hidden-state API. The isolated TorchAO fallback also failed: available packages
did not provide a usable x86 CPU int4 execution path on this system. The exact
probe reports, failed manifest and
[`R011_RUNTIME_READINESS.md`](runs/R011_whole-prompt-semantic-perturbation-feasibility/R011_RUNTIME_READINESS.md)
are retained as curated failure evidence.

Neither prompt was executed, no large model was downloaded and no R011
semantic, network or community result exists. The evidence supports a software
instrumentation blocker, not a system-RAM capacity conclusion. The run number
must not be reused.

## R012 generalised Qwen whole-prompt semantic topology

R012 corrects the R011 runtime choice by using original Hugging Face
Transformers models in BF16 on the RTX 4090. Its corrected contract is
[`R012_PLAN.md`](R012_PLAN.md). The validated capture checkpoint remains in
[`R012_CAPTURE_REPORT.md`](runs/R012_qwen-whole-prompt-paired-capture/R012_CAPTURE_REPORT.md),
while the completed result is
[`R012_MEASUREMENT_REPORT.md`](runs/R012_qwen-whole-prompt-paired-capture/R012_MEASUREMENT_REPORT.md).

The 0.5B smoke gate and 7B primary gate both succeeded. The 7B capture used
`Qwen/Qwen2.5-7B-Instruct` revision
`a09a35458c702b33eeacc393d103063234e8bc28`, recorded 29 states of width
3,584 for each prompt, reproduced both trajectories exactly and generated no
response token. State 00 was identical across the pair, while all 28
post-embedding states differed. The minimum paired cosine was 0.988543 at the
final normalized state, and maximum L2 displacement was 50.2713 at State 27.

The capture-only checkpoint was initially marked successful, then rejected as
incomplete against the intended R011 general-pipeline objective. R012 was
reopened and the valid trajectories were projected against the usable Qwen
input vocabulary. The completed run contains:

- 706,623 selected positive/negative prompt-state memberships;
- 7,066,230 exact directed 10-nearest-neighbour edges;
- 116 prompt/state/side networks;
- 1,181 state-local Louvain communities;
- 112 within-prompt adjacent-state comparisons; and
- 58 same-state paired-prompt comparisons.

The smallest paired membership Jaccard was 0.773731 and the smallest paired
edge Jaccard was 0.558323, both at final State 28 on the negative side. State
00 was identical across prompts. The full measured evidence is exported in
[`chatgpt_community_networks.json`](runs/R012_qwen-whole-prompt-paired-capture/chatgpt_community_networks.json)
and
[`chatgpt_layer_packets.md`](runs/R012_qwen-whole-prompt-paired-capture/chatgpt_layer_packets.md).
Semantic topic labelling, parent reconstruction and GRD/SDA interpretation
remain later ChatGPT work rather than R012 measurements.

## R013 bare-concept permutation topology

R013 removes R012's synthesis question, chat template and assistant-generation
prefix. Its locked contract is [`R013_PLAN.md`](R013_PLAN.md). The same three
concepts are supplied as bare text in all six possible orders, followed by one
fixed newline anchor. The production entry point is `r013_run.py`.

The anchor probe established one shared token ID (`198`), equal 12-token input
lengths and exactly identical State 00 vectors across all permutations. Every
`29 × 3,584` BF16 trajectory reproduced exactly, and no response was generated.
The unchanged R012 measurement method then produced:

- 2,465,642 selected permutation/state/side memberships;
- 24,656,420 exact directed 10-nearest-neighbour edges;
- 348 permutation/state/side networks;
- 3,654 state-local Louvain communities;
- 336 within-permutation adjacent-state comparisons;
- 870 matched-state permutation-pair comparisons; and
- separate item-level support records for 770,924 token instances and
  8,210,395 undirected-edge instances across the six permutations.

The smallest cross-permutation membership Jaccard was `0.320201` and the
smallest edge Jaccard was `0.125235`, both for `BAC` versus `CAB` at State 09
on the positive side. At final State 28, the 6/6 core contained 5,214 positive
tokens and 20,212 positive edges, plus 5,011 negative tokens and 19,219
negative edges. These are structural measurements, not semantic identities or
independent causal estimates of position, recency or adjacency effects.

The factual result is in
[`R013_MEASUREMENT_REPORT.md`](runs/R013_qwen-bare-concept-permutation-topology/R013_MEASUREMENT_REPORT.md),
the exact coverage check is in
[`R013_COMPLETENESS_VERIFICATION.md`](runs/R013_qwen-bare-concept-permutation-topology/R013_COMPLETENESS_VERIFICATION.md),
and the downstream analysis surfaces are
[`chatgpt_community_networks.json`](runs/R013_qwen-bare-concept-permutation-topology/chatgpt_community_networks.json)
and
[`chatgpt_layer_packets.md`](runs/R013_qwen-bare-concept-permutation-topology/chatgpt_layer_packets.md).
Semantic parent reconstruction and order-effect interpretation remain later
ChatGPT work.

## R014 overlapping-context semantic topology

R014 keeps the R013 model, final newline anchor, hidden-state capture,
full-curve cutoff, exact 10-nearest-neighbour graph and state-local Louvain
community methods unchanged. Its locked contract is
[`R014_PLAN.md`](R014_PLAN.md), and the concrete concept selection is justified
from measured R013 evidence in
[`R014_CONCEPT_SELECTION_EVIDENCE.md`](R014_CONCEPT_SELECTION_EVIDENCE.md).

Four concepts form four overlapping probes:

- `laser | city | spatial field`;
- `laser | city | clubs`;
- `laser | spatial field | clubs`; and
- `city | spatial field | clubs`.

Each probe is measured in all six orders, giving 24 prompts. Every concept pair
therefore appears in two different third-concept contexts. The validated run
contains:

- 10,447,003 selected prompt/state/side memberships;
- 104,470,030 exact directed 10-nearest-neighbour edges;
- 1,392 prompt/state/side networks;
- 14,686 state-local Louvain communities;
- 1,344 within-prompt adjacent-state comparisons;
- 3,480 within-probe matched-state permutation comparisons; and
- separate 1/6 through 6/6 token and edge support evidence within each probe.

The smallest within-probe membership Jaccard was `0.289351` for `P3_ABC`
versus `P3_CAB` at State 13 on the negative side. The smallest within-probe
edge Jaccard was `0.104801` for the same prompt pair at State 10 on the
positive side. State 00 topology is identical across every prompt; later
differences arise after contextual processing.

The factual result is in
[`R014_MEASUREMENT_REPORT.md`](runs/R014_qwen-overlapping-context-semantic-map/R014_MEASUREMENT_REPORT.md),
the exact coverage check is in
[`R014_COMPLETENESS_VERIFICATION.md`](runs/R014_qwen-overlapping-context-semantic-map/R014_COMPLETENESS_VERIFICATION.md),
and the downstream analysis surfaces are
[`chatgpt_community_networks.json`](runs/R014_qwen-overlapping-context-semantic-map/chatgpt_community_networks.json)
and
[`chatgpt_layer_packets.md`](runs/R014_qwen-overlapping-context-semantic-map/chatgpt_layer_packets.md).

R014 stops before interpretation. Each probe must first be semantically
reconstructed independently without imposing R013 parent labels. Cross-probe
parent and relation matching, and the decision whether the evidence supports a
local semantic map, remain downstream analytical work.

## Run outputs

Each execution writes a timestamped directory under `runs/` containing:

- `manifest.json` — prompt, model identity, environment, status and hashes;
- `tokens.csv` — the exact tokenization and target position;
- `hidden_states.safetensors` — all prompt-token states at every layer;
- `layer_metrics.csv` — the target token's layer-wise trajectory;
- `target_relationships.csv` — target-to-prompt-token cosine similarities;
- `semantic_neighbors.csv` — static input neighbours and final predictions;
- `figures/target_trajectory.png`;
- `figures/target_relationships.png`;
- `figures/token_similarity_layers.png`.

Generated run directories are excluded from Git by default unless deliberately
selected as curated evidence. The reviewed baseline at
`runs/R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2/`
is deliberately
committed as the first reproducible evidence package; its `manifest.json`
records the exact model revision and hashes for every artifact. R009 and R010
are also tracked as curated interpretive packages. Other later run outputs
should remain local unless they are explicitly selected for comparison or
publication.

## Run naming

Before each execution, set a new sequential `RUN_NUMBER` and a neutral,
lowercase kebab-case `RUN_NAME` in the configuration cell. Run directories use
the form `RNNN_<target>-<purpose>__<UTC>_<model>_<prompt-hash>`. Numbers are
never reused, including for failed or repeated runs, and the notebook stops if
the selected number already exists.

## Interpretation boundary

This experiment is a single-prompt case study. It can validate tensor capture
and reveal candidate layer-wise changes. It cannot establish stable topics, a
generally optimal layer, causal mechanisms or a model-wide semantic topology.
