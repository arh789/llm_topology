# R010 State 02 — Block 1 output latent structure

## State identity

- R010 state index: `02`
- R008/R009 state: `block_01_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **14 positive-head + 13 negative-tail = 27**
- R008 population: **3,063 positive-head + 2,816 negative-tail = 5,879 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 02 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

For every State 02 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_02_block_01_output.md`;
2. State 02 entries in `R009_SUMMARY.html`;
3. all 27 State 02 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. all State 02 within-side relations in R008 `community_edges.csv`;
5. the State 02 R008 layer packet, including the strongest intercommunity
   relations and compact cross-side evidence.

The R009 identity labels were treated as hypotheses. The underlying R008
community records and graph relations controlled the final reconstruction.

No compressed token-level escalation was required for a retained High-confidence
parent. Mixed communities whose compact R008 evidence remained genuinely
heterogeneous were retained as mixed or secondary structures rather than forced
into a parent.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 390 | 1,653 / 1,986 | 13.57 | +0.03092 | Development, activation, task/progress and evaluation dominate: `development`, `activates`, `initiating`, `established`, `recognizing`, `Quantitative`, with `interesting`, `enjoyable`, `satisfactory`, `unsatisfactory`; extremes include `solved`, `accessing`, `recognized`, `Accept`. |
| C1 | 383 | 1,522 / 2,042 | 13.28 | +0.03133 | Biomedical/endocrine/physiological organisation dominates: `angiotensin`, `psychological`, `adolescents`, `glucocortic`, `hypothal`, `pituitary`, `infertility`, `menstrual`; biological outliers remain. |
| C2 | 382 | 2,022 / 1,865 | 15.47 | +0.03129 | Function words and lexical fragments dominate: `is`, `was`, `have`, `more`, `work`, `like`, `down`, with short fragments. Primarily formal linguistic structure. |
| C3 | 379 | 1,593 / 1,732 | 12.98 | +0.03150 | Databases/software/computing vocabulary dominates: `mysql`, `DB`, `MySQL`, `CS`, `SQL`, `Database`, `sqlite`, `txt`; extremes include `NAS`, `CSS`, `nginx`. |
| C4 | 280 | 1,208 / 1,373 | 13.53 | +0.03107 | Countries, nationalities and cities are coherent: `Nigerian`, `Indonesian`, `California`, `Ethiop`, `Sacramento`, `Chinese`, `Canadian`, `Philippines`, `Egyptian`. |
| C5 | 254 | 1,486 / 534 | 13.80 | +0.03217 | Strongly bounded punctuation/bracket/code-formatting cluster; 186 of 254 tokens are punctuation/symbols. |
| C6 | 208 | 796 / 1,309 | 13.95 | +0.03160 | Political/civic/administrative vocabulary dominates: `politically`, `political`, `bureaucracy`, `administrative`, `democratic`, `parliamentary`, with psychosocial, athlete and sport material as a real secondary component. |
| C7 | 206 | 860 / 1,176 | 14.06 | +0.03045 | Contextual modifiers dominate: `Subsequently`, `Eventually`, `professionally`, `emotional`, `Therefore`, `emotionally`, `culturally`, `inevitably`, `environmentally`, `retrospectively`. |
| C8 | 146 | 478 / 785 | 11.92 | +0.03191 | Replacement characters, multilingual fragments and encoding residues dominate. |
| C9 | 118 | 352 / 793 | 12.69 | Genuine mixed structure: `forms`, `form`, `densities`, `complexes`, `Pressure`, `Height` coexist with `Group`, `Login`, `Hash`, `Views`, `Entry`, `Role`, plus `injection`, `hatch`, `cycle`. |
| C10 | 96 | 587 / 174 | 14.04 | +0.02964 | Strong numeric cluster. |
| C11 | 91 | 306 / 599 | 13.31 | +0.03058 | Mathematical physics/computational organisation: `renormalization`, `stochastic`, `Lorentz`, `logarithmic`, `computational`, `dimensional`, `simulations`, `dynamical`, `algebraic`. |
| C12 | 71 | 271 / 455 | 14.04 | +0.03126 | Food/crops/gardening/vegetation cluster: `cabbage`, `gardening`, `rice`, `chocolate`, `vegetation`, `forest`, `bread`; extremes include `curry`, `flowering`, `coconut`. |
| C13 | 59 | 294 / 235 | 13.95 | +0.02962 | Calendar/year/weekday/season structure: `September`, `1988`, `Sunday`, `1992`, `Monday`, `weekend`, `Season`, with `2019`, `months`, `Week`, `August`, `spring`. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 426 | 1,937 / 1,873 | 13.49 | -0.03168 | Personal names and geographic/name fragments dominate: `Luke`, `Nick`, `Hicks`, `Jeff`, `Murphy`, `Lucas`, `Clay`, `McConnell`; no single social domain links them. |
| C1 | 379 | 1,626 / 2,069 | 14.04 | -0.03190 | Interpretation, prohibition, law and institutional judgement dominate: `determination`, `prohibiting`, `interpretation`, `prohibited`, `unconstitutional`, `prohibition`, `unacceptable`, `discriminatory`; extremes include `Laws`, `approved`, `authority`. |
| C2 | 292 | 1,320 / 1,608 | 14.55 | -0.03154 | Common word pieces, suffixes and grammatical fragments dominate. |
| C3 | 275 | 1,133 / 1,589 | 14.02 | -0.03243 | Violence/crime/tragedy is exceptionally coherent: `murdered`, `massacre`, `murders`, `thief`, `killings`, `killing`, `tragedy`, `madness`, `terrifying`. |
| C4 | 232 | 958 / 1,233 | 13.57 | -0.03189 | Built environment, weapons, clothing and objects coexist: `hallway`, `staircase`, `guns`, `sidewalk`, `Transportation`, `jacket`, `rifles`, `cliffs`, `brewery`, `sword`. It is materially mixed. |
| C5 | 218 | 895 / 1,313 | 14.23 | -0.03266 | Occupations, authority figures and fictional/social roles: `producer`, `physician`, `technician`, `Archbishop`, `Duchess`, `Chairman`, `officer`, with `goddess`, `monsters`, `villain`, `warriors`. |
| C6 | 179 | 639 / 1,151 | 13.57 | -0.03176 | Scientific transformation/optimisation/analysis processes: `inhibition`, `Experiments`, `enhancement`, `stabilization`, `initialization`, `detectors`, `minimization`, `Analyses`, `increase`, `decrease`. |
| C7 | 169 | 512 / 1,121 | 12.69 | -0.03242 | Incomplete stems and prefixes dominate. |
| C8 | 165 | 540 / 853 | 11.72 | -0.03068 | Multilingual, encoding and orthographic fragments dominate. |
| C9 | 162 | 599 / 963 | 13.34 | -0.03104 | Biomedical diagnostics/pathology is coherent: `pathophysiology`, `echocardiography`, `epidemiology`, `phenotypes`, `angiography`, `biomarkers`, `erythrocytes`, `anesthesia`, `pathogen`, `microscopy`. |
| C10 | 113 | 326 / 824 | 13.06 | -0.03135 | Technology/digital-media/workspace vocabulary: `technologies`, `Electronics`, `video`, `Generator`, `annotations`, `workspace`, `Photography`, `gallery`; extremes include `plugins`, `sdk`, `Monitor`, `transducer`, `Decoder`, `Devices`. |
| C11 | 106 | 556 / 248 | 12.83 | -0.03079 | Mathematical/code punctuation dominates; 85 of 106 tokens are punctuation/symbols. |
| C12 | 100 | 595 / 235 | 14.25 | -0.03050 | Strong numeric cluster. |

