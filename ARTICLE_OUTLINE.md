# Article Outline

> Working source collection for the project article. The responses below are reproduced verbatim from the recent project discussion and arranged chronologically. Prompts are retained to preserve the context in which each outline, argument, control, or evidence plan was produced. This file is source material, not yet a consolidated article draft.

## 1. Project trajectory and migrating binding constraints

**Recorded:** 17/11/2026, 02:07:35 AEDT  
**Source turn:** `01a1e4e6-3977-72f3-9946-4ebc2cdafb73`

### Prompt

inspect the folders for each run. what need did each run solve? what binding constraint was each run optimising for? what trakectory emerged across all the runs?


### Response

The 18 runs form a clear progression: from proving that layer states could be captured, through constructing and interpreting semantic networks, to testing which higher-order structures survive controlled deformation of the input.

The current binding constraint is no longer model execution or graph construction. It is **identifiability**: determining which parent structures—and eventually which relations between them—recur across sufficiently different prompts and semantic regions to justify treating them as learned training-data topology.

## What each run accomplished

“Binding constraint” below means the principal bottleneck the run was designed around, whether computational, methodological, or epistemic.

| Run | Need addressed | Binding constraint it optimized for | What it unlocked |
|---|---|---|---|
| **R001** | Prove that the target’s representation could be captured across every transformer state. | Local VRAM and basic instrumentability: one Pythia 6.9B prompt, one final target position, 33 states. | The first reproducible hidden-state trajectory and evidence package. |
| **R002** | Project every state against the full input vocabulary and determine whether a usable neighbourhood cutoff existed. | The 50,277-token vocabulary was too large to inspect directly; no additional forward pass should be required. | Full-vocabulary score matrices and the discovery that the initial cutoff-acceptance criteria rejected every state. |
| **R003** | Treat the positive head and negative tail as separate geometric regions. | One undifferentiated cutoff could not represent the asymmetric score distribution; negative cosine could not be assumed to mean suppression. | Explicit upper and lower populations, while exposing the instability and unnecessary complexity of cutoff acceptance rules. |
| **R004** | Remove the “cutoff shenanigans” and create deterministic populations at every state. | Secondary acceptance tests were preventing a simple geometric elbow from being used consistently. | Two unconditional full-curve cutoffs for all 33 states and a stable membership dataset. |
| **R005** | Establish whether the selected populations contained non-random topology. | A cutoff alone did not show that the selected tokens formed meaningful structure; population size required a null control. | Exact k-NN graphs, Louvain communities, random baselines and cross-layer topology comparisons. |
| **R006** | Export separate positive and negative networks in a form ChatGPT could inspect. | Millions of raw edges were analytically unusable; token and dataframe identity had to remain stable. | A useful failure: it exposed an ambiguous pandas-index bug before valid networks were produced. |
| **R007** | Retry the complete compact-network export after fixing R006. | Validation had to distinguish real CSV records from physical lines containing embedded tokenizer newlines. | All computations completed, but the false validation failure exposed the logical-record counting defect. |
| **R008** | Produce a validated, compact, ChatGPT-readable measured evidence package. | Preserve complete provenance while reducing 1.9 million edges into inspectable community networks. | 66 networks and 792 communities, with compact JSON and layer packets suitable for external interpretation. |
| **R009** | Answer the first descriptive question: “What is each community?” | 792 communities were too many to interpret globally, and SDA-3 assumptions could contaminate classification. | A complete state-local semantic classification, deliberately performed before cross-layer synthesis or role assignment. |
| **R010** | Reconstruct parent structures, cross-layer trajectories, coherence difficulty and conflict resolution. | Community IDs were state-local; semantic evolution could not be inferred by naïvely matching labels or IDs. Geometric, partition and semantic change also had to remain distinct. | A staged account of differentiation, repartition, abstraction, selective compression and late functional organisation. |
| **R011** | Move from one contextualized concept to a controlled whole-prompt representation. | The runtime had to expose every intermediate hidden state. `llama.cpp` and the available TorchAO path could not do that. | A useful failed run that eliminated the wrong runtime path; it did not establish a hardware limitation. |
| **R012** | Correct R011 using Hugging Face Transformers and complete the whole-prompt topology pipeline. | Intermediate-state access and GPU fit; later, the realization that capture alone was not a successful topology run. | A reproducible Qwen 7B paired-prompt pipeline extending from capture through communities and ChatGPT-readable exports. |
| **R013** | Remove the synthesis instruction, chat template and assistant prefix, then test all orders of the same bare concepts. | R012 mixed concept topology with instruction-following and response-preparation effects. A fixed neutral anchor still required order controls. | The first clean six-permutation result: exact tokens and edges were order-sensitive, while higher-order parents were much more stable. |
| **R014** | Test whether candidate relations survived changes in third-concept context, not merely word order. | A three-concept experiment cannot separate a pairwise relation from its only surrounding context. | A balanced four-concept, four-probe design in which every pair appeared under two contexts, producing the first local semantic map. |
| **R015** | Move the observation window to adjacent concepts and test whether R014’s map persisted. | R014’s topology might have been an artefact of its literal seed concepts. The instrument had to remain unchanged while every concept changed. | Local continuity with deformation: all six parent families reappeared, including unsupplied process and information structures. |
| **R016** | Determine whether OLMo 3 32B Base could act as a larger open training-data abstraction locally. | The model exceeded VRAM; the test had to use GPU, CPU RAM and disk offload while performing only one first-token forward pass. | Proof that all 65 hidden states and logits could be captured locally in native BF16. |
| **R017** | Run the complete topology and semantic-reconstruction workflow on OLMo 3 32B. | Network construction at 32B scale was expensive, so the first run remained a single prompt in one order. | A complete measured and interpreted 32B semantic map—but one with no order or context invariance evidence. |
| **R018** | Test the R017 concept set under all six orders and separate stable learned structure from presentation effects. | Severe final-position conditioning, 30.8 million edges, validation integrity, and the danger of compressing the result into an overly simple graph. | Strong early/middle order divergence followed by late reconvergence. Higher-order semantic families survive better than exact tokens, communities or relations; one fixed invariant graph is not yet established. |

