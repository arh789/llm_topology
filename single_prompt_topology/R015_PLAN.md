# R015 plan: adjacent semantic-neighbourhood expansion

## Run identity

- Run number: `R015`
- Run directory: `R015_qwen-adjacent-neighbourhood-expansion`
- Run type: measured four-probe, twenty-four-prompt adjacent-region topology
- Status: `planned and frozen; not executed`
- Backend: Hugging Face Transformers + `Qwen/Qwen2.5-7B-Instruct`, BF16
- Measurement baseline: R014

## Stated objective

Repeat the R014 overlapping-context experiment with four neighbouring concepts
drawn from its reconstructed semantic families, changing only the concept
inputs while preserving the measurement instrument.

## Inferred objective

Determine whether R014 recovered a persistent local semantic topology rather
than merely decomposing its literal seed concepts. R015 moves the observation
window to adjacent semantic space and tests whether the R014 topology
continues, deforms, splits, merges or terminates.

R015 does not test SDA-3 and does not move to a distant semantic region.

## Locked concept-selection evidence

The selection is justified in `R015_CONCEPT_SELECTION_EVIDENCE.md` using an
exact scan of all R014 selected token memberships, the independent R014 probe
reconstructions and the pinned tokenizer.

```text
A = sensor
B = apartment
C = line
D = sessions
```

No R014 parent label is used as an R015 prompt concept. `interaction / change`
and `representation / information` remain unsupplied so that their recurrence
can be tested independently.

## Locked probes

| Probe | Concepts | Held out |
|---|---|---|
| P1 | sensor, apartment, line | sessions |
| P2 | sensor, apartment, sessions | line |
| P3 | sensor, line, sessions | apartment |
| P4 | apartment, line, sessions | sensor |

Every probe uses all six local position orders:

```text
ABC, ACB, BAC, BCA, CAB, CBA
```

Here `A`, `B` and `C` name positions inside a probe tuple, not the global
concept keys. This produces exactly 24 prompt trajectories.

Each concept occupies one line. Every input ends with one fixed newline anchor.
No chat template, system message, role marker, assistant prefix, synthesis
question or response generation is permitted.

## Balanced pair and context coverage

Every concept occurs in three probes, and every pair occurs under two
third-concept contexts:

| Pair | Context 1 | Context 2 |
|---|---|---|
| sensor ↔ apartment | line | sessions |
| sensor ↔ line | apartment | sessions |
| sensor ↔ sessions | apartment | line |
| apartment ↔ line | sensor | sessions |
| apartment ↔ sessions | sensor | line |
| line ↔ sessions | sensor | apartment |

## Locked model and capture contract

- Model: `Qwen/Qwen2.5-7B-Instruct`
- Revision: `a09a35458c702b33eeacc393d103063234e8bc28`
- Precision: BF16
- Runtime: Hugging Face Transformers
- Device: RTX 4090
- Cache: `D:\AI\cache\huggingface\hub`
- Model loading: local cache only
- Anchor: newline token ID `198`

For every prompt, capture the final anchor position at the input embedding,
every transformer-block output and final normalisation after Block 27.

Expected trajectory coverage:

```text
24 prompts × 29 states × 3,584 hidden dimensions
```

All states must be finite and exactly reproducible. State 00 must be exactly
equal across all 24 prompts.

## Locked measurement contract

R015 reuses the R014 method unchanged:

- cosine projection against the fixed input-embedding vocabulary;
- exclusion of the shared anchor token from cutoff selection;
- independent positive-head and negative-tail selection using the R004
  full-curve maximum-deviation elbow;
- exact 10-nearest-neighbour graphs in the fixed input-embedding basis;
- edge symmetrisation when either directed relation exists;
- deterministic unweighted NetworkX Louvain partitions;
- token IDs as stable join keys; and
- community IDs local to one prompt, state and side.

No new cutoff, graph, community, curvature or coherence method is permitted.

## Required measured coverage

```text
24 prompts × 29 states × 2 sides = 1,392 networks

24 prompts × 28 transitions × 2 sides
= 1,344 within-prompt transition rows

4 probes × C(6,2) permutation pairs × 29 states × 2 sides
= 3,480 within-probe permutation-comparison rows
```

Within each probe, token and edge support must be counted independently across
support levels 1/6 through 6/6.

## Implementation reuse decision

R014 is complete and reproducible, but its scripts intentionally hard-code
R014 identities, paths and report names. Refactoring the successful R014 code
before R015 would unnecessarily risk the baseline.

