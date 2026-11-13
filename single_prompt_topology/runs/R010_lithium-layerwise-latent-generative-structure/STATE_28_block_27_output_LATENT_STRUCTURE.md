# R010 State 28 — Block 27 output latent structure

## State identity

- R010 state index: `28`
- R008/R009 state: `block_27_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 10 negative-tail = 21**
- R008 population: **2,792 positive-head + 2,730 negative-tail = 5,522 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 28 only. Retrieval and graph inspection were
restricted to `state_index=28 / block_27_output`. No later-state evidence was
used.

## Evidence inventory

For every State 28 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_28_block_27_output.md`;
2. all 21 State 28 rows in R008 `community_nodes.csv`;
3. the complete State 28 within-side relation set in R008
   `community_edges.csv`;
4. the State 28 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 471 | 2,113 / 2,392 | 14.05 | +0.03187 | Characterisation, quantification, testing and developmental/analytical processes. |
| C1 | 464 | 2,092 / 1,806 | 12.91 | +0.03174 | Personal names and geographic/name-like entities. |
| C2 | 325 | 1,647 / 1,685 | 15.32 | +0.03121 | Common grammatical/function words and lexical fragments. |
| C3 | 292 | 1,124 / 1,763 | 13.74 | +0.03239 | Entrepreneurship/business and social activity mixed with media and healthcare. |
| C4 | 288 | 1,101 / 1,662 | 13.42 | +0.03216 | Biomedical/pharmacological and infant-health material mixed with freshness/regenerative terms. |
| C5 | 263 | 906 / 1,481 | 12.52 | +0.03210 | Navigation, search, software/interface and dimensional/imaging concepts. |
| C6 | 226 | 1,207 / 593 | 13.31 | +0.03220 | Mathematical/code punctuation and symbolic formatting. |
| C7 | 136 | 435 / 946 | 13.35 | +0.03167 | Food, sleep, affect and recreational/leisure activity. |
| C8 | 119 | 696 / 263 | 13.91 | +0.02983 | Numeric strings and short coded values. |
| C9 | 118 | 402 / 720 | 12.92 | +0.03172 | Temporal, evaluative and comparative/descriptive discourse language. |
| C10 | 90 | 262 / 717 | 13.79 | +0.03221 | Example morphology mixed with inevitability, reappearance and interpretive stems. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 475 | 2,164 / 2,229 | 13.80 | -0.03093 | Administrative characterisation, regulation and up/down-regulation concepts. |
| C1 | 429 | 1,975 / 1,838 | 13.49 | -0.03057 | Negative/intense evaluation, prohibition and adverse-change language. |
| C2 | 417 | 1,673 / 1,881 | 12.53 | -0.03138 | Common grammatical/function words and multilingual/uppercase lexical fragments. |
| C3 | 344 | 1,344 / 1,770 | 12.96 | -0.03146 | Short name-like and technical/code fragments. |
| C4 | 259 | 999 / 1,434 | 13.25 | -0.03174 | Vehicles, agriculture, built environment and material/household objects. |
| C5 | 216 | 883 / 1,147 | 13.49 | -0.03092 | Cardiovascular disease, malignancy, cytokine biology and pathology. |
| C6 | 206 | 858 / 1,211 | 14.21 | -0.03191 | Monarchy, religion, bureaucracy and mythic/political roles. |
| C7 | 180 | 864 / 915 | 14.68 | -0.03110 | Personal names mixed with geographic entities and regions. |
| C8 | 123 | 565 / 391 | 12.37 | -0.03077 | Mathematical/code punctuation and symbol formatting. |
| C9 | 81 | 461 / 190 | 13.73 | -0.02958 | Numeric strings and quantity words. |

## Population accounting

### Positive head

Total nodes: **2,792**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,450 | 51.9% |
| Formal/name substrate | 1,134 | 40.6% |
| Irreducible semantic | 118 | 4.2% |
| Mixed unresolved | 90 | 3.2% |
| Unclear | 0 | 0.0% |
| **Total** | **2,792** | **100.0%** |

Semantic-eligible denominator: **1,658 nodes**.

### Negative tail

Total nodes: **2,730**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,290 | 47.3% |
| Formal/name substrate | 965 | 35.3% |
| Irreducible semantic | 475 | 17.4% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,730** | **100.0%** |

Semantic-eligible denominator: **1,765 nodes**.

## Positive-side reconstruction

