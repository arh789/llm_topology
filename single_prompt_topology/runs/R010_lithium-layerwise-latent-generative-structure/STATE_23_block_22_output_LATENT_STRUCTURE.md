# R010 State 23 — Block 22 output latent structure

## State identity

- R010 state index: `23`
- R008/R009 state: `block_22_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 11 negative-tail = 24**
- R008 population: **3,261 positive-head + 3,275 negative-tail = 6,536 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 23 only. Retrieval and graph inspection were
restricted to `state_index=23 / block_22_output`. No later-state evidence was
used.

## Evidence inventory

For every State 23 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_23_block_22_output.md`;
2. all 24 State 23 rows in R008 `community_nodes.csv`;
3. the complete State 23 within-side relation set in R008
   `community_edges.csv`;
4. the State 23 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 523 | 2,276 / 2,103 | 12.72 | +0.03109 | Personal names, cities and geographic entities. |
| C1 | 326 | 1,174 / 2,099 | 13.64 | +0.03123 | Exploration, characterisation, negotiation and developmental/process activity. |
| C2 | 305 | 1,151 / 1,985 | 14.06 | +0.03142 | Measurement, interaction, quantification and computational/organisational analysis. |
| C3 | 295 | 1,595 / 783 | 13.47 | +0.03185 | Mathematical/code punctuation and symbolic formatting. |
| C4 | 283 | 1,261 / 1,771 | 15.17 | +0.03068 | Common grammatical/function words and lexical fragments. |
| C5 | 269 | 891 / 1,672 | 12.84 | +0.03109 | Navigation, software/platform management and size/layout concepts. |
| C6 | 249 | 860 / 1,555 | 13.15 | +0.03152 | Food, leisure, shopping, affect and recreational activity. |
| C7 | 246 | 958 / 1,541 | 14.05 | +0.03153 | Biomedical, pharmacological, infant and healthcare terminology. |
| C8 | 232 | 953 / 1,281 | 13.74 | +0.03119 | Anticipation/emergence with temporal and evaluative descriptors. |
| C9 | 201 | 591 / 1,413 | 12.91 | +0.03086 | Emergence/freshness/avoidance/reappearance lexical stem families. |
| C10 | 182 | 694 / 1,163 | 14.02 | +0.03105 | Entrepreneurship, research, filmmaking, photography and business/media activity. |
| C11 | 139 | 816 / 288 | 13.81 | +0.02981 | Numeric strings and short coded values. |
| C12 | 11 | 25 / 82 | 12.00 | +0.03125 | Acknowledgement, greeting and thanks language. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 551 | 2,520 / 2,272 | 13.27 | -0.02985 | Personal names/name-like entities with short lexical fragments. |
| C1 | 476 | 2,161 / 2,160 | 13.62 | -0.02952 | Encouragement, prohibition, removal, legal constraint and adverse evaluation. |
| C2 | 429 | 1,916 / 1,953 | 13.48 | -0.03007 | Grammar/function words and multilingual lexical fragments. |
| C3 | 315 | 1,376 / 1,486 | 13.45 | -0.02914 | Cardiovascular/cytokine/immunological pathology. |
| C4 | 315 | 1,178 / 1,958 | 13.70 | -0.03049 | Administrative characterisation, configuration and constitutional/regulatory concepts. |
| C5 | 304 | 1,165 / 1,668 | 13.15 | -0.03036 | Vehicles, roads, built environment and material/household objects. |
| C6 | 289 | 1,218 / 1,688 | 14.27 | -0.03002 | Administration/beneficiaries mixed with monarchy, religion and political identity. |
| C7 | 222 | 863 / 1,379 | 13.99 | -0.02943 | Negative/intense evaluation, alarm and detriment. |
| C8 | 161 | 612 / 696 | 11.93 | -0.03022 | Multilingual/encoding fragments plus punctuation/tokenisation residue. |
| C9 | 114 | 677 / 232 | 13.91 | -0.02843 | Numeric strings, especially historical years. |
| C10 | 99 | 503 / 556 | 15.78 | -0.03019 | Geographic entities, regions and place-name fragments. |

## Population accounting

### Positive head

Total nodes: **3,261**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,126 | 34.5% |
| Formal/name substrate | 1,441 | 44.2% |
| Irreducible semantic | 694 | 21.3% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,261** | **100.0%** |

Semantic-eligible denominator: **1,820 nodes**.

### Negative tail

