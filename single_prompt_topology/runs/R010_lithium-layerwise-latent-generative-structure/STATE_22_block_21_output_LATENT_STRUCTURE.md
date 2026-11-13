# R010 State 22 — Block 21 output latent structure

## State identity

- R010 state index: `22`
- R008/R009 state: `block_21_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 12 negative-tail = 23**
- R008 population: **2,787 positive-head + 3,188 negative-tail = 5,975 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 22 only. Retrieval and graph inspection were
restricted to `state_index=22 / block_21_output`. No later-state evidence was
used.

## Evidence inventory

For every State 22 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_22_block_21_output.md`;
2. all 23 State 22 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 22 within-side relation set in
   `R008/community_edges.csv`;
4. the State 22 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained
with explicit uncertainty rather than forced into broader parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 507 | 2,230 / 2,608 | 13.94 | +0.03232 | Exploration, measurement, characterisation and analytical/process activity dominate: exploring, Measurements, characterizing, sessions, interactions, quantification, navigating, Measurement, anticipated, negotiating and recorded. |
| C1 | 413 | 1,572 / 2,043 | 12.56 | +0.03230 | Prefix/stem families around emergence, freshness, avoidance and reappearance dominate; incomplete lexical form is the strongest organising principle. |
| C2 | 345 | 1,565 / 1,844 | 14.42 | +0.03133 | Common grammatical/function words and lexical fragments dominate. |
| C3 | 300 | 1,188 / 1,763 | 13.80 | +0.03222 | Research, entrepreneurship and creative/media activity coexist with travel, shopping and play: Researchers, entrepreneurs, filmmakers, photography, Travel, adventures, Training, Animation, shops and Play. |
| C4 | 252 | 1,122 / 1,139 | 13.42 | +0.03259 | Personal names, cities and geographic entities dominate: Karen, Scott, Matt, Manchester, Peter, Mitchell, Jay, Jake, Kashmir, Pakistan and Derek. |
| C5 | 219 | 1,231 / 562 | 13.81 | +0.03363 | Mathematical/code punctuation and symbolic formatting dominate; 166 of 219 tokens are punctuation/symbols. |
| C6 | 209 | 699 / 1,209 | 12.47 | +0.03246 | Software/interface systems and physical layout/dimension concepts coexist: size, widths, Firefox, Address, browsers, javase, Length, dialog, Notification, spacing, durations and versions. |
| C7 | 184 | 702 / 1,234 | 14.34 | +0.03281 | Biomedical, psychiatric, pharmacological and infant/health terminology is coherent: breastfeeding, Baby, dopaminergic, dexamethasone, psychiatry fragments, Medical, tumorigenesis, hospital fragments and analgesic. |
| C8 | 124 | 468 / 767 | 13.73 | +0.03266 | Example-related morphology coexists with temporal/evaluative/clinical descriptors: surprisingly, exempl-, Recently, ejemplo, Next, examples, Example, clinically, clearer and related forms. |
| C9 | 122 | 736 / 246 | 14.08 | +0.03067 | Numeric strings and short coded values dominate. |
| C10 | 112 | 323 / 809 | 12.99 | +0.03239 | Theoretical-physics/regularisation concepts coexist with regeneration, freshness and change language: renormalization, gravitational, perturbative, phenomenological, regeneration, regularization, Fresh, intuitive, Fast and rings. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 594 | 2,747 / 2,581 | 13.59 | -0.02958 | Removal, encouragement, prohibition, legal constraint and adverse evaluation dominate: removing, encourages, encouragement, unconstitutional, prohibiting, unbelievable, resembled, jurisdictional, disastrous, establishment, discriminatory and stupid. |
| C1 | 525 | 2,243 / 2,639 | 13.57 | -0.02987 | Administrative characterisation, recommendations and configuration systems dominate: Characteristics, recommendations, administrators, characteristics, Specific, Configuration, beneficiaries, Comprehensive, regulations and administrator. |
| C2 | 368 | 1,473 / 1,794 | 12.88 | -0.03024 | Short name-like and technical/code abbreviations dominate: GH, Gh, Bra, Gu, Hu, Kh, TC, Tah, Cl, Rh, Comp and Rog. |
| C3 | 299 | 1,197 / 1,562 | 13.23 | -0.03117 | Vehicles, roads, built environment and material/household objects form a broad physical-world domain: trucks, automobiles, pavement, roads, furniture, gravel, chassis, firearms, terrace, vegetables and cylinder. |
| C4 | 271 | 1,136 / 1,355 | 13.38 | -0.02955 | Cardiovascular disease, cytokine biology, immunology and pathology are coherent: downregulation, cardiovascular, macrophage, cytokines, interleukin, atherosclerotic, lipids, lymphocyte and related pathology. |
| C5 | 256 | 1,048 / 1,513 | 14.10 | -0.02983 | Common grammatical/function words and uppercase lexical fragments dominate. |
| C6 | 225 | 1,097 / 1,136 | 14.80 | -0.03010 | Personal names mixed with geographic entities and regions: Sarah, Laura, Alabama, Caroline, Florida, Louisiana, Emily, Claire, Georgia and Martha. |
| C7 | 219 | 823 / 976 | 11.97 | -0.03028 | Multilingual words, suffixes and orthographic fragments dominate. |
| C8 | 194 | 848 / 1,133 | 14.58 | -0.03077 | Monarchy, government, bureaucracy, religion and family/political roles coexist: emperor, Constitution, chapel, palace, warriors, king, Americans, bureaucracy, church, grandmother and Sultan. |
| C9 | 106 | 589 / 261 | 13.58 | -0.02899 | Numeric strings, especially historical years, dominate. |
| C10 | 81 | 316 / 325 | 11.81 | -0.03013 | Mathematical/code punctuation and symbol formatting dominate; 63 of 81 tokens are punctuation/symbols. |
| C11 | 50 | 192 / 305 | 13.78 | -0.02901 | Frequency, manner, qualification and adverbial degree language is coherent: occasionally, Sometimes, particularly, generally, including, fortunately, successively, effectively and uncommon. |

