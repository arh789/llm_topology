# R010 State 11 — Block 10 output latent structure

## State identity

- R010 state index: `11`
- R008/R009 state: `block_10_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **14 positive-head + 12 negative-tail = 26**
- R008 population: **3,161 positive-head + 3,060 negative-tail = 6,221 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 11 only. Retrieval and graph inspection were
restricted to `state_index=11 / block_10_output`. No later-state evidence was
used.

## Evidence inventory

For every State 11 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_11_block_10_output.md`;
2. all 26 State 11 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 11 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 437 | 1,912 / 2,369 | 14.17 | +0.03195 | Psychology, investigation and social/professional activity coexist: negotiating, psychosocial, investigations, conversations, psychological, therapists, determinations, psychiatry fragments, management and research; extremes include employment, fellowship, talks, Business, bidding and games. |
| C1 | 386 | 1,604 / 2,106 | 13.77 | +0.03130 | Common grammatical/function words and short lexical fragments dominate. |
| C2 | 358 | 1,431 / 2,032 | 13.67 | +0.03154 | Observation, evaluation, emergence and process/cognitive actions dominate: initiating, observing, emerging, travelling, resolving, evaluating, motivated, experiencing, remembering, interpreting, originates and overexpressed. |
| C3 | 296 | 1,251 / 1,467 | 13.41 | +0.03154 | Personal names, cities, nationalities and geographic entities form a coherent geographic/name domain. |
| C4 | 285 | 1,180 / 1,708 | 14.27 | +0.03129 | Neuropharmacology, immunity, cellular biology and oxidative processes dominate: immunosuppressive, dopaminergic, antipsychotic fragments, biodegradation fragments, neurotransmitter fragments, transmembrane, dexamethasone, intracellular, anticancer, immunodeficiency fragments, mitochondrial and oxidative. |
| C5 | 269 | 940 / 1,661 | 13.16 | +0.03181 | Interactions, fields, regularisation and mathematical/physical-system structure dominate: interactions, forms, renormalization, coupling, actions, regularization, action, interaction, fields, Lagrangian and interacting. |
| C6 | 232 | 815 / 1,370 | 12.93 | +0.03165 | Food, leisure, daily activity and health/biological material coexist: coffee, rice, grinned, laughed, washing, malaria, amusement, fishermen, stainless, cafe, champagne and sprang. |
| C7 | 226 | 1,302 / 521 | 13.83 | +0.03115 | Strong closing-punctuation/bracket/code-formatting cluster; 176 of 226 tokens are punctuation/symbols. |
| C8 | 195 | 636 / 1,110 | 12.22 | +0.03110 | Multilingual, malformed and fragmentary tokenisation residues dominate. |
| C9 | 195 | 720 / 1,101 | 13.03 | +0.03231 | Web/software, database and publishing/interface systems dominate: Acknowledgements, Django fragment, BytePtrFromString, createElement, CONTRIBUTORS, WordPress, findViewById, mysql, Kubernetes fragment and MySQL. |
| C10 | 126 | 480 / 622 | 12.56 | +0.03181 | Short technical/scientific abbreviations and measurement forms dominate. |
| C11 | 98 | 589 / 179 | 13.85 | +0.03073 | Numeric strings, including years, dominate. |
| C12 | 32 | 104 / 214 | 13.19 | +0.03236 | Comparative physical, freshness, temperature and price descriptors form a coherent modifier cluster: Fresh, wider, freshly, fresh, newer, thicker, Old, inexpensive, cheapest, extra and cold. |
| C13 | 26 | 80 / 188 | 13.38 | +0.03109 | Response, answering, listening and feedback language is coherent: response, Response, responses, responding, answering, answer, listening and answered. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 486 | 2,004 / 2,240 | 12.86 | -0.03027 | Personal names dominate but lexical/technical fragments are substantial: Lucy, Molly, Blair, Claud, Hicks and Dav coexist with discour-, Comp, crypt, glyph and gluc fragments. |
| C1 | 405 | 1,712 / 2,133 | 13.72 | -0.03036 | Scientific characteristics, distributions, instrumentation and quantitative description dominate: Characteristics, environments, distributions, uniforms, technologies, uniformity, instrumentation, circumstance, methodologies and requirement; extremes include Features, specificity, variance, covariance and quotient. |
| C2 | 402 | 1,726 / 2,065 | 13.72 | -0.03032 | Negative evaluation, catastrophe, discrimination and vocal distress dominate: unconstitutional, unreasonable, circumstantial, horrific, catastrophe fragments, discriminatory, disasters, whispers, scream, inaccurate, screams and catastrophe. |
| C3 | 317 | 1,604 / 1,560 | 15.04 | -0.03028 | Common grammatical/function words, punctuation and lexical fragments dominate. |
| C4 | 288 | 1,196 / 1,615 | 13.91 | -0.03035 | Social roles, royalty, religion and fictional/authority figures coexist: warriors, queen, guards, princess, users, priest, Cathedral, prince, chapel, goddess, customers and girls; extremes include throne, speakers, creature, Devil and Doll. |
| C5 | 251 | 982 / 1,439 | 13.56 | -0.03007 | Roads, transport, built environment and natural landscape form a coherent physical-setting domain: hallway, trucks, sidewalk, automobiles, roadway, mountains, dashboard, roads, truck, lake, woods and corridor. |
| C6 | 248 | 1,022 / 1,415 | 13.95 | -0.03051 | Prohibition, elimination, destruction and creation/change actions dominate: prohibiting, eliminating, destroys, Delete, includes, destroyed, prohibited, prohibits, emphasizing, kill, Create and depicts. |
| C7 | 181 | 624 / 901 | 11.87 | -0.02992 | Multilingual words, suffixes and orthographic fragments dominate. |
| C8 | 155 | 961 / 276 | 14.18 | -0.02963 | Numeric strings, especially historical years, dominate. |
| C9 | 145 | 578 / 803 | 13.51 | -0.02940 | Clinical diagnostics, cardiovascular medicine and anatomy/pathology are coherent: echocardiography, physiology, cardiovascular, angiography, dysfunction, epidemiological, epithelium, carcinoma, Disease and thighs. |
| C10 | 99 | 377 / 601 | 13.69 | -0.03136 | Geography, government, law and civic/public entities coexist coherently enough for a public/civic domain: Constitution, citizens, Edinburgh, Scotland, Connecticut, Newcastle, province, Montreal, Romania and provisions. |
| C11 | 83 | 434 / 224 | 13.16 | -0.02831 | Strong mathematical/code punctuation and symbol-formatting cluster; 78 of 83 tokens are punctuation/symbols. |

