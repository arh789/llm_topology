# Single-prompt semantic topology

This proof of concept measures how one target token changes across every layer
of Pythia 6.9B for one fixed prompt. It separates three forms of evidence:

- static neighbours in the input embedding matrix;
- contextual relationships among the prompt tokens across layers;
- the final next-token probability distribution.

The initial capture pipeline is intentionally contained in
`single_prompt_topology.ipynb`. The derived full-vocabulary cutoff analysis is
contained in `full_vocabulary_cutoff.py`. Reusable Python modules, topic
modelling, multi-model comparisons and causal interventions remain outside the
proof-of-concept scope.

This published analysis copy includes the post-baseline plans, manifests,
summary tables, cutoff-adjacent token tables and referenced figures. The
post-baseline implementation scripts and high-volume tensors, tail-membership
tables and trajectory tables remain in authoritative local commit
`f185f1ee3829ac198049497a2f62084f8f2156ad` rather than being duplicated here.

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

Generated run directories are excluded from Git by default. The reviewed
baseline at
`runs/R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2/`
is deliberately
committed as the first reproducible evidence package; its `manifest.json`
records the exact model revision and hashes for every artifact. Later runs
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
