# R005 findings: cutoff-population topology baseline

## Direct observations

- All 33 R004 populations produced exact 10-nearest-neighbour graphs.
- Observed mean nearest-neighbour cosine exceeded the 97.5th percentile of the size-matched random baseline at 33 of 33 states.
- Observed same-region edge fraction exceeded the random 97.5th percentile at 33 of 33 states.
- The largest mean-neighbour-cosine excess occurred at state 0 (`input_embedding`): 0.029047.
- The smallest mean-neighbour-cosine excess occurred at state 26 (`block_25_output`): 0.004257.
- The largest same-region-edge excess occurred at state 0 (`input_embedding`): 0.381059.
- Median adjacent-state combined membership Jaccard was 0.7561; median edge Jaccard was 0.5307; median community adjusted Rand index was 0.3827.
- Louvain community count ranged from 11 to 15; modularity ranged from 0.5241 to 0.5733.
- 191,879 undirected relationships appeared in at least two states.

## Most persistent observed relationships

- `--------------------------------------------------------------------------------------------------------------------------------` ↔ `␠----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------`: 32/33 states, mean cosine 0.2824.
- `␠Princess` ↔ `␠goddess`: 32/33 states, mean cosine 0.1698.
- `␠----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------` ↔ `srep`: 32/33 states, mean cosine 0.1257.
- `␠goddess` ↔ `␠Creator`: 32/33 states, mean cosine 0.1156.
- `␠barrel` ↔ `␠barrels`: 31/33 states, mean cosine 0.5498.
- `␠curb` ↔ `␠sidewalk`: 31/33 states, mean cosine 0.2193.
- `␠Devil` ↔ `␠serpent`: 31/33 states, mean cosine 0.1359.
- `␠development` ↔ `␠regeneration`: 31/33 states, mean cosine 0.1255.
- `␠goddess` ↔ `␠serpent`: 31/33 states, mean cosine 0.1030.
- `␠barrels` ↔ `␠cartridges`: 31/33 states, mean cosine 0.1008.

## Supported conclusion

R004's selected populations can be tested as relationship networks. Differences from the size-matched null establish geometric organization relative to that null; they do not establish semantic topics, contextual evolution of every vocabulary token, an optimal layer or causal conflict.

## Limitations

- The input-embedding geometry is fixed across all states; only selected membership changes.
- The null controls positive, negative and total population sizes only. It does not control token class, morphology, frequency or score rank.
- Louvain communities are state-local geometric partitions. Community IDs are not persistent topic identities.
- Twenty null replicates give a minimum one-sided empirical p-value of 1/21 ≈ 0.0476 and are suitable only for this proof of concept.
