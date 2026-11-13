# R010 State 06 — Block 5 output latent structure

## State identity

- R010 state index: 06
- R008/R009 state: block_05_output
- Analysis model: **GPT-5.6 Sol**
- Protocol: R010_ANALYSIS_PROTOCOL.md
- R009 communities: **13 positive-head + 13 negative-tail = 26**
- R008 population: **2,951 positive-head + 3,152 negative-tail = 6,103 nodes**
- Status: **clean Phase-A rerun complete**

This file replaces the earlier State 06 reconstruction. The replacement was constructed independently from State 06 R008/R009 evidence only. The previous R010 State 06 reconstruction was not inspected before the replacement hypothesis was frozen.

No State 07 semantic content was exposed during this rerun.

## Evidence inventory

Evidence used:

1. R009/STATE_06_block_05_output.md;
2. all 26 State 06 rows in R008 community_nodes.csv;
3. the complete State 06 within-side relation set in R008 community_edges.csv;
4. the State 06-only section of chatgpt_layer_packets.md, trimmed before the State 07 heading, including compact State 06 cross-side relations.

The compressed token-level membership artifact was not decoded through the available GitHub text connector. Materially mixed communities remain mixed or are assigned only where the compact evidence is sufficient.

## Population accounting

### Positive head

Total nodes: **2,951**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,635 | 55.4% |
| Formal/name substrate | 1,057 | 35.8% |
| Irreducible semantic | 259 | 8.8% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,951** | **100.0%** |

Semantic-eligible denominator: **1,894 nodes**.

### Negative tail

Total nodes: **3,152**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,429 | 45.3% |
| Formal/name substrate | 1,441 | 45.7% |
| Irreducible semantic | 282 | 8.9% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,152** | **100.0%** |

Semantic-eligible denominator: **1,711 nodes**.

## Positive-side reconstruction

### P+0 — Operational information and task/work systems

- **Primary children:** C0, C3
- **Primary nodes:** 715
- **Side-relative coverage:** 24.2%
- **Semantic-eligible coverage:** 37.8%
- **Confidence:** High

**Evidence.** C0 is organised around databases, transactions, data handling and information systems. C3 is organised around accessing, initiating, working, maintaining, extracting, withdrawing and solving. Their direct relation has **340 token edges**, mean cosine **0.10167**.

The minimum common generator is an operational information-work system: information is stored, transacted or formatted while tasks act on, access, maintain, extract or resolve that information.

**Exclusion boundary.** C5 contains psychosocial/political/financial material, C4 scientific/biomedical material and C7 discourse/evaluative modifiers. A broader information parent would lose discrimination.

### P+1 — Psychosocial, institutional and territorial organisation

- **Primary children:** C5, C6
- **Primary nodes:** 515
- **Side-relative coverage:** 17.5%
- **Semantic-eligible coverage:** 27.2%
- **Confidence:** Moderate

**Evidence.** C5 contains psychosocial, psychological, political, community, parliamentary, financial and employment-related material. C6 contains countries, cities, nationalities and named places/people. Their direct relation has **217 token edges**, mean cosine **0.09341**.

The common generator is socially and institutionally organised populations situated in territorial/geographic contexts.

**Secondary link:** C7. C5–C7 has **178 edges**, mean cosine **0.10090**, placing discourse/evaluative context around the social-institutional structure.

**Exclusion boundary.** C6 is territorial/entity organisation rather than generic social language; C7 is discourse/modifier structure rather than a social-population child.

### P+2 — Biological, physical and organismal living systems

- **Primary children:** C4, C10
- **Primary nodes:** 405
- **Side-relative coverage:** 13.7%
- **Semantic-eligible coverage:** 21.4%
- **Confidence:** Moderate

**Evidence.** C4 contains biomedical, inflammatory, metabolic, molecular and physical-science concepts. C10 contains food, nutrition, plants and animals. Their direct relation has **110 token edges**, mean cosine **0.08747**.

The common generator is living-system material spanning biological mechanisms, metabolism and organismal/nutritional context.

**Exclusion boundary.** C4 also contains physical-science concepts such as spin, carbon and surfaces; C10 is organismal/nutritional. The parent is therefore kept narrower than a generic science or nature structure.

### Positive irreducible structures

- **C7 — irreducible-semantic:** discourse, temporal and evaluative/adverbial language; secondary to P+1.
- **C12 — irreducible-semantic:** calendar time, years, weekdays and seasons.

### Positive formal/name substrate

- C1 — multilingual/malformed lexical residue
- C2 — grammar/function words and short fragments
- C8 — punctuation/formatting
- C9 — acronyms/initialisms
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Adverse assessment and destructive-state characterisation

- **Primary children:** C1, C2
- **Primary nodes:** 910
- **Side-relative coverage:** 28.9%
- **Semantic-eligible coverage:** 53.2%
- **Confidence:** High

**Evidence.** C1 contains destruction, unacceptability, tragedy, terror, constitutional violation and distress. C2 contains assessment, analysis, interpretation, descriptions and clinical diagnostics. Their direct relation is the strongest State 06 semantic connection: **631 token edges**, mean cosine **0.10173**.

