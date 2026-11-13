# R010 State 04 — Block 3 output latent structure

## State identity

- R010 state index: `04`
- R008/R009 state: `block_03_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 13 negative-tail = 25**
- R008 population: **3,054 positive-head + 3,100 negative-tail = 6,154 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 04 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

For every State 04 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_04_block_03_output.md`;
2. State 04 entries in `R009_SUMMARY.html`;
3. all 25 State 04 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. the full State 04 within-side relation set in
   `R008/community_edges.csv`;
5. the State 04 R008 layer packet.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Communities whose compact underlying evidence
remained materially mixed were retained as mixed or Moderate rather than
promoted through unsupported certainty.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 404 | 1,689 / 1,990 | 13.29 | +0.03088 | Information/task operations dominate: `initiating`, `participating`, `retrieving`, `extracted`, `recognizing`, `formatted`, `determining`, `maintaining`, `accessing`, `formulated`, `withdrawing`. |
| C1 | 373 | 1,680 / 1,962 | 14.27 | +0.03114 | Function words and short lexical fragments dominate. |
| C2 | 372 | 1,604 / 1,967 | 13.91 | +0.03170 | Biomedical/biological vocabulary is prominent: `immunosuppressive`, `glucocortic`, `infertility`, `evolutionary`, `obesity`, `phyt`, `Bcl`; food/agricultural terms such as `rice`, `cakes`, `beet` are genuine secondary structure. |
| C3 | 330 | 1,148 / 1,813 | 12.45 | +0.03111 | Multilingual, encoding and fragmentary lexical residues dominate; no stable semantic centre. |
| C4 | 264 | 1,206 / 1,243 | 13.84 | +0.03092 | Cities, countries, nationalities and personal/place names dominate: Nigerian, Charlotte, Indonesian, Orlando, Sacramento, Charleston, Egyptian, Chicago, Sydney, California. |
| C5 | 262 | 1,081 / 1,331 | 13.33 | +0.03158 | Database/software vocabulary mixed with technical abbreviations: `Database`, `mysql`, `MySQL`, `Django`, `DB`, plus networking/system abbreviations. |
| C6 | 248 | 846 / 1,595 | 13.25 | +0.03128 | Molecular/physical-science and computing/server structure coexist: `conformational`, `renormalization`, `molecule`, `molecules`, `cyclin`, `cationic`, `interacting`, with `Server`, `server`, `Hash`, `Entry`. |
| C7 | 247 | 1,369 / 627 | 13.62 | +0.03160 | Strong punctuation/bracket/code-formatting cluster; 165 of 247 tokens are punctuation/symbols. |
| C8 | 190 | 799 / 1,056 | 13.97 | +0.03129 | Affective/evaluative/contextual language dominates: `emotional`, `emotionally`, `Eventually`, `Subsequently`, `culturally`, `interesting`, `obviously`, `environmentally`, `bitterly`. |
| C9 | 153 | 559 / 1,008 | 13.90 | +0.03142 | Finance, politics, administration and institutional/social relations dominate: `Financial`, `Political`, `parliamentary`, `transactions`, `Goldman`, `Legislative`, `administrative`, `familial`. |
| C10 | 139 | 828 / 284 | 13.96 | +0.02982 | Strong numeric cluster. |
| C11 | 72 | 313 / 340 | 13.42 | +0.03041 | Calendar years, weekdays and time terms coexist with theatre/cinema/performance terms. The calendar component is coherent but the community remains mixed. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 551 | 2,401 / 2,402 | 13.07 | -0.03116 | Personal names dominate but short lexical stems/fragments are substantial; treated as name/form substrate rather than one semantic domain. |
| C1 | 380 | 1,654 / 2,120 | 14.28 | -0.03094 | Analysis, description, estimation and explanation dominate: `Characteristics`, `analysis`, `descriptions`, `estimates`, `pathophysiology`, `recommendations`, `Experiments`, `epidemiology`, `concepts`, `explanations`. |
| C2 | 346 | 1,598 / 1,865 | 14.63 | -0.03134 | Authority, institutional/religious roles and law dominate: `unconstitutional`, `Archbishop`, `Congressman`, `Chairman`, `leaders`, `professor`, `Officers`, `Rabbi`, `Laws`; fictional/creative material broadens it. |
| C3 | 288 | 1,355 / 1,475 | 14.53 | -0.03149 | Function words, suffixes and fragments dominate. |
| C4 | 261 | 1,069 / 1,484 | 13.88 | -0.03165 | Negative evaluation, discomfort, threat and perceptual descriptors dominate: `uncomfortable`, `unacceptable`, `terrifying`, `annoying`, `horrific`, `tragedy`, with positive/intensity counterexamples such as `impressive`, `gorgeous`. |
| C5 | 233 | 855 / 1,462 | 13.61 | -0.03145 | Change/regulation/action vocabulary dominates: `decrease`, `alteration`, `dropped`, `constructing`, `prohibited`, `determined`, `Increase`, `improve`, `reported`; extremes add `Beginning`, `bolster`, `revive`, `mandate`. |
| C6 | 226 | 898 / 1,295 | 13.68 | -0.03133 | Clinical/biological vocabulary is strong (`hospitalization`, `echocardiography`, `angiography`, `pathogens`, `anesthesia`, `cerebellum`, `biopsy`, `allele`) but fantasy/conflict roles (`warriors`, `monsters`, `villain`, `Devil`) are a genuine second component. |
| C7 | 214 | 855 / 1,239 | 13.78 | -0.03148 | Built environment, weapons, transport and objects coexist: hallways/stairs, guns/rifles, cliffs, trucks, floors, sidewalks, clothing, appliances and rail. |
| C8 | 176 | 573 / 1,001 | 12.20 | -0.03134 | Abstract mathematics and software/programming coexist: morphisms/functor/bigoplus/maps alongside databind, addr, compiler, plugins, Decoder, sdk, Pointer and uint. |
| C9 | 137 | 461 / 683 | 11.72 | -0.03084 | Multilingual and orthographic fragments dominate. |
| C10 | 124 | 742 / 214 | 13.69 | -0.03109 | Extremely pure mathematical/code punctuation cluster; 117 of 124 tokens are punctuation/symbols. |
| C11 | 83 | 290 / 595 | 14.16 | -0.03141 | Violence/crime/destruction is coherent: `murdered`, `kill`, `murders`, `massacre`, `killing`, `murder`, `thief`, `uprising`, `destroyed`, `slaughter`; extremes include arrest/indicted/doomed. |
| C12 | 81 | 463 / 193 | 13.81 | -0.02999 | Numeric strings, including historical years, dominate. |

