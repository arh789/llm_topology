# R020 validation amendment

Recorded: `2026-11-18T16:33:48+11:00`

## Status of production attempt 1

Production attempt 1 completed the measurement pipeline, but its verifier
incorrectly reported `PASS` without enforcing the methodology's
full-sequence reconciliation gate. The audit immediately following execution
found that the frozen elementwise tolerance was exceeded. The attempt is
therefore classified as **failed validation calibration** and must not be used
for semantic analysis.

No generated continuation or semantic-network content was inspected when the
problem was found. The diagnosis used only numerical validation fields.

## Preserved attempt-1 identifiers

- Manifest SHA-256:
  `a562a35ea2273d8fc4d0bc2f8124a88db464e5504cf4fed54b02d8db6a8c66b5`
- Artifact-index SHA-256:
  `9b03714e6499322a743a94052659321dde6c353a13970e7089f316cf76032534`
- Capture-validation SHA-256:
  `878fcede4b94f839f722cb6d608bfff19e9c38a54159b3eca50de35d4c31e8cb`
- Full-sequence-reconciliation SHA-256:
  `57c7b6fe20feff3fba1e1efc13b657b0548bac4bb153867f7afef8369908bf0d`

## Failure and cause

- Same-shape deterministic replay was exact for generated token IDs, hidden
  states and logits.
- `68/256` prefix/full-sequence hidden-state comparisons exceeded the
  elementwise `atol=1e-5, rtol=1e-5` gate.
- Those forwards use different causal sequence lengths. Deterministic CUDA
  kernels can use different matrix shapes and accumulate small FP32 numerical
  differences without introducing sampling or run-to-run instability.
- The minimum vector cosine was `0.9999999662655082`.
- Projecting both representations into the exact input-embedding basis kept
  every positive and negative top-50 token set identical.

## Correction

The runner must now fail closed unless exact same-shape replay, directional
full-sequence reconciliation and exact projected top-token-set reconciliation
all pass. The original elementwise comparison remains visible as a diagnostic.
The clean rerun begins only after that gate is implemented and tested.
