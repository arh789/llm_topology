# R010 State 12 — Block 11 output latent structure

## State identity

- R010 state index: `12`
- R008/R009 state: `block_11_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 13 negative-tail = 24**
- R008 population: **3,491 positive-head + 2,945 negative-tail = 6,436 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 12 only. Retrieval and graph inspection were
restricted to `state_index=12 / block_11_output`. No later-state evidence was
used.

## Evidence inventory

For every State 12 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_12_block_11_output.md`;
2. all 24 State 12 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 12 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## R009 / underlying-R008 discrepancy

Negative C12 is materially misdescribed by the R009 prose label.

- R009 labels C12 as **courtroom, evidence, injury, security and safety**.
- The underlying R008 State 12 C12 record instead contains **Alabama,
  Pennsylvania, Connecticut, Georgia, Scotland, Minnesota, Iowa, Montreal,
  Edinburgh, Illinois, Canada, Auckland** and related geographic forms.

The R010 disposition therefore follows the underlying R008 evidence and treats
negative C12 as a **geographic/public-territorial entity community**. The R009
label is not used for its parent inference.

This is precisely the type of discrepancy for which the R010 protocol gives
underlying R008 evidence priority over R009 prose.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 560 | 2,450 / 2,383 | 13.01 | +0.03046 | Personal/geographic entities, political/conflict labels and tokenizer residue coexist: Ken, Berlin, Gary, German, Hamburg, Mumbai, Rick and Palestinian alongside terrorist/militant material, replacement characters and malformed multilingual fragments. |
| C1 | 515 | 2,135 / 2,736 | 13.60 | +0.03079 | Exploration, activity, development and experiential process language dominates: initiating, observing, journeys, adventures, characterizing, innovative, travelling, trembling, originates, versatile, fashionable and motivations. |
| C2 | 475 | 1,875 / 2,796 | 13.78 | +0.03041 | Psychological/social, professional, political and business relations dominate: psychosocial, conversations, negotiating, management, Psychological, investigations, interventions, entrepreneurs, Political, discussions and contractual. |
| C3 | 450 | 1,936 / 2,365 | 13.86 | +0.03007 | Common grammatical/function words and short lexical fragments dominate. |
| C4 | 430 | 1,757 / 2,376 | 13.70 | +0.03014 | Biomedical, pharmacological, reproductive and infectious-disease terminology dominates: immunosuppressive, breastfeeding, dexamethasone, doxorubicin, antifungal, menopausal, pneumonia fragments, malaria, diazepam fragments, antioxidants, dopaminergic and overexpressed. |
| C5 | 265 | 985 / 1,644 | 13.64 | +0.03057 | Interactions, coupling, computation and mathematical/physical-system structure dominates: interactions, forms, coupling, size, actions, molecule, Lagrangian fragment, renormalization, computations, interacting, Transition and development. |
| C6 | 254 | 1,413 / 597 | 13.48 | +0.03058 | Strong punctuation/bracket/code-formatting cluster; 194 of 254 tokens are punctuation/symbols. |
| C7 | 229 | 832 / 1,332 | 13.08 | +0.03088 | Telecommunications, web/software, database and publishing/interface systems dominate: Acknowledgements, telecommunications, BytePtrFromString, Inflater, findViewById, scrolling, COPYRIGHT, mysql and createElement. |
| C8 | 147 | 516 / 792 | 12.41 | +0.03083 | Short technical/scientific abbreviations, units and time/measurement forms dominate; semantic domains are heterogeneous and abbreviation form is the clearer organising principle. |
| C9 | 111 | 683 / 188 | 14.00 | +0.02957 | Numeric strings, including years, dominate. |
| C10 | 55 | 132 / 445 | 12.89 | +0.02993 | Organisation, planning, positioning and situational/relational language is coherent: organizing, planning, anchored, organisation fragments, hosted, organized, situation and correlation fragments; extremes include orient, rapport and situated. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 495 | 2,200 / 2,383 | 13.70 | -0.03096 | Scientific characteristics, distributions and quantitative/clinical description dominate: Characteristics, distributions, environments, hospitalization, uniforms, concepts, recommendations, downregulation, requirement and Configuration; extremes include Features, specificity, variance, variability, quotient and covariance. |
| C1 | 407 | 1,602 / 1,998 | 12.78 | -0.03047 | Personal names dominate but lexical/technical fragments such as Comp, crypt, gluc, glyph, Disc and olith are substantial. |
| C2 | 351 | 1,774 / 1,606 | 14.68 | -0.03077 | Common grammatical/function words, punctuation and lexical fragments dominate. |
| C3 | 324 | 1,379 / 1,784 | 14.02 | -0.03074 | Negative evaluation, catastrophe, discrimination and adversity dominate: unconstitutional, unreasonable, catastrophe fragments, horrific, circumstantial, disasters, tragedy, disastrous, disproportionate, discriminatory and disappointing. |
| C4 | 244 | 1,038 / 1,424 | 14.34 | -0.03139 | Government, civic institutions, royalty, religion and family/social roles coexist: Constitution, citizens, guards, legislature, palace, emperor, Cathedral, queen, princess, cops, prince and priest; extremes include throne, Interior, wedding, aunt, Uncle and Telegraph. |
| C5 | 225 | 898 / 1,277 | 13.66 | -0.03120 | Vehicles, roads, built environment and natural terrain form a coherent physical-setting domain: automobiles, trucks, sidewalk, lake, gravel, driveway, dashboard, chassis, mountains, pavement, truck and hill. |
| C6 | 219 | 898 / 1,250 | 13.91 | -0.03072 | Prohibition, removal, creation and representational/change actions dominate: prohibiting, eliminating, Delete, Remove, includes, prohibited, prohibits, emphasizes, Create, excluding and depicts. |
| C7 | 171 | 722 / 898 | 13.70 | -0.03026 | Clinical diagnostics, cardiovascular medicine, anatomy and pathology are coherent: echocardiography, cardiovascular, angiography, torso, thighs, physiology, morphology, pathology, neuropsychology fragments, Disease and electrophoresis. |
| C8 | 161 | 938 / 431 | 14.33 | -0.03032 | Numeric strings, especially historical years, dominate. |
| C9 | 110 | 390 / 645 | 12.95 | -0.03043 | Adverbial/degree language, multilingual lexical material and measurement forms coexist; lexical/morphological form is the strongest common organisation. |
| C10 | 110 | 382 / 614 | 12.53 | -0.03124 | Technical/electronic/computing abbreviations and short codes dominate; short-code form is stronger than any one technical semantic domain. |
| C11 | 78 | 347 / 287 | 12.58 | -0.02916 | Strong mathematical/code punctuation and symbol-formatting cluster; 60 of 78 tokens are punctuation/symbols. |
| C12 | 50 | 218 / 267 | 14.06 | -0.03070 | Underlying R008 evidence shows a geographic/public-territorial entity community: Alabama, Pennsylvania, Connecticut, Georgia, province, Scotland, Minnesota, Iowa, Montreal, Edinburgh, Illinois, Canada and Auckland. |

