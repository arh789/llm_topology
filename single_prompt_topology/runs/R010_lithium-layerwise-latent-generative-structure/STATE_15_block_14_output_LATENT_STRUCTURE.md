# R010 State 15 — Block 14 output latent structure

## State identity

- R010 state index: `15`
- R008/R009 state: `block_14_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **9 positive-head + 13 negative-tail = 22**
- R008 population: **2,469 positive-head + 2,689 negative-tail = 5,158 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 15 only. Retrieval and graph inspection were
restricted to `state_index=15 / block_14_output`. No later-state evidence was
used.

## Evidence inventory

For every State 15 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_15_block_14_output.md`;
2. all 22 State 15 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 15 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed or secondary rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 387 | 1,857 / 1,867 | 14.42 | +0.03146 | Common grammatical/function words and lexical fragments dominate: `as`, `at`, `back`, `making`, `right`, `used`, suffixes/fragments and malformed short forms. |
| C1 | 331 | 1,430 / 1,497 | 13.16 | +0.03243 | Personal names, cities and national/geographic fragments dominate: Berlin, Manchester, Mitchell, Karen, Mumbai, Hamburg, Amsterdam, Bav- and Portug- fragments. |
| C2 | 324 | 1,701 / 899 | 13.27 | +0.03262 | Strong mathematical/code punctuation and software-formatting structure; 187 of 324 tokens are punctuation/symbols, with LaTeX/software residues such as sizeof and mathchoice. |
| C3 | 317 | 1,138 / 1,728 | 12.63 | +0.03314 | Example-related, memory/process and multilingual lexical fragments dominate: remem-, exempl-, exem-, ejemplo, fres-, reappe-, negot-, instit- and multilingual residues. |
| C4 | 300 | 1,184 / 1,680 | 13.49 | +0.03245 | Exploration, development, memory and motivational/process actions dominate: exploring, characterizing, evolving, remembering, motivations, discuss, developments, retrieved, withdrawing, happiness, develops and advancing. |
| C5 | 295 | 1,056 / 1,701 | 12.93 | +0.03200 | Biomedical/respiratory terminology and affective/bodily-action language coexist: dexamethasone, breastfeeding, pulmonary, ventilation, psychiatry fragments and diazepam fragments with happier, kissing and Hit. |
| C6 | 243 | 891 / 1,557 | 13.74 | +0.03241 | Communication, interaction, research and analytical/measurement activity dominate: conversations, interactions, resolving, discussions, adventures, negotiating, management, computed, Measurements, observed, interventions and perturbative. |
| C7 | 144 | 452 / 973 | 13.03 | +0.03285 | Food, business, shopping, healthcare, housing and online-platform terms coexist: Food, business, workshops, shoppers, hospital, healthcare, shopping, hospitals, apartments, Sleep and facebook. |
| C8 | 128 | 691 / 344 | 13.48 | +0.03171 | Numeric strings and short coded values dominate. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 430 | 1,900 / 2,160 | 13.86 | -0.03182 | Scientific/administrative characterisation, distributions and recommendations dominate: Characteristics, downregulation, recommendations, encouragement, distributions, administrator, representation, algorithms, administrators and distribution; extremes include variance, specificity, enactment, codes and algebra. |
| C1 | 376 | 1,549 / 1,690 | 12.73 | -0.03140 | Common grammatical/function words and multilingual lexical fragments dominate. |
| C2 | 342 | 1,395 / 1,676 | 13.06 | -0.03174 | Personal names dominate but biomedical/technical fragments are substantial: Caroline, Jess, Claude, Claud, Connie and Betty with fluor-, olith-, ocr-, ocy- and related fragments. |
| C3 | 304 | 1,330 / 1,773 | 14.58 | -0.03154 | Catastrophe, discrimination, prohibition and intense evaluation dominate: circumstantial, unconstitutional, discriminatory, unbelievable, disastrous, prohibiting, incredible, catastrophe, disproportionate, jurisdictional and catastrophe fragments. |
| C4 | 261 | 1,147 / 1,434 | 14.28 | -0.03185 | Monarchy, religion, family and mythic/fantastical roles coexist: emperor, Constitution, palace, queen, cathedral, church, Empire, Sultan, mother and grandmother; extremes include Uncle, Universe, Beast, Guardian, wedding and heavens. |
| C5 | 217 | 965 / 1,126 | 14.08 | -0.03093 | Cardiovascular disease, immunology and biomedical pathology are coherent: atherosclerotic, cardiovascular, epidemiological, macrophage, dysfunction, interleukin, cytokine/immunofluorescence fragments, monocyte and erythrocytes. |
| C6 | 187 | 677 / 1,034 | 12.77 | -0.03288 | Short technical/computing abbreviations and code-like fragments dominate: TG, GGT, ACC, UU, CE, RF, COMP, LG and related codes. |
| C7 | 163 | 587 / 1,012 | 13.41 | -0.03308 | Vehicles, roads, built environment and material/household objects form a broad physical-world domain: trucks, chassis, bulbs, automobiles, sidewalk, gravel, Rails, roadway and roads. |
| C8 | 139 | 477 / 881 | 13.20 | -0.03150 | Exclusion, deletion, creation and transformation/change actions dominate: enhances, excluding, exclude, Delete, emphasizes, created, eliminated, activate, distorted, toward, creates and Remove. |
| C9 | 105 | 610 / 301 | 14.49 | -0.03089 | Numeric strings, especially historical years, dominate. |
| C10 | 76 | 271 / 488 | 13.55 | -0.03113 | Vocal distress, facial/body actions and anatomy form a coherent embodied-distress cluster: screamed, extremities, glance, shouts, glances, forehead, glare, scream, shoulders and limbs. |
| C11 | 53 | 231 / 291 | 14.21 | -0.03324 | Geographic entities and regions form a coherent territorial domain: Alabama, Georgia, Iowa, Arkansas, Kerala, Florida, Minnesota, Illinois, Nebraska and Argentina. |
| C12 | 36 | 128 / 146 | 11.17 | -0.03019 | Strong mathematical/code punctuation and symbol-formatting cluster; 35 of 36 tokens are punctuation/symbols. |

