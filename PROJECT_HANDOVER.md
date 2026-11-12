# Project Handover: Semantic Topology Research

## 1. Objective

Develop a reproducible experimental framework using open-weight language
models to investigate the relationship between:

- Semantic coherence and contradiction.
- Internal model representations and geometric structure.
- Coherence-increasing versus contradiction-concealing interventions.
- Changes in model behaviour following competing interventions.
- Pretraining, post-training and coherence-seeking response behaviour.

**Primary objective:** Determine whether regions of high semantic conflict
exhibit measurable internal geometric signatures, and whether these signatures
predict how models resolve or conceal contradictions.

The project must be capable of validating **or falsifying** this hypothesis.

## 2. Core Research Questions

Preserve these five questions as the primary analytical framework:

1. Where is coherence most stable?
2. Where is coherence least stable?
3. What addition A increases coherence?
4. What addition B conceals contradiction by masking conflict?
5. What trajectory follows from A versus B?

Operational definitions:

- **Stable coherence:** Relationships remain consistent under controlled
  perturbation.
- **Unstable coherence:** Competing propositions, assumptions or
  interpretations resist reconciliation.
- **Addition A:** An intervention that increases coherence while preserving
  contradictory evidence.
- **Addition B:** An intervention that increases apparent coherence by
  excluding, suppressing or reinterpreting conflicting evidence without
  resolving it.
- **Trajectory:** Subsequent changes in model responses and internal
  representations after A or B.

A and B are experimental hypotheses, not predetermined truths.

## 3. Critical Epistemic Distinctions

Maintain strict separation between:

| Construct | Definition |
| --- | --- |
| Semantic centrality | Connectivity within a defined conceptual network |
| Semantic conflict | Incompatibility between propositions or constraints |
| Representational distance | Distance between selected internal activation vectors |
| Geometric curvature | A mathematically defined property of a specified representation space |
| Response coherence | Apparent consistency of generated text |
| Contradiction concealment | Apparent consistency achieved without accounting for conflicting evidence |

**Do not assume semantic conflict equals high geometric curvature.**

Do not report inferred properties as measured properties.

Every geometric claim must identify the representation, layer, token position
or pooling rule, distance metric, neighbourhood construction and curvature
estimator.

## 4. Candidate Models

| Model | Purpose | Priority |
| --- | --- | --- |
| Pythia 410M / 2.8B | Establish baseline instrumentation and examine training checkpoints | First |
| OLMo 3 7B | Compare base, SFT, DPO and final instruction-trained variants | Primary research |
| Qwen3 8B | Compare thinking and non-thinking configurations | Secondary |
| Gemma 4 E2B / E4B | Test generalisation across model architectures | Later |

Relevant identifiers:

- `EleutherAI/pythia-2.8b`
- `allenai/Olmo-3-1025-7B`
- `allenai/Olmo-3-7B-Instruct-SFT`
- `allenai/Olmo-3-7B-Instruct-DPO`
- `allenai/Olmo-3-7B-Instruct`
- `Qwen/Qwen3-8B`

Verify model compatibility, exact revisions, licensing and available computing
resources before downloading weights.

Do not compare raw geometric coordinates across unrelated architectures as
though their representation spaces were directly aligned.

## 5. Experimental Design

### Phase A — Establish behavioural baseline

Create a controlled dataset containing:

- Genuine logical contradictions.
- Competing explanations without strict contradiction.
- Ambiguous propositions.
- Internally consistent propositions.
- Contradictions resolved by additional evidence.
- Contradictions apparently resolved by concealing evidence.

Initial target: 30 conflict cases, five paraphrases per case, plus matched
controls.

For every case, record:

- Original propositions and evidence.
- Expected logical relationships.
- Model-generated interpretation.
- Contradictions recognised or omitted.
- Proposed addition A.
- Proposed addition B.
- Subsequent responses under A and B.

Use identical follow-up questions for both interventions. Include neutral
condition labels and blinded evaluation to avoid prompting the desired outcome.

### Phase B — Capture internal representations

Instrument selected models to extract:

- Residual-stream hidden states at specified layers.
- Token-level and pooled representations.
- Relevant output logits and probabilities.
- Activation changes across experimental conditions.

Compare:

1. Baseline.
2. Contradictory evidence introduced.
3. Addition A introduced.
4. Addition B introduced.
5. Subsequent trajectory prompts.

Control for token position, prompt length, paraphrasing, sampling configuration
and representation normalisation.

