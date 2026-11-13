# R010 State 27 — Block 26 output latent structure

## State identity

- R010 state index: `27`
- R008/R009 state: `block_26_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **10 positive-head + 12 negative-tail = 22**
- R008 population: **2,894 positive-head + 3,120 negative-tail = 6,014 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 27 only. Retrieval and graph inspection were
restricted to `state_index=27 / block_26_output`. No later-state evidence was
used.

## Evidence inventory

For every State 27 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_27_block_26_output.md`;
2. all 22 State 27 rows in R008 `community_nodes.csv`;
3. the complete State 27 within-side relation set in R008
   `community_edges.csv`;
4. the State 27 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 515 | 2,241 / 2,625 | 13.80 | +0.03182 | Characterisation, measurement, quantification, testing and developmental processes. |
| C1 | 432 | 1,856 / 1,842 | 12.86 | +0.03152 | Personal names and geographic/name-like entities. |
| C2 | 330 | 1,282 / 1,700 | 12.92 | +0.03205 | Film/media, photography, reading and digital-interface/publishing systems. |
| C3 | 321 | 1,473 / 1,868 | 15.00 | +0.03127 | Common grammatical/function words and lexical fragments. |
| C4 | 303 | 1,151 / 1,790 | 13.50 | +0.03188 | Biomedical/pharmacological and infant-health material mixed with food, sleep and regenerative/freshness terms. |
| C5 | 230 | 822 / 1,476 | 13.57 | +0.03090 | Entrepreneurship/business and institutional/social activity mixed with healthcare, retail and travel. |
| C6 | 223 | 700 / 1,552 | 13.24 | +0.03120 | Communication/interview activity mixed with misunderstanding, uncertainty and reappearance/avoidance stems. |
| C7 | 208 | 1,171 / 479 | 13.56 | +0.03216 | Mathematical/code punctuation and symbolic formatting. |
| C8 | 200 | 773 / 1,165 | 13.56 | +0.03167 | Example-related morphology mixed with temporal, evaluative and freshness descriptors. |
| C9 | 132 | 751 / 299 | 13.64 | +0.02994 | Numeric strings and short coded values. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 423 | 1,790 / 2,051 | 13.31 | -0.03042 | Personal names and name-like fragments with technical residue. |
| C1 | 417 | 1,656 / 2,196 | 13.21 | -0.02985 | Encouragement, prohibition, creation/removal and activation/change actions. |
| C2 | 364 | 1,524 / 2,125 | 14.21 | -0.03030 | Administrative characterisation, downregulation, recommendations and regulatory concepts. |
| C3 | 350 | 1,370 / 1,858 | 13.14 | -0.03072 | Vehicles, agriculture, built environment and material/household objects. |
| C4 | 325 | 1,306 / 1,484 | 12.60 | -0.03028 | Common grammatical/function words and multilingual lexical fragments. |
| C5 | 270 | 1,088 / 1,456 | 13.45 | -0.02949 | Cardiovascular disease, malignancy, cytokine biology and pathology. |
| C6 | 233 | 969 / 1,367 | 14.18 | -0.03071 | Monarchy, religion, political identity and mythic/fantastical roles. |
| C7 | 230 | 912 / 1,349 | 13.80 | -0.03038 | Negative/intense evaluation, frequency and detriment/harm language. |
| C8 | 191 | 688 / 1,049 | 12.70 | -0.02983 | Uppercase lexical stems and technical/code-like abbreviations. |
| C9 | 116 | 538 / 637 | 14.77 | -0.02996 | Geographic entities and regions. |
| C10 | 102 | 597 / 250 | 14.16 | -0.02914 | Numeric strings and quantity words. |
| C11 | 99 | 465 / 316 | 12.59 | -0.02984 | Mathematical/code punctuation and symbol formatting. |

## Population accounting

### Positive head

Total nodes: **2,894**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,298 | 44.9% |
| Formal/name substrate | 1,093 | 37.8% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 503 | 17.4% |
| Unclear | 0 | 0.0% |
| **Total** | **2,894** | **100.0%** |

Semantic-eligible denominator: **1,801 nodes**.

### Negative tail