## Population accounting

### Positive head

Total nodes: **2,469**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 543 | 22.0% |
| Formal/name substrate | 1,487 | 60.2% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 439 | 17.8% |
| Unclear | 0 | 0.0% |
| **Total** | **2,469** | **100.0%** |

Semantic-eligible denominator: **982 nodes**.

### Negative tail

Total nodes: **2,689**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,187 | 44.1% |
| Formal/name substrate | 1,046 | 38.9% |
| Irreducible semantic | 456 | 17.0% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,689** | **100.0%** |

Semantic-eligible denominator: **1,643 nodes**.

## Positive-side reconstruction

### P+0 — Inquiry, interaction and analytical process activity

- **Primary children:** C4, C6
- **Primary nodes:** 543
- **Side-relative coverage:** 22.0%
- **Semantic-eligible coverage:** 55.3%
- **Confidence:** High

**Evidence.** C4 contains exploration, characterisation, development, memory,
retrieval and motivational/process actions. C6 contains conversations,
interactions, resolution, negotiation, management, computation, measurement and
observation. Their direct relation contains **407 token edges**, mean cosine
**0.09922**, the strongest clearly semantic positive relation in the state. The
common generator is goal-directed inquiry and analytical activity carried out
through interaction, communication and measurement.

**Secondary links:** C5 and C7. C4–C5 has **280 edges**, C6–C5 **207**, while
C4–C7 has **124** and C6–C7 **172**. Biomedical/embodied and
commercial/healthcare contexts are strongly adjacent without becoming clean
children.

**Exclusion boundary.** C4 is process/action centred; C6 combines social
communication and analytical/physical measurement. C5 remains mixed across
biomedical and affective/bodily action. C7 spans unrelated commerce, healthcare,
housing and platform concepts.

**Alternative.** Absorb C5 under a broader
`inquiry, interaction and embodied/clinical activity` parent. Rejected because
C5's biomedical and affective/bodily-action mixture is not generated
specifically by inquiry/analysis.

### Positive mixed unresolved structures

- **C5 — mixed-unresolved:** biomedical/respiratory and affective/bodily-action
  semantics coexist; secondary relation to P+0.
