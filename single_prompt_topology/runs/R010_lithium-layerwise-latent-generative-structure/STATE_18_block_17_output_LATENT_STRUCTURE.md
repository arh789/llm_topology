# R010 State 18 — Block 17 output latent structure

## State identity

- R010 state index: `18`
- R008/R009 state: `block_17_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 12 negative-tail = 24**
- R008 population: **3,015 positive-head + 3,291 negative-tail = 6,306 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 18 only. Retrieval and graph inspection were
restricted to `state_index=18 / block_17_output`. No later-state evidence was
used.

## Evidence inventory

For every State 18 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_18_block_17_output.md`;
2. all 24 State 18 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 18 within-side relation set in
   `R008/community_edges.csv`;
4. the State 18 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 526 | 2,415 / 2,107 | 13.19 | +0.03139 | Personal names, cities and national/geographic entities dominate: Manchester, Scott, Hamburg, Mitchell, Karen, Matt, Josh, Amsterdam, Germany and Jay. |
| C1 | 421 | 1,687 / 2,208 | 13.26 | +0.03150 | Food, hospital/medical and health-related material coexists with retail/lifestyle and freshness language: Food, breastfeeding, hospital fragments, pneumonia/psychiatry fragments, shoppers, shops, Sleep, Medical and Fresh. |
| C2 | 392 | 1,583 / 2,221 | 13.74 | +0.03141 | Exploration, entrepreneurship, negotiation and motivational/business activity dominates: exploring, entrepreneurs, anticipated, negotiating, explores, motivations, yields, motivation, anticipation, discuss, business and adventures. |
| C3 | 318 | 1,509 / 1,824 | 15.23 | +0.03069 | Common grammatical/function words and lexical fragments dominate. |
| C4 | 298 | 1,124 / 1,834 | 13.70 | +0.03110 | Transformations, measurements, interactions and quantitative/computational analysis dominate: transformations, determinations, interactions, Measurements, characterizing, Measurement, size, evolving, imaging, computations, evolves and values. |
| C5 | 292 | 1,615 / 727 | 13.55 | +0.03252 | Mathematical/code punctuation and symbolic formatting dominate; 203 of 292 tokens are punctuation/symbols. |
| C6 | 178 | 642 / 1,157 | 13.71 | +0.03157 | Film/media, learning, interviews, photography and workshop activity form a coherent mediated-learning/production domain: conversations, filmmakers, Learning, interviews, photography, interventions, Play, workshops, facebook and therapists. |
| C7 | 145 | 414 / 920 | 12.06 | +0.03135 | Browser, search, session and software/interface systems are coherent: Notification, browsers, Firefox, Resolver, animation, Query, Session, manager and Search. |
| C8 | 135 | 492 / 812 | 13.30 | +0.03086 | Quantitative/evaluative adverbs and discourse/context modifiers dominate: surprisingly, numerically, analytically, Having, With, More, elderly, Now, larger, Next and Clearly. |
| C9 | 120 | 739 / 227 | 14.21 | +0.03037 | Numeric strings and short coded values dominate. |
| C10 | 115 | 325 / 818 | 12.77 | +0.03132 | Prefix/stem families around inevitability, reappearance, reconstruction and interpretation dominate; incomplete lexical form is the primary organisation. |
| C11 | 75 | 286 / 393 | 12.87 | +0.03230 | Example-related multilingual words and morphological fragments dominate. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 512 | 2,222 / 2,663 | 13.88 | -0.03009 | Administrative characterisation, configuration and recommendation systems dominate: Characteristics, administrators, superintendent, Configuration, recommendations, representation and beneficiaries. |
| C1 | 424 | 1,794 / 1,932 | 13.02 | -0.03039 | Personal names and name-like entities dominate. |
| C2 | 366 | 1,485 / 1,723 | 12.82 | -0.03065 | Short technical/computing abbreviations and code-like fragments dominate. |
| C3 | 349 | 1,546 / 1,953 | 14.46 | -0.03037 | Adverse evaluation, legal/jurisdictional constraint and intensity dominate: circumstantial, unconstitutional, discriminatory, incredible, jurisdictional, unbelievable, stupid and brutal. |
| C4 | 335 | 1,544 / 1,498 | 13.69 | -0.02975 | Cardiovascular disease, cytokine biology, immunology and pathology are coherent: cardiovascular, cytokine, atherosclerotic, epidemiological, macrophage, interleukin, monocyte and hypertension. |
| C5 | 326 | 1,328 / 1,721 | 13.43 | -0.02998 | Regulation, encouragement, activation, deletion and institutional/change actions dominate: downregulation, prohibiting, encourages, encouragement, activate, Delete, establishment, excluding and prohibits. |
| C6 | 269 | 1,124 / 1,531 | 14.05 | -0.03108 | Family, monarchy, government and mythic/conflict roles coexist: grandmother, Constitution, palace, emperor, mother, church, dragon, Sultan, queen, warriors, king and Americans. |
| C7 | 241 | 975 / 1,252 | 13.29 | -0.03021 | Common grammatical/function words and multilingual lexical fragments dominate. |
| C8 | 189 | 728 / 1,099 | 13.52 | -0.03181 | Vehicles, roads, built environment and material/household objects form a broad physical-setting domain: automobiles, trucks, terrace, gravel, roads, cylinder, uniforms, pavement, furniture, stones and firearms. |
| C9 | 124 | 699 / 333 | 13.96 | -0.02933 | Numeric strings, especially historical years, dominate. |
| C10 | 82 | 401 / 436 | 15.10 | -0.03058 | Geographic entities and regions form a coherent territorial domain: Pennsylvania fragment, Alabama, Florida, Louisiana, Barcelona fragment, Mexico, Minnesota, Georgia, Argentina, Orleans and Arkansas. |
| C11 | 74 | 315 / 251 | 11.91 | -0.02939 | Mathematical/code punctuation and symbol formatting dominate; 62 of 74 tokens are punctuation/symbols. |