## Population accounting

### Positive head

Total nodes: **3,063**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 2,008 | 65.6% |
| Formal/name substrate | 878 | 28.7% |
| Irreducible semantic | 59 | 1.9% |
| Mixed unresolved | 118 | 3.9% |
| Unclear | 0 | 0.0% |
| **Total** | **3,063** | **100.0%** |

Semantic-eligible denominator, excluding formal/name substrate and unclear:
**2,185 nodes**.

### Negative tail

Total nodes: **2,816**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 995 | 35.3% |
| Formal/name substrate | 1,258 | 44.7% |
| Irreducible semantic | 331 | 11.8% |
| Mixed unresolved | 232 | 8.2% |
| Unclear | 0 | 0.0% |
| **Total** | **2,816** | **100.0%** |

Semantic-eligible denominator: **1,558 nodes**.

## Positive-side reconstruction

### P+0 — Action/progress appraisal and contextual modulation

- **Primary children:** C0, C7
- **Primary nodes:** 596
- **Side-relative coverage:** 19.5%
- **Semantic-eligible coverage:** 27.3%
- **Confidence:** High

**Evidence.** C0 contains development, activation, progress/task and evaluative
actions. C7 contains temporal, affective, cultural and contextual modifiers.
Their relation is one of the strongest semantic links in the state:
**336 token edges**, mean cosine **0.10577**. Together they describe actions or
states being advanced, evaluated and contextually qualified.