- **C7 — mixed-unresolved:** food, commerce, healthcare, housing and online
  platforms coexist; secondary relation to P+0.

### Positive formal/name substrate

- C0 — grammar/function words and lexical fragments
- C1 — personal names/geographic entities
- C2 — mathematical/code punctuation and software-formatting strings
- C3 — example/memory/process and multilingual lexical fragments
- C8 — numeric strings/coded values

## Negative-side reconstruction

### P-0 — Characterisation, adverse constraint and transformation

- **Primary children:** C0, C3, C8
- **Primary nodes:** 873
- **Side-relative coverage:** 32.5%
- **Semantic-eligible coverage:** 53.1%
- **Confidence:** High

**Evidence.** C0 contains scientific/administrative characterisation,
recommendations, distributions and representation. C3 contains catastrophe,
discrimination, prohibition and intense evaluation. C8 contains exclusion,
deletion, creation and transformation/change actions. The structure is strongly
triangulated: C0–C3 has **447 token edges**, mean cosine **0.10178**; C0–C8
**270** at **0.10021**; C3–C8 **202** at **0.10026**. The higher-order
generator is the characterisation, judgement and alteration of problematic,
constrained or disallowed states.

**Secondary links:**
- **C5:** C0–C5 has **228 edges** and C3–C5 **125**, placing biomedical
  pathology adjacent to characterisation/adversity.
- **C10:** C3–C10 has **117 edges**, linking embodied distress to the adverse
  branch.

**Exclusion boundary.** C0 includes neutral administrative/scientific
description; C3 is evaluative/prohibitive; C8 includes constructive creation
and activation as well as deletion/exclusion. The parent therefore cannot be
reduced to “negative evaluation”, “prohibition” or “destruction”.

**Alternative.** Split C0 into a neutral characterisation parent and retain
C3+C8 as adverse/prohibitive transformation. This is semantically defensible,
but the three-way graph support is strong enough to retain the higher-order
parent.

### P-1 — Institutional/familial roles and territorial identity

- **Primary children:** C4, C11
- **Primary nodes:** 314
- **Side-relative coverage:** 11.7%
- **Semantic-eligible coverage:** 19.1%
- **Confidence:** Moderate

**Evidence.** C4 contains monarchy, religion, family and mythic/social roles;
C11 contains geographic regions. Their direct relation contains **74 token
edges**, mean cosine **0.10107**. The common generator is social/institutional
order situated within territorial identity.

**Secondary link:** C7. C4–C7 has **170 edges**, mean cosine **0.09681**,
showing that built/material environments provide settings for roles and public
order without becoming institutional roles themselves.

**Exclusion boundary.** C4 contains family and mythic/fantastical roles as well
as formal institutions; C11 is geographic rather than institutional. C7 is
material setting, not authority or territory.

**Alternative.** Pair C4 with C7 under a broader
`social roles and material settings` parent. That alternative has greater
edge count but weaker semantic discrimination; P-1 retains C11 instead and
records C7 as a secondary material-setting relation.

### Negative irreducible structures

- **C5 — irreducible-semantic:** cardiovascular disease, immunology and
  biomedical pathology; secondary relation to P-0.
- **C7 — irreducible-semantic:** vehicles, roads, built environment and
  material/household objects; secondary relation to P-1.
- **C10 — irreducible-semantic:** vocal distress, facial/body actions and
  anatomy; secondary relation to P-0.

### Negative formal/name substrate

