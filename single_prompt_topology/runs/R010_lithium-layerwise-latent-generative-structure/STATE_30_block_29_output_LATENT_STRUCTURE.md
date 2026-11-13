# R010 State 30 — Block 29 output latent structure

## State identity

- R010 state index: `30`
- R008/R009 state: `block_29_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 12 negative-tail = 23**
- R008 population: **2,887 positive-head + 2,741 negative-tail = 5,628 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 30 only. Retrieval and graph inspection were
restricted to `state_index=30 / block_29_output`. No later-state evidence was
used.

## Evidence inventory

For every State 30 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_30_block_29_output.md`;
2. all 23 State 30 rows in R008 `community_nodes.csv`;
3. the complete State 30 within-side relation set in R008
   `community_edges.csv`;
4. the State 30 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 475 | 2,140 / 1,812 | 12.83 | +0.03107 | Personal names and geographic/name-like entities. |
| C1 | 377 | 1,532 / 2,192 | 13.94 | +0.03188 | Characterisation, discussion, acquisition and developmental/social processes. |
| C2 | 346 | 1,785 / 1,857 | 15.68 | +0.03150 | Common grammatical/function words and lexical fragments. |
| C3 | 342 | 1,390 / 1,919 | 13.74 | +0.03136 | Entrepreneurship, organisations and employment mixed with media and institutional activity. |
| C4 | 318 | 1,246 / 1,820 | 13.56 | +0.03185 | Biomedical/infant-health and theoretical-system concepts mixed with affect and freshness terms. |
| C5 | 248 | 911 / 1,590 | 13.76 | +0.03183 | Measurement, quantification, transformation and detection. |
| C6 | 234 | 1,221 / 615 | 13.06 | +0.03254 | Mathematical/code punctuation and symbolic formatting. |
| C7 | 145 | 482 / 856 | 12.55 | +0.03142 | Photography/browser/software terms mixed with biomedical abbreviations. |
| C8 | 142 | 852 / 255 | 13.80 | +0.03053 | Numeric strings and short coded values. |
| C9 | 130 | 370 / 991 | 13.32 | +0.03188 | Ambiguity, interpretation and uncertainty-related stems; lexical/morphological form remains substantial. |
| C10 | 130 | 439 / 803 | 12.93 | +0.03087 | Acknowledgement, temporal and evaluative/discourse descriptors. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying identity |
|---|---:|---:|---:|---:|---|
| C0 | 472 | 2,171 / 2,015 | 13.47 | -0.03088 | Prohibition, negative/intense evaluation and adverse-change language. |
| C1 | 469 | 1,933 / 2,138 | 12.80 | -0.03154 | Short name-like and technical/code fragments. |
| C2 | 405 | 1,709 / 2,065 | 13.54 | -0.03090 | Administrative characterisation, regulation and constitutional/bureaucratic concepts. |
| C3 | 287 | 1,111 / 1,630 | 13.42 | -0.03150 | Vehicles, terrain, vegetation and built/material objects. |
| C4 | 222 | 1,010 / 1,180 | 14.41 | -0.03155 | Personal names mixed with geographic entities and regions. |
| C5 | 216 | 925 / 1,281 | 14.50 | -0.03235 | Monarchy, empire and mythic/political roles. |
| C6 | 193 | 750 / 846 | 12.16 | -0.03176 | Multilingual words and orthographic/token fragments. |
| C7 | 160 | 683 / 868 | 13.96 | -0.03098 | Cardiovascular disease, malignancy, cytokine biology and pathology. |
| C8 | 106 | 338 / 684 | 12.83 | -0.03104 | Uppercase lexical stems and code/status terms. |
| C9 | 97 | 481 / 272 | 12.72 | -0.03047 | Mathematical/code punctuation and symbol formatting. |
| C10 | 63 | 345 / 163 | 13.54 | -0.02954 | Numeric strings and quantity words. |
| C11 | 51 | 132 / 344 | 11.92 | -0.03099 | Rail transport mixed with Unix/developer tooling. |

## Population accounting

### Positive head

Total nodes: **2,887**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 967 | 33.5% |
| Formal/name substrate | 1,327 | 46.0% |
| Irreducible semantic | 130 | 4.5% |
| Mixed unresolved | 463 | 16.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,887** | **100.0%** |

Semantic-eligible denominator: **1,560 nodes**.

### Negative tail