## Population accounting

### Positive head

Total nodes: **3,161**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,544 | 48.8% |
| Formal substrate | 1,031 | 32.6% |
| Irreducible semantic | 354 | 11.2% |
| Mixed unresolved | 232 | 7.3% |
| Unclear | 0 | 0.0% |
| **Total** | **3,161** | **100.0%** |

Semantic-eligible denominator: **2,130 nodes**.

### Negative tail

Total nodes: **3,060**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,442 | 47.1% |
| Formal/name substrate | 1,222 | 39.9% |
| Irreducible semantic | 396 | 12.9% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,060** | **100.0%** |

Semantic-eligible denominator: **1,838 nodes**.

## Positive-side reconstruction

### P+0 — Investigation, evaluation and information-production systems

- **Primary children:** C0, C2, C9
- **Primary nodes:** 990
- **Side-relative coverage:** 31.3%
- **Semantic-eligible coverage:** 46.5%
- **Confidence:** Moderate / High

**Evidence.** C0 contains investigation, research, management, negotiation and
professional/social activity. C2 contains observing, evaluating, interpreting,
remembering, resolving and other cognitive/process operations. C9 supplies
software, database, web, publishing and interface systems. C0–C2 is the
strongest positive relation at **539 token edges**, mean cosine **0.10195**;
C0–C9 adds **222 edges** and C2–C9 **126**. The common generator is organised
knowledge work in which information is investigated, evaluated, processed and
produced through technical systems.

