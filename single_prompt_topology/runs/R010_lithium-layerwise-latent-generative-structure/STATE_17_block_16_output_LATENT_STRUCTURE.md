# R010 State 17 — Block 16 output latent structure

## State identity

- R010 state index: `17`
- R008/R009 state: `block_16_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 10 negative-tail = 23**
- R008 population: **2,733 positive-head + 2,938 negative-tail = 5,671 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 17 only. Retrieval and graph inspection were
restricted to `state_index=17 / block_16_output`. No later-state evidence was
used.

## Evidence inventory

For every State 17 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_17_block_16_output.md`;
2. all 23 State 17 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 17 within-side relation set in
   `R008/community_edges.csv`;
4. the State 17 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 350 | 1,348 / 2,057 | 13.58 | +0.03172 | Anticipation, development, observation, outcomes and motivation dominate: anticipated, Measurements, anticipation, development, evolving, recorded, happiness, observed, yields, ignored, motivation and develops. |
| C1 | 315 | 1,104 / 1,880 | 12.98 | +0.03243 | Exploration, inevitability/re-emergence and evaluative change coexist: exploring, inevitability/unavoidability fragments, discuss, resolving, Emer-, explores, Fresh, reappe- and controversy fragments. |
| C2 | 287 | 1,055 / 1,686 | 13.23 | +0.03157 | Transformation, interaction, coupling and analytical/relational structure dominate: transformations, determinations, interactions, characterizing, values, coupling, partnerships, results, perturbative, interacting and interventions. |
| C3 | 280 | 1,375 / 1,625 | 15.63 | +0.03121 | Common grammatical/function words and lexical fragments dominate. |
| C4 | 280 | 1,533 / 771 | 13.70 | +0.03289 | Mathematical/code punctuation and symbolic formatting dominate; 180 of 280 tokens are punctuation/symbols. |
| C5 | 248 | 955 / 1,523 | 13.84 | +0.03165 | Business/social activity, food, health, media and institutional terms coexist: entrepreneurs, Food, breastfeeding, conversations, businesses, adventures, negotiating, filmmakers, sleeping, terrorists and Medical. |
| C6 | 224 | 984 / 1,090 | 13.65 | +0.03231 | Cities, regions and personal/geographic names form a coherent entity domain: Manchester, Matt, Bristol, Kashmir, Hamburg, Stockholm, Pakistan fragments, Jay, Karen and Krish. |
| C7 | 218 | 770 / 1,342 | 13.22 | +0.03150 | Biomedical imaging, psychiatry, respiratory medicine and pharmacology are coherent: dexamethasone, psychiatry fragments, imaging, analgesic, pulmonary, pneumonia fragments, ventilation, dopaminergic and related terms. |
| C8 | 176 | 635 / 1,027 | 13.05 | +0.03114 | Discourse, sequencing, evaluation and contextual modifiers dominate: Next, surprisingly, Using, More, Having, Clearly, Wednesday, Estim-, With, interesting and illuminating. |
| C9 | 148 | 531 / 744 | 12.20 | +0.03228 | Example-related multilingual words and orthographic/tokenisation fragments dominate. |
| C10 | 122 | 734 / 238 | 13.98 | +0.03058 | Numeric strings and short coded values dominate. |
| C11 | 56 | 142 / 377 | 11.80 | +0.03076 | Short technical/scientific abbreviations and measurement/medical codes dominate. |
| C12 | 29 | 82 / 232 | 13.66 | +0.03237 | Learning, reading, writing and play form a coherent small semantic domain: Learning, Read, plays, Play, games, Writing, readings, Reading, playful and learning. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 522 | 2,430 / 2,417 | 13.94 | -0.03103 | Regulation, adverse evaluation, recommendation and constraint dominate: circumstantial, disproportionate, unconstitutional, recommendations, encouragement, downregulation, discriminatory, unbelievable, prohibiting, incredible and Specific. |
| C1 | 475 | 2,075 / 2,069 | 13.09 | -0.03106 | Personal names dominate but lexical/technical fragments remain substantial: Caroline, Laura, Connie, Sarah, Claire and Emily coexist with crypt-, ocr-, heter-, ocy- and Comp fragments. |
| C2 | 380 | 1,582 / 2,164 | 14.02 | -0.03124 | Administrative/configuration language and family/social-role vocabulary coexist: Characteristics, Configuration, administrators, representation, administrator, regulations, distribution and characteristics with mother/grandmother; extremes include Uncle, specificity, variance and Executive. |
| C3 | 346 | 1,376 / 1,660 | 12.75 | -0.03105 | Common grammatical/function words and multilingual lexical fragments dominate. |
| C4 | 342 | 1,512 / 1,640 | 13.64 | -0.03106 | Cardiovascular disease, cytokine biology, immunology and pathology are coherent: cardiovascular, atherosclerotic, cytokines, macrophage, monocyte, IGF, epidemiological, staphylococcus fragments and phenotype. |
| C5 | 290 | 1,335 / 1,494 | 14.36 | -0.03127 | Monarchy, government, geography and mythic/conflict roles coexist: palace, emperor, Alabama, king, Constitution, empire, dragon, Chicago, queen, warriors and goddess. |
| C6 | 274 | 1,093 / 1,502 | 13.46 | -0.03205 | Vehicles/material objects coexist with anatomy, weapons and distress: automobiles, trucks, circumferential, vegetables, gravel, pavement, extremities, furniture, firearms, screamed, chassis and disgrace. |
| C7 | 129 | 466 / 767 | 13.17 | -0.03169 | Technical/infrastructure abbreviations coexist with Soviet/political entities: TC, TG, GGT, Rails, USSR, ACC, SSH and related codes; extremes include LCD, CPU, Putin and Stalin. |
| C8 | 113 | 652 / 306 | 14.25 | -0.02960 | Numeric strings, especially historical years, dominate. |
| C9 | 67 | 244 / 269 | 11.30 | -0.03032 | Mathematical/code punctuation and symbol formatting dominate; 52 of 67 tokens are punctuation/symbols. |

