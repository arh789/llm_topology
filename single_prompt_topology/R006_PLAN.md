# R006 pre-run plan: lithium ChatGPT-readable split networks

- Registration status: `executed — failed`
- Plan timestamp: `2026-11-13T06:58:00+11:00`
- Timezone: `Australia/Sydney`
- Run number: `R006`
- Neutral run name: `lithium-chatgpt-readable-split-networks`
- Expected run-directory prefix:
  `R006_lithium-chatgpt-readable-split-networks__`
- Primary source run:
  `R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2`
- Membership source run:
  `R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2`
- Ultimate capture source:
  `R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2`

## Question

What internally connected geometric communities form separately inside R004's
positive-head and negative-tail populations at each of the 33 recorded states,
and can the complete and community-level evidence be exported in formats that
let ChatGPT reconstruct, compare and challenge those networks without treating
geometric alignment as an established semantic label?

## Method

R006 is a derived export and split-network analysis. It will not run the
transformer, recalculate R002's target-to-vocabulary scores or change R004's
cutoffs.

1. Validate the successful R004 and R005 manifests and the hashes, sizes and
   identities of R004's `cutoffs.csv` and `tail_tokens.csv.gz` and R005's
   `knn_edges.csv.gz`.
2. Resolve the exact cached Pythia 6.9B revision recorded by the source runs in
   offline mode and load only `gpt_neox.embed_in.weight`.
3. For each recorded state, split R004 membership into `positive_head` and
   `negative_tail` before neighbour calculation.
4. For each of the resulting 66 state-side populations, calculate an exact
   directed cosine 10-nearest-neighbour graph inside that side only. Do not
   obtain a split graph by filtering R005's combined graph.
5. Symmetrize each directed graph by retaining an undirected edge when either
   endpoint selects the other. Use the unweighted graph for connected
   components, clustering and state-side-local Louvain communities; retain
   cosine similarity as an edge attribute.
6. Track membership, undirected edges and state-local community assignments
   across adjacent states separately for each side. Community identifiers are
   not treated as persistent semantic identities.
7. Retain the cross-region directed edges already measured by R005's combined
   10-nearest-neighbour graphs as a secondary bridge table. These edges are not
   exhaustive cross-side similarities and do not alter the split networks.
8. Export two evidence levels:
   - complete compressed node and directed-edge tables for exact reconstruction;
   - compact community-node, community-edge, JSON and Markdown packets for
     ChatGPT inspection.
9. Include decoded token labels, target-relative scores, ranks, token classes,
   community representatives and transition statistics while preserving raw
   token IDs as the stable join key.

No random baseline is added. R006's purpose is to reorganize and expose the
already selected evidence, not to repeat R005's geometric-enrichment test.

## Required components

1. `source_validation`
2. `embedding_load`
3. `split_networks`
4. `transitions_and_bridges`
5. `chatgpt_exports`
6. `validation`

Failure of any required component makes the complete run failed. The manifest
must be written with status `running` before analysis, updated after every
component, and marked `successful` only after independent artifact validation.

## Success criteria

- R004 and R005 are successful and every required source artifact matches its
  recorded byte size and SHA-256 hash.
- The cached embedding matrix belongs to the exact recorded model revision,
  has 50,277 usable rows and contains only finite, non-zero-norm vectors.
- Exactly 66 primary networks are produced: two sides for each of 33 states.
- Every state-side node count reconciles exactly with R004 membership.
- Every primary network contains exactly `population_size * 10` directed edges,
  with no self-edge and with all endpoints inside the declared side.
- Complete node rows total 191,872 and cover every R004 tail-membership row
  exactly once.
- Adjacent-state transition output contains 64 rows: 32 per side.
- Compact JSON contains all 66 community networks and enough identifiers to
  trace every compact node and edge back to the complete tables.
- Every required output is non-empty and recorded with byte size and SHA-256
  hash in a successful manifest.

## Outputs

- `manifest.json`
- `network_index.csv`
- `nodes.csv.gz`
- `edges.csv.gz`
- `community_nodes.csv`
- `community_edges.csv`
- `state_transitions.csv`
- `persistent_edges.csv.gz`
- `cross_side_edges.csv.gz`
- `chatgpt_community_networks.json`
- `chatgpt_layer_packets.md`
- `findings.md`

## Intended production command

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\export_chatgpt_split_networks.py
```

## Interpretation boundary

R006 measures relations among static vocabulary embeddings inside populations
selected by the moving contextual representation of `lithium`. The vocabulary
geometry does not change across states. `positive_head` means high cosine
compatibility with that contextual target and `negative_tail` means geometric
anti-alignment. Neither side is an established topic, and negative membership
does not establish suppression, contradiction or exclusion. Louvain
communities are geometric graph partitions whose semantic interpretation is a
subsequent analysis task.

## Out of scope

R006 will not run a new prompt, generate text, capture contextual states for
the selected vocabulary tokens, create semantic labels, choose an optimal
layer, calculate curvature density, test coherence, infer suppression, perform
causal intervention or claim model-wide generality.

## Execution record

- Run ID:
  `R006_lithium-chatgpt-readable-split-networks__20261112T200325Z_pythia-6.9b_52ff8f97c2`
- Started: `2026-11-12T20:03:25.632721+00:00`
- Failed: `2026-11-12T20:03:28.097335+00:00`
- Status: `failed`
- Successful components: `source_validation`, `embedding_load`
- Failed component: `split_networks`
- Failure: pandas raised `ValueError` because `token_id` was simultaneously an
  index level and a column label during the first community's extreme-token
  ordering.
- Transformer forward executed: `false`
- Result artifacts accepted: `none`

The failed manifest is retained. No partial output is valid for downstream
analysis. The corrected retry is registered as R007 because run numbers are
never reused.
