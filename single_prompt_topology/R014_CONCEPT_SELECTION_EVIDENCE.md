# R014 concept-selection evidence

## Purpose

Record why the four R014 concepts are admissible samples of the R013 measured
semantic region without treating downstream R013 parent labels as predetermined
R014 results.

## Reproducible evidence scan

The R013 `nodes.csv.gz` table was scanned for rows whose stripped,
case-normalised `decoded_token` matched `laser`, `city`, `field`, `area` or
`clubs`. The scan retained prompt permutation, state, side, token ID and local
community identity.

| Lexeme | Rows | R013 permutations | Distinct states | State range | Positive rows | Negative rows | Community instances |
|---|---:|---:|---:|---|---:|---:|---:|
| laser | 171 | 6/6 | 26 | 01–27 | 171 | 0 | 144 |
| city | 122 | 6/6 | 26 | 01–27 | 3 | 119 | 85 |
| field | 97 | 6/6 | 23 | 01–28 | 12 | 85 | 88 |
| area | 329 | 6/6 | 27 | 01–27 | 0 | 329 | 167 |
| clubs | 88 | 6/6 | 20 | 05–28 | 0 | 88 | 73 |

The direct evidence therefore covers every R013 permutation and substantial
transformer depth. `spatial field` is intentionally represented by the
recurrent `field` and `area` structural vocabulary rather than by claiming the
exact phrase occurred as one measured token.

## Prompt tokenisation control

Using the locked Qwen tokenizer and revision, with no special tokens:

| Concept | Token IDs | Token pieces |
|---|---|---|
| laser | `75 12080` | `l`, `aser` |
| city | `8926` | `city` |
| spatial field | `2154 22433 2070` | `sp`, `atial`, ` field` |
| clubs | `76285` | `clubs` |

All prompts will use the exact lowercase strings above. Token-count differences
are admissible because the fixed capture position is the final newline anchor.

## Selection rationale

- `laser` samples recurrent positive sensory/material/technical evidence.
- `city` samples recurrent place/environment evidence, predominantly negative
  under the R013 anchor-relative cosine measurement.
- `spatial field` samples the recurrent structural vocabulary expressed by
  `field` and `area`, spanning both sectors.
- `clubs` samples recurrent social/activity evidence in the negative sector.

These descriptions justify the sampling design only. R014 semantic analysis
must reconstruct each probe independently and must not assign these labels to
its communities in advance.

## Balanced coverage

Every concept appears in three probes and every pair appears under two third-
concept contexts. This creates the smallest balanced design that distinguishes
order invariance from context invariance.