## Population accounting

### Positive head

Total nodes: **2,733**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 952 | 34.8% |
| Formal/name substrate | 1,110 | 40.6% |
| Irreducible semantic | 423 | 15.5% |
| Mixed unresolved | 248 | 9.1% |
| Unclear | 0 | 0.0% |
| **Total** | **2,733** | **100.0%** |

Semantic-eligible denominator: **1,623 nodes**.

### Negative tail

Total nodes: **2,938**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,466 | 49.9% |
| Formal/name substrate | 1,001 | 34.1% |
| Irreducible semantic | 342 | 11.6% |
| Mixed unresolved | 129 | 4.4% |
| Unclear | 0 | 0.0% |
| **Total** | **2,938** | **100.0%** |

Semantic-eligible denominator: **1,937 nodes**.

## Positive-side reconstruction

### P+0 — Developmental, transformational and evaluative process organisation

- **Primary children:** C0, C1, C2
- **Primary nodes:** 952
- **Side-relative coverage:** 34.8%
- **Semantic-eligible coverage:** 58.7%
- **Confidence:** High

**Evidence.** C0 contains anticipation, development, observation, outcomes and
motivation. C1 contains exploration, re-emergence, resolution and evaluative
change. C2 contains transformation, interaction, coupling and analytical
relations. The three-child structure is strongly connected: C0–C2 has **361
token edges**, mean cosine **0.09742**; C0–C1 **312** at **0.09327**; C1–C2
**202** at **0.09082**. The common generator is process-state evolution:
systems or situations are anticipated, explored, transformed, observed and
evaluated through their interactions and outcomes.

**Secondary link:** C8. C0–C8 has **257 edges**, mean cosine **0.09683**;
C1–C8 has **133** and C2–C8 **94**. C8 supplies sequencing and evaluative
modifiers around the process architecture without becoming a substantive child.

**Secondary link:** C5. C0–C5 has **299 edges**, C1–C5 **182**, C2–C5 **266**.
Its social/business/health/media mixture is highly connected to process
activity but lacks one discriminative child identity.

**Exclusion boundary.** C0 is outcome/development oriented, C1
exploration/change oriented and C2 relational/transformational. C8 is mostly
contextual/discourse modification. C5 is too heterogeneous for primary
absorption.

**Alternative.** Include C8 as a fourth child under a broader
`process evolution and contextual evaluation` parent. Rejected because C8
functions more like a modifier layer than an independent generating domain.

### Positive irreducible and unresolved structures

- **C5 — mixed-unresolved:** business/social activity, food, health, media and
  institutional concepts coexist; secondary relation to P+0 and to C7.