### Phase C — Geometric analysis

Begin with:

- Cosine similarity and distance.
- Neighbourhood stability.
- Representational similarity across conditions.
- Changes in local graph structure.

Then investigate explicitly defined curvature estimators, such as graph-based
Ricci curvature, where justified.

Compare conflict-labelled and non-conflict regions.

Use matched controls, uncertainty estimates and statistical testing.

**The core falsification test:** Do semantic conflict regions exhibit
reproducibly different geometric properties after controlling for unrelated
linguistic and experimental factors?

### Phase D — Causal investigation

Use activation patching, ablation or equivalent controlled interventions.

Determine whether altering candidate representations changes:

- Contradiction recognition.
- Contradiction concealment.
- Response consistency.
- Subsequent response trajectories.

Correlations alone are insufficient to establish causal mechanisms.

### Phase E — Training-stage comparison

Compare OLMo's related training-stage variants.

Investigate whether post-training changes:

- Recognition of conflicting information.
- Preference for coherent explanations.
- Willingness to preserve unresolved contradictions.
- Concealment versus genuine integration.
- Relationships between behavioural outcomes and internal representations.

Do not assume post-training necessarily increases contradiction concealment.

## 6. Evaluation

The framework must distinguish three independent results.

**Behavioural:** Does the model recognise, preserve, resolve or conceal
contradictions?

**Geometric:** Are corresponding internal representations measurably different?

**Causal:** Do interventions on those representations change the behaviour?

Evaluate prediction against controls and chance baselines, with held-out cases
and uncertainty intervals.

A hypothesis is not validated merely because a visualisation appears consistent
with it.

Report null results and contradictory evidence.

## 7. Technical Implementation

Preferred environment:

- Python and PyTorch.
- Hugging Face Transformers.
- NNsight and/or TransformerLens.
- NumPy, pandas, scikit-learn.
- NetworkX for explicitly constructed semantic or activation-derived graphs.
- Appropriate geometric-analysis libraries, selected after defining the
  metric.
- Matplotlib for diagnostic visualisation.

Begin with the smallest suitable model and dataset. Establish memory
requirements before attempting larger activation captures.

Capture model IDs, revisions, prompts, seeds, software versions,
configurations and metric definitions for reproducibility.

Suggested repository structure:

- `config/` — experimental configurations.
- `data/` — controlled stimuli and annotations.
- `src/models/` — loading and instrumentation.
- `src/experiments/` — controlled interventions.
- `src/metrics/` — behavioural and geometric measurements.
- `src/analysis/` — hypothesis testing.
- `tests/` — unit and integration tests.
- `results/` — reproducible outputs.
- `docs/` — methodology, findings and limitations.

## 8. Codex Operating Protocol

Use Objective–State–Execution (OSE).

Before execution:

1. State the objective and success criteria.
2. Inspect the actual repository and computing environment.
3. Identify supported assumptions and unresolved dependencies.
4. Establish the minimum viable experiment.
5. Explicitly distinguish evidence from hypotheses.

During execution:

- Perform bounded operations.
- Verify each operation.
- Preserve successful states.
- Record failures and recovery actions.
- Avoid speculative refactoring or unnecessary infrastructure.
- Do not silently substitute easier measurements for the intended research
  question.

After execution:

- Report what was implemented.
- Report what was tested.
- Present the strongest conclusion supported by evidence.
- State what remains unverified.
- Identify the next experiment that would most increase confidence.

## 9. Initial Deliverable

Build a minimum viable experiment using a small Pythia checkpoint.

It must:

1. Load the model and verify internal activation access.
2. Execute a small set of contradictory and non-contradictory prompts.
3. Capture selected hidden states.
4. Calculate basic representational distances.
5. Compare behavioural and representational changes under A and B.
6. Generate reproducible results and a concise experimental report.

Do not begin large-scale testing or multi-model comparisons before this
experiment works.

## 10. Success Criteria

The initial project succeeds when it can reproducibly determine whether a
defined semantic conflict produces a detectable internal representational
difference under controlled conditions.

The wider project succeeds only if it can establish which relationships
between semantic conflict, measured geometry and model behaviour are supported,
unsupported or unresolved.

**Final governing principle:**

The purpose is not to demonstrate that embedding-space curvature corresponds
to semantic contradiction.

The purpose is to determine whether that relationship exists, how strongly,
under which conditions, and what evidence would invalidate it.
