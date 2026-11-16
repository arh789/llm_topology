# Reproducibility Guide

Status: private working guide for the article's central R018 and R019 evidence.
It documents the executed local path without claiming that every dependency
has yet been frozen into a portable public environment.

## Reproduction target

The central result to reproduce is:

```text
identical prompt + identical local forward pass
    -> exact measured repeatability

same concepts + different order
    -> different intermediate states and topology
    -> partial late reconvergence
```

No response token was generated or sampled in R018 or R019.

## Model identity

| Property | Value |
|---|---|
| Model | `allenai/Olmo-3-1125-32B` |
| Revision | `c2b61dae89a1ad10e4ad5653d0e46b590902607b` |
| Precision | native BF16 |
| Quantisation | none |
| Layers / captured states | 64 / 65 |
| Hidden width | 5,120 |
| Usable vocabulary | 100,278 |
| Embedding weight | `model.embed_tokens.weight` |
| Capture anchor | final newline token, token ID 198 |
| Chat template | not used |
| Response generation | false |

Model, tokenizer and weight-index hashes are stored in each run's
[`manifest.json`](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/manifest.json).

## Executed hardware path

- Windows local workstation.
- NVIDIA GeForce RTX 4090 with 24 GiB VRAM.
- GPU allocation cap: `18GiB`.
- CPU placement cap: `28GiB`.
- Remaining weights offloaded to `D:\AI\cache\offload\...`.
- Hugging Face models stored under `D:\AI\cache\huggingface`.

R018 recorded a peak GPU allocation of 18,699,441,664 bytes. Resource and
placement details are in its [manifest](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/manifest.json)
and [device map](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/device_map.json).

## Software snapshot

The R018 manifest directly records Python `3.11.15`, PyTorch `2.6.0+cu124`
and CUDA `12.4`. On 2026-11-17, the same `myenv` environment reported:

| Package | Version |
|---|---|
| `accelerate` | 1.14.0 |
| `networkx` | 3.6.1 |
| `numpy` | 2.4.4 |
| `pandas` | 3.0.3 |
| `psutil` | 7.0.0 |
| `safetensors` | 0.8.0 |
| `scikit-learn` | 1.8.0 |
| `torch` | 2.6.0+cu124 |
| `transformers` | 5.12.1 |

Only Python, PyTorch and CUDA are execution-time manifest evidence. The
remaining versions are a near-term environment snapshot and should be converted
into a frozen public environment file only when the final publication package
is prepared.

## Core implementation

- [`topology_core.py`](single_prompt_topology/topology_core.py) — elbow
  selection, exact k-NN construction, seeded Louvain communities and graph
  comparisons.
- [`topology_engine.py`](single_prompt_topology/topology_engine.py) —
  configuration-driven capture, projection, persistence and validation.
- [`topology_run.py`](single_prompt_topology/topology_run.py) — general CLI.
- [`r019_repeatability_control.py`](single_prompt_topology/r019_repeatability_control.py)
  — sequential-repeat capture and within/between-order comparisons.

## Validate the existing evidence

From `single_prompt_topology`:

```powershell
python topology_run.py verify `
  --config run_configs/R018_olmo3-choke-point-barrier-spear-permutations.json

python r019_repeatability_control.py verify `
  --config run_configs/R019_olmo3-order-repeatability-control.json
```

The complete local verification requires ignored raw tensors and large graph
files. A Git-only checkout can inspect and validate the committed compact
evidence and hashes, but cannot recreate omitted bytes from hashes alone.

## Run the tests

From `single_prompt_topology`:

```powershell
python -m unittest test_topology_engine -v
python -m unittest test_r017_regression -v
```

The exact network tests and frozen R017 regression require CUDA. The lifecycle
test record is preserved in
[`R018_LIFECYCLE_UPDATE_VERIFICATION.md`](single_prompt_topology/R018_LIFECYCLE_UPDATE_VERIFICATION.md).

## Execute a fresh replication

Do not delete or overwrite a curated run directory. In a separate checkout or
working copy:

1. Confirm the pinned model snapshot and cache locations.
2. Copy the relevant run configuration.
3. Change only `run_id`, `run_number`, `output_directory` and offload
   directory so the replication writes to a new path.
4. Preserve model revision, prompts, anchor, precision, measurement constants
   and random seed.
5. Validate before loading the model:

   ```powershell
   python topology_run.py validate-config --config <replication-config>
   ```

6. Execute and verify:

   ```powershell
   python topology_run.py measure --config <replication-config>
   python topology_run.py verify --config <replication-config>
   ```

For an R019-style repeatability control, substitute
`r019_repeatability_control.py` for `topology_run.py`.

## Data availability boundary

Git tracks the plans, code, configuration, manifests, hashes, compact
measurements, community summaries and reports used by the article.

The following high-volume artifacts remain local and ignored:

- hidden-state safetensors;
- full vocabulary-score safetensors;
- R019 repeat-capture tensors;
- complete token-node and exact-edge gzip tables;
- permutation-support gzip tables where applicable.

Their byte sizes and SHA-256 hashes are retained in `artifact_index.json`.
Before public release, the article package must either archive the required raw
artifacts separately or state clearly that the published package supports
audit of compact evidence but not full raw-data reanalysis.

## Reproduction boundary

Successful rerun of the code would reproduce the measurement procedure. It
would not independently validate:

- the semantic labels assigned to communities;
- the inferred parent structures;
- a causal interpretation of layer changes;
- generalisation beyond the tested prompts, model and environment.

Those require separate semantic reconstruction, replication and intervention.
