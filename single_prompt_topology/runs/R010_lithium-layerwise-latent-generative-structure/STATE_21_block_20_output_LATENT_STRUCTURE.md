# R010 State 21 — Block 20 output latent structure

## State identity

- R010 state index: `21`
- R008/R009 state: `block_20_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 11 negative-tail = 23**
- R008 population: **2,706 positive-head + 3,155 negative-tail = 5,861 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 21 only. Retrieval and graph inspection were
restricted to `state_index=21 / block_20_output`. No later-state evidence was
used.

## Evidence inventory

For every State 21 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_21_block_20_output.md`;
2. all 23 State 21 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 21 within-side relation set in
   `R008/community_edges.csv`;
4. the State 21 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained
with explicit uncertainty rather than forced into broader parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 435 | 1,876 / 1,757 | 12.66 | +0.03249 | Personal names, cities and geographic/name-like entities dominate: Steve, Scott, Matt, Peter, Karen, Josh, Manchester, Mitchell, Nam, Jake, Kashmir and Jay. |
| C1 | 345 | 1,595 / 1,951 | 14.90 | +0.03212 | Common grammatical/function words and lexical fragments dominate. |
| C2 | 340 | 1,404 / 2,024 | 14.21 | +0.03267 | Exploration, measurement, characterisation, motivation and developmental processes dominate: exploring, Measurements, characterizing, quantification, motivations, Measurement, anticipated, recorded, motivation, adventures, resolving and characterize. |
| C3 | 298 | 1,016 / 1,946 | 13.35 | +0.03232 | Interaction, evolution, emergence and theoretical-system concepts dominate: interactions, evolves, evolving, phenomenological, interacting and renormalization, with inevitability/reappearance stems also present. |
| C4 | 276 | 1,051 / 1,585 | 13.36 | +0.03285 | Biomedical, psychiatric, immunological and pharmacological terminology is coherent: breastfeeding, dopaminergic, psychiatry fragments, hospital fragments, Medical, immunostaining, Biomed, dexamethasone, diazepam fragments, tumorigenesis, analgesic and doxorubicin. |
| C5 | 247 | 947 / 1,518 | 13.81 | +0.03225 | Social/professional, creative and commercial activity coexists with food and travel: Food, sessions, entrepreneurs, filmmakers, interventions, conversations, shops, negotiating, Travel, filmmaker, Animation and business. |
| C6 | 246 | 1,340 / 658 | 13.57 | +0.03365 | Mathematical/code punctuation and symbolic formatting dominate; 169 of 246 tokens are punctuation/symbols. |
| C7 | 172 | 587 / 1,001 | 12.65 | +0.03271 | Media/software/interface terms coexist with size, position and layout concepts: photography, facebook, Photo, Netflix, Notification, Address, Position, Session, browsers, widths, spacing and Size. |
| C8 | 124 | 723 / 301 | 14.09 | +0.03080 | Numeric strings and short coded values dominate. |
| C9 | 118 | 427 / 788 | 13.92 | +0.03145 | Temporal, freshness, analytical and evaluative descriptors dominate: surprisingly, fresh fragments, Fresh, Recently, analytically, clinically, Feb, intuitive, score, older and Wednesday. |
| C10 | 69 | 204 / 507 | 13.26 | +0.03339 | Affect, consciousness, sleep, compassion and bodily/social actions form a coherent subjective/embodied-state domain: happiness, consciousness, discomfort, Sleep, kissing, sleeping, Hit, swung, compassion, aspirations and pleasure. |
| C11 | 36 | 140 / 230 | 14.17 | +0.03369 | Example-related multilingual words and morphological fragments dominate. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 580 | 2,649 / 2,702 | 13.79 | -0.02987 | Administrative characterisation, recommendations, regulation and constitutional concepts coexist: Characteristics, recommendations, administrators, Configuration, characteristics, unconstitutional, beneficiaries, regulations, Constitution and encouragement. |
| C1 | 407 | 1,724 / 1,715 | 12.69 | -0.03027 | Common grammatical/function words mixed with multilingual lexical/token fragments dominate. |
| C2 | 396 | 1,591 / 1,936 | 12.92 | -0.03014 | Short name-like and technical/code abbreviations dominate: GH, Cl, RA, Bra, Gh, Tob, Hu, Tah, Gu, Rh, Rog and TC. |
| C3 | 303 | 1,236 / 1,528 | 13.20 | -0.02986 | Downregulation, removal, encouragement, prohibition and verification/change actions dominate: downregulation, removing, encourages, prohibiting, resembled, Delete, creates, prohibited, discouragement fragments, prohibits, undermined and verifying. |
| C4 | 277 | 1,132 / 1,629 | 14.05 | -0.02972 | Negative/intense evaluation, catastrophe and discrimination dominate: unreasonable, disastrous, incredible, occasionally, stupid, spectacular, unbelievable, discriminatory, frightening and exceedingly. |
| C5 | 271 | 1,029 / 1,575 | 13.41 | -0.03117 | Vehicles, roads, built environment and material/household objects form a broad physical-world domain: trucks, automobiles, roads, circumferential, vegetables, cylinder, gravel, pavement, chassis, firearms, Mountains and sidewalk. |
| C6 | 246 | 1,167 / 1,201 | 14.37 | -0.03005 | Personal names mixed with geographic entities and regions: Laura, Alabama, Sarah, Caroline, Florida, Louisiana, Emily, Claire, Arkansas and Canada. |
| C7 | 234 | 1,021 / 1,326 | 14.39 | -0.03051 | Monarchy, bureaucracy, religion, family and political/mythic roles coexist: emperor, bureaucracy, palace, chapel, grandmother, church, Americans, mother, warriors, cathedral, Sultan and king. |
| C8 | 218 | 932 / 1,060 | 13.41 | -0.02980 | Cardiovascular disease, cytokine biology and biomedical pathology are coherent: cardiovascular, cytokines, cytokine, staphylococcus fragments, interleukin, lipids, monocyte, gluc-, sclerosis fragments, lymphocyte and atherosclerotic. |
| C9 | 113 | 645 / 289 | 13.97 | -0.02924 | Numeric strings, especially historical years, dominate. |
| C10 | 110 | 346 / 683 | 12.50 | -0.03162 | Uppercase lexical stems, modal/status terms and code-like fragments dominate: CE, ERS, ABLE, NEVER, ACK, THIS, UAL, SOME, OW, ENTS and doesnt. |

