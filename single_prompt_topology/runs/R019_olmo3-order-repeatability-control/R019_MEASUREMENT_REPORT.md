# R019 order-versus-repeatability measurement report

## Result

`deterministic_order_effect_confirmed`

R019 executed three sequential forward passes for each of the balanced cyclic
permutations `ABC`, `BCA` and `CAB`. No response was generated and no token was
sampled.

## Measured repeat noise floor

- Hidden states exact across identical repeats at all 65 states: `True`
- Full-vocabulary score vectors exact across repeats: `True`
- Final next-token logits exact across repeats: `True`
- Cutoff membership, 10-NN edges and seeded Louvain partitions exact across repeats: `True`
- Maximum within-repeat hidden cosine distance: `0`
- Maximum within-repeat vocabulary-score RMSE: `0`
- Maximum within-repeat next-token Jensen-Shannon divergence: `0`
- Minimum within-repeat membership Jaccard: `1`
- Minimum within-repeat edge Jaccard: `1`
- Minimum within-repeat community ARI: `1`

## Measured order divergence

- Order effect detected after State 00: `True`
- Minimum between-order hidden cosine similarity: `0.609119475`
- Maximum between-order vocabulary-score RMSE: `0.012455868`
- Maximum between-order next-token Jensen-Shannon divergence: `0.052628301`
- Minimum between-order cutoff-membership Jaccard: `0.158392029`
- Minimum between-order 10-NN edge Jaccard: `0.041658627`

The strongest hidden-state divergence occurred for
`ABC_R1` versus
`BCA_R1` at State
`15`
(`block_14_output`).

## Conclusion boundary

This result determines whether R018's permutation differences exceed the
measured repeat noise floor. It does not identify semantic parents or explain
what the order-conditioned structures mean.

The final token seed is irrelevant to this experiment because there was no
sampling. The fixed random seed applies only to deterministic graph-community
bookkeeping.
