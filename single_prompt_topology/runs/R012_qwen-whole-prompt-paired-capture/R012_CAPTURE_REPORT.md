# R012 Qwen whole-prompt paired capture report

## Outcome

R012 succeeded. Hugging Face Transformers exposed and persisted the
final-position hidden-state trajectory for both controlled prompts using
Qwen2.5-0.5B-Instruct and Qwen2.5-7B-Instruct in BF16 on the RTX 4090.

No response token was generated. The measured position was the final token of
the official chat template's assistant-generation prefix. It was token ID 198
(`Ċ`) at input index 41 for both 7B inputs. Each position therefore had causal
access to the complete 42-token templated prompt.

## Controlled prompt pair

Baseline:

```text
What structure forms from electro pink, curvature density, Tokyo nightlife?
```

Variation:

```text
What structure forms from electro pink, Tokyo nightlife, curvature density?
```

The only intended change was the order of `curvature density` and
`Tokyo nightlife`.

## Smoke capture

| Field | Result |
|---|---:|
| Model | Qwen/Qwen2.5-0.5B-Instruct |
| Resolved revision | `7ae557604adf67be50417f59c2c2f167def9a775` |
| Transformer blocks | 24 |
| Recorded states | 25 |
| Hidden width | 896 |
| Precision | BF16 |
| Peak GPU allocation | 1,019,487,232 bytes |
| Deterministic replay | Exact |
| State 00 paired equality | Exact |
| Post-embedding difference | Present |
| Minimum paired cosine | 0.9963737726 at State 15 |
| Maximum paired L2 | 24.9137783 at State 24 |

The smoke capture passed before the 7B model was attempted.

## Primary 7B capture

| Field | Result |
|---|---:|
| Model | Qwen/Qwen2.5-7B-Instruct |
| Resolved revision | `a09a35458c702b33eeacc393d103063234e8bc28` |
| Transformer blocks | 28 |
| Recorded states | 29 |
| Hidden width | 3,584 |
| Precision | BF16 |
| Input tokens per prompt | 42 |
| Capture index | 41 |
| Capture token | ID 198, `Ċ` |
| Peak GPU allocation | 15,306,347,520 bytes |
| Peak GPU reservation | 15,439,233,024 bytes |
| Deterministic replay | Exact |
| State 00 paired equality | Exact |
| Changed post-embedding states | 28 of 28 |
| Minimum paired cosine | 0.9885432720 at State 28 |
| Maximum paired L2 | 50.2713394 at State 27 |

The model fit on the RTX 4090 with a measured peak allocation of approximately
14.25 GiB. After the process exited, GPU memory returned to its pre-run range.

## Factual layerwise result

State 00 was identical because both prompts ended at the same fixed chat-template
token before any transformer block could incorporate the preceding context.

The two trajectories first differed after Block 0. All 28 post-embedding states
differed. The displacement generally increased with depth, although it was not
strictly monotonic:

- Block 0 output: cosine 0.9998824; L2 0.1607594.
- Block 8 output: cosine 0.9946783; L2 3.7221467.
- Block 19 output: cosine 0.9935145; L2 11.6618309.
- Block 22 output: cosine 0.9905756; L2 25.7966423.
- Block 26 output: cosine 0.9922417; L2 50.2713394.
- Final normalisation after Block 27: cosine 0.9885433; L2 42.8996048.

This establishes that swapping two concept phrases measurably changes the
whole-prompt final-position representation from the first transformer block and
that the difference persists through the terminal state. It does not yet
establish which vocabulary relationships, communities or semantic
interpretations changed.

## Validation

- Both model stages returned every expected state.
- Both trajectory pairs had matching dimensions.
- All values were finite.
- Each prompt was forwarded twice and reproduced exactly.
- Both prompts used the same final capture token and index.
- State 00 was exactly equal across each pair.
- At least one later state differed; in the 7B run all later states differed.
- Both Safetensors files were independently reloaded after execution.
- Every stage artifact byte count and SHA-256 hash was independently verified.
- Response generation was not executed.

## Download incident

The first 7B download attempt was interrupted after silent console output was
misdiagnosed as a stall. Later cache inspection showed that it had completed
three shards and most of the remaining shard. The diagnosis and interruption
were therefore incorrect.

The second attempt disabled the Xet transport, reused the cached content,
completed through standard HTTP and then executed successfully. No cached model
content was deleted and the incident did not alter either prompt capture.

## Scope boundary

R012 validates the measurement path and records the first paired whole-prompt
trajectories. It does not perform vocabulary projection, cutoff selection,
network construction, community detection, semantic labelling, quantisation
comparison or larger-model scaling.

The next measured run can now reuse the 7B trajectories to compare vocabulary
neighbourhoods and community structure across the paired prompts without
re-running model inference.
