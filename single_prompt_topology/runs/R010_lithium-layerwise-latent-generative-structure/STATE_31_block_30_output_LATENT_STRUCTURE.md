# R010 State 31 — Block 30 output latent structure

## State identity

- R010 state index: `31`
- R008/R009 state: `block_30_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 13 negative-tail = 24**
- R008 population: **2,536 positive-head + 2,780 negative-tail = 5,316 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 31 only. Retrieval and graph inspection were
restricted to `state_index=31 / block_30_output`. No later-state evidence was
used.

## Evidence inventory

For every State 31 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_31_block_30_output.md`;
2. all 24 State 31 rows in R008 `community_nodes.csv`;
3. the complete State 31 within-side relation set in R008
   `community_edges.csv`;
4. the State 31 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 415 | 1,803 / 2,280 | 14.18 | +0.03224 | Characterisation, measurement, quantification and developmental/social processes. |
| C1 | 379 | 1,625 / 1,596 | 12.79 | +0.03200 | Personal names and geographic/name-like entities. |
| C2 | 292 | 1,491 / 1,597 | 15.68 | +0.03172 | Common grammatical/function words and lexical fragments. |
| C3 | 270 | 974 / 1,488 | 12.73 | +0.03265 | Film/media production and software/interface systems. |
| C4 | 257 | 980 / 1,574 | 13.75 | +0.03207 | Entrepreneurship/business/retail activity mixed with healthcare, reading and family terms. |
| C5 | 206 | 1,116 / 558 | 13.54 | +0.03276 | Mathematical/code punctuation and symbolic formatting with acknowledgement/paratext residue. |
| C6 | 193 | 691 / 1,137 | 13.05 | +0.03196 | Biomedical, psychological and theoretical-system concepts. |
| C7 | 188 | 567 / 1,287 | 12.88 | +0.03186 | Interpretation, uncertainty, discrepancy, dispute and regeneration concepts. |
| C8 | 142 | 834 / 306 | 13.90 | +0.03040 | Numeric strings and short coded values. |
| C9 | 133 | 429 / 854 | 12.87 | +0.03151 | Evaluative, commercial and evidential descriptors. |
| C10 | 61 | 158 / 471 | 12.90 | +0.03243 | Freshness, selection and comparative/action descriptors. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 499 | 2,245 / 2,312 | 13.63 | -0.03086 | Administrative characterisation, regulation and consequence/heterogeneity concepts. |
| C1 | 314 | 1,259 / 1,608 | 13.14 | -0.03208 | Short name-like and technical/code fragments. |
| C2 | 290 | 1,234 / 1,610 | 14.06 | -0.03221 | Monarchy, empire, religion and mythic/political roles. |
| C3 | 255 | 1,031 / 1,275 | 13.09 | -0.03119 | Prohibition, disappearance, creation and attempted/assisted change actions. |
| C4 | 253 | 945 / 1,491 | 13.36 | -0.03114 | Personal names and name-like entities. |
| C5 | 236 | 1,019 / 1,201 | 13.72 | -0.03100 | Cardiovascular disease, vascular biology and pathology. |
| C6 | 228 | 889 / 997 | 12.17 | -0.03153 | Multilingual words and orthographic/token fragments. |
| C7 | 228 | 826 / 1,359 | 13.21 | -0.03145 | Built environment, vehicles, agriculture and material/household objects. |
| C8 | 156 | 612 / 952 | 13.95 | -0.03096 | Negative/intense evaluation and frequency/degree language. |
| C9 | 95 | 298 / 589 | 12.47 | -0.03170 | Uppercase lexical stems and code/status terms. |
| C10 | 91 | 470 / 251 | 13.09 | -0.03045 | Mathematical/code punctuation and symbol formatting. |
| C11 | 70 | 324 / 396 | 14.91 | -0.03175 | Geographic entities and regions. |
| C12 | 65 | 355 / 195 | 13.92 | -0.02954 | Numeric strings and quantity words. |

## Population accounting

### Positive head

Total nodes: **2,536**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,263 | 49.8% |
| Formal/name substrate | 1,019 | 40.2% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 254 | 10.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,536** | **100.0%** |

Semantic-eligible denominator: **1,517 nodes**.

### Negative tail

Total nodes: **2,780**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,270 | 45.7% |
| Formal/name substrate | 1,046 | 37.6% |
| Irreducible semantic | 464 | 16.7% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,780** | **100.0%** |

Semantic-eligible denominator: **1,734 nodes**.

## Positive-side reconstruction

### P+0 — Analytical interpretation and evidential evaluation

- **Primary children:** C0, C7, C9
- **Primary nodes:** 736
- **Side-relative coverage:** 29.0%
- **Semantic-eligible coverage:** 48.5%
- **Confidence:** High / Moderate