## Population accounting

### Positive head

Total nodes: **3,491**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,685 | 48.3% |
| Formal substrate | 962 | 27.6% |
| Irreducible semantic | 284 | 8.1% |
| Mixed unresolved | 560 | 16.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,491** | **100.0%** |

Semantic-eligible denominator: **2,529 nodes**.

### Negative tail

Total nodes: **2,945**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,332 | 45.2% |
| Formal/name substrate | 1,217 | 41.3% |
| Irreducible semantic | 396 | 13.4% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,945** | **100.0%** |

Semantic-eligible denominator: **1,728 nodes**.

## Positive-side reconstruction

### P+0 — Exploratory activity and social-professional coordination

- **Primary children:** C1, C2
- **Primary nodes:** 990
- **Side-relative coverage:** 28.4%
- **Semantic-eligible coverage:** 39.1%
- **Confidence:** High / Moderate

**Evidence.** C1 contains exploration, journeys, development, observation,
characterisation and experiential process language. C2 contains psychosocial,
professional, political, business, negotiation, intervention and discussion
language. Their direct relation is the strongest positive semantic relation in
the state: **688 token edges**, mean cosine **0.10067**. The common generator is
organised human activity in which exploration/development is coordinated
through social, professional and institutional relations.

**Secondary links:** C7 and C10. C1–C7 has **206 edges** and C2–C7 **293**,
placing information/software systems adjacent to organised activity. C1–C10
has **88 edges** and C2–C10 **95**, supporting an organisation/planning
satellite.