Total nodes: **3,120**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,360 | 43.6% |
| Formal/name substrate | 1,140 | 36.5% |
| Irreducible semantic | 620 | 19.9% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,120** | **100.0%** |

Semantic-eligible denominator: **1,980 nodes**.

## Positive-side reconstruction

### P+0 — Analytical, communicative and professional information activity

- **Primary children:** C0, C2, C5, C6
- **Primary nodes:** 1,298
- **Side-relative coverage:** 44.9%
- **Semantic-eligible coverage:** 72.1%
- **Confidence:** High / Moderate

**Evidence.** C0 contains characterisation, measurement, testing, acquisition,
development and motivation. C2 contains film/media production, reading,
publishing and digital interfaces. C5 contains entrepreneurship, business,
institutional/social activity and healthcare/service contexts. C6 contains
conversation, negotiation, interviews, discussion and misunderstanding/
uncertainty. C0 acts as a semantic hub: C0–C2 has **453 token edges**, mean
cosine **0.09715**; C0–C5 **363** at **0.09565**; C0–C6 **346** at
**0.09445**. The satellite communities are also mutually connected:
C2–C5 **230**, C2–C6 **150**, C5–C6 **188**.

The minimum common generator is organised information-producing activity:
situations are measured and characterised, communicated through interviews and
discussion, and operationalised through media, publishing, enterprise and
institutional activity.

**Secondary links:** C4 and C8. C0–C4 has **444 edges**, C5–C4 **232** and
C6–C4 **213**, placing biomedical/health material close to the parent. C0–C8
has **280** and C6–C8 **141**, linking temporal/evaluative/example structure to
the same field.

**Exclusion boundary.** C4 remains too internally mixed across biomedical,
food, sleep and regenerative/freshness material. C8 combines example
morphology with temporal/evaluative descriptors. Neither is necessary to
explain the information-production parent.

**Alternative.** Split this parent into C0+C6
`inquiry/communication` and C2+C5 `media/enterprise activity`. This is the
strongest alternative. The preferred single parent is retained because C0 is
strongly connected to all three satellites and the satellites are not isolated
from one another.

### Positive unresolved structures

- **C4 — mixed-unresolved:** biomedical/pharmacological, infant-health, food,
  sleep and regeneration/freshness content.
- **C8 — mixed-unresolved:** example morphology with temporal/evaluative and
  freshness descriptors.

### Positive formal/name substrate

- C1 — personal names/geographic entities
- C3 — grammar/function words and fragments
- C7 — mathematical/code punctuation
- C9 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Administrative/regulatory characterisation, controlled change and adverse judgement

- **Primary children:** C1, C2, C7
- **Primary nodes:** 1,011
- **Side-relative coverage:** 32.4%
- **Semantic-eligible coverage:** 51.1%
- **Confidence:** High

**Evidence.** C1 contains encouragement, prohibition, creation/removal,
activation and change actions. C2 contains administrative characterisation,
downregulation, recommendations and regulation. C7 contains negative/intense
evaluation, frequency and detriment/harm. The triad is strongly connected:
C1–C2 has **538 token edges**, mean cosine **0.09945**; C1–C7 **375** at
**0.09817**; C2–C7 **241** at **0.10244**. The common generator is organised
state control: conditions are administratively characterised, acted upon
through encouragement/prohibition/removal/activation, and evaluated for harm,
detriment or unacceptable intensity.

**Secondary link:** C5. C2–C5 has **334 edges**, C1–C5 **193** and C7–C5
**146**, placing pathology close to state characterisation and intervention
without collapsing medicine into the parent.

**Exclusion boundary.** C2 is descriptive/administrative, C1 is action/change
oriented and C7 is judgement/harm oriented. C5 remains a distinct medical
ontology.

### P-1 — Territorial identity and institutional/mythic authority

- **Primary children:** C6, C9
- **Primary nodes:** 349
- **Side-relative coverage:** 11.2%
- **Semantic-eligible coverage:** 17.6%
- **Confidence:** Moderate

**Evidence.** C6 contains monarchy, religion, political identity and
mythic/fantastical roles. C9 contains geographic entities and regions. Their
direct relation contains **119 token edges**, mean cosine **0.09841**. The
minimum common generator is social and political authority situated within
territorial identity.

