# R020 — Generation-wide higher-order semantic hypothesis reconstruction

**Status:** Candidate higher-order semantic relationships reconstructed for all 32 generated-token decisions. The human usefulness judgement is pending.

**Governing question:** Does Pythia 70M draw on a common organising semantic hypothesis throughout its response, or does that organisation change as generation proceeds?

## 1. Answer

**The data support intermittent recurrence of a higher-order functional relationship, not uninterrupted maintenance of a single complete hypothesis.**

The recurring candidate concerns **inhabited places, movement/routes, and connection/crossing**. Different communities and token exemplars support related functional relationships at different generation decisions, including decisions where the current input token is punctuation or a function word. The relationship does not, however, appear as a continuously coherent map through every generated token and every transformer state.

The model's output:

~~~text
The city is a bridge that connects the river with the river.

A:

The city is a bridge that connects the river with the river.
~~~

The semantic evidence helps distinguish two possibilities: failure to maintain the overall organising relationship, versus recurrence of its parts without stable assignment of roles such as settlement, constructed crossing, water obstacle and purpose.

## 2. Consolidated functional relationship map

The following map is an **across-decision synthesis**, not a single measured network. Counts represent distinct generation decisions containing qualifying direct intercommunity connections in contextual states S01–S05, **positive cosine sector only**.

~~~text
                    [INHABITANTS / PEOPLE]
                       |               |
                6      |               | 7
                       v               v
                  [SETTLEMENTS]     [BUILT PLACES]
                       |  \              |
                11     |   \ 5           | 7
                       v    v            v
                   [MOVEMENT / ROUTES]----+
                           |
                       8   |
                           v
                   [CONNECTION / CROSSING]
                           |
                           +-- water / terrain:
                               linked contextually in just
                               one decision (D32) at this cutoff

Other contextual candidate:
  [COMMERCE] ↔ [MOVEMENT / ROUTES] — 3 decisions

Arrows indicate recurrence counts, NOT directions of causation.
~~~

| Reconstructed candidate relationship | Contextual decisions | Decision identifiers |
|---|---:|---|
| movement/routes ↔ settlements | 11/32 | 03, 06, 08, 10, 13, 14, 22, 27, 28, 29, 32 |
| crossings/connections ↔ movement/routes | 8/32 | 06, 08, 13, 16, 25, 27, 29, 32 |
| built places ↔ movement/routes | 7/32 | 03, 10, 14, 16, 22, 29, 32 |
| built places ↔ inhabitants | 7/32 | 02, 14, 16, 18, 21, 29, 32 |
| inhabitants ↔ settlements | 6/32 | 02, 14, 17, 18, 29, 32 |
| crossings/connections ↔ settlements | 5/32 | 03, 08, 13, 27, 32 |
| inhabitants ↔ movement/routes | 3/32 | 10, 11, 20 |
| commerce ↔ movement/routes | 3/32 | 10, 25, 29 |
| built places ↔ crossings/connections | 2/32 | 03, 32 |
| built places ↔ commerce | 2/32 | 12, 22 |
| commerce ↔ settlements | 2/32 | 12, 22 |

**Core inference:** The model repeatedly draws from a functional field connecting places, people, routes and crossings. However, the *river-as-obstacle* role does not persist with comparable contextual support. The water and hazard neighbourhoods are most clearly observed in S00 input embeddings, rather than being continuously bound to crossings in the contextual map.

## 3. What this reconstruction actually measures

For every generation decision, each of the eight states and both positive/negative cosine sectors was inspected from the frozen R020 network export. Communities were provisionally associated with semantic functions using multiple representative or extreme vocabulary terms. Crucially, a relationship was recorded only when **two separate measured communities** carrying different candidate functions were joined by a measured cross-community token edge (minimum 30 token edges, normalised affinity at least 0.30).

