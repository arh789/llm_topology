# R019 plan — OLMo 3 order-versus-repeatability control

## Objective

Determine whether the order-conditioned differences measured in R018 are
larger than any variation produced by repeating an identical prompt through
the same local model/runtime.

R019 is a reproducibility control. It does not introduce a new semantic
region and does not perform semantic reconstruction.

## Locked concepts and balanced permutations

```text
A = choke point
B = collapsible barrier
C = spear
```

Use the three cyclic permutations so that every concept occupies every input
position exactly once:

```text
ABC = choke point | collapsible barrier | spear
BCA = collapsible barrier | spear | choke point
CAB = spear | choke point | collapsible barrier
```

Each prompt ends with the same newline anchor and is captured in three
sequential forward passes. There is no response generation and no token
sampling.

## Locked model and runtime contract

- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Precision: native BF16; no quantisation
- Transformer layers: 64
- Recorded states: 65
- Hidden width: 5,120
- Chat template: none
- Special tokens: none added
- Capture position: final newline token
- Repetitions: three sequential forward passes of the same three-prompt batch
- Response generation: none
- Sampling: none
- Placement caps: CUDA 18 GiB, CPU 28 GiB, remaining modules disk-backed

The model is placed in evaluation mode. Random seeds are fixed for runtime
bookkeeping and Louvain community detection, but the forward pass itself does
not contain a sampler.

## Measurement levels

For nine observations (`3 permutations × 3 repeats`), compare all 36
observation pairs and classify each pair as:

```text
within_prompt_repeat
    same ordered prompt, different forward pass

between_order
    different cyclic permutation
```

At every recorded state measure:

1. hidden-state cosine similarity, L2 distance, maximum absolute difference
   and exact equality;
2. full-vocabulary cosine-score similarity, RMSE, maximum absolute difference
   and exact equality;
3. positive-head and negative-tail cutoff membership Jaccard;
4. exact 10-NN edge Jaccard; and
5. Louvain community adjusted Rand index using the locked seed.

At the final prompt position also compare the actual next-token distributions:

- logit cosine, L2 and maximum absolute difference;
- exact logit equality;
- Jensen-Shannon divergence of the softmax distributions; and
- top-100 token-set Jaccard.

The central comparison is:

```text
between-order divergence
────────────────────────
within-repeat divergence + epsilon
```

When repeat divergence is exactly zero, report that the observed order effect
lies above a zero measured noise floor rather than manufacturing an arbitrary
finite ratio.

## Expected coverage

```text
3 permutations × 3 repeats
= 9 observations

9 observations × 65 states × 2 sectors
= 1,170 networks

C(9, 2) × 65 states
= 2,340 hidden-state comparison rows

C(9, 2) × 65 states × 2 sectors
= 4,680 topology comparison rows

within-prompt repeat pairs:
3 permutations × C(3, 2) = 9 pairs

between-order pairs:
C(9, 2) - 9 = 27 pairs
```

## Interpretation rules

The run distinguishes three sources of variation:

```text
raw hidden states differ within repeats
    → model/runtime numerical nondeterminism

hidden states stable but cutoff memberships differ
    → projection or threshold sensitivity

memberships stable but edges/communities differ
    → graph or community-algorithm sensitivity
```

If identical repeats remain exact while permutations diverge after State 00,
R018's order effects are validated as deterministic contextual effects.

If within-repeat divergence is comparable to between-order divergence, the
R018 interpretation must be qualified.

## Success criteria

R019 succeeds as an experiment if:

- all three prompts are captured in three sequential passes;
- all captures and final logits are finite;
- every expected pairwise and network row is present exactly once;
- raw repeat and order comparisons are kept separate;
- graph construction uses the unchanged R018 measurement constants;
- actual next-token distributions are compared without sampling;
- every artifact is indexed and hashed; and
- the report states the observed result whether it confirms or challenges
  deterministic order sensitivity.

An observation of non-zero repeat variation is a valid scientific result.
Missing or internally inconsistent evidence is a failed run.

## Outside scope

- semantic parent reconstruction;
- a new topic or concept set;
- all six permutations;
- response generation or sampled-token comparison;
- cross-model comparison;
- SDA-3, GRD, coherence or curvature interpretation; and
- changing the R018 cutoff, graph or community method.