**Secondary link:** C3. C3–C6 has **233 edges** and C3–C9 **82**, showing that
material and built environments provide settings for institutional/territorial
order.

**Exclusion boundary.** C6 is authority/role centred and C9 is territorial.
C3 is a physical/material environment rather than authority itself.

**Alternative.** Include C3 as a third child under a broader
`territorial-social and material environment` parent. Rejected because this
loses the discriminative distinction between authority/territory and physical
setting.

### Negative irreducible structures

- **C3 — irreducible-semantic:** vehicles, agriculture, built environment and
  material/household objects; secondary relation to P-1.
- **C5 — irreducible-semantic:** cardiovascular/malignancy/cytokine pathology;
  secondary relation to P-0.

### Negative formal/name substrate

- C0 — names/name-like forms with technical fragments
- C4 — grammar/function words and multilingual fragments
- C8 — uppercase lexical/code abbreviations
- C10 — numeric strings/quantity words
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 515 | parent:P+0 | — |
| + | C1 | 432 | formal-substrate | — |
| + | C2 | 330 | parent:P+0 | — |
| + | C3 | 321 | formal-substrate | — |
| + | C4 | 303 | mixed-unresolved | P+0 |
| + | C5 | 230 | parent:P+0 | — |
| + | C6 | 223 | parent:P+0 | — |
| + | C7 | 208 | formal-substrate | — |
| + | C8 | 200 | mixed-unresolved | P+0 |
| + | C9 | 132 | formal-substrate | — |
| − | C0 | 423 | formal-substrate | — |
| − | C1 | 417 | parent:P-0 | — |
| − | C2 | 364 | parent:P-0 | — |
| − | C3 | 350 | irreducible-semantic | P-1 |
| − | C4 | 325 | formal-substrate | — |
| − | C5 | 270 | irreducible-semantic | P-0 |
| − | C6 | 233 | parent:P-1 | — |
| − | C7 | 230 | parent:P-0 | — |
| − | C8 | 191 | formal-substrate | — |
| − | C9 | 116 | parent:P-1 | — |
| − | C10 | 102 | formal-substrate | — |
| − | C11 | 99 | formal-substrate | — |

Every State 27 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Analytical, communicative and professional information activity | C0, C2, C5, C6 | 1,298 | 44.9% | 72.1% | High / Moderate |
| P-0 | Administrative/regulatory characterisation, controlled change and adverse judgement | C1, C2, C7 | 1,011 | 32.4% | 51.1% | High |
| P-1 | Territorial identity and institutional/mythic authority | C6, C9 | 349 | 11.2% | 17.6% | Moderate |

Positive retained parents account for **1,298 nodes**, **44.9% of the positive
population** and **72.1% of semantic-eligible positive nodes**.

Negative retained parents account for **1,360 nodes**, **43.6% of the negative
population** and **68.7% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 is hub-like rather than flat.** C0 supplies the strongest relations to
   C2 (**453 edges**), C5 (**363**) and C6 (**346**), while the satellite
   communities remain mutually connected.

2. **P+0 ↔ C4 — information activity and biomedical/health context — Very High but unresolved.**
   C0–C4 has **444 edges**, C2–C4 **154**, C5–C4 **232**, C6–C4 **213**.
   The relation is strong, but C4's internal mixture blocks primary absorption.

3. **P+0 ↔ C8 — information activity and evaluative/example context — Moderate to High.**
   C0–C8 has **280 edges**, C2–C8 **87**, C5–C8 **92**, C6–C8 **141**.

### Negative-side relations

1. **P-0 ↔ P-1 — control architecture in territorial/authority context — Moderate to High.**
   C1–C6 has **156 edges**, C2–C6 **250**, C7–C6 **142**; C1–C9 **45**,
   C2–C9 **66**, C7–C9 **27**.

2. **P-0 ↔ C5 — control/characterisation and clinical pathology — High.**
   C1–C5 has **193 edges**, C2–C5 **334**, C7–C5 **146**.

