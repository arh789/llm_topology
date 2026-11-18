# What each run is optimising for

The 20 runs are not all optimising the same thing. They progressively change the research target: first making internal representations measurable, then reconstructing semantic relationships, testing whether those relationships survive perturbation, and finally investigating whether recoverable semantic structure is successfully integrated into generated answers.

Here, **optimising for** means the information each experiment is designed to recover or the uncertainty it is designed to eliminate. It does not mean the model's training objective or a parameter being optimised mathematically.

## 1. R001–R010: From measurements to semantic reconstruction

*Model: Pythia 6.9B · Primary concept: lithium*

| Run | What it optimises for |
|---|---|
| **R001** | **Observability.** Establish that the model's internal states can be captured across transformer depth and that a target token's representational trajectory can be inspected. |
| **R002** | **Vocabulary-wide coverage and boundary detection.** Project the target's contextual state against the complete static vocabulary basis; test whether meaningful positive-region cut-offs can be identified reproducibly. The original strict consensus test accepted none. |
| **R003** | **Boundary discrimination.** Distinguish strongly aligned, central and anti-aligned token populations using upper and lower score-distribution boundaries, with explicit stability criteria. |
| **R004** | **Complete population selection.** Remove R003's additional acceptance gate and use both full-curve elbows at every state, ensuring that positive and negative populations exist for subsequent structural analysis. |
| **R005** | **Relational structure beyond random selection.** Determine whether selected tokens form distinctive neighbourhoods and communities compared with size-matched random populations. |
| **R006** | **Independent positive/negative networks and interpretability.** Export separate networks with sufficient community-level evidence for ChatGPT to reconstruct them. Failed during network processing. |
| **R007** | **Recoverable execution.** Correct R006's processing failure while preserving the same analytical objective. Network construction completed, but final validation failed because embedded newlines were incorrectly counted as extra CSV records. |
| **R008** | **Validated, inspectable network evidence.** Complete R006–R007's intended export, with correct validation and traceability across 66 networks. |
| **R009** | **Semantic identification.** Determine what each of the 792 measured community instances represents, distinguishing semantic topics from lexical, numeric, formatting and mixed structures before making higher-order claims. |
| **R010** | **Higher-order reconstruction and structural evolution.** Infer the smallest defensible semantic parents and relationships explaining the communities; compare their evolution across layers and investigate coherence, conflict and reorganisation. |

### What changes across these runs?

```text
R001       Can internal states be observed?
  |
R002–004   Which vocabulary regions are selected?
  |
R005       Do those regions form meaningful networks?
  |
R006–008   Can those networks be exported reliably?
  |
R009       What do the communities represent?
  |
R010       What higher-order relationships organise them?
```

R010 is the first major change in what is being reconstructed. The earlier runs predominantly optimise measurement and classification. R010 begins optimising for **explanatory structure**: a representation that can account for how the observed communities are organised and reorganised.

Its Phase D also introduces a finding that becomes relevant again in R020: conflict may be resolved through repartitioning and changing relationships, rather than eliminating competing information.

## 2. R011–R015: From a local map to controlled semantic invariance

*Transition from Pythia to Qwen 2.5 7B · Controlled changes to concept order and context*

| Run | What it optimises for |
|---|---|
| **R011** | **Model-scale feasibility and whole-prompt capture.** Test whether a 70B–72B quantised model can expose every intermediate state while remaining in system RAM, and support comparison between minimally different prompts. Failed at the runtime instrumentation stage. |
| **R012** | **Generalisation and paired-prompt comparison.** Establish a complete pipeline that measures the final-position representation of a whole prompt rather than a selected concept token. Successfully generates comparable networks for two concept orders. |
| **R013** | **Order invariance.** Remove the synthesis instruction and test all six permutations of *electro pink*, *curvature density* and *Tokyo nightlife*. Identify which token populations and graph relationships survive reordering. |
| **R014** | **Context invariance and local semantic reconstruction.** Use overlapping concept triplets to test whether the same semantic parents and relations recur despite changes to both ordering and surrounding context. |
| **R015** | **Local topological continuity.** Replace every R014 seed with a neighbouring concept while preserving the measurement method. Determine whether the reconstructed map persists, deforms, splits or terminates when the observation window moves. |

The central progression is:

```text
R012   Same prompt concepts, changed order
  |
R013   Same three concepts, all six orders
  |
R014   Four overlapping concept contexts
  |
R015   Entire concept set replaced by neighbours
```

The experiments progressively remove explanations based on the particular words and arrangements used in the original input.

R015 is especially significant because it independently recovers counterparts of all six R014 semantic parent families, even after replacing all four original seed concepts. However, their relationships change, particularly around the process/modification and spatial families.

**The optimisation target has shifted from detecting structure to identifying which structures survive controlled changes to the observation window.**

Sources: [R013 plan](single_prompt_topology/R013_PLAN.md), [R014 plan](single_prompt_topology/R014_PLAN.md), [R014–R015 comparison](single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R014_R015_COMPARISON.md).

## 3. R016–R019: Larger model, distant region and falsification controls

*Model: OLMo 3 32B Base · Concepts: choke point, collapsible barrier, spear*