## The trajectory across the runs

```text
R001
CAN INTERNAL STATES BE CAPTURED?
        ↓
R002–R004
WHICH VOCABULARY REGIONS SHOULD BE RETAINED?
        ↓
R005
DO THOSE REGIONS CONTAIN NON-RANDOM TOPOLOGY?
        ↓
R006–R008
CAN THE TOPOLOGY BE VALIDATED AND MADE INSPECTABLE?
        ↓
R009
WHAT IS EACH COMMUNITY?
        ↓
R010
HOW DO COMMUNITIES FORM PARENTS AND EVOLVE THROUGH DEPTH?
        ↓
R011–R012
CAN THE WHOLE PROMPT BECOME THE MEASURED OBJECT?
        ↓
R013
WHAT SURVIVES INPUT-ORDER PERTURBATION?
        ↓
R014
WHAT SURVIVES THIRD-CONCEPT CONTEXT CHANGES?
        ↓
R015
WHAT SURVIVES MOVEMENT INTO ADJACENT SEMANTIC SPACE?
        ↓
R016–R017
CAN THE SAME INSTRUMENT OPERATE ON A LARGER OPEN BASE MODEL?
        ↓
R018
DOES THE 32B REPRESENTATION CONTAIN A
PERTURBATION-STABLE SEMANTIC BASIS?
```

Three deeper trajectories emerged.

### 1. The useful unit of analysis moved upward

```text
target token
    ↓
vocabulary scores
    ↓
selected populations
    ↓
token networks
    ↓
communities
    ↓
semantic parents
    ↓
relations between parents
```

The lower levels proved highly plastic. Tokens, edges and community partitions change substantially with order and context. Parent families are more stable. Parent-parent relations appear less stable than the parents themselves.

That means the current evidence supports a **stable semantic basis** more strongly than a single invariant semantic graph.

### 2. The layer trajectory is differentiation followed by reconvergence

The recurring pattern is not a representation becoming steadily clearer:

```text
COMMON INPUT BASIS
        ↓
early contextual selection
        ↓
middle-layer differentiation and repartition
        ↓
higher-order abstraction
        ↓
late reconvergence into output-compatible structure
```

R018 makes this especially visible. Identical concept sets form sharply different early and middle organisations depending on the final concept, but their late states become substantially more similar.

The transformer therefore appears to preserve several context-conditioned organisations before compressing them into a more reusable higher-order basis.

### 3. The binding constraint kept migrating

```text
VRAM / capture
    ↓
neighbourhood selection
    ↓
graph construction
    ↓
data validation
    ↓
LLM-readable evidence
    ↓
interpretive bias
    ↓
runtime hidden-state access
    ↓
prompt and position confounds
    ↓
order and context invariance
    ↓
semantic over-compression
    ↓
cross-region identifiability
```

This is important: the project did not simply improve one pipeline. Each run removed the current limiting assumption and exposed the next one.

## The overall scientific result

The runs increasingly support the project’s fundamental hypothesis in a constrained form:

> Changes through transformer depth can expose higher-order semantic organisation learned during training, and controlled perturbations can help separate that organisation from presentation-dependent structure.

But they also establish a boundary:

> The evidence currently supports persistent semantic components or parent families more strongly than it supports one persistent topology of relations between them.

So the model is not revealing one static semantic map hidden inside it. A better emerging picture is:

```text
LEARNED SEMANTIC BASIS
        +
CONTEXT-CONDITIONED RELATIONS
        +
LAYERWISE DIFFERENTIATION
        +
LATE RECONVERGENCE
```

The current binding constraint is therefore **cross-region replication**. R014–R015 establish local continuity, and R018 establishes order-robust higher-order structure for one OLMo concept set. What remains unresolved is whether independently chosen, genuinely distant semantic regions recover recurrent parents and recurrent relations strongly enough to support a broader inferred topology of the learned training data.

The main project account is indexed in [single_prompt_topology/README.md](</D:/Sync/Python Projects/llm_topology/single_prompt_topology/README.md:1>), with the Qwen perturbation sequence beginning at [R011](</D:/Sync/Python Projects/llm_topology/single_prompt_topology/README.md:275>), the adjacent-region replication defined in [R015_PLAN.md](</D:/Sync/Python Projects/llm_topology/single_prompt_topology/R015_PLAN.md:12>), and the present project-level R018 conclusion in [R018_FINAL_REPORT.html](</D:/Sync/Python Projects/llm_topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_FINAL_REPORT.html:137>).

---

## 2. Practical value framed through SDA-3

**Recorded:** 17/11/2026, 04:58:09 AEDT  
**Source turn:** `01a1e582-5f26-7b52-b737-48a71910ed1a`

### Prompt

How is this information useful? Why is this information useful? What is the practical benefit in being able to identify a models learned associations on a given topic, or identify what associations a model is drawing from when generating a prompt?

Respond in sda3 format

### Response

## SDA-3: Practical value of learned-association analysis

### C — Central