**Exclusion boundary.** C1 includes lifestyle/experiential terms and C2
contains political/business structures. The parent is not broadened to generic
“human activity”. C7 remains a technical information-system domain rather than
being absorbed merely because it supports coordinated activity.

**Alternative.** Expand P+0 to include C7 under a broader
`organised activity and information systems` parent. Rejected because web,
database and publishing infrastructure retains a strong independent technical
identity.

### P+1 — Biomedical and interacting physical-system organisation

- **Primary children:** C4, C5
- **Primary nodes:** 695
- **Side-relative coverage:** 19.9%
- **Semantic-eligible coverage:** 27.5%
- **Confidence:** Moderate / High

**Evidence.** C4 supplies biomedical, pharmacological, reproductive and
infectious-disease concepts. C5 supplies interactions, coupling, computation,
molecules and mathematical/physical-system structure. Their direct relation
contains **270 token edges**, mean cosine **0.09505**. The common generator is
biological and physical systems represented through interactions, coupling and
state transitions.

**Secondary links:** C1 and C2. C1–C4 has **446 edges**, C2–C4 **483**, C1–C5
**333** and C2–C5 **312**. Scientific/biomedical structure is deeply embedded in
the broader activity/social field without losing its distinct semantic centre.

**Exclusion boundary.** C5's mathematical/physical content prevents a narrowly
biomedical label; C4's pharmacological/clinical material prevents a generic
physics label.

**Alternative.** Keep C4 and C5 separate as biomedical and
physical/computational-system structures. This remains plausible, so confidence
is Moderate/High rather than unqualified High.

### Positive irreducible and unresolved structures

- **C0 — mixed-unresolved:** personal/geographic entities, political/conflict
  labels and tokenizer residue coexist. Strong graph links to C2 (**451 edges**)
  and C4 (**511**) do not resolve its mixed internal organisation.
- **C7 — irreducible-semantic:** telecommunications, web/software, database and
  publishing/interface systems; secondary link to P+0.
- **C10 — irreducible-semantic:** organisation, planning, positioning and
  situational/relational language; secondary link to P+0.

### Positive formal substrate

- C3 — grammar/function words/fragments
- C6 — punctuation/formatting
- C8 — technical/scientific abbreviations, units and measurement forms
- C9 — numeric strings

## Negative-side reconstruction

### P-0 — Quantitative characterisation, adverse evaluation and restrictive/change operations

- **Primary children:** C0, C3, C6
- **Primary nodes:** 1,038
- **Side-relative coverage:** 35.2%
- **Semantic-eligible coverage:** 60.1%
- **Confidence:** High

**Evidence.** C0 contains scientific characteristics, distributions,
recommendations, quantitative description and clinical descriptors. C3
contains negative evaluation, catastrophe, discrimination and adversity. C6
contains prohibition, removal, creation and representational/change actions.
The three-child relation is strongly triangulated: C0–C3 has **380 token
edges**, mean cosine **0.10298**; C0–C6 **395** at **0.09745**; C3–C6 **295**
at **0.09901**. The common generator is the characterisation, evaluation and
restriction or alteration of problematic, deviant or disallowed states.

**Secondary link:** C7. C0–C7 has **224 edges**, C3–C7 **118** and C6–C7 **28**.
Clinical/pathological content is closely adjacent to the characterisation
branch but does not require primary absorption.

