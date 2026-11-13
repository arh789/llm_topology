# R010 State 13 — Block 12 output latent structure

## State identity

- R010 state index: `13`
- R008/R009 state: `block_12_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 13 negative-tail = 25**
- R008 population: **3,099 positive-head + 3,205 negative-tail = 6,304 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 13 only. Retrieval and graph inspection were
restricted to `state_index=13 / block_12_output`. No later-state evidence was
used.

## Evidence inventory

For every State 13 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_13_block_12_output.md`;
2. all 25 State 13 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 13 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 629 | 2,827 / 2,374 | 12.76 | +0.03114 | Personal/name and geographic material coexist with lexical/tokeniser residue and political/conflict terms. Ken, Karen, Mitchell, Gary and Tony coexist with Coca, remembrance fragments, replacement characters, militant/terrorist material and multilingual fragments. |
| C1 | 503 | 2,219 / 2,547 | 13.89 | +0.03061 | Biomedical/health terminology is substantial: dexamethasone, breastfeeding, dopaminergic, pneumonia fragments, neurotransmitter fragments, Salmonella, antifungal and overweight. Food, telecommunications, motivational and psychosocial language are also material. |
| C2 | 382 | 1,773 / 1,913 | 14.29 | +0.03116 | Common grammatical/function words and short lexical fragments dominate. |
| C3 | 316 | 1,710 / 840 | 13.48 | +0.03109 | Formatting/tokeniser structure dominates: 185 punctuation/symbol tokens, closing delimiters and LaTeX-like forms, with software/paratext tokens such as BytePtrFromString, Acknowledgements, sizeof and getElementById mixed in. |
| C4 | 297 | 1,129 / 1,750 | 13.49 | +0.03193 | Management, conversation, investigation and business/interview activity dominates: management, conversations, investigations, experience, interviews, adventures, negotiating, businesses, discussions, interventions and interviewing. |
| C5 | 233 | 839 / 1,418 | 13.29 | +0.03028 | Physical/computational interactions, coupling and system dynamics dominate: interactions, interacting, superconducting, development, coupling, values, change, computations, perturbative and Lagrangian/renormalisation/Spin/Phase material. |
| C6 | 219 | 788 / 1,463 | 13.88 | +0.03129 | Observation, inference, development and research/process actions dominate: characterizing, initiating, remembering, exploring, observing, entering, hypothesized, inserting, developing, computed, inferred and adopting. |
| C7 | 182 | 580 / 1,040 | 12.09 | +0.03064 | Software/web/database semantics are clear—DB, mysql, Browser, facebook, Entry, Document, WordPress, Kubernetes fragment—but technical abbreviations and units such as MH, MAR, µm, PRES, BA and RAW remain substantial. |
| C8 | 136 | 424 / 880 | 12.71 | +0.03045 | Affect, bodily/social actions and infant/neonatal life coexist: happier, smiled, sleeping, shook, newborn, grinned, gripped, shrugged, kissed, swung, swallowed and neonates; extremes include viable, neonatal fragments and foraging. |
| C9 | 126 | 757 / 238 | 13.90 | +0.03009 | Numeric strings, including years, dominate. |
| C10 | 52 | 229 / 258 | 13.77 | +0.03167 | Cities and geographic entities form a coherent place domain: Manchester, Amsterdam, Mumbai, Berlin, Frankfurt, Stockholm, London, Paris, Brooklyn and Hamburg. |
| C11 | 24 | 58 / 193 | 12.88 | +0.03070 | Calendar/time terms coexist with distance and everyday-object vocabulary: Day, Wednesday, Saturday, Week, Sunday, months alongside mile/miles, ft, trails and shoe. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 512 | 2,403 / 2,353 | 13.98 | -0.02994 | Characterisation, regulation/constraint and evaluative-change language coexist: Characteristics, prohibiting, unconstitutional, circumstantial, encouragement, downregulation, Delete, disproportionate, discriminatory and emphasizing; extremes include specificity, Features, Clause, submit and composed. |
| C1 | 436 | 1,757 / 2,060 | 12.78 | -0.03048 | Personal names dominate but technical and lexical fragments are substantial: Claud, Jess, Dav, Emily, Molly, Freder and Claude coexist with TG, GH, crypt, CI, LCD and PROT-like forms. |
| C2 | 425 | 1,982 / 1,802 | 13.57 | -0.03004 | Common grammatical/function words, punctuation and lexical fragments dominate. |
| C3 | 372 | 1,640 / 1,997 | 14.19 | -0.03080 | Government, royalty, religion and family/social roles coexist: emperor, Constitution, palace, guards, cathedral/church, mother, priest, grandmother, Empire and legislature; extremes include throne, Interior, Uncle, wedding, aunt and Queen. |
| C4 | 336 | 1,293 / 1,817 | 13.10 | -0.03039 | Vehicles, built environment, household objects and natural terrain form a broad physical-world domain: chassis, trucks, automobiles, sidewalk, driveway, mountains, furniture, appliances, gravel and volcano. |
| C5 | 264 | 948 / 1,641 | 13.40 | -0.03058 | Distribution, technology, data, algorithms and quantitative/mathematical concepts coexist: distributions, uniformity, technologies, concepts, database, algorithms, perpendicular, probability and dashboard; extremes include variance, algebra, quotient, codes and methodology. |
| C6 | 250 | 912 / 1,567 | 13.56 | -0.03039 | Catastrophe, tragedy and negative/intense evaluation dominate: disasters, catastrophe fragments, horrific, disastrous, tragedy, catastrophic, incredible, unbelievable, discouragement fragments and glorious; extremes include harsh, bleak and ignorant. |
| C7 | 192 | 863 / 1,007 | 14.23 | -0.02984 | Biomedical diagnostics, cardiovascular disease and laboratory biology are coherent: immunofluorescence, echocardiography, cardiovascular, atherosclerotic, malignancies, diseases, electrophoresis, dysfunction, epithelium and Experiments. |
| C8 | 155 | 940 / 390 | 14.65 | -0.02969 | Numeric strings, especially historical years, dominate. |
| C9 | 91 | 378 / 504 | 13.85 | -0.03047 | Geographic entities and administrative regions form a coherent territorial domain: Alabama, Connecticut, province, Georgia, Minnesota, Edinburgh, Kerala, Illinois and Montreal. |
| C10 | 75 | 257 / 485 | 13.32 | -0.02913 | Adverbial qualification, degree and evaluative emphasis are coherent: particularly, unfortunately, essentially, fortunately, specifically, effectively and literally; extremes include heavily, logically and entirely. |
| C11 | 65 | 311 / 213 | 12.85 | -0.02861 | Strong mathematical/code punctuation and symbol-formatting cluster; 53 of 65 tokens are punctuation/symbols. |
| C12 | 32 | 87 / 234 | 12.75 | -0.02878 | Courtroom, evidence, injury, security and safety form a coherent risk/legal-evidence domain: courtroom, testimony, injuries, security, jury, court, evidence, safety, TBI and harm; extremes include Safety, hazards, testament and privacy. |

