# R020 — Verified consolidated semantic map

**Status: Community-level relational mapping completed; semantic claims evidence-bounded; human usefulness judgement pending.**

**Question:** Why would a city build a bridge across a river?

**Observed answer (Pythia 70M, greedy 32 tokens):**

~~~text
The city is a bridge that connects the river with the river.

A:

The city is a bridge that connects the river with the river.
~~~

**What has been completed:** All 32 decisions × eight states × positive/negative cosine sectors are included in the [interactive 512-network map](R020_RELATIONAL_SEMANTIC_MAPS.html), [four layer/token atlases](R020_LAYER_TOKEN_ATLAS_D01-08.md), and four complete community graph shards. This is a complete *measured community-relationship map*, **not** an assertion that every community can be uniquely named or that geometrically connected modules are coherent learned concepts.

## 1. Semantic maps reconstructed from measured edges

Each diagram below is a *separate recorded network snapshot*. The numbers are measured cross-community token-neighbour edges; they are not probabilities, explanations or evidence of causation. C identifiers are local to the particular state/sector/decision. Labels describe representative words, not predefined topics that the model was required to find.

### A. CITY — decision 03, input embedding S00, positive cosine

~~~text
                       [SETTLEMENT / C3]
                    city, cities, villages, towns
                         /  |    |     \
                     174/  163   93     \77
                       /    |    |       \
        [BUILT PLACES C1]  [LAND C4]  [ROUTES C5]  [INHABITANTS C9]
        hotels, buildings  ocean, lake  highway,   residents, citizens
        shops, rooms       landscape    railway    people, settlers
              \              /
               \---- 197 ----/

        Also: BUILT PLACES C1 ↔ ROUTES C5 = 174 measured edges
~~~

**What is observable:** Distinct settlement, inhabited-place, buildings, landscape and mobility communities are connected in the neighbourhood of *city*. Because this is S00, the graph is inherited from the current token's embedding neighbourhood. It is not evidence of a new reasoning step.

### B. BRIDGE — decision 06, input embedding S00, positive cosine

~~~text
                            [BRIDGE / C0]
                 bridge, traverse, junctions, crossing
                    /          |         \
                 120          125        123
                  /             |           \
          [JOURNEYS C3]  [DISRUPTION C4]  [COMPONENTS C1]
          travel, voyage  floods,         wires, rope,
          trips, journey  catastrophe     pipes, connectors
                |             |
               74            67
                |             |
         [ROAD/RAIL C9] [REBUILDING C11]
         highway, road   reconstruction,
         railway        renovation, restoration

         C3 journeys ↔ C11 rebuilding     55 measured edges
         C2 boats ↔ C5 river/landscape   102 measured edges
         C2 boats ↔ C9 road/rail         85 measured edges
         C5 river ↔ C7 buildings        110 measured edges
~~~

**Most consequential rediscovered branch:** The bridge neighbourhood includes *disruption and rebuilding*, not only transport. The first classification flattened this away. That makes it a concrete candidate for human evaluation. But it is present **before contextual processing**; this evidence alone cannot show that the model inferred a flood-recovery rationale for constructing the bridge.

### C. BRIDGE — decision 06, after transformer block 0, S01, positive cosine

~~~text
[TRANSPORT / ROUTES C2]
transport, transportation, routes
           |
      217 edges
           |
[BRIDGE / TUNNEL / SWITCH C5]
bridge, tunnel, highway, switching
           |
      131 edges
           |
[PASS / MOVE C7]
Pass, Move, moved, passed
~~~

**What changes:** Transport, crossing and motion remain related after a contextual layer. However, the communities also contain military, software and operational vocabulary. No clean stable semantic parent can be assumed across the full depth of this decision. The S00–S01 link cannot be called a newly discovered learned fact just because its wording changes.

### D. RIVER — decision 10, input embedding S00, positive cosine

