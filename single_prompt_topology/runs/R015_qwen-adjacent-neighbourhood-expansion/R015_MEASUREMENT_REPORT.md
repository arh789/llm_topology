# R015 overlapping-context topology measurement report

## Outcome

R015 completed the controlled four-probe, 24-prompt measurement pipeline. Every overlapping concept triplet was measured in six orders at the same final newline anchor. The trajectories were projected into the fixed input-embedding vocabulary, divided by the locked full-curve elbows, converted into 1,392 exact split networks, partitioned into state-local communities and compared within each probe across depth and order.

No chat template, assistant prefix or response generation was used. No semantic topic labels, parent nodes, cross-probe map nodes/edges, SDA roles, GRD roles, coherence claims or semantic-curvature claims were inferred.

## Coverage

- Probes: 4
- Prompts: 24
- Networks: 1392
- Selected token memberships: 10,648,837
- Directed 10-NN edges: 106,488,370
- State-local communities: 14,796
- Within-prompt adjacent-state comparisons: 1344
- Within-probe same-state permutation comparisons: 3480
- Item-level token-support rows: 3,500,996
- Item-level edge-support rows: 37,561,354

## Measured findings

- Positive populations ranged from 4,186 to 9,881 tokens (median 7,868).
- Negative populations ranged from 1,237 to 9,955 tokens (median 7,924).
- The smallest within-probe membership Jaccard was 0.170059 for P3_ACB vs P3_BAC, State 12, negative_tail.
- The smallest within-probe edge Jaccard was 0.044076 for P3_ACB vs P3_BCA, State 09, positive_head.
- The largest adjacent-state membership reorganisation (Jaccard 0.012776) occurred for P1_BAC negative_tail, State 00 → 01.
- P1 final positive 6/6 core: 3,776 tokens and 10,240 edges.
- P1 final negative 6/6 core: 3,898 tokens and 10,681 edges.
- P2 final positive 6/6 core: 4,638 tokens and 15,190 edges.
- P2 final negative 6/6 core: 4,637 tokens and 16,002 edges.
- P3 final positive 6/6 core: 3,188 tokens and 6,776 edges.
- P3 final negative 6/6 core: 3,073 tokens and 6,747 edges.
- P4 final positive 6/6 core: 4,419 tokens and 13,610 edges.
- P4 final negative 6/6 core: 4,442 tokens and 14,008 edges.
- Community counts ranged from 7 to 16 per network.
- State 00 topology was identical across all prompts; subsequent differences arise only after contextual processing.

These are measured structural results. Every probe must be semantically reconstructed independently before cross-probe parent or relation matching. Whether a local semantic map is supported is a downstream analytical question.