- **C7 — irreducible-semantic:** biomedical imaging, psychiatry, respiratory
  medicine and pharmacology; strong relation to C5 but no clean second medical
  child supports a separate parent.
- **C8 — irreducible-semantic:** discourse, sequencing, evaluation and
  contextual modifiers; secondary relation to P+0.
- **C12 — irreducible-semantic:** learning, reading, writing and play.

### Positive formal/name substrate

- C3 — grammar/function words/fragments
- C4 — mathematical/code punctuation and formatting
- C6 — cities, regions and personal/geographic names
- C9 — example-related multilingual/tokenisation forms
- C10 — numeric strings/coded values
- C11 — technical/scientific abbreviations and codes

## Negative-side reconstruction

### P-0 — Regulatory characterisation, administrative configuration and social organisation

- **Primary children:** C0, C2
- **Primary nodes:** 902
- **Side-relative coverage:** 30.7%
- **Semantic-eligible coverage:** 46.6%
- **Confidence:** High

**Evidence.** C0 contains regulation, recommendation, adverse evaluation and
constraint. C2 contains Characteristics, Configuration, administrators,
representation, regulations, distribution and family/social-role language.
Their direct relation contains **784 token edges**, mean cosine **0.09884**,
by far the strongest State 17 negative semantic relation. The common generator
is the description and configuration of organised social or institutional
states: structures are characterised, administered, regulated, recommended,
constrained or altered.

**Secondary links:**
- **C4:** C0–C4 has **310 edges** and C2–C4 **288**, placing clinical/pathology
  characterisation strongly adjacent to the parent.
- **C5:** C0–C5 has **258 edges** and C2–C5 **270**, linking authority,
  government and social-order material to regulatory/administrative structure.
- **C6:** C0–C6 has **342 edges** and C2–C6 **227**, showing a strong relation
  to material/conflict settings.

**Exclusion boundary.** C0 includes adverse evaluative language beyond neutral
administration. C2 includes family/social roles beyond administrative
configuration. C5 is not absorbed because monarchy, geography, mythic and
conflict material form a broader authority/context domain.

**Alternative.** Expand P-0 to C0+C2+C5 under a broader
`institutional regulation and authority` parent. Rejected because doing so
would erase the distinction between configuring/regulating a system and the
social/political actors or settings within that system.

### P-1 — Institutional/conflict roles and material-embodied environments

- **Primary children:** C5, C6
- **Primary nodes:** 564
- **Side-relative coverage:** 19.2%
- **Semantic-eligible coverage:** 29.1%
- **Confidence:** Moderate

**Evidence.** C5 contains monarchy, government, geography and mythic/conflict
roles. C6 contains vehicles, material objects, weapons, anatomy and distress.
Their direct relation contains **234 token edges**, mean cosine **0.09477**.
The common generator is an institutional/conflict environment composed of
actors, authority structures and the material/embodied settings in which
conflict or social order is represented.

**Secondary link:** C7. C5–C7 has **70 edges** and C6–C7 **67**. Its
technical/infrastructure component fits the material setting, while USSR/Putin/
Stalin content fits the political side, but the mixture prevents primary
absorption.

**Exclusion boundary.** C5 contains ordinary government/geography as well as
mythic/conflict roles; C6 contains ordinary vehicles, furniture and terrain as
well as firearms/distress. The parent is not narrowed to “violence” or
broadened to generic physical/social reality.

**Alternative.** Leave C5 and C6 separate. This remains a serious alternative,
so confidence is Moderate.

### Negative irreducible and unresolved structures

- **C4 — irreducible-semantic:** cardiovascular/cytokine/immunological
  pathology; secondary relation to P-0.
- **C7 — mixed-unresolved:** technical/infrastructure abbreviations and
  Soviet/political entities coexist; secondary relation to P-1.

### Negative formal/name substrate