**Exclusion boundary.** C13 is calendar/time organisation, not contextual
modification. C6 is a political/civic domain rather than a general
action/appraisal structure.

**Alternative.** Keep C0 and C7 separate. This becomes preferable only if C0's
evaluation vocabulary proves peripheral relative to its development/action
content.

### P+1 — Computational and mathematical-scientific systems

- **Primary children:** C3, C11
- **Primary nodes:** 470
- **Side-relative coverage:** 15.3%
- **Semantic-eligible coverage:** 21.5%
- **Confidence:** High

**Evidence.** C3 supplies database/software/computing infrastructure; C11
supplies computational mathematical physics, simulations and dynamical systems.
The direct C3–C11 relation contains **74 edges**, mean cosine **0.08949**.
The common higher-order structure is formalised computation and technical
system representation.

**Secondary link:** C9. C3–C9 has **123 edges** and C9 contains forms,
densities, pressure, interface and structural-measurement terms, but its
heterogeneity prevents primary absorption.

**Exclusion boundary.** C1 is biomedical rather than computational despite a
strong C1–C3 graph relation. C9 remains mixed rather than being redefined to fit
this parent.

**Alternative.** Absorb C9 into P+1 as a measurement/interface child. This
would improve compression but would hide its unrelated injection, hatch,
cycle and mixed form/interface content.

### P+2 — Geopolitical and civic/social organisation

- **Primary children:** C4, C6
- **Primary nodes:** 488
- **Side-relative coverage:** 15.9%
- **Semantic-eligible coverage:** 22.3%
- **Confidence:** High

**Evidence.** C4 contains countries, nationalities and cities; C6 contains
politics, administration, civic institutions and related social descriptors.
Their direct graph relation contains **193 token edges**, mean cosine
**0.09301**.

**Exclusion boundary.** Sport/athlete material in C6 is secondary and does not
justify a broader "all social activity" parent. C13's calendar structure is not
geopolitical organisation.

**Alternative.** Treat C4 as name substrate and leave C6 irreducible. This is
not preferred because C4's names form a coherent geographic/nationality domain
and connect directly to the civic/political structure.

### P+3 — Biological, health and cultivated-living systems

- **Primary children:** C1, C12
- **Primary nodes:** 454
- **Side-relative coverage:** 14.8%
- **Semantic-eligible coverage:** 20.8%
- **Confidence:** Moderate

**Evidence.** C1 supplies biomedical/endocrine/physiological life-system
vocabulary. C12 supplies crops, vegetation, food and gardening. C1–C12 has
**99 token edges**, mean cosine **0.09119**. The common parent is biological and
cultivated living systems rather than a narrower medical topic.

**Exclusion boundary.** C6 contains psychosocial and athlete terms but is
primarily civic/political. C9 has isolated biological terms but is too mixed.

**Alternative.** Leave C1 and C12 as separate irreducible biomedical and
agricultural structures. This alternative remains serious because their common
parent is broad and the two communities retain distinct domains.

### Positive irreducible and unresolved structures

- **C13 — irreducible-semantic:** calendar, weekdays, years and seasons.
- **C9 — mixed-unresolved:** structural/measurement, interface and unrelated
  process terms coexist; secondary link to P+1.
- **C2, C5, C8, C10 — formal-substrate:** grammar/fragments, formatting,
  encoding/multilingual residue and numerics.

## Negative-side reconstruction

### P-0 — Prohibition, transgression and harmful social action

- **Primary children:** C1, C3
- **Primary nodes:** 654
- **Side-relative coverage:** 23.2%
- **Semantic-eligible coverage:** 42.0%
- **Confidence:** High

**Evidence.** C1 centres on prohibition, law, institutional judgement,
unacceptability and authority. C3 centres on murder, crime, killing, tragedy and
threat. Their direct intercommunity relation is the strongest semantic relation
on the negative side: **463 token edges**, mean cosine **0.10096**. The parent
captures prohibited or institutionally judged harmful social action.

