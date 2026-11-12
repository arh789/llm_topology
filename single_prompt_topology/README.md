# Single-prompt semantic topology

This proof of concept measures how one target token changes across every layer
of Pythia 6.9B for one fixed prompt. It separates three forms of evidence:

- static neighbours in the input embedding matrix;
- contextual relationships among the prompt tokens across layers;
- the final next-token probability distribution.

The pipeline is intentionally contained in
`single_prompt_topology.ipynb`. Reusable Python modules, clustering, topic
modelling, multi-model comparisons and causal interventions are outside the
proof-of-concept scope.

## Before running

Shut down the kernel used by `pythia_prompt_playground.ipynb` if Pythia 12B is
still loaded. The notebook fails before creating a run when less than 14 GiB of
GPU memory is free.

Open `single_prompt_topology.ipynb`, restart the kernel, and run all cells in
order. Pythia 6.9B is loaded from the shared Hugging Face cache under `D:\AI`.

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
baseline at `runs/20261112T063540Z_pythia-6.9b_52ff8f97c2/` is deliberately
committed as the first reproducible evidence package; its `manifest.json`
records the exact model revision and hashes for every artifact. Later runs
should remain local unless they are explicitly selected for comparison or
publication.

## Interpretation boundary

This experiment is a single-prompt case study. It can validate tensor capture
and reveal candidate layer-wise changes. It cannot establish stable topics, a
generally optimal layer, causal mechanisms or a model-wide semantic topology.
