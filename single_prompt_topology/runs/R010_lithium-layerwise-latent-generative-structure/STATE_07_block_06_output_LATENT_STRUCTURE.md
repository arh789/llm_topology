# R010 State 07 — Block 6 output latent structure

## State identity

- R010 state index: `07`
- R008/R009 state: `block_06_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 12 negative-tail = 24**
- R008 population: **2,934 positive-head + 2,990 negative-tail = 5,924 nodes**
- Status: Phase-A State 07 reconstruction complete, with procedural deviation recorded below

This file reconstructs State 07 only. No R010 reconstruction from another state
was used to shape the parent labels.

## Procedural deviation

During retrieval of the State 07 layer-packet section, the attempted programmatic
section trim failed to stop before the beginning of State 08, causing part of
the State 08 packet to be returned in the tool output.

No State 08 content was used in any State 07 parent inference, relation,
coverage calculation, alternative reconstruction or conclusion. State 07
inference was based only on records explicitly carrying
`state_index=7 / block_06_output`.

The exposure nevertheless violates the strict Phase-A instruction not to inspect
semantic evidence from another state. It is recorded rather than concealed.
State 07 should therefore be treated as **analytically state-local but
procedurally contaminated by incidental State 08 source exposure**. Phase-A
verification must decide whether a clean rerun is required before Phase B.

## Evidence inventory

State 07 inference used only State 07 evidence:

1. `R009/STATE_07_block_06_output.md`;
2. State 07 entries in `R009_SUMMARY.html`;
3. all 24 State 07 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. all State 07 within-side relations in R008 `community_edges.csv`;
5. the State 07 portion of the R008 layer packet and its compact cross-side
   evidence.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 454 | 2,075 / 2,310 | 14.23 | +0.03169 | Biomedical, psychological and inflammatory/therapeutic terminology dominates: `immunosuppressive`, `neurodegenerative`, `psychological`, `psychosocial`, `inflammatory`, `glucocortic`, `regenerative`, `emotional`, `anticancer`, `menopausal`; extremes add mitotic, Immun and personalised treatment language. |
| C1 | 374 | 1,539 / 1,993 | 13.56 | +0.03216 | Work, access, participation and task/process actions dominate: `travelling`, `Working`, `getting`, `accessing`, `initiating`, `participating`, `originating`, `activating`, `researching`; extremes include seeking, solved, resolving, recognised and referenced. |
| C2 | 367 | 1,789 / 1,754 | 14.53 | +0.03174 | Common grammatical/function words and short lexical fragments dominate. |
| C3 | 334 | 1,259 / 1,967 | 13.43 | +0.03217 | Databases, transactions and software/information systems dominate: `Database`, `Connection`, `mysql`, `response`, `DB`, `transactions`, `formatted`, `MySQL`; extremes include Hash, Role, Entry, Server and cycle. |
| C4 | 244 | 957 / 1,453 | 13.80 | +0.03240 | Finance, politics, administration and social/community activity coexist: `Financial`, `political`, `cultural`, `administrative`, `reimbursement`, `business`, `communities`, `basketball`; extremes include employment, Civil, lending, Social, fellowship, franchise and games. |
| C5 | 229 | 1,070 / 1,077 | 14.05 | +0.03168 | Cities, nationalities and place/person names form a coherent geographic/population domain: Pakistani, Indonesian, Cleveland, Charlotte, Mexican, Atlanta, Sacramento, Laura, Charleston, Orlando, Nigerian, California. |
| C6 | 190 | 623 / 1,092 | 12.31 | +0.03208 | Multilingual, malformed and fragmentary tokenisation residues dominate. |
| C7 | 186 | 1,055 / 450 | 13.76 | +0.03201 | Strong punctuation/bracket/code-formatting cluster; 134 of 186 tokens are punctuation/symbols. |
| C8 | 181 | 666 / 1,009 | 12.93 | +0.03224 | Molecular/cell-biology signalling and cell-cycle terms dominate despite abbreviation structure: caspase fragment, cyclin, CDK, Bcl, BRCA, AKT and related biochemical abbreviations. |
| C9 | 161 | 609 / 904 | 13.18 | +0.03101 | Discourse, temporal and evaluative/adverbial language dominates: Eventually, Alternatively, Anyway, Subsequently, unsatisfactory, specific, Following, different; extremes include refreshing, OK, Thank, eventual and pertinent. |
| C10 | 127 | 464 / 738 | 13.12 | +0.03344 | Food, crops and animals form a coherent living/consumption cluster: food, cabbage, cakes, chocolate, rice, coconut, tiger, fish, vegetation and cat; extremes add beet, litter, pig, worm and Bear. |
| C11 | 87 | 524 / 175 | 14.06 | +0.03180 | Numeric strings, including some years, dominate. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 464 | 2,041 / 2,321 | 13.80 | -0.03034 | Analysis, interpretation, recommendation and constraint/regulation dominate: determination, Characteristics, analysis, recommendations, interpretation, environments, prohibited, distinguishes, features, constructing, indistinguishable; extremes include displacement, composed, slated, measure and usage. |
| C1 | 394 | 1,843 / 1,754 | 13.81 | -0.03019 | Personal names and name-like entities dominate. |
| C2 | 388 | 1,722 / 1,794 | 13.50 | -0.03131 | Common grammatical/function words, suffixes and lexical fragments dominate. |
| C3 | 348 | 1,501 / 1,699 | 13.51 | -0.03112 | Clinical diagnostics/anatomy and built-environment/clothing terms coexist: echocardiography, angiography, abdomen, phenotypes, pathophysiology, cerebellum, erythrocytes and biomarkers alongside staircase, hallway, boats, uniforms, stair, nozzle, clad and barrel. |
| C4 | 348 | 1,502 / 1,894 | 14.07 | -0.03106 | Negative evaluation, distress, difference and intensity dominate: disappointment, unconstitutional, unacceptable, terrifying, horrific, dismay, inconsistency, differences, loud, tragedy; extremes include conclusive, robustness, variability, louder, audible and gloom. |
| C5 | 230 | 924 / 1,372 | 14.00 | -0.03028 | Religious/institutional roles, public culture and infrastructure coexist: priest, Archbishop, Constitution, concerts, theolog, Transportation, professor, physician, Cathedral; extremes include Chair, speakers, wireless, composer, broadcasts, officials, Laws and reactors. |
| C6 | 175 | 579 / 1,115 | 12.99 | -0.03142 | Negative/contrastive stems and incomplete lexical forms dominate. |
| C7 | 155 | 557 / 1,109 | 14.34 | -0.03095 | Violence, destruction, crime and threatening/fantastical actors dominate: destroys, destroyed, thief, guns, villain, massacre, murders, killings, murdered, goddess; extremes include Devil, shots, Delete, police, pagan and serpent. |
| C8 | 148 | 426 / 916 | 11.95 | -0.03090 | Low-level computing/hardware is recognisable despite short-token noise: hw, compiler, DAC, LED, Writer, nv; extremes include drv, sdk, Decoder, debug, png, HW and pointer. |
| C9 | 145 | 874 / 232 | 13.66 | -0.03113 | Strong mathematical/code punctuation cluster; 129 of 145 tokens are punctuation/symbols. |
| C10 | 111 | 618 / 281 | 13.67 | -0.03047 | Numeric strings, especially historical years, dominate. |
| C11 | 84 | 313 / 497 | 13.37 | -0.03160 | Mathematical structure is coherent: morphisms, bigoplus, convergence, eigenvalues, variance, covariance, quotient, subset, uniform, zero and reducible. |

## Population accounting

### Positive head

Total nodes: **2,934**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,943 | 66.2% |
| Formal substrate | 830 | 28.3% |
| Irreducible semantic | 161 | 5.5% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,934** | **100.0%** |

Semantic-eligible denominator: **2,104 nodes**.

### Negative tail

Total nodes: **2,990**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,197 | 40.0% |
| Formal/name substrate | 1,213 | 40.6% |
| Irreducible semantic | 232 | 7.8% |
| Mixed unresolved | 348 | 11.6% |
| Unclear | 0 | 0.0% |
| **Total** | **2,990** | **100.0%** |

Semantic-eligible denominator: **1,777 nodes**.

## Positive-side reconstruction

### P+0 — Information systems and work/task operations

- **Primary children:** C1, C3
- **Primary nodes:** 708
- **Side-relative coverage:** 24.1%
- **Semantic-eligible coverage:** 33.7%
- **Confidence:** High

**Evidence.** C1 supplies work, access, participation and task/process actions;
C3 supplies databases, transactions and software/information systems. Their
direct relation contains **413 token edges**, mean cosine **0.09007**. The two
communities form a clear object/operation pair: information systems and the
actions performed through them.

**Secondary link:** C9. C1–C9 has **216 edges**, mean cosine **0.09500**, and
C3–C9 **108**, showing that discourse/evaluation frames task and information
activity.

**Exclusion boundary.** C9 contains general discourse and temporal modifiers,
not information-specific operations. C4 contains social/financial activity but
is not primarily an information-system community.

**Alternative.** Absorb C9 under a broader
`information/task processing and evaluation` parent. Rejected because C9's
general discourse semantics extend well beyond information systems.

### P+1 — Political, social-economic and geographic population organisation

- **Primary children:** C4, C5
- **Primary nodes:** 473
- **Side-relative coverage:** 16.1%
- **Semantic-eligible coverage:** 22.5%
- **Confidence:** High / Moderate

**Evidence.** C4 supplies finance, politics, administration, business,
community and social activity; C5 supplies nationalities, cities and
population/place entities. Their direct relation contains **209 token edges**,
mean cosine **0.09638**. The common structure is organised social populations
and their institutional/economic context.

**Secondary link:** C9. C4–C9 has **101 edges**, consistent with
evaluative/discourse description of social/institutional contexts.

**Exclusion boundary.** Basketball/games in C4 and personal-name material in C5
remain secondary. The parent is not broadened into generic social activity.

**Alternative.** Treat C5 as a geographic entity island and leave C4
irreducible. This remains plausible because C4 is explicitly mixed; confidence
is therefore High/Moderate rather than unqualified High.

### P+2 — Biomedical, cellular and organismal/living systems

- **Primary children:** C0, C8, C10
- **Primary nodes:** 762
- **Side-relative coverage:** 26.0%
- **Semantic-eligible coverage:** 36.2%
- **Confidence:** Moderate to High

**Evidence.** C0 supplies biomedical, inflammatory, psychological and
therapeutic concepts; C8 supplies molecular/cell-cycle signalling terms; C10
supplies foods, crops and animals. The strongest links are C0–C8 at **212
edges**, mean cosine **0.09582**, and C0–C10 at **183 edges**, mean cosine
**0.09123**. C8–C10 is weaker (**47 edges**), so the parent is best understood
as a broad biological/living hierarchy centred on C0 rather than three equally
interconnected children.

**Secondary links:** C4 and C9 through psychosocial/emotional content in C0.

**Exclusion boundary.** Psychological language inside C0 and ordinary
food/animal terms inside C10 prevent a narrowly biomedical label. C8's acronym
form does not make it formal substrate because the underlying terms share a
coherent cell-biology domain.

**Alternative.** Define P+2 only from C0+C8 and retain C10 as an irreducible
food/animal community. This alternative is serious and would be preferred if
broader membership showed weak biological relation between C10 and the other
children.

### Positive irreducible structure

- **C9 — irreducible-semantic:** discourse, temporal and evaluative/adverbial
  language; secondary relations to P+0 and P+1 and a weaker contextual relation
  to P+2.

### Positive formal substrate

- C2 — grammar/function words/fragments
- C6 — multilingual/malformed residues
- C7 — punctuation/formatting
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Assessment, constraint and adverse-state evaluation

- **Primary children:** C0, C4
- **Primary nodes:** 812
- **Side-relative coverage:** 27.2%
- **Semantic-eligible coverage:** 45.7%
- **Confidence:** High

**Evidence.** C0 contains analysis, interpretation, recommendation,
constraint/regulation and characterisation; C4 contains negative evaluation,
distress, difference and intensity. Their relation is the strongest
intercommunity relation in State 07: **577 token edges**, mean cosine
**0.10072**. The higher-order structure is the assessment and regulation of
problematic, discrepant or adverse states.

**Secondary links:**
- **C3:** C0–C3 has **286 edges** and C3–C4 **206**. Its clinical component
  clearly relates to assessment, but its built/clothing component blocks
  primary inclusion.
- **C8:** C0–C8 has **139 edges**; technical systems can support analysis.
- **C11:** C0–C11 has **148 edges**, mean cosine **0.09612**; mathematics
  provides formal analytical structure.

**Exclusion boundary.** C4 contains affective/intensity language beyond formal
assessment; C0 contains neutral analysis and regulatory language. C5 and C7
concern public actors/infrastructure/conflict rather than assessment itself.

**Alternative.** Keep C0 and C4 as separate analytical/regulatory and
adverse-evaluative structures. This preserves semantic distinction but ignores
the exceptional graph coupling; the preferred parent treats them as distinct
children under one higher-order generator.

### P-1 — Institutional/public order and violent transgression

- **Primary children:** C5, C7
- **Primary nodes:** 385
- **Side-relative coverage:** 12.9%
- **Semantic-eligible coverage:** 21.7%
- **Confidence:** Moderate

**Evidence.** C5 contains religious/institutional roles, Constitution, public
culture and infrastructure; C7 contains violence, destruction, crime, police
and threatening/fantastical actors. Their direct relation contains **143 token
edges**, mean cosine **0.10247**. The common structure is social/public order
and its transgression or conflict.

**Secondary link:** C3. C3–C5 has **231 edges** and C3–C7 **163**, making the
mixed clinical/built community a strong physical/embodied bridge to this
structure.

**Exclusion boundary.** Concerts, transportation and medical professions in C5
are not inherently conflictual. C7 includes fantasy actors. The parent is not
reduced to “violence” or broadened to generic public life.

**Alternative.** Leave C5 and C7 separate as public/institutional and
violence/crime communities. This remains a serious alternative, so confidence
is Moderate.

### Negative mixed unresolved structure

- **C3 — mixed-unresolved:** clinical/anatomical and built-environment/clothing
  organisation coexist. It has secondary links to both P-0 and P-1 and is one
  of the clearest state-local bridge-like communities, but no single parent
  explains its full content.

### Negative irreducible structures

- **C8 — irreducible-semantic:** low-level computing/hardware; secondary link
  to P-0.
- **C11 — irreducible-semantic:** algebra/convergence/eigenvalue/statistical
  mathematics; secondary link to P-0.

### Negative formal/name substrate

- C1 — personal names
- C2 — grammar/function words/fragments
- C6 — negative/contrastive stems
- C9 — mathematical/code punctuation
- C10 — numeric strings

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 454 | Biomedical/psychological/inflammatory | parent:P+2 | — | Biomedical/living-system centre. |
| + | C1 | 374 | Work/access/task actions | parent:P+0 | — | Operations performed through systems. |
| + | C2 | 367 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 334 | Databases/transactions/software | parent:P+0 | — | Information-system infrastructure. |
| + | C4 | 244 | Finance/politics/admin/social activity | parent:P+1 | — | Institutional/social-economic organisation. |
| + | C5 | 229 | Cities/nationalities/names | parent:P+1 | — | Geographic/population domain. |
| + | C6 | 190 | Multilingual/malformed residues | formal-substrate | — | Tokeniser/orthographic form. |
| + | C7 | 186 | Punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C8 | 181 | Molecular/cell-biology signalling | parent:P+2 | — | Cellular/biological system. |
| + | C9 | 161 | Discourse/temporal/evaluative language | irreducible-semantic | P+0, P+1 | Cross-domain contextual/evaluative structure. |
| + | C10 | 127 | Food/crops/animals | parent:P+2 | — | Organismal/living-system child. |
| + | C11 | 87 | Numeric strings | formal-substrate | — | Numeric form. |
| − | C0 | 464 | Analysis/interpretation/regulation | parent:P-0 | — | Assessment/constraint structure. |
| − | C1 | 394 | Personal names | formal-substrate | — | Name-form organisation without one domain. |
| − | C2 | 388 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C3 | 348 | Clinical/anatomy + built/clothing | mixed-unresolved | P-0, P-1 | Genuine dual-domain bridge. |
| − | C4 | 348 | Negative evaluation/distress/difference | parent:P-0 | — | Adverse-state evaluation. |
| − | C5 | 230 | Religious/institutional/public culture | parent:P-1 | — | Public/institutional order. |
| − | C6 | 175 | Negative/contrastive stems | formal-substrate | — | Morphological form dominates. |
| − | C7 | 155 | Violence/destruction/crime | parent:P-1 | — | Transgression/conflict structure. |
| − | C8 | 148 | Low-level computing/hardware | irreducible-semantic | P-0 | Technical analytical support. |
| − | C9 | 145 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C10 | 111 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C11 | 84 | Mathematics/convergence/eigenvalues | irreducible-semantic | P-0 | Formal analytical abstraction. |

Every State 07 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information systems and work/task operations | C1, C3 | 708 | 24.1% | 33.7% | High |
| P+1 | Political, social-economic and geographic population organisation | C4, C5 | 473 | 16.1% | 22.5% | High / Moderate |
| P+2 | Biomedical, cellular and organismal/living systems | C0, C8, C10 | 762 | 26.0% | 36.2% | Moderate / High |
| P-0 | Assessment, constraint and adverse-state evaluation | C0, C4 | 812 | 27.2% | 45.7% | High |
| P-1 | Institutional/public order and violent transgression | C5, C7 | 385 | 12.9% | 21.7% | Moderate |

Positive retained parents account for **1,943 nodes**, **66.2% of the positive
population** and **92.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,197 nodes**, **40.0% of the negative
population** and **67.4% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+2 — task/information and biomedical relation — High.**
   C0–C1 has **377 edges**, C0–C3 **433**, C1–C8 **59** and C3–C8 **165**.
   Biomedical/scientific content is strongly embedded in information and task
   systems without becoming reducible to them.

2. **P+0 ↔ P+1 — work/institutional-economic relation — High.**
   C1–C4 has **280 edges**, C3–C4 **245**, and C1–C5 **83**. Work/task and
   information systems are strongly coupled to social/economic organisation.

3. **P+1 ↔ P+2 — psychosocial/population-health relation — High.**
   C0–C4 has **322 edges**, C0–C5 **143**, and C4–C10 **68**. Social,
   political and population contexts are tightly connected to health/living
   systems while remaining distinct.

4. **C9 is a contextual/evaluative bridge-like irreducible structure.**
   It connects to C1 (**216 edges**), C0 (**188**), C3 (**108**) and C4
   (**101**), supporting a cross-domain modifier role without forming a
   multi-community parent.

### Negative-side relations

1. **P-0 ↔ P-1 — regulation/evaluation and public conflict relation — High.**
   C0–C5 has **263 edges**, C0–C7 **219**, C4–C5 **157** and C4–C7 **234**.
   Assessment and adverse-state evaluation are strongly embedded in social
   order/conflict contexts.

2. **C3 bridges P-0 and P-1 — High.**
   C0–C3 has **286 edges**, C4–C3 **206**, C3–C5 **231** and C3–C7 **163**.
   Its clinical and physical-setting components make it structurally adjacent
   to both parents without supporting primary absorption into either.

3. **P-0 ↔ formal technical/quantitative satellites — Moderate.**
   C0–C8 has **139 edges** and C0–C11 **148**. Computing and mathematics
   support analytical structure but remain distinct semantic objects.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The compact State 07 cross-side evidence is dominated by punctuation,
capitalisation/lexical variants, geographic variants and near-identical
calendar forms, including `Australian`↔`Australia` and
`Sunday`↔`Sundays`. These do not establish a parent-level semantic bridge.

Plausible but unpromoted correspondences include:

- positive P+0 and negative C8 through computing/information systems;
- positive P+2 and negative P-0/C3 through biomedical/clinical structure;
- positive P+1 and negative P-1 through social/institutional organisation.

These remain semantic correspondences rather than state-local bridge claims.

## Formal/representational substrate

### Positive — 830 nodes / 28.3%

- grammar/function words and fragments;
- multilingual/malformed residues;
- punctuation/formatting;
- numeric strings.

### Negative — 1,213 nodes / 40.6%

- personal names;
- grammar/function words/suffixes;
- negative/contrastive word stems;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 07 — BLOCK 6 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION SYSTEMS & WORK/TASK OPERATIONS
|   +-- C1 work/access/participation actions
|   `-- C3 databases/transactions/software
|       \
|        -- C9 discourse/evaluation                  [secondary]
|
+-- P+1 POLITICAL / SOCIAL-ECONOMIC / GEOGRAPHIC POPULATION ORGANISATION
|   +-- C4 finance/politics/admin/social activity
|   `-- C5 cities/nationalities/population entities
|       \
|        -- C9 discourse/evaluation                  [secondary]
|
+-- P+2 BIOMEDICAL / CELLULAR / ORGANISMAL-LIVING SYSTEMS
|   +-- C0 biomedical/psychological/inflammatory
|   +-- C8 cell-biology/signalling
|   `-- C10 food/crops/animals
|
+-- C9 discourse/temporal/evaluative language         [irreducible]
`-- C2,C6,C7,C11                                     [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ASSESSMENT / CONSTRAINT / ADVERSE-STATE EVALUATION
|   +-- C0 analysis/interpretation/regulation
|   `-- C4 negative evaluation/distress/difference
|       |
|       +-- C3 clinical + built/clothing              [secondary; mixed]
|       +-- C8 low-level computing                    [secondary]
|       `-- C11 mathematics                          [secondary]
|
+-- P-1 INSTITUTIONAL/PUBLIC ORDER & VIOLENT TRANSGRESSION
|   +-- C5 institutional/public-culture/infrastructure
|   `-- C7 violence/destruction/crime
|       \
|        -- C3 clinical + built/clothing             [secondary; mixed]
|
+-- C3 clinical/anatomy + built/clothing              [mixed unresolved]
+-- C8 low-level computing/hardware                    [irreducible]
+-- C11 mathematics/convergence/eigenvalues            [irreducible]
`-- C1,C2,C6,C9,C10                                  [formal/name substrate]
```

