# R010 State 25 — Block 24 output latent structure

## State identity

- R010 state index: `25`
- R008/R009 state: `block_24_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 10 negative-tail = 21**
- R008 population: **2,713 positive-head + 2,699 negative-tail = 5,412 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 25 only. Retrieval and graph inspection were
restricted to `state_index=25 / block_24_output`. No later-state evidence was
used.

## Evidence inventory

For every State 25 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_25_block_24_output.md`;
2. all 21 State 25 rows in R008 `community_nodes.csv`;
3. the complete State 25 within-side relation set in R008
   `community_edges.csv`;
4. the State 25 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 324 | 1,425 / 1,860 | 14.54 | +0.03172 | Common grammatical/function words and lexical fragments. |
| C1 | 312 | 1,123 / 1,976 | 13.53 | +0.03238 | Exploration, development, anticipation and evolving/process activity. |
| C2 | 309 | 1,287 / 1,471 | 13.09 | +0.03178 | Personal names and geographic/name-like entities. |
| C3 | 298 | 1,088 / 1,698 | 13.00 | +0.03218 | Media production, publishing, writing and digital-platform/software activity. |
| C4 | 296 | 1,154 / 1,853 | 14.06 | +0.03236 | Entrepreneurship, negotiation and social/business activity mixed with healthcare. |
| C5 | 291 | 980 / 1,697 | 12.57 | +0.03259 | Inevitability, interpretation, regeneration and reappearance stem families; lexical form dominates. |
| C6 | 245 | 959 / 1,515 | 14.01 | +0.03189 | Measurement and quantification mixed with example morphology and theoretical-science terms. |
| C7 | 204 | 756 / 1,242 | 13.50 | +0.03256 | Biomedical/pharmacological and infant-health material mixed with food/agricultural terms. |
| C8 | 191 | 1,077 / 460 | 13.69 | +0.03316 | Mathematical/code punctuation and symbolic formatting. |
| C9 | 136 | 516 / 820 | 13.62 | +0.03209 | Temporal, evaluative and comparative/descriptive discourse language. |
| C10 | 107 | 637 / 230 | 14.06 | +0.03054 | Numeric strings and short coded values. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 488 | 2,081 / 2,129 | 12.89 | -0.03144 | Short name-like, technical and code-like fragments. |
| C1 | 391 | 1,689 / 1,966 | 13.67 | -0.03110 | Administrative characterisation, recommendations, constitutional/legal and regulatory concepts. |
| C2 | 361 | 1,819 / 1,643 | 14.63 | -0.03142 | Personal/geographic entities mixed with monarchy, religion and political/social roles. |
| C3 | 290 | 1,144 / 1,586 | 13.36 | -0.03089 | Negative/intense evaluation, discrimination and distress. |
| C4 | 266 | 1,035 / 1,443 | 13.21 | -0.03182 | Vehicles, roads, terrain and material/household objects. |
| C5 | 258 | 1,092 / 1,348 | 13.69 | -0.03109 | Regulation/change actions mixed with qualification, frequency and lexical stems. |
| C6 | 215 | 913 / 1,107 | 13.64 | -0.03052 | Cardiovascular disease, cytokine biology, immunology and pathology. |
| C7 | 173 | 742 / 872 | 13.62 | -0.03074 | Grammar/function fragments mixed with punctuation and tokenisation residue. |
| C8 | 169 | 596 / 804 | 11.81 | -0.03199 | Multilingual words, suffixes and orthographic fragments. |
| C9 | 88 | 485 / 234 | 13.68 | -0.03000 | Numeric strings, historical years and quantity words. |

## Population accounting

### Positive head

Total nodes: **2,713**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 853 | 31.4% |
| Formal/name substrate | 1,222 | 45.0% |
| Irreducible semantic | 434 | 16.0% |
| Mixed unresolved | 204 | 7.5% |
| Unclear | 0 | 0.0% |
| **Total** | **2,713** | **100.0%** |

Semantic-eligible denominator: **1,491 nodes**.

### Negative tail

Total nodes: **2,699**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,566 | 58.0% |
| Formal/name substrate | 918 | 34.0% |
| Irreducible semantic | 215 | 8.0% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,699** | **100.0%** |

