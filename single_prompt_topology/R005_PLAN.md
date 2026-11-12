# R005 pre-run plan: lithium cutoff-population topology baseline

- Registration status: `executed successfully — see execution record below`
- Plan timestamp: `2026-11-12T20:54:02+11:00`
- Timezone: `Australia/Sydney`
- Run number: `R005`
- Neutral run name: `lithium-cutoff-population-topology-baseline`
- Expected run-directory prefix:
  `R005_lithium-cutoff-population-topology-baseline__`
- Source run:
  `R004_lithium-full-curve-cutoffs__20261112T092701Z_pythia-6.9b_52ff8f97c2`
- Ultimate capture source:
  `R001_lithium-initial-output-inspection__20261112T063540Z_pythia-6.9b_52ff8f97c2`

## Question

Do R004's layer-specific positive-head and negative-tail populations form
denser or more region-segregated local relationship networks in Pythia's
static input-embedding space than size-matched random token populations, and
how do population membership, graph edges and community structure vary across
the 33 recorded states?

## Method

R005 is a derived analysis of R004. It will not run the transformer or
recalculate R002's target-to-vocabulary scores.

1. Validate the successful R004 manifest and the hashes, sizes and identities
   of `cutoffs.csv` and `tail_tokens.csv.gz`.
2. Resolve the exact cached Pythia 6.9B revision recorded by R004 in offline
   mode and load only `gpt_neox.embed_in.weight`.
3. Normalize the 50,277 static input embeddings with float32 arithmetic.
4. At each recorded state, combine R004's positive-head and negative-tail
   tokens and calculate an exact directed cosine 10-nearest-neighbour graph,
   excluding self-relations.
5. Symmetrize the directed graph by retaining an undirected edge when either
   endpoint selects the other. Use the unweighted symmetrized graph for
   connected components, clustering and Louvain communities. Preserve cosine
   similarity as a descriptive edge attribute.
6. Record upper-to-upper, lower-to-lower and cross-region directed-edge
   proportions; nearest-neighbour similarity; reciprocity; connected
   components; clustering; community modularity; community composition and
   community-to-region normalized mutual information.
7. For every state, generate 20 deterministic random populations sampled
   without replacement from the target-removed vocabulary. Match the observed
   positive, negative and total population sizes exactly, apply the identical
   10-nearest-neighbour calculation, and compare mean nearest-neighbour
   similarity, same-region edge fraction and reciprocity. Use seed `20261112`.
8. Across adjacent states, calculate combined, positive and negative
   membership Jaccard overlap; undirected edge Jaccard overlap; new,
   disappeared and retained edge counts; region agreement on shared tokens;
   and adjusted Rand index for state-local Louvain assignments on shared
   tokens.
9. Save state-local community assignments and summaries. Community identifiers
   are not treated as persistent identities across layers; adjusted Rand index
   and token overlap provide the declared stability measurements.
10. Create descriptive figures for observed-versus-random metrics, adjacent
    state stability and community-level networks at states 0, 8, 16, 24 and
    32.

The random baseline controls population size only. It does not control token
class, lexical form, frequency or rank, so an observed difference cannot by
itself establish semantic usefulness.

## Required components

1. `source_validation`
2. `embedding_load`
3. `observed_graphs`
4. `random_baselines`
5. `transition_analysis`
6. `communities_and_figures`
7. `validation`

Failure of any required component makes the complete run failed. The manifest
must be written with status `running` before analysis, updated after every
component, and marked `successful` only after independent artifact validation.

## Success criteria

- R004 is successful and every required source artifact matches its recorded
  byte size and SHA-256 hash.
- The cached embedding matrix belongs to the exact model revision recorded by
  R004, has 50,277 usable rows and contains only finite values.
- All 33 observed populations reconcile exactly with R004's cutoff counts.
- Every observed graph contains exactly `population_size * 10` directed edges
  with no self-relation.
- The null table contains exactly `33 * 20` independently sampled,
  size-matched populations.
- All graph, comparison and transition metrics are finite where mathematically
  defined.