**Evidence.** C0 contains characterisation, measurement, quantification,
development, discussion and intervention. C7 contains interpretation,
uncertainty, discrepancy, dispute and challenge. C9 contains evaluative,
commercial and evidential descriptors such as profitable, sustainable,
evident, fraudulent and questionable. The common generator is interpretive
assessment: states or situations are characterised and measured, uncertainty
and disagreement are represented, and resulting claims or conditions are
evaluated evidentially or commercially.

Direct support is substantial: C0–C7 has **318 token edges**, mean cosine
**0.09541**; C0–C9 **208** at **0.09481**; C7–C9 **91** at **0.08930**.

**Secondary links:** C6 and C4. C0–C6 has **256 edges**, C7–C6 **138**,
C9–C6 **75**; C0–C4 has **378**, C7–C4 **164**, C9–C4 **114**. Biomedical/
theoretical and enterprise/healthcare material are strongly adjacent without
being reducible to interpretive evaluation.

**Exclusion boundary.** C0 is process/measurement centred, C7 uncertainty/
interpretation centred and C9 evaluative/evidential. C6 is a biomedical/
theoretical ontology; C4 is a mixed professional/retail/health domain. The
parent therefore stops before those adjacent domains.

**Alternative.** Restrict P+0 to C0+C7 and leave C9 irreducible. This is
plausible, but C9's direct relation to both the measurement and interpretation
branches plus its explicit evidential/evaluative semantics supports inclusion.

### P+1 — Mediated professional, enterprise and information-production activity

- **Primary children:** C3, C4
- **Primary nodes:** 527
- **Side-relative coverage:** 20.8%
- **Semantic-eligible coverage:** 34.7%
- **Confidence:** Moderate / High

**Evidence.** C3 contains filmmaking, photography, notifications, bitmap/
software interfaces, video and output concepts. C4 contains entrepreneurship,
organisations, business, reading, retail, therapists and health/family
material. Their direct relation contains **232 token edges**, mean cosine
**0.09015**. The common generator is mediated professional activity: enterprise,
content production, communication and service activity occur through media,
information and organisational systems.

**Secondary link:** P+0. C0–C3 has **358 edges**, C0–C4 **378**; C7–C3
**102**, C7–C4 **164**. Professional activity is strongly coupled to analytical
and interpretive processes without being the same generator.

**Exclusion boundary.** C3 is media/interface oriented; C4 is enterprise/
retail/service oriented and contains healthcare/family spillover. The parent is
not broadened to generic social activity.

### Positive unresolved structures

- **C6 — mixed-unresolved:** biomedical, psychological and theoretical-system
  concepts coexist; secondary relation to P+0.
- **C10 — mixed-unresolved:** freshness, selection, comparison and action
  descriptors coexist without one sufficiently discriminative generator.

### Positive formal/name substrate

- C1 — personal names/geographic entities
- C2 — grammar/function words and lexical fragments
- C5 — punctuation/formatting with paratext residue
- C8 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Regulatory characterisation, controlled change and adverse judgement

- **Primary children:** C0, C3, C8
- **Primary nodes:** 910
- **Side-relative coverage:** 32.7%
- **Semantic-eligible coverage:** 52.5%
- **Confidence:** High

**Evidence.** C0 contains administrative characterisation, regulation,
consequences, heterogeneity and beneficiaries. C3 contains prohibition,
disappearance, creation, attempts and assisted change. C8 contains negative/
intense evaluation plus degree/frequency language. The triad is strongly
connected: C0–C3 has **463 token edges**, mean cosine **0.09883**; C0–C8
**252** at **0.09911**; C3–C8 **164** at **0.09190**. The common generator is
organised state control: conditions are characterised and regulated, acted upon
through prohibition/creation/removal/change, and judged for adverse or extreme
qualities.

**Secondary links:** C5 and C7. C0–C5 has **292 edges**, C3–C5 **59**,
C8–C5 **80**, linking pathology to administrative judgement. C0–C7 has **321**,
C3–C7 **119**, C8–C7 **76**, placing material environments within the control
field.

**Exclusion boundary.** C0 is administrative/descriptive, C3 is change/action
oriented and C8 is evaluative. C5 remains medical and C7 physical/material.

**Alternative.** Restrict P-0 to C0+C3 and leave C8 irreducible. This is the
strongest alternative, but C8 is directly connected to both branches and adds a
distinct judgement function.

### P-1 — Territorial identity and institutional/mythic authority

- **Primary children:** C2, C11
- **Primary nodes:** 360
- **Side-relative coverage:** 12.9%
- **Semantic-eligible coverage:** 20.8%
- **Confidence:** Moderate

