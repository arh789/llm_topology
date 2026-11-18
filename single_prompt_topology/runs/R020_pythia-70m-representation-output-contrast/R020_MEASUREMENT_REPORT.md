# R020 semantic-topology measurement report

## Outcome

The deterministic Pythia 70M capture, replay, vocabulary projection, topology construction and shuffled-label control completed and validated.

**Overall run status: awaiting semantic analysis.** The continuation has not been evaluated here, and no semantic topics or parents have been assigned.

## Run identity

- Model: `EleutherAI/pythia-70m`
- Revision: `a39f36b100fe8a5377810d56c3f4789b9c53ac42`
- Prompt hash: `5790fa42733d1fd7e991983f27eba90b250e5949b99597f9ef0fc7305fef1e1b`
- Prompt tokens: 16
- Generated-token decisions: 32
- Stop reason: `max_new_tokens`
- Recorded states per decision: 8
- Generation: deterministic greedy argmax
- Generated continuation: deliberately not reproduced in this semantic-free report

## Coverage

- Networks: 512
- Selected token memberships: 1,419,650
- Directed exact 10-NN edges: 14,196,500
- State-local communities: 6,944
- Within-decision state transitions: 448
- Across-decision generation transitions: 496
- Directional full-sequence reconciliation: True
- Projected top-token-set reconciliation: True
- Elementwise full-sequence diagnostic (retained, not concealed): False

## Interpretation boundary

These outputs measure changing vocabulary neighbourhoods, graph partitions and transitions through depth and autoregressive time. They do not yet identify topics, determine whether the visible answer is useful, or establish that an internal structure caused a generated token.