## Population accounting

### Positive head

Total nodes: **2,787**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 807 | 29.0% |
| Formal/name substrate | 1,351 | 48.5% |
| Irreducible semantic | 393 | 14.1% |
| Mixed unresolved | 236 | 8.5% |
| Unclear | 0 | 0.0% |
| **Total** | **2,787** | **100.0%** |

Semantic-eligible denominator: **1,436 nodes**.

### Negative tail

Total nodes: **3,188**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,538 | 48.2% |
| Formal/name substrate | 1,030 | 32.3% |
| Irreducible semantic | 620 | 19.4% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,188** | **100.0%** |

Semantic-eligible denominator: **2,158 nodes**.

## Positive-side reconstruction

### P+0 — Analytical inquiry and applied research/enterprise activity

- **Primary children:** C0, C3
- **Primary nodes:** 807
- **Side-relative coverage:** 29.0%
- **Semantic-eligible coverage:** 56.2%
- **Confidence:** High / Moderate

**Evidence.** C0 contains exploration, measurement, characterisation,
interactions, quantification, navigation, anticipation and negotiation. C3
contains Researchers, entrepreneurs, filmmakers, photography, travel,
training, animation, shopping and play. Their direct relation is the strongest
positive semantic relation in the state: **541 token edges**, mean cosine
**0.10064**. The common generator is applied inquiry: systems or situations are
explored, measured and characterised through research, enterprise, creative
production and other goal-directed activities.

**Secondary links:** C6, C7 and C10. C0–C6 has **259 edges**, C0–C7 **292**
and C0–C10 **227**. Software/layout systems, biomedical domains and
theoretical/regularisation concepts all connect strongly to the inquiry
architecture without becoming the same child type.

**Exclusion boundary.** C0 is method/process centred. C3 is activity/domain
centred and internally broad across research, enterprise, media, travel and
play. C6 remains a software/interface-layout system; C7 remains biomedical; C10
remains mixed across theoretical physics and regeneration/change.

**Alternative.** Include C6 under a broader
`analytical inquiry and technical systems` parent. Rejected because software,
layout and dimension concepts form an independent technical-interface domain
and do not explain C3's research/enterprise/creative activity.

### Positive irreducible and unresolved structures

- **C6 — irreducible-semantic:** software/interface systems plus
  layout/dimension concepts; strong secondary relation to P+0.
- **C7 — irreducible-semantic:** biomedical, psychiatric, pharmacological and
  infant/health terminology; strong secondary relation to P+0.
- **C8 — mixed-unresolved:** example morphology plus temporal/evaluative/
  clinical descriptors.
- **C10 — mixed-unresolved:** theoretical physics/regularisation plus
  regeneration, freshness and change language; secondary relation to P+0.