- C1 — grammar/function words and multilingual lexical fragments
- C2 — personal names plus biomedical/technical fragments
- C6 — short technical/computing abbreviations and code-like fragments
- C9 — numeric strings/years
- C12 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 387 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C1 | 331 | Personal names/cities/geographic fragments | formal-substrate | — | Name/entity organisation without one semantic domain. |
| + | C2 | 324 | Maths/code punctuation/software formatting | formal-substrate | — | Formatting/tokeniser organisation dominates. |
| + | C3 | 317 | Example/memory/process/multilingual fragments | formal-substrate | — | Lexical/morphological organisation dominates. |
| + | C4 | 300 | Exploration/development/memory/process actions | parent:P+0 | — | Inquiry/process-action child. |
| + | C5 | 295 | Biomedical/respiratory + affective/bodily actions | mixed-unresolved | P+0 | Two substantial semantic organisations coexist. |
| + | C6 | 243 | Communication/interaction/research/measurement | parent:P+0 | — | Interactive analytical-process child. |
| + | C7 | 144 | Food/business/shopping/healthcare/housing/platforms | mixed-unresolved | P+0 | Broad multi-domain partition. |
| + | C8 | 128 | Numeric strings/coded values | formal-substrate | — | Numeric/form organisation. |
| − | C0 | 430 | Scientific/admin characterisation/distributions | parent:P-0 | — | Characterisation branch. |
| − | C1 | 376 | Grammar/function/multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C2 | 342 | Personal names + biomedical/technical fragments | formal-substrate | — | Name/form organisation without one semantic class. |
| − | C3 | 304 | Catastrophe/discrimination/prohibition/intensity | parent:P-0 | — | Adverse/prohibitive branch. |
| − | C4 | 261 | Monarchy/religion/family/mythic roles | parent:P-1 | — | Institutional/familial-role child. |
| − | C5 | 217 | Cardiovascular/immunology/pathology | irreducible-semantic | P-0 | Clinical/pathology relation. |
| − | C6 | 187 | Technical/computing abbreviations/code fragments | formal-substrate | — | Abbreviation/code form dominates. |
| − | C7 | 163 | Vehicles/roads/built/material objects | irreducible-semantic | P-1 | Material-setting relation. |
| − | C8 | 139 | Exclusion/deletion/creation/transformation | parent:P-0 | — | Change/constraint-operation branch. |
| − | C9 | 105 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 76 | Vocal distress/body actions/anatomy | irreducible-semantic | P-0 | Embodied adverse-state relation. |
| − | C11 | 53 | Geographic entities/regions | parent:P-1 | — | Territorial-identity child. |
| − | C12 | 36 | Maths/code punctuation | formal-substrate | — | Formatting form. |

Every State 15 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Inquiry, interaction and analytical process activity | C4, C6 | 543 | 22.0% | 55.3% | High |
| P-0 | Characterisation, adverse constraint and transformation | C0, C3, C8 | 873 | 32.5% | 53.1% | High |
| P-1 | Institutional/familial roles and territorial identity | C4, C11 | 314 | 11.7% | 19.1% | Moderate |

Positive retained parents account for **543 nodes**, **22.0% of the positive
population** and **55.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,187 nodes**, **44.1% of the negative
population** and **72.2% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ C5 — inquiry and biomedical/embodied relation — High.**
   C4–C5 has **280 edges**, and C6–C5 **207**. C5 is strongly adjacent to the
   inquiry/interaction parent, but its internal biomedical-versus-affective
   mixture blocks primary absorption.

2. **P+0 ↔ C7 — organised activity and commercial/healthcare context — Moderate.**
   C4–C7 has **124 edges** and C6–C7 **172**. The relation is substantial, but
   C7 spans commerce, healthcare, housing and online platforms rather than one
   generative child domain.

3. **Formal communities remain highly connected without being promoted.**
   For example, C0–C4 has **422 edges** and C0–C6 **339**. High graph
   connectivity alone does not override the predominantly lexical/formal
   organisation of C0.

### Negative-side relations

1. **P-0 ↔ P-1 — adverse/constraint semantics in institutional context — Moderate to High.**
   C0–C4 has **306 edges**, C3–C4 **243**, C0–C11 **31** and C3–C11 **9**.
   The relation is driven mainly through the institutional-role child rather
   than the geographic child.

2. **P-0 ↔ C5 — analytical/adverse and clinical pathology — High.**
   C0–C5 has **228 edges**, C3–C5 **125** and C8–C5 **58**. Biomedical pathology
   is strongly adjacent to state characterisation and adverse judgement while
   remaining a distinct medical domain.

3. **P-1 ↔ C7 — institutional roles and material setting — High.**
   C4–C7 has **170 edges**, mean cosine **0.09681**. Material environments
   strongly contextualise social/institutional roles.

4. **P-0 ↔ C10 — adverse evaluation and embodied distress — Moderate.**
   C3–C10 has **117 edges** and C0–C10 **65**, supporting an embodied
   distress/intensity satellite.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-0 through characterisation/analysis;