The bounded implementation strategy is therefore:

1. preserve every R014 file unchanged;
2. mechanically derive `r015_config.py`, `r015_capture_hidden_states.py`,
   `r015_semantic_topology.py` and `r015_run.py` from their R014 counterparts;
3. change only run identity, config imports, locked concept strings, plan and
   evidence paths, output names and human-readable R015 labels;
4. verify that the computational functions and parameters remain equivalent;
5. defer shared-engine refactoring until after R015 replication.

This small duplication is deliberate proof-of-concept isolation, not a new
abstraction layer.

## Measured-run components

1. `plan_lock`
2. `concept_selection_lock`
3. `environment_probe`
4. `anchor_probe`
5. `primary_capture`
6. `capture_validation`
7. `projection_and_cutoffs`
8. `split_networks_and_communities`
9. `within_prompt_transitions`
10. `within_probe_permutation_comparisons`
11. `within_probe_invariance`
12. `chatgpt_exports`
13. `completeness_validation`
14. `run_report`

The manifest remains `running` until all fourteen components pass.

## Required measured artifacts

R015 must reproduce the R014 artifact contract under the R015 run directory,
including hidden-state captures, prompt records, validation records, vocabulary
scores, cutoffs, selected token and edge tables, community tables, transitions,
pairwise comparisons, permutation support, ChatGPT-readable exports,
completeness verification, measurement report, manifest and artifact index.

The measured pipeline stops before semantic interpretation.

## Independent semantic reconstruction protocol

After measurement succeeds:

1. reconstruct each probe independently from its measured communities;
2. infer the broadest defensible probe-local parents without R014 labels;
3. identify persistent within-probe relations across permutations and states;
4. record held-out-region recovery or failure;
5. complete all four probe reconstructions before cross-probe matching;
6. construct the R015 parent and parent-relation map, if supported;
7. only then compare the completed R015 map with R014.

Required downstream records are:

- `R015_PROBE_RECONSTRUCTIONS.md`;
- `R015_SEMANTIC_MAP_NODES.csv`;
- `R015_SEMANTIC_MAP_EDGES.csv`;
- `R015_SEMANTIC_MAP.json`;
- `R015_RUN_ANALYSIS_AND_RECOMMENDATIONS.html`; and
- an explicit R014 ↔ R015 comparison record.

Every inferred node and edge must remain traceable to probe, prompt,
permutation, state, side, community and token evidence.

## R014 ↔ R015 comparison contract

Only after independent R015 reconstruction, compare:

- parent persistence, deformation, split, merge, disappearance, replacement,
  strength change and sector migration;
- recurrence or failure of the seven R014 mapped relations;
- held-out semantic reconstruction in both runs; and
- unsupplied recurrence or disappearance of structures resembling R014's
  `interaction / change` and `representation / information` parents.

Continuity must not be assumed. Contradictory evidence remains attached to the
specific node or relation it affects.

## Success criteria

Operational success requires:

- exact model, revision, tokenizer, anchor and method equivalence with R014;
- all 24 captures and the three frozen coverage totals;
- exact deterministic replay and State 00 equality;
- complete referential integrity and ChatGPT-readable exports;
- independent probe reconstruction before R014 comparison; and
- traceable positive or negative conclusions.

Scientific success includes either:

- substantial independently reconstructed continuity with R014; or
- a defensible discontinuity that identifies where the local topology changes.

No continuity is required for the experiment to be successful.

## Failure conditions

R015 fails methodologically if:

- the measurement method differs materially from R014;
- any prompt, state, sector, network, transition or comparison is missing;
- the anchor, determinism or State 00 controls fail;
- R014 labels contaminate first-pass R015 reconstruction;
- held-out tests are omitted;
- inferred nodes or edges lack measured provenance;
- contradictory evidence is smoothed into apparent continuity; or
- the run produces data that cannot support independent semantic analysis.

## Outside scope

- distant-region replication;
- SDA-3 or GRD comparison;
- additional seeds, probes or model families;
- changes to the anchor, cutoff, graph or community method;
- response generation;
- curvature or coherence additions;
- global semantic-map construction; and
- refactoring R014 into a generalized framework before replication.

## Next bounded operation

Implement the four R015 scripts through mechanical R014 derivation, verify the
configuration and computational equivalence without loading the model, then
report readiness before executing the 24-prompt run.

Intended production entry point after implementation:

```powershell
C:\Users\arhal\anaconda3\envs\myenv\python.exe single_prompt_topology\r015_run.py
```
