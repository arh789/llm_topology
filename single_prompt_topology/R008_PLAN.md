# R008 pre-run plan: lithium ChatGPT-readable split networks validated retry

- Registration status: `executed successfully — see execution record below`
- Plan timestamp: `2026-11-13T07:07:46+11:00`
- Timezone: `Australia/Sydney`
- Run number: `R008`
- Neutral run name: `lithium-chatgpt-readable-split-networks-validated-retry`
- Expected run-directory prefix:
  `R008_lithium-chatgpt-readable-split-networks-validated-retry__`
- Corrects failed run:
  `R007_lithium-chatgpt-readable-split-networks-retry__20261112T200549Z_pythia-6.9b_52ff8f97c2`
- Primary source run:
  `R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2`
- Membership source run:
  `R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2`
- Ultimate capture source:
  `R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2`

## Correction

R007 completed every analysis and export component, then failed final
validation because physical gzip lines were incorrectly treated as CSV rows.
CSV-aware parsing independently confirmed that R007 contained the planned
191,872 node records; the extra physical lines came from tokenizer strings with
embedded newline characters. R008 validates node rows with pandas CSV parsing
instead. It does not reuse any R007 result artifact and reruns the complete
analysis from the validated R004 and R005 sources.

## Question

What internally connected geometric communities form separately inside R004's
positive-head and negative-tail populations at each of the 33 recorded states,
and can the complete and community-level evidence be exported in formats that
let ChatGPT reconstruct, compare and challenge those networks without treating
geometric alignment as an established semantic label?

## Method

R008 is a derived export and split-network analysis. It will not run the
transformer, recalculate R002's target-to-vocabulary scores or change R004's
cutoffs.

1. Validate the successful R004 and R005 manifests and the exact source
   artifact hashes.
2. Load only the exact cached Pythia input-embedding weight in offline mode.
3. Split every R004 state into `positive_head` and `negative_tail` before
   calculating exact directed cosine 10-nearest-neighbour graphs.
4. Construct and analyze all 66 within-side graphs, with state-side-local
   Louvain communities and unweighted symmetrized topology.
5. Track membership, edge and community-assignment stability across adjacent
   states separately for each side.
6. Retain R005's cross-region combined-graph edges as a secondary, explicitly
   non-exhaustive bridge table.
7. Export complete compressed node and edge data plus compact community CSV,
   JSON and Markdown evidence for ChatGPT.
8. Validate node records with a CSV parser so embedded newlines remain valid
   field content rather than being miscounted as records.

No random baseline is added. R008 reorganizes existing selected evidence and
does not repeat R005's enrichment test.

## Required components

1. `source_validation`
2. `embedding_load`
3. `split_networks`
4. `transitions_and_bridges`
5. `chatgpt_exports`
6. `validation`

Failure of any required component makes the complete run failed. The manifest
must be written as `running` before analysis and may become `successful` only
after every required output passes independent validation.

## Success criteria

- All planned source identities, sizes and hashes validate.
- The exact cached embedding matrix has 50,277 finite, non-zero-norm rows.
- Exactly 66 primary state-side networks are produced.
- Node counts exactly match R004: 191,872 parsed CSV records in total.
- Each network contains exactly `population_size * 10` directed within-side
  edges with no self-edge.
- Transition output contains 64 rows, 32 per side.
- Compact JSON contains all 66 networks and traceable identifiers.
- All required outputs are non-empty, hashed and recorded by a successful
  manifest.

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

R008 measures relations among static vocabulary embeddings inside populations
selected by the moving contextual representation of `lithium`. The vocabulary
geometry does not change. Positive means target-relative cosine alignment and
negative means anti-alignment. Neither establishes a topic, suppression,
contradiction, exclusion or curvature. Communities are geometric partitions
awaiting independent semantic interpretation.

## Out of scope

R008 will not run a new prompt, generate text, capture contextual states for
the selected vocabulary tokens, create semantic labels, choose an optimal
layer, calculate curvature density, test coherence, infer suppression, perform
causal intervention or claim model-wide generality.

## Execution record

- Registration status: `executed successfully`
- Run ID:
  `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Started: `2026-11-12T20:09:04.421258+00:00`
- Completed: `2026-11-12T20:10:54.908947+00:00`
- Status: `successful`
- Required components: `6 successful of 6`
- Output artifacts: `11 of 11 independently hash-validated`
- Primary networks: `66`
- Node-state rows: `191,872`
- Directed within-side edges: `1,918,720`
- State-side community rows: `792`
- Intercommunity edge rows: `4,384`
- Adjacent-state transition rows: `64`
- Persistent within-side edges: `191,262`
- Secondary cross-side directed edges: `604,515`
- Compact JSON networks: `66`
- Peak allocated GPU memory: `2.11 GiB`
- Model forward executed: `false`
- Full model loaded: `false`
- Static embedding weight loaded: `true`

### Principal observations

- Positive-head networks contained 1,871–3,491 nodes and 9–14 Louvain
  communities. Their modularity ranged from 0.4987 to 0.5890.
- Negative-tail networks contained 1,316–3,313 nodes and 10–15 communities.
  Their modularity ranged from 0.4686 to 0.5418.
- Median adjacent-state membership Jaccard was 0.7537 for positive networks and
  0.7582 for negative networks. Median edge Jaccard was 0.5344 and 0.5371,
  respectively.
- Median adjacent-state community adjusted Rand index was 0.3749 for positive
  networks and 0.3986 for negative networks.
- Both sides showed their largest discontinuity from the input embedding to
  block 0 and a second large discontinuity from block 30 to the final
  normalized state.
- Persistent relationships include recognizable lexical pairs and tokenizer or
  formatting artifacts. Semantic topics are not established by persistence or
  community membership alone.
- The 604,515 cross-side relations are 31.51% of R005's combined directed
  edges. They are a secondary retained subset, not an exhaustive bipartite
  similarity graph.

The manifest records the pre-execution SHA-256 of this plan. This execution
record was appended only after the successful manifest and all 11 artifact
hashes were independently revalidated.