- positive C5 and negative C5/P-0 through biomedical/clinical structure;
- positive C1 and negative P-1 through geographic identity;
- positive C7 and negative material/technical structures through healthcare,
  housing and platform contexts.

No parent-level bridge is promoted without direct cross-side community
evidence sufficient to distinguish semantic structure from lexical proximity.

## Formal/representational substrate

### Positive — 1,487 nodes / 60.2%

- grammar/function words and lexical fragments;
- personal-name/geographic entity organisation;
- mathematical/code punctuation and formatting;
- example/memory/process and multilingual lexical fragments;
- numeric/coded values.

### Negative — 1,046 nodes / 38.9%

- grammar/function words and multilingual lexical fragments;
- personal names plus biomedical/technical fragments;
- technical/computing abbreviations and code-like fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 15 — BLOCK 14 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INQUIRY / INTERACTION / ANALYTICAL PROCESS ACTIVITY
|   +-- C4 exploration/development/memory/process actions
|   `-- C6 communication/interaction/research/measurement
|       |
|       +-- C5 biomedical + affective/bodily actions  [secondary; mixed]
|       `-- C7 commerce/healthcare/housing/platforms  [secondary; mixed]
|
+-- C5 biomedical/respiratory + affective/body        [mixed unresolved]
+-- C7 food/business/healthcare/housing/platforms     [mixed unresolved]
`-- C0,C1,C2,C3,C8                                  [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 CHARACTERISATION / ADVERSE CONSTRAINT / TRANSFORMATION
|   +-- C0 scientific/admin characterisation
|   +-- C3 catastrophe/discrimination/prohibition
|   `-- C8 exclusion/deletion/creation/change
|       |
|       +-- C5 cardiovascular/immunology/pathology    [secondary]
|       `-- C10 vocal/body distress                   [secondary]
|
+-- P-1 INSTITUTIONAL/FAMILIAL ROLES & TERRITORIAL IDENTITY
|   +-- C4 monarchy/religion/family/mythic roles
|   `-- C11 geographic entities/regions
|       \
|        -- C7 material/built setting                 [secondary]
|
+-- C5 cardiovascular/immunology/pathology            [irreducible]
+-- C7 vehicles/roads/built/material objects           [irreducible]
+-- C10 vocal distress/body actions/anatomy            [irreducible]
`-- C1,C2,C6,C9,C12                                  [formal/name substrate]
```

The preferred State 15 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by formal/name
substrate and two large mixed semantic communities, so broader compression
would be artificial. The negative side contains a strongly triangulated
characterisation/adverse/transformation structure plus a smaller
institutional-territorial parent.

This statement is local to State 15 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C5 into P+0 under a broader
   **inquiry, interaction and embodied/clinical activity** parent;
2. split negative P-0 into neutral characterisation C0 and
   adverse/prohibitive transformation C3+C8;
3. pair negative C4 with C7 instead of C11 under a broad
   **social roles and material settings** parent;
4. leave negative C4 and C11 separate rather than retaining P-1.

The second alternative is the most serious semantically. The preferred P-0 is
retained because C0–C3, C0–C8 and C3–C8 are all strong, giving genuine
three-way support rather than one incidental edge.

## Uncertainty record

- **Positive P+0:** C6 spans communication, interaction, analytical measurement
  and physical-system language; the parent remains coherent because C4 supplies
  the common inquiry/process axis.
- **Positive C5:** biomedical and affective/bodily-action structures are both
  substantial, so no clean primary parent is assigned.
- **Positive C7:** commerce, healthcare, housing and platform content is too
  broad for a discriminative parent.
- **Negative P-0:** neutral administrative/scientific characterisation and
  adverse/prohibitive semantics remain distinct child functions.
- **Negative P-1:** C4–C11 has high mean similarity but moderate edge count;
  confidence remains Moderate.
- **Negative C5/C7/C10:** all are semantically coherent but lack sufficiently
  discriminative sibling structures for additional parents.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **9 / 9**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **22 / 22**
- Positive node accounting: **2,469 / 2,469**
- Negative node accounting: **2,689 / 2,689**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 15 community inspected at underlying R008 community-record level: **yes**
- All State 15 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 15 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 15 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
