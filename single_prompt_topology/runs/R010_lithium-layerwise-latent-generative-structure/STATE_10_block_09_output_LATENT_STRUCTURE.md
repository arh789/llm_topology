# R010 State 10 — Block 9 output latent structure

## State identity

- R010 state index: `10`
- R008/R009 state: `block_09_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 14 negative-tail = 27**
- R008 population: **2,963 positive-head + 3,095 negative-tail = 6,058 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 10 only. Retrieval and graph inspection were
restricted to `state_index=10 / block_09_output`. No later-state evidence was
used.

## Evidence inventory

For every State 10 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_10_block_09_output.md`;
2. all 27 State 10 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 10 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 408 | 1,750 / 2,264 | 14.13 | +0.03141 | Psychology/social relations coexist with politics, transactions and employment: `psychological`, `psychosocial`, `conversations`, `motivational`, `environmentally`, `professionally`, `transactions`, `determinations`, `Political`; extremes include employment, fellowship, stake, bidding and Business. |
| C1 | 388 | 1,683 / 2,018 | 13.88 | +0.03202 | Investigation, research, management and task/process actions dominate: making, investigations, Working, management, resolving, investigative, initiating, requesting, research, getting, walking and researching; extremes include seeking, uploads, keeping, solved and travelled. |
| C2 | 361 | 1,613 / 1,852 | 14.07 | +0.03141 | Biomedical, immune, cellular and pharmacological terminology dominates: immunosuppressive, immunodeficiency fragments, biodegradable fragments, conformational, glucocorticoid fragments, intracellular, antipsychotic fragments, dexamethasone, inflammatory, transmembrane and proliferative. |
| C3 | 360 | 1,507 / 1,999 | 13.93 | +0.03120 | Common grammatical/function words and short lexical fragments dominate. |
| C4 | 254 | 1,140 / 1,117 | 13.37 | +0.03098 | Cities, countries, nationalities and personal/place names form a coherent geographic/name domain: Charleston, Stockholm, Springfield, Atlanta, Mumbai, Brooklyn, Berlin, Nigerian, Sri, Indonesian, Egyptian and Sacramento. |
| C5 | 242 | 874 / 1,379 | 12.92 | +0.03204 | Telecommunications, databases, web/UI and software systems dominate: telecommunications, mysql, DB, MySQL, createElement, findViewById and BytePtrFromString; extremes include sizeof, Entry, Views, getElementById, Permission, Forms and Hash. |
| C6 | 190 | 650 / 1,036 | 12.29 | +0.03180 | Short technical/scientific abbreviations and measurement forms dominate. |
| C7 | 178 | 989 / 438 | 13.57 | +0.03191 | Strong closing-punctuation/bracket/code-formatting cluster; 134 of 178 tokens are punctuation or symbols. |
| C8 | 163 | 508 / 1,004 | 12.39 | +0.03174 | Multilingual, malformed and fragmentary tokenisation residues dominate. |
| C9 | 141 | 462 / 946 | 13.26 | +0.03179 | Food/cuisine, literature/leisure and biological material coexist: coffee, rice, Coca, foods, literary, washing, theatre fragments, culinary, Shakespeare fragment and fungal; extremes include resorts, breakfast, Casino, calorie, Chocolate and mating. |
| C10 | 108 | 357 / 792 | 13.94 | +0.03253 | Interactions, coupling and dynamical/physical-system relations dominate: interactions, renormalization, interacting, coupling, relations, activities, response, responses, actions and Lagrangian; extremes include Spin, active, corrections and cyclo. |
| C11 | 86 | 537 / 151 | 14.24 | +0.03079 | Numeric strings, including years, dominate. |
| C12 | 84 | 291 / 520 | 13.12 | +0.03192 | Temporal/sequential, freshness and comparative descriptors dominate: Following, Day, Alternatively, Using, Having, sprang, Next, freshly, Subsequently, Fresh, Afterwards and wider; extremes include refreshing, seasonal, Week, oldest and cheaper. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 492 | 2,201 / 2,537 | 14.10 | -0.03053 | Characteristics/evaluation, adversity, constraints and quantitative description coexist: Characteristics, unconstitutional, horrific, environments, catastrophe fragment, unreasonable, disappointing, concepts and discriminatory; extremes include Features, variability, covariance, circumstance, departure and conclusive. |
| C1 | 363 | 1,576 / 1,738 | 13.47 | -0.03018 | Personal names dominate, with geographic/media/name-like entities such as province, Telegraph, Mirror and borough. |
| C2 | 328 | 1,672 / 1,690 | 15.35 | -0.03055 | Common grammatical/function words, punctuation and lexical fragments dominate. |
| C3 | 317 | 1,432 / 1,665 | 14.29 | -0.03043 | Built environment, geography, religion/institutions and conflict coexist: Cathedral, warriors, hallway, sidewalk, priest, mountains, Archbishop, trucks, fireplace, automobiles and Constitution; extremes include Devil, Territory, creature, roads, Highway and Empire. |
| C4 | 261 | 1,078 / 1,490 | 13.97 | -0.03051 | Prohibition, exclusion, destruction and removal dominate: prohibiting, eliminating, destroyed, prohibit, destroys, includes, exclude, kill, prohibited, prohibits, murders and depicts; extremes include Delete, shots, creates and reject. |
| C5 | 233 | 782 / 1,312 | 12.34 | -0.03001 | Software, compiler, interface and low-level technical systems dominate: notification, compiler, initialization, dashboard, Sig, Hex; extremes include CI, signal, glyph, HW, logs and DP. |
| C6 | 222 | 675 / 1,344 | 12.14 | -0.03079 | Negative/contrastive word stems and multilingual lexical fragments dominate. |
| C7 | 161 | 943 / 310 | 13.64 | -0.02983 | Numeric strings, especially historical years, dominate. |
| C8 | 157 | 494 / 1,058 | 13.03 | -0.02961 | Users, consumers, passengers and social/authority roles dominate: customers, guards, users, passengers, subscriber, consume, enthusiasts, thieves, officials and captain; extremes include Chair, broadcasts, aides, buyer and subscribers. |
| C9 | 149 | 463 / 962 | 12.67 | -0.03091 | Mathematics/geometry and technical/physical objects coexist: geometry, algebra, anisotropy and subset with emitter, LED, rifles, cartridges, colors and barrel; extremes include quotient, cylinder, zero, codec, emit and quadrant. |
| C10 | 132 | 547 / 718 | 13.73 | -0.03018 | Clinical diagnostics, anatomy and pathology are coherent: echocardiography, angiography, pelvis, dysfunction, epithelium, thighs, physiology, forearm, neuropathy fragments and torso. |
| C11 | 102 | 565 / 233 | 13.36 | -0.02994 | Strong mathematical/code punctuation and symbol-formatting cluster; 94 of 102 tokens are punctuation or symbols. |
| C12 | 93 | 298 / 574 | 12.58 | -0.02995 | Astronomy/cosmology and multilingual world-language terms coexist: Universe, photometric, planets, Kepler/spacecraft material with sempre, guerra, mundo, monde, apenas and jamais. |
| C13 | 85 | 329 / 505 | 13.68 | -0.03014 | Intensity, shouting, screaming and manner adverbs dominate: drastically, screams, effectively, scream, violently, shouted, yelled and loudly; extremes include louder, speakers, screamed, audible and speaker. |