## Population accounting

### Positive head

Total nodes: **3,099**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,155 | 37.3% |
| Formal substrate | 824 | 26.6% |
| Irreducible semantic | 467 | 15.1% |
| Mixed unresolved | 653 | 21.1% |
| Unclear | 0 | 0.0% |
| **Total** | **3,099** | **100.0%** |

Semantic-eligible denominator: **2,275 nodes**.

### Negative tail

Total nodes: **3,205**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,681 | 52.4% |
| Formal/name substrate | 1,081 | 33.7% |
| Irreducible semantic | 443 | 13.8% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,205** | **100.0%** |

Semantic-eligible denominator: **2,124 nodes**.

## Positive-side reconstruction

### P+0 — Coordinated inquiry, management and process activity

- **Primary children:** C4, C6
- **Primary nodes:** 516
- **Side-relative coverage:** 16.7%
- **Semantic-eligible coverage:** 22.7%
- **Confidence:** High / Moderate

**Evidence.** C4 contains management, conversations, investigations,
interviews, negotiation and business activity. C6 contains observation,
inference, exploration, hypothesis, computation and development actions. Their
direct relation contains **250 token edges**, mean cosine **0.10370**, one of
the highest-mean semantic relations in the positive graph. The common generator
is coordinated inquiry and goal-directed process activity: information is
observed, inferred, developed and acted upon within managed/interpersonal work.

**Secondary links:** C1 and C7. C1–C4 has **430 edges**, C1–C6 **370**, while
C4–C7 has **122** and C6–C7 **38**. Biomedical/psychosocial and software
material are strongly adjacent to coordinated inquiry but remain distinct or
mixed domains.