## Population accounting

### Positive head

Total nodes: **3,015**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,013 | 33.6% |
| Formal/name substrate | 1,446 | 48.0% |
| Irreducible semantic | 135 | 4.5% |
| Mixed unresolved | 421 | 14.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,015** | **100.0%** |

Semantic-eligible denominator: **1,569 nodes**.

### Negative tail

Total nodes: **3,291**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,538 | 46.7% |
| Formal/name substrate | 1,229 | 37.3% |
| Irreducible semantic | 524 | 15.9% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,291** | **100.0%** |

Semantic-eligible denominator: **2,062 nodes**.

## Positive-side reconstruction

### P+0 — Goal-directed development, transformation and quantitative activity

- **Primary children:** C2, C4
- **Primary nodes:** 690
- **Side-relative coverage:** 22.9%
- **Semantic-eligible coverage:** 44.0%
- **Confidence:** High

**Evidence.** C2 contains exploration, entrepreneurship, negotiation,
motivation, anticipation and business activity. C4 contains transformations,
measurements, interactions, quantitative/computational analysis and
characterisation. Their direct relation is the strongest clearly semantic
positive relation in the state: **468 token edges**, mean cosine **0.09844**.
The common generator is goal-directed development: situations or systems are
explored, anticipated, negotiated, transformed, measured and evaluated through
their resulting interactions and values.

**Secondary links:** C8 and C6. C2–C8 has **148 edges** and C4–C8 **81**,
placing contextual/evaluative modifiers around the process. C2–C6 has **270**
edges and C4–C6 **198**, linking mediated learning/production activity to the
developmental/analytical structure.

**Exclusion boundary.** C2 contains entrepreneurship and social motivation,
while C4 is analytical/quantitative and system-oriented. C6 is mediated
learning/production rather than the underlying development/transformation
process. C1 is too internally heterogeneous to join.

**Alternative.** Add C6 as a third child under a broader
`development, learning and mediated production` parent. Rejected because its
film/media/interview/learning identity remains discriminable from the
developmental/quantitative pair.

### P+1 — Mediated learning, communication and software-interface systems

- **Primary children:** C6, C7
- **Primary nodes:** 323
- **Side-relative coverage:** 10.7%
- **Semantic-eligible coverage:** 20.6%
- **Confidence:** Moderate / High

**Evidence.** C6 contains filmmaking, learning, interviews, photography,
workshops, interventions and online media activity. C7 contains browsers,
search, sessions, queries and software/interface systems. Their direct relation
contains **102 token edges**, mean cosine **0.09284**. The common generator is
mediated information activity: communication, learning and content production
occur through software/search/interface systems.

**Secondary link:** P+0 through C2–C6 (**270 edges**), C4–C6 (**198**),
C2–C7 (**126**) and C4–C7 (**153**). Mediated systems strongly support
goal-directed activity without becoming identical to it.

**Exclusion boundary.** C6 includes social/creative learning activity, whereas
C7 is technical interface/search infrastructure. A broader “information”
parent would become too generic.

