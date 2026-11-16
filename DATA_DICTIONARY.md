# Data Dictionary

Status: focused private dictionary for the article-facing R018 and R019
evidence. Earlier runs use closely related schemas but remain documented by
their own manifests and plans.

## Epistemic classes

| Class | Examples | Meaning |
|---|---|---|
| **Measured** | hidden states, logits, vocabulary scores | Direct numerical model outputs. |
| **Derived** | cosine distance, cutoffs, k-NN edges, Jaccard, ARI | Deterministic calculations from measured outputs. |
| **Interpreted** | community topic, parent label, parent relation | Semantic reconstruction performed after measurement. |

## Common identifiers

| Field | Meaning |
|---|---|
| `prompt_id` | Stable identifier for one prompt ordering. |
| `observation_id` | One permutation/repeat capture, such as `ABC_R1`. |
| `permutation` | Concept ordering, such as `ABC`, `BCA` or `CAB`. |
| `repeat_index` | Sequential repeat number within one permutation. |
| `state_index` | Captured transformer state. State 0 is the input embedding; later indices are block outputs, with the final state defined by the run configuration. |
| `state_label` | Human-readable state name, for example `block_14_output`. |
| `side` | `positive_head` or `negative_tail`, selected from opposite ends of the target-relative cosine-score distribution. |
| `comparison_type` | Usually `within_permutation_repeat` or `between_order`. |

`positive_head` means geometric alignment and `negative_tail` means geometric
anti-alignment under the selected score. Neither label independently means
helpful/harmful, accepted/rejected or central/suppressed.

## Provenance artifacts

| File | Purpose |
|---|---|
| `run_config.json` | Frozen model, prompt, capture and measurement configuration copied into the run. |
| `manifest.json` | Component status, timings, resource observations, validation and run conclusion. |
| `artifact_index.json` | Artifact path, byte size and SHA-256 hash. |
| `prompt_records.json` | Exact prompt text, token IDs, capture position and anchor identity. |
| `device_map.json` | Actual model placement across GPU, CPU and disk offload. |
| `capture_validation.json` | Shape, finiteness and deterministic-replay checks. |

## Hidden-state and score metrics

| Field | Meaning |
|---|---|
| `cosine_similarity` | Cosine of two vectors. One means identical direction; it does not require equal magnitude. |
| `cosine_distance` | `1 - cosine_similarity`. |
| `l2_distance` | Euclidean distance between two vectors. |
| `maximum_absolute_difference` | Largest absolute elementwise difference. |
| `exact_equal` | Exact tensor equality under the stored comparison path. |
| `rmse` | Root-mean-square difference between vocabulary-score vectors. |
| `jensen_shannon_divergence` | Symmetric divergence between final next-token probability distributions. |
| `top_100_token_jaccard` | Jaccard overlap between the two highest-probability 100-token sets. |

Central files:

- R018: [`pairwise_hidden_state_metrics.csv`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_hidden_state_metrics.csv).
- R019: [`pairwise_hidden_state_metrics.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_hidden_state_metrics.csv),
  [`pairwise_vocabulary_score_metrics.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_vocabulary_score_metrics.csv)
  and [`pairwise_next_token_distribution_metrics.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_next_token_distribution_metrics.csv).

## Cutoff fields

| Field | Meaning |
|---|---|
| `eligible_vocabulary_size` | Vocabulary rows available after explicit exclusions. |
| `excluded_capture_token_id` | Fixed anchor token omitted from its own neighbourhood. |
| `upper_cutoff_rank` | Full-curve elbow rank defining the positive head. |
| `lower_cutoff_rank` | Full-curve elbow rank defining the negative tail. |
| `upper_cutoff_score` / `lower_cutoff_score` | Cosine score at the selected rank. |
| `upper_elbow_strength` / `lower_elbow_strength` | Geometric strength of the selected elbow. |
| `positive_head_count` / `negative_tail_count` | Selected population size. |
| `central_body_count` | Vocabulary rows between the two selected tails. |

These cutoffs define reproducible geometric populations. They do not establish
a semantic relevance threshold.

## Network fields

Each state and side becomes an exact directed 10-nearest-neighbour graph in
the fixed input-embedding basis.

| Field | Meaning |
|---|---|
| `population_size` | Selected token count. |
| `directed_edge_count` | Directed k-NN edge count. |
| `undirected_edge_count` | Unique edge count after direction is ignored. |
| `mean_knn_cosine` | Mean cosine across selected k-NN edges. |
| `reciprocal_edge_fraction` | Fraction of directed relationships present in both directions. |
| `connected_component_count` | Number of undirected connected components. |
| `largest_component_fraction` | Fraction of nodes in the largest component. |
| `average_clustering` | Mean undirected clustering coefficient. |
| `community_count` | Number of seeded Louvain communities. |
| `community_modularity` | Louvain modularity under the recorded resolution. |

See [`network_index.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/network_index.csv).