The central benefit is that it reveals the **semantic frame organising the model’s answer**.

An output tells you what the model said. The association map can indicate:

- what interpretation it treated as primary;
- which concepts it used to organise the topic;
- what higher-order relationships shaped the answer;
- whether the prompt activated the intended meaning.

This separates two useful objects:

```text
LEARNED TOPOLOGY
What the model generally associates with the topic

ACTIVE TOPOLOGY
Which of those associations this prompt recruited
```

The difference makes model behaviour more diagnosable and controllable.

Practical uses include prompt refinement, answer auditing, retrieval selection, training-data investigation and identifying stable semantic structures learned during training.

### S — Suppressed

This identifies plausible interpretations or evidence that progressively lose influence relative to the dominant frame.

That is useful because many model failures are failures of omission:

- an alternative explanation is not considered;
- contradictory evidence disappears;
- one meaning of an ambiguous concept dominates;
- a minority or unusual perspective is displaced;
- an inconvenient constraint is underrepresented.

Once identified, the supposedly suppressed structure can be explicitly reintroduced:

```text
dominant answer
      ↓
identify displaced alternative
      ↓
add targeted evidence or adversarial question
      ↓
observe whether the topology and answer change
```

This creates a practical method for testing bias, incompleteness and robustness.

However, geometric anti-alignment alone does not prove suppression. Suppression requires a coherent, relevant alternative that demonstrably loses influence.

### A — Adjacent

Adjacent structures are relevant to the topic but do not determine the answer.

They are useful for identifying:

- contextual factors that deserve acknowledgement;
- related domains that may improve the answer;
- bridges between otherwise separate concepts;
- secondary considerations that should not be allowed to dominate.

This helps control scope. An adjacent association can either be incorporated when useful or deliberately left peripheral.

For research and creative work, adjacent structures are particularly valuable because they expose meaningful relationships the user may not have initially considered.

### HCU — Highly Correlated Unrelated

HCU identifies strongly represented associations that do not contribute to the developing explanation.

These can arise from:

- repeated corpus co-occurrence;
- lexical or morphological similarity;
- famous names or places;
- cultural stereotypes;
- tokenizer effects;
- domain associations that are statistically strong but irrelevant here.

This category helps distinguish:

```text
strong association
        ≠
useful evidence
```

Its practical value is substantial. HCU structures can explain irrelevant digressions, stereotyped responses, false analogies and confident hallucinations.

Detecting them allows the system to exclude correlated residue before it contaminates the conclusion.

### E — Emerging

Emerging structures begin peripherally but gain influence as processing proceeds or as the prompt changes.

They reveal:

- where the model’s interpretation is heading;
- which weak association may become decisive;
- why a minor wording change produces a different answer;
- which new evidence could reorganise the semantic frame;
- where the representation is unstable or underspecified.

This provides an early-warning system for prompt sensitivity.

If a potentially undesirable interpretation is emerging, the prompt can be clarified before it dominates. If a valuable interpretation is emerging, additional context can strengthen it.

## Practical synthesis

```text
C — What is constructing the answer?

S — What plausible alternative is being displaced?

A — What matters without determining the answer?

HCU — What is strongly associated but functionally irrelevant?

E — What is becoming increasingly influential?
```

Together, these categories turn association analysis into an intervention system:

```text
MEASURE ASSOCIATIONS
        ↓
IDENTIFY STRUCTURAL ROLES
        ↓
DIAGNOSE THE ANSWER'S FRAME
        ↓
ADD, REMOVE OR REWEIGHT CONTEXT
        ↓
RUN AGAIN
        ↓
TEST WHETHER THE ANSWER IMPROVES
```

The practical applications are therefore:

- **Prompt control:** understand why small wording or ordering changes redirect the answer.
- **Reliability:** detect omitted alternatives and irrelevant correlations.
- **Bias auditing:** identify which interpretations dominate and which consistently recede.
- **Retrieval augmentation:** supply the missing evidence most likely to correct the active structure.
- **Training and fine-tuning:** distinguish persistent learned associations from prompt-specific effects.
- **Semantic mapping:** aggregate perturbation-stable parent structures to infer the higher-order topology learned from training data.
- **Agent oversight:** compare the semantic structure required by the task with the structure actually organising the answer.

The deepest benefit is not simply explaining an answer after it has been generated. It is discovering **which semantic organisation produced the answer and what intervention could produce a better one**.

The defensible claim is not that this recovers literal thoughts or exact training documents. Individual tokens and edges are often highly prompt-sensitive. The strongest evidence comes from higher-order structures that survive controlled changes in wording, order and context.

---

## 3. Order sensitivity versus stochastic instability

**Recorded:** 17/11/2026, 05:36:03 AEDT  
**Source turn:** `01a1e5a5-1452-7ff2-a515-ea0f3d76c436`

### Prompt

Is the order of tokens producing different distributions or samples, or is it a case of the model being inherently unstable if not at a sufficient level of sophistication, and the same prompt would inherently return different token distributions if a hard seed isn’t enforced?

### Response

In these runs, **token order is producing different contextual representations and score distributions**. It is not sampling instability: the pipeline performs a forward pass and captures hidden states without sampling a generated token.

The distinction is:

```text
Different token order
        ↓
different attention relationships and positional encoding
        ↓
different hidden states
        ↓
different semantic-neighbourhood scores
        ↓
generally different next-token distributions
```

Versus:

```text
Identical prompt
        ↓
same hidden states and logits
        ↓
stochastic sampler
        ↓
potentially different selected tokens
```

A seed controls the second process—the random selection from a distribution. It does not normally change the distribution produced by the initial forward pass.