**Alternative.** Leave C6 and C7 separate and treat their relation as
activity-to-tool adjacency. This remains plausible, so confidence is
Moderate/High rather than unqualified High.

### Positive irreducible and unresolved structures

- **C1 — mixed-unresolved:** food/health, medical, retail/lifestyle and
  freshness language coexist. Strong connections to C2 (**417 edges**) and C4
  (**295**) do not establish one discriminative latent parent.
- **C8 — irreducible-semantic:** quantitative/evaluative discourse and
  contextual modifiers; secondary relation to P+0.

### Positive formal/name substrate

- C0 — personal names/geographic entities
- C3 — grammar/function words/fragments
- C5 — mathematical/code punctuation and formatting
- C9 — numeric strings/coded values
- C10 — inevitability/reappearance/reconstruction lexical stems
- C11 — example-related multilingual morphology

## Negative-side reconstruction

### P-0 — Administrative characterisation, adverse constraint and institutional change

- **Primary children:** C0, C3, C5
- **Primary nodes:** 1,187
- **Side-relative coverage:** 36.1%
- **Semantic-eligible coverage:** 57.6%
- **Confidence:** High

**Evidence.** C0 contains administrative characterisation, configuration and
recommendation. C3 contains adverse/legal evaluation and jurisdictional
constraint. C5 contains regulation, encouragement, activation, deletion and
institutional/change actions. The structure is exceptionally well triangulated:
C0–C5 has **557 token edges**, mean cosine **0.10227**; C0–C3 **481** at
**0.10204**; C3–C5 **394** at **0.09836**. The common generator is organised
state control: systems are characterised/configured, judged against legal or
normative constraints, and encouraged, prohibited, activated, deleted or
otherwise changed.

**Secondary links:**
- **C4:** C0–C4 has **334 edges**, C3–C4 **171** and C5–C4 **122**, placing
  clinical/pathological states adjacent to characterisation and intervention.
- **C6:** C0–C6 has **337 edges**, C3–C6 **244**, C5–C6 **119**, linking
  institutional/social actors to regulatory/change processes.
- **C8:** C0–C8 has **265 edges**, C3–C8 **109**, C5–C8 **88**, placing
  material environments within the same broader operational field without
  requiring primary inclusion.

**Exclusion boundary.** C0 is administrative/descriptive, C3 is evaluative and
constraint-oriented, and C5 is action/change-oriented. The parent therefore
cannot be reduced to regulation, negative evaluation or administration alone.

**Alternative.** Split C0 away from C3+C5, retaining a neutral administrative
parent and a separate adverse/regulatory-change parent. This preserves semantic
purity but discards unusually strong three-way evidence.

### P-1 — Institutional/familial authority and territorial identity

- **Primary children:** C6, C10
- **Primary nodes:** 351
- **Side-relative coverage:** 10.7%
- **Semantic-eligible coverage:** 17.0%
- **Confidence:** Moderate / High

**Evidence.** C6 contains family, monarchy, government and mythic/conflict
roles; C10 contains geographic entities and regions. Their direct relation
contains **101 token edges**, mean cosine **0.09955**. The common generator is
social and institutional authority situated within territorial identity.

**Secondary link:** C8. C6–C8 has **153 edges**, mean cosine **0.10119**,
showing that vehicles, buildings and material environments provide settings for
authority and social order.

**Exclusion boundary.** C6 includes family/mythic/conflict roles as well as
government. C10 is territorial rather than institutional. C8 is material
setting, not authority or territorial identity.

**Alternative.** Pair C6 with C8 instead under an
`institutional roles and material setting` parent. That has stronger raw edge
count, but C6–C10 yields a more discriminative institutional-territorial
generator. The material relation is retained as secondary.

### Negative irreducible structures

- **C4 — irreducible-semantic:** cardiovascular/cytokine/immunological
  pathology; secondary relation to P-0.
- **C8 — irreducible-semantic:** vehicles, roads, built environment and
  material/household objects; secondary relation to P-1 and P-0.

### Negative formal/name substrate

