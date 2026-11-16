# R018 plan — OLMo 3 choke-point / barrier / spear permutation topology

## Objective

Measure how input order changes the layerwise topology formed by the three
bare concepts used in R017:

```text
A = choke point
B = collapsible barrier
C = spear
```

Run all six permutations with one final newline anchor:

```text
ABC  ACB  BAC  BCA  CAB  CBA
```

R018 is the OLMo 3 32B counterpart of the R013 permutation design. It tests
order-conditioned topology; it does not assume that R017's inferred parent
structures are correct or stable.

## Historical boundary

R016 and R017 are frozen historical evidence. R018 must not modify their
scripts, manifests, captures, networks, communities or reports.

## Locked model and capture contract

- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Precision: native BF16; no quantisation
- Transformer layers: 64
- Recorded states: 65
- Hidden width: 5,120
- Prompt form: three concepts separated by newlines plus one final newline
- Chat template: none
- Special tokens: none added
- Capture position: the final newline token for each prompt
- Response generation: none
- Primary capture: all six prompts in one padded batch
- Deterministic control: repeat the identical batch and require exact equality
- Model cache: `D:\AI\cache\huggingface\hub`
- Placement caps: CUDA 18 GiB, CPU 28 GiB, remaining modules disk-backed

## Measurement constants

The R017 scientific method remains unchanged:

1. cosine projection against the usable input-embedding vocabulary;
2. final newline token excluded from cutoff selection;
3. independent positive-head and negative-tail full-curve maximum-deviation
   elbows;
4. exact 10-nearest-neighbour graphs within each selected population;
5. symmetrisation when either directed neighbour relation exists;
6. deterministic unweighted Louvain partitioning;
7. token IDs as stable join keys;
8. community IDs local to one prompt, state and sector.

## Expected coverage

```text
6 prompts × 65 states × 2 sectors
= 780 networks

6 prompts × 64 adjacent transitions × 2 sectors
= 768 within-prompt transition rows

15 unordered prompt pairs × 65 states × 2 sectors
= 1,950 same-state permutation comparisons

65 states × 2 sectors × 2 item types × 6 support levels
= 1,560 permutation-invariance summary rows
```

## Measurement and interpretation boundary

R018 ends at validated, semantic-free evidence:

```text
hidden states
→ vocabulary scores
→ cutoffs and memberships
→ token networks
→ state-local communities
→ adjacent-state comparisons
→ same-state permutation comparisons
→ token/edge support across permutations
```

Parent identities, parent relations, semantic maps, SDA-3 roles and GRD roles
are downstream interpretations and are not required for measurement success.

## Success criteria

R018 is measurement-successful only if:

- the versioned configuration validates before model loading;
- the run directory did not exist before execution;
- all six prompt/token/anchor records are persisted;
- all 65 × 6 anchor states are finite;
- deterministic replay is exactly equal;
- every expected network, transition and pairwise comparison exists once;
- every selected node has exactly ten directed neighbours;
- every selected node belongs to exactly one local community;
- streamed rows, community totals and all references reconcile;
- every persisted measurement artifact is indexed and hashed;
- the measured report contains no semantic parent labels; and
- the manifest reaches `measurement_successful` independently of analysis.

An unstable or order-dependent topology is a valid scientific result. Missing,
contaminated or internally inconsistent evidence is a failed run.

## Outside scope

- response generation;
- changing the three concepts;
- additional contexts or overlapping probes;
- cross-model comparison;
- changing the R017 measurement method;
- semantic parent reconstruction;
- SDA-3, GRD, coherence or curvature interpretation;
- overwriting or resuming a pre-existing R018 directory.

