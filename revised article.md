## R020 — SDA-3 Structural Analysis

### 1. CENTRAL — What fundamentally defines the run?

**Inferred task:** Determine whether a language model's internal representations contain reconstructable semantic relationships that its generated response fails to express.

**Inferred goal:** Establish whether those relationships can be made accessible as a network through which a human can discover possibilities they would not otherwise know to investigate.

R020 deliberately separates two capabilities:

```text id="djun1f"
LANGUAGE MODEL
│
├── Generative capability
│   └── Produce a coherent, useful response
│
└── Representational capability
    └── Retain structured semantic associations
        │
        └── Reconstruct those associations
            └── Expose a wider possibility space
                └── Enable human investigation
```

Pythia 70M was intentionally selected because its limited generative capability offered an opportunity to investigate whether meaningful semantic organisation remained accessible despite poor output.

The bridge question was chosen because its answer is elementary, but its surrounding semantic territory is broad.

**The experiment is fundamentally about whether representational usefulness can exceed generative usefulness.**

### 2. SUPPRESSED — What is obscured by the conventional interpretation?

The conventional interpretation of a failed response is that the model has little useful information to contribute.

R020 challenges the assumption that:

**Poor generated output = absence of useful learned associations.**

The original hypothesis suggests another possibility: useful semantic relationships may be recoverable even when the model cannot organise them into a satisfactory answer.

The run is not primarily attempting to:

- Repair Pythia's generated response.
- Demonstrate that the model secretly reasoned out the correct answer.
- Recover individual training documents.
- Establish that every reconstructed association is meaningful.
- Automatically determine which relationships deserve investigation.

Here, *suppressed* identifies what the conventional output-centred interpretation neglects. It is not a claim that the model actively suppressed particular concepts.

### 3. ADJACENT — What surrounding structures become accessible?

The minimal answer concerns connecting places and crossing a river.

R020's reconstructed networks expose a wider associative neighbourhood:

```text id="3k84tr"
BRIDGE / CITY / RIVER
│
├── Crossing and movement
│   ├── Journeys
│   └── Roads and railways
│
├── Human organisation
│   ├── Settlements
│   ├── Inhabitants
│   └── Commerce
│
├── Environment
│   ├── Rivers and terrain
│   └── Flooding and disruption
│
└── Reconstruction
    ├── Repairs
    └── Restoration
```

These are candidate relationships reconstructed from recorded network evidence, not a single model-generated explanation.

Their importance is that they offer **additional directions of enquiry**, rather than merely improving the original answer.

### 4. HCU — What correlates without an established explanation?

The late-state mathematical branch provides a particularly useful example.

At D32/S05, a connections community links to vocabulary including Poisson, Riemannian and manifold through 74 measured token-neighbour edges.

That relationship does not establish that Pythia was reasoning about mathematical bridge structures.

Nevertheless, it raises a legitimate exploratory question:

**Why does this mathematical vocabulary appear near connections in this measured representation?**

Possible interpretations include semantic association, vocabulary geometry, tokenisation effects or other structural relationships.

The distinction matters:

- The measured edge relationship exists.
- Its semantic explanation remains uncertain.
- Its uncertainty does not make it unworthy of investigation.

HCU here is an exploratory classification of the unexpected association, not a measured R020 label.

### 5. EMERGING — What higher-order structure forms?

In the broader LLM Topology project, R020 becomes more than an experiment comparing model representations with generated text.

It provides a practical demonstration of a different discovery process.

```text id="jhpmql"
MODEL
Produces a narrow or failed response
              │
              ▼
ANALYTICAL SYSTEM
Reconstructs a wider semantic network
              │
              ▼
HUMAN
Encounters unfamiliar relationships
              │
              ▼
HUMAN
Recognises something worth investigating
              │
              ▼
EVIDENCE INSPECTION
Examines the relationship and its provenance
              │
              ▼
HUMAN
Asks a question that was not available initially
              │
              ▼
AGENT + HUMAN
Investigate and reconstruct further
              │
              ▼
NEW KNOWLEDGE BECOMES ACCESSIBLE
```

This is where R020 connects directly to the project's wider methodology.

The human need not know what the relevant relationship is before encountering the network.

The analytical system need not know which relationship the human will find significant.

The network supplies possibilities. Human recognition determines the next direction.

## 6. What did R020 actually establish?

The recorded experiment demonstrated that additional semantic associations could be reconstructed and inspected despite the model's poor answer.

However, the strongest prompt-related relationships often appeared in the static input-embedding neighbourhood. The experiment did **not** establish that Pythia had developed a robust, context-specific hidden explanation, or prove that the reconstructed associations were independently more useful than its output.

That distinction does not invalidate the project's exploratory purpose.

R020 established the feasibility of constructing an inspectable semantic instrument. Whether its relationships lead to useful discoveries is a subsequent human-directed question.

---

## Fundamental synthesis

**R020's immediate experimental task:**

Determine whether useful semantic organisation can be reconstructed from a weak language model independently of its ability to produce a coherent answer.

**R020's higher-order goal within LLM Topology:**

Make otherwise unexpressed semantic relationships accessible so a human can discover new questions without already knowing what to search for.

The resulting human-use methodology is precisely:

> **Find a relationship you did not expect. Inspect its evidence. Decide what question it raises.**

**The ultimate objective is not to extract a better answer from the model. It is to expand the space of questions available to the human.**
