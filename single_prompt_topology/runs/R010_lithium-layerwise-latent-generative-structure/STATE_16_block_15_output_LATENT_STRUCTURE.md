# R010 State 16 — Block 15 output latent structure

## State identity

- R010 state index: `16`
- R008/R009 state: `block_15_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 12 negative-tail = 23**
- R008 population: **2,550 positive-head + 2,643 negative-tail = 5,193 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 16 only. Retrieval and graph inspection were
restricted to `state_index=16 / block_15_output`. No later-state evidence was
used.

## Evidence inventory

For every State 16 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_16_block_15_output.md`;
2. all 23 State 16 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 16 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 544 | 2,431 / 2,073 | 12.75 | +0.03232 | Personal names and geographic/name-like entities dominate, but lexical and multilingual residue remains substantial: Manchester, Jay, Mitchell, Karen, Hamburg, Berlin and Krish coexist with remem-, Portug-, Compan-, prem- and malformed fragments. |
| C1 | 419 | 1,733 / 2,222 | 13.58 | +0.03226 | Transformations, interactions, exploration and developmental/measurement processes dominate: transformations, interactions, exploring, anticipated, development, Measurements, resolving, characterizing, discuss, ignored, evolving and recorded. |
| C2 | 294 | 1,166 / 1,679 | 13.64 | +0.03199 | Food/health and affective-social experience coexist with interview/intervention language: Food, breastfeeding, happiness, adventures, negotiating, discomfort, interviews, conversations, compassion, remembering, mindfulness and interventions. |
| C3 | 264 | 1,199 / 1,545 | 14.94 | +0.03189 | Common grammatical/function words and lexical fragments dominate. |
| C4 | 243 | 877 / 1,431 | 13.11 | +0.03187 | Biomedical, respiratory, imaging and analgesic/psychiatric terminology dominates: dexamethasone, pulmonary, fibres, analgesic, imaging, pneumonia fragments, ventilation, psychiatry fragments and related terms. |
| C5 | 192 | 1,126 / 457 | 14.11 | +0.03275 | Mathematical/code punctuation and symbolic formatting dominate; 161 of 192 tokens are punctuation/symbols. |
| C6 | 177 | 561 / 1,058 | 12.32 | +0.03252 | Management, platform/software and technical publishing/interface concepts form a recognisable technical-system domain: management, Notification, platforms, Length, PhysRev, Resolver, javase, setlength and Address, with implementation residues in the extremes. |
| C7 | 121 | 417 / 740 | 13.01 | +0.03255 | Temporal/discourse sequencing, evaluation and action language dominates: Next, Got, With, adopting, More, Clearly, Now, Wednesday and Working; extremes include Coming, obvious, True and thank. |
| C8 | 110 | 323 / 813 | 13.26 | +0.03289 | Reappearance, renewal/transformation and bodily/sound actions coexist: reappe-, unve-, reconst-, fres-, Fresh, diseng-, rings, Hit, swung, conjug-, manoeuvre fragments and recycling. |
| C9 | 109 | 652 / 227 | 14.05 | +0.03076 | Numeric strings and short coded values dominate. |
| C10 | 77 | 283 / 409 | 12.66 | +0.03276 | Example-related multilingual words and morphological fragments dominate: exempl-, ejemplo, exem-, Example, quando and wir, with multilingual/example fragments in the extremes. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 522 | 2,418 / 2,508 | 14.07 | -0.03135 | Characterisation, configuration, regulation and recommendation language dominates: Characteristics, circumstantial, downregulation, unconstitutional, Configuration, recommendations, discriminatory, encouragement, regulations, prohibiting and Comprehensive. |
| C1 | 408 | 1,663 / 1,901 | 12.81 | -0.03174 | Common grammatical/function words and multilingual lexical fragments dominate. |
| C2 | 314 | 1,258 / 1,617 | 13.16 | -0.03154 | Personal names dominate with lexical residue: Claire, Caroline, Betty, Connie, Sarah and Claude coexist with catastrophe/name fragments and multilingual forms. |
| C3 | 253 | 1,113 / 1,265 | 13.80 | -0.03132 | Cardiovascular disease, immunology, epidemiology and pathology are coherent: cardiovascular, atherosclerotic, macrophage, erythrocytes, epidemiological, sclerosis/staphylococcus fragments, monocyte, morphology, lymphocytes and fractures. |
| C4 | 215 | 834 / 1,325 | 13.92 | -0.03219 | Evaluative intensity, catastrophe and degree/frequency language dominates: disproportionate, unbelievable, disastrous, incredible, catastrophic, Excellent, Sometimes, occasionally, enthusiastic, fortunately and brutal. |
| C5 | 201 | 727 / 1,232 | 13.36 | -0.03306 | Vehicles, roads, built environment and material/household objects form a broad physical-world domain: trucks, chassis, gravel, automobiles, roadway, vegetables, Rails, cylinder, driveway and terrace. |
| C6 | 160 | 522 / 1,106 | 13.44 | -0.03169 | Distribution, uniformity, probability and mathematical/statistical relations dominate: representation, distribution, uniforms, uniformity, perpendicular, distributions, contradictory, probability, improper and inconsistent. |
| C7 | 159 | 636 / 989 | 14.22 | -0.03214 | Geography, civic institutions and national/political identity are coherent: Constitution, Alabama, Philadelphia, Louisiana, Florida, Americans, Chicago, Iowa, Edinburgh and nationalist. |
| C8 | 130 | 561 / 787 | 14.68 | -0.03216 | Monarchy, religion, family and mythic/fantastical roles coexist: emperor, queen, cathedral, palace, Sultan, church, Empire, grandmother, dragon, prince, goddess and mother. |
| C9 | 120 | 383 / 751 | 12.64 | -0.03290 | Technical/computing abbreviations and code-like fragments dominate. |
| C10 | 104 | 589 / 316 | 14.37 | -0.03060 | Numeric strings, especially historical years, dominate. |
| C11 | 57 | 197 / 249 | 11.28 | -0.03068 | Mathematical/code punctuation and symbol formatting dominate; 45 of 57 tokens are punctuation/symbols. |

