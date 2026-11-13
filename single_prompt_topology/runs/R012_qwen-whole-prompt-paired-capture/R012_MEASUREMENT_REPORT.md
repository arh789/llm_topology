# R012 whole-prompt semantic-topology measurement report

## Outcome

R012 completed the intended generalised measured pipeline. The validated Qwen hidden-state trajectories were projected into the fixed input-embedding vocabulary, divided by full-curve elbows, converted into 116 exact split networks, partitioned into state-local communities, compared through depth and compared across the paired prompts.

The model was not re-run and no response token was generated. No semantic topic labels, parent nodes, GRD roles or SDA-3 roles were inferred.

## Coverage

- Networks: 116
- Selected token memberships: 706,623
- Directed 10-NN edges: 7,066,230
- State-local communities: 1,181
- Adjacent-state comparisons: 112
- Same-state paired-prompt comparisons: 58

## Measured findings

- Positive populations ranged from 4,186 to 8,785 tokens (median 5,952).
- Negative populations ranged from 1,237 to 9,024 tokens (median 6,001).
- The smallest paired-prompt membership Jaccard was 0.773731 at State 28 on negative_tail.
- The smallest paired-prompt edge Jaccard was 0.558323 at State 28 on negative_tail.
- The largest adjacent membership reorganisation (lowest Jaccard 0.016019) occurred for variation negative_tail, State 00 → 01.
- Community counts ranged from 7 to 16 per network.
- State 00 was structurally identical across prompts, as required by the identical capture-position input embedding; later differences therefore arise after contextual processing.

These are measured structural results. Their semantic meaning is intentionally deferred to downstream ChatGPT analysis using the JSON, Markdown and CSV exports.

## Method boundary

The Qwen model is the first validated backend for the minimal capture contract. Vocabulary projection, cutoff calculation, networks, communities and comparisons are model-independent once trajectories, input embeddings and vocabulary are supplied.