## Population accounting

### Positive head

Total nodes: **2,963**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,507 | 50.9% |
| Formal substrate | 977 | 33.0% |
| Irreducible semantic | 338 | 11.4% |
| Mixed unresolved | 141 | 4.8% |
| Unclear | 0 | 0.0% |
| **Total** | **2,963** | **100.0%** |

Semantic-eligible denominator: **1,986 nodes**.

### Negative tail

Total nodes: **3,095**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,227 | 39.6% |
| Formal/name substrate | 1,176 | 38.0% |
| Irreducible semantic | 450 | 14.5% |
| Mixed unresolved | 242 | 7.8% |
| Unclear | 0 | 0.0% |
| **Total** | **3,095** | **100.0%** |

Semantic-eligible denominator: **1,919 nodes**.

## Positive-side reconstruction

### P+0 — Organised task, transaction and information activity

- **Primary children:** C0, C1, C5
- **Primary nodes:** 1,038
- **Side-relative coverage:** 35.0%
- **Semantic-eligible coverage:** 52.3%
- **Confidence:** Moderate / High

**Evidence.** C0 supplies social/administrative, transactional and employment
context; C1 supplies investigation, research, management and task actions; C5
supplies telecommunications, databases and software systems. The three-child
structure is strongly triangulated: C0–C1 has **586 token edges**, mean cosine
**0.09789**; C0–C5 has **249** at **0.09189**; C1–C5 has **217** at
**0.09131**. The common generator is organised activity in which information,
transactions, investigation and management are performed through technical and
institutional systems.