## Population accounting

### Positive head

Total nodes: **3,054**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,703 | 55.8% |
| Formal substrate | 1,089 | 35.7% |
| Irreducible semantic | 190 | 6.2% |
| Mixed unresolved | 72 | 2.4% |
| Unclear | 0 | 0.0% |
| **Total** | **3,054** | **100.0%** |

Semantic-eligible denominator: **1,965 nodes**.

### Negative tail

Total nodes: **3,100**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,529 | 49.3% |
| Formal/name substrate | 1,181 | 38.1% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 390 | 12.6% |
| Unclear | 0 | 0.0% |
| **Total** | **3,100** | **100.0%** |

Semantic-eligible denominator: **1,919 nodes**.

## Positive-side reconstruction

### P+0 — Information/task operations and digital systems

- **Primary children:** C0, C5
- **Primary nodes:** 666
- **Side-relative coverage:** 21.8%
- **Semantic-eligible coverage:** 33.9%
- **Confidence:** High

**Evidence.** C0 supplies information retrieval, formatting, recognition,
maintenance and task/process operations. C5 supplies databases, software and
technical systems. Their direct relation contains **127 token edges**, mean
cosine **0.08533**. More importantly, both are strongly embedded with C6 and
other technical communities, supporting a common information/technical frame.

**Secondary link:** C6. C0–C6 has **356 edges**, one of the strongest positive
relations, and C5–C6 has **125**. C6 is not a primary child because its
molecular/physical-science structure is equally material.