### What should happen with the identical prompt?

With:

- identical token IDs;
- identical model weights;
- `eval()` mode, so dropout is disabled;
- identical numerical backend;
- no autoregressive sampling;

the hidden states and initial token distribution should be identical, or differ only by negligible GPU numerical nondeterminism. A hard seed should not be necessary.

If stochastic generation is enabled, the first distribution remains the same, but different tokens can be sampled:

```text
same first-token distribution
        ├─ sample token X
        │       ↓
        │  subsequent distribution X
        │
        └─ sample token Y
                ↓
           subsequent distribution Y
```

Once different tokens are selected, the generation trajectories diverge.

### What the permutation results mean

The permutations are different prompts at the token-sequence level, even though they contain the same concepts:

```text
choke point | collapsible barrier | spear
spear | choke point | collapsible barrier
```

Causal transformers are inherently order-sensitive. Each position can attend only to its prefix, and the concept immediately before the capture anchor has a privileged positional relationship to it.

The observed pattern therefore indicates:

- early and middle layers strongly organise around token order and the final concept;
- different orders produce different local semantic organisations;
- later layers partially reconverge on common higher-order semantic families;
- the invariant parent families are more stable than their exact tokens, edges or relations.

This is **structured order sensitivity**, not random instability.

### Does model sophistication matter?

Potentially, but it is not the primary explanation.

A more capable model might:

- abstract away from superficial order more effectively;
- reconverge more strongly in later layers;
- preserve a more stable higher-order structure;
- show a weaker final-position bias.

But even a highly capable model should not be completely order-invariant, because order can change meaning. Complete invariance would itself be undesirable.

### The decisive test

The pipeline should include a replicate control:

```text
1 exact prompt
×
multiple identical forward passes
×
no sampling
```

Then compare hidden states, neighbourhood scores and logits.

- **Identical repeats, divergent permutations:** genuine order-conditioned topology.
- **Divergent identical repeats before sampling:** runtime or pipeline nondeterminism.
- **Identical distributions but different generated tokens:** ordinary stochastic sampling.
- **Different distributions only after different tokens are sampled:** normal autoregressive branching.

So the current evidence points to **different deterministic semantic distributions caused by order**, not an insufficiently sophisticated model randomly producing different representations because no seed was enforced.

---

## 4. Proposed repeatability control

**Recorded:** 17/11/2026, 06:30:06 AEDT  
**Source turn:** `01a1e5d6-8e5d-7340-9237-314f990c0555`

### Prompt

Should we perform an additional run, with three permutations of the previous prompt each repeated three times, then test for some form of divergence?

### Response

Yes. This is the correct control experiment, and it should remain deliberately narrow.

Let:

- A = `choke point`
- B = `collapsible barrier`
- C = `spear`

Use the balanced cyclic permutations:

```text
ABC — choke point | collapsible barrier | spear
BCA — collapsible barrier | spear | choke point
CAB — spear | choke point | collapsible barrier
```

This places every concept once in each position. Run each permutation three times independently, producing nine captures.

Do not generate or sample tokens. Use the same model, precision, anchor, tokenizer, pipeline and settings as R018. Fix the seed used by community detection so Louvain randomness cannot masquerade as model instability.

For every transformer state, calculate:

```text
WITHIN-PROMPT DIVERGENCE
differences among three identical repeats

BETWEEN-ORDER DIVERGENCE
differences among the three permutations
```

Compare:

- hidden-state cosine and maximum absolute difference;
- vocabulary-score RMSE and rank correlation;
- positive/negative membership Jaccard;
- edge Jaccard;
- community ARI;
- actual next-token Jensen–Shannon divergence, if final logits are saved.

The central statistic is:

```text
order divergence
────────────────────────
repeat divergence + ε
```

### Successful result

```text
identical repeats
    → zero or negligible divergence

different permutations
    → materially larger divergence
```

This would establish that the R018 differences are genuine, deterministic order effects rather than stochastic instability.

### Diagnostic failure modes

```text
Raw hidden states differ between repeats
    → model/runtime numerical nondeterminism

Hidden states stable, selected tokens differ
    → cutoff sensitivity

Token membership stable, edges differ
    → graph-construction sensitivity

Graphs stable, communities differ
    → community-detection randomness or degeneracy
```

If repeat divergence approaches permutation divergence, the earlier semantic conclusions require qualification.

Three permutations repeated three times are sufficient for this control. Repeating all six would add cost without materially improving the immediate test. This run would establish a **measurement noise floor** against which all subsequent order and context effects can be judged.

---

## 5. R019 repeatability-control findings

**Recorded:** 17/11/2026, 06:31:12 AEDT  
**Source turn:** `01a1e5d7-92d7-79d1-a654-7898d7d270f2`

### Prompt

Proceed

### Response

R019 completed successfully. The result is unambiguous: **the differences are deterministic order effects, not instability caused by an unenforced sampling seed.**

Key findings:

- Identical prompts produced bit-for-bit identical hidden states across all 65 states.
- Vocabulary-score vectors and final next-token logits were identical.
- Cutoff memberships, 10-NN edges and seeded communities were identical.
- Within-repeat divergence was exactly zero.
- No tokens were generated or sampled.

Different concept orders produced:

- Minimum hidden-state cosine: `0.609119475`
- Maximum next-token Jensen–Shannon divergence: `0.052628301`
- Minimum membership Jaccard: `0.158392029`
- Minimum edge Jaccard: `0.041658627`

The strongest divergence was `ABC` versus `BCA` around Blocks 14–15.

Therefore:

```text
same ordered prompt
    → same internal states
    → same next-token distribution
    → same topology

different order
    → different contextual processing
    → different next-token distribution
    → different topology
```

A seed would only control which token is sampled from a distribution. It is not needed to stabilise the forward-pass distribution measured here.

The run, all 18 indexed artifact hashes, and 12 regression tests passed:

- [R019 measurement report](<D:/Sync/Python Projects/llm_topology/single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_MEASUREMENT_REPORT.md>)
- [Machine-readable result](<D:/Sync/Python Projects/llm_topology/single_prompt_topology/runs/R019_olmo3-order-repeatability-control/R019_RESULT.json>)
- [R019 plan](<D:/Sync/Python Projects/llm_topology/single_prompt_topology/R019_PLAN.md>)

The result and methodology are recorded as MA-0117. Large replay tensors remain local; compact evidence is ready to commit. Nothing has been committed or pushed yet.

---

## 6. Intermediate-layer repeat divergence

**Recorded:** 17/11/2026, 07:19:21 AEDT  
**Source turn:** `01a1e603-a810-7730-9bce-27fa736e2830`

### Prompt

When passing through the intermediate transformer layers in the last run, for repeated runs of the same permutation was there any divergence?

### Response

No. Each permutation was run three times, and the repeated trajectories were **bit-for-bit identical at every recorded state**:

- Input embedding
- All 64 transformer-layer outputs
- Final normalisation
- Vocabulary-score distributions
- Final next-token logits
- Cutoff memberships, edges and communities

Across all 585 within-permutation layer comparisons:

```text
maximum absolute difference = 0
L2 distance                = 0
cosine distance            = 0
```

So no intermediate-layer divergence was detected. This establishes reproducibility across sequential forward passes in the same loaded model/runtime. It does not yet test reproducibility across separate process launches, hardware or numerical backends.

---

## 7. Constraint-driven article structure

**Recorded:** 17/11/2026, 07:21:52 AEDT  
**Source turn:** `01a1e605-f37a-7140-b664-27ae74968bc9`

### Prompt

The deepest benefit is not simply explaining an answer after it has been generated. It is discovering which semantic organisation produced the answer and what intervention could produce a better one.

—-

If this was part of the opening for a blog article about this project, given the outlined trajectory and the binding constraints outlined immediately prior, what would the structure of the article be, in ascii tree diagram form

### Response

I would structure it as a constraint-driven investigation rather than a chronological run log:

```text
WORKING TITLE

THE HIDDEN MAP BEHIND AN AI ANSWER
How transformer layers expose learned associations—and how those
associations might be changed before the model responds


ARTICLE
│
├── OPENING — FROM EXPLANATION TO INTERVENTION
│   │
│   ├── Epigraph / central claim
│   │
│   │   “The deepest benefit is not simply explaining an answer
│   │    after it has been generated. It is discovering which
│   │    semantic organisation produced the answer and what
│   │    intervention could produce a better one.”
│   │
│   ├── Concrete problem
│   │   │
│   │   ├── A model produces a fluent answer
│   │   ├── The answer reveals its conclusion
│   │   └── It does not reveal the semantic frame that selected it
│   │
│   ├── Practical question
│   │
│   │   What was treated as central?
│   │   What was left peripheral?
│   │   What competing interpretation lost influence?
│   │   What irrelevant association remained active?
│   │
│   └── Article thesis
│
│       If the active semantic organisation can be measured,
│       it may become possible to intervene before or during
│       answer construction rather than merely criticising
│       the completed output.
│
├── 1. THE OBJECT BEING MEASURED
│   │
│   ├── Not literal thoughts
│   ├── Not a hidden natural-language monologue
│   ├── Not recovery of particular training documents
│   │
│   └── Instead
│       │
│       ├── learned associations encoded by training
│       ├── prompt-conditioned activation of those associations
│       ├── changing relationships across transformer depth
│       └── the higher-order structures that survive perturbation
│
│       TRAINING DATA
│             ↓
│       MODEL COMPRESSES RECURRING RELATIONS
│             ↓
│       CONTROLLED PROMPT
│             ↓
│       LAYERWISE INTERNAL STATES
│             ↓
│       MEASURED SEMANTIC TOPOLOGY
│
├── 2. WHY THE OUTPUT ALONE IS INSUFFICIENT
│   │
│   ├── Similar answers can arise from different semantic frames
│   ├── A correct answer can conceal omitted alternatives
│   ├── A fluent rationale can be reconstructed after generation
│   ├── Prompt changes can alter the answer without explaining why
│   └── Output evaluation detects failure only after selection occurred
│
│       OUTPUT ANALYSIS
│       “What did the model say?”
│
│                       versus
│
│       TOPOLOGY ANALYSIS
│       “What semantic organisation made this answer likely?”
│
├── 3. THE BINDING CONSTRAINTS THAT SHAPED THE PIPELINE
│   │
│   ├── OBSERVABILITY
│   │   └── Use an open model whose intermediate states can be captured
│   │
│   ├── HARDWARE
│   │   └── One short forward pass must fit a local RTX 4090 system
│   │       using GPU, CPU and disk offloading where necessary
│   │
│   ├── SELECTION
│   │   └── Full vocabularies are too large
│   │       → identify positive and negative score regions
│   │       → use measured elbows rather than arbitrary top-k choices
│   │
│   ├── SCALE
│   │   └── Individual tokens are too unstable and numerous
│   │       → tokens
│   │       → edges
│   │       → communities
│   │       → parent structures
│   │
│   ├── INTERPRETATION CONTAMINATION
│   │   └── Do not impose SDA-3 or desired topic labels during measurement
│   │       → measure first
│   │       → reconstruct independently
│   │       → interpret afterwards
│   │
│   ├── PROMPT CONTAMINATION
│   │   └── Instruction shells such as “What structure forms from…”
│   │       contribute their own semantics
│   │       → bare concepts
│   │       → fixed neutral anchor
│   │
│   ├── POSITIONAL CONFOUNDING
│   │   └── The final concept receives privileged causal proximity
│   │       → test every order
│   │       → compare invariant and order-conditioned structure
│   │
│   └── STOCHASTICITY
│       └── Apparent permutation effects could be runtime instability
│           → repeat identical prompts
│           → establish the measurement noise floor
│
├── 4. HOW THE EXPERIMENT EVOLVED
│   │
│   ├── R001–R004 — CAN THE SCORE LANDSCAPE BE MEASURED?
│   │   │
│   │   ├── capture representations across layers
│   │   ├── project them against the vocabulary
│   │   └── determine defensible positive and negative boundaries
│   │
│   ├── R005–R008 — DOES THE LANDSCAPE CONTAIN STRUCTURE?
│   │   │
│   │   ├── construct token-neighbour graphs
│   │   ├── detect communities
│   │   ├── compare layers
│   │   └── export evidence for independent interpretation
│   │
│   ├── R009–R010 — WHAT ARE THE COMMUNITIES DOING?
│   │   │
│   │   ├── classify communities without imposing SDA-3
│   │   ├── reconstruct parent structures
│   │   ├── track splitting, merging and reorganisation
│   │   └── distinguish measurement from semantic interpretation
│   │
│   ├── R011–R012 — CAN THE WHOLE PROMPT BECOME THE UNIT?
│   │   │
│   │   ├── move beyond one contextualised target word
│   │   ├── capture the whole-prefix decision state
│   │   └── expose the instruction-shell confound
│   │
│   ├── R013 — WHAT SURVIVES CHANGING WORD ORDER?
│   │   │
│   │   ├── remove the semantic instruction
│   │   ├── run all six bare-concept permutations
│   │   └── discover that parents survive better than tokens or edges
│   │
│   ├── R014–R015 — WHAT SURVIVES CHANGING CONTEXT?
│   │   │
│   │   ├── test overlapping concept sets
│   │   ├── repeat in an adjacent semantic region
│   │   └── begin constructing local maps rather than isolated clusters
│   │
│   ├── R016–R017 — CAN A LARGER BASE MODEL RUN LOCALLY?
│   │   │
│   │   ├── establish OLMo 3 32B feasibility
│   │   └── perform a complete new-topic topology run
│   │
│   ├── R018 — IS THERE AN ORDER-INVARIANT MAP?
│   │   │
│   │   ├── run all six permutations
│   │   ├── reconstruct each independently
│   │   └── find a stable semantic basis but conditional relations
│   │
│   └── R019 — IS THE ORDER EFFECT ACTUALLY RANDOMNESS?
│       │
│       ├── three balanced permutations
│       ├── three sequential repeats each
│       ├── no generation or sampling
│       └── zero measured repeat divergence
│
├── 5. WHAT THE MODEL ACTUALLY DID
│   │
│   ├── IDENTICAL PROMPT
│   │   │
│   │   ├── identical hidden states at every layer
│   │   ├── identical vocabulary-score distribution
│   │   ├── identical next-token logits
│   │   └── identical networks and communities
│   │
│   └── DIFFERENT ORDER
│       │
│       ├── different intermediate hidden states
│       ├── different vocabulary neighbourhoods
│       ├── different graph memberships and edges
│       ├── strongest divergence around Blocks 14–15
│       └── partial late reconvergence
│
│       SAME CONCEPTS
│             ↓
│       DIFFERENT ORDER
│             ↓
│       DIFFERENT LOCAL ORGANISATION
│             ↓
│       PARTIAL RECONVERGENCE
│             ↓
│       SHARED HIGHER-ORDER SEMANTIC BASIS
│
├── 6. THE CENTRAL RESULT
│   │
│   ├── Tokens are highly plastic
│   ├── Exact edges are highly plastic
│   ├── Community partitions remain order-conditioned
│   ├── Parent structures are more stable
│   └── Parent relations remain partly conditional
│
│       The learned representation is not one immutable graph.
│
│       It is better described as:
│
│       STABLE SEMANTIC COMPONENTS
│                   +
│       CONTEXT-CONDITIONED ORGANISATION
│                   =
│       ACTIVE SEMANTIC FRAME
│
├── 7. SDA-3 AS AN INTERPRETIVE LENS
│   │
│   ├── C — CENTRAL
│   │   └── Which structure currently organises the answer?
│   │
│   ├── S — SUPPRESSED
│   │   └── Which relevant alternative progressively loses influence?
│   │       Negative cosine alone is not sufficient evidence.
│   │
│   ├── A — ADJACENT
│   │   └── What remains relevant without determining the conclusion?
│   │
│   ├── HCU — HIGHLY CORRELATED UNRELATED
│   │   └── What remains strongly associated without serving the task?
│   │
│   └── E — EMERGING
│       └── What peripheral structure is becoming increasingly influential?
│
│       MEASURED TOPOLOGY
│             ↓
│       SEMANTIC RECONSTRUCTION
│             ↓
│       SDA-3 ROLE ASSIGNMENT
│
│       not:
│
│       SDA-3 ASSUMPTIONS
│             ↓
│       FORCED INTERPRETATION OF THE DATA
│
├── 8. WHY THIS IS PRACTICALLY USEFUL
│   │
│   ├── PROMPT DESIGN
│   │   └── discover how ordering and wording select different frames
│   │
│   ├── MODEL AUDITING
│   │   └── detect persistent omissions, stereotypes and irrelevant associations
│   │
│   ├── RETRIEVAL AUGMENTATION
│   │   └── add evidence targeted at missing or displaced structures
│   │
│   ├── ADVERSARIAL TESTING
│   │   └── explicitly recover plausible interpretations that lost influence
│   │
│   ├── AGENT OVERSIGHT
│   │   └── compare the structure required by the task with the structure
│   │       actually organising the model’s next-token distribution
│   │
│   ├── TRAINING-DATA SEMANTIC MAPPING
│   │   └── aggregate perturbation-stable parents and relations across probes
│   │
│   └── ANSWER IMPROVEMENT
│       │
│       ├── observe the active organisation
│       ├── choose an intervention
│       ├── rerun the prompt
│       └── test whether both topology and output improve
│
├── 9. FROM DIAGNOSIS TO INTERVENTION
│   │
│   ├── If the wrong structure is CENTRAL
│   │   └── clarify the task or change ordering
│   │
│   ├── If relevant evidence is SUPPRESSED
│   │   └── reintroduce it explicitly
│   │
│   ├── If an ADJACENT factor should matter
│   │   └── connect it causally or functionally to the objective
│   │
│   ├── If HCU material contaminates the answer
│   │   └── constrain scope or provide counter-context
│   │
│   └── If a useful structure is EMERGING
│       └── strengthen it before generation continues
│
│       OBSERVE
│          ↓
│       CLASSIFY
│          ↓
│       INTERVENE
│          ↓
│       RE-MEASURE
│          ↓
│       COMPARE OUTPUT AND TOPOLOGY
│
├── 10. WHAT THE PROJECT DOES NOT YET PROVE
│   │
│   ├── It does not recover exact training documents
│   ├── It does not expose literal private reasoning
│   ├── It does not prove negative alignment means suppression
│   ├── It does not establish one universal semantic graph
│   ├── It does not yet prove topology-guided intervention improves answers
│   ├── It does not establish cross-model generality
│   └── It does not establish that every inferred parent is causally active
│
├── 11. THE HUMAN–LLM COLLABORATION BEHIND THE METHOD
│   │
│   ├── HUMAN
│   │   ├── identifies objective drift
│   │   ├── rejects inflated abstractions
│   │   ├── supplies utility judgement
│   │   └── decides which interpretation preserves the real goal
│   │
│   ├── AGENT
│   │   ├── captures and validates evidence
│   │   ├── constructs the networks
│   │   ├── executes repeated experiments
│   │   └── externalises the evolving methodology
│   │
│   └── SHARED EXTERNAL STATE
│       ├── run artefacts
│       ├── protocols
│       ├── reports
│       └── metaanalysis
│
└── CONCLUSION — THE NEXT EXPERIMENT
    │
    ├── Select a measured semantic organisation
    ├── Predict an intervention using SDA-3
    ├── alter prompt order, context or supplied evidence
    ├── rerun the instrumented forward pass
    ├── measure whether the intended structure becomes central
    └── determine whether the generated answer actually improves

        MEASURED ASSOCIATIONS
                  ↓
        TARGETED INTERVENTION
                  ↓
        TOPOLOGICAL CHANGE
                  ↓
        OUTPUT CHANGE
                  ↓
        BETTER ANSWER?

        The project becomes valuable when the map stops being
        merely descriptive and begins supporting interventions
        whose effects can be predicted, measured and reproduced.
```