**Exclusion boundary.** C4 is socially and professionally organised; C6 is more
general cognitive/process action. C7 is not absorbed because technical
abbreviations and units are substantial. C1 is not absorbed because biomedical,
food, telecommunications and psychosocial structures coexist.

**Alternative.** Expand P+0 with C7 under a broader
`inquiry, management and information systems` parent. Rejected because C7's
abbreviation/unit organisation materially weakens the semantic compression.

### P+1 — Biomedical, developmental and embodied-life organisation

- **Primary children:** C1, C8
- **Primary nodes:** 639
- **Side-relative coverage:** 20.6%
- **Semantic-eligible coverage:** 28.1%
- **Confidence:** Moderate

**Evidence.** C1 contains biomedical, pharmacological, reproductive,
infectious-disease and psychosocial material. C8 contains affective bodily
actions and infant/neonatal life. Their direct relation contains **244 token
edges**, mean cosine **0.10151**. The common structure is embodied living-system
organisation spanning health, development, physiological/social state and
early-life processes.

**Secondary link:** C5. C1–C5 has **315 edges**, and C5 provides interaction,
coupling and system-dynamics language that can describe biological systems.

**Exclusion boundary.** Telecommunications and food material inside C1 are
explicitly preserved as heterogeneity. C8 includes general social/bodily
actions, not only neonatal biology. C5 remains a physical/computational-system
domain rather than being redefined as biological machinery.

**Alternative.** Leave C1 mixed-unresolved and retain C8 as an irreducible
embodied/infant-life community. This is a serious alternative; P+1 therefore
remains Moderate.

### Positive irreducible and unresolved structures

- **C0 — mixed-unresolved:** names/geography, conflict/political labels and
  tokenizer residue coexist. Strong graph connectivity does not resolve its
  internal organisation.
- **C5 — irreducible-semantic:** physical/computational interactions, coupling
  and system dynamics; secondary relation to P+1.
- **C7 — irreducible-semantic:** software/web/database system domain with
  substantial abbreviation/unit noise; secondary relation to P+0.
- **C10 — irreducible-semantic:** cities and geographic entities.
- **C11 — mixed-unresolved:** calendar/time, distance and everyday-object
  vocabulary coexist.

### Positive formal substrate

- C2 — grammar/function words/fragments
- C3 — formatting/tokeniser structure with software/paratext residue
- C9 — numeric strings

## Negative-side reconstruction

### P-0 — Evaluative constraint, regulation and adverse-state organisation

- **Primary children:** C0, C6
- **Primary nodes:** 762
- **Side-relative coverage:** 23.8%
- **Semantic-eligible coverage:** 35.9%
- **Confidence:** High

**Evidence.** C0 contains characterisation, prohibition, constitutional and
discriminatory/constraint language; C6 contains catastrophe, tragedy and
negative/intense evaluation. Their direct relation contains **381 token
edges**, mean cosine **0.10291**, the strongest-mean major semantic relation in
the negative graph. The common generator is adverse-state characterisation and
constraint: problematic states are evaluated, prohibited, down-regulated,
discriminated or otherwise marked as unacceptable/deviant.

**Secondary links:** C10 and C12. C0–C10 has **144 edges**, supporting degree
and evaluative qualification; C0–C12 has **60**, while C6–C12 has **28**,
linking legal/evidence/safety material to the adverse/constraint structure.

**Exclusion boundary.** C0 also contains neutral characterisation and
representational change; C6 includes intensity/evaluation without regulation.
C12 is a distinct legal-risk/evidence domain rather than merely a subtype of
negative evaluation.

**Alternative.** Split C0 and C6 into regulatory-characterisation and
catastrophe/evaluation structures. This preserves semantic purity but gives up
a strong direct relation and a discriminative higher-order adverse/constraint
generator.

### P-1 — Civic/institutional authority and territorial identity

- **Primary children:** C3, C9
- **Primary nodes:** 463
- **Side-relative coverage:** 14.4%
- **Semantic-eligible coverage:** 21.8%
- **Confidence:** Moderate / High

**Evidence.** C3 contains government, monarchy, religion, institutional and
family/social roles. C9 contains states, provinces and cities. Their direct
relation contains **112 token edges**, mean cosine **0.09899**. The common
generator is civic/institutional order situated within geographic-political
territories.

