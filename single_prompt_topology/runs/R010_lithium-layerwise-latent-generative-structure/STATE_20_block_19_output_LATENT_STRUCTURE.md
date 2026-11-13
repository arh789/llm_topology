# R010 State 20 — Block 19 output latent structure

## State identity

- R010 state index: `20`
- R008/R009 state: `block_19_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 11 negative-tail = 23**
- R008 population: **2,727 positive-head + 2,948 negative-tail = 5,675 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 20 only. Retrieval and graph inspection were
restricted to `state_index=20 / block_19_output`. No later-state evidence was
used.

## Evidence inventory

For every State 20 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_20_block_19_output.md`;
2. all 23 State 20 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 20 within-side relation set in
   `R008/community_edges.csv`;
4. the State 20 section of `chatgpt_layer_packets.md`, including compact
   cross-side relations.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained
with explicit uncertainty rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 369 | 1,515 / 1,668 | 12.73 | +0.03236 | Personal names, cities and geographic/name-like entities dominate: Manchester, Scott, Matt, Peter, Mitchell, Kashmir, Karen, Hamburg and Krish; terrorists and fishermen are semantic outliers. |
| C1 | 356 | 1,613 / 1,942 | 14.52 | +0.03162 | Common grammatical/function words and lexical fragments dominate. |
| C2 | 285 | 1,074 / 1,547 | 12.96 | +0.03239 | Film/media production, photography, animation and online-platform systems dominate: filmmakers, filmmaker, Bitmap, photography, Netflix, Notification, filming, Animation, facebook, Learning, writers and Play. |
| C3 | 275 | 1,021 / 1,650 | 13.43 | +0.03237 | Exploration, entrepreneurship, motivation and emerging/developmental activity dominate: exploring, entrepreneurs, motivations, motivation, happiness, anticipated, explores, discuss, yields, emerging, business and modulates. |
| C4 | 263 | 946 / 1,647 | 13.46 | +0.03238 | Biomedical, psychiatric, hospital and pharmacological terminology is coherent: breastfeeding, psychiatry fragments, hospital fragments, Sleep, dexamethasone, biomedical fragments, Medical, tumorigenesis and dopaminergic. |
| C5 | 245 | 1,386 / 644 | 13.94 | +0.03342 | Mathematical/code punctuation and symbolic formatting dominate; 181 of 245 tokens are punctuation/symbols. |
| C6 | 221 | 704 / 1,447 | 12.92 | +0.03239 | Prefix/stem families around emergence, freshness, reappearance and negotiation dominate; incomplete lexical form is the stronger organising principle. |
| C7 | 186 | 705 / 1,335 | 14.76 | +0.03289 | Interactions, measurements, quantification and system dynamics dominate: interactions, Measurements, characterizing, Measurement, evolves, quantification, recorded, imaging, dynamics, simulations, develops and evolving. |
| C8 | 142 | 483 / 1,016 | 13.96 | +0.03210 | Social/professional interaction coexists with food, retail and travel/leisure: Food, conversations, sessions, negotiating, interventions, interviews, adventures, shoppers, discussions, workshops and interviewing. |
| C9 | 138 | 520 / 825 | 13.51 | +0.03142 | Discourse, temporal and comparative physical descriptors dominate: surprisingly, size, Recently, Clearly, Fall, larger, Next, widths, spacing, Now and older. |
| C10 | 126 | 472 / 650 | 12.65 | +0.03302 | Example-related multilingual words and morphological fragments dominate. |
| C11 | 121 | 713 / 265 | 13.98 | +0.03143 | Numeric strings and short coded values dominate. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 577 | 2,632 / 2,637 | 13.69 | -0.03066 | Characterisation, regulation, constitutional constraint and administrative concepts coexist: Characteristics, circumstantial, downregulation, recommendations, unconstitutional, encouragement, Constitution, administrators, Configuration, characteristics and circumstances. |
| C1 | 438 | 1,838 / 1,865 | 12.65 | -0.03102 | Short name-like, technical and multilingual lexical fragments dominate: Gh/GH, Rub, Kh, Rog, Tob, Tah, Bra, LH, discouragement fragments and Arabic/technical forms. |
| C2 | 398 | 1,773 / 1,717 | 13.22 | -0.03103 | Common grammatical/function words and multilingual lexical fragments dominate. |
| C3 | 342 | 1,514 / 1,730 | 13.91 | -0.03161 | Monarchy/religion and family roles coexist with vehicles, built environment and conflict: emperor, trucks, palace, automobiles, warriors, chapel, cathedral, chassis, archaeological, church, grandmother and gravel. |
| C4 | 300 | 1,310 / 1,437 | 13.52 | -0.03010 | Cardiovascular disease, cytokine biology, immunology and pathology are coherent: cardiovascular, macrophage, cytokines, interleukin, atherosclerotic, epidemiological, staphylococcus/sclerosis fragments, erythrocytes and TNF. |
| C5 | 295 | 1,269 / 1,568 | 13.92 | -0.03045 | Negative/intense evaluation, catastrophe and contradiction dominate: incredible, stupid, occasionally, disastrous, unbelievable, brutal, frightening, spectacular, contradictory and Sometimes. |
| C6 | 243 | 1,173 / 1,177 | 14.50 | -0.03085 | Personal names and geographic entities/regions coexist: Sarah, Laura, Caroline, Emily, Florida, Alabama, Louisiana, Connie, Mexico and Jess; extremes add Illinois, Canada and Africans. |
| C7 | 171 | 661 / 1,007 | 13.62 | -0.03049 | Encouragement, prohibition, removal, activation and verification/change actions dominate: encourages, prohibiting, removing, resembled, Delete, prohibited, activates, verifying, created, received, creates and prohibits. |
| C8 | 95 | 549 / 223 | 13.91 | -0.02947 | Numeric strings, especially historical years, dominate. |
| C9 | 60 | 233 / 229 | 11.58 | -0.02981 | Mathematical/code punctuation and symbol formatting dominate; 51 of 60 tokens are punctuation/symbols. |
| C10 | 29 | 85 / 186 | 12.28 | -0.03207 | Rail transport and developer/software tooling coexist: Rails, rails, Rail, Railroad and Steam with SSH, CLI, Ruby, Git, Unix and utils. |

