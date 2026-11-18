# R020 run methodology — tiny-model representation/output contrast

## Status

```text
run_status         = planned
measurement_status = not_started
analysis_status    = not_started
```

This document defines what must take place for R020. It does not record an
executed run. The originating discussion is preserved in `hypothesis.md`.

## 1. Controlling question

R020 tests whether an intentionally very small language model can contain a
useful, prompt-conditioned semantic organisation even when its generated
answer is incoherent, irrelevant or materially less informative.

The comparison is between two products of the same model and prompt:

```text
same model + same prompt
        |
        +-- autoregressive continuation
        |
        `-- layerwise semantic evidence across the generation trajectory
```

The intended conclusion is not assumed in advance. A coherent answer, an
uninformative topology or a null difference are valid scientific outcomes.

## 2. Fixed experimental scope

R020 uses one model, one prompt and one deterministic continuation.

### Model

- Intended checkpoint: `EleutherAI/pythia-70m`.
- The exact immutable model revision must be resolved and recorded before
  execution. The run must not begin with an unresolved or floating revision.
- The model must run in evaluation mode without quantisation.
- Use FP32 unless a documented incompatibility prevents it. A change of
  precision after results are observed is not permitted.
- The tokenizer identity, revision, vocabulary size, special-token settings,
  layer count, hidden width and embedding-matrix identity must be recorded.
- No chat template is used.
- No fine-tuning or prompt optimisation is allowed.
- Before any model access or download, read `D:\AI\README.md`, inspect the
  shared stores and use `D:\AI\cache` for the ordinary framework cache.
- Model weights must not be stored in this repository.

Pythia 70M must not be replaced because its result is inconvenient. A model
change would require a separately planned run.

### Prompt

The exact UTF-8 prompt is:

```text
Question: Why would a city build a bridge across a river?
Answer:
```

The tokenizer output must be persisted before inference. The primary prompt
capture position is the final encoded prompt token. Its token ID, decoded
form and character alignment must be recorded rather than assuming that the
colon is independently tokenised.

### Generation

- Greedy decoding only: `do_sample = false`.
- Maximum continuation: 32 new tokens.
- Stop on the model's EOS token if it occurs earlier.
- Record the stop reason.
- Do not clean, correct or regenerate an unattractive continuation.
- Preserve both the raw decoded continuation and its token-by-token form.

## 3. Autoregressive capture contract

R020 must capture the internal state that produces every generated token, not
only the state preceding the first token.

For generated token `y_t`, the causal alignment is:

```text
prompt + y_1 ... y_(t-1)
        |
        v
all layer states at the current final position
        |
        v
next-token logits and probability distribution
        |
        v
argmax selection of y_t
```

The representation of `y_t` after it is appended contributes to the decision
for `y_(t+1)`; it did not produce itself. Every persisted record must preserve
this distinction.

### Required states

For every decoding decision, capture:

1. the input embedding state at the decision position;
2. the raw output of every transformer block;
3. the final normalised state used by the language-model head;
4. the complete next-token logits; and
5. the selected token, its probability and its rank.

The adapter must inspect the actual Pythia implementation and label these
states explicitly. It must not silently treat a final-normalised state as a
raw final-block output. Forward hooks may be used where the model's standard
`hidden_states` return does not expose both objects separately.

### Required token coverage

Persist both:

- a decision tensor indexed by generation step, recorded state and hidden
  dimension; and
- a final full-sequence tensor indexed by recorded state, sequence position
  and hidden dimension, covering every prompt and generated token.

A token-alignment table must identify:

- sequence position;
- prompt or generated status;
- generation step;
- token ID and decoded token text;
- the preceding position/state that predicted it; and
- whether it was the final token or an EOS token.

Because the model is intentionally small, the preferred implementation is a
manual greedy loop using full-prefix forward passes with caching disabled.
This favours inspectability and alignment over generation speed.

## 4. Layerwise vocabulary measurement

For every generation decision and every recorded state:

1. project the decision vector against the fixed usable input-embedding
   vocabulary using cosine similarity;
2. preserve the full vocabulary score vector or an exactly reconstructable
   compressed representation;
3. export ranked positive and negative tokens;
4. retain the top-token view needed for direct human inspection;
5. determine positive-head and negative-tail populations using the existing
   full-curve cutoff method;
6. construct the existing within-population token-similarity networks; and
7. calculate deterministic state-local communities.

The existing topology method should be reused where structurally applicable:

- token IDs are stable join keys;
- positive and negative cosine sectors remain separate;
- negative cosine is geometric anti-alignment, not semantic suppression;
- graph and community seeds are fixed and recorded;
- community IDs are local to one generation step, state and sector; and
- any method change or insufficient population must be reported rather than
  silently repaired.

Top tokens are measured evidence, not yet semantic conclusions. Parent
structures and adjacent topics are interpretive outputs produced later.

## 5. Two-dimensional topic-trajectory analysis

R020 must analyse the measured evidence along two independent axes:

```text
                         TRANSFORMER DEPTH
