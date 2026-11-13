# R013 plan: bare-concept permutation topology

## Run identity

- Run number: `R013`
- Run directory: `R013_qwen-bare-concept-permutation-topology`
- Run type: measured six-permutation whole-prefix semantic topology
- Initial status: `planned`
- Backend: Hugging Face Transformers + `Qwen/Qwen2.5-7B-Instruct`, BF16

## Objective

Measure the layer-wise semantic topology induced jointly by the same three
concepts without an explicit synthesis instruction or assistant-generation
prefix. Determine which measured tokens and edges are invariant across every
concept ordering and which structures vary with ordering conditions.

R013 measures structural dependencies associated with order, concept position,
final-position/recency, adjacency and residual ordering interactions. A single
three-concept permutation experiment does not independently identify those as
separate causal effects.

Semantic interpretation remains outside R013.

## Locked concepts and permutations

```text
A = electro pink
B = curvature density
C = Tokyo nightlife
```

The six labels and raw-text orders are:

| Permutation | Position 1 | Position 2 | Position 3 |
|---|---|---|---|
| ABC | A | B | C |
| ACB | A | C | B |
| BAC | B | A | C |
| BCA | B | C | A |
| CAB | C | A | B |
| CBA | C | B | A |

Each concept occupies one line. The input ends with one candidate newline
anchor. No chat template, system message, user-role marker, assistant prefix,
synthesis question or response generation is permitted.

## Anchor control

The candidate anchor is the final newline in each raw input. Before the model
capture is accepted, the tokenizer probe must establish that:

- newline alone tokenises to exactly one token;
- the final token in all six inputs is that same token ID;
- the final token is unambiguously the capture position;
- the capture rule is identical for all permutations; and
- the State 00 vector is exactly equal across all six trajectories.

If any condition fails, the run must stop before topology analysis. A different
minimal delimiter may be selected only before the main capture and must then be
recorded and fixed for all six inputs.

Equal tokenised input length is recorded but is not required; the controlled
position is always the final anchor token.

## Locked model and runtime

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- Precision: BF16
- Runtime: Hugging Face Transformers
- Device: RTX 4090
- Cache: `D:\AI\cache\huggingface`
- Model loading: local cache only

Keeping the R012 model fixed isolates the prompt-design change. A base-model
comparison belongs to a later run.

## Capture contract

For each permutation, capture the final anchor position at:

1. input embedding state;
2. every transformer-block output; and
3. final normalisation after Block 27.

Expected trajectory coverage:

```text
6 permutations × 29 states × 3,584 hidden dimensions
```

Every trajectory must be finite and exactly reproducible on deterministic
replay. State 00 equality across all permutations is a hard control. Later
states may be equal or different; either result is admissible evidence.

## Measurement contract

Reuse the R012 method unchanged:

- cosine projection against the fixed input-embedding vocabulary;
- exclusion of the shared capture-anchor token from cutoff selection;
- independent positive-head and negative-tail selection using the R004
  full-curve maximum-deviation elbow;
- exact 10-nearest-neighbour graphs in the fixed input-embedding basis;
- edge symmetrisation when either directed relation exists;
- deterministic unweighted NetworkX Louvain partitions;
- token IDs as stable join keys; and
- community IDs local to one permutation, state and side.

No new cutoff, graph, community or composite-curvature method is permitted.

## Required measured coverage

```text
6 permutations × 29 states × 2 sides = 348 networks
6 permutations × 28 transitions × 2 sides = 336 adjacent-state rows
C(6,2) × 29 states × 2 sides = 870 matched-state pair rows
```

For every state and side, token and undirected-edge support must be counted
independently across the six permutations:

```text
support = 1/6, 2/6, 3/6, 4/6, 5/6 or 6/6
```

Token survival and edge survival are distinct measurements. Community
comparison remains pairwise through adjusted Rand index and overlap evidence;
R013 does not claim that local community IDs persist across permutations.

## Required components

1. `plan_lock`
2. `environment_probe`
3. `anchor_probe`
4. `primary_capture`
5. `capture_validation`
6. `projection_and_cutoffs`
7. `split_networks_and_communities`
8. `within_permutation_transitions`
9. `pairwise_permutation_comparisons`
10. `permutation_invariance`
11. `chatgpt_exports`
12. `completeness_validation`
13. `run_report`

The manifest remains `running` until all thirteen components pass.

## Required artifacts

- `primary_7b_bf16/*_hidden_states.safetensors`
- `primary_7b_bf16/prompt_records.json`
- `primary_7b_bf16/permutation_validation.json`
- `primary_7b_bf16/pairwise_hidden_state_metrics.csv`
- `vocabulary_scores.safetensors`
- `cutoffs.csv`
- `tail_tokens.csv.gz`
- `network_index.csv`
- `nodes.csv.gz`
- `edges.csv.gz`
- `community_nodes.csv`
- `community_edges.csv`
- `state_transitions.csv`
- `pairwise_permutation_comparisons.csv`
- `permutation_invariance.csv`
- `token_permutation_support.csv.gz`
- `edge_permutation_support.csv.gz`
- `community_transition_evidence.csv`
- `chatgpt_community_networks.json`
- `chatgpt_layer_packets.md`
- `R013_COMPLETENESS_VERIFICATION.md`
- `R013_MEASUREMENT_REPORT.md`
- `manifest.json`
- `artifact_index.json`

## Success criteria

- Every capture control passes.
- All exact coverage counts and referential-integrity checks pass.
- Every network has exactly ten directed neighbours per selected token.
- State 00 membership, edges and deterministic communities are identical
  across all fifteen permutation pairs on both sides.
- Token and edge support are calculated separately for every state and side.
- ChatGPT can inspect every measured network and community from the exported
  JSON, Markdown and CSV evidence.
- No model weights are stored in the repository.
- No response is generated.
- No semantic topics, parent nodes, SDA roles, GRD roles, coherence claims or
  semantic-curvature claims are introduced.

A null order effect or an absence of a 6/6 invariant core is a valid result if
the measurement and validation are complete.

## Failure conditions

- the anchor probe or State 00 equality control fails;
- any trajectory is missing, non-finite, dimensionally wrong or not exactly
  reproducible;
- model identity, revision or cache identity differs from the locked plan;
- any cutoff population overlaps or lacks a valid interior elbow;
- any of the 348 networks, 336 transitions or 870 pairwise comparisons is
  absent;
- token/edge support does not reconcile with all network populations;
- network, community or artifact referential integrity fails;
- ChatGPT-readable exports omit measured networks or communities; or
- the manifest is marked successful before all required checks pass.

## Outside scope

- semantic interpretation;
- additional concept sets;
- base-model or larger-model comparisons;
- alternative anchors after capture begins;
- response generation;
- pairwise concept deletion;
- alternative graph/community parameters;
- GRD, SDA-3, parent reconstruction, coherence or curvature analysis;
- committing or pushing Git changes.

## Production entry point

The complete run is executed by:

```powershell
C:\Users\arhal\anaconda3\envs\myenv\python.exe single_prompt_topology\r013_run.py
```

That entry point must run capture, validation and topology production stages in
order and return a failure status if any required stage fails.