## Population accounting

### Positive head

Total nodes: **2,727**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 888 | 32.6% |
| Formal/name substrate | 1,438 | 52.7% |
| Irreducible semantic | 401 | 14.7% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,727** | **100.0%** |

Semantic-eligible denominator: **1,289 nodes**.

### Negative tail

Total nodes: **2,948**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,628 | 55.2% |
| Formal/name substrate | 991 | 33.6% |
| Irreducible semantic | 300 | 10.2% |
| Mixed unresolved | 29 | 1.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,948** | **100.0%** |

Semantic-eligible denominator: **1,957 nodes**.

## Positive-side reconstruction

### P+0 — Goal-directed development and quantitative system dynamics

- **Primary children:** C3, C7
- **Primary nodes:** 461
- **Side-relative coverage:** 16.9%
- **Semantic-eligible coverage:** 35.8%
- **Confidence:** High

**Evidence.** C3 contains exploration, entrepreneurship, motivation,
anticipation, emergence and development. C7 contains interactions,
measurements, characterisation, quantification, imaging, dynamics and
simulation. Their direct relation contains **265 token edges**, mean cosine
**0.09803**, the strongest clearly semantic positive relation not dominated by
formal structure. The common generator is goal-directed system development:
systems or situations are explored, motivated and developed, then measured,
characterised and analysed through their dynamics and interactions.

**Secondary links:** C8 and C9. C3–C8 has **192 edges**, C7–C8 **126**;
C3–C9 **133**, C7–C9 **77**. Social/professional activity and contextual
comparative descriptors surround the core process without becoming primary
children.

**Exclusion boundary.** C3 is motivational/developmental; C7 is
measurement/system-dynamics oriented. C8 contains food/retail/travel material
in addition to professional interaction. C9 is modifier/descriptive rather
than a substantive generating domain.

**Alternative.** Include C8 as a third child under a broader
`development, interaction and professional activity` parent. Rejected because
C8's food, retail and leisure content materially broadens the child beyond the
shared process relation.

### P+1 — Mediated creative and professional activity

- **Primary children:** C2, C8
- **Primary nodes:** 427
- **Side-relative coverage:** 15.7%
- **Semantic-eligible coverage:** 33.1%
- **Confidence:** Moderate

**Evidence.** C2 contains filmmaking, photography, animation, online platforms,
learning and writing. C8 contains conversations, sessions, negotiating,
interventions, interviews, workshops and interviewing, plus food/retail/travel
material. Their direct relation contains **190 token edges**, mean cosine
**0.09596**. The shared generator is mediated professional/social activity:
content production, communication, interviewing and collaborative work occur
through media and platform contexts.

**Secondary link:** P+0. C2–C3 has **181 edges**, C2–C7 **169**, while C8–C3
has **192** and C8–C7 **126**. Creative/professional activity is strongly
connected to developmental and analytical processes.

