# R010 State 26 — Block 25 output latent structure

## State identity

- R010 state index: `26`
- R008/R009 state: `block_25_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 12 negative-tail = 24**
- R008 population: **3,005 positive-head + 3,313 negative-tail = 6,318 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 26 only. Retrieval and graph inspection were
restricted to `state_index=26 / block_25_output`. No later-state evidence was
used.

## Evidence inventory

For every State 26 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_26_block_25_output.md`;
2. all 24 State 26 rows in R008 `community_nodes.csv`;
3. the complete State 26 within-side relation set in R008
   `community_edges.csv`;
4. the State 26 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 388 | 1,591 / 2,243 | 13.98 | +0.03129 | Entrepreneurship, research and social/business activity mixed with media and healthcare. |
| C1 | 353 | 1,321 / 2,008 | 13.17 | +0.03202 | Biomedical/pharmacological and infant-health material mixed with food, affect and freshness. |
| C2 | 337 | 1,545 / 1,926 | 14.88 | +0.03097 | Common grammatical/function words and lexical fragments. |
| C3 | 324 | 1,484 / 1,464 | 13.68 | +0.03185 | Personal names and geographic/name-like entities. |
| C4 | 306 | 1,010 / 1,775 | 12.40 | +0.03127 | Inevitability, discrepancy, regeneration and temporal lexical stem families. |
| C5 | 273 | 957 / 1,538 | 12.64 | +0.03160 | Navigation, software/interface systems and dimensional/spatial concepts. |
| C6 | 254 | 943 / 1,699 | 14.11 | +0.03135 | Measurement/quantification and interaction mixed with example morphology and theoretical-science concepts. |
| C7 | 246 | 1,369 / 599 | 13.57 | +0.03195 | Mathematical/code punctuation and symbolic formatting. |
| C8 | 184 | 593 / 1,325 | 13.65 | +0.03144 | Anticipation, prediction, acquisition and developmental change. |
| C9 | 130 | 760 / 283 | 13.87 | +0.02998 | Numeric strings and short coded values. |
| C10 | 114 | 445 / 657 | 13.57 | +0.03067 | Temporal, evaluative and comparative/descriptive discourse language. |
| C11 | 96 | 321 / 665 | 13.61 | +0.03250 | Film, photography, reading, writing and publishing/media activity. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 639 | 2,839 / 2,486 | 12.78 | -0.03015 | Short name-like, technical and code-like fragments. |
| C1 | 518 | 2,261 / 2,640 | 13.83 | -0.02959 | Administrative characterisation, recommendations, regulation and constitutional concepts. |
| C2 | 337 | 1,337 / 1,780 | 13.22 | -0.02946 | Encouragement, prohibition, removal, activation and suppression/change actions. |
| C3 | 264 | 1,123 / 1,393 | 13.78 | -0.02963 | Common grammatical/function words and multilingual lexical fragments. |
| C4 | 262 | 1,095 / 1,469 | 13.97 | -0.03028 | Monarchy, religion, family and political/mythic roles. |
| C5 | 257 | 1,019 / 1,398 | 13.37 | -0.03058 | Vehicles, transport, built environment and physical/material objects. |
| C6 | 252 | 1,182 / 1,287 | 14.49 | -0.02978 | Personal names mixed with geographic entities and regions. |
| C7 | 215 | 917 / 1,125 | 13.76 | -0.02915 | Cardiovascular disease, vascular biology, cytokines and pathology. |
| C8 | 196 | 682 / 1,182 | 12.99 | -0.03018 | Qualification/frequency language mixed with uppercase lexical and code/status fragments. |
| C9 | 170 | 663 / 1,054 | 14.00 | -0.02926 | Negative/intense evaluation, alarm and threat. |
| C10 | 110 | 641 / 246 | 13.89 | -0.02829 | Numeric strings, especially historical years and quantity words. |
| C11 | 93 | 453 / 256 | 12.49 | -0.02956 | Mathematical/code punctuation and symbol formatting. |

## Population accounting

### Positive head

Total nodes: **3,005**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,195 | 39.8% |
| Formal/name substrate | 1,343 | 44.7% |
| Irreducible semantic | 114 | 3.8% |
| Mixed unresolved | 353 | 11.7% |
| Unclear | 0 | 0.0% |
| **Total** | **3,005** | **100.0%** |

Semantic-eligible denominator: **1,662 nodes**.

### Negative tail

Total nodes: **3,313**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,539 | 46.5% |
| Formal/name substrate | 1,106 | 33.4% |
| Irreducible semantic | 472 | 14.2% |
| Mixed unresolved | 196 | 5.9% |
| Unclear | 0 | 0.0% |
| **Total** | **3,313** | **100.0%** |

Semantic-eligible denominator: **2,207 nodes**.

## Positive-side reconstruction

### P+0 — Applied inquiry, measurement and developmental change