**Exclusion boundary.** C0 includes neutral scientific/quantitative
description, C3 is evaluative/adverse, and C6 includes constructive creation
and representation as well as prohibition/removal. The parent therefore cannot
be reduced to “negative evaluation”, “pathology” or “destruction”.

**Alternative.** Split C0 into an analytical/quantitative structure and retain
C3+C6 as an adverse-evaluation/restrictive-change structure. This preserves a
cleaner semantic distinction but sacrifices the strongest higher-order
triangulation in the negative graph.

### P-1 — Civic/social authority and geographic-public identity

- **Primary children:** C4, C12
- **Primary nodes:** 294
- **Side-relative coverage:** 10.0%
- **Semantic-eligible coverage:** 17.0%
- **Confidence:** Moderate

**Evidence.** C4 contains government, civic institutions, royalty, religion
and family/social roles. Underlying R008 C12 contains states, countries,
provinces and cities. Their direct relation contains **52 token edges**, mean
cosine **0.09856**. The shared higher-order structure is public/civic identity:
authority and social roles organised within geographic-political entities.

**Secondary link:** C5. C4–C5 has **209 edges**, mean cosine **0.09890**,
showing strong adjacency between civic/social roles and physical/public
settings. C5–C12 has **28** edges.

**Exclusion boundary.** C4 includes royalty, religion and family relations as
well as government, while C12 is geographic rather than institutional. C5 is
not absorbed because vehicles, roads and terrain are material settings rather
than civic identity itself.

**Alternative.** Leave C4 and C12 separate. This is a serious alternative
because their direct edge count is modest; the parent is retained only at
Moderate confidence.

### Negative irreducible structures

- **C5 — irreducible-semantic:** vehicles, roads, built environment and natural
  terrain; secondary link to P-1.
- **C7 — irreducible-semantic:** clinical diagnostics, cardiovascular medicine,
  anatomy and pathology; secondary link to P-0.

### Negative formal/name substrate

- C1 — personal names plus lexical/technical fragments
- C2 — grammar/function words/punctuation/fragments
- C8 — numeric strings
- C9 — adverbial/multilingual/measurement lexical forms
- C10 — technical/electronic short-code forms
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 560 | Personal/geographic + conflict + tokenizer residue | mixed-unresolved | — | Multiple semantic/formal organisations coexist. |
| + | C1 | 515 | Exploration/activity/development/process | parent:P+0 | — | Exploratory/developmental activity child. |
| + | C2 | 475 | Psychosocial/professional/political/business | parent:P+0 | — | Social-professional coordination child. |
| + | C3 | 450 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C4 | 430 | Biomedical/pharmacological/reproductive/infectious | parent:P+1 | — | Biological/clinical-system child. |
| + | C5 | 265 | Interactions/coupling/computation/physical systems | parent:P+1 | — | Physical/dynamical-system child. |
| + | C6 | 254 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C7 | 229 | Telecom/web/software/database/publishing | irreducible-semantic | P+0 | Information-system support relation without primary absorption. |
| + | C8 | 147 | Technical abbreviations/units/time forms | formal-substrate | — | Abbreviation/measurement form dominates. |
| + | C9 | 111 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C10 | 55 | Organisation/planning/situational language | irreducible-semantic | P+0 | Coordination/planning satellite without a sibling parent. |
| − | C0 | 495 | Scientific characteristics/distributions/quantitative | parent:P-0 | — | Analytical/quantitative characterisation. |
| − | C1 | 407 | Personal names + lexical/technical fragments | formal-substrate | — | Name/form organisation without one semantic class. |
| − | C2 | 351 | Grammar/function words/punctuation/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C3 | 324 | Negative evaluation/catastrophe/discrimination | parent:P-0 | — | Adverse-state evaluation. |
| − | C4 | 244 | Government/civic/royal/religious/social roles | parent:P-1 | — | Civic/social authority child. |
| − | C5 | 225 | Vehicles/roads/built environment/terrain | irreducible-semantic | P-1 | Material/public-setting relation. |
| − | C6 | 219 | Prohibition/removal/creation/change | parent:P-0 | — | Restrictive/change-operation child. |
| − | C7 | 171 | Clinical diagnostics/cardiovascular/anatomy | irreducible-semantic | P-0 | Clinical characterisation relation. |
| − | C8 | 161 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 110 | Adverbial/multilingual/measurement forms | formal-substrate | — | Lexical/morphological organisation dominates. |
| − | C10 | 110 | Technical/electronic short codes | formal-substrate | — | Abbreviation form dominates. |
| − | C11 | 78 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 50 | **Underlying R008: geographic/public-territorial entities** | parent:P-1 | — | Geographic-political identity; R009 prose label rejected. |