## Population accounting

### Positive head

Total nodes: **2,706**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,057 | 39.1% |
| Formal/name substrate | 1,186 | 43.8% |
| Irreducible semantic | 463 | 17.1% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,706** | **100.0%** |

Semantic-eligible denominator: **1,520 nodes**.

### Negative tail

Total nodes: **3,155**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,640 | 52.0% |
| Formal/name substrate | 1,026 | 32.5% |
| Irreducible semantic | 489 | 15.5% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,155** | **100.0%** |

Semantic-eligible denominator: **2,129 nodes**.

## Positive-side reconstruction

### P+0 — Exploratory measurement and evolving system dynamics

- **Primary children:** C2, C3
- **Primary nodes:** 638
- **Side-relative coverage:** 23.6%
- **Semantic-eligible coverage:** 42.0%
- **Confidence:** High

**Evidence.** C2 contains exploration, measurement, characterisation,
quantification, motivation, anticipation and developmental process. C3 contains
interactions, evolution, emergence, phenomenological/system language and
renormalisation, with reappearance/inevitability stems around that core. Their
direct relation contains **408 token edges**, mean cosine **0.09720**. The
common generator is evolving system investigation: systems or situations are
explored, measured, characterised and motivated while their interactions,
emergence and evolution are represented dynamically.

**Secondary links:** C5 and C9. C2–C5 has **358 edges**, C3–C5 **223**;
C2–C9 **147**, C3–C9 **120**. Social/professional activity and
temporal/evaluative descriptors surround the process architecture without
becoming core children.

**Exclusion boundary.** C2 is investigative/developmental and C3 is
interaction/evolution oriented. C5 includes food, travel and commercial
material as well as professional activity; C9 is primarily a modifier domain.

**Alternative.** Expand P+0 with C5 under a broader
`development, interaction and professional activity` parent. Rejected because
C5's travel/food/commercial content materially exceeds the shared process
structure.

### P+1 — Mediated social/creative activity and interface systems

- **Primary children:** C5, C7
- **Primary nodes:** 419
- **Side-relative coverage:** 15.5%
- **Semantic-eligible coverage:** 27.6%
- **Confidence:** Moderate

**Evidence.** C5 contains sessions, entrepreneurs, filmmakers, interventions,
conversations, shops, negotiation, travel, animation and business. C7 contains
photography, social/media platforms, Netflix, notifications, browsers, sessions,
addresses and layout/interface concepts. Their direct relation contains **164
token edges**, mean cosine **0.08995**. The shared generator is mediated
social/creative/professional activity: communication, content production and
commercial/professional interaction occur through media and interface systems.

**Secondary link:** P+0. C2–C5 has **358 edges**, C3–C5 **223**, C2–C7 **152**
and C3–C7 **107**. Mediated activity strongly supports the exploratory/system
parent without becoming identical to it.

