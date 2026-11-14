# R015 concept-selection evidence

## Purpose

Establish whether `sensor`, `apartment`, `line` and `sessions` are defensible
neighbouring replacements for the four R014 seeds before R015 is implemented.
This document locks the prompt concepts; it does not predetermine the semantic
parents that R015 must reconstruct independently.

## Reproducible measured-evidence scan

R014 `nodes.csv.gz` was scanned as a stream. `decoded_token` was stripped and
case-normalised, then matched exactly against the four proposed strings. The
scan retained prompt, probe, permutation, state, side, token ID and local
community identity. It covered all 10,447,003 selected R014 token memberships.

| Concept | Rows | R014 prompts | Probes | Local permutations | Distinct states | State range | Positive rows | Negative rows | Community instances |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|
| sensor | 521 | 24/24 | 4/4 | 6/6 | 23 | 05–28 | 518 | 3 | 486 |
| apartment | 524 | 24/24 | 4/4 | 6/6 | 26 | 02–27 | 524 | 0 | 416 |
| line | 395 | 24/24 | 4/4 | 6/6 | 26 | 01–28 | 194 | 201 | 314 |
| sessions | 432 | 24/24 | 4/4 | 6/6 | 26 | 01–28 | 0 | 432 | 376 |

Coverage within each R014 probe is also complete at the prompt level:

| Concept | P1 rows | P2 rows | P3 rows | P4 rows | Prompts per probe |
|---|---:|---:|---:|---:|---:|
| sensor | 130 | 133 | 130 | 128 | 6/6 each |
| apartment | 126 | 179 | 99 | 120 | 6/6 each |
| line | 113 | 75 | 107 | 100 | 6/6 each |
| sessions | 101 | 103 | 116 | 112 | 6/6 each |

The multiple measured token IDs associated with some normalised strings arise
from vocabulary surface variants that collapse after stripping and decoding.
R015 prompts use the exact lowercase strings and the locked tokenizer outputs
recorded below.

## Independent R014 reconstruction evidence

`R014_PROBE_RECONSTRUCTIONS.md` identifies the proposed concepts inside the
corresponding probe-local structures before R015 was proposed:

- `sensor` and `sensors` recur with laser, electrodes, signals and technical
  apparatus in the dominant positive technical/sensing lineage.
- `apartment` recurs with city, kitchen, shops, named places and built or
  situated environments.
- `line` recurs with field, area, space, parameters, weighting and measurement
  or structural vocabulary, spanning both cosine sectors.
- `sessions` recurs with clubs, groups, activities, teams, exhibitions and
  sport in the persistent negative social/group-activity lineage.

This downstream semantic record is selection evidence only. R015 must not use
these labels when first reconstructing its own communities.

## Locked prompt tokenisation

The pinned R014 tokenizer was loaded from the shared cache only:

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- Tokenizer class: `Qwen2Tokenizer`

With special tokens disabled:

| Exact string | Token IDs | Token pieces |
|---|---|---|
| sensor | `29511` | `sensor` |
| apartment | `391 3195` | `ap`, `artment` |
| line | `1056` | `line` |
| sessions | `50964` | `sessions` |
| newline anchor | `198` | `Ċ` |

Token-count differences are admissible because the fixed capture position is
the final newline anchor, not any seed token.

## Selection decision

The R014 evidence does not contradict the proposed concept set. All four
concepts recur across every R014 probe, every local permutation and substantial
transformer depth, and each appears in the independently reconstructed family
it is intended to sample.

The set is therefore frozen as:

```text
A = sensor
B = apartment
C = line
D = sessions
```

## Remaining uncertainty

Measured recurrence does not prove functional equivalence with the R014 seed
it replaces. `line` is particularly polysemous and spans both sectors, while
`apartment` is a two-token prompt concept. These are observations to test, not
reasons to change the set. R015 must determine whether the resulting topology
persists, deforms, splits, merges or terminates.