**Secondary links:** C12 and C4. C1–C12 has **113 edges**, C0–C12 **102**, and
C0–C4 **171**; sequential/time descriptors and geographic populations provide
context without becoming core children.

**Exclusion boundary.** C0 contains psychology/social language, C1 includes
general physical activity and C5 contains technical implementation detail.
The parent therefore does not expand into generic “social systems” or “all
technical activity”. C2 remains a distinct biomedical domain despite strong
connections to C0/C1.

**Alternative.** Split C0 from C1+C5, retaining a social/institutional parent
and an investigation/information parent. This preserves domain purity but loses
the strongest positive relation and the shared transactional/management
organisation.

### P+1 — Biomedical and interacting physical/biological systems

- **Primary children:** C2, C10
- **Primary nodes:** 469
- **Side-relative coverage:** 15.8%
- **Semantic-eligible coverage:** 23.6%
- **Confidence:** Moderate / High

**Evidence.** C2 contains biomedical, immune, cellular and pharmacological
terminology. C10 contains interactions, coupling, dynamical/physical-system
relations and response/action concepts. Their direct relation contains **188
token edges**, mean cosine **0.09973**. The higher-order structure is biological
and physical systems understood through interaction, coupling and dynamic
response.

**Secondary link:** C9 through its food/biological component. C2–C9 has **195
edges**, mean cosine **0.10209**, but C9's literature/leisure/travel content
prevents primary absorption.

**Exclusion boundary.** C10's Lagrangian/Spin/renormalization material prevents
a narrowly biomedical label, while C2's pharmacology/clinical content prevents a
generic physics parent.

**Alternative.** Keep C10 as an irreducible physical/dynamical-relations
community and C2 as an irreducible biomedical community. This is a serious
alternative because the common parent spans biological and physical systems.

### Positive irreducible and unresolved structures

- **C4 — irreducible-semantic:** cities, countries, nationalities and
  personal/place names. It has a secondary population-context relation to P+0
  but lacks a second community that supports a discriminative parent.
- **C12 — irreducible-semantic:** temporal/sequential, freshness and comparative
  descriptors; secondary relation to P+0.
- **C9 — mixed-unresolved:** food/cuisine, literature/leisure and biological
  material. Its biological component links to P+1, but the cultural/leisure
  component is equally material.

### Positive formal substrate

- C3 — grammar/function words/fragments
- C6 — short technical/scientific abbreviations
- C7 — punctuation/formatting
- C8 — multilingual/malformed fragments
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Evaluative characterisation, constraint and destructive change

- **Primary children:** C0, C4
- **Primary nodes:** 753
- **Side-relative coverage:** 24.3%
- **Semantic-eligible coverage:** 39.2%
- **Confidence:** High / Moderate

**Evidence.** C0 combines characteristics/evaluation, adversity, constraint and
quantitative description. C4 contains prohibition, exclusion, destruction and
removal. Their direct relation is the strongest negative semantic relation in
the state: **451 token edges**, mean cosine **0.10349**. The common generator is
the characterisation and constraint of problematic or disallowed states,
including actions that exclude, prohibit, remove or destroy them.

**Secondary links:**
- **C13:** C0–C13 has **161 edges**, mean cosine **0.09823**, and C4–C13 **49**;
  intensity/vocal expression functions as an adverse-event modifier.
- **C3:** C0–C3 has **285 edges** and C4–C3 **155**, linking the structure to
  institutional/material conflict settings.