**Exclusion boundary.** C5 includes food/travel/commercial terms beyond media,
while C7 includes size/layout concepts beyond software. The parent therefore
remains Moderate rather than being broadened to generic “information activity”.

**Alternative.** Leave C5 and C7 separate. This remains a serious alternative
because both communities retain internal heterogeneity.

### Positive irreducible structures

- **C4 — irreducible-semantic:** biomedical, psychiatric, immunological and
  pharmacological terminology; secondary relation to P+0 through C2–C4
  (**191 edges**) and C3–C4 (**298**).
- **C9 — irreducible-semantic:** temporal/freshness/analytical/evaluative
  descriptors; secondary relation to P+0.
- **C10 — irreducible-semantic:** affect, consciousness, sleep, compassion and
  bodily/social actions. Its relation to C4 is meaningful (**90 edges**, mean
  cosine **0.09727**) but insufficient for a separate parent without
  over-compression.

### Positive formal/name substrate

- C0 — personal names/geographic entities
- C1 — grammar/function words/fragments
- C6 — mathematical/code punctuation and formatting
- C8 — numeric strings/coded values
- C11 — example-related multilingual morphology

## Negative-side reconstruction

### P-0 — Administrative/regulatory characterisation, adverse evaluation and controlled change

- **Primary children:** C0, C3, C4
- **Primary nodes:** 1,160
- **Side-relative coverage:** 36.8%
- **Semantic-eligible coverage:** 54.5%
- **Confidence:** High

**Evidence.** C0 contains administrative characterisation, recommendations,
regulation and constitutional concepts. C3 contains downregulation, removal,
encouragement, prohibition and verification/change actions. C4 contains
negative/intense evaluation, catastrophe and discrimination. The structure is
strongly triangulated: C0–C3 has **576 token edges**, mean cosine **0.10264**;
C0–C4 **419** at **0.10214**; C3–C4 **304** at **0.09798**. The common
generator is organised state judgement and control: systems are characterised
and regulated, evaluated as adverse or unacceptable, then encouraged,
prohibited, removed, verified or otherwise changed.

**Secondary links:** C8 and P-1. C0–C8 has **267 edges**, linking pathology to
state characterisation. C0–C7 has **330**, placing institutional authority
close to the control architecture without requiring primary absorption.

**Exclusion boundary.** C0 contains neutral administration and
characterisation, C3 is action/change oriented, and C4 is evaluative/intensity
oriented. The parent cannot be reduced to regulation, negative evaluation or
change alone.

**Alternative.** Restrict P-0 to C0+C3 and leave C4 irreducible. This preserves
a cleaner administration/control parent, but C4's strong relation to both
branches supports its inclusion.

### P-1 — Civic/territorial authority and social order

- **Primary children:** C6, C7
- **Primary nodes:** 480
- **Side-relative coverage:** 15.2%
- **Semantic-eligible coverage:** 22.5%
- **Confidence:** Moderate / High

**Evidence.** C6 contains personal names plus geographic regions; C7 contains
monarchy, bureaucracy, religion, family and political/mythic roles. Their
direct relation contains **227 token edges**, mean cosine **0.09622**. The
common generator is social and civic order situated within territorial
identity.

**Secondary link:** C5. C5–C7 has **227 edges** and C5–C6 **172**, showing that
roads, vehicles and material environments strongly contextualise civic and
social structures without themselves being authority/territory.

**Exclusion boundary.** C6 is entity/territory-centred; C7 is role/authority
centred. C5 is a material environment, not civic order itself.

**Alternative.** Include C5 as a third child under a broader
`civic/territorial and material-public environment` parent. Rejected because
the physical-world community remains discriminable and would make the parent
too broad.

### Negative irreducible structures

- **C5 — irreducible-semantic:** vehicles, roads, built environment and
  material/household objects; secondary relation to P-1 and P-0.
- **C8 — irreducible-semantic:** cardiovascular/cytokine biomedical pathology;
  secondary relation to P-0.

### Negative formal/name substrate

