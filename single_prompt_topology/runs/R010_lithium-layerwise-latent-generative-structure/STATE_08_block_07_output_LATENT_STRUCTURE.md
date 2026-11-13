# R010 State 08 — Block 7 output latent structure

## State identity

- R010 state index: `08`
- R008/R009 state: `block_07_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 12 negative-tail = 25**
- R008 population: **3,214 positive-head + 3,211 negative-tail = 6,425 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 08 only. Retrieval and graph inspection were
filtered to `state_index=8 / block_07_output`. No later-state evidence was
used.

## Evidence inventory

For every State 08 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_08_block_07_output.md`;
2. all 25 State 08 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. all State 08 within-side relations in R008 `community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained
as mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 446 | 1,878 / 2,065 | 13.05 | +0.03108 | Work, management, access and task/process actions dominate: `travelling`, `Working`, `initiating`, `management`, `accessing`, `formatted`, `researching`, `giving`, `withdrawing`; extremes include seeking, Reading, solved, recognised and resolving. |
| C1 | 429 | 1,999 / 2,077 | 14.16 | +0.03087 | Common grammatical/function words and short lexical fragments dominate. |
| C2 | 377 | 1,767 / 2,065 | 14.85 | +0.03170 | Biomedical, psychological, immune and inflammatory terminology dominates: immunosuppressive, neurodegenerative, psychosocial, psychological, immunodeficiency fragments, angiotensin, inflammatory, psychiatric, glucocorticoid fragments, emotional, antipsychotic fragments. |
| C3 | 364 | 1,743 / 1,644 | 14.09 | +0.03110 | Geography/nationality, politics/culture and sport coexist: Pakistani, Indonesian, Atlanta, Sacramento, Charleston, Nigerian, Mumbai, Australian, Political, cultural, basketball; extremes include Civil, Social, Cultural, Championships and games. |
| C4 | 330 | 1,191 / 1,728 | 12.45 | +0.03169 | Multilingual, malformed and fragmentary tokenisation residues dominate. |
| C5 | 305 | 1,125 / 1,702 | 12.96 | +0.03138 | Databases, data processing and software/information systems dominate: DB, Database, mysql, MySQL, Connection, Processing, SQL, BytePtrFromString and Relations; extremes include Hash, Entry, connections, Cyber and sizeof. |
| C6 | 237 | 850 / 1,463 | 13.35 | +0.03187 | Molecular/physical-science, dynamical and structural-form vocabulary dominates: conformational, renormalization, molecule, dynamical, hierarchical, chemical, loop, interacting and complexes; extremes include Spin, cycle, carbon, Forms and spacing. |
| C7 | 213 | 741 / 1,453 | 13.78 | +0.03176 | Finance, employment, business and organisational activity dominates: Financial, activities, Employment, development, organising, lending, business and financial. |
| C8 | 174 | 1,049 / 324 | 13.92 | +0.03174 | Strong punctuation/bracket/code-formatting cluster; 148 of 174 tokens are punctuation/symbols. |
| C9 | 115 | 465 / 719 | 14.34 | +0.03127 | Social, cultural, temporal and discourse/adverbial language dominates: emotionally, Eventually, culturally, Anyway, Alternatively, electronically, Subsequently, socially and professionally. |
| C10 | 107 | 660 / 176 | 13.98 | +0.03053 | Numeric strings, including years, dominate. |
| C11 | 89 | 281 / 580 | 12.83 | +0.03240 | Food, crops, cuisine and animals form a coherent living/consumption cluster: rice, food, foods, vegetation fragment, chocolate, coconut, culinary, spinach, cabbage, insects and pig. |
| C12 | 28 | 79 / 198 | 12.71 | +0.03342 | Prefix/opposition/novelty word-form families dominate: Anti/anti, antid-, antib-, antis-, neo-, pseudo-, cyber-, counter-, cis- and multid-. Primarily lexical/morphological. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 632 | 2,875 / 2,359 | 12.83 | -0.03036 | Strong personal-name content coexists with negative/contrastive stems such as catastroph-, brill-, disaster-, unmistak-, gluc- and displacement/comp fragments. The two organising principles are both substantial. |
| C1 | 415 | 1,761 / 2,216 | 13.83 | -0.02983 | Analysis, assessment, scientific description and recommendations dominate: determination, assessments, Characteristics, analysis, manifestations, environments, phenotypes, technologies, recommendations, Notification and prohibited; extremes include variability, robustness, Features and covariance. |
| C2 | 412 | 1,826 / 2,034 | 13.80 | -0.02959 | Religious, institutional, cultural and fictional/social roles/places coexist: Archbishop, priest, Cathedral, concerts, Constitution, Palace, Princess, producer and monsters; extremes include Chair, Devil, speakers, thief, officials, creature, broadcasts, Rabbi and police. |
| C3 | 382 | 1,884 / 1,779 | 14.52 | -0.03074 | Common grammatical/function words, suffixes and lexical fragments dominate. |
| C4 | 304 | 1,353 / 1,668 | 14.39 | -0.03018 | Negative evaluation, distress, tragedy and intense affect dominate: disappointment, unconstitutional, tragedy, horrific, unacceptable, indistinguishable, stunning, scream, discriminatory, sadness and terrifying. |
| C5 | 266 | 1,041 / 1,561 | 13.70 | -0.03024 | Destruction, removal, construction and compositional change dominate: destroys, destroyed, removed, dropped, murders, creating, eliminated, murdered, depicts, contains, combines and constructing. |
| C6 | 220 | 853 / 1,261 | 13.49 | -0.02994 | Built environment, terrain, transport, weapons and objects coexist: hallway, staircase, stairs, guns, mountains, trucks, corridor, gown, cliffs, boats, tube and wavelengths; extremes include barrel, nozzle, spacecraft, roads and tiles. |
| C7 | 143 | 475 / 770 | 12.03 | -0.03094 | Low-level computing/hardware is recognisable despite short-code noise: GCC, compiler, LED, hw, GPIO and FFFF; extremes include drv, png, sdk, Decoder, HW and debug. |
| C8 | 138 | 580 / 771 | 13.99 | -0.03040 | Clinical diagnostics, anatomy and pathology are coherent: echocardiography, pathophysiology, abdomen, angiography, microscopy, cerebellum, pelvis and physician; extremes include erythrocytes, allele, NRAS, torso, dysplasia, therapy and degeneration. |
| C9 | 134 | 807 / 239 | 13.83 | -0.03066 | Strong mathematical/code punctuation cluster; 121 of 134 tokens are punctuation/symbols. |
| C10 | 110 | 673 / 210 | 14.15 | -0.02958 | Numeric strings, especially historical years, dominate. |
| C11 | 55 | 210 / 290 | 12.91 | -0.03324 | Abstract algebra and mathematical notation are coherent: morphisms, bigoplus, homomorphism, maps, homogeneous, algebra, diag, uniform and bigcup; extremes include quotient, subset, zero, nonzero, bounded and periodic. |

## Population accounting

### Positive head

Total nodes: **3,214**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 2,031 | 63.2% |
| Formal substrate | 1,068 | 33.2% |
| Irreducible semantic | 115 | 3.6% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,214** | **100.0%** |

Semantic-eligible denominator: **2,146 nodes**.

### Negative tail

Total nodes: **3,211**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,755 | 54.7% |
| Formal substrate | 626 | 19.5% |
| Irreducible semantic | 198 | 6.2% |
| Mixed unresolved | 632 | 19.7% |
| Unclear | 0 | 0.0% |
| **Total** | **3,211** | **100.0%** |

Semantic-eligible denominator: **2,585 nodes**.

## Positive-side reconstruction

### P+0 — Work/task operations and information systems

- **Primary children:** C0, C5
- **Primary nodes:** 751
- **Side-relative coverage:** 23.4%
- **Semantic-eligible coverage:** 35.0%
- **Confidence:** High

**Evidence.** C0 supplies work, management, access and task/process operations;
C5 supplies databases, data processing and software/information systems. Their
direct relation contains **276 token edges**, mean cosine **0.09688**. The
parent captures operations performed through organised information systems.

**Secondary links:** C7 and C9. C0–C7 has **313 edges**, mean cosine
**0.10399**, while C0–C9 has **173**. Organisational/economic activity and
discourse/evaluation strongly contextualise task activity.

**Exclusion boundary.** C7 is organisational/economic rather than
information-system-specific. C9 is general social/discourse modulation rather
than a task-system child.

**Alternative.** Absorb C7 under a broad work/organisation parent. Rejected
because employment/business organisation is a domain in its own right rather
than merely an information-system operation.

### P+1 — Political, geographic and organisational-economic activity

- **Primary children:** C3, C7
- **Primary nodes:** 577
- **Side-relative coverage:** 18.0%
- **Semantic-eligible coverage:** 26.9%
- **Confidence:** High / Moderate

**Evidence.** C3 combines nationalities/geography with politics, culture and
sport; C7 contains finance, employment, business and organisational activity.
Their direct relation contains **207 token edges**, mean cosine **0.09253**.
The common generator is organised social populations and institutional/economic
activity.

**Secondary link:** C9. C3–C9 has **75 edges** with high mean cosine
**0.11541**, and C7–C9 has **56 edges** at **0.10296**, supporting a
social/cultural discourse relation.

**Exclusion boundary.** Sport in C3 and generic response/development terms in
C7 are preserved as heterogeneity. C0 concerns work/task operations rather than
the social institutions in which they occur.

**Alternative.** Leave C3 and C7 separate. This remains plausible because C3
is explicitly mixed; confidence is therefore High/Moderate rather than
unqualified High.

### P+2 — Biomedical, molecular-scientific and organismal/living systems

- **Primary children:** C2, C6, C11
- **Primary nodes:** 703
- **Side-relative coverage:** 21.9%
- **Semantic-eligible coverage:** 32.8%
- **Confidence:** Moderate / High

**Evidence.** C2 supplies biomedical, psychological, immune and inflammatory
terminology; C6 supplies molecular/physical-science, dynamical and structural
concepts; C11 supplies food, crops and animals. C2–C6 has **332 edges**, mean
cosine **0.09845**, and C2–C11 **139 edges** at **0.09316**. C6–C11 is weaker
at **56 edges**, so C2 acts as the main bridge between molecular/scientific and
organismal/living organisation.

**Secondary links:** C9 through social/emotional material in C2.

**Exclusion boundary.** C6's formal/structural terms and C11's ordinary
food/animal vocabulary prevent a narrowly biomedical interpretation. C3's
population/social material is excluded despite health-adjacent possibilities.

**Alternative.** Define P+2 only from C2+C6 and retain C11 as an irreducible
food/animal community. This is the strongest alternative because C11 is less
tightly connected to C6.

### Positive irreducible structure

- **C9 — irreducible-semantic:** social, cultural, temporal and
  discourse/adverbial language; secondary relation to P+0 and P+1 and weaker
  contextual relation to P+2.

### Positive formal substrate

- C1 — grammar/function words/fragments
- C4 — multilingual/malformed fragments
- C8 — punctuation/formatting
- C10 — numeric strings
- C12 — prefix/word-form families

## Negative-side reconstruction

### P-0 — Analytical/clinical assessment and characterisation

- **Primary children:** C1, C8
- **Primary nodes:** 553
- **Side-relative coverage:** 17.2%
- **Semantic-eligible coverage:** 21.4%
- **Confidence:** High

**Evidence.** C1 contains assessment, analysis, scientific description,
manifestations, phenotypes, recommendations and measurement-like concepts. C8
contains clinical diagnostics, anatomy and pathology. Their direct relation
contains **190 token edges**, mean cosine **0.09992**. The common generator is
analytical characterisation of biological/clinical and other system states.

**Secondary links:** C11 and C7. C1–C11 has **78 edges**, mean cosine
**0.09878**, and C1–C7 **133**; mathematics and computing provide formal or
technical support to analytical characterisation.

**Exclusion boundary.** C1 also contains general technologies/environments and
prohibition language; C8 is specifically clinical. C4 and C5 concern adverse
evaluation/change rather than characterisation itself.

**Alternative.** Expand P-0 to include C11 as a formal mathematical child.
Rejected because abstract algebra is a distinct mathematical object system,
not merely a method of clinical characterisation.

### P-1 — Adverse evaluation and destructive/compositional change

- **Primary children:** C4, C5
- **Primary nodes:** 570
- **Side-relative coverage:** 17.8%
- **Semantic-eligible coverage:** 22.1%
- **Confidence:** High

**Evidence.** C4 contains negative evaluation, distress, tragedy and intense
affect. C5 contains destruction, removal, elimination, creation, composition
and construction. Their direct relation contains **360 token edges**, mean
cosine **0.10014**, one of the strongest semantic relations in the state.
Together they describe adverse states and transformations that create, remove,
damage or alter them.

**Secondary link:** C2. C2–C4 has **235 edges** and C2–C5 **177**; public and
institutional actors/places can provide social context for adverse events and
change.

**Exclusion boundary.** C5 includes constructive/neutral creation and
composition as well as destruction, so the parent is not labelled purely
“violence”. C4 contains evaluation/intensity rather than change mechanisms.

**Alternative.** Split C4 and C5 into separate evaluation and transformation
parents. This preserves a cleaner distinction but ignores their strong direct
relation; the preferred reconstruction keeps them as distinct children.

### P-2 — Institutional/public environments and material settings

- **Primary children:** C2, C6
- **Primary nodes:** 632
- **Side-relative coverage:** 19.7%
- **Semantic-eligible coverage:** 24.4%
- **Confidence:** Moderate

**Evidence.** C2 contains religious/institutional/cultural roles and places:
Archbishop, priest, Cathedral, Constitution, Palace, Princess, producer,
broadcasts, police and related public actors. C6 contains built environment,
terrain, transport, weapons and physical objects. Their direct relation
contains **317 token edges**, mean cosine **0.10126**, among the strongest
negative-side relations. The common generator is the social/public environment
and its material setting.

**Secondary link:** P-1 through C2–C4 (**235 edges**) and C2–C5 (**177**).

**Exclusion boundary.** C2 contains fictional actors and cultural material; C6
contains terrain, clothing and technical objects. A broader label such as
“human world” would be vacuous. The retained parent is limited to public/social
settings plus their physical environment.

**Alternative.** Leave C2 and C6 separate as an institutional-role/place
community and a physical-world community. This remains a serious alternative,
so confidence is Moderate.

### Negative mixed unresolved structure

- **C0 — mixed-unresolved:** names and negative/contrastive lexical stems are
  both structurally substantial. Despite its size and strong graph relations
  (including C0–C2 at **518 edges**), no single semantic parent can absorb it
  without rewriting one of its two dominant organisations.

### Negative irreducible structures

- **C7 — irreducible-semantic:** low-level computing/hardware; secondary link
  to P-0.
- **C11 — irreducible-semantic:** abstract algebra/mathematical notation;
  secondary link to P-0.

### Negative formal substrate

- C3 — grammar/function words/fragments
- C9 — mathematical/code punctuation
- C10 — numeric strings

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 446 | Work/management/access/task actions | parent:P+0 | — | Task/work operations. |
| + | C1 | 429 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C2 | 377 | Biomedical/psychological/immune | parent:P+2 | — | Biomedical/living-system centre. |
| + | C3 | 364 | Geography/politics/culture/sport | parent:P+1 | — | Population/social-institutional structure dominates. |
| + | C4 | 330 | Multilingual/malformed fragments | formal-substrate | — | Tokeniser/orthographic form. |
| + | C5 | 305 | Databases/data/software systems | parent:P+0 | — | Information-system infrastructure. |
| + | C6 | 237 | Molecular/physical science/structure | parent:P+2 | — | Molecular/scientific child. |
| + | C7 | 213 | Finance/employment/business | parent:P+1 | — | Organisational-economic activity. |
| + | C8 | 174 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C9 | 115 | Social/cultural/temporal/discourse | irreducible-semantic | P+0, P+1 | Cross-domain contextual/discourse structure. |
| + | C10 | 107 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C11 | 89 | Food/crops/cuisine/animals | parent:P+2 | — | Organismal/living-system child. |
| + | C12 | 28 | Prefix/opposition word forms | formal-substrate | — | Lexical/morphological form. |
| − | C0 | 632 | Names + negative/contrastive stems | mixed-unresolved | — | Two dominant organisations; no defensible primary parent. |
| − | C1 | 415 | Analysis/assessment/scientific description | parent:P-0 | — | Analytical characterisation. |
| − | C2 | 412 | Religious/institutional/cultural roles/places | parent:P-2 | P-1 | Public/social environment with adverse-event relation. |
| − | C3 | 382 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 304 | Negative evaluation/distress/tragedy | parent:P-1 | — | Adverse-state evaluation. |
| − | C5 | 266 | Destruction/removal/construction/change | parent:P-1 | — | Destructive/compositional transformation. |
| − | C6 | 220 | Built/terrain/transport/weapons/objects | parent:P-2 | — | Material setting of public/social environments. |
| − | C7 | 143 | Low-level computing/hardware | irreducible-semantic | P-0 | Technical support relation. |
| − | C8 | 138 | Clinical diagnostics/anatomy/pathology | parent:P-0 | — | Clinical analytical domain. |
| − | C9 | 134 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C10 | 110 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C11 | 55 | Abstract algebra/notation | irreducible-semantic | P-0 | Formal analytical abstraction. |

Every State 08 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Work/task operations and information systems | C0, C5 | 751 | 23.4% | 35.0% | High |
| P+1 | Political, geographic and organisational-economic activity | C3, C7 | 577 | 18.0% | 26.9% | High / Moderate |
| P+2 | Biomedical, molecular-scientific and organismal/living systems | C2, C6, C11 | 703 | 21.9% | 32.8% | Moderate / High |
| P-0 | Analytical/clinical assessment and characterisation | C1, C8 | 553 | 17.2% | 21.4% | High |
| P-1 | Adverse evaluation and destructive/compositional change | C4, C5 | 570 | 17.8% | 22.1% | High |
| P-2 | Institutional/public environments and material settings | C2, C6 | 632 | 19.7% | 24.4% | Moderate |

Positive retained parents account for **2,031 nodes**, **63.2% of the positive
population** and **94.6% of semantic-eligible positive nodes**.

Negative retained parents account for **1,755 nodes**, **54.7% of the negative
population** and **67.9% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — work/organisation relation — High.**
   C0–C7 has **313 edges**, C5–C7 **227**, C0–C3 **129** and C5–C3 **195**.
   Work/task and information systems are strongly embedded in organisational,
   political and economic activity.

2. **P+0 ↔ P+2 — information/scientific relation — High.**
   C0–C2 has **311 edges**, C0–C6 **240**, C5–C6 **221** and C5–C2 **178**.
   Scientific/biological structure is strongly coupled to task and information
   systems without being reducible to them.

3. **P+1 ↔ P+2 — population/health-science relation — High.**
   C2–C3 has **251 edges**, C2–C7 **212**, C3–C6 **92** and C3–C11 **99**.
   Social/population organisation is strongly connected to biological and
   scientific structure.

4. **C9 is a contextual/discourse bridge-like irreducible structure.**
   Its strongest parent-facing relations include C0–C9 **173**, C2–C9 **94**,
   C5–C9 **81**, C3–C9 **75** and C7–C9 **56**.

### Negative-side relations

1. **P-0 ↔ P-1 — analysis and adverse-change relation — High.**
   C1–C4 has **324 edges**, C1–C5 **420**, C8–C4 **39** and C8–C5 **33**.
   Analytical description is tightly coupled to adverse evaluation and state
   transformation while remaining semantically distinct.

2. **P-0 ↔ P-2 — analysis of institutional/material environments — High.**
   C1–C2 has **301 edges**, C1–C6 **197**, C8–C2 **121** and C8–C6 **95**.

3. **P-1 ↔ P-2 — social-event and material-setting relation — High.**
   C2–C4 has **235 edges**, C2–C5 **177**, C6–C4 **121** and C6–C5 **103**.
   Adverse events and transformations are strongly embedded in social/public
   and physical settings.

4. **C0 remains outside the semantic architecture despite strong connectivity.**
   Its C0–C2 relation has **518 edges**, but connectivity cannot resolve the
   underlying names-versus-lexical-stems ambiguity.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The available State 08 cross-side evidence is not required to explain the
within-side parent architecture, and no parent-level bridge is established from
the current evidence without stronger cross-side community support.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative C7 through computing/information systems;
- positive P+2 and negative P-0 through biomedical/clinical structure;
- positive P+1 and negative P-2 through social/institutional organisation.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,068 nodes / 33.2%

- grammar/function words and fragments;
- multilingual/malformed residues;
- punctuation/formatting;
- numeric strings;
- prefix/word-form families.

### Negative — 626 nodes / 19.5%

- grammar/function words/fragments;
- mathematical/code punctuation;
- numeric strings.

Negative C0 is **not** counted as formal substrate because its large
name/stem mixture is materially unresolved rather than purely formal.

## Minimal state-level architecture

```text
STATE 08 — BLOCK 7 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 WORK/TASK OPERATIONS & INFORMATION SYSTEMS
|   +-- C0 work/management/access/task actions
|   `-- C5 databases/data/software
|       \
|        -- C9 social/discourse modulation          [secondary]
|
+-- P+1 POLITICAL / GEOGRAPHIC / ORGANISATIONAL-ECONOMIC ACTIVITY
|   +-- C3 geography/politics/culture/sport
|   `-- C7 finance/employment/business
|       \
|        -- C9 social/cultural discourse            [secondary]
|
+-- P+2 BIOMEDICAL / MOLECULAR-SCIENTIFIC / ORGANISMAL-LIVING SYSTEMS
|   +-- C2 biomedical/psychological/immune
|   +-- C6 molecular/physical science
|   `-- C11 food/crops/cuisine/animals
|
+-- C9 social/cultural/temporal/discourse             [irreducible]
`-- C1,C4,C8,C10,C12                                 [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ANALYTICAL / CLINICAL ASSESSMENT & CHARACTERISATION
|   +-- C1 analysis/assessment/scientific description
|   `-- C8 clinical diagnostics/anatomy/pathology
|       |
|       +-- C7 low-level computing                   [secondary]
|       `-- C11 abstract algebra                    [secondary]
|
+-- P-1 ADVERSE EVALUATION & DESTRUCTIVE/COMPOSITIONAL CHANGE
|   +-- C4 negative evaluation/distress/tragedy
|   `-- C5 destruction/removal/construction/change
|
+-- P-2 INSTITUTIONAL/PUBLIC ENVIRONMENTS & MATERIAL SETTINGS
|   +-- C2 religious/institutional/cultural roles/places
|   `-- C6 built/terrain/transport/weapons/objects
|
+-- C0 names + negative/contrastive stems             [mixed unresolved]
+-- C7 low-level computing/hardware                   [irreducible]
+-- C11 abstract algebra/notation                     [irreducible]
`-- C3,C9,C10                                        [formal substrate]
```

The preferred State 08 reconstruction contains three positive and three
negative multi-community parents. The positive side is highly compressible into
work/information, social-organisational and biological/scientific structures.
The negative side separates analytical/clinical characterisation,
adverse/destructive transformation and institutional/material environment,
while its largest community remains unresolved because it combines names with
contrastive lexical stems.

This statement is local to State 08 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. restrict positive P+2 to C2+C6 and retain C11 as a separate food/animal
   community;
2. leave negative C2 and C6 separate rather than retaining P-2;
3. split negative P-1 into separate adverse-evaluation and transformation
   structures.

Each alternative increases semantic purity while reducing explanatory
compression. The preferred reconstruction retains the higher-order parents
because their direct graph relations and shared organising principles remain
discriminative, but Moderate confidence is preserved where the abstraction is
broad.

## Uncertainty record

- **Positive P+2:** C11 is less strongly connected to the molecular child than
  to the biomedical child; the three-child living-system hierarchy remains
  Moderate/High rather than unqualified High.
- **Positive P+1:** C3 is genuinely mixed across geography, politics, culture
  and sport.
- **Negative P-2:** the public/social-environment abstraction is broad and its
  children can defensibly remain separate.
- **Negative C0:** is the largest unresolved structure. Strong graph
  connectivity does not justify erasing its name/stem dual organisation.
- **Negative C7:** computing semantics are real but short-code noise remains.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **25 / 25**
- Positive node accounting: **3,214 / 3,214**
- Negative node accounting: **3,211 / 3,211**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1, P-2**
- Every retained parent has an exclusion boundary: **yes**
- Every State 08 community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 08 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 08 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