Every State 12 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Exploratory activity and social-professional coordination | C1, C2 | 990 | 28.4% | 39.1% | High / Moderate |
| P+1 | Biomedical and interacting physical-system organisation | C4, C5 | 695 | 19.9% | 27.5% | Moderate / High |
| P-0 | Quantitative characterisation, adverse evaluation and restrictive/change operations | C0, C3, C6 | 1,038 | 35.2% | 60.1% | High |
| P-1 | Civic/social authority and geographic-public identity | C4, C12 | 294 | 10.0% | 17.0% | Moderate |

Positive retained parents account for **1,685 nodes**, **48.3% of the positive
population** and **66.6% of semantic-eligible positive nodes**.

Negative retained parents account for **1,332 nodes**, **45.2% of the negative
population** and **77.1% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — activity/social and scientific relation — High.**
   C1–C4 has **446 edges**, C2–C4 **483**, C1–C5 **333** and C2–C5 **312**.
   Biomedical/physical-system structure is deeply embedded in exploration and
   social-professional activity without becoming the same semantic generator.

2. **P+0 ↔ C7 — organised activity/information-system relation — High.**
   C1–C7 has **206 edges**, C2–C7 **293**. Software, publishing and
   telecommunications are strongly adjacent to coordinated activity, but their
   technical identity remains independent.

3. **P+0 ↔ C10 — planning/coordination satellite — Moderate.**
   C1–C10 has **88 edges**, C2–C10 **95**. The semantic fit is strong enough to
   record a secondary relation but not enough to manufacture a third parent
   child.

4. **C0 is structurally connected but semantically unresolved.**
   C0–C2 has **451 edges**, C0–C4 **511**, and C0–C3 **476**. High connectivity
   cannot resolve its geography/name, conflict and tokenizer-residue mixture.

### Negative-side relations

1. **P-0 ↔ P-1 — characterisation/constraint in civic context — High.**
   C0–C4 has **305 edges**, C3–C4 **224**, C0–C12 **20**, C3–C12 **22** and
   C6–C12 **2**. The principal relation runs through C4: evaluative and
   restrictive processes are embedded in public/civic authority contexts.

2. **P-1 ↔ C5 — civic roles and material setting — High.**
   C4–C5 has **209 edges**, mean cosine **0.09890**. Roads, vehicles and built
   environments act as material settings for civic/public organisation without
   becoming authority structures themselves.

3. **P-0 ↔ C7 — clinical characterisation relation — Moderate to High.**
   C0–C7 has **224 edges**, C3–C7 **118** and C6–C7 **28**. Clinical/pathology
   semantics are strongly adjacent to analytical/adverse-state
   characterisation but remain a distinct medical domain.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-1 through organised social/professional systems;
- positive P+1 and negative C7/P-0 through biomedical and clinical structure;
- positive C7 and negative technical/formal populations through information
  and computing systems.

No direct cross-side community evidence was inspected that justified a
parent-level bridge.

## Formal/representational substrate

### Positive — 962 nodes / 27.6%

- grammar/function words and fragments;
- punctuation/formatting;
- technical/scientific abbreviations, units and measurement forms;
- numeric strings.

### Negative — 1,217 nodes / 41.3%

