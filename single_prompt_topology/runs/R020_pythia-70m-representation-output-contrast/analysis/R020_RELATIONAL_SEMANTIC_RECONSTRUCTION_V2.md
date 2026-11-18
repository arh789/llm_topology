# R020 — Relational semantic reconstruction (second pass)

**Status:** Full state-by-state *community-relationship maps* generated; semantic interpretation remains evidence-bounded and provisionally evaluated. The human usefulness judgement is still open.

**Controlling question:** Can the model's measured internal semantic associations reveal useful information beyond its circular generated response?

## 1. What this reconstruction adds

The first R020 analysis screened representative tokens against predefined domain terms. This second pass instead builds an **explicit network of measured communities and their recorded intercommunity links** for **every** decision, state and cosine sector.

| Measured / reconstructed object | Coverage |
|---|---:|
| Autoregressive next-token decisions | 32 |
| Recorded states per decision | 8 |
| Positive and negative cosine sectors | 2 |
| Distinct local networks reconstructed | 512 / 512 |
| Original local communities retained | 6,944 / 6,944 |
| Deterministic connectivity-derived structural modules | 1,231 |
| Within-decision depth transitions | 448 |
| Across-decision generation transitions | 496 |
| Candidate cross-state *module overlap* links | 901 across depth; 1,084 across generation |

All 512 interactive network views show the actual community nodes, representative vocabulary and a measured-link backbone (up to three strongest normalised links incident to each community). The four relational-map datasets preserve the community records, original IDs, module membership and edge strengths; full measured cross-community edges remain in the frozen `../chatgpt_community_networks.json`.

**A structural module is not automatically a semantic parent.** Purely geometric connectivity sometimes joins biologically, computationally or lexically unrelated vocabulary. The module labels in the interactive map are intentionally *community exemplars*, not imposed coherent topics. Ambiguous connections remain available for human interpretation.

## 2. First map: urban environment, routes and inhabitants

**Decision 03; S00; positive cosine**, when the model's current input token is *city*:

~~~text
                       [SETTLEMENTS C3]
                 city, cities, villages, towns
                      /       |       \
                 174 /   163 |    93  \      77 to inhabitants
                    /         |         \
        [BUILT PLACES C1] [WATER/LAND C4] [ROUTES C5]
        hotels, buildings  lake, ocean      highway,
        shops, rooms       landscape        railway, streets
              \                    /
               +---- 174 edges ---+

          [INHABITANTS C9]
          residents, citizens, settlers, people
                 ↔ C3 (77 edges)
~~~

The diagram is an intentionally compact subset of the actual measured intercommunity graph, not a reconstructed causal explanation. C1 and C4 have a further 197 cross-community token edges. The numbers represent *measured token-neighbour connections*, not independent training examples or confidence probabilities.

**Interpretation:** The input neighbourhood has separate communities for inhabited places, buildings, surrounding geography, routes and residents, with measured relationships between them. These are richer associations than a literal single-word synonym list, but because this is **S00**, they are a baseline of the word's learned embedding neighbourhood, not yet contextual reasoning.

## 3. Second map: bridge, movement, disruption and reconstruction

**Decision 06; S00; positive cosine**, when the current input token is *bridge* and the next generated word will be *that*:

~~~text
                    [BRIDGE / CROSSING C0]
                bridge, bridging, traverse,
                 junctions, connections
                     /     |        \
                120 /  125|     123 \
                   /       |          \
         [JOURNEY C3] [DISRUPTION C4] [COMPONENTS C1]
         travel, trips   floods,       rope, wires,
         voyage, routes  explosions,   pipes, connectors
             |           catastrophe
          74 |              |
             v           67 |
        [ROADS C9]          v
        highway,        [RECONSTRUCTION C11]
        railway         rebuilding, restoration,
                        renovation, stabilisation

   Additional measured links:
     Journey C3 ↔ Reconstruction C11    55 edges
     Boats C2  ↔ River/Landscape C5    102 edges
     Boats C2  ↔ Road/Rail C9           85 edges
     River C5  ↔ Buildings C7          110 edges
     Buildings C7 ↔ Courtyard C8        90 edges
~~~

This is more informative than the earlier classification table because it preserves **which communities connect**, not merely which words appear. The specific disruption/reconstruction branch had been flattened out in the first summary.

However, **the disruption/repair link is present at the input embedding state**. It is evidence of an associative neighbourhood around *bridge*, not proof that the model contextualised urban planning, flood mitigation or recovery as an answer.

### Contextual change in the same decision

At **D06/S01/positive**, the measured structures include:

~~~text
[TRANSPORT / ROUTES C2] --217--> [BRIDGE / TUNNEL / SWITCH C5]
                                           |
                                         131
                                           |
                                     [PASS / MOVE C7]
~~~

This is a contextual-state observation, but the parent modules become mixed: software tokens, medical vocabulary, movement verbs and operational language appear alongside transport. A real semantic reconstruction must preserve this mixture instead of calling the entire module *urban transport planning*.

At **D06/S02–S05**, some movement/transfer vocabulary remains, but no single clean bridge-related parent can be traced unchanged through every state. Representative-token module matching at D06/S00→S01 shares only five IDs in its strongest qualifying link (Jaccard 0.036), and D06/S05→S06 supplies **no qualifying module link** under the conservative criterion. Absence of a token-ID match is **not** proof of semantic absence.

## 4. Third map: a later network contains both relevant and unrelated associations