The preferred State 07 reconstruction contains three positive and two negative
multi-community parents. The positive semantic population is highly
compressible into information/task systems, social-geographic organisation and
biological/living systems. The negative population contains a dominant
assessment/adverse-state structure plus a separate public-order/conflict
structure, bridged by a genuinely mixed clinical/physical-setting community.

This statement is local to State 07 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction makes two changes:

1. define positive P+2 only from C0+C8 and leave C10 as an irreducible
   food/animal structure;
2. keep negative C5 and C7 separate rather than joining them under P-1.

Both alternatives preserve narrower semantic purity.

The preferred reconstruction retains the broader parents because the current
state contains enough graph and semantic evidence to support them, but both
remain explicit alternatives rather than being discarded.

## Uncertainty record

- **Procedural contamination:** State 08 packet content was incidentally exposed
  during a failed State 07 section trim. It was not used in State 07 inference,
  but strict Phase-A source isolation was technically breached.
- **Positive P+2:** the C10 food/animal child is less tightly coupled to C8 than
  the biomedical/cellular children are to C0, so the broader living-system
  parent remains Moderate/High rather than unqualified High.
- **Positive P+1:** C4 is mixed and C5 contains some personal names; the
  population/institutional abstraction remains broad.
- **Negative P-1:** the institutional/public and violence/crime communities
  support a higher-order social-order/transgression frame, but they can still
  defensibly remain separate.
- **Negative C3:** is the principal bridge ambiguity; its clinical and
  built/clothing components prevent a single clean parent assignment.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **24 / 24**
- Positive node accounting: **2,934 / 2,934**
- Negative node accounting: **2,990 / 2,990**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 07 community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- State 08 evidence used in State 07 inference: **no**
- Strict state-isolation source exposure breach: **yes — recorded**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as the State 07 hypothesis produced from State 07
evidence. It must not be retroactively renamed or restructured merely to
improve correspondence with another state.

Because incidental State 08 source exposure occurred, Phase-A completeness
verification must explicitly decide whether State 07 requires a clean rerun
before Phase B.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