**Exclusion boundary.** C0 contains neutral quantitative description as well as
adversity; C4 includes compositional inclusion/depiction as well as
prohibition/destruction. The parent is therefore not reduced to “violence” or
“negative emotion”.

**Alternative.** Split C0 and C4 into separate evaluation/characterisation and
prohibition/destruction structures. This preserves semantic purity but ignores
their exceptionally strong direct relation.

### P-1 — Public/social actors and institutional-material environments

- **Primary children:** C3, C8
- **Primary nodes:** 474
- **Side-relative coverage:** 15.3%
- **Semantic-eligible coverage:** 24.7%
- **Confidence:** Moderate

**Evidence.** C3 contains built environments, geography,
religious/institutional entities and conflict material. C8 contains users,
consumers, passengers, guards, officials, subscribers and authority/social
roles. Their direct relation contains **203 token edges**, mean cosine
**0.09606**. The common generator is public/social actors situated within
institutional and material environments.

**Secondary links:** P-0 through C3–C0 (**285 edges**), C3–C4 (**155**), and
C8–C0 (**194**). These actors/settings are strongly adjacent to constraint and
adverse-state processes.

**Exclusion boundary.** C3 contains terrain, religion and conflict as well as
ordinary built environments; C8 contains commercial users/consumers as well as
authority roles. A broader “human world” label would be vacuous.

**Alternative.** Leave C3 and C8 separate as institutional/material setting and
social-role communities. This remains a serious alternative, so confidence is
Moderate.

### Negative irreducible and unresolved structures

- **C5 — irreducible-semantic:** software/compiler/interface/low-level technical
  systems.
- **C10 — irreducible-semantic:** clinical diagnostics, anatomy and pathology.
- **C13 — irreducible-semantic:** intensity, shouting, screaming and manner
  language; secondary link to P-0.
- **C9 — mixed-unresolved:** mathematics/geometry and technical/physical
  objects. Strong technical affinity does not explain its full mathematical
  structure.
- **C12 — mixed-unresolved:** astronomy/cosmology and multilingual
  world-language material coexist.

### Negative formal/name substrate

- C1 — personal names plus geographic/media name-like entities
- C2 — grammar/function words/fragments
- C6 — negative/contrastive and multilingual stems
- C7 — numeric strings
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 408 | Psychology/social + politics/transactions/employment | parent:P+0 | C4 | Organised social/transactional activity dominates. |
| + | C1 | 388 | Investigation/research/management/task actions | parent:P+0 | C12 | Operational/task child. |
| + | C2 | 361 | Biomedical/immune/cellular/pharmacology | parent:P+1 | C9 | Biological-system child. |
| + | C3 | 360 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C4 | 254 | Cities/countries/nationalities/names | irreducible-semantic | P+0 | Coherent geographic/population domain without a sibling parent. |
| + | C5 | 242 | Telecom/databases/web/software | parent:P+0 | — | Technical information-system child. |
| + | C6 | 190 | Short technical/scientific abbreviations | formal-substrate | — | Abbreviation/measurement form dominates. |
| + | C7 | 178 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C8 | 163 | Multilingual/malformed fragments | formal-substrate | — | Orthographic/tokeniser form. |
| + | C9 | 141 | Food/culture/leisure/biological | mixed-unresolved | P+1 | Biological affinity is real, but cultural/leisure content remains material. |
| + | C10 | 108 | Interaction/coupling/dynamical systems | parent:P+1 | — | Dynamic physical/biological relation structure. |
| + | C11 | 86 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C12 | 84 | Temporal/sequential/freshness/comparative | irreducible-semantic | P+0 | Operational temporal modifier without a sibling parent. |
| − | C0 | 492 | Characteristics/evaluation/adversity/quantitative | parent:P-0 | — | Evaluative/constraint characterisation. |
| − | C1 | 363 | Personal names + geographic/media names | formal-substrate | — | Name/entity organisation without one semantic class. |
| − | C2 | 328 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C3 | 317 | Built/geography/religion/institutions/conflict | parent:P-1 | P-0 | Public/material environment dominates, with conflict relation. |
| − | C4 | 261 | Prohibition/exclusion/destruction/removal | parent:P-0 | — | Constraint/destructive-change child. |
| − | C5 | 233 | Software/compiler/interface systems | irreducible-semantic | — | Distinct technical-system domain. |
| − | C6 | 222 | Negative/contrastive/multilingual stems | formal-substrate | — | Morphological form dominates. |
| − | C7 | 161 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C8 | 157 | Users/consumers/passengers/social roles | parent:P-1 | P-0 | Public/social actor child. |
| − | C9 | 149 | Mathematics/geometry + technical objects | mixed-unresolved | — | Dual formal-mathematical and physical-technical organisation. |
| − | C10 | 132 | Clinical diagnostics/anatomy/pathology | irreducible-semantic | — | Distinct clinical domain. |
| − | C11 | 102 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 93 | Astronomy/cosmology + multilingual language | mixed-unresolved | — | Two incompatible organising structures coexist. |
| − | C13 | 85 | Intensity/shouting/screaming/manner | irreducible-semantic | P-0 | Adverse/intensity modifier relation. |

