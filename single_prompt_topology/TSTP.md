# Transformer State Topology Pipeline (TSTP)

TSTP is the model-interchangeable form of the complete autoregressive
measurement workflow validated by R020. It captures the internal state that
produces every generated token, projects those states into the model's fixed
input-embedding vocabulary, constructs positive and negative topology, and
stops before semantic interpretation.

## Boundary

```text
MODEL CONFIGURATION
        ↓
ARCHITECTURE ADAPTER
        ↓
STANDARD STATE CAPTURE
        ↓
VOCABULARY PROJECTION
        ↓
CUTOFF POPULATIONS
        ↓
NETWORKS AND COMMUNITIES
        ↓
MEASURED EXPORTS
        ↓
STOP BEFORE SEMANTIC INTERPRETATION
```

The first supported adapters are:

| Adapter | Architecture | Validated model |
|---|---|---|
| `pythia` | `GPTNeoXForCausalLM` | `EleutherAI/pythia-70m` |
| `qwen2` | `Qwen2ForCausalLM` | `Qwen/Qwen2.5-0.5B-Instruct` |

An adapter exposes only:

- transformer blocks in forward order;
- final normalisation;
- architecture identity;
- standard input and output embeddings supplied by Transformers.

Everything after capture is shared.

## Captured state contract

For every greedy next-token decision, TSTP records:

```text
S00  input embedding
S01  raw block 0 output
S02  raw block 1 output
...
SNN  raw final-block output
SNN+1 final-normalised state used by the language-model head
```

The common decision tensor has shape:

```text
[generated-token decision, recorded state, hidden dimension]
```

Forward hooks expose raw block outputs. The adapter reapplies final
normalisation and requires it to reconcile with the model's returned final
hidden state. Missing blocks, an incorrect final norm or an incompatible
architecture fails before topology is constructed.

## Configuration

TSTP uses the R020 configuration shape with an explicit adapter:

```json
{
  "schema_version": 1,
  "run_number": 21,
  "run_id": "R021_example-tstp-run",
  "run_directory": "single_prompt_topology/runs/R021_example-tstp-run",
  "initial_files": ["run_config.json", "R021_RUN_METHODOLOGY.md"],
  "model": {
    "id": "Qwen/Qwen2.5-0.5B-Instruct",
    "revision": "<immutable revision>",
    "snapshot_path": "D:/AI/cache/huggingface/hub/<snapshot>",
    "adapter": "qwen2",
    "architecture": "Qwen2ForCausalLM",
    "dtype": "bfloat16",
    "quantized": false,
    "expected_layer_count": 24,
    "expected_hidden_width": 896,
    "expected_embedding_rows": 151936,
    "device": "cuda:0",
    "attn_implementation": "eager"
  }
}
```

Model, prompt, generation, capture and topology fields remain frozen in the
run configuration. Model weights remain under `D:\AI`; they never enter this
repository.

## CLI

From `single_prompt_topology`:

```powershell
& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' tstp_engine.py validate-config `
  --config runs\<run_id>\run_config.json

& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' tstp_engine.py preflight `
  --config runs\<run_id>\run_config.json

& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' tstp_engine.py measure `
  --config runs\<run_id>\run_config.json

& 'C:\Users\arhal\anaconda3\envs\myenv\python.exe' tstp_engine.py verify `
  --config runs\<run_id>\run_config.json
```

`preflight` performs one generated-token decision and writes no scientific
evidence. `measure` refuses to overwrite an existing manifest or undeclared
run-directory content.

## Outputs

Every adapter produces the same evidence classes:

- configuration, manifest, model metadata and prompt record;
- local raw decision states, logits and full-sequence tensors;
- deterministic replay and reconciliation metrics;
- vocabulary scores, cutoffs and extreme-token tables;
- network index, community nodes and intercommunity edges;
- within-layer and across-generation transitions;
- shuffled-label control;
- ChatGPT-readable measured JSON and Markdown packets;
- completeness reports and artifact index.

TSTP does not assign semantic community labels, reconstruct parent structures,
apply SDA-3/GRD roles or create a derived human-facing semantic graph.

## Adding another architecture

Add one adapter in `tstp/adapters.py` that declares the supported model class
and exposes `blocks(model)` and `final_norm(model)`. A new adapter is not
supported until it passes:

1. adapter contract tests;
2. raw-block and final-normalisation reconciliation;
3. deterministic replay;
4. an end-to-end measured-export validation.

Do not add architecture conditionals to `tstp_engine.py`, `tstp/capture.py` or
the topology calculations.
