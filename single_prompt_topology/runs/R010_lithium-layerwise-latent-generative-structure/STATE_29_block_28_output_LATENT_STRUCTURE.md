# R010 State 29 — Block 28 output latent structure

## State identity

- R010 state index: `29`
- R008/R009 state: `block_28_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **9 positive-head + 12 negative-tail = 21**
- R008 population: **3,105 positive-head + 2,918 negative-tail = 6,023 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 29 only. Retrieval and graph inspection were
restricted to `state_index=29 / block_28_output`. No later-state evidence was
used.

## Evidence inventory

For every State 29 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_29_block_28_output.md`;
2. all 21 State 29 rows in R008 `community_nodes.csv`;
3. the complete State 29 within-side relation set in R008
   `community_edges.csv`;
4. the State 29 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 486 | 2,073 / 2,725 | 14.14 | +0.03136 | Quantification, measurement, characterisation and developmental/interpretive processes. |
| C1 | 464 | 2,059 / 1,867 | 12.90 | +0.03049 | Personal names and geographic/name-like entities. |
| C2 | 428 | 1,626 / 2,375 | 13.15 | +0.03104 | Biomedical/pharmacological and theoretical-system concepts mixed with uncertainty/anticipation stems. |
| C3 | 426 | 1,683 / 2,402 | 13.54 | +0.03146 | Entrepreneurship/business activity mixed with media, healthcare and organisational terms. |
| C4 | 392 | 1,993 / 2,066 | 15.44 | +0.03046 | Common grammatical/function words and lexical fragments. |
| C5 | 258 | 983 / 1,505 | 13.45 | +0.03126 | Infant/age and freshness concepts mixed with evaluative, comparative and emergence language. |
| C6 | 257 | 1,336 / 744 | 13.29 | +0.03195 | Mathematical/code punctuation and symbolic formatting. |
| C7 | 246 | 848 / 1,376 | 12.49 | +0.03165 | Software/interface, browser and dimensional/layout concepts. |
| C8 | 148 | 888 / 288 | 13.95 | +0.02968 | Numeric strings and short coded values. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 545 | 2,389 / 2,343 | 13.07 | -0.03094 | Personal names and name-like fragments. |
| C1 | 535 | 2,383 / 2,465 | 13.52 | -0.03059 | Administrative characterisation, regulation, up/down-regulation and consequence concepts. |
| C2 | 484 | 2,195 / 2,156 | 13.52 | -0.03003 | Negative/intense evaluation, prohibition and adverse-change language. |
| C3 | 297 | 1,178 / 1,624 | 13.40 | -0.03131 | Vehicles, agriculture, vegetation and built/material objects. |
| C4 | 224 | 918 / 1,211 | 13.60 | -0.03026 | Cardiovascular disease, malignancy, cytokine biology and pathology. |
| C5 | 223 | 946 / 1,290 | 14.27 | -0.03147 | Monarchy, religion, empire and mythic/political roles. |
| C6 | 220 | 833 / 1,012 | 12.17 | -0.03140 | Multilingual words and orthographic fragments mixed with modal/status tokens. |
| C7 | 109 | 571 / 316 | 13.38 | -0.02999 | Mathematical/code punctuation and symbol formatting. |
| C8 | 108 | 347 / 729 | 13.18 | -0.03157 | Uppercase technical and lexical abbreviations. |
| C9 | 86 | 416 / 481 | 15.27 | -0.03111 | Geographic entities and regions. |
| C10 | 74 | 426 / 162 | 13.70 | -0.02937 | Numeric strings and quantity words. |
| C11 | 13 | 33 / 95 | 12.38 | -0.02780 | Unix, Git and command-line/developer tooling. |

## Population accounting

### Positive head

Total nodes: **3,105**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,158 | 37.3% |
| Formal/name substrate | 1,261 | 40.6% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 686 | 22.1% |
| Unclear | 0 | 0.0% |
| **Total** | **3,105** | **100.0%** |

Semantic-eligible denominator: **1,844 nodes**.

### Negative tail

Total nodes: **2,918**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,328 | 45.5% |
| Formal/name substrate | 1,056 | 36.2% |
| Irreducible semantic | 534 | 18.3% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,918** | **100.0%** |

Semantic-eligible denominator: **1,862 nodes**.