- **Primary children:** C0, C6, C8
- **Primary nodes:** 826
- **Side-relative coverage:** 27.5%
- **Semantic-eligible coverage:** 49.7%
- **Confidence:** High / Moderate

**Evidence.** C0 contains entrepreneurship, research, negotiation,
conversation, business and training, with healthcare/media spillover. C6
contains characterisation, quantification, measurements, computation and
interaction, with theoretical/example spillover. C8 contains anticipation,
prediction, acquisition and developmental change. The triad is strongly
connected: C0–C6 has **352 token edges**, mean cosine **0.09855**; C0–C8
**280** at **0.09785**; C6–C8 **207** at **0.10891**. The minimum common
generator is applied inquiry and development: organised activities are pursued,
measured and characterised while their future or evolving state is anticipated
and changed.

**Secondary links:** C5 and C11. C0–C5 has **236 edges**, C6–C5 **220** and
C8–C5 **100**, placing software/interface systems around the applied inquiry
architecture. C0–C11 has **157**, C6–C11 **90** and C8–C11 **40**, linking
media/publishing activity without requiring primary inclusion.

**Exclusion boundary.** C0 is activity/enterprise oriented, C6 is
measurement/analysis oriented and C8 is prospective/developmental. C5 is
technical infrastructure, while C11 is media/information production. C1 is not
absorbed despite its strong C0 relation because its biomedical, food, affect and
freshness mixture cannot be explained discriminatively by this parent.

**Alternative.** Include C1 under a broader
`applied social, health and developmental systems` parent. Rejected because
the abstraction becomes too broad and explains C1 largely by shared human/
health context rather than a specific generating relation.

### P+1 — Digital interface and mediated information-production systems

- **Primary children:** C5, C11
- **Primary nodes:** 369
- **Side-relative coverage:** 12.3%
- **Semantic-eligible coverage:** 22.2%
- **Confidence:** Moderate

**Evidence.** C5 contains navigation, bitmap/interface concepts, notifications,
addresses, browsers, dimensions, maps and scores. C11 contains film,
photography, reading, writing, publishing, Netflix and other media activity.
Their direct relation contains **106 token edges**, mean cosine **0.08801**.
The common generator is mediated information activity: content is created,
read, published or navigated through digital/media interfaces.

**Secondary link:** P+0. C0–C5 has **236 edges**, C6–C5 **220**; C0–C11
**157** and C6–C11 **90**. Information systems support applied inquiry without
being identical to it.

**Exclusion boundary.** C5 includes spatial/dimensional interface concepts;
C11 is content/media-production oriented. A generic “information” parent would
be too broad. Confidence therefore remains Moderate.

**Alternative.** Leave C5 and C11 separate. This is a serious alternative
because their direct relation is weaker than the P+0 triad.

### Positive irreducible and unresolved structures

- **C1 — mixed-unresolved:** biomedical/pharmacological, infant-health, food,
  affect and freshness content coexist. Its C0 relation is strong
  (**384 edges**) but does not justify a discriminative shared parent.
- **C10 — irreducible-semantic:** temporal, evaluative and comparative
  descriptors; secondary relation to P+0.

### Positive formal/name substrate

- C2 — grammar/function words and fragments
- C3 — personal names/geographic entities
- C4 — lexical stem families
- C7 — mathematical/code punctuation
- C9 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Administrative/regulatory characterisation, controlled change and adverse judgement

- **Primary children:** C1, C2, C9
- **Primary nodes:** 1,025
- **Side-relative coverage:** 30.9%
- **Semantic-eligible coverage:** 46.4%
- **Confidence:** High

**Evidence.** C1 contains administrative characterisation, recommendations,
regulation and constitutional concepts. C2 contains encouragement,
prohibition, removal, activation and suppression/change actions. C9 contains
negative/intense evaluation, alarm and threat. The triad is strongly connected:
C1–C2 has **551 token edges**, mean cosine **0.10523**; C1–C9 **247** at
**0.09785**; C2–C9 **197** at **0.10144**. The common generator is organised
state control: conditions are characterised and regulated, acted upon through
encouragement/prohibition/removal/activation, and evaluated for adverse or
threatening qualities.

**Secondary links:** C7 and C8. C1–C7 has **286 edges**, linking clinical
pathology to state characterisation. C1–C8 has **272** and C2–C8 **234**,
placing frequency/qualification language around the control architecture.

**Exclusion boundary.** C1 is descriptive/administrative, C2 is intervention
or change oriented, and C9 is adverse-evaluative. C8 contains substantial
code/status morphology, while C7 remains a medical ontology.

**Alternative.** Restrict P-0 to C1+C2 and leave C9 irreducible. This is the
strongest alternative, but C9 has substantial direct support to both children
and supplies a discriminative judgement function.

### P-1 — Territorial identity and institutional/political authority

