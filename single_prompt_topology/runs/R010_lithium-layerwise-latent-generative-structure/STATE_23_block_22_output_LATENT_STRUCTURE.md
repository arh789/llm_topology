# R010 State 23 — Block 22 output latent structure

## State identity

- R010 state index: `23`
- R008/R009 state: `block_22_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 11 negative-tail = 24**
- R008 population: **3,261 positive-head + 3,275 negative-tail = 6,536 nodes**
- Status: **clean Phase-A rerun complete**

This file replaces the earlier State 23 reconstruction. The replacement was constructed independently from State 23 R008/R009 evidence only. The previous R010 State 23 reconstruction was not inspected before the replacement hypothesis was frozen.

No State 24 semantic content was exposed during this rerun.

## Evidence inventory

Evidence used:

1. `R009/STATE_23_block_22_output.md`;
2. all 24 State 23 rows in R008 `community_nodes.csv`;
3. the complete State 23 within-side relation set in R008 `community_edges.csv`.

The State 23 layer packet was deliberately **not used** because a safely bounded State 23-only packet extraction could not be completed without risking spill into State 24. The compressed token-level membership artifact was also not decoded through the GitHub text connector.

Accordingly, no cross-side bridge is retained in this rerun.

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

**Evidence.** C1 contains exploration, characterisation, negotiation, modelling, recording and developmental/process activity. C2 contains measurement, interaction, quantification, computation, interventions, comparisons and organisational analysis. Their direct relation is the strongest positive semantic pair: **388 token edges**, mean cosine **0.10448**.

The minimum common generator is developmental system analysis: evolving situations are explored and characterised while being measured, modelled and compared through quantitative and organisational processes.

**Secondary links:** C5, C8 and C10. C1–C5 has **277 edges**, C2–C5 **271**; C1–C8 **242**, C2–C8 **126**; C1–C10 **162**, C2–C10 **155**.

**Exclusion boundary.** C5 is software/platform/interface activity, C8 is anticipation/evaluative description and C10 is enterprise/research/media activity. All are adjacent to the analytical process but remain discriminable domains.

### P+1 — Embodied wellbeing and biomedical health

- **Primary children:** C6, C7
- **Primary nodes:** 495
- **Side-relative coverage:** 15.2%
- **Semantic-eligible coverage:** 27.2%
- **Confidence:** Moderate / High

**Evidence.** C6 contains food, leisure, shopping, affect, discomfort, compassion and recreational activity. C7 contains biomedical, pharmacological, infant-health and healthcare terminology. Their direct relation has **215 token edges**, mean cosine **0.10124**.

The common generator is embodied wellbeing spanning lived affective/everyday activity and biomedical/health states.

**Secondary links:** C1 and C2. C1–C6 **249**, C2–C6 **185**; C1–C7 **139**, C2–C7 **229**.

**Exclusion boundary.** C6 is lived/affective/recreational while C7 is clinical/biomedical. The parent is not broadened to generic human activity.

### Positive irreducible structures

- **C5 — irreducible-semantic:** navigation, software/platform management and layout concepts; secondary to P+0.
- **C8 — irreducible-semantic:** anticipation/emergence with temporal/evaluative descriptors; secondary to P+0.
- **C10 — irreducible-semantic:** entrepreneurship, research, filmmaking, photography and business/media activity; secondary to P+0 and C5.
- **C12 — irreducible-semantic:** acknowledgement, greeting and thanks language.

### Positive formal/name substrate

- C0 — personal names, cities and geographic entities
- C3 — mathematical/code punctuation and symbolic formatting
- C4 — grammar/function words and lexical fragments
- C9 — incomplete emergence/freshness/reappearance stem families
- C11 — numeric strings/coded values

## Negative-side reconstruction

### P-0 — Regulatory intervention, administrative characterisation and adverse judgement

- **Primary children:** C1, C4, C7
- **Primary nodes:** 1,013
- **Side-relative coverage:** 30.9%
- **Semantic-eligible coverage:** 50.1%
- **Confidence:** High

**Evidence.** C1 contains encouragement, prohibition, removal, legal constraint and adverse evaluation. C4 contains administrative characterisation, configuration, regulation and constitutional concepts. C7 contains negative/intense evaluation, alarm and detriment.

The three-way structure is strongly supported:

- C1–C4: **512 token edges**, mean cosine **0.10266**
- C1–C7: **407**, mean cosine **0.10244**
- C4–C7: **134**, mean cosine **0.09258**

The minimum common generator is organised state control: conditions are administratively characterised, regulated or constrained, acted upon through encouragement/prohibition/removal, and judged for adverse or extreme qualities.

**Secondary links:** C3 and P-1. C1–C3 **183**, C4–C3 **232**, C7–C3 **145** link pathology to the control field. C1–C6 **276**, C4–C6 **267**, C7–C6 **187** connect authority/institutional identity.

**Exclusion boundary.** C3 is a biomedical pathology ontology; C6 is institutional/authority identity; C5 is physical/material environment. These remain distinct from the control/judgement mechanism.

### P-1 — Institutional/territorial authority and political order

- **Primary children:** C6, C10
- **Primary nodes:** 388
- **Side-relative coverage:** 11.8%
- **Semantic-eligible coverage:** 19.2%
- **Confidence:** Moderate / High

**Evidence.** C6 contains administrators, beneficiaries, monarchy, religion and political identity. C10 contains geographic entities and regions. Their direct relation has **129 token edges**, mean cosine **0.10270**.

The minimum common generator is institutional and political authority situated within territorial identity.

**Secondary link:** C5. C5–C6 has **250 edges** and C5–C10 **66**, placing material/built settings around authority and territory.

**Exclusion boundary.** C6 is authority/role centred and C10 territorial. C5 is a physical/material environment rather than authority itself.

### Negative irreducible structures

- **C3 — irreducible-semantic:** cardiovascular/cytokine biomedical pathology; secondary to P-0.
- **C5 — irreducible-semantic:** vehicles, roads, built environment and material objects; secondary to P-1 and P-0.

### Negative formal/name substrate

- C0 — personal names/name-like entities with fragments
- C2 — grammar/function words and multilingual lexical fragments
- C8 — multilingual/encoding and punctuation/tokenisation residue
- C9 — numeric strings/historical years

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 523 | Names/cities/geography | formal-substrate | — | Entity organisation without a common semantic role. |
| + | C1 | 326 | Exploration/development/process | parent:P+0 | — | Developmental/process branch. |
| + | C2 | 305 | Measurement/quantification/analysis | parent:P+0 | — | Quantitative/organisational branch. |
| + | C3 | 295 | Mathematical/code punctuation | formal-substrate | — | Formatting organisation. |
| + | C4 | 283 | Grammar/function words/fragments | formal-substrate | — | Lexical/function organisation. |
| + | C5 | 269 | Navigation/software/platform/layout | irreducible-semantic | P+0 | Technical/interface domain adjacent to analysis. |
| + | C6 | 249 | Food/leisure/affect/recreation | parent:P+1 | — | Lived wellbeing branch. |
| + | C7 | 246 | Biomedical/pharma/infant health | parent:P+1 | — | Clinical/health branch. |
| + | C8 | 232 | Anticipation/emergence/evaluation | irreducible-semantic | P+0 | Prospective/evaluative descriptor domain. |
| + | C9 | 201 | Emergence/freshness/reappearance stems | formal-substrate | — | Morphological form dominates. |
| + | C10 | 182 | Entrepreneurship/research/media | irreducible-semantic | P+0 | Professional/media domain. |
| + | C11 | 139 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| + | C12 | 11 | Acknowledgement/greetings/thanks | irreducible-semantic | — | Coherent discourse-act domain. |
| − | C0 | 551 | Names/name-like fragments | formal-substrate | — | Entity/form organisation dominates. |
| − | C1 | 476 | Encouragement/prohibition/removal/constraint | parent:P-0 | — | Intervention/control branch. |
| − | C2 | 429 | Grammar/function/multilingual fragments | formal-substrate | — | Lexical/form organisation. |
| − | C3 | 315 | Cardiovascular/cytokine pathology | irreducible-semantic | P-0 | Distinct medical ontology. |
| − | C4 | 315 | Administrative/configuration/regulatory | parent:P-0 | — | Characterisation/regulation branch. |
| − | C5 | 304 | Vehicles/roads/built/material | irreducible-semantic | P-0, P-1 | Physical/material setting. |
| − | C6 | 289 | Administration/monarchy/religion/politics | parent:P-1 | P-0 | Institutional/authority branch. |
| − | C7 | 222 | Negative/intense evaluation/detriment | parent:P-0 | — | Adverse-judgement branch. |
| − | C8 | 161 | Encoding/punctuation/tokenisation residue | formal-substrate | — | Formatting/tokeniser organisation. |
| − | C9 | 114 | Numeric strings/historical years | formal-substrate | — | Numeric form. |
| − | C10 | 99 | Geographic entities/regions | parent:P-1 | — | Territorial branch. |

Every State 23 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Developmental process and quantitative-organisational analysis | C1, C2 | 631 | 19.3% | 34.7% | High |
| P+1 | Embodied wellbeing and biomedical health | C6, C7 | 495 | 15.2% | 27.2% | Moderate / High |
| P-0 | Regulatory intervention, administrative characterisation and adverse judgement | C1, C4, C7 | 1,013 | 30.9% | 50.1% | High |
| P-1 | Institutional/territorial authority and political order | C6, C10 | 388 | 11.8% | 19.2% | Moderate / High |

Positive retained parents account for **1,126 nodes**, **34.5% of the positive population** and **61.9% of semantic-eligible positive nodes**.

Negative retained parents account for **1,401 nodes**, **42.8% of the negative population** and **69.4% of semantic-eligible negative nodes**.

## Relations among parents

### Positive side

1. **P+0 ↔ P+1 — developmental analysis and embodied health/wellbeing — High.** C1–C6 **249**, C2–C6 **185**, C1–C7 **139**, C2–C7 **229**.
2. **P+0 ↔ C5 — analytical process and software/interface systems — High.** C1–C5 **277**, C2–C5 **271**.
3. **P+0 ↔ C8 — developmental process and anticipation/evaluation — High.** C1–C8 **242**, C2–C8 **126**.
4. **P+0 ↔ C10 — analysis and research/media/enterprise activity — High.** C1–C10 **162**, C2–C10 **155**.

### Negative side

1. **P-0 ↔ P-1 — regulatory control in institutional/territorial context — High.** C1–C6 **276**, C4–C6 **267**, C7–C6 **187**.
2. **P-0 ↔ C3 — regulation/judgement and clinical pathology — High.** C1–C3 **183**, C4–C3 **232**, C7–C3 **145**.
3. **P-0 ↔ C5 — regulation/judgement and material setting — High.** C1–C5 **187**, C4–C5 **251**, C7–C5 **185**.
4. **P-1 ↔ C5 — authority/territory and physical environment — High.** C5–C6 **250**, C5–C10 **66**.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The State 23 packet/cross-side compact evidence was not used in this clean rerun because a safely bounded State 23-only packet extraction was not available without risking State 24 exposure. The protocol permits absence of a bridge; no bridge is inferred from within-side evidence alone.

## Formal/representational substrate

Positive: **1,441 nodes / 44.2%**  
Negative: **1,255 nodes / 38.3%**

The substrate is primarily names/entities, grammar/function morphology, incomplete lexical stems, punctuation/tokeniser organisation and numeric strings.

## Minimal state-level architecture

~~~text
STATE 23 — BLOCK 22 OUTPUT

POSITIVE
├─ P+0 Developmental process + quantitative-organisational analysis
├─ P+1 Embodied wellbeing + biomedical health
├─ software/platform/interface systems             [irreducible]
├─ anticipation/emergence/evaluative descriptors  [irreducible]
├─ research/media/enterprise activity              [irreducible]
└─ acknowledgement/greeting/thanks                 [irreducible]

NEGATIVE
├─ P-0 Regulatory intervention
│      + administrative characterisation
│      + adverse judgement
├─ P-1 Institutional/territorial authority
│      + political order
├─ cardiovascular/cytokine pathology               [irreducible]
└─ vehicles/roads/built/material objects            [irreducible]
~~~

## Alternative reconstruction

The strongest alternatives are:

1. **Positive:** create a mediated professional/technical parent from C5+C10. This would be favoured if their **158-edge** relation is judged sufficient to override their distinct software-interface versus enterprise/media organisation.
2. **Positive:** leave C6 and C7 separate rather than retaining P+1. This would be favoured if lived wellbeing and clinical health are judged adjacent rather than jointly generated.
3. **Negative:** restrict P-0 to C1+C4 and leave C7 irreducible. This would be favoured if adverse judgement is treated as a modifier rather than a constitutive control function.
4. **Negative:** leave C6 and C10 separate rather than retaining P-1. This would be favoured if C6's mixed administrative/monarchic/religious content is judged too heterogeneous for a territorial-authority parent.

The preferred reconstruction retains P+1 and P-1 because each compresses two strongly related semantic communities while preserving explicit exclusion boundaries.

## Uncertainty record

- Positive P+1 is Moderate/High because C6 spans several lived-experience domains.
- Positive C5/C10 could support an alternative professional/technical parent, but that relation is weaker than the retained parents.
- Negative P-1 is Moderate/High because C6 is internally mixed across administrative, monarchic, religious and political identity.
- Negative C5 is broadly material/physical and connects to both retained negative parents.
- Full token-level compressed membership was not inspected.
- State 23 compact cross-side packet evidence was deliberately not inspected during this rerun.

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
- State 23 compact cross-side evidence inspected: **no — intentionally omitted to preserve isolation**
- Full token-membership inspection falsely claimed: **no**
- Existing R010 State 23 reconstruction inspected before hypothesis freeze: **no**
- State 24 semantic content exposed during this rerun: **no**
- State 24 evidence used in State 23 inference: **no**
- Strict state-isolation source exposure breach during this rerun: **no**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This clean State 23 replacement is frozen as an independent hypothesis. It was constructed only from State 23 semantic evidence and does not infer continuity with any other state.

No persistence, emergence, disappearance, split, merge, polarity change, optimal-layer, SDA-3 or curvature inference is made here.
