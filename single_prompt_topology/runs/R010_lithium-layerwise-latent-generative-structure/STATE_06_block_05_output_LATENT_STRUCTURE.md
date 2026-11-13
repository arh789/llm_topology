# R010 State 06 — Block 5 output latent structure

## State identity

- R010 state index: `06`
- R008/R009 state: `block_05_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 13 negative-tail = 26**
- R008 population: **2,951 positive-head + 3,152 negative-tail = 6,103 nodes**
- Status: Phase-A State 06 reconstruction complete, with procedural deviation recorded below

This file reconstructs State 06 only. No R010 reconstruction from another state
was used to shape the parent labels.

## Procedural deviation

During underlying-source inspection, two requested line ranges extended beyond
the final State 06 row and returned some State 07 rows in the tool response.
Those State 07 rows were not requested for analysis and were not used in any
State 06 parent inference, relation, coverage calculation or alternative
reconstruction.

This nevertheless constitutes a technical breach of R010's strict Phase-A
instruction not to inspect semantic content from another state. The breach is
therefore recorded rather than concealed. State 06 should be treated as
**analytically state-local but procedurally contaminated by incidental source
exposure**. A later Phase-A verification may require a clean rerun if the
project owner judges the contamination material.

## Evidence inventory

State 06 inference used only State 06 evidence:

1. `R009/STATE_06_block_05_output.md`;
2. State 06 entries in `R009_SUMMARY.html`;
3. all 26 State 06 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. all State 06 within-side relations in R008 `community_edges.csv`;
5. the State 06 section of the R008 layer packet and its compact cross-side
   evidence.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 409 | 1,601 / 2,144 | 13.07 | +0.03171 | Databases, data handling, transactions and information-system terms dominate: `mysql`, `DB`, `formatted`, `transactions`, `Database`, `MySQL`, `response`; extremes include `Form`, `Role`, `Views`, `Hash`, `Forms`, `spacing`. |
| C1 | 347 | 1,262 / 1,861 | 12.64 | +0.03209 | Replacement characters, multilingual fragments and malformed lexical residues dominate. |
| C2 | 346 | 1,595 / 1,736 | 14.24 | +0.03141 | Function words and short lexical fragments dominate: `of`, `is`, `was`, `have`, `all`, `and`, `like`, `am`, plus partial forms. |
| C3 | 306 | 1,239 / 1,652 | 13.50 | +0.03111 | Task/access/work/information-handling actions dominate: `travelling`, `initiating`, `accessing`, `Working`, `Having`, `giving`, `extracted`, `maintaining`, `withdrawing`; extremes include `seeking`, `solved`, `resolving`, `recognized`, `referenced`. |
| C4 | 306 | 1,308 / 1,767 | 14.32 | +0.03173 | Biomedical and physical-science concepts coexist: `immunosuppressive`, `neurodegenerative`, `conformational`, `glucocortic`, `inflammatory`, `metabolic`, `substances`, `rheumatoid` with `renormalization`, `Spin`, `carbon`, `surfaces`, `Gas`, `coherence`. |
| C5 | 278 | 1,114 / 1,677 | 14.05 | +0.03185 | Psychology/social life, politics, finance and sport coexist: `psychosocial`, `psychological`, `political`, `communities`, `emotional`, `parliamentary`, `financial`, `reimbursement`, `basketball`, `psychiat`. |
| C6 | 237 | 1,095 / 1,136 | 14.03 | +0.03095 | Cities, countries, nationalities and place/person names form a coherent geographic/name domain. |
| C7 | 230 | 913 / 1,282 | 13.51 | +0.03140 | Discourse, temporal and evaluative/adverbial language dominates: `Subsequently`, `Eventually`, `Alternatively`, `Anyway`, `professionally`, `Active`, `unsatisfactory`, `Following`. |
| C8 | 168 | 990 / 374 | 14.01 | +0.03174 | Strong punctuation/bracket/code-formatting cluster; 134 of 168 tokens are punctuation/symbols. |
| C9 | 111 | 396 / 647 | 12.96 | +0.03265 | Acronyms, initialisms and short technical/scientific abbreviations dominate. |
| C10 | 99 | 368 / 573 | 13.22 | +0.03238 | Food, nutrition and domestic/agricultural animals form a coherent living/consumption cluster. |
| C11 | 85 | 491 / 199 | 13.89 | +0.03038 | Strong numeric cluster. |
| C12 | 29 | 124 / 132 | 13.10 | +0.03200 | Calendar years, weekdays and seasons form a coherent time cluster. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 472 | 2,144 / 1,985 | 13.29 | -0.03032 | Personal names and name-like entities dominate; no common social domain links them. |
| C1 | 464 | 2,061 / 2,347 | 13.94 | -0.03055 | Negative evaluation, adversity, destruction and distress dominate: `disappointment`, `destroys`, `unconstitutional`, `unacceptable`, `destroyed`, `tragedy`, `terrifying`, `Delete`; extremes include `authority`, `madness`, `fault`. |
| C2 | 446 | 2,082 / 2,247 | 14.37 | -0.03045 | Analysis/assessment and clinical diagnostics coexist: `Characteristics`, `assessments`, `analysis`, `interpretation`, `descriptions`, `manifestations`, `constructions` with `echocardiography`, `pathophysiology`, `angiography`; extremes include `robustness`, `variability`, `biomarkers`, `covariance`. |
| C3 | 332 | 1,601 / 1,677 | 14.70 | -0.03067 | Function words, suffixes and lexical fragments dominate. |
| C4 | 311 | 1,137 / 1,677 | 12.70 | -0.03096 | Negative/contrastive stems and incomplete forms dominate: `brilli`, `catast`, `comp`, `unmist`, `discontin`, `unsatisf`, `arrog`, `imposs`, `abol`, `discour`. |
| C5 | 291 | 1,315 / 1,602 | 14.54 | -0.03116 | Religious/institutional roles, authority, crime and places coexist: `Archbishop`, `priest`, `Constitution`, `technicians`, `officer`, `Palace`, with `goddess`, `thief`, `Devil`, `Rabbi`, `officials`. |
| C6 | 228 | 872 / 1,312 | 13.40 | -0.03107 | Built environment and transport mix with weapons/violence: `staircase`, `hallway`, boats, cliffs, guns, sword, trucks, corridor, plus `murders`, `kill`, shots, barrel and nozzle. |
| C7 | 138 | 520 / 786 | 13.23 | -0.03080 | Anatomy/clinical biology and clothing/body-surface terms coexist: abdomen, cerebellum, skull, epidermis, erythrocytes, gluc, torso alongside uniforms, robe, clad. |
| C8 | 137 | 813 / 225 | 13.51 | -0.03108 | Strong mathematical/code punctuation cluster; 128 of 137 tokens are punctuation/symbols. |
| C9 | 106 | 605 / 225 | 13.54 | -0.03000 | Numeric strings, especially historical years, dominate. |
| C10 | 95 | 268 / 605 | 12.01 | -0.03090 | Programming, low-level computing and data-stream systems are coherent: hw, compiler, databind, logs, Decoder, Writer, io, DAC, Stream, with drv, sdk, debug, png, src among extremes. |
| C11 | 83 | 290 / 405 | 11.87 | -0.03143 | Multilingual suffixes and orthographic fragments dominate. |
| C12 | 49 | 202 / 235 | 13.04 | -0.03251 | Abstract algebra and notation are coherent: morphisms, bigoplus, commutative, functor, homomorphism, subset, setminus, homogeneous; extremes include uniform, zero, quotient, bounded, nonzero. |

## Population accounting

### Positive head

Total nodes: **2,951**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,635 | 55.4% |
| Formal substrate | 1,057 | 35.8% |
| Irreducible semantic | 259 | 8.8% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,951** | **100.0%** |

Semantic-eligible denominator: **1,894 nodes**.

### Negative tail

Total nodes: **3,152**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,429 | 45.3% |
| Formal/name substrate | 1,441 | 45.7% |
| Irreducible semantic | 144 | 4.6% |
| Mixed unresolved | 138 | 4.4% |
| Unclear | 0 | 0.0% |
| **Total** | **3,152** | **100.0%** |

Semantic-eligible denominator: **1,711 nodes**.

## Positive-side reconstruction

### P+0 — Information systems and task/work operations

- **Primary children:** C0, C3
- **Primary nodes:** 715
- **Side-relative coverage:** 24.2%
- **Semantic-eligible coverage:** 37.8%
- **Confidence:** High

**Evidence.** C0 contains databases, data handling, transactions and information
systems; C3 contains access, work and information-handling actions. Their direct
relation contains **340 token edges**, mean cosine **0.10167**, one of the
strongest positive semantic relations in the state.

**Secondary link:** C7. C3–C7 has **282 edges**, mean cosine **0.09606**, and
C0–C7 has **172**, showing that discourse/evaluation often modifies or frames
task/information activity.

**Exclusion boundary.** C7 contains general discourse and temporal modifiers,
not information-specific operations. C9 is abbreviation form rather than one
technical domain.

**Alternative.** Absorb C7 under a broader
`information/task processing and evaluation` parent. Rejected because C7's
general temporal and discourse semantics extend beyond information systems.

### P+1 — Psychosocial, political and geographic organisation

- **Primary children:** C5, C6
- **Primary nodes:** 515
- **Side-relative coverage:** 17.5%
- **Semantic-eligible coverage:** 27.2%
- **Confidence:** Moderate

**Evidence.** C5 contains psychosocial, psychological, political, financial,
administrative and community terms; C6 contains geographic/nationality and
place/person entities. Their direct relation contains **217 token edges**, mean
cosine **0.09341**. The common structure is populations and their
social/institutional context.

**Secondary link:** C7. C5–C7 has **178 edges**, mean cosine **0.10090**,
consistent with discourse/evaluation describing social and political context.

**Exclusion boundary.** Sport and psychiatric material inside C5 remain real
heterogeneity. C6's personal-name component is not sufficient to redefine the
parent as generic named entities.

**Alternative.** Leave C5 and C6 separate. This remains plausible because C5
is broad and mixed; parent confidence is therefore Moderate.

### P+2 — Biomedical, physical-scientific and living/consumption systems

- **Primary children:** C4, C10
- **Primary nodes:** 405
- **Side-relative coverage:** 13.7%
- **Semantic-eligible coverage:** 21.4%
- **Confidence:** Moderate

**Evidence.** C4 supplies biomedical, molecular and physical-science concepts;
C10 supplies food, nutrition and living/animal material. Their direct relation
contains **110 token edges**, mean cosine **0.08747**. The shared higher-order
structure is biological/living systems and substances.

**Secondary link:** C5. C4–C5 has **255 edges**, mean cosine **0.09783**,
reflecting strong psychosocial/health overlap.

**Exclusion boundary.** Physical-science terms in C4 and ordinary food/animal
terms in C10 are preserved rather than collapsed into a narrowly biomedical
parent.

**Alternative.** Keep C4 and C10 separate. This is a serious alternative
because their direct relation is weaker than the other positive parent pairs.

### Positive irreducible structures

- **C7 — irreducible-semantic:** discourse, temporal and evaluative/adverbial
  language; secondary links to P+0 and P+1.
- **C12 — irreducible-semantic:** calendar years, weekdays and seasons.

### Positive formal substrate

- C1 — multilingual/malformed fragments
- C2 — grammar/function words/fragments
- C8 — punctuation/formatting
- C9 — acronyms/initialisms
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Adverse-state evaluation, assessment and clinical characterisation

- **Primary children:** C1, C2
- **Primary nodes:** 910
- **Side-relative coverage:** 28.9%
- **Semantic-eligible coverage:** 53.2%
- **Confidence:** High / Moderate

**Evidence.** C1 centres on negative evaluation, adversity, destruction and
distress. C2 centres on characteristics, assessments, analysis,
interpretation, manifestations and clinical diagnostics. Their relation is the
strongest negative-side relation by a large margin: **631 token edges**, mean
cosine **0.10173**. A defensible common generator is the evaluation and
characterisation of adverse, abnormal or problematic states.

**Secondary links:**
- **C7:** clinical anatomy/body-surface material; C2–C7 has **187 edges**,
  mean cosine **0.10304**.
- **C10:** computing/data infrastructure; C2–C10 has **131 edges**.
- **C12:** mathematical abstraction; C2–C12 has **61 edges**.

**Exclusion boundary.** C1 includes legal/social adversity as well as
destruction, while C2 includes neutral analytical description and clinical
measurement. The parent is therefore not labelled simply “pathology” or
“negative evaluation”. C5 and C6 concern actors/settings of conflict rather
than assessment itself.

**Alternative.** Split C1 and C2 into separate parents or irreducible
structures: one adverse-evaluative, one analytical/clinical. This is the
strongest alternative because the semantic distinction is real despite the
exceptionally dense graph relation.

### P-1 — Institutional/religious authority and conflict environment

- **Primary children:** C5, C6
- **Primary nodes:** 519
- **Side-relative coverage:** 16.5%
- **Semantic-eligible coverage:** 30.3%
- **Confidence:** Moderate

**Evidence.** C5 contains institutional, religious and authority roles plus
crime/place material. C6 contains built environments, transport, weapons and
violence. Their direct relation contains **227 token edges**, mean cosine
**0.09536**. Together they plausibly describe actors/institutions and the
physical/conflict environment in which social order or transgression occurs.

**Secondary link:** C7. C6–C7 has **117 edges** and C5–C7 **54**; body/clothing
terms can participate in embodied social scenes, but C7 is too mixed for
primary inclusion.

**Exclusion boundary.** C5 includes many non-conflict religious/institutional
roles; C6 includes ordinary buildings, transport and objects. The parent is
therefore broader than violence but narrower than “human world”.

**Alternative.** Leave C5 and C6 separate as an institutional-role island and a
mixed physical/conflict-setting community. This remains a serious alternative,
so confidence is Moderate.

### Negative irreducible and unresolved structures

- **C7 — mixed-unresolved:** anatomy/clinical biology plus clothing/body-surface
  terms; secondary links to both P-0 and P-1.
- **C10 — irreducible-semantic:** programming/low-level computing/data streams;
  secondary link to P-0.
- **C12 — irreducible-semantic:** abstract algebra/mathematical notation;
  secondary link to P-0.

### Negative formal/name substrate

- C0 — personal names
- C3 — grammar/function words/suffixes
- C4 — negative/contrastive stems
- C8 — mathematical/code punctuation
- C9 — numeric strings
- C11 — multilingual morphology

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 409 | Databases/data/transactions/info systems | parent:P+0 | — | Information-system infrastructure. |
| + | C1 | 347 | Multilingual/malformed fragments | formal-substrate | — | Tokeniser/orthographic form. |
| + | C2 | 346 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 306 | Task/access/work/info actions | parent:P+0 | — | Operations on/through information systems. |
| + | C4 | 306 | Biomedical + physical science | parent:P+2 | — | Biological/scientific core dominates. |
| + | C5 | 278 | Psychology/social/politics/finance/sport | parent:P+1 | P+2 | Social/institutional core with health overlap. |
| + | C6 | 237 | Cities/countries/nationalities/names | parent:P+1 | — | Geographic/population domain. |
| + | C7 | 230 | Discourse/temporal/evaluative language | irreducible-semantic | P+0, P+1 | Cross-domain contextual/evaluative structure. |
| + | C8 | 168 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C9 | 111 | Acronyms/initialisms | formal-substrate | — | Abbreviation form dominates. |
| + | C10 | 99 | Food/nutrition/animals | parent:P+2 | — | Living/consumption-system structure. |
| + | C11 | 85 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C12 | 29 | Calendar time/years/weekdays | irreducible-semantic | — | Coherent time structure. |
| − | C0 | 472 | Personal names | formal-substrate | — | Name-form organisation without one domain. |
| − | C1 | 464 | Negative evaluation/adversity/destruction | parent:P-0 | — | Adverse-state evaluation. |
| − | C2 | 446 | Analysis/assessment + clinical diagnostics | parent:P-0 | — | Assessment and characterisation of states. |
| − | C3 | 332 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 311 | Negative/contrastive stems | formal-substrate | — | Morphological form dominates. |
| − | C5 | 291 | Religious/institutional roles + crime/places | parent:P-1 | — | Institutional/social-order actors. |
| − | C6 | 228 | Built/transport + weapons/violence | parent:P-1 | — | Physical/conflict environment. |
| − | C7 | 138 | Anatomy/clinical + clothing/body surface | mixed-unresolved | P-0, P-1 | Dual clinical/embodied-surface structure. |
| − | C8 | 137 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C9 | 106 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 95 | Programming/low-level computing/data streams | irreducible-semantic | P-0 | Technical infrastructure adjacent to analysis. |
| − | C11 | 83 | Multilingual suffixes/fragments | formal-substrate | — | Morphological/orthographic form. |
| − | C12 | 49 | Abstract algebra/notation | irreducible-semantic | P-0 | Formal analytical abstraction. |

Every State 06 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information systems and task/work operations | C0, C3 | 715 | 24.2% | 37.8% | High |
| P+1 | Psychosocial, political and geographic organisation | C5, C6 | 515 | 17.5% | 27.2% | Moderate |
| P+2 | Biomedical, physical-scientific and living/consumption systems | C4, C10 | 405 | 13.7% | 21.4% | Moderate |
| P-0 | Adverse-state evaluation, assessment and clinical characterisation | C1, C2 | 910 | 28.9% | 53.2% | High / Moderate |
| P-1 | Institutional/religious authority and conflict environment | C5, C6 | 519 | 16.5% | 30.3% | Moderate |

Positive retained parents account for **1,635 nodes**, **55.4% of the positive
population** and **86.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,429 nodes**, **45.3% of the negative
population** and **83.5% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — information/social activity relation — High.**
   C0–C5 has **352 edges**, C3–C5 **273**, and C0–C6 **116**. Information and
   task systems are strongly embedded in social, political and financial
   contexts.

2. **P+0 ↔ P+2 — information/scientific relation — High.**
   C0–C4 has **345 edges** and C3–C4 **193**. Scientific/biomedical material is
   strongly coupled to data and task operations.

3. **P+1 ↔ P+2 — psychosocial/health relation — High.**
   C4–C5 has **255 edges**, and C4–C6 has **121**. Health/science and
   psychosocial/political organisation are tightly connected without becoming
   one parent.

4. **C7 is an evaluative/contextual bridge-like irreducible structure.**
   C3–C7 has **282 edges**, C5–C7 **178**, and C0–C7 **172**.

### Negative-side relations

1. **P-0 ↔ P-1 — evaluation/analysis and social-conflict relation — High.**
   C1–C5 has **314 edges**, C1–C6 **274**, C2–C5 **279**, and C2–C6 **226**.
   Adverse-state assessment is strongly embedded in institutional and conflict
   contexts without being reducible to them.

2. **P-0 ↔ C7 — clinical/body relation — Moderate.**
   C2–C7 has **187 edges**, but C7's clothing/body-surface component prevents
   primary absorption.

3. **P-0 ↔ C10/C12 — technical/formal analytical satellites — Moderate.**
   C2–C10 has **131 edges** and C2–C12 **61**. Computing and mathematics support
   analytical structure without becoming the same semantic parent.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The strongest compact State 06 cross-side evidence is dominated by formatting,
case/lexical variants, numerics and near-form correspondences. It does not
independently establish a parent-level semantic bridge.

Plausible but unpromoted semantic correspondences include:

- positive P+0 and negative C10 through information/computing systems;
- positive P+2 and negative P-0 through biomedical/clinical structure;
- positive P+1 and negative P-1 through institutional/social organisation.

These remain correspondences rather than bridge candidates.

## Formal/representational substrate

### Positive — 1,057 nodes / 35.8%

- multilingual/malformed fragments;
- grammar/function words;
- punctuation/formatting;
- acronyms/initialisms;
- numeric strings.

### Negative — 1,441 nodes / 45.7%

- personal names;
- grammar/function words/suffixes;
- negative/contrastive lexical stems;
- mathematical/code punctuation;
- numeric strings;
- multilingual morphology.

## Minimal state-level architecture

```text
STATE 06 — BLOCK 5 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION SYSTEMS & TASK/WORK OPERATIONS
|   +-- C0 databases/data/transactions
|   `-- C3 task/access/work/info actions
|       \
|        -- C7 discourse/evaluation                 [secondary]
|
+-- P+1 PSYCHOSOCIAL / POLITICAL / GEOGRAPHIC ORGANISATION
|   +-- C5 psychology/social/politics/finance
|   `-- C6 cities/countries/nationalities
|       \
|        -- C7 discourse/evaluation                 [secondary]
|
+-- P+2 BIOMEDICAL / PHYSICAL-SCIENTIFIC / LIVING-CONSUMPTION SYSTEMS
|   +-- C4 biomedical + physical science
|   `-- C10 food/nutrition/animals
|
+-- C7 discourse/temporal/evaluative language        [irreducible]
+-- C12 calendar/time                                [irreducible]
`-- C1,C2,C8,C9,C11                                 [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADVERSE-STATE EVALUATION / ASSESSMENT / CLINICAL CHARACTERISATION
|   +-- C1 negative evaluation/adversity/destruction
|   `-- C2 analysis/assessment + clinical diagnostics
|       |
|       +-- C7 anatomy/body-surface                  [secondary; mixed]
|       +-- C10 low-level computing                  [secondary]
|       `-- C12 abstract algebra                    [secondary]
|
+-- P-1 INSTITUTIONAL/RELIGIOUS AUTHORITY & CONFLICT ENVIRONMENT
|   +-- C5 institutional/religious roles + crime/places
|   `-- C6 built/transport + weapons/violence
|       \
|        -- C7 anatomy/body-surface                 [secondary; mixed]
|
+-- C7 anatomy/clinical + clothing/body surface      [mixed unresolved]
+-- C10 low-level computing/data streams             [irreducible]
+-- C12 abstract algebra/notation                     [irreducible]
`-- C0,C3,C4,C8,C9,C11                              [formal/name substrate]
```

The preferred State 06 reconstruction contains three positive and two negative
multi-community parents. The positive semantic population is organised around
information/task systems, psychosocial-geographic organisation and
biological/scientific/living systems. The negative population is dominated by
a large adverse-state evaluation/assessment structure and a separate
institutional/conflict-environment structure.

This statement is local to State 06 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction splits negative P-0 into two structures:

1. adverse/destructive evaluation (C1);
2. analytical/clinical characterisation (C2).

That alternative preserves a clearer semantic distinction but sacrifices the
most substantial higher-order relation in the state: C1–C2 has **631 token
edges**, with a shared orientation towards evaluating or characterising
problematic/abnormal states.

The preferred reconstruction therefore keeps the higher-order parent but marks
its confidence as High/Moderate rather than treating the child domains as
identical.

A second alternative leaves positive C4 and C10 separate rather than joining
them under a broad living/biological parent; that remains plausible because
their direct graph relation is weaker than the other positive parent pairs.

## Uncertainty record

- **Procedural contamination:** State 07 rows were incidentally returned by two
  over-wide source ranges. They were not used, but strict Phase-A source
  isolation was technically breached.
- **Negative P-0:** this is the main semantic boundary decision. Its graph
  support is exceptionally strong, but adverse evaluation and clinical
  assessment remain distinct child functions.
- **Negative P-1:** Moderate because its children contain both ordinary
  institutional/built-world material and conflict/violence.
- **Negative C7:** genuinely mixed clinical/anatomical and clothing/body-surface
  organisation; it is not forced into either parent.
- **Positive P+2:** Moderate because physical science in C4 and ordinary
  food/animal terms in C10 broaden the common living-system abstraction.
- **Positive C7:** remains irreducible despite strong connections across two
  parents.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **26 / 26**
- Positive node accounting: **2,951 / 2,951**
- Negative node accounting: **3,152 / 3,152**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 06 community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- State 07 evidence used in State 06 inference: **no**
- Strict state-isolation source exposure breach: **yes — recorded**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as the State 06 hypothesis produced from State 06
evidence. It must not be retroactively renamed or restructured merely to
improve correspondence with another state.

Because incidental State 07 source exposure occurred, the Phase-A completeness
verification must explicitly decide whether State 06 requires a clean rerun
before Phase B.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