Total nodes: **3,275**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,401 | 42.8% |
| Formal/name substrate | 1,255 | 38.3% |
| Irreducible semantic | 619 | 18.9% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,275** | **100.0%** |

Semantic-eligible denominator: **2,020 nodes**.

## Positive-side reconstruction

### P+0 — Developmental process and quantitative-organisational analysis

- **Primary children:** C1, C2
- **Primary nodes:** 631
- **Side-relative coverage:** 19.3%
- **Semantic-eligible coverage:** 34.7%
- **Confidence:** High

**Evidence.** C1 contains exploration, characterisation, negotiation,
development, conversation and modelling. C2 contains measurement, interaction,
quantification, computation, intervention, comparison and organisational
analysis. Their direct relation contains **388 token edges**, mean cosine
**0.10448**, the strongest clearly semantic positive pair. The minimum common
generator is an organised developmental-analysis process in which systems are
explored, negotiated and developed while being measured, modelled and compared.

**Secondary links:** C5, C8 and C10. C1–C5 has **277 edges**, C2–C5 **271**;
C1–C8 **242**, C2–C8 **126**; C1–C10 **162**, C2–C10 **155**. Software
management, anticipation/evaluation and enterprise/research activity surround
the core without becoming necessary children.

**Exclusion boundary.** C5 is technical interface/management infrastructure.
C8 is modifier-heavy. C10 is an enterprise/media domain. None is required to
explain the C1–C2 analytical-developmental relation.

### P+1 — Embodied wellbeing and biomedical health

- **Primary children:** C6, C7
- **Primary nodes:** 495
- **Side-relative coverage:** 15.2%
- **Semantic-eligible coverage:** 27.2%
- **Confidence:** Moderate / High

**Evidence.** C6 contains food, leisure, shopping, happiness, discomfort,
compassion, play and aspirations. C7 contains biomedical, pharmacological,
infant and healthcare concepts. Their direct relation contains **215 token
edges**, mean cosine **0.10124**. The common generator is embodied health and
wellbeing spanning lived affective/consumption states and clinical/biological
states.

**Secondary links:** P+0 through C1–C6 (**249 edges**), C2–C6 (**185**),
C1–C7 (**139**) and C2–C7 (**229**). Health/wellbeing is strongly embedded in
activity and analysis without collapsing into that parent.

**Exclusion boundary.** C6 is lived/recreational/affective; C7 is explicitly
medical. The parent is not broadened to generic lifestyle or consumer activity.

### Positive irreducible structures

- **C5:** navigation, software/platform management and layout concepts;
  secondary relation to P+0.
- **C8:** anticipation/emergence plus temporal/evaluative descriptors;
  secondary relation to P+0.
- **C10:** entrepreneurship, research, filmmaking, photography and
  business/media activity; secondary relation to P+0.
- **C12:** acknowledgement, greeting and thanks language.

### Positive formal/name substrate

- C0 — names/geographic entities
- C3 — mathematical/code punctuation
- C4 — grammar/function words/fragments
- C9 — lexical stem families
- C11 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Regulatory intervention, administrative characterisation and adverse judgement

- **Primary children:** C1, C4, C7
- **Primary nodes:** 1,013
- **Side-relative coverage:** 30.9%
- **Semantic-eligible coverage:** 50.1%
- **Confidence:** High

**Evidence.** C1 contains encouragement, prohibition, removal, legal constraint
and adverse evaluation. C4 contains administrative characterisation,
configuration, regulations and constitutional concepts. C7 contains negative
evaluation, alarm and detriment. C1–C4 has **512 token edges**, mean cosine
**0.10266**; C1–C7 **407** at **0.10244**; C4–C7 **134** at **0.09258**.
The common generator is institutional state judgement and intervention:
conditions are described administratively, evaluated for adverse or
unacceptable properties, and encouraged, prohibited, removed or otherwise
constrained.

**Secondary links:** C3 and P-1. C1–C3 has **183 edges**, C4–C3 **232** and
C7–C3 **145**, linking pathology to judgement/control. C1–C6 has **276** and
C4–C6 **267**, linking institutional actors and authority to the same field
without requiring primary absorption.

**Exclusion boundary.** C4 is descriptive/administrative; C1 is
intervention/legal-constraint oriented; C7 is evaluative/alarm oriented.
Authority actors and medical pathology remain distinct ontologies.

### P-1 — Institutional/territorial authority and political order

