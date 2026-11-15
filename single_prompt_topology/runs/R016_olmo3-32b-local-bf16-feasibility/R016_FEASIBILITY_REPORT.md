# R016 OLMo 3 32B local BF16 feasibility report

## Result

**Successful.** The exact native-BF16 OLMo 3 32B Base model completed the
project's required instrumented first-token-prediction workload locally.

- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Repository size: 64,476,978,123 bytes
- Precision: native BF16; no quantisation
- Response generation: not executed
- Prompt tokens: 9
- Transformer layers: 64
- Captured hidden states: 65
- Capture shape: 65 × 5,120
- First-token vocabulary logits: 100,278
- Hidden states and logits finite: yes

## Measured placement

The locked placement caps were 18 GiB CUDA and 28 GiB CPU RAM, with the
remainder disk-backed.

- GPU: input embeddings and Layers 0–16
- CPU RAM: Layers 17–45
- Disk-backed: Layers 46–63, final norm, rotary embedding and LM head
- Device-map entries: 18 GPU, 29 CPU and 21 disk
- Peak GPU allocation during forward: 18,650,070,016 bytes
- Peak GPU reservation during forward: 18,662,555,648 bytes
- Process RSS after forward: 33,279,561,728 bytes
- Physical RAM still available after forward: 13,023,551,488 bytes

## Timing

- Snapshot acquisition: 792.78 seconds
- Device-map construction: 2.19 seconds
- Model load: 28.70 seconds
- Instrumented forward pass: 60.89 seconds
- Capture validation: 0.03 seconds
- Resource cleanup: 4.59 seconds
- Successful attempt total: 890.77 seconds

The cached snapshot makes later attempts materially shorter because the
792.78-second network stage is no longer required.

## Component results

- `plan_lock`: successful
- `environment_preflight`: successful
- `model_metadata_lock`: successful
- `snapshot_download`: successful
- `device_map_preflight`: successful
- `model_load`: successful
- `instrumented_forward`: successful
- `capture_validation`: successful
- `resource_cleanup`: successful
- `feasibility_decision`: successful

## Transport recovery note

Two early download attempts were interrupted after temporary shard files
appeared not to grow. Post-attempt file sizes showed that transfer progress had
been buffered and became visible late; the initial stall classification was
therefore premature. The successful attempt used Xet with one worker. The
interrupted attempts left approximately 8.9 GB of redundant incomplete cache
fragments. They are not model evidence and were deliberately not deleted.

## Validation

The persisted capture was independently reopened from Safetensors. Its shape,
BF16 dtype and finite values were confirmed, all ten required manifest
components were confirmed successful, and every persisted artifact hash
matched the manifest.

## Decision

OLMo 3 32B Base is locally feasible as a semantic-topology measurement
instrument on this system. The demonstrated configuration is slow but has
adequate memory headroom for the short first-token-prediction workload.

R016 does not establish the runtime of a 24-prompt topology run. Batching those
prompts should be tested separately because disk-backed layers may make batch
execution much more efficient than 24 sequential forward passes.
