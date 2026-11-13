# R011 pre-run plan: whole-prompt semantic perturbation feasibility

## Run identity

- Run number: `R011`
- Neutral run name: `whole-prompt-semantic-perturbation-feasibility`
- Run type: measured paired-prompt capture feasibility
- Status at plan lock: `running`
- Ultimate target model class: CPU/RAM-resident 70B–72B quantised causal model
- Primary target candidate: `Qwen/Qwen2.5-72B-Instruct`, `Q4_K_M`
- Same-architecture probe: cached `Qwen2.5-7B-Instruct-Q5_K_M.gguf`

R011 is not a continuation of the lithium interpretation. It tests whether the
existing topology method can be generalised from one final concept token to a
fixed whole-prompt decision position and used to compare two prompts that
differ in exactly one controlled way.

## Stated objective

Create the next measured run and proceed with the smallest decisive technical
test before downloading a 70B–72B model.

## Inferred objective

Establish a reusable pipeline that can:

1. process a complete prompt containing multiple concepts;
2. capture the fixed final model-input position at every transformer state;
3. preserve only the required final-position trajectory;
4. compare a baseline with a minimally perturbed prompt; and
5. pass successful captures into the existing vocabulary, cutoff, network and
   community analysis stages.

## Controlled prompt pair

The first pair changes concept order only.

### Baseline

```text
What structure forms from electro pink, curvature density, Tokyo nightlife?
```

### Variation

```text
What structure forms from electro pink, Tokyo nightlife, curvature density?
```

The model's official chat template must be used. The measured position is the
final assistant-prefix/model-input position immediately before autoregressive
generation. No response token is sampled or generated.

## Representation contract

- The complete templated prompt is the model input.
- State 00 is the fixed final-position input embedding and is expected to be
  identical across the paired prompts when their assistant prefix is identical.
- Subsequent states are the final-position representation after each
  transformer block.
- Final normalisation is recorded separately when the architecture exposes it.
- Only the final-position vector is retained per state.
- Prompt-wide influence is inferred from causal access to the complete prefix;
  the pipeline does not claim that the vector is a pure semantic intersection.
- Input embeddings provide the fixed vocabulary basis used by the established
  cosine-scoring stages.

## Required components

1. `plan_lock`
2. `runtime_capability_probe`
3. `same_architecture_baseline_capture`
4. `same_architecture_variation_capture`
5. `paired_capture_validation`
6. `large_model_readiness_decision`

The run remains `running` until every required component succeeds. A runtime
capability probe succeeds when it establishes, with persisted evidence, whether
the runtime can expose intermediate states. Finding that a runtime is
unsupported is a valid probe result but does not satisfy either capture
component.

## Success criteria

- The quantised model remains quantised in memory.
- Every expected state is captured for both prompts.
- Each state contains exactly one finite vector of the model hidden width.
- The two captures use the same model revision, quantisation, tokenizer, chat
  template, assistant prefix and capture rule.
- State 00 matches across prompts.
- At least one later state differs; no particular magnitude is required.
- The embedding basis can be retained or exported without retaining the full
  model.
- The persisted manifest records timings, memory observations, component
  results, hashes and any fallback used.

## Outside scope

- response generation or response-quality evaluation;
- interactive inference optimisation;
- capturing every prompt-token state;
- simultaneous multi-model comparison;
- more than one controlled perturbation;
- R009/R010-style semantic interpretation before paired capture validation;
- Phase D conflict-resolution analysis;
- proving SDA-3 or GRD from this run alone;
- a general runtime abstraction layer or user interface.

## Failure conditions

R011 must not be marked successful if:

- the runtime exposes only the final embedding or logits;
- quantised weights are expanded beyond available RAM;
- any expected layer state is missing or non-finite;
- the paired prompts use different capture anchors or templates;
- stale artifacts are used after a failed capture;
- only token lists are produced without a validated trajectory; or
- measured and interpretive evidence are not kept separate.

## Execution order

1. Inspect the existing quantised runtime API without loading a large model.
2. Use the cached Qwen2.5-7B GGUF for any required same-architecture runtime
   test.
3. If the installed runtime cannot expose intermediate states, record that
   result and test one minimal quantised CPU runtime that preserves PyTorch-like
   layer access.
4. Complete and validate both prompt captures on the probe architecture.
5. Re-measure available RAM with nonessential applications closed.
6. Select 72B Q4 when the instrumented runtime and memory margin support it;
   otherwise select the 32B fallback.
7. Only then download or pin new model weights.

## Planned run artifacts

The local run directory is:

```text
runs/R011_whole-prompt-semantic-perturbation-feasibility/
```

It must contain at minimum:

- `manifest.json`
- `runtime_probe.json`
- exact templated prompt/token records for both inputs
- one final-position trajectory per prompt
- capture validation results
- the large-model readiness decision

Generated measurement artifacts remain ignored by default until deliberately
selected as curated project evidence.
