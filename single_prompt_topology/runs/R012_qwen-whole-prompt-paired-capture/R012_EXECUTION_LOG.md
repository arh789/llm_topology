# R012 execution log

## 2026-11-13 17:55 AEDT — run opened

- Status: `running`
- Source Git commit: `36333cce1916a75f180f64d02dfa9dc42bac7aec`
- R011 and all pre-existing uncommitted changes are being preserved.
- The canonical model-cache rules in `D:\AI\README.md` were read before any
  download.
- The existing project Conda environment was selected as the production path:
  `C:\Users\arhal\anaconda3\envs\myenv\python.exe`.
- Environment probe: Python 3.11.15, PyTorch 2.6.0+cu124, Transformers 5.12.1,
  Accelerate 1.14.0, Safetensors 0.8.0.
- CUDA probe: RTX 4090 detected, 24,564 MiB total, 20,512 MiB free.
- Neither required text-only Qwen model was cached at the time of inspection.
- No model had been downloaded or loaded when this entry was written.

Next gate: syntax-check the capture entry point, then execute only the 0.5B
smoke stage. The 7B stage remains prohibited until the smoke capture and its
paired validation succeed.

## 2026-11-13 17:59 AEDT — 0.5B smoke gate passed

- Model: `Qwen/Qwen2.5-0.5B-Instruct`
- Resolved revision: `7ae557604adf67be50417f59c2c2f167def9a775`
- Runtime: Transformers 5.12.1, PyTorch 2.6.0+cu124, BF16 on RTX 4090.
- Model load plus download stage completed successfully.
- Both controlled prompts were captured twice without response generation.
- Expected and observed trajectory shape: 25 states × 896 dimensions.
- Every value was finite.
- Both deterministic replays were exactly equal to their first capture.
- The paired prompts used the same capture token.
- State 00 was exactly equal across prompts.
- Later states differed as required.
- Minimum paired cosine similarity: 0.9963737726 at State 15.
- Maximum L2 distance: 24.9137783 at State 24.
- Peak GPU allocation: 1,019,487,232 bytes.
- All recorded artifact byte counts and SHA-256 hashes were independently
  verified after the process exited.
- Both Safetensors trajectories were reloaded and their shapes independently
  verified.

The smoke gate therefore authorises the planned 7B BF16 stage. No vocabulary
scoring, network construction or semantic interpretation has been performed.

## 2026-11-13 18:03 AEDT — 7B download attempt 1 interrupted

- The default Hugging Face Hub transport created four model-shard locks at
  18:00:30 AEDT.
- For more than two minutes afterward, no shard or Xet staging file grew and no
  worker progress was reported.
- The command was diagnosed as stalled rather than merely slow.
- It was interrupted with exit code 1.
- The model was not loaded and neither prompt was forwarded.
- The only stage artifact was the initial `running` status record.
- No cached model content was deleted.
- Recovery path: retry the identical capture with `HF_HUB_DISABLE_XET=1` so
  the Hub client uses its standard HTTP downloader and reuses valid cached
  metadata.

The manifest remains `running`; this is a transport retry within the existing
7B capture component, not a semantic or methodological fallback.

## 2026-11-13 18:04 AEDT — correction to the attempt-1 diagnosis

Subsequent inspection of the full Hub cache showed that the first transfer had
been healthy despite its silent console output. Three weight shards had
completed and the remaining shard had reached 3.26 GB before interruption.

The earlier diagnosis of a stalled download was therefore wrong, and the
interruption was premature. The standard-HTTP retry was allowed to continue
without using silence alone as a reason to stop it.

## 2026-11-13 18:05 AEDT — 7B capture and validation passed

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Resolved revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- Successful transport: standard HTTP with `HF_HUB_DISABLE_XET=1`.
- Runtime: Transformers 5.12.1, PyTorch 2.6.0+cu124, BF16 on RTX 4090.
- Both controlled prompts were captured twice without response generation.
- Input length: 42 tokens for each prompt.
- Shared capture anchor: index 41, token ID 198 (`Ċ`).
- Expected and observed trajectory shape: 29 states × 3,584 dimensions.
- Every value was finite.
- Both deterministic replays were exactly equal to their first capture.
- State 00 was exactly equal across prompts.
- All 28 post-embedding states differed.
- Minimum paired cosine similarity: 0.9885432720 at State 28.
- Maximum L2 distance: 50.2713394 at State 27.
- Peak GPU allocation: 15,306,347,520 bytes.
- All artifact hashes and byte counts were independently verified.
- Both Safetensors trajectories were independently reloaded and verified.

R012 is complete and successful. No vocabulary projection, cutoff calculation,
network construction, community detection or semantic interpretation was
performed.