**Exclusion boundary.** C2 is media/platform oriented. C8 is socially and
professionally active but also contains food/retail/travel concepts. The parent
is therefore kept Moderate and is not broadened to generic “social activity”.

**Alternative.** Leave C8 irreducible or mixed-unresolved and retain C2 alone.
This is a serious alternative because C8 is heterogeneous.

### Positive irreducible structures

- **C4 — irreducible-semantic:** biomedical, psychiatric, hospital and
  pharmacological terminology; strong secondary relation to P+0 through
  C3–C4 (**188 edges**) and C7–C4 (**214**).
- **C9 — irreducible-semantic:** discourse, temporal and comparative physical
  descriptors; secondary relation to P+0.

### Positive formal/name substrate

- C0 — personal names/geographic entities
- C1 — grammar/function words/fragments
- C5 — mathematical/code punctuation and formatting
- C6 — emergence/freshness/reappearance lexical stems
- C10 — example-related multilingual morphology
- C11 — numeric strings/coded values

## Negative-side reconstruction

### P-0 — Characterisation, adverse judgement and institutional change

- **Primary children:** C0, C5, C7
- **Primary nodes:** 1,043
- **Side-relative coverage:** 35.4%
- **Semantic-eligible coverage:** 53.3%
- **Confidence:** High

**Evidence.** C0 contains characterisation, regulation, constitutional
constraint and administrative concepts. C5 contains negative/intense
evaluation, catastrophe and contradiction. C7 contains encouragement,
prohibition, removal, activation, verification and change actions. C0 is the
hub: C0–C5 has **470 token edges**, mean cosine **0.09977**; C0–C7 **435** at
**0.10305**; C5–C7 **224** at **0.09625**. The common generator is organised
state judgement and intervention: systems are characterised and constrained,
evaluated as adverse or contradictory, then encouraged, prohibited, removed,
activated, verified or otherwise changed.

**Secondary links:** C4 and P-1. C0–C4 has **407 edges** and C5–C4 **124**,
placing pathology adjacent to state characterisation and adverse evaluation.
C0–C3 has **455 edges**, linking the parent strongly to institutional/material
contexts without requiring primary absorption.

**Exclusion boundary.** C0 contains neutral administrative description as well
as constraint. C5 is evaluative/intensity-heavy. C7 is action/change-oriented.
The parent cannot be reduced to regulation, negative evaluation or
transformation alone.

**Alternative.** Restrict P-0 to C0+C7 and leave C5 irreducible. This preserves
a cleaner control/intervention parent, but C5's strong relations to both
children support its inclusion as an adverse-judgement branch.

### P-1 — Institutional/territorial and material-public environment

- **Primary children:** C3, C6
- **Primary nodes:** 585
- **Side-relative coverage:** 19.8%
- **Semantic-eligible coverage:** 29.9%
- **Confidence:** Moderate / High

**Evidence.** C3 contains monarchy, religion, family roles, vehicles,
built-environment and conflict material. C6 contains personal names,
geographic entities and regions. Their direct relation contains **296 token
edges**, mean cosine **0.09977**, one of the strongest semantic negative
relations outside P-0. The common generator is a public/institutional
environment: authority and family/social roles, territorial identities and
their material settings are represented together.

**Secondary link:** P-0. C0–C3 has **455 edges**, C5–C3 **224** and C7–C3
**70**. Institutional/material environments strongly contextualise adverse
judgement and intervention.

**Exclusion boundary.** C3 is internally broad, spanning roles, buildings,
vehicles and conflict; C6 is entity/territory oriented. The parent is not
broadened to generic “human world” and does not absorb pathology or technical
form communities.

**Alternative.** Leave C3 and C6 separate. This remains a serious alternative
because C3 is itself mixed; confidence is therefore Moderate/High rather than
unqualified High.

### Negative irreducible and unresolved structures

- **C4 — irreducible-semantic:** cardiovascular/cytokine/immunological
  pathology; secondary relation to P-0.
- **C10 — mixed-unresolved:** rail transport and software/developer tooling
  coexist without a single explanatory parent.

### Negative formal/name substrate