Total nodes: **2,741**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,315 | 48.0% |
| Formal/name substrate | 928 | 33.9% |
| Irreducible semantic | 447 | 16.3% |
| Mixed unresolved | 51 | 1.9% |
| Unclear | 0 | 0.0% |
| **Total** | **2,741** | **100.0%** |

Semantic-eligible denominator: **1,813 nodes**.

## Positive-side reconstruction

### P+0 — Developmental, organisational and quantitative activity

- **Primary children:** C1, C3, C5
- **Primary nodes:** 967
- **Side-relative coverage:** 33.5%
- **Semantic-eligible coverage:** 62.0%
- **Confidence:** High

**Evidence.** C1 contains characterisation, conversation, acquisition,
development, discussion and negotiation. C3 contains entrepreneurship,
organisations, employment, media production and institutional activity. C5
contains measurement, quantification, transformation, regularisation and
detection. The triad is strongly connected: C1–C3 has **432 token edges**,
mean cosine **0.09716**; C1–C5 **378** at **0.10507**; C3–C5 **255** at
**0.09556**. The minimum common generator is organised developmental activity:
situations or systems are discussed and developed, institutionalised through
enterprise/organisational action, and measured or transformed through
quantitative analysis.

**Secondary links:** C4, C7 and C10. C1–C4 has **302 edges**, C3–C4 **339**
and C5–C4 **208**, placing biomedical/theoretical material close to the
parent. C3–C7 has **120** and C5–C7 **138**, linking media/software activity.
C1–C10 has **176**, C3–C10 **111**, C5–C10 **52**, placing evaluative/discourse
language around the structure.

**Exclusion boundary.** C4 combines biomedical, infant-health,
theoretical-system, affect and freshness semantics. C7 combines
photography/software with biomedical abbreviations. C10 is modifier/discourse
oriented. None is required to explain the core developmental-organisational-
quantitative relation.

**Alternative.** Include C4 under a broader
`developmental, organisational and biomedical systems` parent. Rejected
because the biomedical/theoretical/affective mixture is not discriminatively
explained by the same generator.

### Positive irreducible and unresolved structures

- **C4 — mixed-unresolved:** biomedical/infant-health, theoretical-system,
  affect and freshness material; strong secondary relation to P+0.
- **C7 — mixed-unresolved:** photography/browser/software concepts mixed with
  biomedical abbreviations.
- **C10 — irreducible-semantic:** acknowledgement, temporal and evaluative/
  discourse descriptors; secondary relation to P+0.

### Positive formal/name substrate

- C0 — personal names/geographic entities
- C2 — grammar/function words and fragments
- C6 — mathematical/code punctuation
- C8 — numeric strings/codes
- C9 — ambiguity/interpretation/uncertainty stems with dominant
  lexical/morphological organisation

## Negative-side reconstruction

### P-0 — Regulatory characterisation and adverse/prohibitive intervention

- **Primary children:** C0, C2
- **Primary nodes:** 877
- **Side-relative coverage:** 32.0%
- **Semantic-eligible coverage:** 48.4%
- **Confidence:** High

**Evidence.** C0 contains prohibition, adverse evaluation, detriment and
negative change. C2 contains administrative characterisation, regulation,
constitutional/bureaucratic concepts and beneficiaries. Their direct relation
contains **663 token edges**, mean cosine **0.09749**, the strongest semantic
relation in State 30. The minimum common generator is institutional state
control: conditions are administratively characterised and regulated while
being prohibited, negatively evaluated or subjected to adverse change.

**Secondary links:**
- **C3:** C0–C3 has **307 edges**, C2–C3 **298**, placing material/built
  environments strongly inside the control field.
- **C7:** C0–C7 has **131 edges**, C2–C7 **162**, linking pathology to
  regulation and adverse evaluation.
- **P-1:** C0–C5 has **214**, C2–C5 **296**, connecting authority roles to the
  control architecture without absorbing them.

**Exclusion boundary.** C0 is evaluative/prohibitive while C2 is
administrative/descriptive. C3 remains physical/material, C7 remains clinical,
and C5/C4 represent authority and territory rather than the control operation
itself.

### P-1 — Territorial identity and institutional/mythic authority

- **Primary children:** C4, C5
- **Primary nodes:** 438
- **Side-relative coverage:** 16.0%
- **Semantic-eligible coverage:** 24.2%
- **Confidence:** Moderate / High

**Evidence.** C4 contains personal names plus geographic entities and regions.
C5 contains monarchy, empire and mythic/political roles. Their direct relation
contains **217 token edges**, mean cosine **0.09680**. The minimum common
generator is institutional and symbolic authority situated within territorial
and social identity.

