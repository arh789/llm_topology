# R012 plan: generalised whole-prompt semantic topology

## Run identity and status history

- Run number: `R012`
- Existing run directory: `R012_qwen-whole-prompt-paired-capture`
- Run type: measured paired-prompt whole-prompt semantic topology
- Current status: `running`
- First validated backend: Hugging Face Transformers +
  `Qwen/Qwen2.5-7B-Instruct`, BF16

The directory name is retained for provenance. It does not limit the run to
capture. R012 is the corrected implementation of the general pipeline intended
by R011. The Qwen capture is an intermediate prerequisite, not the final
research output.

R012 was initially marked successful after hidden-state capture. Subsequent
scope review established that this was a failure of completion criteria: the
run had not produced semantic-network evidence suitable for ChatGPT analysis.
The capture artifacts remain valid and immutable, while the overall run is
reopened as `running` until the downstream measured pipeline completes.

## Objective

Implement and validate a generalised whole-prompt semantic-topology pipeline
using a model/runtime that exposes intermediate hidden states. Convert the
existing paired Qwen trajectories through vocabulary projection, full-curve
region selection, token-network construction, community detection,
cross-layer comparison, paired-prompt comparison and ChatGPT-readable measured
exports.

Semantic interpretation remains outside R012.

## Controlled prompt pair

Baseline:

```text
What structure forms from electro pink, curvature density, Tokyo nightlife?
```

Variation:

```text
What structure forms from electro pink, Tokyo nightlife, curvature density?
```

The only intended change is the order of `curvature density` and
`Tokyo nightlife`.

## Minimal backend contract

A model backend must provide the equivalent of:

1. `capture_states(prompt)`
2. `get_embedding_matrix()`
3. `get_vocabulary()`
4. `get_state_labels()`
5. `get_model_metadata()`

R012 validates one direct Qwen implementation. It does not add registries,
factories or untested model adapters. Everything after those five inputs is
model-independent.

## Measurement contract

- Reuse the already validated final-position hidden-state trajectories.
- Project every state against the fixed input-embedding vocabulary with cosine
  similarity.
- Determine positive-head and negative-tail membership independently with the
  R004 full-curve maximum-deviation elbow method; do not add acceptance gates.
- Exclude neither side on interpretive grounds. Negative cosine means geometric
  anti-alignment, not established suppression or contradiction.
- Within each prompt, state and side, create an exact 10-nearest-neighbour graph
  in the fixed input-embedding space.
- Symmetrise an edge when either directed relation exists.
- Detect state-local communities with deterministic unweighted NetworkX
  Louvain partitions.
- Compare adjacent states within each prompt and compare the paired prompts at
  identical states.
- Preserve token IDs as stable join keys. Community IDs remain local to one
  prompt, state and side.
- Export measured evidence without semantic topic labels or GRD/SDA roles.

## Required components

1. `plan_lock`
2. `environment_probe`
3. `smoke_0_5b_capture`
4. `smoke_0_5b_validation`
5. `primary_7b_capture`
6. `primary_7b_validation`
7. `projection_and_cutoffs`
8. `split_networks_and_communities`
9. `within_prompt_transitions`
10. `paired_prompt_comparisons`
11. `chatgpt_exports`
12. `completeness_validation`
13. `run_report`

The run is successful only if all thirteen components succeed.

## Required coverage and artifacts

- 2 prompts × 29 states × 2 sides = **116** networks.
- 2 prompts × 28 adjacent transitions × 2 sides = **112** within-prompt
  transition rows.
- 29 states × 2 sides = **58** same-state paired-prompt comparison rows.
- Every selected token belongs to exactly one state-local community.
- Every edge endpoint belongs to its corresponding network.

Required outputs include:

- `vocabulary_scores.safetensors`
- `cutoffs.csv`
- `tail_tokens.csv.gz`
- `network_index.csv`
- `nodes.csv.gz`
- `edges.csv.gz`
- `community_nodes.csv`
- `community_edges.csv`
- `state_transitions.csv`
- `paired_state_comparisons.csv`
- `community_transition_evidence.csv`
- `chatgpt_community_networks.json`
- `chatgpt_layer_packets.md`
- `R012_COMPLETENESS_VERIFICATION.md`
- updated `manifest.json`
- updated factual run report

## Execution order

1. Preserve and verify the existing capture artifacts.
2. Reopen the manifest as `running` and record the scope-correction history.
3. Load only the cached Qwen tokenizer and input-embedding tensor; do not load
   the full model or perform another forward pass.
4. Project both trajectories and calculate full-curve cutoffs.
5. Construct all split networks and state-local communities.
6. Calculate adjacent-state and paired-prompt structural comparisons.
7. Export complete token-level evidence and compact ChatGPT-readable packets.
8. Validate coverage, referential integrity, finiteness and artifact hashes.
9. Mark the run `successful` only after every required component passes.

## Success criteria

- All required components and exact coverage counts pass.
- No model weights are stored in the repository.
- The model is not re-run and no response token is generated.
- Cutoffs are derived from the complete score curve by the locked R004 method.
- ChatGPT can reconstruct every network and inspect every community from the
  exported JSON/Markdown/CSV evidence.
- Measurement remains distinct from semantic interpretation.
- A null paired-prompt difference is accepted if the evidence is complete.

## Outside scope

- response generation;
- semantic topic labels or parent-node reconstruction;
- GRD, SDA-3 or Phase B/C/D interpretation;
- additional prompt variations;
- quantisation comparisons;
- larger models;
- adapter registries or speculative abstraction layers;
- modification of R011;
- committing or pushing Git changes.

## Failure conditions

- any required capture artifact fails hash or identity validation;
- the input embedding or tokenizer cannot be loaded from the shared cache;
- any state projection is missing, non-finite or dimensionally inconsistent;
- any state-side lacks a valid interior elbow or the two populations overlap;
- any of the 116 networks, 112 transitions or 58 paired comparisons is absent;
- nodes, edges or communities fail referential-integrity checks;
- semantic labels are introduced into measured artifacts;
- ChatGPT-readable exports omit measured networks or communities; or
- the manifest is marked successful before all validation passes.