**Secondary link:** C13. It contributes response/answer/feedback language and
connects to C2 (**38 edges**), C0 (**28**) and C9 (**14**), but is too small and
weakly linked to require primary absorption.

**Exclusion boundary.** C0 contains employment/social material, C2 contains
general process language and C9 contains publishing/interface specifics. The
parent does not expand into generic social activity or all software. C4 remains
a distinct biomedical domain despite C0–C4 (**307 edges**) and C2–C4
(**190**) being substantial.

**Alternative.** Define P+0 only from C0+C2 and leave C9 irreducible. This
preserves a narrower cognitive/investigative parent but loses the strong
information-production/system relation expressed by C0–C9 and C2–C9.

### P+1 — Biological and interacting physical-system organisation

- **Primary children:** C4, C5
- **Primary nodes:** 554
- **Side-relative coverage:** 17.5%
- **Semantic-eligible coverage:** 26.0%
- **Confidence:** Moderate / High

**Evidence.** C4 supplies neuropharmacology, immunity, cellular biology and
oxidative processes. C5 supplies interactions, fields, coupling,
regularisation and mathematical/physical-system structure. Their direct
relation contains **232 token edges**, mean cosine **0.09496**. The common
generator is interacting biological/physical systems represented through
coupling, fields and dynamic relations.

**Secondary link:** C6. C4–C6 has **248 edges**, mean cosine **0.09860**, but
C6's leisure/daily-life content prevents primary absorption. C5–C6 has **138**
edges.

**Exclusion boundary.** C5's mathematical/physical content prevents a narrowly
biomedical label, while C4's pharmacological/cellular content prevents a
generic physics parent. C6 remains mixed rather than being redefined through
its biological component alone.

**Alternative.** Pair C4 with C6 under a broad health/living-systems parent.
That alternative has slightly stronger raw connectivity but performs worse
semantically because C6 contains food, leisure and daily-life material that is
not generated by the same scientific structure.

### Positive irreducible and unresolved structures

- **C3 — irreducible-semantic:** personal names, cities, nationalities and
  geographic entities.
- **C12 — irreducible-semantic:** comparative physical/freshness/temperature
  and price descriptors.
- **C13 — irreducible-semantic:** response, answering, listening and feedback;
  secondary link to P+0.
- **C6 — mixed-unresolved:** food, leisure, daily activity and
  health/biological material; secondary link to P+1.

### Positive formal substrate

- C1 — grammar/function words/fragments
- C7 — punctuation/formatting
- C8 — multilingual/malformed fragments
- C10 — technical/scientific abbreviations
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Quantitative characterisation, adverse evaluation and destructive constraint

- **Primary children:** C1, C2, C6
- **Primary nodes:** 1,055
- **Side-relative coverage:** 34.5%
- **Semantic-eligible coverage:** 57.4%
- **Confidence:** High

**Evidence.** C1 contains scientific characteristics, distributions,
instrumentation and quantitative description. C2 contains negative evaluation,
catastrophe, discrimination and distress. C6 contains prohibition,
elimination, destruction and creation/change. The three-child structure is
strongly triangulated: C1–C2 has **432 token edges**, mean cosine **0.09869**;
C1–C6 **320** at **0.09564**; C2–C6 **379** at **0.10130**. The larger
generator is the characterisation, evaluation and constraint of problematic,
deviant or disallowed states.

**Secondary link:** C9. C1–C9 has **179 edges**, C2–C9 **91** and C6–C9 **39**,
placing clinical/pathological description adjacent to the characterisation
branch without requiring primary absorption.

**Exclusion boundary.** C1 includes neutral quantitative description, C2
contains affective/vocal distress and C6 contains both destructive and
constructive change. The parent therefore cannot be reduced to “negative
emotion”, “pathology” or “destruction”.