### Positive formal/name substrate

- C1 — emergence/freshness/avoidance/reappearance lexical stems
- C2 — grammar/function words and fragments
- C4 — personal names/geographic entities
- C5 — mathematical/code punctuation and formatting
- C9 — numeric strings/coded values

## Negative-side reconstruction

### P-0 — Regulatory/adverse intervention and administrative state characterisation

- **Primary children:** C0, C1
- **Primary nodes:** 1,119
- **Side-relative coverage:** 35.1%
- **Semantic-eligible coverage:** 51.9%
- **Confidence:** High

**Evidence.** C0 contains removal, encouragement, prohibition, legal constraint
and adverse evaluation. C1 contains administrative characterisation,
recommendations, configuration and regulation. Their direct relation contains
**880 token edges**, mean cosine **0.09910**, by far the strongest State 22
semantic intercommunity relation. The common generator is organised state
control: systems or conditions are characterised administratively and then
encouraged, prohibited, removed, constrained, judged or otherwise
intervened upon.

**Secondary links:**
- **C4:** C0–C4 has **217 edges**, C1–C4 **310**, placing pathology and
  downregulation strongly adjacent to state characterisation/control.
- **C8:** C0–C8 has **269 edges**, C1–C8 **223**, linking authority and
  institutional roles to regulatory structure.
- **C11:** C0–C11 has **126 edges**, C1–C11 **78**, positioning
  frequency/qualification language as a modifier around the control structure.

**Exclusion boundary.** C0 combines intervention/action and adverse/legal
evaluation; C1 is primarily descriptive/administrative. C8 is an authority-role
domain, not the control operation itself. C4 remains a distinct medical
ontology.

**Alternative.** Expand P-0 to C0+C1+C8 under a broader
`regulatory administration and authority` parent. Rejected because doing so
would erase the distinction between controlling/configuring a system and the
social/institutional actors represented within it.

### P-1 — Territorial/civic authority and social order

- **Primary children:** C6, C8
- **Primary nodes:** 419
- **Side-relative coverage:** 13.1%
- **Semantic-eligible coverage:** 19.4%
- **Confidence:** Moderate / High

**Evidence.** C6 contains personal names plus geographic regions. C8 contains
monarchy, government, bureaucracy, religion and family/political roles. Their
direct relation contains **211 token edges**, mean cosine **0.10123**, a strong
and semantically discriminative relation. The common generator is social and
civic order situated within territorial identity.

**Secondary link:** C3. C3–C6 has **166 edges** and C3–C8 **176**, showing that
roads, buildings, vehicles and material environments provide physical settings
for territorial and authority structures.

**Exclusion boundary.** C6 is entity/territory-centred; C8 is authority/role
centred. C3 is a material environment, not civic order itself.

**Alternative.** Include C3 as a third child under a broader
`civic/territorial and material-public environment` parent. Rejected because
the material-object community remains clearly discriminable and would make the
parent too broad.

### Negative irreducible structures

- **C3 — irreducible-semantic:** vehicles, roads, built environment and
  material/household objects; secondary relation to P-1.
- **C4 — irreducible-semantic:** cardiovascular/cytokine/immunological
  pathology; secondary relation to P-0.
- **C11 — irreducible-semantic:** frequency, manner and qualification/adverbial
  degree language; modifier relation to P-0.

### Negative formal/name substrate