- C1 — personal names
- C2 — technical/computing abbreviations and code-like fragments
- C7 — grammar/function words and multilingual fragments
- C9 — numeric strings/years
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 526 | Names/cities/geographic entities | formal-substrate | — | Entity-form organisation without one semantic domain. |
| + | C1 | 421 | Food/medical + retail/lifestyle/freshness | mixed-unresolved | P+0 | Multiple substantial semantic organisations coexist. |
| + | C2 | 392 | Exploration/entrepreneurship/motivation/business | parent:P+0 | P+1 | Goal-directed developmental activity child. |
| + | C3 | 318 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C4 | 298 | Transformations/measurements/interactions/analysis | parent:P+0 | P+1 | Analytical transformation child. |
| + | C5 | 292 | Maths/code punctuation/formatting | formal-substrate | — | Formatting/symbolic organisation. |
| + | C6 | 178 | Film/media/learning/interviews/workshops | parent:P+1 | P+0 | Mediated learning/production child. |
| + | C7 | 145 | Browser/search/session/software systems | parent:P+1 | P+0 | Technical mediation/interface child. |
| + | C8 | 135 | Quantitative/evaluative discourse modifiers | irreducible-semantic | P+0 | Contextual modifier relation. |
| + | C9 | 120 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| + | C10 | 115 | Inevitability/reappearance/reconstruction stems | formal-substrate | — | Lexical/morphological form dominates. |
| + | C11 | 75 | Example-related multilingual morphology | formal-substrate | — | Lexical/morphological organisation. |
| − | C0 | 512 | Administrative characterisation/configuration | parent:P-0 | — | Administrative/descriptive child. |
| − | C1 | 424 | Personal names | formal-substrate | — | Name/entity organisation. |
| − | C2 | 366 | Technical/computing abbreviations | formal-substrate | — | Abbreviation/code form dominates. |
| − | C3 | 349 | Adverse/legal evaluation/jurisdictional constraint | parent:P-0 | — | Evaluative/constraint child. |
| − | C4 | 335 | Cardiovascular/cytokine/immunology/pathology | irreducible-semantic | P-0 | Clinical-state relation. |
| − | C5 | 326 | Regulation/encouragement/activation/deletion | parent:P-0 | — | Institutional/change-operation child. |
| − | C6 | 269 | Family/monarchy/government/mythic roles | parent:P-1 | P-0 | Institutional/authority child. |
| − | C7 | 241 | Grammar/function/multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C8 | 189 | Vehicles/roads/built/material objects | irreducible-semantic | P-1, P-0 | Material-setting relation. |
| − | C9 | 124 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 82 | Geographic entities/regions | parent:P-1 | — | Territorial-identity child. |
| − | C11 | 74 | Maths/code punctuation | formal-substrate | — | Formatting form. |

Every State 18 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Goal-directed development, transformation and quantitative activity | C2, C4 | 690 | 22.9% | 44.0% | High |
| P+1 | Mediated learning, communication and software-interface systems | C6, C7 | 323 | 10.7% | 20.6% | Moderate / High |
| P-0 | Administrative characterisation, adverse constraint and institutional change | C0, C3, C5 | 1,187 | 36.1% | 57.6% | High |
| P-1 | Institutional/familial authority and territorial identity | C6, C10 | 351 | 10.7% | 17.0% | Moderate / High |

Positive retained parents account for **1,013 nodes**, **33.6% of the positive
population** and **64.6% of semantic-eligible positive nodes**.

Negative retained parents account for **1,538 nodes**, **46.7% of the negative
population** and **74.6% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — goal-directed activity and mediated information systems — High.**
   C2–C6 has **270 edges**, C4–C6 **198**, C2–C7 **126** and C4–C7 **153**.
   Developmental/analytical activity is strongly coupled to media, learning and
   software systems without becoming identical to them.

2. **P+0 ↔ C1 — health/retail/lifestyle context — High but unresolved.**
   C1–C2 has **417 edges** and C1–C4 **295**. C1 is strongly embedded in the
   developmental/analytical field, but medical, retail and lifestyle content
   cannot be reduced to one child function.

3. **P+0 ↔ C8 — evaluative/contextual modification — Moderate.**
   C2–C8 has **148 edges** and C4–C8 **81**. C8 behaves as a discourse/modifier
   structure around the substantive process parent.

### Negative-side relations

1. **P-0 ↔ P-1 — organised state control and authority context — High.**
   C0–C6 has **337 edges**, C3–C6 **244**, C5–C6 **119**, C0–C10 **38** and
   C3–C10 **24**. Regulatory/control semantics are strongly situated in
   institutional and authority contexts.

2. **P-0 ↔ C4 — control/characterisation and clinical pathology — High.**
   C0–C4 has **334 edges**, C3–C4 **171** and C5–C4 **122**. Clinical states
   are strongly adjacent to description, evaluation and intervention while
   retaining a distinct medical ontology.

3. **P-1 ↔ C8 — authority and material setting — High.**
   C6–C8 has **153 edges**, mean cosine **0.10119**. Material environments
   support authority/social order without being absorbed into it.