- personal names plus lexical/technical fragments;
- grammar/function words/punctuation/fragments;
- numeric strings;
- adverbial/multilingual/measurement lexical forms;
- technical/electronic short-code forms;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 12 — BLOCK 11 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 EXPLORATORY ACTIVITY & SOCIAL-PROFESSIONAL COORDINATION
|   +-- C1 exploration/activity/development/process
|   `-- C2 psychosocial/professional/political/business relations
|       |
|       +-- C7 telecom/web/software/publishing         [secondary]
|       `-- C10 organisation/planning/situation       [secondary]
|
+-- P+1 BIOMEDICAL & INTERACTING PHYSICAL-SYSTEM ORGANISATION
|   +-- C4 biomedical/pharmacological/reproductive/infectious
|   `-- C5 interactions/coupling/computation/physical systems
|
+-- C0 names/geography + conflict + tokenizer residue  [mixed unresolved]
+-- C7 telecom/web/software/database/publishing        [irreducible]
+-- C10 organisation/planning/situational              [irreducible]
`-- C3,C6,C8,C9                                       [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 QUANTITATIVE CHARACTERISATION / ADVERSE EVALUATION / RESTRICTIVE-CHANGE OPERATIONS
|   +-- C0 scientific characteristics/distributions
|   +-- C3 negative evaluation/catastrophe/discrimination
|   `-- C6 prohibition/removal/creation/change
|       \
|        -- C7 clinical diagnostics/pathology         [secondary]
|
+-- P-1 CIVIC/SOCIAL AUTHORITY & GEOGRAPHIC-PUBLIC IDENTITY
|   +-- C4 government/civic/royal/religious/social roles
|   `-- C12 geographic/public-territorial entities
|       \
|        -- C5 roads/vehicles/built environment       [secondary]
|
+-- C5 vehicles/roads/built environment/terrain        [irreducible]
+-- C7 clinical diagnostics/cardiovascular/anatomy     [irreducible]
`-- C1,C2,C8,C9,C10,C11                               [formal/name substrate]
```

The preferred State 12 reconstruction contains two positive and two negative
multi-community parents. The negative side contains an especially strong
three-child higher-order structure linking quantitative characterisation,
adverse evaluation and restrictive/change operations. The positive side is
more selective: exploratory/social-professional coordination and
biomedical/physical-system organisation are retained, while software/publishing
and the large mixed name/conflict community remain outside those parents.

This statement is local to State 12 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C7 into P+0 under a broader
   **organised activity and information systems** parent;
2. keep positive C4 and C5 separate as biomedical and physical/computational
   structures;
3. split negative P-0 into analytical/quantitative C0 and adverse
   evaluation/restrictive change C3+C6;
4. leave negative C4 and C12 separate rather than retaining P-1.

The third alternative is the most serious because neutral quantitative
description is semantically distinct from adversity and prohibition. The
preferred reconstruction retains P-0 because C0–C3, C0–C6 and C3–C6 form
strong triangulation rather than a single incidental link.

## Uncertainty record

- **Positive P+0:** C1 is broad across exploration, lifestyle and process
  language, while C2 spans psychosocial, political and business relations.
- **Positive P+1:** biomedical and mathematical/physical systems remain distinct
  child domains joined by interaction/coupling.
- **Positive C0:** is the main positive unresolved community; its very high
  connectivity does not resolve its mixed entity/conflict/tokenizer structure.
- **Negative P-0:** is semantically broad but has strong three-way graph
  support.
- **Negative P-1:** retained only at Moderate confidence because C4–C12 direct
  edge count is modest.
- **Negative C12:** R009 prose conflicts materially with underlying R008. R010
  follows R008 and records the discrepancy explicitly.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **3,491 / 3,491**
- Negative node accounting: **2,945 / 2,945**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 12 community inspected at underlying R008 community-record level: **yes**
- All State 12 within-side community relations inspected: **yes**
- R009/R008 discrepancy followed in favour of underlying R008: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 12 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 12 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