## Population accounting

### Positive head

Total nodes: **2,550**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,077 | 42.2% |
| Formal/name substrate | 1,186 | 46.5% |
| Irreducible semantic | 177 | 6.9% |
| Mixed unresolved | 110 | 4.3% |
| Unclear | 0 | 0.0% |
| **Total** | **2,550** | **100.0%** |

Semantic-eligible denominator: **1,364 nodes**.

### Negative tail

Total nodes: **2,643**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,186 | 44.9% |
| Formal/name substrate | 1,003 | 37.9% |
| Irreducible semantic | 454 | 17.2% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,643** | **100.0%** |

Semantic-eligible denominator: **1,640 nodes**.

## Positive-side reconstruction

### P+0 — Transformational process, sequencing and evaluation

- **Primary children:** C1, C7
- **Primary nodes:** 540
- **Side-relative coverage:** 21.2%
- **Semantic-eligible coverage:** 39.6%
- **Confidence:** High / Moderate

**Evidence.** C1 contains transformation, interaction, exploration,
development, measurement, resolution and characterisation processes. C7
contains temporal/discourse sequencing, evaluation and action language. Their
direct relation contains **193 token edges**, mean cosine **0.09654**. The
common generator is process-state evolution: events or systems are developed,
transformed, observed and evaluated within a temporal/action sequence.

**Secondary links:** C6 and C8. C1–C6 has **207 edges**, while C1–C8 has
**184** and C7–C8 **36**. Technical management/interface systems and
renewal/action language are adjacent but not clean parent children.

**Exclusion boundary.** C7 is modifier/sequence-heavy while C1 is substantive
process and interaction language. C6 retains a technical management/interface
identity. C8 mixes renewal with bodily/sound actions.

**Alternative.** Keep C7 irreducible and treat C1 as a single semantic island.
This is plausible because C7 is small and discourse-like; confidence is
therefore High/Moderate rather than unqualified High.

### P+1 — Health, psychosocial and biomedical organisation

- **Primary children:** C2, C4
- **Primary nodes:** 537
- **Side-relative coverage:** 21.1%
- **Semantic-eligible coverage:** 39.4%
- **Confidence:** Moderate / High

**Evidence.** C2 contains food/health, breastfeeding, discomfort, compassion,
mindfulness, conversations and interventions; C4 contains biomedical,
respiratory, imaging, analgesic and psychiatric terminology. Their direct
relation contains **248 token edges**, mean cosine **0.09091**. The common
generator is health and embodied/psychosocial intervention spanning lived
experience and clinical/biomedical description.

**Secondary link:** C1. C1–C2 has **557 edges** and C1–C4 **255**, showing that
health/psychosocial material is deeply embedded in developmental and
transformational processes without becoming the same parent.