- **Primary children:** C4, C6
- **Primary nodes:** 514
- **Side-relative coverage:** 15.5%
- **Semantic-eligible coverage:** 23.3%
- **Confidence:** Moderate / High

**Evidence.** C4 contains monarchy, religion, family and political/mythic roles.
C6 contains personal names plus geographic entities and regions. Their direct
relation contains **264 token edges**, mean cosine **0.10154**. The common
generator is institutional and social authority situated within territorial
identity.

**Secondary link:** C5. C4–C5 has **210 edges** and C5–C6 **103**, showing that
transport, buildings and material objects provide settings for institutional
and territorial structure.

**Exclusion boundary.** C4 is authority/role centred; C6 is entity/territory
centred. C5 is physical/material rather than institutional authority.

**Alternative.** Include C5 as a third child under a broader
`institutional/territorial and material-public environment` parent. Rejected
because C5 remains a clearly discriminable physical-world domain.

### Negative irreducible and unresolved structures

- **C5 — irreducible-semantic:** vehicles, transport, built environment and
  material objects; secondary relation to P-1.
- **C7 — irreducible-semantic:** cardiovascular/vascular/cytokine pathology;
  secondary relation to P-0.
- **C8 — mixed-unresolved:** qualification/frequency language and uppercase
  code/status fragments coexist; secondary relation to P-0.

### Negative formal/name substrate

- C0 — short name-like, technical and code fragments
- C3 — grammar/function words and multilingual fragments
- C10 — numeric strings/years
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 388 | parent:P+0 | — |
| + | C1 | 353 | mixed-unresolved | P+0 |
| + | C2 | 337 | formal-substrate | — |
| + | C3 | 324 | formal-substrate | — |
| + | C4 | 306 | formal-substrate | — |
| + | C5 | 273 | parent:P+1 | P+0 |
| + | C6 | 254 | parent:P+0 | — |
| + | C7 | 246 | formal-substrate | — |
| + | C8 | 184 | parent:P+0 | — |
| + | C9 | 130 | formal-substrate | — |
| + | C10 | 114 | irreducible-semantic | P+0 |
| + | C11 | 96 | parent:P+1 | P+0 |
| − | C0 | 639 | formal-substrate | — |
| − | C1 | 518 | parent:P-0 | — |
| − | C2 | 337 | parent:P-0 | — |
| − | C3 | 264 | formal-substrate | — |
| − | C4 | 262 | parent:P-1 | — |
| − | C5 | 257 | irreducible-semantic | P-1 |
| − | C6 | 252 | parent:P-1 | — |
| − | C7 | 215 | irreducible-semantic | P-0 |
| − | C8 | 196 | mixed-unresolved | P-0 |
| − | C9 | 170 | parent:P-0 | — |
| − | C10 | 110 | formal-substrate | — |
| − | C11 | 93 | formal-substrate | — |

Every State 26 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Applied inquiry, measurement and developmental change | C0, C6, C8 | 826 | 27.5% | 49.7% | High / Moderate |
| P+1 | Digital interface and mediated information-production systems | C5, C11 | 369 | 12.3% | 22.2% | Moderate |
| P-0 | Administrative/regulatory characterisation, controlled change and adverse judgement | C1, C2, C9 | 1,025 | 30.9% | 46.4% | High |
| P-1 | Territorial identity and institutional/political authority | C4, C6 | 514 | 15.5% | 23.3% | Moderate / High |

Positive retained parents account for **1,195 nodes**, **39.8% of the positive
population** and **71.9% of semantic-eligible positive nodes**.

Negative retained parents account for **1,539 nodes**, **46.5% of the negative
population** and **69.7% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — applied inquiry and mediated information systems — High.**
   C0–C5 has **236 edges**, C6–C5 **220**, C8–C5 **100**, C0–C11 **157**,
   C6–C11 **90** and C8–C11 **40**.

2. **P+0 ↔ C1 — applied inquiry and biomedical/embodied context — Very High but unresolved.**
   C0–C1 has **384 edges**, C6–C1 **247** and C8–C1 **170**. The relation is
   strong, but C1's mixed biomedical/food/affect/freshness organisation blocks
   primary absorption.

3. **P+0 ↔ C10 — developmental process and contextual evaluation — Moderate.**
   C0–C10 has **122 edges**, C6–C10 **54** and C8–C10 **75**.

4. **Formal/name communities remain highly connected without semantic promotion.**
   C3–C4 has **348 edges**, while C2–C8 has **248**. Connectivity alone does
   not override entity or lexical organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — regulatory control in institutional/territorial context — High.**
   C1–C4 has **341 edges**, C1–C6 **143**, C2–C4 **117**, C2–C6 **44** and
   C9–C4 **128**.