## Topology-comparison fields

| Field | Meaning |
|---|---|
| `shared_token_count` | Tokens present in both selected populations. |
| `membership_jaccard` | Intersection divided by union of selected token IDs. |
| `retained_edge_count` | Exact graph edges present in both networks. |
| `new_edge_count` | Edges present only in the target network. |
| `disappeared_edge_count` | Edges present only in the source network. |
| `edge_jaccard` | Intersection divided by union of exact edge identities. |
| `community_adjusted_rand` | Adjusted Rand Index over community assignments for shared tokens. |

ARI compares partitions only; it does not state what a community means.

Central files:

- R018: [`pairwise_permutation_comparisons.csv`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_permutation_comparisons.csv).
- R019: [`pairwise_topology_metrics.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/pairwise_topology_metrics.csv).

## Community exports

### `community_nodes.csv`

One row per state-local community.

| Field | Meaning |
|---|---|
| `community_id` | Identifier local to one prompt, state and side. It is not stable across states. |
| `community_size` | Number of selected tokens assigned to the community. |
| `internal_edge_count` | Token edges contained within the community. |
| `boundary_edge_count` | Token edges crossing its boundary. |
| `representative_tokens` | High-degree representative tokens. |
| `most_extreme_tokens` | Tokens with the most extreme target-relative score. |
| `token_class_counts` | Broad lexical/token-shape counts. |

### `community_edges.csv`

One row per observed relationship between two state-local communities.
`token_edge_count` counts underlying token edges; `mean_cosine_similarity` and
`maximum_cosine_similarity` summarise their weights.

Community files are measured/derived graph summaries. Broad community
identities are not contained in them until a later semantic reconstruction.

## Invariance fields

| Field | Meaning |
|---|---|
| `support_count` | Number of permutations containing the token or edge. |
| `item_count` | Number of items at that support level. |
| `total_unique_items` | Union size across all permutations. |
| `fraction_of_unique_items` | `item_count / total_unique_items`. |

R018 stores these in
[`permutation_invariance.csv`](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/permutation_invariance.csv).

R019's [`divergence_by_state.csv`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/divergence_by_state.csv)
contrasts the worst observed within-permutation repeat difference with mean and
worst between-order differences at each state.

## Semantic-map outputs

`R018_SEMANTIC_MAP_NODES.csv`, `R018_SEMANTIC_MAP_EDGES.csv` and
`R018_SEMANTIC_MAP.json` are **interpreted**, not direct model outputs.

| Field | Meaning |
|---|---|
| `label` | Assigned higher-order semantic identity. |
| `status` | Invariant, contextual or excluded classification under that analysis. |
| `permutation_support` | Number of independently reconstructed permutations supporting the structure. |
| `evidence` | Tokens, communities or states used to justify the label. |
| `confidence` | Interpretive confidence, not a calibrated probability. |
| `relation` | Assigned parent-parent association. |
| `directionality` | Whether the analysis claims direction. R018 uses associative, non-causal links. |

The later [MA-0114 revision](META_ANALYSIS.md#ma-0114--chatgpt-revised-r018-semantic-analysis)
narrows the current article-level conclusion: parent-family recurrence is
better supported than one fixed invariant graph of their relations.