- **Primary children:** C6, C10
- **Primary nodes:** 388
- **Side-relative coverage:** 11.8%
- **Semantic-eligible coverage:** 19.2%
- **Confidence:** Moderate / High

**Evidence.** C6 contains administrators, beneficiaries, palace, king,
warriors, emperor, chapel, liberals, Sultan, USSR, church and Americans. C10
contains geographic entities and regions. Their direct relation contains
**129 token edges**, mean cosine **0.10270**. The common generator is
institutional and political authority situated within territorial identity.

**Secondary link:** C5. C5–C6 has **250 edges** and C5–C10 **66**, showing that
material environments provide settings for political/social order without
becoming authority themselves.

**Exclusion boundary.** C6 contains authority, administration and political
identity; C10 is geographic. C5 remains a material-world domain.

### Negative irreducible structures

- **C3:** cardiovascular/cytokine/immunological pathology; secondary relation to
  P-0.
- **C5:** vehicles, roads, built environment and material objects; secondary
  relation to P-1.

### Negative formal/name substrate

- C0 — personal names/name-like forms
- C2 — grammar/function words and multilingual fragments
- C8 — multilingual/tokeniser/formatting residue
- C9 — numeric strings/years

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 523 | formal-substrate | — |
| + | C1 | 326 | parent:P+0 | — |
| + | C2 | 305 | parent:P+0 | — |
| + | C3 | 295 | formal-substrate | — |
| + | C4 | 283 | formal-substrate | — |
| + | C5 | 269 | irreducible-semantic | P+0 |
| + | C6 | 249 | parent:P+1 | P+0 |
| + | C7 | 246 | parent:P+1 | P+0 |
| + | C8 | 232 | irreducible-semantic | P+0 |
| + | C9 | 201 | formal-substrate | — |
| + | C10 | 182 | irreducible-semantic | P+0 |
| + | C11 | 139 | formal-substrate | — |
| + | C12 | 11 | irreducible-semantic | — |
| − | C0 | 551 | formal-substrate | — |
| − | C1 | 476 | parent:P-0 | — |
| − | C2 | 429 | formal-substrate | — |
| − | C3 | 315 | irreducible-semantic | P-0 |
| − | C4 | 315 | parent:P-0 | — |
| − | C5 | 304 | irreducible-semantic | P-1 |
| − | C6 | 289 | parent:P-1 | P-0 |
| − | C7 | 222 | parent:P-0 | — |
| − | C8 | 161 | formal-substrate | — |
| − | C9 | 114 | formal-substrate | — |
| − | C10 | 99 | parent:P-1 | — |

Every State 23 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Developmental process and quantitative-organisational analysis | C1, C2 | 631 | 19.3% | 34.7% | High |
| P+1 | Embodied wellbeing and biomedical health | C6, C7 | 495 | 15.2% | 27.2% | Moderate / High |
| P-0 | Regulatory intervention, administrative characterisation and adverse judgement | C1, C4, C7 | 1,013 | 30.9% | 50.1% | High |
| P-1 | Institutional/territorial authority and political order | C6, C10 | 388 | 11.8% | 19.2% | Moderate / High |

Positive retained parents account for **1,126 nodes**, **34.5% of the positive
population** and **61.9% of semantic-eligible positive nodes**.

Negative retained parents account for **1,401 nodes**, **42.8% of the negative
population** and **69.4% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — analytical activity and health/wellbeing — High.**
   C1–C6 has **249 edges**, C2–C6 **185**, C1–C7 **139** and C2–C7 **229**.

2. **P+0 ↔ C5 — analytical activity and software/platform management — High.**
   C1–C5 has **277 edges**, C2–C5 **271**.

3. **P+0 ↔ C8 — development and anticipation/evaluation — High.**
   C1–C8 has **242 edges**, C2–C8 **126**.

4. **P+0 ↔ C10 — process analysis and enterprise/media activity — Moderate to High.**
   C1–C10 has **162 edges**, C2–C10 **155**.

### Negative-side relations

1. **P-0 ↔ P-1 — regulatory judgement in institutional/political context — High.**
   C1–C6 has **276 edges**, C4–C6 **267**, C7–C6 **187**, while C1–C10 has
   **32** and C4–C10 **28**.

2. **P-0 ↔ C3 — control/judgement and clinical pathology — High.**
   C1–C3 has **183 edges**, C4–C3 **232**, C7–C3 **145**.