Semantic-eligible denominator: **1,781 nodes**.

## Positive-side reconstruction

### P+0 — Developmental, organisational and quantitative inquiry

- **Primary children:** C1, C4, C6
- **Primary nodes:** 853
- **Side-relative coverage:** 31.4%
- **Semantic-eligible coverage:** 57.2%
- **Confidence:** High / Moderate

**Evidence.** C1 contains exploration, development, anticipation, resolution and
evolving processes. C4 contains entrepreneurship, negotiation, sessions,
interventions, business, conversations and motivation, with healthcare
spillover. C6 contains measurement, characterisation, quantification,
understanding and theoretical-science material, with example morphology
spillover. The three-child structure is strongly connected: C1–C4 has **439
token edges**, mean cosine **0.09811**; C1–C6 **266** at **0.10041**; C4–C6
**242** at **0.09996**. The minimum common generator is goal-directed inquiry
and development: systems, projects or situations are explored and developed,
organised through social/professional activity, and measured or quantified.

**Secondary link:** C3. C3–C4 has **282 edges** and C3–C6 **272**, placing
media/publishing/software systems close to the inquiry architecture without
requiring primary absorption.

**Exclusion boundary.** C4 contains healthcare and social activity beyond
enterprise; C6 contains example morphology and theoretical-science terms beyond
measurement. C3 is media/software infrastructure rather than the underlying
developmental/analytical process.

**Alternative.** Split the architecture into C1+C6
`developmental/quantitative analysis` and C3+C4
`mediated professional/enterprise activity`. This is the strongest competing
reconstruction. The preferred single parent is retained because C1–C4,
C1–C6 and C4–C6 provide genuine three-way support.

### Positive irreducible and unresolved structures

- **C3 — irreducible-semantic:** media production, publishing, writing and
  digital-platform/software activity; secondary relation to P+0.
- **C7 — mixed-unresolved:** biomedical/infant-health and food/agricultural
  material coexist.
- **C9 — irreducible-semantic:** temporal, evaluative and comparative
  descriptors; secondary relation to P+0.

### Positive formal/name substrate

- C0 — grammar/function words and fragments
- C2 — personal names/geographic entities
- C5 — lexical stem families
- C8 — mathematical/code punctuation
- C10 — numeric strings/codes

## Negative-side reconstruction

### P-0 — Administrative/regulatory characterisation, adverse judgement and controlled change

- **Primary children:** C1, C3, C5
- **Primary nodes:** 939
- **Side-relative coverage:** 34.8%
- **Semantic-eligible coverage:** 52.7%
- **Confidence:** High

**Evidence.** C1 contains administrative characterisation, recommendations,
constitutional/legal and regulatory concepts. C3 contains adverse/intense
evaluation, discrimination and distress. C5 contains downregulation,
encouragement, prohibition and other change actions, mixed with qualification
language. The triad is strongly connected: C1–C5 has **436 token edges**, mean
cosine **0.10087**; C3–C5 **346** at **0.10003**; C1–C3 **284** at
**0.09558**. The common generator is institutional state judgement and control:
conditions are characterised administratively, evaluated for adverse or
unacceptable qualities, and regulated, encouraged, prohibited or otherwise
changed.

**Secondary links:** C6 and P-1. C1–C6 has **182 edges** and C3–C6 **159**,
linking pathology to characterisation/judgement. C1–C2 has **318**, linking
institutional/social actors to the same control field.

**Exclusion boundary.** C1 is descriptive/administrative; C3 is
evaluative/distress-oriented; C5 is intervention/change-oriented and contains
qualification spillover. The parent cannot be reduced to any one child
function.

### P-1 — Institutional/territorial order and material-public environment

- **Primary children:** C2, C4
- **Primary nodes:** 627
- **Side-relative coverage:** 23.2%
- **Semantic-eligible coverage:** 35.2%
- **Confidence:** Moderate

**Evidence.** C2 combines personal/geographic entities with monarchy, religion
and political/social roles. C4 contains vehicles, roads, terrain and
material/household objects. Their direct relation contains **266 token edges**,
mean cosine **0.09128**. The common generator is an organised social/public
environment: territorial and authority identities occur within material and
infrastructural settings.