**Alternative.** Split C1 into an analytical/quantitative parent and retain
C2+C6 as an adverse-evaluation/destructive-constraint parent. This preserves a
clearer semantic distinction, but the observed triangulation supports the
higher-order parent strongly enough to retain it.

### P-1 — Civic/institutional authority and social roles

- **Primary children:** C4, C10
- **Primary nodes:** 387
- **Side-relative coverage:** 12.6%
- **Semantic-eligible coverage:** 21.1%
- **Confidence:** Moderate / High

**Evidence.** C4 contains royalty, religion, social roles and authority figures;
C10 contains geography, government, law and civic/public entities. Their direct
relation contains **111 token edges**, mean cosine **0.10284**. The common
generator is institutional/civic order expressed through roles, authority,
governance and public entities.

**Secondary link:** C5. C4–C5 has **257 edges**, reflecting the material
settings in which institutional/social roles occur. C5–C10 has **49** edges.

**Exclusion boundary.** C4 includes fictional figures and ordinary customers,
while C10 includes geographic names as well as legal/government terms. C5 is
not absorbed because roads, landscape and transport are material settings
rather than civic authority itself.

**Alternative.** Leave C4 and C10 separate and treat their relation as
authority-to-civic-context adjacency. This remains plausible, so confidence is
Moderate/High rather than unqualified High.

### Negative irreducible structures

- **C5 — irreducible-semantic:** roads, transport, built environment and natural
  landscape; secondary relation to P-1.
- **C9 — irreducible-semantic:** clinical diagnostics, cardiovascular medicine
  and anatomy/pathology; secondary relation to P-0.

### Negative formal/name substrate

- C0 — personal names mixed with lexical/technical fragments
- C3 — grammar/function words/punctuation/fragments
- C7 — multilingual morphology
- C8 — numeric strings
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 437 | Psychology/investigation/social-professional activity | parent:P+0 | — | Knowledge-work/investigation structure dominates. |
| + | C1 | 386 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C2 | 358 | Observation/evaluation/process-cognitive actions | parent:P+0 | — | Cognitive/evaluative operations. |
| + | C3 | 296 | Names/cities/nationalities/geography | irreducible-semantic | — | Coherent geographic/name domain without a sibling parent. |
| + | C4 | 285 | Neuropharmacology/immunity/cellular biology | parent:P+1 | — | Biological-system child. |
| + | C5 | 269 | Interactions/fields/regularisation/physical systems | parent:P+1 | — | Physical/dynamical-system child. |
| + | C6 | 232 | Food/leisure/daily-life + biological material | mixed-unresolved | P+1 | Biological affinity is real, but daily/leisure content remains material. |
| + | C7 | 226 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C8 | 195 | Multilingual/malformed fragments | formal-substrate | — | Orthographic/tokeniser form. |
| + | C9 | 195 | Web/software/database/publishing systems | parent:P+0 | — | Information-production/system child. |
| + | C10 | 126 | Technical/scientific abbreviations | formal-substrate | — | Abbreviation/measurement form dominates. |
| + | C11 | 98 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C12 | 32 | Comparative physical/freshness/price descriptors | irreducible-semantic | — | Coherent modifier domain without a sibling parent. |
| + | C13 | 26 | Response/answer/listening/feedback | irreducible-semantic | P+0 | Information-response relation but insufficient evidence for primary absorption. |
| − | C0 | 486 | Personal names + lexical/technical fragments | formal-substrate | — | Name/form organisation without one semantic class. |
| − | C1 | 405 | Scientific characteristics/distributions/quantitative | parent:P-0 | — | Analytical/quantitative characterisation. |
| − | C2 | 402 | Negative evaluation/catastrophe/distress | parent:P-0 | — | Adverse-state evaluation. |
| − | C3 | 317 | Grammar/function words/punctuation/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 288 | Social roles/royalty/religion/authority figures | parent:P-1 | — | Institutional/social-role child. |
| − | C5 | 251 | Roads/transport/built environment/landscape | irreducible-semantic | P-1 | Material-setting relation without civic-role identity. |
| − | C6 | 248 | Prohibition/elimination/destruction/change | parent:P-0 | — | Constraint/destructive-change child. |
| − | C7 | 181 | Multilingual words/suffixes/fragments | formal-substrate | — | Morphological/orthographic form. |
| − | C8 | 155 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 145 | Clinical diagnostics/cardiovascular/anatomy | irreducible-semantic | P-0 | Clinical characterisation adjacent to analytical parent. |
| − | C10 | 99 | Geography/government/law/civic entities | parent:P-1 | — | Civic/public-order child. |
| − | C11 | 83 | Maths/code punctuation | formal-substrate | — | Formatting form. |