2. **P-0 ↔ C7 — control/characterisation and clinical pathology — High.**
   C1–C7 has **286 edges**, C2–C7 **76** and C9–C7 **76**.

3. **P-0 ↔ C8 — control architecture and qualification/status structure — High.**
   C1–C8 has **272 edges**, C2–C8 **234** and C9–C8 **90**. C8 remains mixed
   because qualification language and code/status morphology coexist.

4. **P-1 ↔ C5 — authority/territory and material setting — High.**
   C4–C5 has **210 edges**, C5–C6 **103**.

5. **Negative C0 remains formal despite high connectivity.**
   C0–C6 has **403 edges**, C0–C3 **408** and C0–C7 **305**; its underlying
   organisation remains dominated by short name-like, technical and code
   fragments.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 26 cross-side evidence is dominated by near-form relations:
`aiser`↔` Kaiser`, `transmit`↔`transmitting`,
`height`↔`Height` and `raised`↔`raising`. These do not establish a
parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C1 and negative C7 through biomedical/health structure;
- positive C3 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,343 nodes / 44.7%

- grammar/function words and fragments;
- personal names/geographic entities;
- lexical stem families;
- mathematical/code punctuation;
- numeric strings.

### Negative — 1,106 nodes / 33.4%

- short name-like, technical and code fragments;
- grammar/function words and multilingual fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 26 — BLOCK 25 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 APPLIED INQUIRY / MEASUREMENT / DEVELOPMENTAL CHANGE
|   +-- C0 enterprise/research/social-business activity
|   +-- C6 measurement/quantification/interaction
|   `-- C8 anticipation/prediction/development
|       |
|       +-- C5 software/interface systems              [secondary]
|       +-- C11 media/publishing activity              [secondary]
|       `-- C1 biomedical/food/affect/freshness       [secondary; mixed]
|
+-- P+1 DIGITAL INTERFACE & MEDIATED INFORMATION-PRODUCTION SYSTEMS
|   +-- C5 navigation/software/interface/dimensions
|   `-- C11 film/photography/reading/writing/publishing
|
+-- C1 biomedical/infant-health + food/affect/freshness [mixed unresolved]
+-- C10 temporal/evaluative/comparative descriptors     [irreducible]
`-- C2,C3,C4,C7,C9                                    [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE/REGULATORY CHARACTERISATION / CONTROLLED CHANGE / ADVERSE JUDGEMENT
|   +-- C1 administrative/regulatory/constitutional characterisation
|   +-- C2 encouragement/prohibition/removal/change
|   `-- C9 adverse/intense evaluation/alarm/threat
|       |
|       +-- C7 cardiovascular/vascular pathology       [secondary]
|       `-- C8 qualification/frequency + code/status   [secondary; mixed]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/POLITICAL AUTHORITY
|   +-- C4 monarchy/religion/family/political roles
|   `-- C6 names/geographic entities/regions
|       \
|        -- C5 transport/built/material setting        [secondary]
|
+-- C5 transport/built/material objects                 [irreducible]
+-- C7 cardiovascular/vascular/cytokine pathology       [irreducible]
+-- C8 qualification/frequency + code/status fragments  [mixed unresolved]
`-- C0,C3,C10,C11                                     [formal/name substrate]
```

The preferred State 26 reconstruction contains two positive and two negative
multi-community parents. The positive side is dominated by applied inquiry,
measurement and developmental change, with a smaller digital/media information
system. The negative side is dominated by administrative control, change
operations and adverse judgement, with territorial/institutional authority
retained separately.

This statement is local to State 26 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C1 into P+0 under a broader social/health developmental
   systems parent;
2. leave positive C5 and C11 separate rather than retaining P+1;
3. restrict negative P-0 to C1+C2 and leave C9 irreducible;
4. include negative C5 under P-1 as a material-setting child.

The first and third alternatives are the most serious. The preferred P+0
rejects C1 because the biomedical/food/affect/freshness mixture loses
discrimination at the broader level. P-0 retains C9 because both C1–C9 and
C2–C9 are substantial and C9 supplies a distinct judgement function.

## Uncertainty record

- **Positive P+0:** C0 and C6 are internally mixed; confidence is High/Moderate.
- **Positive P+1:** direct graph support is weaker than P+0, so confidence is
  Moderate.
- **Positive C1:** is the principal positive unresolved community despite very
  strong adjacency to P+0.
- **Negative P-0:** C1–C2 is the dominant core; C9 is the main boundary
  ambiguity.
- **Negative P-1:** C4 is broad across monarchy, religion, family and political
  roles, but its C6 relation is strong and discriminative.
- **Negative C8:** qualification/frequency and code/status structures coexist.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **3,005 / 3,005**
- Negative node accounting: **3,313 / 3,313**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 26 community inspected at underlying R008 community-record level: **yes**
- All State 26 within-side community relations inspected: **yes**
- State 26 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 26 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 26 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