- C1 — short technical/name-like/multilingual lexical fragments
- C2 — grammar/function words and multilingual fragments
- C8 — numeric strings/years
- C9 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 369 | Names/cities/geography | formal-substrate | — | Entity-form organisation. |
| + | C1 | 356 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C2 | 285 | Film/media/photography/animation/platforms | parent:P+1 | P+0 | Mediated creative/professional child. |
| + | C3 | 275 | Exploration/entrepreneurship/motivation/development | parent:P+0 | P+1 | Developmental/motivational child. |
| + | C4 | 263 | Biomedical/psychiatric/hospital/pharmacology | irreducible-semantic | P+0 | Distinct clinical domain. |
| + | C5 | 245 | Maths/code punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C6 | 221 | Emergence/freshness/reappearance stems | formal-substrate | — | Lexical/morphological form dominates. |
| + | C7 | 186 | Interaction/measurement/quantification/dynamics | parent:P+0 | P+1 | Analytical/system-dynamics child. |
| + | C8 | 142 | Social/professional + food/retail/travel | parent:P+1 | P+0 | Professional/social activity retained with heterogeneity explicit. |
| + | C9 | 138 | Discourse/temporal/comparative descriptors | irreducible-semantic | P+0 | Contextual/modifier relation. |
| + | C10 | 126 | Example-related multilingual morphology | formal-substrate | — | Lexical/morphological organisation. |
| + | C11 | 121 | Numeric strings/codes | formal-substrate | — | Numeric form. |
| − | C0 | 577 | Characterisation/regulation/constitutional/admin | parent:P-0 | P-1 | Characterisation/control hub. |
| − | C1 | 438 | Short technical/name-like/multilingual fragments | formal-substrate | — | Lexical/form organisation dominates. |
| − | C2 | 398 | Grammar/function/multilingual fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C3 | 342 | Monarchy/religion/family + vehicles/built/conflict | parent:P-1 | P-0 | Institutional/material-public child. |
| − | C4 | 300 | Cardiovascular/cytokine/immunology/pathology | irreducible-semantic | P-0 | Clinical-state relation. |
| − | C5 | 295 | Negative/intense evaluation/catastrophe | parent:P-0 | — | Adverse-judgement child. |
| − | C6 | 243 | Personal names + geographic entities/regions | parent:P-1 | — | Territorial/entity child. |
| − | C7 | 171 | Encouragement/prohibition/removal/activation/change | parent:P-0 | — | Intervention/change child. |
| − | C8 | 95 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 60 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C10 | 29 | Rail transport + developer/software tooling | mixed-unresolved | — | Two organising domains coexist. |

Every State 20 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Goal-directed development and quantitative system dynamics | C3, C7 | 461 | 16.9% | 35.8% | High |
| P+1 | Mediated creative and professional activity | C2, C8 | 427 | 15.7% | 33.1% | Moderate |
| P-0 | Characterisation, adverse judgement and institutional change | C0, C5, C7 | 1,043 | 35.4% | 53.3% | High |
| P-1 | Institutional/territorial and material-public environment | C3, C6 | 585 | 19.8% | 29.9% | Moderate / High |

Positive retained parents account for **888 nodes**, **32.6% of the positive
population** and **68.9% of semantic-eligible positive nodes**.

Negative retained parents account for **1,628 nodes**, **55.2% of the negative
population** and **83.2% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — development/analysis and mediated professional activity — High.**
   C3–C2 has **181 edges**, C7–C2 **169**, C3–C8 **192** and C7–C8 **126**.
   Creative/professional activity is strongly coupled to developmental and
   analytical processes without becoming the same generator.

2. **P+0 ↔ C4 — developmental/analytical and biomedical relation — High.**
   C3–C4 has **188 edges** and C7–C4 **214**. Biomedical states are strongly
   embedded in process/measurement structure but retain a distinct clinical
   ontology.

3. **P+0 ↔ C9 — process and contextual comparison — Moderate.**
   C3–C9 has **133 edges** and C7–C9 **77**. Temporal/comparative language acts
   as a modifier around the substantive process architecture.

4. **P+1 ↔ C4 — mediated activity and health context — Moderate.**
   C2–C4 has **166 edges**, C8–C4 **139**. Health/medical content contextualises
   professional/media activity without defining its parent.

### Negative-side relations

1. **P-0 ↔ P-1 — state judgement/intervention in institutional-material context — High.**
   C0–C3 has **455 edges**, C5–C3 **224**, C7–C3 **70**, while C0–C6 has
   **185**. The parent is strongly situated in authority, territorial and
   material settings.

2. **P-0 ↔ C4 — state characterisation and clinical pathology — High.**
   C0–C4 has **407 edges**, C5–C4 **124** and C7–C4 **48**. Pathology is
   strongly adjacent to characterisation/judgement while remaining a medical
   ontology.