- C1 — personal names plus lexical/technical fragments
- C3 — grammar/function words and multilingual fragments
- C8 — numeric strings/years
- C9 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 350 | Anticipation/development/observation/outcomes | parent:P+0 | — | Developmental/outcome process child. |
| + | C1 | 315 | Exploration/re-emergence/evaluative change | parent:P+0 | — | Exploration/change child. |
| + | C2 | 287 | Transformation/interaction/coupling/analysis | parent:P+0 | — | Relational/transformation child. |
| + | C3 | 280 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C4 | 280 | Maths/code punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C5 | 248 | Business/social + food/health/media/institution | mixed-unresolved | P+0 | Multiple semantic organisations coexist. |
| + | C6 | 224 | Cities/regions/personal-geographic names | formal-substrate | — | Name/entity organisation. |
| + | C7 | 218 | Biomedical imaging/psychiatry/respiratory | irreducible-semantic | C5 | Distinct medical domain without a sibling parent. |
| + | C8 | 176 | Discourse/sequencing/evaluation/modifiers | irreducible-semantic | P+0 | Contextual/evaluative modifier structure. |
| + | C9 | 148 | Example-related multilingual/tokeniser forms | formal-substrate | — | Lexical/tokenisation organisation. |
| + | C10 | 122 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| + | C11 | 56 | Technical/scientific abbreviations/codes | formal-substrate | — | Abbreviation form dominates. |
| + | C12 | 29 | Learning/reading/writing/play | irreducible-semantic | — | Coherent small semantic domain. |
| − | C0 | 522 | Regulation/adverse evaluation/recommendation | parent:P-0 | — | Regulatory/constraint child. |
| − | C1 | 475 | Personal names + lexical/technical fragments | formal-substrate | — | Name/form organisation. |
| − | C2 | 380 | Admin/configuration + family/social roles | parent:P-0 | P-1 | Administrative/configuration child with social-role spillover. |
| − | C3 | 346 | Grammar/function/multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 342 | Cardiovascular/cytokine/immunology/pathology | irreducible-semantic | P-0 | Clinical-state characterisation relation. |
| − | C5 | 290 | Monarchy/government/geography/mythic-conflict roles | parent:P-1 | P-0 | Institutional/conflict actor child. |
| − | C6 | 274 | Vehicles/material/anatomy/weapons/distress | parent:P-1 | P-0 | Material/embodied environment child. |
| − | C7 | 129 | Technical infrastructure + Soviet/political entities | mixed-unresolved | P-1 | Two organising structures coexist. |
| − | C8 | 113 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 67 | Maths/code punctuation | formal-substrate | — | Formatting form. |

Every State 17 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Developmental, transformational and evaluative process organisation | C0, C1, C2 | 952 | 34.8% | 58.7% | High |
| P-0 | Regulatory characterisation, administrative configuration and social organisation | C0, C2 | 902 | 30.7% | 46.6% | High |
| P-1 | Institutional/conflict roles and material-embodied environments | C5, C6 | 564 | 19.2% | 29.1% | Moderate |

Positive retained parents account for **952 nodes**, **34.8% of the positive
population** and **58.7% of semantic-eligible positive nodes**.

Negative retained parents account for **1,466 nodes**, **49.9% of the negative
population** and **75.7% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ C5 — process and social/business/health activity — High.**
   C0–C5 has **299 edges**, C1–C5 **182**, and C2–C5 **266**. The mixed C5
   population is deeply embedded in process organisation without yielding one
   clean child identity.

2. **P+0 ↔ C7 — process and biomedical relation — High.**
   C0–C7 has **194 edges**, C1–C7 **252**, and C2–C7 **191**. Biomedical
   content is strongly connected to process/evaluation while remaining a
   distinct medical domain.

3. **P+0 ↔ C8 — process and contextual evaluation — High.**
   C0–C8 has **257 edges**, C1–C8 **133**, and C2–C8 **94**. C8 acts as a
   modifier/context layer rather than a coequal generating domain.

4. **C5 ↔ C7 — health/social adjacency — High.**
   Their direct relation has **208 edges**, mean cosine **0.09869**, but C5's
   business/media/institutional material blocks a clean health parent.

### Negative-side relations

1. **P-0 ↔ P-1 — regulation/configuration and institutional-material context — High.**
   C0–C5 has **258 edges**, C0–C6 **342**, C2–C5 **270**, and C2–C6 **227**.
   Regulatory/administrative structure is strongly embedded in social authority
   and material/conflict contexts without becoming identical to them.

2. **P-0 ↔ C4 — regulatory/administrative and clinical characterisation — High.**
   C0–C4 has **310 edges** and C2–C4 **288**. Clinical pathology is strongly
   adjacent to the parent but remains a distinct medical ontology.