## Positive-side reconstruction

### P+0 — Analytical, organisational and technical information systems

- **Primary children:** C0, C3, C7
- **Primary nodes:** 1,158
- **Side-relative coverage:** 37.3%
- **Semantic-eligible coverage:** 62.8%
- **Confidence:** High

**Evidence.** C0 contains quantification, measurement, characterisation,
testing, development and interpretation. C3 contains entrepreneurship,
business, intervention, media production, healthcare and organisational
activity. C7 contains software, browser, interface, management and
dimensional/layout concepts. The three-child structure is strongly
triangulated: C0–C3 has **696 token edges**, mean cosine **0.09821**; C0–C7
**310** at **0.09394**; C3–C7 **292** at **0.09033**. The minimum common
generator is organised analytical activity implemented through institutional
and technical systems: states are measured and interpreted, operationalised
through enterprise/organisational activity, and represented or managed through
software interfaces.

**Secondary link:** C2. C0–C2 has **610 edges**, C2–C3 **426**, and C2–C7
**191**. This is exceptionally strong adjacency, but C2 combines biomedical,
pharmacological, theoretical-system and uncertainty/anticipation structures.
It is therefore not promoted into P+0 without flattening materially distinct
content.

**Secondary link:** C5. C0–C5 has **317 edges**, C3–C5 **271**, and C7–C5
**95**. Infant/age, freshness and evaluative/emergence content is strongly
embedded in the larger field but remains internally mixed.

**Exclusion boundary.** C2 is not merely a scientific-analysis child; its
biomedical and uncertainty components are substantial. C5 is not merely a
developmental-state child; infant, comparative and freshness semantics coexist.
The parent therefore stops at C0+C3+C7.

**Alternative.** Expand P+0 to include C2 under a broader
`analytical, scientific and organisational systems` parent. Rejected because
the gain in graph coverage would come at substantial loss of discrimination.

### Positive unresolved structures

- **C2 — mixed-unresolved:** biomedical/pharmacological and theoretical-system
  concepts coexist with uncertainty and anticipation stems. Strong secondary
  relation to P+0.
- **C5 — mixed-unresolved:** infant/age and freshness concepts coexist with
  evaluative, comparative and emergence language. Strong secondary relation to
  P+0.

### Positive formal/name substrate

- C1 — personal names/geographic entities
- C4 — grammar/function words and fragments
- C6 — mathematical/code punctuation
- C8 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Administrative/regulatory characterisation and adverse/prohibitive control

- **Primary children:** C1, C2
- **Primary nodes:** 1,019
- **Side-relative coverage:** 34.9%
- **Semantic-eligible coverage:** 54.7%
- **Confidence:** High

**Evidence.** C1 contains administrative characterisation, recommendations,
regulation, up/down-regulation and consequence concepts. C2 contains negative
and intense evaluation, prohibition, adverse change and detriment. Their direct
relation contains **803 token edges**, mean cosine **0.09997**, by far the
strongest semantic relation in State 29. The minimum common generator is
institutional state control: conditions are characterised and regulated while
being judged adverse, prohibited, discouraged or otherwise changed.

**Secondary links:**
- **C3:** C1–C3 has **422 edges**, C2–C3 **284**, placing material and built
  environments inside the regulatory/control field.
- **C4:** C1–C4 has **266 edges**, C2–C4 **152**, linking pathology to
  state-characterisation and adverse judgement.
- **C5:** C1–C5 has **300 edges**, C2–C5 **233**, linking authority and
  institutional roles to the control architecture.

**Exclusion boundary.** C1 is primarily administrative/descriptive, while C2
is evaluative/prohibitive. C3 is a material environment, C4 a medical ontology,
and C5 an authority/role domain. Their strong adjacency does not erase those
distinctions.

### P-1 — Territorial identity and institutional/mythic authority

- **Primary children:** C5, C9
- **Primary nodes:** 309
- **Side-relative coverage:** 10.6%
- **Semantic-eligible coverage:** 16.6%
- **Confidence:** Moderate

**Evidence.** C5 contains monarchy, religion, empire and mythic/political roles.
C9 contains geographic entities and regions. Their direct relation contains
**93 token edges**, mean cosine **0.09942**. The minimum common generator is
institutional and symbolic authority situated within territorial identity.

