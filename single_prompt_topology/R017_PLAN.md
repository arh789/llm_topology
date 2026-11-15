# R017 plan — OLMo 3 choke-point / barrier / spear semantic map

## Objective

Run the validated local `allenai/Olmo-3-1125-32B` native-BF16 backend on the bare-concept prompt:

```text
choke point
collapsible barrier
spear
```

Capture the final newline-anchor representation at every transformer state, project every state into the fixed input-embedding vocabulary basis, construct separate positive-head and negative-tail exact 10-nearest-neighbour graphs, detect state-local Louvain communities, and reconstruct the smallest defensible semantic map supported by those measurements.

## Locked model and capture contract

- Model: `allenai/Olmo-3-1125-32B`
- Revision: `c2b61dae89a1ad10e4ad5653d0e46b590902607b`
- Precision: native BF16; no quantisation
- Prompt form: three concepts separated by newlines, followed by one final newline
- Chat template: none
- Special tokens: none added
- Capture position: final newline token
- Response generation: none
- Expected transformer states: 65 (input embedding plus 64 block/final-normalisation states)
- Model cache: `D:\AI\cache\huggingface\hub`
- Placement caps: CUDA 18 GiB, CPU 28 GiB, remaining weights disk-backed

## Measurement contract

For each of the 65 captured states:

1. Calculate cosine similarity against every usable input-embedding vocabulary row.
2. Exclude the newline anchor token from cutoff selection.
3. Select positive and negative populations independently using the established full-curve maximum-deviation elbow.
4. Construct an exact 10-nearest-neighbour graph within each selected population using static input-embedding cosine similarity.
5. Symmetrise directed neighbours when either direction exists.
6. Partition the unweighted graph using deterministic Louvain community detection.
7. Export network, community, intercommunity-edge and adjacent-state transition evidence.

Expected measured coverage:

- 65 states × 2 cosine sectors = **130 networks**
- 64 adjacent transitions × 2 cosine sectors = **128 transition rows**

## Interpretation and report contract

The final report will follow the useful structure of R014/R015 while remaining appropriate to a single-prompt run:

1. strongest supported result;
2. experimental input and measurement status;
3. measured sector and depth development;
4. independently reconstructed parent structures;
5. relations between parents;
6. minimum semantic map;
7. evidence and limitations;
8. report fields that should be standardised after the run.

Positive and negative mean geometric alignment and anti-alignment with the evolving anchor state. Negative does not independently establish suppression, contradiction or rejection. Community IDs are local to a single state and sector. Semantic parent labels and relations are interpretations added only after measured exports are complete.

## Success criteria

R017 succeeds only if all of the following are persisted and validated:

- exact prompt/token record and 65 finite anchor states;
- finite full-vocabulary scores for every state;
- independently calculated positive and negative cutoffs for every state;
- 130 unique measured networks with exact 10-neighbour coverage;
- complete community and adjacent-transition exports;
- a ChatGPT-readable measured packet with no pre-imposed semantic labels;
- an evidence-linked semantic-map report that clearly separates measurement from interpretation;
- a successful manifest whose component counts reconcile with the exported files.

If any required component fails, the run is failed and no stale or partial data may be interpreted as the result.

## Outside scope

- autoregressive response generation;
- prompt permutations or context-invariance testing;
- comparison of OLMo with Qwen or another model;
- SDA-3 or GRD role assignment;
- changing the R014/R015 reports or designing a universal report system before this run supplies evidence about what should be standardised;
- committing or pushing without a separate user instruction.