3. **P-1 is a heterogeneous environment parent rather than a flat topic.**
   C3–C6 has **296 edges**, mean cosine **0.09977**. C3 contributes authority,
   material and conflict settings; C6 contributes territorial and entity
   identity.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 20 cross-side evidence is dominated by near-form relations:
`Greek`↔` Greek`, `transmit`↔`transmitting`,
`height`↔`Height`, `raised`↔`raising`, and matching delimiter forms.
These do not establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative P-0 through characterisation/change;
- positive C4 and negative C4 through biomedical/pathological structure;
- positive C0 and negative P-1 through geographic/entity organisation.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,438 nodes / 52.7%

- personal names/geographic entities;
- grammar/function words and fragments;
- mathematical/code punctuation and formatting;
- emergence/freshness/reappearance lexical stems;
- example-related multilingual morphology;
- numeric strings.

### Negative — 991 nodes / 33.6%

- short technical/name-like/multilingual lexical fragments;
- grammar/function words and multilingual fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 20 — BLOCK 19 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 GOAL-DIRECTED DEVELOPMENT & QUANTITATIVE SYSTEM DYNAMICS
|   +-- C3 exploration/entrepreneurship/motivation/development
|   `-- C7 interaction/measurement/quantification/dynamics
|       |
|       +-- C4 biomedical/clinical                       [secondary]
|       `-- C9 discourse/temporal/comparative          [secondary]
|
+-- P+1 MEDIATED CREATIVE & PROFESSIONAL ACTIVITY
|   +-- C2 film/media/photography/animation/platforms
|   `-- C8 social/professional interaction + mixed lifestyle
|
+-- C4 biomedical/psychiatric/hospital/pharmacology     [irreducible]
+-- C9 discourse/temporal/comparative descriptors       [irreducible]
`-- C0,C1,C5,C6,C10,C11                                [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 CHARACTERISATION / ADVERSE JUDGEMENT / INSTITUTIONAL CHANGE
|   +-- C0 characterisation/regulation/constitutional/admin
|   +-- C5 negative/intense evaluation/catastrophe
|   `-- C7 encouragement/prohibition/removal/change
|       \
|        -- C4 cardiovascular/cytokine pathology       [secondary]
|
+-- P-1 INSTITUTIONAL/TERRITORIAL & MATERIAL-PUBLIC ENVIRONMENT
|   +-- C3 monarchy/religion/family + vehicles/built/conflict
|   `-- C6 personal names/geographic entities/regions
|
+-- C4 cardiovascular/cytokine/immunology/pathology     [irreducible]
+-- C10 rail transport + developer/software tooling     [mixed unresolved]
`-- C1,C2,C8,C9                                        [formal/name substrate]
```

The preferred State 20 reconstruction contains two positive and two negative
multi-community parents. The positive side separates developmental/quantitative
process from mediated creative/professional activity. The negative side is
highly compressible into a large characterisation/adverse/change parent plus an
institutional/territorial/material environment.

This statement is local to State 20 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. leave positive C8 outside P+1 because its food/retail/travel content is
   heterogeneous;
2. add positive C4 to P+0 under a broader biomedical/process-systems parent;
3. restrict negative P-0 to C0+C7 and leave C5 irreducible;
4. leave negative C3 and C6 separate rather than retaining P-1.

The third and fourth alternatives are the most serious. The preferred
reconstruction retains P-0 because C0–C5, C0–C7 and C5–C7 form strong
three-way support, and retains P-1 because C3–C6 is itself one of the strongest
semantic relations in the negative graph.

## Uncertainty record

- **Positive P+1:** C8 is internally broad across professional interaction,
  food, retail and leisure; confidence remains Moderate.
- **Positive C4:** biomedical semantics are coherent and strongly connected to
  P+0 but lack a second clean medical child.
- **Positive C9:** modifier-like structure is not forced into P+0.
- **Negative P-0:** C0 already mixes characterisation, regulation,
  constitutional and administrative language, but its relations to C5 and C7
  support a higher-order state-judgement architecture.
- **Negative P-1:** C3 is itself mixed across authority, material environment
  and conflict, so the parent remains Moderate/High.
- **Negative C10:** rail and software/developer semantics remain unresolved.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **11 / 11**
- Total communities accounted for: **23 / 23**
- Positive node accounting: **2,727 / 2,727**
- Negative node accounting: **2,948 / 2,948**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 20 community inspected at underlying R008 community-record level: **yes**
- All State 20 within-side community relations inspected: **yes**
- State 20 compact cross-side evidence inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 20 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained with explicit uncertainty: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 20 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