~~~text
                      [RIVER / C1]
                 river, lake, ocean, valleys
                   /    |     |       \
                 136   165   76       84
                 /      |     |         \
        [WATER C0]  [PLACES C3] [JOURNEYS C6] [DISRUPTION C9]
        groundwater  city, town  trek, travel  flood, storms
        drainage     countryside crossing    catastrophe
~~~

At **D10/S01/positive/C3**, the measured representative words include \`transport\`, \`transporting\`, \`transportation\` and \`travelled\`. A relevant transport association is still present after one transformer block, but competing and unrelated vocabulary prevents a claim that a unique contextual explanation survives through the whole network.

### E. LATE INTERMEDIATE STATE — decision 32, S05, positive cosine

~~~text
                [SETTLEMENTS / BUILDINGS C0]
                buildings, cities, towns, streets
                      |             \
                     494            299
                      |               \
              [PLACES C4] -------- [CONNECTIONS C7]
              courtyard, terrace   links, relations,
              café, ridge          associations
                       164            |
                                     74
                                      |
                              [MATHEMATICS C12]
                              Poisson, Riemannian,
                              cohomology, manifold
~~~

This demonstrates that **some relevant place–connection vocabulary remains visible** after several blocks, even while the generated response is circular. The mathematical branch is a real measured association, but it is an *unresolved residual*: it cannot be promoted to a hidden theory of bridge geometry or urban design.

### F. OUTPUT-PROXIMAL STATE — decision 32, S07

~~~text
POSITIVE COSINE

      [EVALUATIVE TERMS C2]
      intriguing, fascinating, noteworthy
             /             \
          387              292
           /                \
 [THEOLOGY / EXPERTISE C3]  [INTENSITY C5]
 theology, wisdom,          considerably,
 expertise                  remarkably
           |
          224
           |
 [SCHOLARSHIP C7]
 scholar, academics, professors


NEGATIVE COSINE (ANTI-ALIGNED, NOT "SUPPRESSED")

      [OPERATIONS C0] --600-- [MEASUREMENT C1]
       regulates,            transformations,
       enhances              variables
                                     |
                                    263
                                     |
                              [BIOLOGY C3]
                              cells, mutants
~~~

The highly recurrent output-proximal representation is largely **off-topic** under the available representative vocabulary. Its stability is not evidence that the model possesses a task-specific bridge answer just below the surface of generation.

## 2. How the representation evolves

The reconstruction tracks separate snapshots along both axes:

~~~text
AUTOREGRESSIVE DECISIONS (01–32)
        |
        +-- S00: current-token embedding neighbourhood
        |         city / bridge / river and other input-token associations
        |
        +-- S01–S05: contextual reorganisation, mixed categories
        |         transport / motion / urban places persist intermittently
        |         many other communities compete or replace them
        |
        +-- S06–S07: recurrent output-proximal vocabulary
                  evaluation / scholarship / operations / biology
                  plus multilingual fragments, numbers, formatting

Across decisions: the model conditions on its own increasingly
repetitive continuation. The state predicting a generated token
precedes that token's addition to the input sequence.
~~~

A key methodological warning: a change in community membership is not proof of a change in higher-order semantics, while strong community recurrence is not proof of context-specific meaning. The saved candidate module correspondences should be treated as **continuity candidates**, not established parent identities.

### Repeated-current-token control

Independent comparison of representative-token sets across all 496 pairs of token decisions reproduces the prior diagnostic. Twenty-six pairs have the same current input token; 470 have different current input tokens.

| State | Same current token, positive-set mean Jaccard | Different current token, positive-set mean Jaccard |
|---|---:|---:|
| S00 | 1.000 | 0.096 |
| S01 | 0.360 | 0.048 |
| S02 | 0.292 | 0.053 |
| S03 | 0.250 | 0.053 |
| S04 | 0.156 | 0.047 |
| S05 | 0.145 | 0.047 |
| S06 | 0.498 | 0.377 |
| S07 | 0.515 | 0.459 |

**Interpretation:** At S00, identical input tokens reproduce identical embedding-neighbour sets. At S07, different tokens have extensive common representative vocabulary. This favours caution: late recurrent structure may partly reflect shared projection geometry rather than task-specific reasoning. These comparisons share one prompt and are not independent experimental trials.

## 3. What the source audit establishes

The [independent source-to-map reconciliation](R020_SOURCE_TO_SEMANTIC_MAP_AUDIT.json) directly compared the raw recorded community networks with the four relational map shards and transition records.

| Audit | Outcome |
|---|---:|
| State/sector networks matching source | 512 / 512 |
| Communities and representative token IDs matching source | 6,944 / 6,944 |
| Geometric structural modules with complete partitions | 1,231 across 512 valid networks |
| Measured cross-community edges in source | 42,291 |
| Displayed backbone edges matching source | 15,292 / 15,292 |
| Depth transition cases | 448 |
| Generation transition cases | 496 |
| Candidate module links recomputed successfully | 1,985 / 1,985 |
| Repeated-token/different-token diagnostic | Reproduced |

**Audit passed.** This establishes that the displayed maps are faithful to the compact measured evidence and that the declared trajectory matching rule was applied consistently. It does **not** prove semantic interpretations, recover complete original token memberships, independently validate the post-hoc lexicon, or establish human usefulness.

## 4. Result against the R020 hypothesis

**Observed generated-answer outcome:** The continuation fails to explain the reason for the bridge and repeats itself.

**Internal evidence:** There are semantic relationships absent from the answer, including inhabitants, routes, travel, natural hazards, rebuilding, roads and railways. Some transport/movement associations persist into contextual states. Unusual unrelated associations are also exposed and preserved rather than silently removed.

**Strongest limitation:** The clearest prompt-relevant maps often occur in **static input-token neighbourhoods**. The later contextual structures are mixed, and the final states are recurrent but mostly not task-specific. Thus the experiment **does not currently demonstrate a robust, newly contextualised hidden explanation that the model was unable to express**.

**Conclusion:** R020 successfully provides a way to inspect additional learned *associations* even when generation is poor. Whether those associations are *useful*, rather than simply interesting or obvious, remains a human judgement. The stronger claim that representational usefulness exceeded generative usefulness in an independently validated way is **not established by this single experiment**.

## 5. Complete per-token and per-layer evidence

The four atlases enumerate every decision and recorded state in both cosine sectors. The original community IDs, individual community exemplars and measured link structures are retained in the full relational-map data.

- [Interactive semantic maps — select any of 512 networks](R020_RELATIONAL_SEMANTIC_MAPS.html)
- [Decisions 01–08: eight states × two sectors per decision](R020_LAYER_TOKEN_ATLAS_D01-08.md)
- [Decisions 09–16](R020_LAYER_TOKEN_ATLAS_D09-16.md)
- [Decisions 17–24](R020_LAYER_TOKEN_ATLAS_D17-24.md)
- [Decisions 25–32](R020_LAYER_TOKEN_ATLAS_D25-32.md)
- [Complete module/node evidence, decisions 01–08](R020_RELATIONAL_MAP_D01-08.json), [09–16](R020_RELATIONAL_MAP_D09-16.json), [17–24](R020_RELATIONAL_MAP_D17-24.json), [25–32](R020_RELATIONAL_MAP_D25-32.json)
- [All candidate across-state trajectories](R020_RELATIONAL_TRAJECTORIES.json)
- [Independent source reconciliation audit](R020_SOURCE_TO_SEMANTIC_MAP_AUDIT.json)

**Completion boundary:** The requested *community-level semantic maps across every measured generation decision and transformer state* are constructed and independently reconciled to the source export. No claim is made that all 1,231 structural modules have uniquely determined semantic parent identities. The human must decide whether the visible associations are worth investigating. No additional model run or reinterpretation is required to inspect the existing maps.