This establishes traceable candidate relations, rather than inferring semantic continuity solely from identical token IDs. Original community IDs, state numbers, token evidence and measured edge strengths are retained in the four per-decision JSON checkpoint files. Negative-cosine candidates are recorded separately and not treated as positive associations.

Results:

| Measure | Result |
|---|---:|
| Autoregressive generation decisions | 32 |
| State/sector networks examined | 512 |
| Original communities available in the source | 6,944 |
| Raw intercommunity edges examined | 42,291 |
| Communities matching at least one deliberately limited anchor family | 818 |
| Decisions with a qualifying positive contextual relationship | **21/32** |
| Decisions with a *same* relationship evidenced in at least two contextual states | **6/32** |
| Decisions with task-candidate relations at the input-embedding state | 8/32 |
| Decisions with qualifying positive task-candidate links at S06 or S07 | **0/32** |

The unmatched communities are **not discarded**; they remain in the source and earlier full relational maps. Missing matches here mean only that this conservative interpretation screen did not identify qualifying relations.

## 4. Integrated map for every token decision

The table shows up to the two strongest contextual candidate relationships for each decision, together with the supporting transformer states. The underlying decision checkpoint contains all other qualifying links, both sectors, competing community evidence and unexplained communities.

S00 is the input embedding; S01–S06 are successive transformer-block outputs; S07 is final normalisation. A decision's states predict the *next* token named in the second column.

| Decision | Current input → next generated token | Leading contextual candidate relationships |
|---|---|---|
| 01 | `:` → `·The` | No qualifying direct contextual relation |
| 02 | `·The` → `city` | built places ↔ inhabitants (S1, S4); inhabitants ↔ settlements (S4) |
| 03 | `city` → `is` | built places ↔ settlements (S1); built places ↔ movement/routes (S1) |
| 04 | `is` → `a` | hazards ↔ movement/routes (S1) |
| 05 | `a` → `bridge` | No qualifying direct contextual relation |
| 06 | `bridge` → `that` | crossings/connections ↔ movement/routes (S1, S2); movement/routes ↔ settlements (S1) |
| 07 | `that` → `connects` | No qualifying direct contextual relation |
| 08 | `connects` → `the` | crossings/connections ↔ movement/routes (S2, S3); crossings/connections ↔ settlements (S5) |
| 09 | `the` → `river` | No qualifying direct contextual relation |
| 10 | `river` → `with` | built places ↔ movement/routes (S1); movement/routes ↔ settlements (S2) |
| 11 | `with` → `the` | inhabitants ↔ movement/routes (S2) |
| 12 | `the` → `river` | built places ↔ commerce (S5); commerce ↔ settlements (S5) |
| 13 | `river` → `.` | crossings/connections ↔ movement/routes (S2); movement/routes ↔ settlements (S2) |
| 14 | `.` → `↵` | built places ↔ movement/routes (S2, S5); built places ↔ inhabitants (S2, S4) |
| 15 | `↵` → `↵` | No qualifying direct contextual relation |
| 16 | `↵` → `A` | built places ↔ movement/routes (S4, S5); crossings/connections ↔ movement/routes (S2) |
| 17 | `A` → `:` | inhabitants ↔ settlements (S2) |
| 18 | `:` → `↵` | built places ↔ inhabitants (S5); commerce ↔ inhabitants (S5) |
| 19 | `↵` → `↵` | No qualifying direct contextual relation |
| 20 | `↵` → `The` | inhabitants ↔ movement/routes (S2) |
| 21 | `The` → `city` | built places ↔ inhabitants (S1) |
| 22 | `city` → `is` | built places ↔ movement/routes (S1); movement/routes ↔ settlements (S1) |
| 23 | `is` → `a` | No qualifying direct contextual relation |
| 24 | `a` → `bridge` | No qualifying direct contextual relation |
| 25 | `bridge` → `that` | crossings/connections ↔ movement/routes (S2); commerce ↔ movement/routes (S4) |
| 26 | `that` → `connects` | No qualifying direct contextual relation |
| 27 | `connects` → `the` | crossings/connections ↔ settlements (S5); crossings/connections ↔ movement/routes (S3) |
| 28 | `the` → `river` | movement/routes ↔ settlements (S1) |
| 29 | `river` → `with` | built places ↔ movement/routes (S1); commerce ↔ movement/routes (S3) |
| 30 | `with` → `the` | No qualifying direct contextual relation |
| 31 | `the` → `river` | No qualifying direct contextual relation |
| 32 | `river` → `.` | crossings/connections ↔ settlements (S2, S5); built places ↔ movement/routes (S1) |