**Exclusion boundary.** C8 is contextual/evaluative rather than information
infrastructure. C3 contains fragmentary forms rather than semantic technical
content.

**Alternative.** Include C6 as a third child under a broader
`information, computation and scientific systems` parent. This is rejected
because it would erase C6's molecular/physical-science organisation.

### P+1 — Biological, molecular and physical-scientific systems

- **Primary children:** C2, C6
- **Primary nodes:** 620
- **Side-relative coverage:** 20.3%
- **Semantic-eligible coverage:** 31.6%
- **Confidence:** High / Moderate

**Evidence.** C2 contains biomedical, biological, metabolic and food/agricultural
material. C6 contains conformational, molecular, physical-science and
interaction terms. Their direct relation contains **336 token edges**, mean
cosine **0.09366**, one of the strongest positive semantic relations in the
state.

**Secondary link:** C5 and C0 through C6's computing/server component.

**Exclusion boundary.** C2's food/agricultural terms and C6's server/hash terms
are preserved as heterogeneity rather than reinterpreted. C9 is institutional
and financial rather than scientific.

**Alternative.** Leave C2 and C6 as separate mixed communities. This becomes
preferable if complete token membership shows their secondary components are
comparable in size to the proposed scientific cores.

### P+2 — Geographic, political and institutional-economic organisation

- **Primary children:** C4, C9
- **Primary nodes:** 417
- **Side-relative coverage:** 13.7%
- **Semantic-eligible coverage:** 21.2%
- **Confidence:** High

**Evidence.** C4 supplies cities, countries and nationalities. C9 supplies
finance, politics, parliament, legislation, administration, employment and
institutional relations. Their direct relation contains **142 token edges**,
mean cosine **0.09334**.

**Exclusion boundary.** C8 is evaluative/contextual language rather than a
social institution domain. C11 is calendar/performance scheduling.

**Alternative.** Treat C4 as a name/geography substrate and leave C9
irreducible. This is not preferred because C4 is a coherent geographic domain,
not an arbitrary collection of names.

### Positive irreducible and unresolved structures

- **C8 — irreducible-semantic:** affective/evaluative/contextual discourse. It
  connects strongly to several parents but remains too general to belong
  primarily to one.
- **C11 — mixed-unresolved:** calendar/time plus theatre/cinema/performance
  scheduling.
- **C1, C3, C7, C10 — formal-substrate:** grammar/fragments,
  multilingual/encoding residue, punctuation and numerics.

## Negative-side reconstruction

### P-0 — Analytical/clinical description and explanation

- **Primary children:** C1, C6
- **Primary nodes:** 606
- **Side-relative coverage:** 19.5%
- **Semantic-eligible coverage:** 31.6%
- **Confidence:** Moderate

**Evidence.** C1 centres on analysis, description, estimation, recommendations,
experiments, epidemiology and explanation. C6 contains clinical diagnostics,
pathology, anatomy and biological mechanisms. Their direct relation contains
**226 token edges**, mean cosine **0.10591**, among the strongest semantic
relations in the state.

**Secondary link:** C8. C1–C8 has **210 edges**, but C8's mathematical/software
mixture is too heterogeneous for primary absorption.

**Exclusion boundary.** C6's fantasy/conflict terms are explicitly preserved.
C5 concerns state change/regulation rather than description and explanation.

**Alternative.** Absorb C8 into a broader
`formal/scientific analysis and computation` parent. This is rejected because
C8 contains two different organising principles and would make the parent less
discriminative.

### P-1 — Evaluation, regulation and state change

- **Primary children:** C4, C5
- **Primary nodes:** 494
- **Side-relative coverage:** 15.9%
- **Semantic-eligible coverage:** 25.7%
- **Confidence:** High