**Secondary link:** C4. C3–C4 has **337 edges**, mean cosine **0.09566**,
showing that material environments strongly contextualise institutional/social
roles. C4–C9 adds **50** edges.

**Exclusion boundary.** C3 includes family and religious roles as well as
government; C9 is territorial rather than institutional. C4 is not absorbed
because vehicles, buildings, household objects and terrain are material
settings, not civic authority.

**Alternative.** Leave C3 and C9 separate. This remains plausible because the
direct relation is moderate rather than dominant; confidence is therefore
Moderate/High.

### P-2 — Scientific/quantitative and clinical systems

- **Primary children:** C5, C7
- **Primary nodes:** 456
- **Side-relative coverage:** 14.2%
- **Semantic-eligible coverage:** 21.5%
- **Confidence:** Moderate / High

**Evidence.** C5 contains distributions, technologies, databases, algorithms,
probability and mathematical/statistical concepts. C7 contains biomedical
diagnostics, cardiovascular disease and laboratory biology. Their direct
relation contains **158 token edges**, mean cosine **0.09420**. The common
generator is formal/scientific system analysis, with quantitative and technical
methods connected to clinical and laboratory domains.

**Secondary link:** C0. C0–C5 has **471 edges** and C0–C7 **144**. C0's
characterisation language is strongly adjacent to scientific/clinical analysis
but is retained under P-0 because regulatory/evaluative structure is also
central there.

**Exclusion boundary.** C5 spans data technology and mathematics rather than
only biomedical science. C7 is specifically medical/diagnostic. The parent is
therefore not reduced to “clinical analysis”.

**Alternative.** Leave C5 and C7 separate as quantitative/technical and
clinical domains. This is a serious alternative; P-2 remains Moderate/High.

### Negative irreducible structures

- **C4 — irreducible-semantic:** vehicles, built environment, household objects
  and terrain; secondary relation to P-1.
- **C10 — irreducible-semantic:** adverbial qualification, degree and evaluative
  emphasis; secondary relation to P-0.
- **C12 — irreducible-semantic:** courtroom, evidence, injury, security and
  safety; secondary relation to P-0 and weaker relation to P-1.

### Negative formal/name substrate

- C1 — personal names plus technical/lexical fragments
- C2 — grammar/function words/punctuation/fragments
- C8 — numeric strings
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 629 | Names + geography + conflict + tokenizer residue | mixed-unresolved | — | Multiple entity, semantic and formal organisations coexist. |
| + | C1 | 503 | Biomedical/health + food/telecom/psychosocial | parent:P+1 | C5 | Biomedical/embodied-life core retained with heterogeneity explicit. |
| + | C2 | 382 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 316 | Formatting + software/paratext residue | formal-substrate | — | Punctuation/tokeniser organisation dominates. |
| + | C4 | 297 | Management/conversation/investigation/business | parent:P+0 | — | Coordinated inquiry/work child. |
| + | C5 | 233 | Physical/computational interactions/coupling | irreducible-semantic | P+1 | Distinct dynamical-system domain. |
| + | C6 | 219 | Observation/inference/development/research actions | parent:P+0 | — | Inquiry/process child. |
| + | C7 | 182 | Software/web/database + abbreviations/units | irreducible-semantic | P+0 | Technical-system domain with acknowledged form noise. |
| + | C8 | 136 | Affect/bodily actions + infant/neonatal life | parent:P+1 | — | Embodied/developmental-life child. |
| + | C9 | 126 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C10 | 52 | Cities/geographic entities | irreducible-semantic | — | Coherent geographic domain without a sibling parent. |
| + | C11 | 24 | Calendar/time + distance/everyday objects | mixed-unresolved | — | Multiple organising domains coexist. |
| − | C0 | 512 | Characterisation/regulation/evaluative-change | parent:P-0 | P-2 | Constraint/evaluative organisation dominates; analytical relation retained. |
| − | C1 | 436 | Personal names + technical/lexical fragments | formal-substrate | — | Name/form organisation without one semantic class. |
| − | C2 | 425 | Grammar/function words/punctuation/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C3 | 372 | Government/royalty/religion/family roles | parent:P-1 | — | Civic/institutional-role child. |
| − | C4 | 336 | Vehicles/built environment/objects/terrain | irreducible-semantic | P-1 | Material-setting relation without authority identity. |
| − | C5 | 264 | Distribution/technology/data/math | parent:P-2 | — | Quantitative/technical-system child. |
| − | C6 | 250 | Catastrophe/tragedy/intense evaluation | parent:P-0 | — | Adverse-state evaluation child. |
| − | C7 | 192 | Biomedical diagnostics/cardiovascular/lab biology | parent:P-2 | — | Clinical/laboratory-system child. |
| − | C8 | 155 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 91 | Geographic/administrative regions | parent:P-1 | — | Territorial/public-identity child. |
| − | C10 | 75 | Adverbial qualification/degree/emphasis | irreducible-semantic | P-0 | Evaluative modifier relation. |
| − | C11 | 65 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 32 | Courtroom/evidence/injury/security/safety | irreducible-semantic | P-0, P-1 | Legal-risk/evidence relation without parent absorption. |