- C2 — short name-like and technical/code abbreviations
- C5 — grammar/function words and uppercase fragments
- C7 — multilingual lexical/morphological fragments
- C9 — numeric strings/years
- C10 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 507 | Exploration/measurement/characterisation/process | parent:P+0 | — | Analytical inquiry/process child. |
| + | C1 | 413 | Emergence/freshness/avoidance/reappearance stems | formal-substrate | — | Lexical/morphological form dominates. |
| + | C2 | 345 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 300 | Research/enterprise/media + travel/shopping/play | parent:P+0 | — | Applied research/enterprise child with heterogeneity explicit. |
| + | C4 | 252 | Names/cities/geography | formal-substrate | — | Entity-form organisation. |
| + | C5 | 219 | Maths/code punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C6 | 209 | Software/interface + layout/dimension | irreducible-semantic | P+0 | Technical-interface relation. |
| + | C7 | 184 | Biomedical/psychiatric/pharmacological/infant-health | irreducible-semantic | P+0 | Distinct medical/health domain. |
| + | C8 | 124 | Example morphology + temporal/evaluative/clinical | mixed-unresolved | — | Multiple organising principles coexist. |
| + | C9 | 122 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| + | C10 | 112 | Theoretical physics/regularisation + regeneration/change | mixed-unresolved | P+0 | Two semantic structures coexist. |
| − | C0 | 594 | Removal/prohibition/legal constraint/adverse evaluation | parent:P-0 | — | Intervention/adverse-control child. |
| − | C1 | 525 | Administrative characterisation/configuration | parent:P-0 | — | Administrative-description child. |
| − | C2 | 368 | Short name-like + technical/code abbreviations | formal-substrate | — | Abbreviation/form organisation dominates. |
| − | C3 | 299 | Vehicles/roads/built/material objects | irreducible-semantic | P-1 | Material-setting relation. |
| − | C4 | 271 | Cardiovascular/cytokine/immunology/pathology | irreducible-semantic | P-0 | Clinical-state relation. |
| − | C5 | 256 | Grammar/function + uppercase fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C6 | 225 | Names + geographic entities/regions | parent:P-1 | — | Territorial/entity child. |
| − | C7 | 219 | Multilingual words/suffixes/fragments | formal-substrate | — | Morphological/orthographic organisation. |
| − | C8 | 194 | Monarchy/government/bureaucracy/religion/family roles | parent:P-1 | P-0 | Authority/social-order child. |
| − | C9 | 106 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 81 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C11 | 50 | Frequency/manner/qualification/adverbial degree | irreducible-semantic | P-0 | Modifier relation without primary absorption. |

Every State 22 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Analytical inquiry and applied research/enterprise activity | C0, C3 | 807 | 29.0% | 56.2% | High / Moderate |
| P-0 | Regulatory/adverse intervention and administrative state characterisation | C0, C1 | 1,119 | 35.1% | 51.9% | High |
| P-1 | Territorial/civic authority and social order | C6, C8 | 419 | 13.1% | 19.4% | Moderate / High |

Positive retained parents account for **807 nodes**, **29.0% of the positive
population** and **56.2% of semantic-eligible positive nodes**.

Negative retained parents account for **1,538 nodes**, **48.2% of the negative
population** and **71.3% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ C6 — inquiry and technical-interface systems — High.**
   C0–C6 has **259 edges**, mean cosine **0.09692**. Software, interface and
   layout systems strongly support analytical activity while retaining a
   distinct technical identity.

2. **P+0 ↔ C7 — inquiry and biomedical/health structure — High.**
   C0–C7 has **292 edges**, mean cosine **0.09706**, and C3–C7 **234** at
   **0.09735**. Biomedical content is strongly embedded in inquiry and applied
   activity but remains a separate medical ontology.

3. **P+0 ↔ C10 — inquiry and theoretical/change systems — Moderate to High.**
   C0–C10 has **227 edges**, mean cosine **0.09412**, while C3–C10 has **83**.
   The relation is substantial, but C10's theoretical-physics and
   regeneration/change mixture prevents primary absorption.

4. **Formal communities remain highly connected without semantic promotion.**
   C0–C2 has **515 edges** and C0–C1 **384**. High graph connectivity alone
   does not override lexical/formal organisation.

### Negative-side relations

1. **P-0 ↔ P-1 — control architecture in authority/territorial context — High.**
   C0–C8 has **269 edges**, C1–C8 **223**, C0–C6 **120** and C1–C6 **109**.
   Regulatory/administrative control is strongly situated within social,
   political and territorial structures without becoming identical to them.

2. **P-0 ↔ C4 — state control and clinical pathology — High.**
   C0–C4 has **217 edges**, C1–C4 **310**. Pathological states are strongly
   adjacent to administrative/regulatory characterisation but remain a
   distinct medical ontology.

3. **P-1 ↔ C3 — civic/social order and material setting — High.**
   C3–C6 has **166 edges** and C3–C8 **176**. Physical environments contextualise
   territorial and authority structure without being absorbed into the parent.

4. **C11 acts as a qualification satellite around P-0.**
   C0–C11 has **126 edges** and C1–C11 **78**, with especially high mean
   similarity on C1–C11 (**0.10834**).

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 22 cross-side evidence is dominated by near-form relations:
`Greek`↔` Greek`, adjacent years, `transmit`↔`transmitting`,
`height`↔`Height`, and `raised`↔`raising`. These do not establish a
parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/intervention;
- positive C7 and negative C4 through biomedical/pathological structure;
- positive C4 and negative P-1 through geographic/entity organisation.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,351 nodes / 48.5%