**Secondary link:** P-0. C1–C2 has **318 edges**, C3–C2 **207** and C5–C2
**95**. Institutional/territorial structure strongly contextualises
regulatory/adverse judgement.

**Exclusion boundary.** C2 is already internally mixed across entities,
authority and geography; C4 is physical/material. The parent is therefore
Moderate and is not broadened to generic “human world”.

**Alternative.** Leave C2 and C4 separate. This is a serious alternative
because C2 is heterogeneous and the direct relation is weaker than the P-0
triad.

### Negative irreducible structure

- **C6 — irreducible-semantic:** cardiovascular/cytokine/immunological
  pathology; secondary relation to P-0.

### Negative formal/name substrate

- C0 — short name-like, technical and code fragments
- C7 — grammar/function fragments plus punctuation/tokenisation residue
- C8 — multilingual lexical/morphological fragments
- C9 — numeric strings/years

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 324 | formal-substrate | — |
| + | C1 | 312 | parent:P+0 | — |
| + | C2 | 309 | formal-substrate | — |
| + | C3 | 298 | irreducible-semantic | P+0 |
| + | C4 | 296 | parent:P+0 | — |
| + | C5 | 291 | formal-substrate | — |
| + | C6 | 245 | parent:P+0 | — |
| + | C7 | 204 | mixed-unresolved | — |
| + | C8 | 191 | formal-substrate | — |
| + | C9 | 136 | irreducible-semantic | P+0 |
| + | C10 | 107 | formal-substrate | — |
| − | C0 | 488 | formal-substrate | — |
| − | C1 | 391 | parent:P-0 | — |
| − | C2 | 361 | parent:P-1 | P-0 |
| − | C3 | 290 | parent:P-0 | — |
| − | C4 | 266 | parent:P-1 | — |
| − | C5 | 258 | parent:P-0 | — |
| − | C6 | 215 | irreducible-semantic | P-0 |
| − | C7 | 173 | formal-substrate | — |
| − | C8 | 169 | formal-substrate | — |
| − | C9 | 88 | formal-substrate | — |

Every State 25 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Developmental, organisational and quantitative inquiry | C1, C4, C6 | 853 | 31.4% | 57.2% | High / Moderate |
| P-0 | Administrative/regulatory characterisation, adverse judgement and controlled change | C1, C3, C5 | 939 | 34.8% | 52.7% | High |
| P-1 | Institutional/territorial order and material-public environment | C2, C4 | 627 | 23.2% | 35.2% | Moderate |

Positive retained parents account for **853 nodes**, **31.4% of the positive
population** and **57.2% of semantic-eligible positive nodes**.

Negative retained parents account for **1,566 nodes**, **58.0% of the negative
population** and **87.9% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ C3 — inquiry/development and media/software production — High.**
   C1–C3 has **191 edges**, C4–C3 **282**, C6–C3 **272**.

2. **P+0 ↔ C7 — inquiry/development and biomedical/health material — Moderate.**
   C1–C7 has **164 edges**, C4–C7 **188**, C6–C7 **137**. C7 remains mixed
   across biomedical and food/agricultural terms.

3. **P+0 ↔ C9 — development and temporal/evaluative description — Moderate.**
   C1–C9 has **162 edges**, C4–C9 **107**, C6–C9 **91**.

4. **Formal/name populations remain graph-connected without semantic promotion.**
   C0–C1 has **323 edges** and C2–C7 **241**; connectivity alone does not
   override their underlying form/entity organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — regulatory judgement in institutional/material context — High.**
   C1–C2 has **318 edges**, C1–C4 **277**, C3–C2 **207**, C3–C4 **163**.

2. **P-0 ↔ C6 — control/judgement and clinical pathology — High.**
   C1–C6 has **182 edges**, C3–C6 **159**, C5–C6 **82**.

3. **P-1 is heterogeneous rather than a flat topic.**
   C2–C4 has **266 edges**, but C2 already combines territorial, personal and
   authority content while C4 is material/physical.

