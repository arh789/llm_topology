# R008 findings: ChatGPT-readable split networks

## Direct observations

- All 66 planned primary networks were produced: one positive-head and one negative-tail network at each of 33 states.
- The complete export contains 191,872 node-state rows and 1,918,720 directed within-side 10-nearest-neighbour edges.
- The secondary R005 bridge table contains 604,515 directed cross-side relations retained by the earlier combined graphs.
- positive_head population size ranged from 1,871 to 3,491; community count ranged from 9 to 14; modularity ranged from 0.4987 to 0.5890.
- positive_head median adjacent-state membership Jaccard was 0.7537, median edge Jaccard was 0.5344, and median community adjusted Rand index was 0.3749.
- negative_tail population size ranged from 1,316 to 3,313; community count ranged from 10 to 15; modularity ranged from 0.4686 to 0.5418.
- negative_tail median adjacent-state membership Jaccard was 0.7582, median edge Jaccard was 0.5371, and median community adjusted Rand index was 0.3986.

## Supported conclusion

The R004 positive and negative populations can now be reconstructed and inspected as separate static-embedding relationship networks at every recorded state. Compact community-level exports make those networks accessible for external semantic interpretation while the complete tables preserve the measured evidence.

## Limitations

- The static vocabulary geometry is fixed. Layer-wise changes come from changing target-relative membership, not contextual movement of every selected vocabulary token.
- Community representatives can expose lexical, morphological and tokenizer structure; they are not automatic topic labels.
- Cross-side relations are only those retained by R005's combined 10-nearest-neighbour graphs and are not an exhaustive bipartite graph.
- Positive alignment does not establish semantic centrality, and negative anti-alignment does not establish suppression or exclusion.
- R008 does not test coherence, semantic conflict or curvature density.