**Secondary links:**
- **C5:** roles such as officer, Chairman, Archbishop, warriors and villain
  connect actors/authority to the parent; C3–C5 has **194 edges**, C1–C5
  **164**.
- **C4:** weapons and physical settings provide an event/material environment;
  C3–C4 has **183 edges**, C1–C4 **145**.

**Exclusion boundary.** C4 is too broad physically to become a primary harm
child, and C5 contains many occupational/fictional roles unrelated to
transgression. C6 is scientific transformation rather than social prohibition.

**Alternative.** Expand P-0 to include C5 as a social-role/authority child.
This is rejected because producer, physician, technician, goddess, monsters and
creative figures prevent a clean transgression/authority interpretation.

### P-1 — Scientific/biomedical analysis and controlled transformation

- **Primary children:** C6, C9
- **Primary nodes:** 341
- **Side-relative coverage:** 12.1%
- **Semantic-eligible coverage:** 21.9%
- **Confidence:** High

**Evidence.** C6 contains experiments, inhibition, enhancement,
stabilisation, minimisation, analysis, increase/decrease and detector-related
scientific processes. C9 contains diagnostics, pathology, epidemiology,
biomarkers, angiography and microscopy. C6–C9 has **123 token edges**, mean
cosine **0.09542**. The higher-order structure is scientific analysis of
biological systems and controlled state change.

**Secondary links:**
- **C10:** technologies, electronics, transducers, decoders and devices are
  technical infrastructure adjacent to scientific analysis. C6–C10 has
  **74 edges** and C9–C10 **73**.
- **C1:** C1–C6 has **275 edges**, reflecting transformation/constraint
  vocabulary shared across normative and scientific contexts, but C1's
  social/legal semantics prevent primary absorption.

**Exclusion boundary.** C10 is too broad across media, workspace and creative
technology to become a primary scientific child. C1 concerns institutional
prohibition/judgement rather than scientific mechanism.

**Alternative.** Pair C1 with C6 under a broader "constraint and
transformation" parent and leave C9 irreducible. This has stronger raw edge
count but sacrifices the distinction between normative constraint and
scientific/biological transformation.

### Negative irreducible and unresolved structures

- **C5 — irreducible-semantic:** occupations, titles, authority and
  fictional/social roles; secondary link to P-0.
- **C10 — irreducible-semantic:** technology/digital-media/workspace systems;
  secondary link to P-1.
- **C4 — mixed-unresolved:** built environment, weapons, clothing and physical
  objects; secondary link to P-0.
- **C0, C2, C7, C8, C11, C12 — formal/name substrate:** names, morphology,
  multilingual/encoding residue, punctuation and numerics.

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 390 | Development/activation/evaluation actions | parent:P+0 | — | Action/progress plus appraisal structure. |
| + | C1 | 383 | Biomedical/endocrine/physiological | parent:P+3 | — | Biological/health-system structure. |
| + | C2 | 382 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 379 | Databases/software/computing | parent:P+1 | — | Computational-system infrastructure. |
| + | C4 | 280 | Countries/nationalities/cities | parent:P+2 | — | Coherent geographic/nationality domain. |
| + | C5 | 254 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser structure. |
| + | C6 | 208 | Politics/admin/civic + social/sport | parent:P+2 | — | Civic/social institutional organisation dominates. |
| + | C7 | 206 | Contextual/adverbial/affective modifiers | parent:P+0 | — | Contextual modulation of actions/states. |
| + | C8 | 146 | Multilingual/encoding residue | formal-substrate | — | Orthographic/tokeniser form. |
| + | C9 | 118 | Form/measurement + interface mixed | mixed-unresolved | P+1 | Technical/measurement affinity, but heterogeneous membership. |
| + | C10 | 96 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C11 | 91 | Mathematical physics/computation | parent:P+1 | — | Formalised computational/scientific system. |
| + | C12 | 71 | Food/crops/vegetation/gardening | parent:P+3 | — | Cultivated/living-system organisation. |
| + | C13 | 59 | Calendar/years/weekdays/seasons | irreducible-semantic | — | Coherent time/calendar structure without a sibling parent. |
| − | C0 | 426 | Personal names/geographic entities | formal-substrate | — | Name-form organisation without one social domain. |
| − | C1 | 379 | Interpretation/prohibition/law/judgement | parent:P-0 | — | Normative/institutional constraint. |
| − | C2 | 292 | Word pieces/suffixes/fragments | formal-substrate | — | Morphological form. |
| − | C3 | 275 | Violence/crime/tragedy | parent:P-0 | — | Harmful/transgressive social action. |
| − | C4 | 232 | Built environment/weapons/clothing/objects | mixed-unresolved | P-0 | Physical threat/event setting is present but not exclusive. |
| − | C5 | 218 | Occupations/titles/fictional roles | irreducible-semantic | P-0 | Actor/authority relation, but broad role heterogeneity. |
| − | C6 | 179 | Scientific transformation/optimisation | parent:P-1 | — | Controlled scientific transformation and analysis. |
| − | C7 | 169 | Incomplete stems/prefixes | formal-substrate | — | Morphological form. |
| − | C8 | 165 | Multilingual/encoding fragments | formal-substrate | — | Orthographic/tokeniser organisation. |
| − | C9 | 162 | Biomedical diagnostics/pathology | parent:P-1 | — | Clinical/scientific analysis. |
| − | C10 | 113 | Technology/digital media/tools | irreducible-semantic | P-1 | Technical infrastructure adjacent to scientific analysis. |
| − | C11 | 106 | Mathematical/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 100 | Numeric strings | formal-substrate | — | Numeric form. |