### P+0 — Analytical inquiry, enterprise and technical information systems

- **Primary children:** C0, C3, C5
- **Primary nodes:** 1,026
- **Side-relative coverage:** 36.7%
- **Semantic-eligible coverage:** 61.9%
- **Confidence:** High

**Evidence.** C0 contains characterisation, quantification, testing, measurement,
development and acquisition. C3 contains entrepreneurship, conversation,
intervention, negotiation, business and media/professional activity. C5
contains navigation, search, browsers, notifications, imaging, dimensions and
software/interface systems. The structure is strongly triangulated:
C0–C3 has **468 token edges**, mean cosine **0.09998**; C0–C5 **335** at
**0.09312**; C3–C5 **252** at **0.09145**. The minimum common generator is
organised analytical activity supported by enterprise and technical information
systems: situations are measured and characterised, operationalised through
professional activity, and navigated or represented through software/search
interfaces.

**Secondary links:** C4 and C9. C0–C4 has **355 edges**, C3–C4 **187** and
C5–C4 **171**, placing health/biomedical material close to the parent. C0–C9
has **150**, C3–C9 **83**, C5–C9 **48**, placing temporal/evaluative language
around the architecture.

**Exclusion boundary.** C4 remains internally mixed across biomedical,
infant-health and regeneration/freshness material. C7 is lived wellbeing and
recreation rather than analytical/professional infrastructure. C10 is
morphologically mixed and modifier-like.

### P+1 — Embodied health and lived wellbeing

- **Primary children:** C4, C7
- **Primary nodes:** 424
- **Side-relative coverage:** 15.2%
- **Semantic-eligible coverage:** 25.6%
- **Confidence:** Moderate

**Evidence.** C4 contains breastfeeding, neonatal/infant health,
pharmacological and medical material, with regeneration/freshness spillover. C7
contains food, sleep, discomfort, consciousness, compassion, leisure and
recreational activity. Their direct relation contains **163 token edges**, mean
cosine **0.09297**. The minimum common generator is embodied health and
wellbeing spanning clinical/biological conditions and lived affective or
everyday activity.

**Secondary link:** P+0. C0–C4 has **355 edges**, C3–C4 **187**, C5–C4
**171**; C0–C7 has **209**, C3–C7 **161**, C5–C7 **78**. Health and wellbeing
are strongly embedded in broader analytical/professional activity without
becoming identical to it.

**Exclusion boundary.** C4 is explicitly biomedical/infant-health, while C7 is
lived/affective/recreational. The parent is not broadened to generic consumer or
social activity.

**Alternative.** Leave C4 and C7 separate. This remains plausible because C4
contains regeneration/freshness spillover and the pair is weaker than P+0.

### Positive irreducible and unresolved structures

- **C9 — irreducible-semantic:** temporal, evaluative and comparative
  descriptors; secondary relation to P+0.
- **C10 — mixed-unresolved:** example morphology plus inevitability,
  reappearance and interpretive stems.

### Positive formal/name substrate

- C1 — personal names/geographic entities
- C2 — grammar/function words and fragments
- C6 — mathematical/code punctuation
- C8 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Regulatory characterisation and adverse/prohibitive intervention

- **Primary children:** C0, C1
- **Primary nodes:** 904
- **Side-relative coverage:** 33.1%
- **Semantic-eligible coverage:** 51.2%
- **Confidence:** High

**Evidence.** C0 contains administrative characterisation, recommendations,
regulation, up/down-regulation, administrators and consequences. C1 contains
negative/intense evaluation, prohibition, adverse change and detriment. Their
direct relation contains **674 token edges**, mean cosine **0.09902**, by far
the strongest semantic relation in State 28. The minimum common generator is
institutional state control: conditions are characterised and regulated while
being prohibited, judged adversely or subjected to change.

**Secondary links:** C4, C5 and P-1. C0–C4 has **380 edges** and C1–C4 **201**,
placing material environments in the regulatory field. C0–C5 has **279** and
C1–C5 **147**, linking pathology to regulation/judgement. C0–C6 has **256**
and C1–C6 **195**, connecting institutional authority to the same field.

**Exclusion boundary.** C0 is primarily administrative/descriptive; C1 is
evaluative/prohibitive. C5 remains a medical ontology, while C6/C7 represent
authority and territory rather than the control operation itself.

### P-1 — Territorial identity and institutional/mythic authority