3. **P-1 ↔ C7 — political/technical setting — Moderate.**
   C5–C7 has **70 edges**, C6–C7 **67**. Technical infrastructure and Soviet
   political entities bridge both children, but their mixed organisation
   prevents primary inclusion.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 17 cross-side evidence is dominated by lexical/case and
near-form relations such as `Greek`↔` Greek`, `Mot`↔`mot`, adjacent
years, `height`↔`Height`, and `anest`↔`anesthesia`. These do not
establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/evaluation;
- positive C7 and negative C4 through biomedical/clinical structure;
- positive C6 and negative P-1 through geographic/institutional context.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,110 nodes / 40.6%

- grammar/function words and fragments;
- mathematical/code punctuation and formatting;
- cities/regions/personal-name entity organisation;
- multilingual/example-related tokenisation forms;
- numeric strings;
- technical/scientific abbreviations.

### Negative — 1,001 nodes / 34.1%

- personal names plus lexical/technical fragments;
- grammar/function words and multilingual fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 17 — BLOCK 16 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 DEVELOPMENTAL / TRANSFORMATIONAL / EVALUATIVE PROCESS ORGANISATION
|   +-- C0 anticipation/development/observation/outcomes
|   +-- C1 exploration/re-emergence/evaluative change
|   `-- C2 transformation/interaction/coupling/analysis
|       |
|       +-- C8 discourse/sequencing/evaluation         [secondary]
|       +-- C5 social/business/health/media             [secondary; mixed]
|       `-- C7 biomedical/clinical                     [secondary]
|
+-- C5 business/social + food/health/media             [mixed unresolved]
+-- C7 biomedical imaging/psychiatry/respiratory       [irreducible]
+-- C8 discourse/sequencing/contextual modifiers       [irreducible]
+-- C12 learning/reading/writing/play                   [irreducible]
`-- C3,C4,C6,C9,C10,C11                               [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY CHARACTERISATION / ADMINISTRATIVE CONFIGURATION / SOCIAL ORGANISATION
|   +-- C0 regulation/adverse evaluation/recommendation
|   `-- C2 administration/configuration + social roles
|       |
|       +-- C4 cardiovascular/cytokine pathology       [secondary]
|       `-- P-1 institutional/material context         [related]
|
+-- P-1 INSTITUTIONAL/CONFLICT ROLES & MATERIAL-EMBODIED ENVIRONMENTS
|   +-- C5 monarchy/government/geography/conflict roles
|   `-- C6 vehicles/material/anatomy/weapons/distress
|       \
|        -- C7 technical infrastructure + politics    [secondary; mixed]
|
+-- C4 cardiovascular/cytokine/immunology/pathology    [irreducible]
+-- C7 technical infrastructure + Soviet/political     [mixed unresolved]
`-- C1,C3,C8,C9                                       [formal/name substrate]
```

The preferred State 17 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by a broad but
well-supported process-evolution architecture. The negative side separates an
exceptionally strong regulatory/administrative configuration structure from a
more heterogeneous institutional/conflict and material-environment structure.

This statement is local to State 17 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. include positive C8 under P+0 as a fourth contextual/evaluative child;
2. create a positive health/social parent from C5+C7;
3. expand negative P-0 to C0+C2+C5 under a broader
   **institutional regulation and authority** parent;
4. leave negative C5 and C6 separate rather than retaining P-1.

The third alternative gives greater compression, but the preferred
reconstruction preserves the distinction between regulating/configuring an
organised system and the authority actors/material settings represented within
that system.

## Uncertainty record

- **Positive P+0:** broad, but all three children are independently semantic and
  mutually connected; confidence is High.
- **Positive C5:** is the main positive unresolved community because business,
  social, food, health and media content coexist.
- **Positive C8:** is semantically coherent but modifier-like, so it is not
  forced into P+0.
- **Negative P-0:** C2 contains family/social-role material as well as
  administrative/configuration language, but the C0–C2 relation is
  exceptionally strong.
- **Negative P-1:** C5 and C6 are broad mixed domains; confidence remains
  Moderate.
- **Negative C7:** technical infrastructure and Soviet/political identities
  coexist without one sufficient parent.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **10 / 10**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,733 / 2,733**
- Negative node accounting: **2,938 / 2,938**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 17 community inspected at underlying R008 community-record level: **yes**
- All State 17 within-side community relations inspected: **yes**
- State 17 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 17 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 17 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