Every State 13 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Coordinated inquiry, management and process activity | C4, C6 | 516 | 16.7% | 22.7% | High / Moderate |
| P+1 | Biomedical, developmental and embodied-life organisation | C1, C8 | 639 | 20.6% | 28.1% | Moderate |
| P-0 | Evaluative constraint, regulation and adverse-state organisation | C0, C6 | 762 | 23.8% | 35.9% | High |
| P-1 | Civic/institutional authority and territorial identity | C3, C9 | 463 | 14.4% | 21.8% | Moderate / High |
| P-2 | Scientific/quantitative and clinical systems | C5, C7 | 456 | 14.2% | 21.5% | Moderate / High |

Positive retained parents account for **1,155 nodes**, **37.3% of the positive
population** and **50.8% of semantic-eligible positive nodes**.

Negative retained parents account for **1,681 nodes**, **52.4% of the negative
population** and **79.1% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — inquiry/health relation — High.**
   C1–C4 has **430 edges**, C1–C6 **370**, C4–C8 **84** and C6–C8 **99**.
   Biomedical/embodied-life content is strongly embedded in managed inquiry and
   process activity without collapsing into it.

2. **P+1 ↔ C5 — biological/dynamical-system relation — High.**
   C1–C5 has **315 edges**, and C5–C8 has **81**. Physical/computational
   interaction language is adjacent to embodied biological organisation but
   retains an independent domain identity.

3. **P+0 ↔ C7 — inquiry/information-system relation — Moderate.**
   C4–C7 has **122 edges** and C6–C7 **38**. The relation is real but weaker
   than the core P+0 pair and does not overcome C7's abbreviation/unit noise.

4. **C0 is highly connected but remains unresolved.**
   Its relations include C0–C1 **542**, C0–C4 **237**, C0–C7 **277** and
   C0–C10 **136**. Connectivity cannot determine whether its name/geography,
   conflict or tokenizer components should dominate.

### Negative-side relations

1. **P-0 ↔ P-2 — characterisation and scientific/clinical analysis — High.**
   C0–C5 has **471 edges**, C0–C7 **144**, C6–C5 **119** and C6–C7 **84**.
   Evaluative/regulatory characterisation is tightly connected to quantitative
   and clinical analysis without becoming identical to it.

2. **P-0 ↔ P-1 — constraint/evaluation in institutional context — High.**
   C0–C3 has **405 edges**, C6–C3 **239**, C0–C9 **19** and C6–C9 **27**.
   Public/institutional order contextualises adverse and regulatory semantics.

3. **P-1 ↔ C4 — authority and material setting — High.**
   C3–C4 has **337 edges**, while C4–C9 has **50**. Physical environments are
   strongly associated with institutional/social roles but remain a distinct
   material domain.

4. **C12 is a small legal-risk bridge-like irreducible community.**
   It links most strongly to P-0 through C0–C12 **60** and C6–C12 **28**, with
   weaker civic/institutional relations.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-2 through inquiry/analysis;
- positive P+1 and negative P-2 through biomedical/clinical structure;
- positive C10 and negative P-1 through geography/territorial identity;
- positive C7 and negative C5 through software/data systems.

No parent-level bridge is promoted without direct cross-side community
evidence sufficient to distinguish semantic structure from lexical proximity.

## Formal/representational substrate

### Positive — 824 nodes / 26.6%

- grammar/function words and fragments;
- formatting/tokeniser structure;
- numeric strings.