**Evidence.** C4 contains negative evaluation, threat, discomfort and
distinguishability/intensity descriptors. C5 contains decrease/increase,
alteration, construction, prohibition, determination, improvement and mandate.
Their direct relation contains **221 token edges**, mean cosine **0.09947**.
Together they describe states being evaluated and altered, constrained or
regulated.

**Secondary link:** C11. C4–C11 has **85 edges**, and violent/destructive
events instantiate highly adverse state changes.

**Exclusion boundary.** C11 is specifically violence/crime, not general
evaluation/change. C2 concerns authority/social roles rather than change
mechanisms.

**Alternative.** Include C11 as a third child under an
`adverse evaluation and destructive change` parent. This is rejected because
P-1 also contains neutral/constructive change and comparative/perceptual
evaluation.

### P-2 — Institutional authority, social roles and conflict

- **Primary children:** C2, C11
- **Primary nodes:** 429
- **Side-relative coverage:** 13.8%
- **Semantic-eligible coverage:** 22.4%
- **Confidence:** Moderate

**Evidence.** C2 contains institutional, religious and authority roles plus
law-related terms. C11 contains violence, crime and destruction. Their direct
relation contains **118 token edges**, mean cosine **0.09888**. The larger frame
is authority/social order and conflict or transgression.

**Secondary links:** C7 through weapons/built settings; C6 through
warrior/monster/villain content.

**Exclusion boundary.** C2 contains professions/religious figures not inherently
conflictual, while C11 is specifically violent. C7 includes ordinary transport,
clothing and built-environment objects.

**Alternative.** Leave C11 irreducible and treat C2 as an institutional-role
island. This remains a serious alternative; P-2 is therefore Moderate.

### Negative mixed unresolved structures

- **C7 — mixed-unresolved:** built environment, weapons, transport, clothing
  and physical objects. It has secondary relations to P-2 and P-1 but no single
  parent explains the whole community.
- **C8 — mixed-unresolved:** abstract mathematics and software/programming. It
  has a secondary analytical relation to P-0 but retains two organising
  principles.

### Negative formal/name substrate

- C0 — names plus lexical fragments
- C3 — grammar/function words/suffixes
- C9 — multilingual/orthographic fragments
- C10 — mathematical/code punctuation
- C12 — numeric strings

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 404 | Information retrieval/task/process actions | parent:P+0 | — | Information/task operations. |
| + | C1 | 373 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C2 | 372 | Biomedical/biological + food/agriculture | parent:P+1 | — | Biological/scientific core dominates. |
| + | C3 | 330 | Multilingual/encoding fragments | formal-substrate | — | Tokeniser/orthographic form. |
| + | C4 | 264 | Cities/countries/nationalities/names | parent:P+2 | — | Coherent geographic domain. |
| + | C5 | 262 | Databases/software/technical abbreviations | parent:P+0 | — | Digital/information systems. |
| + | C6 | 248 | Molecular/physical science + computing | parent:P+1 | P+0 | Scientific core with technical-system overlap. |
| + | C7 | 247 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser structure. |
| + | C8 | 190 | Affective/evaluative/discourse | irreducible-semantic | P+0, P+2 | General contextual/evaluative structure overlaps domains without belonging wholly to one. |
| + | C9 | 153 | Finance/politics/admin/institutional relations | parent:P+2 | — | Institutional-economic organisation. |
| + | C10 | 139 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C11 | 72 | Calendar/time + leisure/performance | mixed-unresolved | — | Calendar and performance structures coexist. |
| − | C0 | 551 | Personal names + fragments | formal-substrate | — | Name/form organisation without one domain. |
| − | C1 | 380 | Analysis/scientific description/explanation | parent:P-0 | — | Analytical/scientific description. |
| − | C2 | 346 | Authority/institutional/religious/social roles + law | parent:P-2 | — | Institutional authority/social-order structure. |
| − | C3 | 288 | Grammar/function words/suffixes | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 261 | Negative evaluation/threat/discomfort | parent:P-1 | — | Evaluation/adverse-state description. |
| − | C5 | 233 | Change/construction/regulation actions | parent:P-1 | — | State change and regulation. |
| − | C6 | 226 | Clinical biology + fantasy/conflict | parent:P-0 | P-2 | Clinical core supports analysis parent; conflict material retained as heterogeneity. |
| − | C7 | 214 | Built/weapons/transport/objects | mixed-unresolved | P-2 | Physical setting/weapon relation, but broad object content. |
| − | C8 | 176 | Abstract maths + software/programming | mixed-unresolved | P-0 | Analytical affinity but dual organising principles. |
| − | C9 | 137 | Multilingual/orthographic fragments | formal-substrate | — | Orthographic form. |
| − | C10 | 124 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C11 | 83 | Violence/crime/destruction | parent:P-2 | P-1 | Conflict/transgression structure with adverse-change relation. |
| − | C12 | 81 | Numeric strings/years | formal-substrate | — | Numeric form. |