**Exclusion boundary.** C2 contains food and social-experience material beyond
medicine; C4 is explicitly clinical/biomedical. The parent is therefore not
reduced to “medicine”.

**Alternative.** Leave C2 mixed-unresolved and retain C4 as an irreducible
biomedical domain. This remains a serious alternative because C2 is
heterogeneous.

### Positive irreducible and unresolved structures

- **C6 — irreducible-semantic:** management/platform/software and technical
  publishing/interface systems; secondary relation to P+0.
- **C8 — mixed-unresolved:** renewal/reappearance/transformation and
  bodily/sound actions coexist; secondary relation to P+0.

### Positive formal/name substrate

- C0 — personal names/geographic entities with lexical residue
- C3 — grammar/function words/fragments
- C5 — mathematical/code punctuation
- C9 — numeric strings/coded values
- C10 — example-related multilingual morphology

## Negative-side reconstruction

### P-0 — Characterisation, evaluative intensity and quantitative consistency

- **Primary children:** C0, C4, C6
- **Primary nodes:** 897
- **Side-relative coverage:** 33.9%
- **Semantic-eligible coverage:** 54.7%
- **Confidence:** High / Moderate

**Evidence.** C0 contains characterisation, configuration, regulation and
recommendation language. C4 contains evaluative intensity, catastrophe and
degree/frequency language. C6 contains distribution, uniformity, probability
and mathematical/statistical consistency. C0 is the hub: C0–C4 has **415
edges**, mean cosine **0.10065**; C0–C6 **421** at **0.09497**; C4–C6 **121**
at **0.09967**. The common generator is assessment of system states: systems
are characterised, evaluated for severity or quality, and judged against
distributional/consistency structure.

**Secondary link:** C3. C0–C3 has **265 edges** and C4–C3 **105**, placing
clinical/pathological states adjacent to assessment without absorbing medicine
into the parent.

**Exclusion boundary.** C0 includes neutral administrative/regulatory
description; C4 is evaluative/intensity-heavy; C6 is formal quantitative
structure. The parent is therefore not reduced to “negative evaluation”,
“statistics” or “regulation”.

**Alternative.** Split C6 away and retain a narrower C0+C4
characterisation/evaluation parent. This is a serious alternative because C6
is a mathematical/statistical object system rather than merely a judgement
operation.

### P-1 — Civic/territorial authority and social order

- **Primary children:** C7, C8
- **Primary nodes:** 289
- **Side-relative coverage:** 10.9%
- **Semantic-eligible coverage:** 17.6%
- **Confidence:** Moderate / High

**Evidence.** C7 contains geography, civic institutions and national/political
identity. C8 contains monarchy, religion, family and mythic/fantastical roles.
Their direct relation contains **113 token edges**, mean cosine **0.09844**.
The common generator is social and political order situated within territorial,
institutional and authority structures.

**Secondary link:** C5. C5–C7 has **123 edges** and C5–C8 **127**, showing that
physical/material environments provide settings for civic and authority
structures without becoming authority themselves.

**Exclusion boundary.** C8 includes family and mythic roles as well as formal
authority; C7 is territorial/civic rather than role-based. C5 is material
setting, not social order.

**Alternative.** Include C5 as a third child under a broader
`public order and material environment` parent. Rejected because this loses
the discriminative distinction between authority/territory and physical
setting.

### Negative irreducible structures

- **C3 — irreducible-semantic:** cardiovascular disease, immunology,
  epidemiology and pathology; secondary relation to P-0.
- **C5 — irreducible-semantic:** vehicles, roads, built environment and
  material/household objects; secondary relation to P-1.

### Negative formal/name substrate