### Negative — 1,081 nodes / 33.7%

- personal names plus technical/lexical fragments;
- grammar/function words/punctuation/fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 13 — BLOCK 12 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 COORDINATED INQUIRY / MANAGEMENT / PROCESS ACTIVITY
|   +-- C4 management/conversation/investigation/business
|   `-- C6 observation/inference/development/research actions
|       \
|        -- C7 software/web/database systems          [secondary]
|
+-- P+1 BIOMEDICAL / DEVELOPMENTAL / EMBODIED-LIFE ORGANISATION
|   +-- C1 biomedical/health + mixed contextual material
|   `-- C8 affect/bodily actions + infant/neonatal life
|       \
|        -- C5 physical/computational dynamics        [secondary]
|
+-- C0 names/geography + conflict + tokenizer residue  [mixed unresolved]
+-- C5 physical/computational interactions             [irreducible]
+-- C7 software/web/database + abbreviations/units      [irreducible]
+-- C10 geographic entities                            [irreducible]
+-- C11 time + distance/everyday objects               [mixed unresolved]
`-- C2,C3,C9                                          [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 EVALUATIVE CONSTRAINT / REGULATION / ADVERSE-STATE ORGANISATION
|   +-- C0 characterisation/regulation/evaluative-change
|   `-- C6 catastrophe/tragedy/intense evaluation
|       |
|       +-- C10 qualification/degree/emphasis          [secondary]
|       `-- C12 courtroom/evidence/security/safety    [secondary]
|
+-- P-1 CIVIC/INSTITUTIONAL AUTHORITY & TERRITORIAL IDENTITY
|   +-- C3 government/royalty/religion/family roles
|   `-- C9 geographic/administrative regions
|       \
|        -- C4 physical/material environment          [secondary]
|
+-- P-2 SCIENTIFIC/QUANTITATIVE & CLINICAL SYSTEMS
|   +-- C5 distribution/technology/data/math
|   `-- C7 biomedical diagnostics/laboratory biology
|
+-- C4 vehicles/built environment/objects/terrain      [irreducible]
+-- C10 adverbial qualification/degree                 [irreducible]
+-- C12 courtroom/evidence/injury/security/safety      [irreducible]
`-- C1,C2,C8,C11                                      [formal/name substrate]
```

The preferred State 13 reconstruction contains two positive and three negative
multi-community parents. The positive side is intentionally conservative
because the largest positive communities contain unresolved mixtures. The
negative side supports stronger decomposition into adverse/regulatory
organisation, civic-territorial order and scientific/clinical systems.

This statement is local to State 13 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. leave positive C1 mixed-unresolved and retain C8 as an irreducible
   embodied/infant-life community instead of P+1;
2. expand positive P+0 with C7 as an information-system child;
3. split negative P-0 into regulatory/characterisation C0 and
   catastrophe/evaluation C6;
4. leave negative P-2 as separate quantitative/technical C5 and clinical C7
   domains;
5. absorb negative C4 into P-1 as a material-setting child.

The first and fourth alternatives are the most serious. The preferred
reconstruction retains the parents because the direct graph relations and
shared higher-order functions are sufficient, while confidence remains
explicitly Moderate where child heterogeneity is substantial.

## Uncertainty record

- **Positive P+1:** C1 is strongly mixed across biomedical, psychosocial, food
  and telecommunications material. The parent is therefore Moderate.
- **Positive C0:** is the largest unresolved positive structure; high
  connectivity cannot solve its entity/conflict/tokenizer mixture.
- **Positive C7:** software semantics are real but abbreviation/unit structure
  is substantial.
- **Negative P-0:** C0 contains both regulation and general characterisation,
  while C6 is primarily adverse/intense evaluation.
- **Negative P-1:** the institutional-territorial parent is semantically
  coherent but not the strongest edge pair in the state.
- **Negative P-2:** quantitative/data and clinical/laboratory systems are
  related but remain distinct child domains.
- **Negative C12:** is small but semantically coherent; it is retained outside
  parents rather than being over-compressed.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **25 / 25**
- Positive node accounting: **3,099 / 3,099**
- Negative node accounting: **3,205 / 3,205**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1, P-2**
- Every retained parent has an exclusion boundary: **yes**
- Every State 13 community inspected at underlying R008 community-record level: **yes**
- All State 13 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 13 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 13 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