- **Primary children:** C6, C7
- **Primary nodes:** 386
- **Side-relative coverage:** 14.1%
- **Semantic-eligible coverage:** 21.9%
- **Confidence:** Moderate / High

**Evidence.** C6 contains monarchy, religion, bureaucracy and mythic/political
roles. C7 contains personal names plus geographic entities and regions. Their
direct relation contains **207 token edges**, mean cosine **0.09883**. The
minimum common generator is institutional/social authority situated within
territorial identity.

**Secondary link:** C4. C4–C6 has **205 edges** and C4–C7 **114**, showing
that roads, buildings and material environments provide settings for authority
and territory.

**Exclusion boundary.** C6 is role/authority centred and C7 is
entity/territory-centred. C4 is physical/material rather than institutional
authority.

### Negative irreducible structures

- **C4 — irreducible-semantic:** vehicles, agriculture, built environment and
  material/household objects; secondary relation to P-0 and P-1.
- **C5 — irreducible-semantic:** cardiovascular/malignancy/cytokine pathology;
  secondary relation to P-0.

### Negative formal/name substrate

- C2 — grammar/function and multilingual/uppercase fragments
- C3 — short name-like and technical/code fragments
- C8 — mathematical/code punctuation
- C9 — numeric strings/quantity words

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 471 | parent:P+0 | — |
| + | C1 | 464 | formal-substrate | — |
| + | C2 | 325 | formal-substrate | — |
| + | C3 | 292 | parent:P+0 | — |
| + | C4 | 288 | parent:P+1 | P+0 |
| + | C5 | 263 | parent:P+0 | — |
| + | C6 | 226 | formal-substrate | — |
| + | C7 | 136 | parent:P+1 | P+0 |
| + | C8 | 119 | formal-substrate | — |
| + | C9 | 118 | irreducible-semantic | P+0 |
| + | C10 | 90 | mixed-unresolved | — |
| − | C0 | 475 | parent:P-0 | — |
| − | C1 | 429 | parent:P-0 | — |
| − | C2 | 417 | formal-substrate | — |
| − | C3 | 344 | formal-substrate | — |
| − | C4 | 259 | irreducible-semantic | P-0, P-1 |
| − | C5 | 216 | irreducible-semantic | P-0 |
| − | C6 | 206 | parent:P-1 | P-0 |
| − | C7 | 180 | parent:P-1 | — |
| − | C8 | 123 | formal-substrate | — |
| − | C9 | 81 | formal-substrate | — |

Every State 28 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Analytical inquiry, enterprise and technical information systems | C0, C3, C5 | 1,026 | 36.7% | 61.9% | High |
| P+1 | Embodied health and lived wellbeing | C4, C7 | 424 | 15.2% | 25.6% | Moderate |
| P-0 | Regulatory characterisation and adverse/prohibitive intervention | C0, C1 | 904 | 33.1% | 51.2% | High |
| P-1 | Territorial identity and institutional/mythic authority | C6, C7 | 386 | 14.1% | 21.9% | Moderate / High |

Positive retained parents account for **1,450 nodes**, **51.9% of the positive
population** and **87.5% of semantic-eligible positive nodes**.

Negative retained parents account for **1,290 nodes**, **47.3% of the negative
population** and **73.1% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 is strongly triangulated rather than merely hub-like.**
   C0–C3 has **468 edges**, C0–C5 **335**, C3–C5 **252**.

2. **P+0 ↔ P+1 — analytical/professional activity and health/wellbeing — High.**
   C0–C4 has **355 edges**, C3–C4 **187**, C5–C4 **171**; C0–C7 **209**,
   C3–C7 **161**, C5–C7 **78**.

3. **P+0 ↔ C9 — analytical activity and contextual evaluation — Moderate.**
   C0–C9 has **150 edges**, C3–C9 **83**, C5–C9 **48**.

4. **C10 remains unresolved despite adjacency.**
   C0–C10 has **165 edges** and C3–C10 **89**, but morphology and interpretive
   stems coexist without one sufficient parent identity.

### Negative-side relations

1. **P-0 ↔ P-1 — regulation/judgement in institutional context — High.**
   C0–C6 has **256 edges**, C1–C6 **195**, C0–C7 **81**, C1–C7 **52**.

2. **P-0 ↔ C4 — regulation and material environment — High.**
   C0–C4 has **380 edges**, C1–C4 **201**.