---

## 8. Primary-research evidence and publication links

**Recorded:** 17/11/2026, 07:31:49 AEDT  
**Source turn:** `01a1e60f-0ed7-7ec3-a3ad-a341e1f873d3`

### Prompt

What data, code or other from the runs can you reference in the article to establish that this is primary research, given the data can be seen and linked from GitHub?

### Response

Yes. The project already contains the components of primary empirical research. The article should expose the complete evidence chain, not cite only the final reports:

```text
RESEARCH QUESTION
      ↓
LOCKED PLAN
      ↓
EXACT MODEL + PROMPT + TOKENISATION
      ↓
CAPTURE CODE
      ↓
MACHINE-READABLE MEASUREMENTS
      ↓
VALIDATION AND CONTROLS
      ↓
SEMANTIC RECONSTRUCTION
      ↓
BOUNDED CONCLUSION
```

## What to reference for each major claim

| Article claim | Best supporting evidence |
|---|---|
| Internal states were directly measured | Capture code, prompt records, capture validation and manifests |
| Concept order changes internal processing | R018 hidden-state and permutation-comparison CSVs |
| The effect is not stochastic instability | R019 repeat metrics and next-token-distribution comparisons |
| Tokens and edges are less stable than higher-order structures | R013/R018 permutation-invariance data and community exports |
| Some structure survives changes in context | R014 and R015 measurements and semantic-map comparisons |
| OLMo 3 32B could be instrumented locally | R016 feasibility report, manifest and device map |
| Semantic parents were reconstructed from measured communities | Community-node/edge data followed by the separately labelled semantic reconstruction |
| The method developed through failures and corrections | Plans, failed validations, recovery records and `META_ANALYSIS.md` |

## 1. Locked experimental protocols

The plans show that the experiments were specified before their conclusions were known:

- [R013 permutation plan](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/R013_PLAN.md)
- [R014 context-invariance plan](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/R014_PLAN.md)
- [R015 adjacent-region replication plan](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/R015_PLAN.md)
- [R018 six-permutation plan](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/R018_PLAN.md)