The 11 decisions with no qualifying direct positive-sector relationship (D01, D05, D07, D09, D15, D19, D23, D24, D26, D30 and D31) are **unresolved at the declared screening threshold**, not proven to be devoid of meaningful semantic structure.

## 5. Strong examples of higher-order recurrence

### D03 — processing “city”, predicting “is”

At **S01 positive**, the measured graph links buildings and shops (C1), transport/walking (C4) and towns/cities (C8). Direct community connections support *built places ↔ movement*, *movement ↔ settlement*, and *built places ↔ settlement* within one state. At S02, settlement/built-place vocabulary connects to crossing/transfer vocabulary. The broad role of an inhabited place linked to movement or crossing is reconstructable here, but not unchanged through every state.

### D06 — processing “bridge”, predicting “that”

At **S01 positive**, transport/routes (C2) link to bridge/tunnel/switch (C5) with 217 measured cross-community token edges; the transport community also links to village/city vocabulary (C11). Related crossing and movement vocabulary recurs at S02. This is stronger than a static bridge-synonym list, although its functional interpretation remains provisional.

### D08 and D27 — processing “connects” in two passages

At **D08/S02 positive**, walking (C2) links to transfer/crossing (C5) and also to villages/towns (C14). At D08/S05, connections/links (C3) connect with cities/towns (C10).

In the repeated sentence, **D27/S03** again associates walking/movement with transfers, and **D27/S05** links communities/cities/towns with connections. The same functional relations reappear with changed community identities and state locations. This is evidence of **recurrence across representations**, not persistence of the same token set.

### D10, D13 and D32 — processing “river”

At **D10/S02 positive**, travelling (C0) is directly connected with villages/towns (C6); at D13/S02, transportation, crossings and settlements appear as directly connected communities. By **D32/S02**, the network includes links between movement, crossings and a community containing both settlement and river/valley vocabulary; S05 also links buildings and connections.

The D32 evidence is especially relevant because it partially reunites water/terrain, movement, settlements and crossings after much of the answer has already been generated. It does not establish that those roles were held together continuously.

### D14 and D16 — contextual relationships after punctuation

At **D14**, whose current input is a full stop, movement ↔ built places and built places ↔ inhabitants appear in two contextual states. At **D16**, following a newline, movement ↔ built places recurs across S04 and S05.

These observations make it inadequate to explain every contextual relationship as simply the current input word's nearest neighbours. They do not by themselves establish that the relationships are specific to the original bridge question rather than to the accumulated generated text.

## 6. Does the second sentence reuse the same semantic map?

The model repeats much of its answer, but the inferred relation maps are not exact copies.

| Repeated context | Relationship(s) preserved | Meaningful differences |
|---|---|---|
| D03 vs D22 — *city* | Settlement ↔ movement; built places ↔ movement | First occurrence connects settlement/built places to crossing; second develops commercial/built-place links |
| D06 vs D25 — *bridge* | Crossing ↔ movement | Settlement link is not recovered in the second occurrence; commerce ↔ movement appears |
| D08 vs D27 — *connects* | Crossing ↔ movement; crossing ↔ settlement; movement ↔ settlement | Relationships recur at different transformer states |
| D10 vs D29 — *river* | Built places ↔ movement; movement ↔ settlement; commerce ↔ movement | Second occurrence additionally links crossings, people and places |
| D13 vs D32 — *river* | Crossing ↔ movement; movement ↔ settlement | D32 adds explicit contextual water/terrain links and further built-place/inhabitant connections |