- C1 — grammar/function words with multilingual/token fragments
- C2 — short name-like and technical/code abbreviations
- C9 — numeric strings/years
- C10 — uppercase lexical/status/code fragments

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 435 | Names/cities/geography | formal-substrate | — | Entity-form organisation. |
| + | C1 | 345 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C2 | 340 | Exploration/measurement/characterisation/motivation | parent:P+0 | — | Investigative/developmental child. |
| + | C3 | 298 | Interaction/evolution/emergence/theoretical systems | parent:P+0 | — | Dynamic-system child. |
| + | C4 | 276 | Biomedical/psychiatric/immunological/pharmacological | irreducible-semantic | P+0 | Distinct clinical/biological domain. |
| + | C5 | 247 | Social/professional/creative/commercial + food/travel | parent:P+1 | P+0 | Mediated activity child with heterogeneity explicit. |
| + | C6 | 246 | Maths/code punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C7 | 172 | Media/software/interface + layout concepts | parent:P+1 | P+0 | Interface/media child with layout spillover. |
| + | C8 | 124 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| + | C9 | 118 | Temporal/freshness/analytical/evaluative descriptors | irreducible-semantic | P+0 | Contextual/modifier relation. |
| + | C10 | 69 | Affect/consciousness/sleep/compassion/body actions | irreducible-semantic | C4 | Subjective/embodied-state domain. |
| + | C11 | 36 | Example-related multilingual morphology | formal-substrate | — | Lexical/morphological organisation. |
| − | C0 | 580 | Administrative/regulatory/constitutional characterisation | parent:P-0 | — | Characterisation/control hub. |
| − | C1 | 407 | Grammar/function + multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C2 | 396 | Short name-like + technical/code abbreviations | formal-substrate | — | Form/abbreviation organisation dominates. |
| − | C3 | 303 | Downregulation/removal/prohibition/change | parent:P-0 | — | Controlled-change child. |
| − | C4 | 277 | Negative/intense evaluation/catastrophe/discrimination | parent:P-0 | — | Adverse-evaluation child. |
| − | C5 | 271 | Vehicles/roads/built/material objects | irreducible-semantic | P-1, P-0 | Material-setting relation. |
| − | C6 | 246 | Names + geographic entities/regions | parent:P-1 | — | Territorial/entity child. |
| − | C7 | 234 | Monarchy/bureaucracy/religion/family/political roles | parent:P-1 | P-0 | Authority/social-order child. |
| − | C8 | 218 | Cardiovascular/cytokine pathology | irreducible-semantic | P-0 | Clinical-state relation. |
| − | C9 | 113 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 110 | Uppercase lexical/status/code fragments | formal-substrate | — | Lexical/code form dominates. |

Every State 21 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Exploratory measurement and evolving system dynamics | C2, C3 | 638 | 23.6% | 42.0% | High |
| P+1 | Mediated social/creative activity and interface systems | C5, C7 | 419 | 15.5% | 27.6% | Moderate |
| P-0 | Administrative/regulatory characterisation, adverse evaluation and controlled change | C0, C3, C4 | 1,160 | 36.8% | 54.5% | High |
| P-1 | Civic/territorial authority and social order | C6, C7 | 480 | 15.2% | 22.5% | Moderate / High |

Positive retained parents account for **1,057 nodes**, **39.1% of the positive
population** and **69.5% of semantic-eligible positive nodes**.

Negative retained parents account for **1,640 nodes**, **52.0% of the negative
population** and **77.0% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — system development and mediated activity — High.**
   C2–C5 has **358 edges**, C3–C5 **223**, C2–C7 **152** and C3–C7 **107**.
   Social/creative/interface activity is strongly coupled to exploratory system
   processes without becoming the same generator.

2. **P+0 ↔ C4 — dynamic process and biomedical relation — High.**
   C2–C4 has **191 edges** and C3–C4 **298**. Biomedical states are strongly
   embedded in process/evolution structure while retaining an independent
   medical ontology.

3. **P+0 ↔ C9 — temporal/evaluative modification — Moderate.**
   C2–C9 has **147 edges** and C3–C9 **120**. C9 acts as a contextual/modifier
   layer around substantive process structure.

4. **C4 ↔ C10 — clinical and subjective embodied state — Moderate.**
   Their direct relation has **90 edges**, mean cosine **0.09727**. This is
   meaningful but insufficient to justify another parent without forcing a
   small subjective-state community into medicine.

### Negative-side relations

1. **P-0 ↔ P-1 — control architecture in civic/authority context — High.**
   C0–C7 has **330 edges**, C3–C7 **92**, C4–C7 **151**, C0–C6 **148** and
   C4–C6 **63**. Regulatory/evaluative/control semantics are strongly situated
   within authority and territorial structures.

2. **P-0 ↔ C8 — control/characterisation and clinical pathology — High.**
   C0–C8 has **267 edges**, C3–C8 **58** and C4–C8 **86**. Pathological states
   are strongly adjacent to state characterisation and judgement while
   remaining a distinct medical ontology.