**Secondary link:** C3. C3–C5 has **218 edges**, C3–C9 **63**, showing that
material/built environments provide settings for authority and territorial
structure.

**Exclusion boundary.** C5 is authority/role centred and C9 is territorial.
C3 is physical/material rather than institutional authority.

**Alternative.** Leave C5 and C9 separate. This remains plausible because the
parent is much smaller and less strongly connected than P-0.

### Negative irreducible structures

- **C3 — irreducible-semantic:** vehicles, agriculture, vegetation and
  built/material objects; secondary relation to P-0 and P-1.
- **C4 — irreducible-semantic:** cardiovascular/malignancy/cytokine pathology;
  secondary relation to P-0.
- **C11 — irreducible-semantic:** Unix, Git and command-line/developer tooling.
  Its small size and weak higher-order relations do not justify a parent.

### Negative formal/name substrate

- C0 — personal names/name-like fragments
- C6 — multilingual morphology/status fragments
- C7 — mathematical/code punctuation
- C8 — uppercase technical/lexical abbreviations
- C10 — numeric strings/quantity words

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 486 | parent:P+0 | — |
| + | C1 | 464 | formal-substrate | — |
| + | C2 | 428 | mixed-unresolved | P+0 |
| + | C3 | 426 | parent:P+0 | — |
| + | C4 | 392 | formal-substrate | — |
| + | C5 | 258 | mixed-unresolved | P+0 |
| + | C6 | 257 | formal-substrate | — |
| + | C7 | 246 | parent:P+0 | — |
| + | C8 | 148 | formal-substrate | — |
| − | C0 | 545 | formal-substrate | — |
| − | C1 | 535 | parent:P-0 | — |
| − | C2 | 484 | parent:P-0 | — |
| − | C3 | 297 | irreducible-semantic | P-0, P-1 |
| − | C4 | 224 | irreducible-semantic | P-0 |
| − | C5 | 223 | parent:P-1 | P-0 |
| − | C6 | 220 | formal-substrate | — |
| − | C7 | 109 | formal-substrate | — |
| − | C8 | 108 | formal-substrate | — |
| − | C9 | 86 | parent:P-1 | — |
| − | C10 | 74 | formal-substrate | — |
| − | C11 | 13 | irreducible-semantic | — |

Every State 29 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Analytical, organisational and technical information systems | C0, C3, C7 | 1,158 | 37.3% | 62.8% | High |
| P-0 | Administrative/regulatory characterisation and adverse/prohibitive control | C1, C2 | 1,019 | 34.9% | 54.7% | High |
| P-1 | Territorial identity and institutional/mythic authority | C5, C9 | 309 | 10.6% | 16.6% | Moderate |

Positive retained parents account for **1,158 nodes**, **37.3% of the positive
population** and **62.8% of semantic-eligible positive nodes**.

Negative retained parents account for **1,328 nodes**, **45.5% of the negative
population** and **71.3% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 is strongly triangulated.**
   C0–C3 has **696 edges**, C0–C7 **310**, C3–C7 **292**.

2. **P+0 ↔ C2 — analytical/organisational and biomedical-theoretical structure — Very High but unresolved.**
   C0–C2 has **610 edges**, C3–C2 **426**, C7–C2 **191**. The graph relation is
   stronger than many retained parents, but C2's internal semantic mixture
   prevents a non-vacuous parent assignment.

3. **P+0 ↔ C5 — analytical/organisational and infant/evaluative structure — High.**
   C0–C5 has **317 edges**, C3–C5 **271**, C7–C5 **95**.

4. **Formal/name communities remain strongly connected without semantic promotion.**
   C0–C4 has **530 edges**, C1–C4 **343**, and C1–C2 **462**. Connectivity
   alone does not override lexical or entity organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — regulatory control in authority/territorial context — Moderate to High.**
   C1–C5 has **300 edges**, C2–C5 **233**, C1–C9 **51**, C2–C9 **39**.

2. **P-0 ↔ C3 — regulatory control and material environment — High.**
   C1–C3 has **422 edges**, C2–C3 **284**.

3. **P-0 ↔ C4 — control/judgement and clinical pathology — High.**
   C1–C4 has **266 edges**, C2–C4 **152**.