3. **P-1 ↔ C5 — authority and material setting — High.**
   C5–C6 has **250 edges** and C5–C10 **66**.

4. **Negative C0 is graph-connected but remains name/form substrate.**
   Its strong relations, including C0–C2 **543**, do not justify semantic
   promotion because the underlying community is dominated by names and
   fragments.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 23 cross-side evidence is dominated by near-form or lexical
relations such as `aiser`↔` Kaiser`, `Greek`↔` Greek`, adjacent years,
`transmit`↔`transmitting` and `height`↔`Height`. These do not
establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/intervention;
- positive P+1 and negative C3 through biomedical/health structure;
- positive C0 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,441 nodes / 44.2%

- names/geographic entities;
- mathematical/code punctuation;
- grammar/function words and fragments;
- lexical stem families;
- numeric strings.

### Negative — 1,255 nodes / 38.3%

- personal names/name-like forms;
- grammar/function words and multilingual fragments;
- multilingual/tokenisation/formatting residue;
- numeric strings.

## Minimal state-level architecture

```text
STATE 23 — BLOCK 22 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 DEVELOPMENTAL PROCESS & QUANTITATIVE-ORGANISATIONAL ANALYSIS
|   +-- C1 exploration/characterisation/negotiation/development
|   `-- C2 measurement/interaction/quantification/computation
|       |
|       +-- C5 software/platform management            [secondary]
|       +-- C8 anticipation/emergence/evaluation       [secondary]
|       `-- C10 enterprise/research/media             [secondary]
|
+-- P+1 EMBODIED WELLBEING & BIOMEDICAL HEALTH
|   +-- C6 food/leisure/affect/recreation
|   `-- C7 biomedical/pharmacological/infant-health
|
+-- C5 software/platform management                    [irreducible]
+-- C8 anticipation/emergence/evaluative descriptors  [irreducible]
+-- C10 entrepreneurship/research/media                [irreducible]
+-- C12 acknowledgement/greeting/thanks                [irreducible]
`-- C0,C3,C4,C9,C11                                  [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY INTERVENTION / ADMINISTRATIVE CHARACTERISATION / ADVERSE JUDGEMENT
|   +-- C1 encouragement/prohibition/removal/legal constraint
|   +-- C4 administrative characterisation/configuration
|   `-- C7 adverse/intense evaluation/alarm/detriment
|       \
|        -- C3 cardiovascular/cytokine pathology      [secondary]
|
+-- P-1 INSTITUTIONAL/TERRITORIAL AUTHORITY & POLITICAL ORDER
|   +-- C6 administration/monarchy/religion/politics
|   `-- C10 geographic entities/regions
|       \
|        -- C5 vehicles/roads/material setting        [secondary]
|
+-- C3 cardiovascular/cytokine/immunology/pathology    [irreducible]
+-- C5 vehicles/roads/built/material objects            [irreducible]
`-- C0,C2,C8,C9                                       [formal/name substrate]
```

The preferred State 23 reconstruction contains two positive and two negative
multi-community parents. The positive side separates developmental/analytical
process from embodied health/wellbeing. The negative side separates a strong
regulatory-administrative-adverse-judgement architecture from
institutional/territorial political order.

This statement is local to State 23 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. include positive C5 under P+0 as a technical-management child;
2. create a positive enterprise/media parent from C5+C10;
3. restrict negative P-0 to C1+C4 and leave C7 irreducible;
4. include negative C5 under P-1 as a material-setting child.

The third alternative is the most serious. The preferred P-0 retains C7
because C1–C7 is strong and C7 supplies a discriminative adverse-judgement
function rather than merely duplicating C1.

## Uncertainty record

- **Positive P+1:** lived wellbeing and clinical health remain distinct child
  domains; confidence is Moderate/High.
- **Positive C5:** combines navigation/software management with layout/size
  concepts.
- **Positive C8:** combines anticipation/emergence with modifier-like
  evaluative language.
- **Negative P-0:** C4 and C1 are the strongest structural core; C7 is a
  higher-order evaluative branch.
- **Negative P-1:** C6 itself mixes administration, monarchy, religion and
  political identity.
- **Negative C5:** material-setting semantics are coherent and strongly related
  to P-1 but remain discriminable.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **11 / 11**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **3,261 / 3,261**
- Negative node accounting: **3,275 / 3,275**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 23 community inspected at underlying R008 community-record level: **yes**
- All State 23 within-side community relations inspected: **yes**
- State 23 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 23 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 23 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