4. **Negative C0 is highly connected but remains fragmentary/formal.**
   Its strongest relation is C0–C2 at **393 edges**; the underlying community
   remains dominated by short name-like and technical fragments.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 25 cross-side evidence is dominated by near-form relations:
`height`↔`Height`, matching delimiter forms, `Notification`↔
`notification`, `stairs`↔`stair`, and `printed`↔`printing`.
These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C7 and negative C6 through biomedical/health structure;
- positive C2 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,222 nodes / 45.0%

- grammar/function words and fragments;
- personal names/geographic entities;
- lexical stem families;
- mathematical/code punctuation;
- numeric strings.

### Negative — 918 nodes / 34.0%

- short name-like, technical and code fragments;
- grammar/function fragments and punctuation/tokenisation residue;
- multilingual lexical/morphological fragments;
- numeric strings/years.

## Minimal state-level architecture

```text
STATE 25 — BLOCK 24 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 DEVELOPMENTAL / ORGANISATIONAL / QUANTITATIVE INQUIRY
|   +-- C1 exploration/development/anticipation/process
|   +-- C4 enterprise/negotiation/social-business + healthcare
|   `-- C6 measurement/quantification + theoretical/example material
|       |
|       +-- C3 media/publishing/software                [secondary]
|       `-- C9 temporal/evaluative descriptors         [secondary]
|
+-- C3 media/publishing/software                        [irreducible]
+-- C7 biomedical/infant-health + food/agriculture     [mixed unresolved]
+-- C9 temporal/evaluative/comparative language        [irreducible]
`-- C0,C2,C5,C8,C10                                   [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE/REGULATORY CHARACTERISATION / ADVERSE JUDGEMENT / CONTROLLED CHANGE
|   +-- C1 administrative/constitutional/regulatory characterisation
|   +-- C3 adverse/intense evaluation/discrimination/distress
|   `-- C5 regulation/change + qualification/frequency
|       \
|        -- C6 cardiovascular/cytokine pathology      [secondary]
|
+-- P-1 INSTITUTIONAL/TERRITORIAL ORDER & MATERIAL-PUBLIC ENVIRONMENT
|   +-- C2 personal/geographic + monarchy/religion/political roles
|   `-- C4 vehicles/roads/terrain/material objects
|
+-- C6 cardiovascular/cytokine/immunology/pathology    [irreducible]
`-- C0,C7,C8,C9                                       [formal/name substrate]
```

The preferred State 25 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by an integrated
development–organisation–measurement architecture. The negative side contains a
strong administration–adverse judgement–change-control triad plus a more
uncertain institutional/territorial/material environment.

This statement is local to State 25 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. split positive P+0 into C1+C6
   **developmental/quantitative analysis** and C3+C4
   **mediated professional/enterprise activity**;
2. leave positive C4 outside P+0 because healthcare/social material broadens it;
3. restrict negative P-0 to C1+C5 and leave C3 irreducible;
4. leave negative C2 and C4 separate rather than retaining P-1.

The first and fourth alternatives are the most serious. The preferred positive
parent is retained because C1–C4, C1–C6 and C4–C6 form a dense three-way
structure. P-1 remains Moderate because its children are broad and internally
heterogeneous.

## Uncertainty record

- **Positive P+0:** C4 and C6 are mixed communities, so confidence is
  High/Moderate rather than unqualified High.
- **Positive C3:** media/software activity is strongly linked to P+0 but remains
  a distinct information-production domain.
- **Positive C7:** biomedical and food/agricultural content coexist.
- **Negative P-0:** C5 includes qualification/frequency language as well as
  regulation/change.
- **Negative P-1:** C2 is internally mixed and the parent is consequently only
  Moderate.
- **Negative C6:** pathology is strongly adjacent to P-0 but remains a medical
  ontology.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **10 / 10**
- Total communities accounted for: **21 / 21**
- Positive node accounting: **2,713 / 2,713**
- Negative node accounting: **2,699 / 2,699**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 25 community inspected at underlying R008 community-record level: **yes**
- All State 25 within-side community relations inspected: **yes**
- State 25 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 25 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 25 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