3. **P-0 ↔ C5 — regulation/judgement and clinical pathology — High.**
   C0–C5 has **279 edges**, C1–C5 **147**.

4. **P-1 ↔ C4 — authority/territory and material setting — High.**
   C4–C6 has **205 edges**, C4–C7 **114**.

5. **Negative formal communities remain highly connected without semantic promotion.**
   C2–C3 has **539 edges**, but both underlying communities are fragmentary/
   lexical rather than coherent higher-order semantic domains.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 28 cross-side evidence is dominated by near-form relations:
`transmit`↔`transmitting`, `height`↔`Height`,
`raised`↔`raising`, `Notification`↔`notification`, and
`stairs`↔`stair`. These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/control;
- positive P+1 and negative C5 through health/pathology;
- positive C1 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,134 nodes / 40.6%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation;
- numeric strings.

### Negative — 965 nodes / 35.3%

- grammar/function and multilingual/uppercase fragments;
- short name-like and technical/code fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 28 — BLOCK 27 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ANALYTICAL INQUIRY / ENTERPRISE / TECHNICAL INFORMATION SYSTEMS
|   +-- C0 characterisation/quantification/testing/development
|   +-- C3 enterprise/business/social-media activity
|   `-- C5 navigation/search/software/interface systems
|       |
|       +-- P+1 health/wellbeing                      [related]
|       `-- C9 temporal/evaluative descriptors       [secondary]
|
+-- P+1 EMBODIED HEALTH & LIVED WELLBEING
|   +-- C4 biomedical/pharmacological/infant-health
|   `-- C7 food/sleep/affect/recreation
|
+-- C9 temporal/evaluative/comparative language       [irreducible]
+-- C10 example morphology + interpretive stems       [mixed unresolved]
`-- C1,C2,C6,C8                                      [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY CHARACTERISATION & ADVERSE/PROHIBITIVE INTERVENTION
|   +-- C0 administrative regulation/up-down-regulation
|   `-- C1 adverse evaluation/prohibition/change
|       |
|       +-- C4 material environment                   [secondary]
|       +-- C5 cardiovascular/malignancy pathology    [secondary]
|       `-- P-1 institutional authority              [related]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/MYTHIC AUTHORITY
|   +-- C6 monarchy/religion/bureaucracy/mythic roles
|   `-- C7 names/geographic entities/regions
|       \
|        -- C4 vehicles/agriculture/material setting [secondary]
|
+-- C4 vehicles/agriculture/built/material objects    [irreducible]
+-- C5 cardiovascular/malignancy/cytokine pathology  [irreducible]
`-- C2,C3,C8,C9                                     [formal/name substrate]
```

The preferred State 28 reconstruction contains two positive and two negative
multi-community parents. The positive side separates a strongly triangulated
analytical/professional/technical information architecture from a smaller
health/wellbeing structure. The negative side is dominated by a very strong
regulatory-characterisation/adverse-intervention parent, with
territorial/institutional authority retained separately.

This statement is local to State 28 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C4 into P+0 under a broader applied health/professional
   systems parent;
2. leave positive C4 and C7 separate rather than retaining P+1;
3. expand negative P-0 to include C6 under a broader regulatory-authority
   parent;
4. include negative C4 under P-1 as a material-setting child.

The second and fourth alternatives are the most serious. P+1 remains Moderate
because C4 contains regeneration/freshness spillover, while C4 on the negative
side remains irreducible because material setting is strongly related to both
control and authority without being reducible to either.

## Uncertainty record

- **Positive P+0:** strongly supported by three-way graph evidence; confidence
  is High.
- **Positive P+1:** biomedical and everyday-wellbeing branches are related but
  distinct; confidence remains Moderate.
- **Positive C10:** is genuinely mixed across example morphology and
  interpretive/reappearance stems.
- **Negative P-0:** C0–C1 is exceptionally strong and provides a clean minimum
  parent.
- **Negative P-1:** C6 is internally broad across monarchy, religion,
  bureaucracy and mythic roles, but its territorial relation is strong.
- **Negative C4:** physical/material structure is strongly connected to both
  retained parents and is therefore left irreducible.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **10 / 10**
- Total communities accounted for: **21 / 21**
- Positive node accounting: **2,792 / 2,792**
- Negative node accounting: **2,730 / 2,730**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 28 community inspected at underlying R008 community-record level: **yes**
- All State 28 within-side community relations inspected: **yes**
- State 28 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 28 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 28 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