3. **P-1 ↔ C5 — civic/social order and material setting — High.**
   C5–C7 has **227 edges**, C5–C6 **172**. Physical environments contextualise
   authority and territory without being absorbed into the parent.

4. **C5 also connects to P-0 through state characterisation.**
   C0–C5 has **357 edges**, showing that material environments participate in
   the broader state-description field even though their semantic identity
   remains physical/material.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 21 cross-side evidence is dominated by near-form relations:
`Greek`↔` Greek`, adjacent years, `transmit`↔`transmitting`,
`height`↔`Height`, and `raised`↔`raising`. These do not establish a
parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C4 and negative C8 through biomedical/pathological structure;
- positive C0 and negative P-1 through geographic/entity organisation.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,186 nodes / 43.8%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation and formatting;
- numeric strings;
- example-related multilingual morphology.

### Negative — 1,026 nodes / 32.5%

- grammar/function words with multilingual/token fragments;
- short name-like and technical/code abbreviations;
- numeric strings;
- uppercase lexical/status/code fragments.

## Minimal state-level architecture

```text
STATE 21 — BLOCK 20 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 EXPLORATORY MEASUREMENT & EVOLVING SYSTEM DYNAMICS
|   +-- C2 exploration/measurement/characterisation/motivation
|   `-- C3 interaction/evolution/emergence/theoretical systems
|       |
|       +-- C4 biomedical/clinical                     [secondary]
|       `-- C9 temporal/evaluative descriptors        [secondary]
|
+-- P+1 MEDIATED SOCIAL/CREATIVE ACTIVITY & INTERFACE SYSTEMS
|   +-- C5 social/professional/creative/commercial activity
|   `-- C7 media/software/interface + layout concepts
|
+-- C4 biomedical/psychiatric/immunological/pharmacological [irreducible]
+-- C9 temporal/freshness/analytical/evaluative descriptors [irreducible]
+-- C10 affect/consciousness/sleep/compassion/body actions  [irreducible]
`-- C0,C1,C6,C8,C11                                  [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADMINISTRATIVE/REGULATORY CHARACTERISATION / ADVERSE EVALUATION / CONTROLLED CHANGE
|   +-- C0 administrative/regulatory/constitutional characterisation
|   +-- C3 downregulation/removal/prohibition/change
|   `-- C4 adverse/intense evaluation/catastrophe/discrimination
|       \
|        -- C8 cardiovascular/cytokine pathology      [secondary]
|
+-- P-1 CIVIC/TERRITORIAL AUTHORITY & SOCIAL ORDER
|   +-- C6 names/geographic entities/regions
|   `-- C7 monarchy/bureaucracy/religion/family/political roles
|       \
|        -- C5 vehicles/roads/material setting        [secondary]
|
+-- C5 vehicles/roads/built/material objects            [irreducible]
+-- C8 cardiovascular/cytokine pathology                [irreducible]
`-- C1,C2,C9,C10                                      [formal/name substrate]
```

The preferred State 21 reconstruction contains two positive and two negative
multi-community parents. The positive side separates evolving exploratory
system processes from mediated social/creative/interface activity. The negative
side is dominated by a strongly triangulated administrative/regulatory,
adverse-evaluation and controlled-change architecture, with civic/territorial
authority retained as a distinct parent.

This statement is local to State 21 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C5 into P+0 under a broader development/professional-activity
   parent;
2. leave positive C5 and C7 separate rather than retaining P+1;
3. restrict negative P-0 to C0+C3 and leave C4 irreducible;
4. absorb negative C5 into P-1 as a material-setting child.

The third alternative is the most serious semantically. The preferred P-0 is
retained because C0–C3, C0–C4 and C3–C4 form strong three-way evidence rather
than a single incidental relation.

## Uncertainty record

- **Positive P+1:** both children are internally heterogeneous; confidence is
  Moderate.
- **Positive C4:** strongly connected to P+0 but remains a distinct biomedical
  ontology.
- **Positive C10:** subjective/embodied-state semantics are coherent but small;
  no parent is manufactured from semantic similarity alone.
- **Negative P-0:** broad, but three-way graph support is strong and its child
  functions remain discriminable.
- **Negative P-1:** C6 combines personal names and geography while C7 combines
  formal and mythic/social authority; confidence remains Moderate/High.
- **Negative C5:** material-setting semantics connect strongly to both P-0 and
  P-1, but remain irreducible.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **11 / 11**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,706 / 2,706**
- Negative node accounting: **3,155 / 3,155**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 21 community inspected at underlying R008 community-record level: **yes**
- All State 21 within-side community relations inspected: **yes**
- State 21 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 21 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 21 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
