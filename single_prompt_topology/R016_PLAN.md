# R016 plan: OLMo 3 32B local BF16 feasibility

## Run identity

- Run number: `R016`
- Run directory: `R016_olmo3-32b-local-bf16-feasibility`
- Run type: local model-loading and instrumented-forward feasibility
- Status at plan lock: `planned; not yet executed`
- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Precision: native BF16
- Runtime: Hugging Face Transformers with Accelerate big-model dispatch

## Stated objective

Determine whether OLMo 3 32B Base can execute the project's required
instrumented first-token-prediction workload on the local RTX 4090 and system
RAM.

## Inferred objective

Establish whether the project can use a substantially larger, fully open base
model as an instrument for recovering learned semantic topology without remote
compute, quantising the model or generating a response.

R016 is a feasibility gate. It does not repeat R014 or R015 and does not
construct semantic networks.

## Locked model evidence

The official model repository reports:

- 32 billion parameters stored in BF16;
- 64 transformer layers;
- hidden width 5,120;
- 14 Safetensors weight shards;
- 64,476,978,123 repository bytes; and
- Transformers 4.57.0 or later.

The model snapshot belongs in the shared Hugging Face cache under
`D:\AI\cache`, never in the Git repository.

## Local preflight evidence

At plan time:

- GPU: NVIDIA GeForce RTX 4090, 24,564 MiB total;
- observed free VRAM: 19,918 MiB;
- physical RAM: 68,523,761,664 bytes total;
- observed available RAM: 38,631,174,144 bytes;
- free `D:` space: 1,171,207,970,816 bytes;
- PyTorch: 2.6.0+cu124;
- Transformers: 5.12.1;
- Accelerate: 1.14.0; and
- Safetensors: 0.8.0.

The feasibility configuration deliberately caps model placement at 18 GiB on
CUDA and 28 GiB in CPU RAM. Remaining weights are disk-offloaded under
`D:\AI\cache\offload\R016_olmo3-32b`. These caps preserve operating-system
headroom under the observed workload instead of assuming all applications have
been closed.

## Locked prompt and capture contract

The single prompt is:

```text
laser
city
spatial field
```

The final newline is the fixed capture anchor. The prompt is tokenised without
a chat template or added special tokens.

The run performs exactly one causal forward pass with:

```python
output_hidden_states=True
use_cache=False
```

No response token is sampled or generated. The run retains only the final
anchor position from every returned hidden state and the first-token logits
needed for validation.

## Required components

1. `plan_lock`
2. `environment_preflight`
3. `model_metadata_lock`
4. `snapshot_download`
5. `device_map_preflight`
6. `model_load`
7. `instrumented_forward`
8. `capture_validation`
9. `resource_cleanup`
10. `feasibility_decision`

The manifest must be `running` before network or model activity begins. Any
required component failure makes the run fail.

## Success criteria

R016 succeeds only if:

- the exact pinned BF16 snapshot is used;
- the complete model loads through a persisted GPU/CPU/disk device map;
- one forward pass completes without response generation;
- exactly 65 hidden states are returned for the 64-layer model;
- every captured anchor vector has width 5,120 and contains only finite values;
- finite first-token logits are returned over the complete vocabulary;
- the capture and logits are persisted with hashes;
- peak GPU allocation, process RSS, elapsed time and placement evidence are
  recorded; and
- model objects are released and CUDA memory is cleared after validation.

Successful loading without a completed forward pass is not success.

## Failure conditions

R016 fails if:

- the exact snapshot cannot be downloaded or verified;
- loading exhausts GPU, CPU, virtual memory or disk;
- the runtime cannot dispatch the model across the required devices;
- any expected hidden state is absent, malformed or non-finite;
- logits are absent or non-finite;
- a quantised or instruction-tuned substitute is used;
- response generation is used as a proxy for hidden-state capture; or
- stale artifacts are used after a failed component.

An operational failure is still a useful feasibility result when the exact
failure, resource state and attempted device map are persisted.

## Outside scope

- the 24-prompt R014/R015 workload;
- vocabulary projection, cutoffs, graphs or communities;
- semantic interpretation;
- model-quality comparison;
- quantisation;
- response generation;
- changes to R012–R015 artifacts; and
- deleting the downloaded model snapshot or offload cache.

## Production command

```powershell
C:\Users\arhal\anaconda3\envs\myenv\python.exe single_prompt_topology\r016_olmo3_32b_feasibility.py
```