Every State 02 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Action/progress appraisal and contextual modulation | C0, C7 | 596 | 19.5% | 27.3% | High |
| P+1 | Computational and mathematical-scientific systems | C3, C11 | 470 | 15.3% | 21.5% | High |
| P+2 | Geopolitical and civic/social organisation | C4, C6 | 488 | 15.9% | 22.3% | High |
| P+3 | Biological, health and cultivated-living systems | C1, C12 | 454 | 14.8% | 20.8% | Moderate |
| P-0 | Prohibition, transgression and harmful social action | C1, C3 | 654 | 23.2% | 42.0% | High |
| P-1 | Scientific/biomedical analysis and controlled transformation | C6, C9 | 341 | 12.1% | 21.9% | High |

Positive retained parents jointly account for **2,008 nodes**, **65.6% of the
positive side** and **91.9% of semantic-eligible positive nodes**.

Negative retained parents jointly account for **995 nodes**, **35.3% of the
negative side** and **63.9% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+2 — social/contextual action relation — Moderate.**
   C0–C6 has **251 edges**, and C0–C4 **75**; C7 also relates to C6. The
   action/appraisal structure is frequently instantiated in social/political
   contexts without collapsing into that domain.

2. **P+1 ↔ P+3 — scientific/computational relation — Moderate to High.**
   C1–C3 has **351 edges** and C1–C11 **139**. Biological/health content is
   strongly coupled to computational/scientific representation, but the
   domains remain discriminable.

3. **P+0 ↔ P+1 — task/analysis relation — Moderate.**
   C0–C3 has **148 edges**, C0–C11 **122**, and C7–C11 **59**. Development,
   evaluation and contextual modulation overlap technical/scientific work.

4. **C9 is a mixed technical bridge, not a retained parent.**
   It links especially to P+1 through C3–C9 (**123 edges**) but remains too
   heterogeneous for primary absorption.

### Negative-side relations

1. **P-0 ↔ P-1 — constraint/transformation analogy — Moderate.**
   C1–C6 has **275 edges**, one of the strongest negative-side relations.
   Normative/social constraint and scientific transformation share a language
   of state limitation/change while remaining semantically distinct.

2. **P-0 ↔ C5/C4 — actor and setting relation — Moderate.**
   Roles/authority and weapons/physical environments plausibly supply actors
   and settings for harmful/transgressive actions, but their broader content
   blocks primary inclusion.

3. **P-1 ↔ C10 — technical-infrastructure relation — Moderate.**
   Technology/tools are adjacent to scientific analysis but extend into media
   and workspace systems.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact R008 cross-side evidence for State 02 is dominated by near-lexical
or morphological correspondences such as geographic-name variants, formatting
variants and closely related word forms. It does not independently establish a
semantic bridge between the retained positive and negative parents.

Two semantic correspondences remain noteworthy but unpromoted:

- positive P+3 and negative P-1 both contain biological/biomedical structure;
- positive P+1 and negative C10 both contain computational/technical structure.

Neither is promoted to a bridge without stronger cross-side community-level
evidence.

## Formal/representational substrate

### Positive — 878 nodes / 28.7%