Every State 10 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Organised task, transaction and information activity | C0, C1, C5 | 1,038 | 35.0% | 52.3% | Moderate / High |
| P+1 | Biomedical and interacting physical/biological systems | C2, C10 | 469 | 15.8% | 23.6% | Moderate / High |
| P-0 | Evaluative characterisation, constraint and destructive change | C0, C4 | 753 | 24.3% | 39.2% | High / Moderate |
| P-1 | Public/social actors and institutional-material environments | C3, C8 | 474 | 15.3% | 24.7% | Moderate |

Positive retained parents account for **1,507 nodes**, **50.9% of the positive
population** and **75.9% of semantic-eligible positive nodes**.

Negative retained parents account for **1,227 nodes**, **39.6% of the negative
population** and **63.9% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — operational/scientific relation — High.**
   C0–C2 has **368 edges**, C1–C2 **264**, C0–C10 **177**, C1–C10 **149** and
   C5–C10 **79**. Biomedical and dynamical systems are strongly embedded in
   organised task/information activity without becoming the same structure.

2. **P+0 ↔ C4 — population/institutional context — Moderate.**
   C0–C4 has **171 edges**, C1–C4 **70** and C5–C4 **87**. Geographic
   populations contextualise organised social and technical activity.

3. **P+1 ↔ C9 — biological/cultural-living relation — Moderate.**
   C2–C9 has **195 edges**, one of C9's strongest semantic links, but C9's
   literature/leisure/travel component blocks primary absorption.

4. **C12 is an operational temporal satellite.**
   Its C1 relation has **113 edges**, C0–C12 **102** and C5–C12 **33**.

### Negative-side relations

1. **P-0 ↔ P-1 — constraint/adversity in public/material context — High.**
   C0–C3 has **285 edges**, C0–C8 **194**, C4–C3 **155** and C4–C8 **143**.
   Evaluation, prohibition and destructive change are strongly situated within
   institutional/material environments and social actors.

2. **P-0 ↔ C13 — intensity/expression relation — Moderate.**
   C0–C13 has **161 edges**, mean cosine **0.09823**, supporting an intensity
   modifier around adverse evaluation and conflict.

3. **Technical/scientific islands remain adjacent but unmerged.**
   C0–C9 has **260 edges**, C0–C10 **144**, C5–C9 **85** and C9–C10 **72**.
   These graph relations are substantial but do not justify a vacuous
   “technical/scientific” parent spanning software, geometry, physical objects
   and clinical anatomy.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative C5 through software/information systems;
- positive P+1 and negative C10 through biological/clinical structure;
- positive C4/P+0 and negative P-1 through social/institutional populations.

The within-side evidence does not require a cross-side bridge, and no stronger
cross-side community evidence was inspected that would justify promotion.

## Formal/representational substrate

### Positive — 977 nodes / 33.0%

- grammar/function words and fragments;
- short technical/scientific abbreviations;
- punctuation/formatting;
- multilingual/malformed fragments;
- numeric strings.

### Negative — 1,176 nodes / 38.0%

