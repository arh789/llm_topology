# R012 pre-run plan: Qwen whole-prompt paired capture

## Run identity

- Run number: `R012`
- Neutral run name: `qwen-whole-prompt-paired-capture`
- Run type: measured paired-prompt hidden-state capture
- Initial status: `running`
- Runtime: Hugging Face Transformers with CUDA
- Smoke-test model: `Qwen/Qwen2.5-0.5B-Instruct`, BF16
- Primary model: `Qwen/Qwen2.5-7B-Instruct`, BF16

R012 corrects the runtime choice that caused R011 to fail. R011 remains an
immutable failed feasibility record. R012 uses the original Transformers model
format because the experiment requires the hidden state returned at every
transformer depth.

## Objective

Validate a minimal, reproducible method for measuring how a controlled prompt
change alters the final model-input representation across transformer depth.
The smoke test establishes the capture mechanism. The 7B run is the first
research-quality capture.

## Controlled prompt pair

Baseline:

```text
What structure forms from electro pink, curvature density, Tokyo nightlife?
```

Variation:

```text
What structure forms from electro pink, Tokyo nightlife, curvature density?
```

The only intended change is the order of `curvature density` and
`Tokyo nightlife`.

## Measurement contract

- Use the tokenizer's official chat template with `add_generation_prompt=True`.
- Do not generate a response token.
- Capture the final model-input position, which has causal access to the full
  templated prefix.
- Request `output_hidden_states=True` and `use_cache=False`.
- Retain one vector per exposed state, not every prompt-token vector.
- Transformers exposes the input embedding followed by block outputs, with the
  last state including the architecture's final normalisation.
- Save the exact templated text, token IDs, decoded tokens, capture position,
  model revision, dtype, shape, timings and GPU-memory observations.
- Re-run each forward pass and require deterministic equality.
- Require matching state shapes, identical State 00 vectors and at least one
  differing later state across the paired prompts.

## Required components

1. `plan_lock`
2. `environment_probe`
3. `smoke_0_5b_capture`
4. `smoke_0_5b_validation`
5. `primary_7b_capture`
6. `primary_7b_validation`
7. `run_report`

The run is successful only if all seven components succeed. Any failed capture
or validation marks the run failed and prevents later stages from using its
data.

## Execution order

1. Persist this plan and a `running` manifest.
2. Validate the existing CUDA Transformers environment and shared model cache.
3. Download and run Qwen2.5-0.5B-Instruct from `D:\AI\cache`.
4. Validate both prompt captures and deterministic replay.
5. Only after smoke success, download and run Qwen2.5-7B-Instruct in BF16.
6. Validate the paired 7B trajectories and persist a factual run report.
7. Stop before vocabulary scoring, networks, semantic interpretation or larger
   models.

## Success criteria

- No model weights are stored in the repository.
- Both models use the same fixed prompt pair and capture rule.
- Every expected state is present, finite and the correct hidden width.
- Deterministic replay is exact for both prompts.
- State 00 is identical across the prompt pair.
- At least one later state differs.
- All curated artifacts have recorded byte counts and SHA-256 hashes.
- The manifest is completed as `successful` only after both model stages pass.

## Outside scope

- response generation;
- vocabulary scoring, cutoffs, networks or community detection;
- semantic interpretation of prompt differences;
- quantisation comparisons;
- Qwen2.5-14B, 32B or 72B;
- modification of R011;
- committing or pushing Git changes.

## Failure conditions

- CUDA or required packages are unavailable;
- the official chat template cannot be applied;
- hidden states are missing, non-finite or have unexpected dimensions;
- capture anchors differ across prompts;
- deterministic replay differs;
- State 00 differs across prompts;
- no later state differs; or
- the smoke stage fails and the 7B stage is nevertheless attempted.