Every State 04 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information/task operations and digital systems | C0, C5 | 666 | 21.8% | 33.9% | High |
| P+1 | Biological, molecular and physical-scientific systems | C2, C6 | 620 | 20.3% | 31.6% | High / Moderate |
| P+2 | Geographic, political and institutional-economic organisation | C4, C9 | 417 | 13.7% | 21.2% | High |
| P-0 | Analytical/clinical description and explanation | C1, C6 | 606 | 19.5% | 31.6% | Moderate |
| P-1 | Evaluation, regulation and state change | C4, C5 | 494 | 15.9% | 25.7% | High |
| P-2 | Institutional authority, social roles and conflict | C2, C11 | 429 | 13.8% | 22.4% | Moderate |

Positive retained parents account for **1,703 nodes**, **55.8% of the positive
population** and **86.7% of semantic-eligible positive nodes**.

Negative retained parents account for **1,529 nodes**, **49.3% of the negative
population** and **79.7% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — technical/scientific system relation — High.**
   C0–C6 has **356 edges**, C2–C6 **336**, C2–C5 **222**, and C5–C6 **125**.
   Scientific material and information systems are strongly interwoven while
   retaining distinct organising principles.

2. **P+0 ↔ P+2 — information/institutional relation — Moderate.**
   C0–C9 has **191 edges**, C4–C5 **140**, and C5–C9 **44**. Information
   operations and digital systems participate in institutional/economic
   organisation without reducing to it.

3. **P+1 ↔ P+2 — biological/social context relation — Moderate.**
   C2–C9 has **181 edges**, C2–C4 **200**, and C4–C6 **83**. The domains are
   connected but remain discriminable.

4. **C8 is an evaluative/contextual bridge-like irreducible structure.**
   It connects to C0 (**274 edges**), C2 (**135**) and C9 (**90**) but is too
   general to justify a separate multi-community parent.

### Negative-side relations

1. **P-0 ↔ P-1 — analysis/evaluation/change relation — High.**
   C1–C4 has **286 edges**, C1–C5 **318**, C4–C6 **107** and C5–C6 **69**.
   Analytical description, evaluation and state change are tightly coupled but
   remain distinguishable.

2. **P-0 ↔ P-2 — analysis/institutional relation — High.**
   C1–C2 has **281 edges**, C2–C6 **202**, and C1–C11 **74**. Institutional
   roles and clinical/scientific description strongly interact.

3. **P-1 ↔ P-2 — adverse change/conflict relation — Moderate.**
   C4–C11 has **85 edges**, C2–C5 **142**, and C5–C11 **77**. Conflict and
   institutional authority are connected to evaluation/change without being
   identical.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible semantic correspondences exist between:

- positive P+0 and negative C8 through computing/software;
- positive P+1 and negative P-0 through biomedical/scientific structure;
- positive P+2 and negative P-2 through institutional/social organisation.

The compact cross-side evidence does not independently establish these as
parent-level bridges, so they remain unpromoted.

## Formal/representational substrate

### Positive — 1,089 nodes / 35.7%