generation decision     input → block 0 → ... → final state
          1                 topic reorganisation
          |
          2                 topic reorganisation
          |
          3                 topic reorganisation
          v
                 AUTOREGRESSIVE GENERATION TIME
```

The unit of interpretation is therefore not an isolated top-token list. It is
a topic or parent structure traced through the lattice of generation decision,
recorded state and cosine sector.

### Community-first topic reconstruction

Do not apply LDA, BERTopic or another document-topic model independently to
the top-ten lists. Ranked vocabulary projections are not natural documents,
and small rank changes could manufacture artificial topic changes.

Use this sequence instead:

```text
full selected token population
        ↓
token relationship network
        ↓
state-local communities
        ↓
broad semantic identity with confidence
        ↓
matches across transformer states
        ↓
matches across generation decisions
        ↓
topic trajectory
```

Top-token lists remain compact evidence for inspection, but topic identity and
trajectory must use the broader membership, edge and community evidence where
available.

### Within-decision layer trajectories

For each next-token decision, determine:

- which structures already exist at the input embedding state;
- which structures appear only after contextualisation;
- which strengthen, weaken, split, merge, disappear or reappear through
  depth;
- which survive into the final prediction state; and
- whether the selected token is consistent with the final structures.

The final selected-token alignment must be interpreted cautiously because the
language-model head and vocabulary projection may share or closely relate to
the embedding basis. Structure at intermediate states and change relative to
the input-state baseline are more discriminating evidence.

### Across-decision generation trajectories

Match corresponding structures between successive generation decisions and
record whether each structure:

- persists throughout the continuation;
- is expressed in a generated token;
- remains internally present but unexpressed;
- is introduced only after a semantically related generated token;
- decays before the response becomes incoherent; or
- changes sector, membership or role as the model consumes its own output.

The update observed after appending one generated token is an autoregressive
conditioning update. Without a counterfactual branch, it must not be called a
causal effect of that token.

### Topic-origin classification

Every reconstructed structure should receive the strongest defensible origin
classification, with ambiguity preserved:

- **Prompt-conditioned:** present before the first answer token exists.
- **Lexically inherited:** already present in the current final token's input
  embedding neighbourhood.
- **Contextually recruited:** absent at the input state but appears through
  transformer depth using the full prefix.
- **Self-conditioned:** first appears after the model generates a related
  token.
- **Persistent but unexpressed:** remains visible internally without being
  verbalised in the continuation.
- **Decaying or displaced:** initially present but progressively loses its
  measured structure.

These are descriptive trajectory labels, not claims about literal thoughts.

### Expression alignment

For every topic, record its internal and textual status:

| Internal evidence | Expressed in continuation | Interpretation |
| --- | --- | --- |
| Present | Yes | Internal structure reached the response |
| Present | No | Learned association was available but not verbalised |
| Not detected | Yes | Output lacks a persistent topic trace under this measurement |
| Not detected | No | No evidence that the model represented it |

The second row is the result most directly relevant to the R020 hypothesis,
especially when the structure is prompt-conditioned, survives multiple states
or decisions and is absent from the shuffled-label control.

### Divergence-point analysis

Identify the earliest generation decision, if any, at which:

- answer coherence materially deteriorates;
- the core question-relevant structure disappears;
- adjacent structures become diffuse or unrelated;
- selected tokens cease to align with the dominant final-state structure; or
- internal semantic organisation and visible output begin to tell different
  stories.

The analysis must distinguish:

```text
semantic organisation collapses → incoherent output follows

from

useful semantic organisation persists → output fails to express it
```

The latter is stronger evidence for representational usefulness exceeding
generative usefulness.

### Topic matching evidence

Cross-state and cross-decision matches must retain:

- source and destination community identifiers;
- token-membership overlap;
- edge overlap where available;
- representative and extreme tokens;
- sector and score/rank evidence;
- semantic identity and confidence;
- match confidence; and
- unresolved alternatives.

Do not reduce these fields to one opaque topic-probability score. Different
cutoff sizes and score distributions can otherwise create artificial topic
emergence or decay.

## 6. Controls

### Input-state baseline

The input embedding state provides the baseline for associations attributable
to the final prompt token before transformer contextualisation. Intermediate
states add evidence only if they reorganise the neighbourhood beyond that
baseline.

### Deterministic replay

Repeat the complete greedy capture once with the same model, prompt, runtime
and tensor shapes. Compare:

- generated token IDs;
- raw hidden states;
- logits;
- vocabulary scores; and
- derived memberships, edges and communities.

Any non-zero difference must be recorded. It is a measured runtime property,
not grounds for silently selecting the more convenient replay.

### Shuffled semantic control

Create a deterministic global permutation of usable vocabulary labels while
preserving measured scores, graph structure, community structure and
cross-state identity. Apply the same permutation consistently across the
control package.

This control tests whether a later analyst can manufacture plausible semantic
coherence from structurally organised but semantically meaningless labels.
The seed and permutation hash must be recorded. The unshuffled evidence
remains the scientific measurement; the shuffled package is an analysis
control.

## 7. Independent evaluation

Measurement and semantic interpretation must remain separate.

```text
CODEX
capture → validate → score → construct networks → export → stop