Every State 11 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Investigation, evaluation and information-production systems | C0, C2, C9 | 990 | 31.3% | 46.5% | Moderate / High |
| P+1 | Biological and interacting physical-system organisation | C4, C5 | 554 | 17.5% | 26.0% | Moderate / High |
| P-0 | Quantitative characterisation, adverse evaluation and destructive constraint | C1, C2, C6 | 1,055 | 34.5% | 57.4% | High |
| P-1 | Civic/institutional authority and social roles | C4, C10 | 387 | 12.6% | 21.1% | Moderate / High |

Positive retained parents account for **1,544 nodes**, **48.8% of the positive
population** and **72.5% of semantic-eligible positive nodes**.

Negative retained parents account for **1,442 nodes**, **47.1% of the negative
population** and **78.5% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — investigation/scientific relation — High.**
   C0–C4 has **307 edges**, C0–C5 **329**, C2–C4 **190**, C2–C5 **286** and
   C9–C5 **142**. Investigation, evaluation and information systems are strongly
   coupled to biological and physical-system content without becoming the same
   semantic structure.

2. **P+1 ↔ C6 — biological/lived-world relation — High but heterogeneous.**
   C4–C6 has **248 edges** and C5–C6 **138**. The biological component of C6
   clearly connects to P+1, but leisure and daily-life material prevents
   primary absorption.

3. **P+0 ↔ C3 — social/geographic context — Moderate.**
   C0–C3 has **240 edges** and C2–C3 **85**. Geographic populations contextualise
   social/professional investigation without forming a common parent.

4. **C13 is a small response/feedback satellite of P+0.**
   Its direct links are modest, so semantic fit is recorded without overstating
   graph support.

### Negative-side relations

1. **P-0 ↔ P-1 — constraint/evaluation and institutional order — High.**
   C1–C4 has **279 edges**, C2–C4 **279**, C1–C10 **83**, C2–C10 **82** and
   C6–C10 **41**. Evaluation and constraint are strongly situated within
   authority, governance and public-order contexts.

2. **P-1 ↔ C5 — institutional role and material setting — High.**
   C4–C5 has **257 edges**, one of the strongest non-P-0 semantic relations in
   the state. The physical environment is tightly connected to public/social
   roles while remaining a distinct material domain.

3. **P-0 ↔ C9 — clinical characterisation relation — Moderate.**
   C1–C9 has **179 edges**, C2–C9 **91** and C6–C9 **39**. Clinical/pathological
   content is adjacent to quantitative/adverse-state characterisation but does
   not require primary absorption.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-0 through investigation/evaluation;
- positive P+1 and negative C9 through biological/clinical structure;
- positive C3 and negative P-1 through geographic/civic context;
- positive C9 and negative analytical/technical material through information
  systems.

The within-side evidence does not require a cross-side bridge, and none is
promoted without direct community-level cross-side support.

## Formal/representational substrate

### Positive — 1,031 nodes / 32.6%

- grammar/function words and fragments;
- punctuation/formatting;
- multilingual/malformed fragments;
- technical/scientific abbreviations;
- numeric strings.

### Negative — 1,222 nodes / 39.9%