| Run | What it optimises for |
|---|---|
| **R016** | **Instrumentable model capacity.** Establish whether a substantially larger, fully open base model can be run locally with native BF16 weights, using GPU, RAM and disk offloading. Successful feasibility test, not a semantic experiment. |
| **R017** | **Semantic reconstruction in a different region.** Apply the established pipeline to a new concept set and infer its higher-order functional structure. Produces a candidate tactical-interception map, but tests only one input ordering. |
| **R018** | **Perturbation-stable semantic structure.** Run all six orders of R017's concepts to distinguish persistent semantic parents from order-conditioned relationships and interpretations. |
| **R019** | **Elimination of a measurement confound.** Repeat identical inputs and compare them with different input orders, establishing whether the observed variation comes from concept order rather than runtime instability. |

The distinction between R017 and R018 is particularly revealing.

R017 optimises for **recovering the most coherent evidence-supported map from one trajectory**. R018 optimises for **determining how much of that map survives when the input is rearranged**.

R017's tactical interpretation was more specific than R018's permutation-stable result could support. R018 recovered recurring semantic families but found that their relationships and emphasis remained strongly order-conditioned.

R019 then established an exact repeatability baseline under the tested conditions. The order effects were reproducible, not artefacts of variable forward-pass behaviour.

Consequently, these runs progressively separate **the coherence of an interpretation** from **the stability of the measured structure supporting it**.

Sources: [R017 reconstruction](single_prompt_topology/runs/R017_olmo3-choke-point-barrier-spear-semantic-map/R017_SEMANTIC_RECONSTRUCTION.md), [R018 reconstruction](single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md), [R019 control results](single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md).

## 4. R020: From recoverable structure to useful information

*Model: Pythia 70M · 32 generated-token decisions · 8 states per decision*

| Run | What it optimises for |
|---|---|
| **R020** | **Separating semantic availability, integration and expression.** Determine whether a very small model contains recoverable semantic relationships that exceed the usefulness of its generated response, and whether a higher-order organising hypothesis persists across successive generated tokens. |

R020 changes two important experimental dimensions.

First, it deliberately reduces model capacity rather than increasing it. This makes poor generated output a useful experimental condition.

Second, it tracks the representation through **generation time as well as transformer depth**.

R020 therefore asks a question that R001–R019 cannot directly answer:

**What information does the model appear to possess, what relationships does it successfully integrate, and what does it finally express?**

Its current conclusion distinguishes recoverable semantic associations from a fully integrated hypothesis. Relevant structures recur, but their roles are not consistently assembled into a successful explanation.

Source: [R020 final conclusion](single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/R020_FINAL_CONCLUSION.md).

---

## 5. What the complete sequence is optimising for

Across all twenty runs, I identify five progressively stronger research targets.

### Project optimisation trajectory

```text
R001–R008
MEASUREMENT RELIABILITY
Can the information be captured and structured?
           |
           v
R009–R010
SEMANTIC INTERPRETABILITY
Can the structures and their relations
be reconstructed?
           |
           v
R011–R015
STRUCTURAL GENERALISATION
Do the structures survive changes
to context and observation position?
           |
           v
R016–R019
ROBUSTNESS AND FALSIFICATION
Do the findings survive larger-model
instrumentation, order controls
and repeatability tests?
           |
           v
R020
INFORMATIONAL UTILITY
Can recoverable semantic information
exceed what the model can successfully
integrate and express?
```

### The optimisation trade-offs

| Optimisation target | What it improves | What can be lost |
|---|---|---|
| Measurement coverage | More observable tokens, communities and relationships | Interpretability |
| Semantic compression | Fewer, more comprehensible parent structures | Important intermediate relationships |
| Invariance | Stronger confidence that a structure survives perturbation | Context-dependent but informative structures |
| Functional integration | More useful explanations of how concepts relate | Contradictions, competing interpretations and residual evidence |
| Generative expression | A concise, coherent answer | Access to alternative or unexpressed semantic relationships |

This exposes a tension running through the project.

**The most stable structure is not necessarily the most informative structure. The most coherent interpretation is not necessarily the most accurate reconstruction. And the most fluent generated response is not necessarily the richest representation of what the model has learned.**

## 6. The inferred project-level objective

The original project objective was to infer learned semantic topology from transformer-state changes.

That objective remains intact. But the experimental sequence has revealed that recovering a semantic network is only part of the problem.

There are now three distinct questions:

1. **Availability:** What higher-order semantic structures can be inferred from the model's representations?
2. **Integration:** Under what conditions are those structures organised into coherent functional relationships?
3. **Expression:** Under what conditions does the model successfully use those relationships to generate an answer?

R001–R019 predominantly investigate the first question, including the reliability and stability of the reconstruction. R010 also begins examining integration through coherence and structural reorganisation.

R020 makes the distinction between all three explicit.

### The central inference

The project has progressively been optimising for **recovering usable semantic relationships without mistaking measurement stability, interpretive coherence or output fluency for semantic understanding**.

There is also a methodological consequence. The agent must expose enough of the network for a human to judge which relationships matter, rather than selecting only those relationships that make its own explanation coherent.

That connects the experimental progression directly to MA-0126: semantic integration is simultaneously a property being investigated and a challenge encountered while interpreting the evidence.

**The strongest overall conclusion is that the project is no longer merely about mapping learned semantic space. It is becoming an investigation into the conditions under which recoverable semantic structure becomes useful information.**