**Secondary link:** C3. C3–C4 has **167 edges** and C3–C5 **200**, showing
that built/material environments provide settings for authority and territory.

**Exclusion boundary.** C4 is entity/territory centred and C5 is authority/role
centred. C3 is a material environment rather than authority itself.

### Negative irreducible and unresolved structures

- **C3 — irreducible-semantic:** vehicles, terrain, vegetation and
  built/material objects; secondary relation to P-0 and P-1.
- **C7 — irreducible-semantic:** cardiovascular/malignancy/cytokine pathology;
  secondary relation to P-0.
- **C11 — mixed-unresolved:** rail transport and Unix/developer tooling coexist
  without a single sufficient generator.

### Negative formal/name substrate

- C1 — short name-like and technical/code fragments
- C6 — multilingual lexical/orthographic fragments
- C8 — uppercase lexical/status/code fragments
- C9 — mathematical/code punctuation
- C10 — numeric strings/quantity words

## Community disposition table

| Side | Community | Size | Primary disposition | Secondary links |
|---|---|---:|---|---|
| + | C0 | 475 | formal-substrate | — |
| + | C1 | 377 | parent:P+0 | — |
| + | C2 | 346 | formal-substrate | — |
| + | C3 | 342 | parent:P+0 | — |
| + | C4 | 318 | mixed-unresolved | P+0 |
| + | C5 | 248 | parent:P+0 | — |
| + | C6 | 234 | formal-substrate | — |
| + | C7 | 145 | mixed-unresolved | P+0 |
| + | C8 | 142 | formal-substrate | — |
| + | C9 | 130 | formal-substrate | — |
| + | C10 | 130 | irreducible-semantic | P+0 |
| − | C0 | 472 | parent:P-0 | — |
| − | C1 | 469 | formal-substrate | — |
| − | C2 | 405 | parent:P-0 | — |
| − | C3 | 287 | irreducible-semantic | P-0, P-1 |
| − | C4 | 222 | parent:P-1 | — |
| − | C5 | 216 | parent:P-1 | P-0 |
| − | C6 | 193 | formal-substrate | — |
| − | C7 | 160 | irreducible-semantic | P-0 |
| − | C8 | 106 | formal-substrate | — |
| − | C9 | 97 | formal-substrate | — |
| − | C10 | 63 | formal-substrate | — |
| − | C11 | 51 | mixed-unresolved | — |

Every State 30 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Developmental, organisational and quantitative activity | C1, C3, C5 | 967 | 33.5% | 62.0% | High |
| P-0 | Regulatory characterisation and adverse/prohibitive intervention | C0, C2 | 877 | 32.0% | 48.4% | High |
| P-1 | Territorial identity and institutional/mythic authority | C4, C5 | 438 | 16.0% | 24.2% | Moderate / High |

Positive retained parents account for **967 nodes**, **33.5% of the positive
population** and **62.0% of semantic-eligible positive nodes**.

Negative retained parents account for **1,315 nodes**, **48.0% of the negative
population** and **72.5% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 is strongly triangulated.**
   C1–C3 has **432 edges**, C1–C5 **378**, C3–C5 **255**.

2. **P+0 ↔ C4 — organised activity and biomedical/theoretical structure — High but unresolved.**
   C1–C4 has **302 edges**, C3–C4 **339**, C5–C4 **208**. The graph evidence
   is strong, but C4's internal biomedical/theoretical/affective mixture blocks
   primary absorption.

3. **P+0 ↔ C7 — organisational activity and media/software structure — Moderate.**
   C1–C7 has **46 edges**, C3–C7 **120**, C5–C7 **138**.

4. **P+0 ↔ C10 — activity and evaluative/discourse context — Moderate.**
   C1–C10 has **176 edges**, C3–C10 **111**, C5–C10 **52**.

5. **Formal/name communities remain graph-connected without semantic promotion.**
   C1–C2 has **437 edges**, C2–C5 **297**, and C0–C4 **326**. Connectivity
   alone does not override formal or entity organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — control architecture in authority/territorial context — High.**
   C0–C5 has **214 edges**, C2–C5 **296**, C0–C4 **90**, C2–C4 **115**.

2. **P-0 ↔ C3 — regulation/adverse control and material environment — High.**
   C0–C3 has **307 edges**, C2–C3 **298**.

3. **P-0 ↔ C7 — control/judgement and clinical pathology — Moderate to High.**
   C0–C7 has **131 edges**, C2–C7 **162**.