- emergence/freshness/avoidance/reappearance lexical stems;
- grammar/function words and fragments;
- personal names/geographic entities;
- mathematical/code punctuation and formatting;
- numeric strings.

### Negative — 1,030 nodes / 32.3%

- short name-like and technical/code abbreviations;
- grammar/function words and uppercase fragments;
- multilingual lexical/morphological fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 22 — BLOCK 21 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ANALYTICAL INQUIRY & APPLIED RESEARCH/ENTERPRISE ACTIVITY
|   +-- C0 exploration/measurement/characterisation/process
|   `-- C3 research/entrepreneurship/media + travel/shopping/play
|       |
|       +-- C6 software/interface/layout systems       [secondary]
|       +-- C7 biomedical/health                       [secondary]
|       `-- C10 theoretical physics + regeneration    [secondary; mixed]
|
+-- C6 software/interface + layout/dimension           [irreducible]
+-- C7 biomedical/psychiatric/pharmacological/health   [irreducible]
+-- C8 example morphology + temporal/evaluative        [mixed unresolved]
+-- C10 theoretical physics + regeneration/change      [mixed unresolved]
`-- C1,C2,C4,C5,C9                                    [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 REGULATORY/ADVERSE INTERVENTION & ADMINISTRATIVE STATE CHARACTERISATION
|   +-- C0 removal/prohibition/legal constraint/adverse evaluation
|   `-- C1 administrative characterisation/configuration
|       |
|       +-- C4 cardiovascular/cytokine pathology      [secondary]
|       `-- C11 frequency/qualification language      [secondary]
|
+-- P-1 TERRITORIAL/CIVIC AUTHORITY & SOCIAL ORDER
|   +-- C6 names/geographic entities/regions
|   `-- C8 monarchy/government/bureaucracy/religion/family roles
|       \
|        -- C3 vehicles/roads/material setting        [secondary]
|
+-- C3 vehicles/roads/built/material objects           [irreducible]
+-- C4 cardiovascular/cytokine/immunology/pathology    [irreducible]
+-- C11 frequency/manner/qualification language        [irreducible]
`-- C2,C5,C7,C9,C10                                   [formal/name substrate]
```

The preferred State 22 reconstruction contains one positive and two negative
multi-community parents. The positive side is dominated by a broad applied
inquiry/research-enterprise structure, while several technical, biomedical and
theoretical communities remain distinct. The negative side is dominated by an
exceptionally strong regulatory/adverse-intervention and administrative
characterisation parent, with civic/territorial authority retained separately.

This statement is local to State 22 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. include positive C6 under P+0 as a technical-system child;
2. leave positive C3 outside P+0 because travel/shopping/play broaden its
   research/enterprise identity;
3. expand negative P-0 to C0+C1+C8 under a broader regulatory-authority parent;
4. include negative C3 under P-1 as a material-setting child.

The second and third alternatives are the most serious. The preferred
reconstruction retains P+0 because C0–C3 is the strongest semantic positive
relation in the state, while keeping P-0 distinct from authority roles because
the **880-edge C0–C1 relation** already provides a much more discriminative
control/configuration structure.

## Uncertainty record

- **Positive P+0:** C3 is heterogeneous across research, enterprise, creative
  work, travel and shopping; confidence is High/Moderate rather than
  unqualified High.
- **Positive C6:** software/interface semantics are coherent but overlap with
  layout and physical-dimension concepts.
- **Positive C8:** example morphology and temporal/evaluative descriptors are
  genuinely mixed.
- **Positive C10:** theoretical physics and regeneration/change language coexist.
- **Negative P-0:** C0 combines adverse evaluation with intervention/action;
  C1 is administrative/descriptive, but their direct relation is exceptionally
  strong.
- **Negative P-1:** C6 mixes personal names and geography while C8 combines
  formal authority, religion and family roles.
- **Negative C11:** coherent but modifier-like and too small to justify a
  separate parent.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,787 / 2,787**
- Negative node accounting: **3,188 / 3,188**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 22 community inspected at underlying R008 community-record level: **yes**
- All State 22 within-side community relations inspected: **yes**
- State 22 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 22 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 22 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