- Every required output is non-empty and recorded with byte size and SHA-256
  hash in a successful manifest.

Statistical enrichment is not a success criterion. A null or contrary result
is a valid R005 finding.

## Outputs

- `manifest.json`
- `state_topology_metrics.csv`
- `random_baseline_metrics.csv`
- `observed_vs_random.csv`
- `knn_edges.csv.gz`
- `community_assignments.csv.gz`
- `community_summary.csv`
- `state_transitions.csv`
- `persistent_edges.csv.gz`
- `findings.md`
- `figures/topology_vs_random.png`
- `figures/transition_stability.png`
- `figures/selected_state_community_networks.png`

## Intended production command

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' single_prompt_topology\cutoff_population_topology.py
```

## Interpretation boundary

R005 measures relations among static vocabulary embeddings inside populations
selected by a moving contextual `lithium` representation. The vocabulary
geometry itself does not change across states. Any layer-wise change therefore
comes from population selection, not contextual evolution of every selected
token. Communities are geometric graph partitions, not established semantic
topics. Negative-tail membership remains anti-alignment under R002's cosine
measurement, not evidence of predictive suppression or contradiction.

## Out of scope

R005 will not run another prompt, generate text, capture contextual states for
the selected vocabulary, choose an optimal layer, calculate curvature density,
perform causal intervention, infer semantic conflict, tune graph parameters to
the observed result, or claim model-wide generality.

## Execution record

- Registration status: `executed successfully`
- Run ID:
  `R005_lithium-cutoff-population-topology-baseline__20261112T095944Z_pythia-6.9b_52ff8f97c2`
- Started: `2026-11-12T09:59:44.418264+00:00`
- Completed: `2026-11-12T10:01:29.377084+00:00`
- Total elapsed time: approximately `104.96 seconds`
- Status: `successful`
- Required components: `7 successful of 7`
- Output artifacts: `12 of 12 independently hash-validated`
- Observed states: `33 of 33`
- Directed 10-nearest-neighbour edges: `1,918,720`
- Random populations: `660` (`20` per state)
- Community-assignment rows: `191,872`
- Persistent undirected edges present in at least two states: `191,879`
- Peak allocated GPU memory: `2.11 GiB`
- Model forward executed: `false`
- Full model loaded: `false`
- Static embedding weight loaded: `true`

### Principal observations

- Mean nearest-neighbour cosine exceeded the size-matched random 97.5th
  percentile at all 33 states. The median observed-minus-random difference was
  `0.005669`; the range was `0.004257` to `0.029047`.
- Same-region edge fraction exceeded the random 97.5th percentile at all 33
  states. The median excess was `0.179517`, while the input-embedding state's
  excess was `0.381059`.
- Reciprocity was mixed rather than universally enriched: 16 states exceeded
  the random 97.5th percentile and two fell below the random 2.5th percentile.
- Median adjacent-state combined membership Jaccard was `0.7561`; median edge
  Jaccard was `0.5307`; median state-local community adjusted Rand index was
  `0.3827`.
- The input-to-block-0 transition was discontinuous: membership Jaccard
  `0.0409` and edge Jaccard `0.0032`.
- The block-30-to-final-normalized transition was also discontinuous:
  membership Jaccard `0.2100` and edge Jaccard `0.0580`. Because the capture
  lacks raw block-31 output, this change cannot be separated into block-31 and
  final-layer-normalization effects.
- Community-to-region normalized mutual information was `0.2791` at the input
  embedding, fell to `0.0121` after block 0 and had a median of `0.0134` across
  all states. Later communities therefore mixed positive and negative
  membership despite the elevated same-region local-edge fraction.
- Persistent edges included recognizable lexical or morphological relations,
  such as `barrel`–`barrels`, alongside repeated punctuation and tokenizer
  artifacts. This prevents a semantic-topic interpretation from geometry alone.

The manifest records the pre-execution SHA-256 of this plan. This execution
record was appended only after the successful manifest and all 12 artifact
hashes were independently revalidated.