4. **P-1 ↔ C3 — authority/territory and material setting — High.**
   C3–C4 has **167 edges**, C3–C5 **200**.

5. **Negative C1 remains formal despite broad connectivity.**
   C1–C6 has **338 edges**, C1–C4 **332**, C1–C3 **319**; its underlying
   community is dominated by short name-like and technical fragments.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 30 cross-side evidence inspected in the State 30 packet is
dominated by near-form relations such as `chr`↔` chr` and
`height`↔`Height`. These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C4 and negative C7 through biomedical/pathological structure;
- positive C0 and negative P-1 through geographic/entity organisation.

## Formal/representational substrate

### Positive — 1,327 nodes / 46.0%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation;
- numeric strings;
- ambiguity/interpretation/uncertainty lexical stems.

### Negative — 928 nodes / 33.9%

- short name-like and technical/code fragments;
- multilingual lexical/orthographic fragments;
- uppercase lexical/status/code fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 30 — BLOCK 29 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 DEVELOPMENTAL / ORGANISATIONAL / QUANTITATIVE ACTIVITY
|   +-- C1 characterisation/discussion/acquisition/development
|   +-- C3 enterprise/organisations/employment/media
|   `-- C5 measurement/quantification/transformation/detection
|       |
|       +-- C4 biomedical/theoretical/affect/freshness   [secondary; mixed]
|       +-- C7 photography/software + biomedical abbrev  [secondary; mixed]
|       `-- C10 acknowledgement/temporal/evaluative     [secondary]
|
+-- C4 biomedical/infant-health + theoretical/affect    [mixed unresolved]
+-- C7 photography/browser/software + biomedical abbrev [mixed unresolved]
+-- C10 acknowledgement/temporal/evaluative discourse   [irreducible]
`-- C0,C2,C6,C8,C9                                     [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY CHARACTERISATION & ADVERSE/PROHIBITIVE INTERVENTION
|   +-- C0 prohibition/adverse evaluation/change
|   `-- C2 administration/regulation/constitutional structure
|       |
|       +-- C3 material environment                     [secondary]
|       +-- C7 cardiovascular/malignancy pathology      [secondary]
|       `-- P-1 institutional/mythic authority          [related]
|
+-- P-1 TERRITORIAL IDENTITY & INSTITUTIONAL/MYTHIC AUTHORITY
|   +-- C4 names/geographic entities/regions
|   `-- C5 monarchy/empire/mythic-political roles
|       \
|        -- C3 vehicles/terrain/material setting       [secondary]
|
+-- C3 vehicles/terrain/vegetation/material objects     [irreducible]
+-- C7 cardiovascular/malignancy/cytokine pathology    [irreducible]
+-- C11 rail transport + Unix/developer tooling         [mixed unresolved]
`-- C1,C6,C8,C9,C10                                   [formal/name substrate]
```

The preferred State 30 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by a strongly
triangulated developmental-organisational-quantitative architecture. The
negative side is dominated by a strong regulatory/adverse-control parent, with
territorial/institutional authority retained separately.

This statement is local to State 30 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. expand positive P+0 to include C4 under a broader
   **developmental/biomedical/organisational systems** parent;
2. split positive P+0 into C1+C5 **developmental/quantitative analysis** and
   C3 **organisational activity**;
3. expand negative P-0 to include C5 under a broader
   **regulation and institutional authority** parent;
4. leave negative C4 and C5 separate rather than retaining P-1.

The first and fourth alternatives are the most serious. C4 is exceptionally
well connected to the positive parent but remains too heterogeneous for
non-vacuous inclusion. P-1 is retained because C4–C5 is both semantically
discriminative and strongly connected.

## Uncertainty record

- **Positive P+0:** strongly triangulated and therefore High confidence.
- **Positive C4:** principal positive ambiguity because graph evidence favours
  inclusion but semantic discrimination favours leaving it unresolved.
- **Positive C7:** coherent software/media material is mixed with biomedical
  abbreviations.
- **Negative P-0:** C0–C2 is the dominant semantic core.
- **Negative P-1:** semantically coherent and reasonably strong, but smaller
  than P-0.
- **Negative C11:** rail transport and developer tooling coexist in one small
  mixed community.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,887 / 2,887**
- Negative node accounting: **2,741 / 2,741**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 30 community inspected at underlying R008 community-record level: **yes**
- All State 30 within-side community relations inspected: **yes**
- State 30 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 30 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 30 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
