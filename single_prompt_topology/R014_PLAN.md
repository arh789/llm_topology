# R014 plan: overlapping-context local semantic map

## Run identity

- Run number: `R014`
- Run directory: `R014_qwen-overlapping-context-semantic-map`
- Run type: measured four-probe, twenty-four-prompt context-invariance topology
- Initial status: `planned`
- Backend: Hugging Face Transformers + `Qwen/Qwen2.5-7B-Instruct`, BF16

## Objective

Test whether the higher-order semantic structures identified downstream from
R013 can be reconstructed across different overlapping concept contexts, not
merely across different orders of one fixed triplet.

R014 produces the measured evidence needed to reconstruct four probes
independently and later determine whether stable semantic parents and parent
relations recur across probes. Transformer depth remains the measurement
instrument. The intended downstream object is a local semantic map, if the
evidence supports one.

Semantic parent reconstruction and map construction remain outside the
measured R014 pipeline.

## Locked concept-selection evidence

The concept pool is derived from R013 measured networks and is documented in
`R014_CONCEPT_SELECTION_EVIDENCE.md`.

```text
A = laser
B = city
C = spatial field
D = clubs
```

These concrete concepts sample four parts of the R013 semantic region without
feeding the inferred parent labels themselves into the prompts.

## Locked probes and prompts

The four overlapping probes are:

| Probe | Concepts |
|---|---|
| P1 | laser, city, spatial field |
| P2 | laser, city, clubs |
| P3 | laser, spatial field, clubs |
| P4 | city, spatial field, clubs |

Every probe is measured in all six local position orders:

```text
ABC, ACB, BAC, BCA, CAB, CBA
```

Here `A`, `B` and `C` denote positions in one probe's three-item tuple, not
the global concept letters. This yields exactly 24 prompt trajectories.

Each concept occupies one line. Every raw input ends with one fixed candidate
newline anchor. No chat template, system message, user-role marker, assistant
prefix, synthesis question or response generation is permitted.

## Pair and context coverage

Every concept occurs in three probes. Every concept pair occurs in two
different third-concept contexts:

| Pair | Context 1 | Context 2 |
|---|---|---|
| laser ↔ city | spatial field | clubs |
| laser ↔ spatial field | city | clubs |
| laser ↔ clubs | city | spatial field |
| city ↔ spatial field | laser | clubs |
| city ↔ clubs | laser | spatial field |
| spatial field ↔ clubs | laser | city |

This is the minimum balanced four-concept design that tests both order and
context perturbation without expanding to a global map.

## Anchor control

Before capture is accepted, the tokenizer probe must establish that:

- newline alone tokenises to exactly one token;
- the final token in all 24 inputs is the same newline token ID;
- the final token is the capture position in every input;
- the capture rule is identical for every probe and permutation; and
- State 00 is exactly equal across all 24 trajectories.

Any failure stops the run before topology analysis.

## Locked model and runtime

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- Precision: BF16
- Runtime: Hugging Face Transformers
- Device: RTX 4090
- Cache: `D:\AI\cache\huggingface`
- Model loading: local cache only

R014 must not change the R013 measurement instrument.

## Capture contract

For every prompt, capture the final anchor position at:

1. input embedding state;
2. every transformer-block output; and
3. final normalisation after Block 27.

Expected trajectory coverage:

```text
24 prompts × 29 states × 3,584 hidden dimensions
```

Every trajectory must be finite and exactly reproducible on deterministic
replay. State 00 equality across all 24 prompts is a hard control.

## Measurement contract

Reuse R013 unchanged:

- cosine projection against the fixed input-embedding vocabulary;
- exclusion of the shared capture-anchor token from cutoff selection;
- independent positive-head and negative-tail selection using the R004
  full-curve maximum-deviation elbow;
- exact 10-nearest-neighbour graphs in the fixed input-embedding basis;
- edge symmetrisation when either directed relation exists;
- deterministic unweighted NetworkX Louvain partitions;
- token IDs as stable join keys; and
- community IDs local to one prompt, state and side.

No new cutoff, graph, community or composite-curvature method is permitted.

## Required measured coverage

```text
24 prompts × 29 states × 2 sides = 1,392 networks

24 prompts × 28 transitions × 2 sides
= 1,344 within-prompt transition rows

4 probes × C(6,2) permutation pairs × 29 states × 2 sides
= 3,480 within-probe permutation-comparison rows
```

Within each probe, token and edge support must be counted independently across
its six permutations at support levels 1/6 through 6/6.

## Required components

1. `plan_lock`
2. `concept_selection_lock`
3. `environment_probe`
4. `anchor_probe`
5. `primary_capture`
6. `capture_validation`
7. `projection_and_cutoffs`
8. `split_networks_and_communities`
9. `within_prompt_transitions`
10. `within_probe_permutation_comparisons`
11. `within_probe_invariance`
12. `chatgpt_exports`
13. `completeness_validation`
14. `run_report`

The manifest remains `running` until all fourteen components pass.

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
- `R014_COMPLETENESS_VERIFICATION.md`
- `R014_MEASUREMENT_REPORT.md`
- `manifest.json`
- `artifact_index.json`

## Success criteria

- Every capture control passes.
- The three frozen coverage counts are exact.
- Every network has exactly ten directed neighbours per selected token.
- State 00 topology is identical across all within-probe permutation pairs on
  both sides.
- Every node and edge remains traceable to probe, prompt, permutation, state
  and side.
- ChatGPT can inspect all 1,392 measured networks and their communities.
- No model weights are stored in the repository.
- No response is generated.
- No R013 parent labels are imposed on R014 communities.
- No semantic parents, map nodes, map edges, SDA/GRD roles, coherence claims or
  semantic-curvature claims are introduced by the measured pipeline.

A result with no stable cross-context semantic map remains scientifically
valid if the measurement and downstream independent reconstruction can
establish it.

## Failure conditions

- the anchor probe or State 00 equality control fails;
- any trajectory is missing, non-finite, dimensionally wrong or not exactly
  reproducible;
- model identity, revision or cache identity differs from the lock;
- any cutoff population overlaps or lacks a valid interior elbow;
- any required network, transition or within-probe comparison is absent;
- support accounting or referential integrity fails;
- ChatGPT-readable exports omit measured networks or communities; or
- the manifest is marked successful before all required checks pass.

## Outside scope

- semantic parent reconstruction during measurement;
- forcing R013 labels onto R014 communities;
- additional concepts or probes;
- cross-model or base-versus-instruct comparisons;
- alternative anchors, cutoffs, graph parameters or community algorithms;
- response generation;
- global semantic-map construction;
- external corpus comparison;
- curvature/coherence composites; and
- committing or pushing Git changes during the run.

## Production entry point

```powershell
C:\Users\arhal\anaconda3\envs\myenv\python.exe single_prompt_topology\r014_run.py
```

This command must execute capture, validation and topology production in order
and return failure if any required component fails.
