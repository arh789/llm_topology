# TSTP engineering validation

- Date: `2026-11-22`
- Scope: engineering validation only; no new research run or semantic analysis
- Hardware: local RTX 4090
- Model storage: canonical shared store under `D:\AI`

## Pythia regression

The `pythia` adapter loaded the immutable R020 Pythia 70M snapshot and repeated
the complete 32-token greedy capture. The new TSTP capture matched the frozen
R020 local evidence exactly for:

- generated token IDs;
- decision hidden states;
- decision logits;
- full-sequence hidden states;
- post-generation logits.

This establishes that moving architecture access behind the adapter did not
change the R020 capture.

## Qwen architecture validation

The `qwen2` adapter loaded the cached immutable
`Qwen/Qwen2.5-0.5B-Instruct` snapshot in native BF16 with eager attention.
The capture exposed 26 states:

```text
1 input embedding
+ 24 raw transformer-block outputs
+ 1 final-normalised state
= 26 recorded states
```

Raw intermediate states and final normalisation reconciled with the standard
Transformers hidden-state return. All captured states and logits were finite.

## Qwen end-to-end validation

A one-decision engineering fixture then passed through the shared R020-derived
measurement path:

```text
capture
→ deterministic replay
→ vocabulary projection
→ full-curve cutoffs
→ 52 state/sector networks
→ communities
→ within-state transitions
→ shuffled-label control
→ compact JSON and Markdown exports
```

Coverage was exactly:

```text
1 generated-token decision × 26 states × 2 sectors = 52 networks
```

The temporary validation outputs were not retained as research evidence.

## Defects exposed during validation

The first end-to-end attempt showed that the inherited R020 exporter assumed
at least two generation decisions when sorting across-token transitions. TSTP
permits one-token validation, so the exporter was corrected to emit a valid
empty transition table with headers.

The second attempt completed the networks but exposed a missing shuffled-control
seed in the synthetic test fixture. The fixture was corrected; no production
pipeline behaviour changed for that issue.

The final end-to-end attempt passed.

## Result

TSTP has two independently validated architecture adapters and one common
measured-output contract. This establishes model interchangeability for the
supported Pythia and Qwen2 architectures; it does not imply universal
Transformers compatibility.