The common generator is adverse-state assessment: conditions are analysed or diagnosed while being represented as destructive, unacceptable, tragic or otherwise adverse.

**Secondary links:** C5 and C6. C1–C5 has **314 edges**, mean cosine **0.10641**; C2–C5 **279** at **0.10087**. C1–C6 has **274**, C2–C6 **226**. These relations place institutional/authority and conflict/material settings around the adverse-assessment structure without requiring primary inclusion.

**Exclusion boundary.** C5 is role/authority organisation and C6 is built/transport/weapon/violence material. C7 is anatomy/clinical biology. They remain discriminable from the assessment/adversity mechanism.

### P-1 — Institutional authority, conflict and material setting

- **Primary children:** C5, C6
- **Primary nodes:** 519
- **Side-relative coverage:** 16.5%
- **Semantic-eligible coverage:** 30.3%
- **Confidence:** Moderate

**Evidence.** C5 contains religious and institutional roles, constitutional authority, officers, officials, crime and places. C6 contains built environment, transport, weapons and violence. Their direct relation has **227 token edges**, mean cosine **0.09536**.

The common generator is authority/conflict embedded in a material environment: institutional and role structures coexist with the built, transport and weapon settings through which conflict or control is enacted.

**Secondary relation to P-0:** C1–C5 **314**, C2–C5 **279**, C1–C6 **274**, C2–C6 **226**.

**Exclusion boundary.** C5 is authority/role-centred and C6 material/conflict-setting-centred. C7 is anatomical/clinical and is not absorbed merely because it contains body-surface terms.

### Negative irreducible structures

- **C7 — irreducible-semantic:** anatomy and clinical biology mixed with clothing/body-surface terms.
- **C10 — irreducible-semantic:** programming, low-level computing and data-stream systems.
- **C12 — irreducible-semantic:** abstract algebra and mathematical notation.

### Negative formal/name substrate

- C0 — personal names/name-like entities
- C3 — grammar/function words and lexical fragments
- C4 — negative/contrastive incomplete word stems
- C8 — mathematical/code punctuation
- C9 — numeric strings/historical years
- C11 — multilingual suffixes/orthographic fragments

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 409 | Databases/data handling/transactions | parent:P+0 | — | Operational information-system core. |
| + | C1 | 347 | Multilingual/malformed fragments | formal-substrate | — | Form/tokenisation dominates. |
| + | C2 | 346 | Grammar/function words/fragments | formal-substrate | — | Lexical/function organisation. |
| + | C3 | 306 | Task/access/work/information actions | parent:P+0 | — | Operational task/action branch. |
| + | C4 | 306 | Biomedical + physical science | parent:P+2 | — | Biological/physical living-system branch. |
| + | C5 | 278 | Psychology/social/politics/finance | parent:P+1 | — | Psychosocial/institutional organisation. |
| + | C6 | 237 | Cities/countries/nationalities/names | parent:P+1 | — | Territorial/social identity branch. |
| + | C7 | 230 | Discourse/temporal/evaluative language | irreducible-semantic | P+1 | Contextual modifier structure. |
| + | C8 | 168 | Punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C9 | 111 | Acronyms/technical abbreviations | formal-substrate | — | Abbreviation/form organisation. |
| + | C10 | 99 | Food/nutrition/animals | parent:P+2 | — | Organismal/nutritional branch. |
| + | C11 | 85 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C12 | 29 | Calendar time/years/seasons | irreducible-semantic | — | Coherent temporal domain. |
| − | C0 | 472 | Personal names/name-like entities | formal-substrate | — | Name/entity organisation without common semantic role. |
| − | C1 | 464 | Adversity/destruction/distress | parent:P-0 | — | Adverse-state branch. |
| − | C2 | 446 | Analysis/assessment + diagnostics | parent:P-0 | — | Characterisation/diagnostic branch. |
| − | C3 | 332 | Grammar/function words/fragments | formal-substrate | — | Lexical/function organisation. |
| − | C4 | 311 | Negative/contrastive word stems | formal-substrate | — | Morphological form dominates. |
| − | C5 | 291 | Religious/institutional/authority/crime | parent:P-1 | P-0 | Authority/role branch. |
| − | C6 | 228 | Built environment/transport/weapons/violence | parent:P-1 | P-0 | Material/conflict-setting branch. |
| − | C7 | 138 | Anatomy/clinical biology + clothing | irreducible-semantic | P-0 | Mixed but coherent enough to retain separately. |
| − | C8 | 137 | Mathematical/code punctuation | formal-substrate | — | Formatting organisation. |
| − | C9 | 106 | Numeric strings/historical years | formal-substrate | — | Numeric form. |
| − | C10 | 95 | Programming/low-level computing | irreducible-semantic | — | Coherent technical domain. |
| − | C11 | 83 | Multilingual suffixes/fragments | formal-substrate | — | Orthographic/morphological form. |
| − | C12 | 49 | Abstract algebra/math notation | irreducible-semantic | — | Coherent mathematical domain. |