The article can describe these as the experimental contracts: model, revision, prompts, capture position, expected states, graph method and success criteria were fixed independently of the findings.

## 2. Exact inputs and provenance

For every important run, reference:

- `run_config.json` — model, revision, precision and constants;
- `prompt_records.json` — exact text, token IDs and capture position;
- `manifest.json` — component status, environment and coverage;
- `device_map.json` — actual GPU/CPU/disk placement;
- `artifact_index.json` — byte sizes and SHA-256 hashes.

For example:

- [R018 configuration](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/run_config.json)
- [R018 prompt records](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/prompt_records.json)
- [R018 manifest](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/manifest.json)
- [R018 artifact hashes](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/artifact_index.json)

These establish that the reported observations came from a precisely identified model and stimulus.

## 3. The implementation

The most important methodological code is:

- [Topology calculations](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/topology_core.py) — elbows, exact k-nearest-neighbour graphs, seeded Louvain communities and graph comparisons.
- [Measurement engine](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/topology_engine.py) — capture, vocabulary projection, validation, persistence and provenance.
- [Engine tests](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/test_topology_engine.py)
- [Frozen R017 regression test](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/test_r017_regression.py)

This lets the article say that the graphs were generated by published, inspectable procedures rather than manually assembled from suggestive tokens.

## 4. Layerwise numerical evidence

For the claim that order changes internal processing, use:

- [Pairwise hidden-state metrics](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_hidden_state_metrics.csv)
- [Pairwise topology comparisons](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/pairwise_permutation_comparisons.csv)
- [Permutation-invariance measurements](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/permutation_invariance.csv)

These are stronger evidence than quoting the final analysis because readers can inspect the state-by-state values themselves.

For each article chart, link:

```text
FIGURE
├── source CSV
├── plotting code
├── run configuration
└── commit SHA
```

## 5. The measured network data

The following expose the actual objects from which the semantic claims were reconstructed:

- [Community nodes](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/community_nodes.csv)
- [Community edges](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/community_edges.csv)
- [Intermediate semantic-network dataset](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_NETWORK_GRAPH_DATA.json)

These show that the semantic map was not invented directly from the final answer. It was reconstructed from measured token populations, edges and communities.

## 6. Keep interpretation visibly separate

Then link the downstream interpretation:

- [R018 semantic reconstruction](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_RECONSTRUCTION.md)
- [Structured semantic map](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_SEMANTIC_MAP.json)

The article should explicitly label these as interpretive products:

```text
MEASURED

hidden states
scores
cutoffs
tokens
edges
communities

        ↓ interpretation

INFERRED

community identities
parent structures
parent relations
semantic map
SDA-3 roles
```

That separation considerably strengthens the research claim.

## 7. Failed experiments and validation recovery

Primary research is more credible when unsuccessful paths are retained.

R011 records the failed model/runtime route. R018 also preserves its first validation failure and the correction:

- [R018 validation recovery](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/single_prompt_topology/runs/R018_olmo3-choke-point-barrier-spear-permutation-topology/R018_VALIDATION_RECOVERY.md)

This shows that an apparent failure was diagnosed as a CSV record-counting error, while hashes demonstrated that the measured evidence itself was not altered.

## 8. The research history

[META_ANALYSIS.md](https://github.com/arh789/chatgpt-analysis/blob/33edfac92a7212f687738821fa95914969473b24/projects/llm-topology/META_ANALYSIS.md) documents:

- original hypotheses;
- failed interpretations;
- methodological corrections;
- human objections;
- protocol changes;
- separation of measurement and interpretation;
- the emergence of the larger training-data-topology objective.

It is valuable as a research notebook, although it should support—not replace—the numerical evidence.

## R019 is the strongest new control, but it is not on GitHub yet

R019 provides the evidence that identical prompts have:

```text
hidden-state divergence     = 0
vocabulary-score divergence = 0
next-token divergence       = 0
membership divergence       = 0
edge divergence             = 0
community divergence        = 0
```

Its most useful article sources will be:

- `pairwise_hidden_state_metrics.csv`
- `pairwise_next_token_distribution_metrics.csv`
- `pairwise_vocabulary_score_metrics.csv`
- `pairwise_topology_metrics.csv`
- `divergence_by_state.csv`
- `R019_RESULT.json`
- `R019_MEASUREMENT_REPORT.md`
- `r019_repeatability_control.py`

However, R019 is currently uncommitted and has not been pushed. It cannot yet be cited as GitHub-visible evidence.

## Important publication limitation

The connected `arh789/chatgpt-analysis` repository is currently **private**. Its links work for authorised accounts, but public blog readers cannot inspect them.

For the published article, the strongest solution is a frozen public research package:

```text
publication/
├── README.md
├── METHODS.md
├── CLAIM_EVIDENCE_INDEX.md
├── DATA_DICTIONARY.md
├── CITATION.cff
├── LICENSE
├── environment.yml
├── code/
├── plans/
├── configurations/
├── measured-data/
├── semantic-reconstructions/
├── figures/
└── checksums/
```

Then:

1. Publish it at a fixed release tag.
2. Use commit-permalink links rather than mutable `main` links.
3. Archive the release with Zenodo for a DOI.
4. Publish large tensors as release assets or in the archive.
5. Link every article figure to both its source data and generating code.

GitHub does not itself make the work primary research. What establishes that is the presence of **novel controlled measurements, disclosed methods, reproducibility controls, negative results and an auditable path from data to interpretation**.