- personal names plus lexical/technical fragments;
- grammar/function words/punctuation/fragments;
- multilingual morphology;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 11 — BLOCK 10 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INVESTIGATION / EVALUATION / INFORMATION-PRODUCTION SYSTEMS
|   +-- C0 psychology/investigation/social-professional activity
|   +-- C2 observation/evaluation/process-cognitive actions
|   `-- C9 web/software/database/publishing systems
|       \
|        -- C13 response/answer/feedback             [secondary]
|
+-- P+1 BIOLOGICAL & INTERACTING PHYSICAL-SYSTEM ORGANISATION
|   +-- C4 neuropharmacology/immunity/cellular biology
|   `-- C5 interactions/fields/regularisation/physical systems
|       \
|        -- C6 food/leisure/daily-life/biology       [secondary; mixed]
|
+-- C3 names/geography                                [irreducible]
+-- C6 food/leisure/daily-life/biology                [mixed unresolved]
+-- C12 comparative physical/freshness/price          [irreducible]
+-- C13 response/answer/feedback                       [irreducible]
`-- C1,C7,C8,C10,C11                                 [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 QUANTITATIVE CHARACTERISATION / ADVERSE EVALUATION / DESTRUCTIVE CONSTRAINT
|   +-- C1 scientific characteristics/quantitative description
|   +-- C2 negative evaluation/catastrophe/distress
|   `-- C6 prohibition/elimination/destruction/change
|       \
|        -- C9 clinical diagnostics/pathology        [secondary]
|
+-- P-1 CIVIC/INSTITUTIONAL AUTHORITY & SOCIAL ROLES
|   +-- C4 royalty/religion/social/authority figures
|   `-- C10 geography/government/law/civic entities
|       \
|        -- C5 roads/transport/built environment     [secondary]
|
+-- C5 roads/transport/built environment              [irreducible]
+-- C9 clinical diagnostics/cardiovascular/anatomy    [irreducible]
`-- C0,C3,C7,C8,C11                                  [formal/name substrate]
```

The preferred State 11 reconstruction contains two positive and two negative
multi-community parents. The positive side separates organised knowledge work
and information production from biological/physical-system organisation. The
negative side contains a strongly triangulated higher-order structure joining
quantitative characterisation, adverse evaluation and destructive constraint,
plus a separate civic/institutional authority structure.

This statement is local to State 11 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. restrict positive P+0 to C0+C2 and leave C9 irreducible;
2. replace positive P+1 with a C4+C6 health/living-systems parent;
3. split negative P-0 into analytical/quantitative C1 and adverse
   evaluation/constraint C2+C6;
4. leave negative C4 and C10 separate rather than retaining P-1.

The third alternative is the most serious. It preserves a clear distinction
between neutral quantitative description and adverse evaluation/destructive
constraint. The preferred reconstruction retains the higher-order parent
because C1–C2, C1–C6 and C2–C6 form unusually strong triangulation.

## Uncertainty record

- **Positive P+0:** C0 is broad across psychology, investigation and employment;
  C9 includes publishing as well as software. The common knowledge-work parent
  remains Moderate/High rather than pure.
- **Positive P+1:** biological and mathematical/physical systems are related
  through interaction/coupling but remain distinct child domains.
- **Positive C6:** is the main positive unresolved community because its
  biological/health material coexists with food, leisure and daily-life
  content.
- **Negative P-0:** is semantically broad, but it has the strongest
  multi-community triangulation in the state.
- **Negative P-1:** C4 includes fictional roles and C10 includes geographic
  entities; the civic/institutional parent remains Moderate/High.
- **Negative C0:** is treated as formal/name substrate despite some semantic
  fragments because no coherent semantic class explains its mixed name/fragment
  organisation.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **14 / 14**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **26 / 26**
- Positive node accounting: **3,161 / 3,161**
- Negative node accounting: **3,060 / 3,060**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 11 community inspected at underlying R008 community-record level: **yes**
- All State 11 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 11 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 11 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