- C1 — grammar/function words and multilingual lexical fragments
- C2 — personal names plus lexical fragments
- C9 — technical/computing abbreviations and code-like fragments
- C10 — numeric strings/years
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 544 | Names/geography + lexical residue | formal-substrate | — | Name/form organisation dominates. |
| + | C1 | 419 | Transformations/interactions/exploration/development | parent:P+0 | P+1 | Core process-state organisation. |
| + | C2 | 294 | Food/health + affective-social/intervention | parent:P+1 | P+0 | Health/psychosocial core retained with heterogeneity explicit. |
| + | C3 | 264 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C4 | 243 | Biomedical/respiratory/imaging/analgesic | parent:P+1 | — | Clinical/biomedical child. |
| + | C5 | 192 | Maths/code punctuation | formal-substrate | — | Formatting/symbolic form. |
| + | C6 | 177 | Management/platform/software/publishing interface | irreducible-semantic | P+0 | Distinct technical-system domain. |
| + | C7 | 121 | Temporal/discourse sequencing/evaluation/action | parent:P+0 | — | Sequencing/evaluation child. |
| + | C8 | 110 | Renewal/reappearance + bodily/sound actions | mixed-unresolved | P+0 | Two semantic organisations coexist. |
| + | C9 | 109 | Numeric strings/coded values | formal-substrate | — | Numeric form. |
| + | C10 | 77 | Example-related multilingual morphology | formal-substrate | — | Lexical/morphological organisation. |
| − | C0 | 522 | Characterisation/configuration/regulation | parent:P-0 | — | Assessment/characterisation hub. |
| − | C1 | 408 | Grammar/function/multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C2 | 314 | Personal names + lexical fragments | formal-substrate | — | Name/form organisation. |
| − | C3 | 253 | Cardiovascular/immunology/pathology | irreducible-semantic | P-0 | Clinical-state relation. |
| − | C4 | 215 | Evaluative intensity/catastrophe/degree | parent:P-0 | — | Evaluation/intensity child. |
| − | C5 | 201 | Vehicles/roads/built/material objects | irreducible-semantic | P-1 | Material-setting relation. |
| − | C6 | 160 | Distribution/uniformity/probability/math | parent:P-0 | — | Quantitative consistency child. |
| − | C7 | 159 | Geography/civic/national identity | parent:P-1 | — | Civic/territorial child. |
| − | C8 | 130 | Monarchy/religion/family/mythic roles | parent:P-1 | — | Authority/social-role child. |
| − | C9 | 120 | Technical/computing abbreviations | formal-substrate | — | Abbreviation/code form dominates. |
| − | C10 | 104 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C11 | 57 | Maths/code punctuation | formal-substrate | — | Formatting form. |

Every State 16 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Transformational process, sequencing and evaluation | C1, C7 | 540 | 21.2% | 39.6% | High / Moderate |
| P+1 | Health, psychosocial and biomedical organisation | C2, C4 | 537 | 21.1% | 39.4% | Moderate / High |
| P-0 | Characterisation, evaluative intensity and quantitative consistency | C0, C4, C6 | 897 | 33.9% | 54.7% | High / Moderate |
| P-1 | Civic/territorial authority and social order | C7, C8 | 289 | 10.9% | 17.6% | Moderate / High |

Positive retained parents account for **1,077 nodes**, **42.2% of the positive
population** and **79.0% of semantic-eligible positive nodes**.

Negative retained parents account for **1,186 nodes**, **44.9% of the negative
population** and **72.3% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — process and health/psychosocial relation — Very High.**
   C1–C2 has **557 edges**, C1–C4 **255**, C7–C2 **80** and C7–C4 **29**.
   Developmental/transformational processes are strongly embedded in
   psychosocial and biomedical contexts without becoming the same parent.

2. **P+0 ↔ C6 — process and technical-system relation — High.**
   C1–C6 has **207 edges**; technical platforms and management systems support
   organised process activity but retain a separate system identity.

3. **P+0 ↔ C8 — transformation/renewal relation — Moderate.**
   C1–C8 has **184 edges** and C7–C8 **36**. Renewal semantics align with
   process evolution, but bodily/sound actions prevent primary absorption.

4. **Formal/name populations remain graph-connected without semantic promotion.**
   C0–C1 has **215 edges**, C0–C8 **232**, and C3–C7 **168**. Connectivity
   alone does not override formal or entity-centred organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — assessment within civic/social order — High.**
   C0–C7 has **214 edges**, C0–C8 **171**, C4–C7 **58** and C4–C8 **84**.
   System characterisation/evaluation is strongly contextualised by civic and
   authority structures.

2. **P-0 ↔ C3 — analytical/evaluative and clinical pathology — High.**
   C0–C3 has **265 edges**, C4–C3 **105** and C6–C3 **91**. Medical pathology
   is strongly adjacent to assessment but remains a distinct domain.

3. **P-1 ↔ C5 — civic order and material setting — High.**
   C5–C7 has **123 edges** and C5–C8 **127**, placing physical environments
   around civic and authority organisation without collapsing them.