4. **P-0 ↔ C8 — intervention in material settings — Moderate to High.**
   C0–C8 has **265 edges**, C3–C8 **109** and C5–C8 **88**, placing material
   environments within the broader field of state description and change.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 18 cross-side evidence is dominated by lexical/case and
near-form relations such as `Greek`↔` Greek`, `pneum`↔`neum`,
adjacent years, `transmit`↔`transmitting`, and
`height`↔`Height`. These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C1 and negative C4 through biomedical/health structure;
- positive P+1 and negative administrative/technical structures through
  software and mediated information systems.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,446 nodes / 48.0%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation and formatting;
- numeric strings/coded values;
- inevitability/reappearance/reconstruction lexical stems;
- example-related multilingual morphology.

### Negative — 1,229 nodes / 37.3%

- personal names;
- technical/computing abbreviations and code-like forms;
- grammar/function words and multilingual fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 18 — BLOCK 17 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 GOAL-DIRECTED DEVELOPMENT / TRANSFORMATION / QUANTITATIVE ACTIVITY
|   +-- C2 exploration/entrepreneurship/motivation/business
|   `-- C4 transformations/measurements/interactions/analysis
|       |
|       +-- C8 evaluative/contextual discourse         [secondary]
|       `-- C1 health/retail/lifestyle                 [secondary; mixed]
|
+-- P+1 MEDIATED LEARNING / COMMUNICATION / SOFTWARE-INTERFACE SYSTEMS
|   +-- C6 film/media/learning/interviews/workshops
|   `-- C7 browser/search/session/software
|
+-- C1 food/medical + retail/lifestyle/freshness       [mixed unresolved]
+-- C8 quantitative/evaluative discourse               [irreducible]
`-- C0,C3,C5,C9,C10,C11                               [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE CHARACTERISATION / ADVERSE CONSTRAINT / INSTITUTIONAL CHANGE
|   +-- C0 administrative characterisation/configuration
|   +-- C3 adverse/legal evaluation/jurisdictional constraint
|   `-- C5 regulation/encouragement/activation/deletion
|       |
|       +-- C4 cardiovascular/cytokine pathology       [secondary]
|       `-- C8 material environment                    [secondary]
|
+-- P-1 INSTITUTIONAL/FAMILIAL AUTHORITY & TERRITORIAL IDENTITY
|   +-- C6 family/monarchy/government/mythic roles
|   `-- C10 geographic entities/regions
|       \
|        -- C8 vehicles/roads/material setting         [secondary]
|
+-- C4 cardiovascular/cytokine/immunology/pathology    [irreducible]
+-- C8 vehicles/roads/built/material objects            [irreducible]
`-- C1,C2,C7,C9,C11                                   [formal/name substrate]
```

The preferred State 18 reconstruction contains two positive and two negative
multi-community parents. The positive side divides goal-directed
development/quantitative transformation from mediated learning/software
systems. The negative side is dominated by a strongly triangulated
administrative/adverse/change-control structure plus a smaller
institutional-territorial authority structure.

This statement is local to State 18 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C6 into P+0 as a mediated-development child;
2. leave positive C6 and C7 separate rather than retaining P+1;
3. split negative P-0 into administrative C0 and adverse/change C3+C5;
4. pair negative C6 with C8 rather than C10 under an
   **institutional roles and material settings** parent.

The third alternative is the most serious semantically. The preferred P-0 is
retained because C0–C5, C0–C3 and C3–C5 form exceptionally strong
three-way evidence.

## Uncertainty record

- **Positive P+0:** C2 contains business/entrepreneurship while C4 is much more
  quantitative/technical; their high direct relation supports the parent.
- **Positive P+1:** C6 is activity/content oriented and C7 is technical
  infrastructure; the parent remains Moderate/High.
- **Positive C1:** is the principal unresolved positive community because
  health, retail, lifestyle and freshness language coexist.
- **Negative P-0:** broad but supported by three strong pairwise relations.
- **Negative P-1:** C6 is internally mixed across family, government and mythic
  roles; confidence remains Moderate/High.
- **Negative C8:** material-setting semantics are coherent but connect strongly
  to both P-0 and P-1, so it remains irreducible with secondary links.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **3,015 / 3,015**
- Negative node accounting: **3,291 / 3,291**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 18 community inspected at underlying R008 community-record level: **yes**
- All State 18 within-side community relations inspected: **yes**
- State 18 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 18 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 18 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