- grammar/function words and fragments;
- multilingual/encoding residues;
- punctuation/formatting;
- numeric strings.

### Negative — 1,181 nodes / 38.1%

- personal names plus fragments;
- grammar/function words/suffixes;
- multilingual/orthographic fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 04 — BLOCK 3 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION / TASK OPERATIONS & DIGITAL SYSTEMS
|   +-- C0 retrieval/participation/process actions
|   `-- C5 databases/software/technical systems
|       \
|        -- C6 scientific/computing overlap          [secondary]
|
+-- P+1 BIOLOGICAL / MOLECULAR / PHYSICAL-SCIENTIFIC SYSTEMS
|   +-- C2 biomedical/biological + food/agriculture
|   `-- C6 molecular/physical science + computing
|
+-- P+2 GEOGRAPHIC / POLITICAL / INSTITUTIONAL-ECONOMIC ORGANISATION
|   +-- C4 cities/countries/nationalities
|   `-- C9 finance/politics/admin/social relations
|
+-- C8 affective/evaluative/contextual discourse       [irreducible]
+-- C11 calendar/time + performance                    [mixed unresolved]
`-- C1,C3,C7,C10                                      [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ANALYTICAL / CLINICAL DESCRIPTION & EXPLANATION
|   +-- C1 analysis/scientific description
|   `-- C6 clinical biology + conflict heterogeneity
|       \
|        -- C8 abstract maths/software                [secondary; mixed]
|
+-- P-1 EVALUATION / REGULATION / STATE CHANGE
|   +-- C4 negative evaluation/threat/discomfort
|   `-- C5 change/construction/regulation
|       \
|        -- C11 violence/destruction                  [secondary]
|
+-- P-2 INSTITUTIONAL AUTHORITY / SOCIAL ROLES / CONFLICT
|   +-- C2 authority/institutional/religious roles + law
|   `-- C11 violence/crime/destruction
|       \
|        -- C7 weapons/physical setting               [secondary; mixed]
|
+-- C7 built/weapons/transport/objects                 [mixed unresolved]
+-- C8 abstract maths/software                         [mixed unresolved]
`-- C0,C3,C9,C10,C12                                  [formal/name substrate]
```

The preferred State 04 reconstruction contains three positive and three
negative multi-community parents. The positive side is organised around
information/technical systems, scientific/biological systems and
geographic-institutional organisation. The negative side is organised around
analysis/clinical description, evaluation/change and institutional
authority/conflict, while mixed physical-object and maths/software communities
remain deliberately unresolved.

This statement is local to State 04 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction makes two broader mergers:

1. merge positive P+0 and P+1 into a single
   **technical/scientific information systems** parent, motivated by the very
   strong C0–C6 and C2–C6 relations;
2. merge negative P-1 and P-2 into an
   **adverse regulation, authority and conflict** parent.

Both improve compression but weaken discriminative value. The positive merger
would collapse scientific objects/processes into their information
infrastructure; the negative merger would conflate general state change and
evaluation with social authority and violence.

## Uncertainty record

- **Positive P+1:** C2 and C6 are both mixed, so the parent remains partly
  dependent on their dominant scientific cores rather than complete purity.
- **Positive C8:** is structurally well connected but too general and
  modifier-like to assign primarily to one parent.
- **Positive C11:** calendar/time and performance terms coexist; it remains
  mixed-unresolved.
- **Negative P-0:** C6 contains substantial fantasy/conflict vocabulary, so the
  clinical-analysis parent is Moderate rather than fully clean.
- **Negative P-2:** authority/social-role and violence structures form a
  plausible larger frame, but neither implies the other; confidence remains
  Moderate.
- **Negative C7/C8:** both are genuinely mixed and were not forced into parents
  despite strong graph connectivity.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **25 / 25**
- Positive node accounting: **3,054 / 3,054**
- Negative node accounting: **3,100 / 3,100**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1, P-2**
- Every retained parent has an exclusion boundary: **yes**
- Every community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 04 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