**Decision 32; S05; positive cosine** (the state predicting the second repeated sentence's final full stop):

~~~text
         [CITIES / BUILDINGS C0]
        buildings, cities, houses,
        towns, communities, streets
                  |
             494  |
                  v
         [PLACES / COURTYARDS C4]
        courtyard, terrace, café,
        ridge, cliffs, beach
                  |
                164
                  |
                  v
         [CONNECTIONS C7] <---- 299 edges from C0
        connections, relationships,
        association, link
                  |
                74
                  |
                  v
        [MATHEMATICAL TERMS C12]
        Poisson, hyperbolic, Riemannian,
        cohomology, holomorphic, manifold
~~~

The mathematical branch is real as an observed vocabulary community and measured connection. It is **not** automatically an explanation of urban connectivity, a hidden geometrical theory of bridges, or evidence of a causal inference. It remains an unexplained association that a human could choose to investigate.

This snapshot also shows why the earlier hypothesis needs careful evaluation: recognisable buildings and connection vocabulary can remain in an intermediate state even when the final text repeats a malformed answer.

## 5. Fourth map: output-proximal convergence is not task understanding

**Decision 32; S07; positive cosine**:

~~~text
[EVALUATIVE ADJECTIVES C2]
 intriguing, unfortunate, fascinating, mysterious
             /       \
      387   /         \ 292
           v           v
[THEOLOGY / EXPERTISE C3]   [INTENSITY C5]
 theology, demise, wisdom    remarkably, considerably
           |
         224
           |
           v
[SCHOLARS / PROFESSIONS C7]
 scholar, professors, academics
~~~

This network does not visibly organise the bridge-building question into a useful answer. Similar evaluation/knowledge structures recur in the final states across many generated-token decisions.

### Input-token identity test

For each sector and state, I compared the union of **representative token IDs** between all 496 pairs of next-token decisions. There are 26 pairs where the exact current input token ID repeats, and 470 pairs where it differs.

| State | Same input ID, positive sector | Different input ID, positive sector |
|---|---:|---:|
| S00 | 1.000 | 0.096 |
| S01 | 0.360 | 0.048 |
| S02 | 0.292 | 0.053 |
| S03 | 0.250 | 0.053 |
| S04 | 0.156 | 0.047 |
| S05 | 0.145 | 0.047 |
| S06 | 0.498 | 0.377 |
| S07 | 0.515 | 0.459 |

A corresponding rise is observed in the negative cosine sector: at S07, same-token mean Jaccard is **0.527**, compared with **0.466** for different tokens.

This shows a sharp shift: earlier representations are much more dependent on the specific input-token identity, whereas output-proximal representative vocabularies have **substantial overlap even for different input tokens**.

It is therefore unsafe to interpret the highly recurrent S06/S07 communities as particularly strong *prompt-specific* learned knowledge. Global projection biases, limited model capacity or shared normalisation geometry remain possible explanations. These pairwise comparisons are not independent trials.

## 6. What the generated response did and did not convey

Generated response, unchanged:

~~~text
The city is a bridge that connects the river with the river.

A:

The city is a bridge that connects the river with the river.
~~~

The response expresses *connection* but fails to explain **why** the bridge is built. The reconstructed early networks contain candidate related structures for routes, journeys, settlements, river environments and rebuilding that are not articulated in the continuation. This makes them **possible sources of additional useful information**, subject to human evaluation.

The stronger hypothesis — that the model's contextually reconstructed semantic topology contains a robust, useful answer which generation failed to express — **is not yet demonstrated**. The strongest task-related early links often come from the static input-token embedding neighbourhood; the most stable late-state structure is largely off-task.

### Interpretative boundary

- The maps contain all **6,944 original communities**, but their full original selected-vocabulary token membership is not present in the compact graph export. Only representative/extreme tokens and measured community edges are available for this reconstruction.
- The graph partitions are deterministically formed from normalised cross-community edge counts (count divided by the square root of both community sizes). Such a module is a **structural grouping**, not proof of a coherent semantic parent.
- The 1,985 across-state module overlaps are **candidate correspondences** based on at least four shared representative token IDs and an overlap coefficient of at least 0.08. They are not validated semantic identities, and different representations of the same concept can fail the matching rule.
- Cosine-negative networks are anti-aligned vocabulary populations, not intrinsically *suppressed* thoughts.
- This analysis was not blind to the generated continuation or hypothesised adjacent topics. No causal mechanism or specific training-document recovery is claimed.
- The human reviewer evaluates whether the recovered possibilities, particularly the unexpected ones, are actually useful.

## 7. Saved analysis products

- **[Interactive relational semantic maps — all 512 networks](R020_RELATIONAL_SEMANTIC_MAPS.html)**: choose any token decision, state, and positive/negative sector; inspect nodes, measured connections, structural grouping, and numeric recurrence.
- [Decision maps 01–08](R020_RELATIONAL_MAP_D01-08.json)
- [Decision maps 09–16](R020_RELATIONAL_MAP_D09-16.json)
- [Decision maps 17–24](R020_RELATIONAL_MAP_D17-24.json)
- [Decision maps 25–32](R020_RELATIONAL_MAP_D25-32.json)
- [Within-layer and across-generation candidate trajectories](R020_RELATIONAL_TRAJECTORIES.json)
- [Repeated-input versus different-input representation comparisons](R020_REPRESENTATIVE_REUSE_DIAGNOSTICS.json)
- [Previous provisional semantic report](R020_SEMANTIC_RECONSTRUCTION_REPORT.md)
- [Raw measured community and edge networks](../chatgpt_community_networks.json)

**Current end state:** The full two-dimensional **community-level graph is inspectable**; a unique complete semantic interpretation of every module has *not* been proved and is not imposed. The next meaningful operation is to let the human interrogate the maps, then reconstruct the particular promising or contradictory regions more deeply instead of assigning arbitrary categories to every community.