4. **P-0 is hub-like rather than fully homogeneous.**
   C0 links strongly to both C4 and C6, while C4–C6 is weaker. The parent is
   therefore a higher-order assessment architecture centred on C0 rather than
   a flat single topic.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-0 through characterisation/evaluation;
- positive P+1 and negative C3 through biomedical/clinical structure;
- positive C6 and negative technical/formal populations through platform and
  computing systems;
- positive C0 and negative P-1 through geographic/entity organisation.

No parent-level bridge is promoted without direct cross-side community
evidence sufficient to distinguish semantic structure from lexical proximity.

## Formal/representational substrate

### Positive — 1,186 nodes / 46.5%

- personal names/geographic entities with lexical residue;
- grammar/function words/fragments;
- mathematical/code punctuation;
- numeric strings/coded values;
- example-related multilingual morphology.

### Negative — 1,003 nodes / 37.9%

- grammar/function words and multilingual lexical fragments;
- personal names plus lexical fragments;
- technical/computing abbreviations and code-like forms;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 16 — BLOCK 15 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 TRANSFORMATIONAL PROCESS / SEQUENCING / EVALUATION
|   +-- C1 transformations/interactions/exploration/development
|   `-- C7 temporal/discourse sequencing/evaluation/action
|       |
|       +-- C6 management/platform/software systems   [secondary]
|       `-- C8 renewal + bodily/sound actions         [secondary; mixed]
|
+-- P+1 HEALTH / PSYCHOSOCIAL / BIOMEDICAL ORGANISATION
|   +-- C2 food/health + affective-social/intervention
|   `-- C4 biomedical/respiratory/imaging/analgesic
|
+-- C6 management/platform/software/publishing        [irreducible]
+-- C8 renewal/reappearance + bodily/sound actions    [mixed unresolved]
`-- C0,C3,C5,C9,C10                                  [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 CHARACTERISATION / EVALUATIVE INTENSITY / QUANTITATIVE CONSISTENCY
|   +-- C0 characterisation/configuration/regulation
|   +-- C4 evaluative intensity/catastrophe/degree
|   `-- C6 distribution/uniformity/probability/math
|       \
|        -- C3 cardiovascular/immunology/pathology   [secondary]
|
+-- P-1 CIVIC/TERRITORIAL AUTHORITY & SOCIAL ORDER
|   +-- C7 geography/civic/national identity
|   `-- C8 monarchy/religion/family/mythic roles
|       \
|        -- C5 vehicles/roads/material setting       [secondary]
|
+-- C3 cardiovascular/immunology/pathology            [irreducible]
+-- C5 vehicles/roads/built/material objects           [irreducible]
`-- C1,C2,C9,C10,C11                                 [formal/name substrate]
```

The preferred State 16 reconstruction contains two positive and two negative
multi-community parents. The positive side separates process-state
transformation/sequencing from health/psychosocial organisation. The negative
side contains a hub-like assessment architecture joining characterisation,
evaluative intensity and quantitative consistency, plus a separate
civic/territorial authority structure.

This statement is local to State 16 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. leave positive C7 irreducible and retain only C1 as a process island;
2. leave positive C2 mixed-unresolved and C4 irreducible rather than retaining
   P+1;
3. split negative P-0 into C0+C4 characterisation/evaluation and a separate
   quantitative C6 domain;
4. include negative C5 under P-1 as a material-setting child.

The third alternative is the most serious because C6 is genuinely a
mathematical/statistical object system. The preferred reconstruction retains
P-0 because C0 provides a clear higher-order assessment hub linking both
evaluation and quantitative consistency.

## Uncertainty record

- **Positive P+0:** C7 is small and discourse-like, so the parent remains
  High/Moderate rather than unqualified High.
- **Positive P+1:** C2 is internally broad across health, food, affect and
  intervention; confidence remains Moderate/High.
- **Positive C6:** management/platform/software semantics are coherent enough
  for irreducible-semantic treatment despite technical implementation noise.
- **Positive C8:** renewal and bodily/sound-action structures coexist.
- **Negative P-0:** C6 is the main boundary ambiguity because mathematical
  structure is distinct from evaluative judgement.
- **Negative P-1:** authority/role and territorial communities support a common
  civic-order abstraction but remain semantically distinct children.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,550 / 2,550**
- Negative node accounting: **2,643 / 2,643**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 16 community inspected at underlying R008 community-record level: **yes**
- All State 16 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 16 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 16 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
