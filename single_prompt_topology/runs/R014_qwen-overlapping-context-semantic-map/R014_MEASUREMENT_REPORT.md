# R014 overlapping-context topology measurement report

## Outcome

R014 completed the controlled four-probe, 24-prompt measurement pipeline. Every overlapping concept triplet was measured in six orders at the same final newline anchor. The trajectories were projected into the fixed input-embedding vocabulary, divided by the locked full-curve elbows, converted into 1,392 exact split networks, partitioned into state-local communities and compared within each probe across depth and order.

No chat template, assistant prefix or response generation was used. No semantic topic labels, parent nodes, cross-probe map nodes/edges, SDA roles, GRD roles, coherence claims or semantic-curvature claims were inferred.

## Coverage

- Probes: 4
- Prompts: 24
- Networks: 1392
- Selected token memberships: 10,447,003
- Directed 10-NN edges: 104,470,030
- State-local communities: 14,686
- Within-prompt adjacent-state comparisons: 1344
- Within-probe same-state permutation comparisons: 3480
- Item-level token-support rows: 3,244,887
- Item-level edge-support rows: 34,622,652

## Measured findings

- Positive populations ranged from 4,186 to 10,020 tokens (median 7,740).
- Negative populations ranged from 1,237 to 9,563 tokens (median 7,752).
- The smallest within-probe membership Jaccard was 0.289351 for P3_ABC vs P3_CAB, State 13, negative_tail.
- The smallest within-probe edge Jaccard was 0.104801 for P3_ABC vs P3_CAB, State 10, positive_head.
- The largest adjacent-state membership reorganisation (Jaccard 0.012365) occurred for P1_CAB negative_tail, State 00 → 01.
- P1 final positive 6/6 core: 4,871 tokens and 15,864 edges.
- P1 final negative 6/6 core: 4,789 tokens and 15,888 edges.
- P2 final positive 6/6 core: 4,648 tokens and 16,022 edges.
- P2 final negative 6/6 core: 4,721 tokens and 16,677 edges.
- P3 final positive 6/6 core: 4,535 tokens and 14,161 edges.
- P3 final negative 6/6 core: 4,333 tokens and 13,365 edges.
- P4 final positive 6/6 core: 3,497 tokens and 8,228 edges.
- P4 final negative 6/6 core: 3,469 tokens and 8,622 edges.
- Community counts ranged from 7 to 16 per network.
- State 00 topology was identical across all prompts; subsequent differences arise only after contextual processing.

These are measured structural results. Every probe must be semantically reconstructed independently before cross-probe parent or relation matching. Whether a local semantic map is supported is a downstream analytical question.