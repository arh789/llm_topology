# R011 runtime readiness decision

## Outcome

**FAILED — no available quantised CPU runtime satisfied the intermediate-state
capture requirement.**

R011 stopped before loading a model or executing either prompt. No semantic,
trajectory, cutoff, network or community output was produced.

## Required capability

The runtime had to satisfy both conditions:

1. keep a 70B–72B-class model quantised in system RAM; and
2. expose the final-position representation after every transformer block.

## Installed GGUF runtime

The installed `llama-cpp-python 0.3.34` API was inspected without loading the
cached Qwen2.5-7B model.

Observed public access was limited to:

- final embeddings;
- token-position or sequence embeddings;
- logits/evaluation state; and
- serialised runtime state.

No explicit per-layer hidden-state interface was exposed. The complete API
inventory is persisted in `runtime_probe.json`.

**Decision:** the installed GGUF runtime is unsuitable for R011 without a
modified llama.cpp build or another instrumentation mechanism.

## TorchAO fallback

The fallback was tested in isolated temporary package directories. The existing
project and WSL environments were not modified.

### TorchAO 0.18

- Imported with PyTorch `2.13.0` and Transformers `5.14.1`.
- The default int4 weight-only path required unavailable `mslk >= 1.0.0`.
- The CPU-specific dynamic-int8-activation/int4-weight path reported that the
  `torchao::da8w4_linear_cpu` kernel was not built into the available wheel.

### TorchAO 0.17

- The documented `Int4CPULayout` interface was not present in the installed
  package.
- The persisted final probe therefore failed before model loading.
- The exact failure is recorded in `torchao_probe.json`.

**Decision:** the available TorchAO packages do not provide a usable x86 CPU
int4 path on this system for the required Transformers capture.

## Failure boundary

The following components were deliberately not executed after the runtime
requirement failed:

- same-architecture baseline capture;
- same-architecture variation capture;
- paired capture validation;
- large-model download;
- 70B–72B model loading;
- vocabulary scoring;
- graph or community analysis; and
- semantic interpretation.

No stale R001–R010 artifacts were reused as R011 results.

## Strongest supported conclusion

The machine's RAM capacity remains potentially sufficient for a 70B–72B Q4
single-pass experiment. The current blocker is software instrumentation, not
the measured memory capacity.

R011 must not be reused. A later run may test one newly authorised route, such
as a purpose-built llama.cpp layer-export patch or another CPU quantisation
backend that demonstrably retains Transformers-style hidden-state access.