**Evidence.** C2 contains monarchy, empire, religion and mythic/political roles.
C11 contains geographic entities and regions. Their direct relation contains
**111 token edges**, mean cosine **0.09913**. The minimum common generator is
institutional and symbolic authority situated within territorial identity.

**Secondary links:** C4 and C7. C2–C4 has **226 edges**, while C11–C4 has
**82**, indicating personal/social entity context. C2–C7 has **251** and
C11–C7 **44**, showing that built/material environments provide settings for
authority and territory.

**Exclusion boundary.** C2 is authority/role centred and C11 territorial.
C4 is primarily personal-name/entity organisation and C7 is a material
environment, so neither is promoted as a primary child.

**Alternative.** Leave C2 and C11 separate. This remains plausible because the
parent is much smaller than P-0 and C2 is internally broad across political,
religious and mythic roles.

### Negative irreducible structures

- **C5 — irreducible-semantic:** cardiovascular/vascular pathology; secondary
  relation to P-0.
- **C7 — irreducible-semantic:** built environment, vehicles, agriculture and
  material/household objects; secondary relation to P-0 and P-1.

### Negative formal/name substrate

- C1 — short name-like and technical/code fragments
- C4 — personal names/name-like entities
- C6 — multilingual lexical/orthographic fragments
- C9 — uppercase lexical/status/code fragments
- C10 — mathematical/code punctuation
- C12 — numeric strings/quantity words

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 415 | parent:P+0 | — |
| + | C1 | 379 | formal-substrate | — |
| + | C2 | 292 | formal-substrate | — |
| + | C3 | 270 | parent:P+1 | P+0 |
| + | C4 | 257 | parent:P+1 | P+0 |
| + | C5 | 206 | formal-substrate | — |
| + | C6 | 193 | mixed-unresolved | P+0 |
| + | C7 | 188 | parent:P+0 | — |
| + | C8 | 142 | formal-substrate | — |
| + | C9 | 133 | parent:P+0 | — |
| + | C10 | 61 | mixed-unresolved | — |
| − | C0 | 499 | parent:P-0 | — |
| − | C1 | 314 | formal-substrate | — |
| − | C2 | 290 | parent:P-1 | — |
| − | C3 | 255 | parent:P-0 | — |
| − | C4 | 253 | formal-substrate | P-1 |
| − | C5 | 236 | irreducible-semantic | P-0 |
| − | C6 | 228 | formal-substrate | — |
| − | C7 | 228 | irreducible-semantic | P-0, P-1 |
| − | C8 | 156 | parent:P-0 | — |
| − | C9 | 95 | formal-substrate | — |
| − | C10 | 91 | formal-substrate | — |
| − | C11 | 70 | parent:P-1 | — |
| − | C12 | 65 | formal-substrate | — |

Every State 31 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Analytical interpretation and evidential evaluation | C0, C7, C9 | 736 | 29.0% | 48.5% | High / Moderate |
| P+1 | Mediated professional, enterprise and information-production activity | C3, C4 | 527 | 20.8% | 34.7% | Moderate / High |
| P-0 | Regulatory characterisation, controlled change and adverse judgement | C0, C3, C8 | 910 | 32.7% | 52.5% | High |
| P-1 | Territorial identity and institutional/mythic authority | C2, C11 | 360 | 12.9% | 20.8% | Moderate |

Positive retained parents account for **1,263 nodes**, **49.8% of the positive
population** and **83.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,270 nodes**, **45.7% of the negative
population** and **73.2% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — analytical interpretation and mediated professional activity — High.**
   C0–C3 has **358 edges**, C0–C4 **378**, C7–C3 **102**, C7–C4 **164**,
   C9–C3 **63** and C9–C4 **114**.

2. **P+0 ↔ C6 — interpretive analysis and biomedical/theoretical structure — High.**
   C0–C6 has **256 edges**, C7–C6 **138**, C9–C6 **75**. C6 remains mixed
   rather than being absorbed into the parent.

3. **P+1 ↔ C6 — professional activity and biomedical/theoretical context — Moderate.**
   C3–C6 has **116 edges**, C4–C6 **191**.

4. **Formal/name populations remain highly connected without semantic promotion.**
   C0–C2 has **435 edges** and C1–C7 **261**; connectivity alone does not
   override form/entity organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — regulation/change in authority/territorial context — High.**
   C0–C2 has **363 edges**, C3–C2 **132**, C8–C2 **114**, while C0–C11 has
   **51**, C3–C11 **15** and C8–C11 **12**.

2. **P-0 ↔ C5 — regulation/judgement and clinical pathology — High.**
   C0–C5 has **292 edges**, C3–C5 **59**, C8–C5 **80**.

