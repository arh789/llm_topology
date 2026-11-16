# R018 permutation-topology measurement report

## Outcome

R018 completed the six-permutation OLMo 3 32B measurement pipeline. The report contains measured structural evidence only; semantic parent reconstruction remains outside the run.

## Run identity

- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Prompts: 6
- Recorded states per prompt: 65
- Capture position: final newline token
- Response generation: not executed
- Deterministic replay: exact

## Coverage

- Networks: 780
- Selected token memberships: 3,081,305
- Directed 10-NN edges: 30,813,050
- State-local communities: 11,872
- Adjacent-state comparisons: 768
- Same-state permutation comparisons: 1950

## Measured comparison summary

- Minimum cross-permutation membership Jaccard: 0.154572
- Minimum cross-permutation edge Jaccard: 0.040741
- Mean membership Jaccard for pairs sharing the final concept: 0.523249
- Mean membership Jaccard for pairs with different final concepts: 0.364111

These measurements test order and final-position association. They do not identify semantic parents or establish what the measured differences mean.

## Interpretation boundary

The measured outputs end at tokens, scores, networks, state-local communities, transitions and permutation comparisons. Any parent structures, relations or semantic maps must be reconstructed independently downstream.