- personal-name/geographic-media entity organisation;
- grammar/function words/fragments;
- negative/contrastive multilingual stems;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 10 — BLOCK 9 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 ORGANISED TASK / TRANSACTION / INFORMATION ACTIVITY
|   +-- C0 psychology/social + politics/transactions/employment
|   +-- C1 investigation/research/management/task actions
|   `-- C5 telecom/databases/web/software
|       |
|       +-- C4 geographic/population context          [secondary]
|       `-- C12 temporal/sequential descriptors      [secondary]
|
+-- P+1 BIOMEDICAL & INTERACTING PHYSICAL/BIOLOGICAL SYSTEMS
|   +-- C2 biomedical/immune/cellular/pharmacology
|   `-- C10 interactions/coupling/dynamical relations
|       \
|        -- C9 food/culture/leisure/biology          [secondary; mixed]
|
+-- C4 geographic/name domain                         [irreducible]
+-- C9 food/culture/leisure/biology                   [mixed unresolved]
+-- C12 temporal/sequential/freshness                 [irreducible]
`-- C3,C6,C7,C8,C11                                  [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 EVALUATIVE CHARACTERISATION / CONSTRAINT / DESTRUCTIVE CHANGE
|   +-- C0 characteristics/evaluation/adversity/quantitative
|   `-- C4 prohibition/exclusion/destruction/removal
|       |
|       +-- C13 intensity/vocal expression            [secondary]
|       `-- C3 institutional/material conflict       [secondary]
|
+-- P-1 PUBLIC/SOCIAL ACTORS & INSTITUTIONAL-MATERIAL ENVIRONMENTS
|   +-- C3 built/geography/religion/institutions/conflict
|   `-- C8 users/consumers/passengers/social roles
|
+-- C5 software/compiler/interface systems            [irreducible]
+-- C9 mathematics/geometry + technical objects       [mixed unresolved]
+-- C10 clinical diagnostics/anatomy/pathology         [irreducible]
+-- C12 astronomy/cosmology + multilingual language   [mixed unresolved]
+-- C13 intensity/shouting/screaming                   [irreducible]
`-- C1,C2,C6,C7,C11                                  [formal/name substrate]
```

The preferred State 10 reconstruction contains two positive and two negative
multi-community parents. The positive side is dominated by a large
operational/transactional/information parent and a smaller
biomedical/dynamical-systems parent. The negative side separates
evaluation/constraint/destructive change from the public/social actors and
material environments in which those processes occur. Several technically
connected communities remain outside parents because their internal semantic
mixtures are not reducible without losing discriminative structure.

This statement is local to State 10 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. split positive P+0 into separate social/administrative and
   investigation/information-system structures;
2. keep positive C2 and C10 separate rather than retaining P+1;
3. split negative P-0 into evaluative/quantitative characterisation and
   prohibition/destructive-change structures;
4. create a broad negative technical/scientific parent from C5, C9 and C10.

The fourth alternative is rejected most strongly: although graph relations
exist, the proposed parent would conflate software systems, mathematical
geometry/technical objects and clinical anatomy. It fails the anti-vacuity
test.

## Uncertainty record

- **Positive P+0:** C0 is genuinely mixed across psychosocial,
  political/economic and transactional content; the parent is supported by
  dense triangulation rather than pure child labels.
- **Positive P+1:** biological and physical/dynamical-system semantics are
  related but distinct; the parent remains Moderate/High.
- **Positive C9:** is the main positive unresolved community because food,
  culture/leisure and biological structures coexist.
- **Negative P-0:** C0 contains neutral quantitative description as well as
  adversity, so the parent cannot be reduced to “negative evaluation”.
- **Negative P-1:** C3 is broad across built environment, religion,
  institutions and conflict; the actor/environment parent remains Moderate.
- **Negative C9/C12:** both remain unresolved despite useful graph relations
  because each contains incompatible semantic organisations.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **14 / 14**
- Total communities accounted for: **27 / 27**
- Positive node accounting: **2,963 / 2,963**
- Negative node accounting: **3,095 / 3,095**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 10 community inspected at underlying R008 community-record level: **yes**
- All State 10 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 10 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 10 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