3. **P-0 ↔ C7 — regulation/change and material setting — High.**
   C0–C7 has **321 edges**, C3–C7 **119**, C8–C7 **76**.

4. **P-1 ↔ C7 — authority/territory and material environment — High.**
   C2–C7 has **251 edges**, C11–C7 **44**.

5. **Negative C4 remains name/entity substrate despite substantial relations.**
   C1–C4 has **358 edges**, C2–C4 **226**, C7–C4 **173**; its primary
   organisation remains personal-name/entity based.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 31 cross-side evidence is dominated by near-form relations
such as `transmit`↔`transmitting` and
`Notification`↔`notification`. These do not establish a parent-level
semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/evaluation/change;
- positive C6 and negative C5 through biomedical/pathological structure;
- positive C1 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,019 nodes / 40.2%

- personal names/geographic entities;
- grammar/function words and lexical fragments;
- mathematical/code punctuation and paratext residue;
- numeric strings.

### Negative — 1,046 nodes / 37.6%

- short name-like and technical/code fragments;
- personal names/name-like entities;
- multilingual lexical/orthographic fragments;
- uppercase lexical/status/code fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 31 — BLOCK 30 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ANALYTICAL INTERPRETATION & EVIDENTIAL EVALUATION
|   +-- C0 characterisation/measurement/development/social process
|   +-- C7 interpretation/uncertainty/dispute/regeneration
|   `-- C9 evaluative/commercial/evidential descriptors
|       \
|        -- C6 biomedical/psychological/theoretical   [secondary; mixed]
|
+-- P+1 MEDIATED PROFESSIONAL / ENTERPRISE / INFORMATION-PRODUCTION ACTIVITY
|   +-- C3 film/media/software/interface systems
|   `-- C4 enterprise/business/retail + healthcare/reading/family
|
+-- C6 biomedical/psychological/theoretical systems   [mixed unresolved]
+-- C10 freshness/selection/comparative-action        [mixed unresolved]
`-- C1,C2,C5,C8                                      [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY CHARACTERISATION / CONTROLLED CHANGE / ADVERSE JUDGEMENT
|   +-- C0 administration/regulation/consequence
|   +-- C3 prohibition/disappearance/creation/change
|   `-- C8 adverse/intense evaluation/degree
|       |
|       +-- C5 cardiovascular/vascular pathology      [secondary]
|       `-- C7 built/vehicles/agriculture/material    [secondary]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/MYTHIC AUTHORITY
|   +-- C2 monarchy/empire/religion/mythic roles
|   `-- C11 geographic entities/regions
|       \
|        -- C7 built/material environment             [secondary]
|
+-- C5 cardiovascular/vascular pathology              [irreducible]
+-- C7 built/vehicles/agriculture/material objects     [irreducible]
`-- C1,C4,C6,C9,C10,C12                              [formal/name substrate]
```

The preferred State 31 reconstruction contains two positive and two negative
multi-community parents. The positive side separates interpretive/evidential
analysis from mediated professional/enterprise activity. The negative side is
dominated by a strongly triangulated regulation-change-judgement architecture,
with territorial/institutional authority retained separately.

This statement is local to State 31 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. merge positive P+0 and P+1 into one broad analytical/professional
   information-activity parent;
2. restrict positive P+0 to C0+C7 and leave C9 irreducible;
3. restrict negative P-0 to C0+C3 and leave C8 irreducible;
4. leave negative C2 and C11 separate rather than retaining P-1.

The first and third alternatives are the most serious. The preferred positive
split preserves a discriminative distinction between interpretive/evidential
assessment and mediated enterprise activity. The preferred negative triad
retains C8 because it supplies a distinct judgement function and has direct
support to both C0 and C3.

## Uncertainty record

- **Positive P+0:** C9 is smaller and modifier-like relative to C0/C7, so
  confidence is High/Moderate rather than unqualified High.
- **Positive P+1:** C4 is internally mixed across business, retail, healthcare,
  reading and family concepts.
- **Positive C6:** biomedical, psychological and theoretical-system concepts
  coexist.
- **Positive C10:** freshness, selection and comparative/action descriptors
  remain unresolved.
- **Negative P-0:** C0–C3 is the dominant core; C8 is the main boundary
  ambiguity.
- **Negative P-1:** smaller and less strongly connected than P-0, so confidence
  remains Moderate.
- **Negative C7:** material-setting structure is strongly adjacent to both
  retained negative parents but remains discriminable.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **2,536 / 2,536**
- Negative node accounting: **2,780 / 2,780**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 31 community inspected at underlying R008 community-record level: **yes**
- All State 31 within-side community relations inspected: **yes**
- State 31 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 31 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 31 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