3. **P-1 ↔ C3 — authority/territory and material environment — High.**
   C3–C6 has **233 edges** and C3–C9 **82**.

4. **Negative C0 remains formal/entity substrate despite connectivity.**
   C0–C4 has **421 edges**, C0–C3 **281**, C0–C8 **277**; the underlying
   organisation remains dominated by names and fragments.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 27 cross-side evidence is dominated by near-form relations:
`transmit`↔`transmitting`, `height`↔`Height`,
`raised`↔`raising`, `Notification`↔`notification`, and
`stairs`↔`stair`. These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C4 and negative C5 through biomedical/pathological structure;
- positive C1 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,093 nodes / 37.8%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation;
- numeric strings.

### Negative — 1,140 nodes / 36.5%

- names/name-like forms with technical fragments;
- grammar/function words and multilingual fragments;
- uppercase lexical/code abbreviations;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 27 — BLOCK 26 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ANALYTICAL / COMMUNICATIVE / PROFESSIONAL INFORMATION ACTIVITY
|   +-- C0 characterisation/measurement/testing/development
|   +-- C2 media/publishing/digital-interface systems
|   +-- C5 enterprise/business/institutional-social activity
|   `-- C6 communication/interviews/uncertainty
|       |
|       +-- C4 biomedical/health                      [secondary; mixed]
|       `-- C8 example/evaluative/temporal structure [secondary; mixed]
|
+-- C4 biomedical/infant-health + food/sleep/regeneration [mixed unresolved]
+-- C8 example morphology + temporal/evaluative/freshness [mixed unresolved]
`-- C1,C3,C7,C9                                        [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE/REGULATORY CHARACTERISATION / CONTROLLED CHANGE / ADVERSE JUDGEMENT
|   +-- C1 encouragement/prohibition/removal/activation
|   +-- C2 administrative/downregulation/regulatory characterisation
|   `-- C7 adverse/intense evaluation/detriment/harm
|       \
|        -- C5 cardiovascular/malignancy/cytokine pathology [secondary]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/MYTHIC AUTHORITY
|   +-- C6 monarchy/religion/political/mythic roles
|   `-- C9 geographic entities/regions
|       \
|        -- C3 vehicles/agriculture/material setting   [secondary]
|
+-- C3 vehicles/agriculture/built/material objects      [irreducible]
+-- C5 cardiovascular/malignancy/cytokine pathology    [irreducible]
`-- C0,C4,C8,C10,C11                                  [formal/name substrate]
```

The preferred State 27 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by a broad
information-producing professional-activity architecture. The negative side
contains a strong administrative/change/adverse-judgement parent plus a
smaller territorial/authority structure.

This statement is local to State 27 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. split positive P+0 into C0+C6 **inquiry/communication** and C2+C5
   **media/enterprise activity**;
2. absorb positive C4 into P+0 under a broader health/social systems parent;
3. restrict negative P-0 to C1+C2 and leave C7 irreducible;
4. include negative C3 under P-1 as a material-setting child.

The first and fourth alternatives are the most serious. The preferred positive
parent is retained because C0 is strongly connected to all three satellites and
the satellites remain mutually connected. P-1 remains Moderate because its
territorial/authority core is much cleaner than a broader authority-plus-
material-environment parent.

## Uncertainty record

- **Positive P+0:** broad and hub-like; confidence is High/Moderate rather than
  unqualified High.
- **Positive C4:** strongly linked to P+0 but internally mixed across health,
  food, sleep and regeneration.
- **Positive C8:** example morphology and evaluative/temporal descriptors
  coexist.
- **Negative P-0:** C1–C2 is the dominant core; C7 supplies a distinct judgement
  branch.
- **Negative P-1:** graph support is meaningful but smaller than P-0, so
  confidence remains Moderate.
- **Negative C3:** material-setting structure is strongly adjacent to P-1 but
  remains discriminable.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **10 / 10**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **22 / 22**
- Positive node accounting: **2,894 / 2,894**
- Negative node accounting: **3,120 / 3,120**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 27 community inspected at underlying R008 community-record level: **yes**
- All State 27 within-side community relations inspected: **yes**
- State 27 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 27 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 27 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