D02 and D21 display the same written word *The* but are **different tokenizer IDs** (`ĠThe` and `The`), so this pair is not an identical-token control.

This is most consistent with **selective reactivation and contextual transformation of a common functional field**, not a stored semantic network replayed without change.

## 7. Leading organising hypothesis and alternatives

**H1 — Fragmentary functional connectivity, with unstable role binding.** The model repeatedly recruits associations among inhabited places, transport, crossings and people, but does not retain an adequately connected account of *city as agent, bridge as constructed means, river as obstacle and crossing as purpose*. The visible answer confuses those roles: “the city is a bridge” and “river with the river”.

**H2 — Local token-triggered association without a generation-wide hypothesis.** Much of the strongest input-state evidence occurs when the current word is *city*, *bridge* or *river*. Similar relations in some other decisions might arise from generic contextual vocabulary rather than one shared functional map.

**H3 — Representational change obscured by the projection basis.** The screen identifies no qualifying question-related positive links at S06–S07, yet the experiment projects those states against the **input** embedding matrix while the model's actual output embeddings are untied. A failure to recover relations in this projection cannot establish that the model discarded them.

**Best-supported statement:** H1 identifies a plausible organising relationship that recurs intermittently across semantically different tokens. H2 and H3 remain material alternatives. The current evidence does not establish one uninterrupted, fully role-bound semantic hypothesis throughout all 32 decisions, and it does not justify declaring the entire semantic process incoherent because the output is.

## 8. Evidence boundaries and next human judgement

- The candidate semantic families were constructed after inspecting R020 evidence; they are interpretive anchors, not independently learned topic identities.
- This screen matches 818 of 6,944 communities and therefore makes no completeness claim about all semantic possibilities. All other community evidence remains available in the previous relational maps.
- Every qualifying relationship is a recorded connection between vocabulary communities. The labels describe possible functional relationships; the graph is not a direct causal model of the output.
- A single repeated answer supplies useful within-run contrasts, not independent experiments. The same semantic family can also be expressed by vocabulary this screen did not match.
- The output-proximal negative result is conditional on the projection basis and edge threshold; it is not an argument that semantic information is absent.
- The generated response and expected adjacent domains were known before interpretation; this is not a blinded reconstruction.
- **Your usefulness judgement is intentionally open.** The immediate question is whether the recovered *settlement–movement–crossing* field, its unexpected branches and its discontinuities provide useful information the generated answer did not convey.

## 9. Saved evidence and recovery

- [One integrated candidate relational map per generated-token decision, D01–D08](R020_FUNCTIONAL_HYPOTHESIS_D01-08.json)
- [D09–D16](R020_FUNCTIONAL_HYPOTHESIS_D09-16.json)
- [D17–D24](R020_FUNCTIONAL_HYPOTHESIS_D17-24.json)
- [D25–D32](R020_FUNCTIONAL_HYPOTHESIS_D25-32.json)
- [Cross-generation recurrence counts and exact-token repeat comparisons](R020_CROSS_GENERATION_HYPOTHESIS_TRAJECTORY.json)
- [Deterministic analysis reproducer](R020_SEMANTIC_CONTINUITY_REPRODUCER.js)
- [Previous full relational community map, all 512 networks](R020_RELATIONAL_SEMANTIC_MAPS.html)
- [Previous independent source-to-map audit](R020_SOURCE_TO_SEMANTIC_MAP_AUDIT.json)

**Completion boundary:** The requested cross-generation higher-order reconstruction has been attempted for all 32 decisions, with positive direct-link evidence, competing interpretations, unclassified residuals and saved per-decision maps. The evidence favours intermittent functional recurrence rather than an invariant fully maintained hypothesis. Whether this reconstruction is *useful* belongs to the human reviewer, as established in the project methodology.