4. **P-1 ↔ C3 — authority/territory and material setting — Moderate.**
   C3–C5 has **218 edges**, C3–C9 **63**.

5. **Negative C0 remains name/form substrate despite broad connectivity.**
   C0–C6 has **364 edges**, C0–C2 **328**, C0–C1 **307**, C0–C4 **305**.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 29 cross-side evidence is dominated by near-form relations:
`chr`↔` chr`, `height`↔`Height`, `raised`↔`raising`,
matching delimiter forms and `Notification`↔`notification`. These do not
establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/control;
- positive C2/C5 and negative C4 through biomedical/health structure;
- positive C1 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,261 nodes / 40.6%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation;
- numeric strings.

### Negative — 1,056 nodes / 36.2%

- personal names/name-like fragments;
- multilingual morphology/status fragments;
- mathematical/code punctuation;
- uppercase technical/lexical abbreviations;
- numeric strings.

## Minimal state-level architecture

```text
STATE 29 — BLOCK 28 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ANALYTICAL / ORGANISATIONAL / TECHNICAL INFORMATION SYSTEMS
|   +-- C0 quantification/measurement/characterisation/development
|   +-- C3 enterprise/business/media/organisational activity
|   `-- C7 software/browser/interface/layout systems
|       |
|       +-- C2 biomedical/theoretical/uncertainty       [secondary; mixed]
|       `-- C5 infant/freshness/evaluative-emergence    [secondary; mixed]
|
+-- C2 biomedical/theoretical + uncertainty/anticipation [mixed unresolved]
+-- C5 infant/age + freshness/evaluation/emergence       [mixed unresolved]
`-- C1,C4,C6,C8                                        [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE/REGULATORY CHARACTERISATION & ADVERSE/PROHIBITIVE CONTROL
|   +-- C1 administration/regulation/up-down-regulation
|   `-- C2 adverse evaluation/prohibition/change
|       |
|       +-- C3 vehicles/agriculture/material setting    [secondary]
|       +-- C4 cardiovascular/malignancy pathology      [secondary]
|       `-- P-1 institutional/mythic authority          [related]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/MYTHIC AUTHORITY
|   +-- C5 monarchy/religion/empire/mythic roles
|   `-- C9 geographic entities/regions
|       \
|        -- C3 built/material environment               [secondary]
|
+-- C3 vehicles/agriculture/vegetation/material objects  [irreducible]
+-- C4 cardiovascular/malignancy/cytokine pathology     [irreducible]
+-- C11 Unix/Git/command-line tooling                    [irreducible]
`-- C0,C6,C7,C8,C10                                    [formal/name substrate]
```

The preferred State 29 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by an
analytical-organisational-technical information architecture, with two highly
connected but internally mixed semantic communities left unresolved. The
negative side is dominated by an exceptionally strong administrative/adverse
control pair, with a smaller territorial/authority structure retained
separately.

This statement is local to State 29 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. expand positive P+0 to include C2 under a broader
   **analytical/scientific/organisational systems** parent;
2. create a positive health/development parent from C2+C5;
3. expand negative P-0 to include C5 under a broader
   **regulation and institutional authority** parent;
4. leave negative C5 and C9 separate rather than retaining P-1.

The first alternative is the most serious because C2 is extremely strongly
connected to all P+0 children. It is rejected only because its biomedical,
theoretical and uncertainty content remains materially heterogeneous.

## Uncertainty record

- **Positive P+0:** graph support is very strong and triangulated; confidence is
  High.
- **Positive C2:** is the principal State 29 ambiguity because graph evidence
  strongly favours inclusion while semantic discrimination favours leaving it
  unresolved.
- **Positive C5:** infant/age, freshness and evaluation/emergence coexist.
- **Negative P-0:** the C1–C2 relation is exceptionally strong and provides a
  clean minimum parent.
- **Negative P-1:** relatively small and weaker than P-0; confidence remains
  Moderate.
- **Negative C11:** semantically coherent but too small and weakly connected for
  higher-order promotion.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **9 / 9**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **21 / 21**
- Positive node accounting: **3,105 / 3,105**
- Negative node accounting: **2,918 / 2,918**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 29 community inspected at underlying R008 community-record level: **yes**
- All State 29 within-side community relations inspected: **yes**
- State 29 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 29 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 29 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