CHATGPT
reconstruct semantic structures → compare with control → evaluate answer
→ write final analysis
```

### Generated-answer evaluation

Score the continuation without access to the semantic reconstruction:

- correctness;
- grammatical and logical coherence;
- relevance to the question;
- coverage of the central relation; and
- useful information beyond superficial word reuse.

The minimal reference answer is:

> A city builds a bridge to connect places and allow people and goods to
> cross the river.

This reference establishes answer correctness. It must not be treated as a
complete semantic map.

### Topology evaluation

The first semantic pass must not see the generated continuation or the list
of anticipated adjacent topics. It should classify the measured communities
and trajectories, state uncertainty and distinguish semantic material from
lexical/tokenizer artefacts.

Only after that reconstruction is frozen should it be compared with the
prompt and assessed for:

- recovery of the core bridge/crossing relation;
- defensible adjacent structures not required by the minimal answer;
- reorganisation through transformer depth;
- persistence or loss during autoregressive generation;
- additional information absent from the continuation;
- differences from the input-state baseline; and
- superiority to the shuffled-label control.

Engineering, transport, geography, environment, infrastructure, planning,
government, access, community, commerce, logistics and trade are candidate
adjacent domains documented before execution. They are not mandatory labels
and must not be imposed on unclear evidence.

## 8. Outcome classification

Scientific outcome and run validity are separate.

| Generated answer | Measured topology | Interpretation |
| --- | --- | --- |
| Poor | Useful and control-separated | Supports the R020 hypothesis |
| Useful | Useful | Semantic structure exists; no strong representational advantage shown |
| Poor | Uninformative or control-equivalent | Hypothesis unsupported |
| Useful | Uninformative | Measurement method did not expose the structure supporting the answer |

An ambiguous result must be labelled unresolved. It must not be converted
into support through additional prompts, models or post-hoc criteria.

## 9. Required run artifacts

The exact packaging may reuse existing pipeline formats, but R020 must retain
the following evidence classes:

```text
R020_pythia-70m-representation-output-contrast/
├── hypothesis.md
├── R020_RUN_METHODOLOGY.md
├── run_config.json
├── manifest.json
├── model_metadata.json
├── prompt_records.json
├── generation_trace.csv
├── token_alignment.csv
├── capture_validation.json
├── artifact_index.json
├── top_tokens_by_step_and_state.csv
├── cutoffs.csv
├── network_index.csv
├── community_nodes.csv
├── community_edges.csv
├── chatgpt_community_networks.json
├── chatgpt_layer_packets.md
├── controls/
│   └── shuffled_label_package.*
├── local_raw_capture/
│   ├── decision_states.*
│   ├── full_sequence_states.*
│   └── vocabulary_scores.*
├── R020_MEASUREMENT_REPORT.md
├── R020_SEMANTIC_RECONSTRUCTION.md
├── analysis/
│   ├── topic_instances.csv
│   ├── topic_layer_trajectories.csv
│   ├── topic_generation_trajectories.csv
│   ├── topic_expression_alignment.csv
│   └── R020_TOPIC_TRAJECTORY_REPORT.html
└── R020_FINAL_REPORT.html
```

Large raw tensors may remain local rather than be committed, but their paths,
shapes, data types and cryptographic hashes must be recorded. Compact measured
evidence required for independent analysis must be suitable for GitHub and
ChatGPT. Model weights must never enter the repository.

## 10. Validation and lifecycle gates

### Before model execution

- Inspect Git status and preserve unrelated changes.
- Make the intended R020 files trackable without exposing ignored raw data.
- Read `D:\AI\README.md` and inspect existing model storage.
- Resolve and freeze the exact model revision.
- Validate the run configuration and prompt hash.
- Verify that no stale measurement artifacts exist.
- Set the manifest to `running` before the first scientific capture.

### Measurement succeeds only if

- every generated token has a correctly aligned decision record;
- every transformer block and required boundary state is captured;
- all hidden states, logits and scores are finite;
- greedy argmax selections reproduce the recorded token sequence;
- the final full-sequence capture reconciles with the per-step trace within a
  declared numerical tolerance;
- deterministic replay comparisons are complete;
- every required state/step/sector network exists exactly once;
- every selected node and community reference reconciles;
- the shuffled control is complete and hashed;
- every persisted artifact is indexed and hashed; and
- the measurement report contains no semantic parent conclusions.

On any fatal failure, mark the manifest `measurement_failed` immediately and
do not perform downstream interpretation using partial or stale evidence.

After successful measurement:

```text
measurement_status = measurement_successful
analysis_status    = not_started
run_status         = awaiting_semantic_analysis
```

R020 becomes complete only after independent semantic reconstruction, answer
evaluation, control comparison and the final report are all present and
validated.

### Analysis succeeds only if

- every interpreted topic instance links back to measured step, state, sector
  and community evidence;
- within-decision layer matching is complete for every generated-token
  decision;
- across-decision matching covers the complete generated sequence;
- topic-origin classifications retain confidence and ambiguity;
- internal-versus-expressed alignment is complete;
- a divergence point is identified or explicitly found absent;
- the shuffled-label control is analysed under the same procedure;
- the topic-trajectory files reconcile with one another; and
- the topic-trajectory and final reports distinguish measurement from
  interpretation.

## 11. Execution order

1. Freeze and validate the model revision, tokenizer, prompt, decoding rules
   and output schema.
2. Inspect shared model storage and download only if the checkpoint is absent.
3. Adapt the existing capture adapter to expose raw block outputs, final
   normalisation, logits and per-step token alignment.
4. Perform a disposable technical preflight outside the scientific output
   package.
5. Initialise the manifest as `running` and execute the deterministic primary
   capture.
6. Execute the identical replay.
7. Produce vocabulary projections, top-token tables, cutoffs, networks and
   communities for every decision step and state.
8. Produce the shuffled-label control and compact ChatGPT-readable exports.
9. Reconcile expected and observed coverage, hash all artifacts and write the
   semantic-free measurement report.
10. Freeze the measurement evidence.
11. Conduct independent semantic reconstruction without revealing the
    continuation or anticipated adjacent-domain list.
12. Construct topic instances and match them first across transformer states,
    then across generation decisions.
13. Classify topic origins, expression status and the point of divergence, if
    any, while applying the same procedure to the shuffled control.
14. Freeze the topic trajectory, then reveal and evaluate the generated
    answer and compare it with the reconstruction and control.
15. Write the topic-trajectory and final reports and update the manifest to
    `complete` only after every required component validates.
16. Commit and push only when explicitly authorised.

## 12. Outside scope

- additional prompts, paraphrases or permutations;
- changing the model after inspecting results;
- comparing model families or parameter scales;
- optimising generation until it becomes coherent or incoherent;
- sampled decoding or multiple candidate answers;
- fine-tuning or activation intervention;
- curvature, SDA-3 or GRD analysis;
- treating top tokens as literal thoughts or a causal reasoning transcript;
- recovery of specific training documents; and
- claims that one prompt establishes a universal advantage for internal-state
  analysis over generated responses.

## 13. Validation amendment after the first production attempt

The first production attempt exposed an overly strict technical validation
criterion before any semantic inspection took place. Exact same-shape replay
was bit-for-bit identical for generated token IDs, decision hidden states and
logits. However, 68 of the 256 comparisons between prefix-length forwards and
the separate 48-token full-sequence forward failed elementwise
`torch.allclose(atol=1e-5, rtol=1e-5)`. Different causal sequence lengths can
select different deterministic CUDA matrix shapes and therefore accumulate
small FP32 rounding differences even though future positions remain masked.

The observed diagnostic bounds were:

- minimum double-precision cosine similarity: `0.9999999662655082`;
- maximum absolute hidden-state difference: `0.0047760009765625`;
- maximum hidden-state L2 difference: `0.025218963483017432`;
- maximum vocabulary cosine-score difference: `5.0768256187438965e-05`;
- exact top-50 positive-set overlap: `50/50` for all 256 comparisons; and
- exact top-50 negative-set overlap: `50/50` for all 256 comparisons.

That first attempt is a failed validation calibration, not scientific
evidence. Its hashes and diagnosis are retained in
`R020_VALIDATION_AMENDMENT.md`. The clean rerun uses the following declared
gate in addition to retaining the original elementwise result as a diagnostic:

1. generated token IDs, decision states and decision logits must reproduce
   exactly under a same-shape deterministic replay;
2. every prefix/full-sequence state pair must have double-precision cosine
   similarity of at least `0.9999999`;
3. every pair must retain all 50 tokens in both its positive and negative
   projected top-token sets; and
4. all elementwise, directional and projection metrics must remain recorded
   rather than replacing or concealing the failed elementwise diagnostic.

This amendment changes only the numerical reconciliation gate. It does not
change the model, precision, prompt, generated continuation, projection basis,
cutoff, network construction, community method or semantic-analysis boundary.