- grammar/function words and fragments;
- punctuation/formatting;
- multilingual/encoding residue;
- numeric strings.

Geographic C4 is **not** counted as formal substrate because its underlying
membership forms a coherent geographic/nationality domain and participates in
P+2.

### Negative — 1,258 nodes / 44.7%

- personal names;
- word pieces/suffixes;
- incomplete stems;
- multilingual/encoding fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 02 — BLOCK 1 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ACTION / PROGRESS APPRAISAL & CONTEXTUAL MODULATION
|   +-- C0 development/activation/evaluation actions
|   `-- C7 temporal/affective/contextual modifiers
|
+-- P+1 COMPUTATIONAL & MATHEMATICAL-SCIENTIFIC SYSTEMS
|   +-- C3 databases/software/computing
|   `-- C11 mathematical physics/computation
|       \
|        -- C9 form/measurement/interface           [secondary; mixed]
|
+-- P+2 GEOPOLITICAL & CIVIC/SOCIAL ORGANISATION
|   +-- C4 countries/nationalities/cities
|   `-- C6 politics/administration/civic structures
|
+-- P+3 BIOLOGICAL / HEALTH / CULTIVATED-LIVING SYSTEMS
|   +-- C1 biomedical/endocrine/physiological
|   `-- C12 crops/food/vegetation/gardening
|
+-- C13 calendar/time                                [irreducible]
+-- C9 form/measurement/interface                    [mixed unresolved]
`-- C2,C5,C8,C10                                   [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 PROHIBITION / TRANSGRESSION / HARMFUL SOCIAL ACTION
|   +-- C1 prohibition/law/institutional judgement
|   `-- C3 violence/crime/tragedy
|       |
|       +-- C5 roles/authority                       [secondary]
|       `-- C4 weapons/physical setting             [secondary; mixed]
|
+-- P-1 SCIENTIFIC / BIOMEDICAL ANALYSIS & CONTROLLED TRANSFORMATION
|   +-- C6 scientific transformation/optimisation
|   `-- C9 diagnostics/pathology/clinical science
|       \
|        -- C10 technology/tools                    [secondary]
|
+-- C5 occupations/titles/fictional roles           [irreducible]
+-- C10 technology/digital-media systems             [irreducible]
+-- C4 built/weapons/clothing/objects                [mixed unresolved]
`-- C0,C2,C7,C8,C11,C12                            [formal/name substrate]
```

The preferred State 02 reconstruction contains four positive and two negative
multi-community parents. The positive semantic population admits strong
compression while preserving distinct action/context, technical/scientific,
civic/geographic and biological/living structures. The negative side is
organised principally around a social harm/constraint structure and a
scientific/biomedical transformation structure, with role, technology and
physical-world communities remaining outside those parents.

This statement is local to State 02 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction makes two broader merges:

1. absorb positive C9 into P+1, yielding a larger
   **computation/measurement/interface** parent;
2. replace negative P-0/P-1 with one larger **constraint, transformation and
   state-change** parent joining C1, C3 and C6.

The first alternative is rejected because C9 is materially heterogeneous.

The second is rejected because violence/social prohibition and scientific
optimisation are semantically distinct despite strong graph connectivity. The
broader parent would satisfy compression at the cost of discriminative value.

## Uncertainty record

- **P+3:** remains Moderate because biomedical health and cultivated plant/food
  systems share a living-system abstraction but retain distinct domains.
- **Positive C9:** is the major positive ambiguity. Its graph relations support
  technical/scientific affinity, but the underlying compact record is too mixed
  for primary parent membership.
- **Negative C4:** weapons and physical settings connect naturally to P-0, but
  clothing, transport and general built-object content prevent primary
  absorption.
- **Negative C5:** authority figures and warriors support a P-0 secondary link,
  but occupations, creative figures and fictional roles make it irreducible.
- **Negative P-1:** is preferred over a broader constraint/transformation
  parent because the biomedical/scientific relationship between C6 and C9 is
  more discriminative.
- **Cross-side semantic correspondence:** potentially present but not promoted
  because the available compact cross-side evidence does not establish it.

## Verification

- Positive communities accounted for: **14 / 14**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **27 / 27**
- Positive node accounting: **3,063 / 3,063**
- Negative node accounting: **2,816 / 2,816**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2, P+3**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every community inspected at underlying R008 community-record level: **yes**
- Materially ambiguous communities left unresolved or secondary rather than forced: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 02 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