Every State 06 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Operational information and task/work systems | C0, C3 | 715 | 24.2% | 37.8% | High |
| P+1 | Psychosocial, institutional and territorial organisation | C5, C6 | 515 | 17.5% | 27.2% | Moderate |
| P+2 | Biological, physical and organismal living systems | C4, C10 | 405 | 13.7% | 21.4% | Moderate |
| P-0 | Adverse assessment and destructive-state characterisation | C1, C2 | 910 | 28.9% | 53.2% | High |
| P-1 | Institutional authority, conflict and material setting | C5, C6 | 519 | 16.5% | 30.3% | Moderate |

Positive retained parents account for **1,635 nodes**, **55.4% of the positive population** and **86.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,429 nodes**, **45.3% of the negative population** and **83.5% of semantic-eligible negative nodes**.

## Relations among parents

### Positive side

1. **P+0 ↔ P+1 — operational information/work in social-institutional context — High.** C0–C5 has **352 edges**, C3–C5 **273**, C0–C6 **116**, C3–C6 **53**.
2. **P+0 ↔ P+2 — operational information/work and biological/physical systems — High.** C0–C4 has **345 edges**, C3–C4 **193**, C0–C10 **76**, C3–C10 **58**.
3. **P+1 ↔ P+2 — psychosocial/institutional and biomedical/physical context — High.** C4–C5 has **255 edges**, C4–C6 **121**, C5–C10 **65**, C6–C10 **67**.

### Negative side

1. **P-0 ↔ P-1 — adverse assessment in institutional/conflict context — High.** C1–C5 has **314 edges**, C2–C5 **279**, C1–C6 **274**, C2–C6 **226**.
2. **P-0 ↔ C7 — assessment and anatomy/clinical biology — Moderate.** C2–C7 has **187 edges**, mean cosine **0.10304**; C1–C7 is much weaker (**44 edges**), so C7 remains irreducible.
3. **P-1 ↔ C7 — material/conflict setting and embodied anatomy — Moderate.** C6–C7 has **117 edges**, C5–C7 **54**.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The State 06 compact cross-side relations are dominated by near-form matches: punctuation variants, captain/ Captain, numeric 14, mathemat case variants and shining/shine. These do not establish a discriminative parent-level semantic bridge.

## Formal/representational substrate

Positive: **1,057 nodes / 35.8%**  
Negative: **1,441 nodes / 45.7%**

The substrate is primarily grammatical/function morphology, malformed or multilingual fragments, punctuation/formatting, abbreviations, names and numeric strings.

## Minimal state-level architecture

~~~text
STATE 06 — BLOCK 5 OUTPUT

POSITIVE
├─ P+0 Operational information + task/work systems
├─ P+1 Psychosocial/institutional + territorial organisation
├─ P+2 Biological/physical + organismal living systems
├─ discourse/temporal/evaluative context          [irreducible]
└─ calendar/time                                  [irreducible]

NEGATIVE
├─ P-0 Adverse assessment + destructive-state characterisation
├─ P-1 Institutional authority/conflict + material setting
├─ anatomy/clinical biology                       [irreducible]
├─ programming/low-level computing                [irreducible]
└─ abstract algebra                               [irreducible]
~~~

## Alternative reconstruction

The strongest alternatives are:

1. **Positive:** leave C10 irreducible rather than retaining P+2. This would be favoured if the C4–C10 relation is judged too weak to outweigh C4's substantial physical-science content.
2. **Positive:** leave C6 as name/geographic organisation rather than retaining P+1. This would be favoured if territorial identity is treated as entity structure rather than part of psychosocial/institutional organisation.
3. **Negative:** absorb C5 into P-0 under a broader adverse institutional assessment/control parent. This would be favoured by its strong C1/C2 relations, but loses the distinct authority/role structure.
4. **Negative:** leave C5 and C6 separate rather than retaining P-1. This would be favoured if institutional authority and material conflict setting are treated as adjacent rather than jointly generated.

The preferred reconstruction retains P+1/P+2 because each reduces complexity without requiring a generic parent label and each has a clear exclusion boundary.

## Uncertainty record

- P+1 and P+2 are Moderate confidence.
- Positive C4 is internally mixed across biomedical and physical-science terms.
- Positive C5 is internally mixed across psychosocial, political, financial and sport material.
- Negative C5 and C6 are heterogeneous but share a defensible authority/conflict-setting relation.
- Full token-level compressed membership was not inspected.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **26 / 26**
- Positive node accounting: **2,951 / 2,951**
- Negative node accounting: **3,152 / 3,152**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 06 community inspected at underlying R008 community-record level: **yes**
- All State 06 within-side community relations inspected: **yes**
- State 06 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Existing R010 State 06 reconstruction inspected before hypothesis freeze: **no**
- State 07 semantic content exposed during this rerun: **no**
- State 07 evidence used in State 06 inference: **no**
- Strict state-isolation source exposure breach during this rerun: **no**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This clean State 06 replacement is frozen as an independent hypothesis. It was constructed only from State 06 semantic evidence and does not infer continuity with any other state.

No persistence, emergence, disappearance, split, merge, polarity change, optimal-layer, SDA-3 or curvature inference is made here.
