# R010 State 09 — Block 8 output latent structure

## State identity

- R010 state index: `09`
- R008/R009 state: `block_08_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 12 negative-tail = 25**
- R008 population: **3,059 positive-head + 2,942 negative-tail = 6,001 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 09 only. Retrieval and graph inspection were
bounded to `state_index=9 / block_08_output`. No later-state evidence was used.

## Evidence inventory

For every State 09 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_09_block_08_output.md`;
2. all 25 State 09 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. all 144 State 09 within-side community relations in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 500 | 2,233 / 2,469 | 13.87 | +0.03136 | Administration, evaluation, finance and task-resolution language coexist: `determinations`, `administrative`, `acceptable`, `Financial`, `Political`, `satisfactory`, `resolving`, `initiating`, `unsatisfactory`, `management`; extremes include employment, fellowship, threatened, solved, Managed and mediation. |
| C1 | 449 | 1,770 / 2,267 | 12.93 | +0.03196 | Interaction/process concepts mix with databases, computation and physical science: `interactions`, `activities`, `renormalization`, `createElement`, `development`, `transactions`, `DB`, `forms`, `actions`, `coupling`, `mysql`; extremes include Spin, Hash, uploads and lengths. |
| C2 | 421 | 1,873 / 2,159 | 14.03 | +0.03099 | Common grammatical/function words and short lexical fragments dominate. |
| C3 | 398 | 1,819 / 2,107 | 14.43 | +0.03095 | Biomedical, immune, psychiatric and cellular terminology dominates: immunosuppressive, neurodegenerative, psychosocial, conformational, glucocorticoid fragments, psychological, immunodeficiency fragments, psychiatric, biodegradable fragments and intracellular; extremes include mitotic, rheumatoid, regeneration and overweight. |
| C4 | 283 | 1,269 / 1,250 | 13.39 | +0.03099 | Cities, countries and personal/place names form a coherent geographic/name domain: Atlanta, Indonesian, Charleston, Springfield, Nigerian, Terry, Anne, Orlando, Bradley, Mumbai and Sacramento. |
| C5 | 204 | 650 / 1,212 | 12.31 | +0.03188 | Multilingual, malformed and fragmentary tokenisation residues dominate. |
| C6 | 195 | 1,133 / 464 | 14.00 | +0.03170 | Strong punctuation/bracket/code-formatting cluster; 146 of 195 tokens are punctuation/symbols. |
| C7 | 157 | 528 / 1,016 | 13.20 | +0.03234 | Travel, food, literature/culture and biological/agricultural material coexist: travelling, rice, literary, culinary, theatre, fibres, cafe, randomised, Shakespeare fragment, fungal and feeding; extremes add games, resort, Casino, fry and flowering. |
| C8 | 129 | 440 / 781 | 12.88 | +0.03168 | Work, daily life, seasonal/time and renewal language coexist: Working, Day, living, keeping, walking, freshly, winter, January, Halloween and sprang; extremes include Week, seasonal, renew, laying and nodded. |
| C9 | 115 | 706 / 228 | 14.26 | +0.03062 | Strong numeric cluster, including years. |
| C10 | 100 | 306 / 606 | 12.18 | +0.03158 | Acronyms, initialisms and short technical/biomedical abbreviations dominate. |
| C11 | 70 | 234 / 530 | 14.26 | +0.03177 | Culture, society, communities and environmental/social descriptors are coherent: cultural, culturally, professionally, electronically, communities, environmentally, socially, civilized, societal and nationality. |
| C12 | 38 | 118 / 265 | 13.18 | +0.03148 | Publishing, acknowledgements, references and review/paratext language is coherent: Acknowledgements, Thank, Bibliography, Publishing, praised, thanks, Books and advertising; extremes include References, Penguin, Dear and Review. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 517 | 2,444 / 2,346 | 13.99 | -0.03104 | Built environment, institutions/religion and violence/conflict coexist: hallway, Cathedral, Constitution, palace, uniforms, trucks, murders, disasters, priest, massacre and Archbishop; extremes include shots, Chair, Devil, speakers, thief, Territory and roads. |
| C1 | 464 | 1,946 / 1,956 | 12.60 | -0.03133 | Negative/contrastive lexical stems and incomplete forms dominate. |
| C2 | 418 | 1,726 / 2,189 | 13.50 | -0.03093 | Analysis, scientific description, technology and experimental concepts dominate: environments, Characteristics, technologies, analysis, recommendations, Analyses, concepts, Experiments, hardware and circumstance; extremes include Features, variability, robustness, quotient, uniform and codec. |
| C3 | 378 | 1,589 / 1,982 | 13.65 | -0.03052 | Regulation, exclusion, destruction and compositional change dominate: unconstitutional, destroys, requirement, unreasonable, exclude, inconsistent, precluded, creates, eliminated, Remove, combines and indistinguishable; extremes include Delete, reject, authority and composed. |
| C4 | 285 | 1,338 / 1,517 | 14.71 | -0.03096 | Common grammatical/function words, suffixes and lexical fragments dominate. |
| C5 | 153 | 672 / 770 | 13.82 | -0.03088 | Clinical diagnostics, anatomy and pathology are coherent: echocardiography, angiography, cerebellum, phenotypes, abdomen, epithelium, pelvis, symptoms, physiology, torso and epidermis; extremes include erythrocytes, allele, therapy and gait. |
| C6 | 152 | 625 / 910 | 14.21 | -0.03067 | Negative affect, tragedy, fear and loud/vocal expression dominate: horrific, incredible, tragedy, stunning, disappointing, screamed, sadness, terrifying, furious, loud and scream. |
| C7 | 144 | 639 / 731 | 13.95 | -0.03102 | Personal names dominate but geographic/media entities such as Calgary, province, Telegraph, Mirror, Gates and borough are substantial. |
| C8 | 120 | 722 / 220 | 13.87 | -0.03055 | Strong mathematical/code punctuation cluster; 110 of 120 tokens are punctuation/symbols. |
| C9 | 115 | 372 / 673 | 12.32 | -0.02964 | Low-level computing/electronics abbreviations and hardware tokens are evident: GCC, emitter, LED, GPIO, FFFF, CI, HW, DP and LLP; short letter codes add noise. |
| C10 | 108 | 661 / 194 | 14.04 | -0.03059 | Numeric strings, especially historical years, dominate. |
| C11 | 88 | 374 / 366 | 12.66 | -0.03160 | Multilingual words, suffixes and orthographic fragments dominate. |

## Population accounting

### Positive head

Total nodes: **3,059**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,302 | 42.6% |
| Formal/name substrate | 1,035 | 33.8% |
| Irreducible semantic | 565 | 18.5% |
| Mixed unresolved | 157 | 5.1% |
| Unclear | 0 | 0.0% |
| **Total** | **3,059** | **100.0%** |

Semantic-eligible denominator: **2,024 nodes**.

### Negative tail

Total nodes: **2,942**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,216 | 41.3% |
| Formal/name substrate | 1,209 | 41.1% |
| Irreducible semantic | 0 | 0.0% |
| Mixed unresolved | 517 | 17.6% |
| Unclear | 0 | 0.0% |
| **Total** | **2,942** | **100.0%** |

Semantic-eligible denominator: **1,733 nodes**.

## Positive-side reconstruction

### P+0 — Operational, transactional and interaction systems

- **Primary children:** C0, C1
- **Primary nodes:** 949
- **Side-relative coverage:** 31.0%
- **Semantic-eligible coverage:** 46.9%
- **Confidence:** Moderate / High

**Evidence.** C0 contains administration, evaluation, finance, management and
task-resolution language. C1 contains interactions, activities, development,
transactions, databases, forms and actions. Their direct relation is the
strongest positive intercommunity relation in the state: **575 token edges**,
mean cosine **0.09288**. The common structure is organised activity in which
tasks, transactions and interactions are initiated, managed, evaluated and
resolved.

**Secondary links:** C8 and C12. C0–C8 has **186 edges** and C0–C12 **68**;
daily work/time activity and publishing/paratext can participate in organised
operational processes without becoming primary children.

**Exclusion boundary.** C1 contains genuine physical-science terms, and C0
contains political/evaluative language. The parent therefore does not absorb
C3 merely because C0–C3 (**492 edges**) and C1–C3 (**443**) are dense. C3 has a
distinct biomedical domain identity.

**Alternative.** Split C0 and C1 into administrative/task and
interaction/technical-system structures. This preserves their mixed-domain
differences but loses the strongest shared operational relation in the
positive graph.

### P+1 — Geographic and social-cultural identity

- **Primary children:** C4, C11
- **Primary nodes:** 353
- **Side-relative coverage:** 11.5%
- **Semantic-eligible coverage:** 17.4%
- **Confidence:** Moderate

**Evidence.** C4 supplies cities, countries and personal/place names; C11
supplies culture, society, communities, nationality and environmental/social
descriptors. Their direct relation is smaller by edge count (**49 edges**) but
has high mean cosine **0.11445**. The common structure is geographic and
social-cultural identity or population context.

**Secondary link:** C0. C0–C4 has **162 edges** and C0–C11 **134**, reflecting
administrative/political organisation around geographic/social populations.

**Exclusion boundary.** C4 includes personal names as well as places, while C11
contains general descriptors such as electronically and professionally. The
parent is therefore not broadened to generic named entities or generic social
language.

**Alternative.** Treat C4 as a name/geography island and C11 as irreducible
social-cultural discourse. This is a serious alternative, so confidence
remains Moderate.

### Positive irreducible and unresolved structures

- **C3 — irreducible-semantic:** biomedical, immune, psychiatric and cellular
  terminology. It is strongly connected to P+0 but remains a distinct domain.
- **C8 — irreducible-semantic:** work/daily-life, seasonal/time and renewal
  language; secondary relation to P+0.
- **C12 — irreducible-semantic:** publishing, acknowledgements, references and
  paratext; secondary relation to P+0.
- **C7 — mixed-unresolved:** travel, food, literature/culture and
  biological/agricultural material. Its C3 relation is substantial (**208
  edges**, mean cosine **0.09870**) but the cultural/travel component blocks
  absorption into a biological parent.

### Positive formal/name substrate

- C2 — grammar/function words/fragments
- C5 — multilingual/malformed fragments
- C6 — punctuation/formatting
- C9 — numeric strings
- C10 — acronyms/initialisms

## Negative-side reconstruction

### P-0 — Scientific/clinical analysis and technical systems

- **Primary children:** C2, C5, C9
- **Primary nodes:** 686
- **Side-relative coverage:** 23.3%
- **Semantic-eligible coverage:** 39.6%
- **Confidence:** Moderate / High

**Evidence.** C2 contains analysis, scientific description, technologies,
experiments, hardware and quantitative concepts. C5 contains clinical
diagnostics, anatomy and pathology. C9 contains low-level
computing/electronics. C2 acts as the hub: C2–C5 has **186 edges**, mean cosine
**0.09576**, and C2–C9 **142 edges**, mean cosine **0.08864**. C5–C9 is weaker
(**45 edges**), so the structure is best understood as analytical/scientific
organisation supported by clinical and technical-system subdomains.

**Exclusion boundary.** C9's short-code noise is preserved, and C5 remains a
clinical domain rather than generic science. C3 concerns regulation/change,
not scientific characterisation.

**Alternative.** Define P-0 only from C2+C5 and leave C9 irreducible. This is a
serious alternative because the clinical-computing relation is weaker than
their separate relations to C2.

### P-1 — Regulation, destructive change and adverse affect

- **Primary children:** C3, C6
- **Primary nodes:** 530
- **Side-relative coverage:** 18.0%
- **Semantic-eligible coverage:** 30.6%
- **Confidence:** High

**Evidence.** C3 contains regulation, exclusion, destruction, removal and
compositional change. C6 contains tragedy, fear, distress and loud/vocal
expression. Their direct relation contains **231 token edges**, mean cosine
**0.10186**. Together they describe adverse or conflict-laden states and the
actions that prohibit, remove, destroy or transform them.

**Secondary link:** C0. C0–C3 has **392 edges** and C0–C6 **205**. The mixed
built/institution/religion/conflict community clearly supplies actors, settings
and conflict material, but its breadth prevents primary absorption.

**Exclusion boundary.** C3 includes neutral compositional creation as well as
destruction, while C6 is affective/intensity language rather than a change
mechanism. C0 includes ordinary built and institutional material.

**Alternative.** Include C0 as a third child under a broad
`institutional conflict and destructive change` parent. Rejected because
hallways, palaces, trucks, uniforms, religion and public institutions are not
all instances of adverse change.

### Negative mixed unresolved structure

- **C0 — mixed-unresolved:** built environment, institutions/religion and
  violence/conflict. It has a strong secondary relation to P-1 but no single
  retained parent explains the whole community.

### Negative formal/name substrate

- C1 — negative/contrastive lexical stems
- C4 — grammar/function words/fragments
- C7 — personal names plus geographic/media entities
- C8 — mathematical/code punctuation
- C10 — numeric strings
- C11 — multilingual morphology

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 500 | Administration/evaluation/finance/task resolution | parent:P+0 | P+1 | Operational/administrative activity dominates. |
| + | C1 | 449 | Interaction/process + databases/computation/physical science | parent:P+0 | — | Transactional/interaction-system structure dominates. |
| + | C2 | 421 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 398 | Biomedical/immune/psychiatric/cellular | irreducible-semantic | — | Distinct biomedical domain despite dense graph links. |
| + | C4 | 283 | Cities/countries/personal-place names | parent:P+1 | — | Geographic/population identity. |
| + | C5 | 204 | Multilingual/malformed fragments | formal-substrate | — | Tokeniser/orthographic form. |
| + | C6 | 195 | Punctuation/formatting | formal-substrate | — | Formatting organisation. |
| + | C7 | 157 | Travel/food/literature/biological material | mixed-unresolved | — | Multiple organising domains remain material. |
| + | C8 | 129 | Work/daily life/seasonal renewal | irreducible-semantic | P+0 | Operational relation, but distinct temporal/lived structure. |
| + | C9 | 115 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C10 | 100 | Acronyms/initialisms | formal-substrate | — | Abbreviation form dominates. |
| + | C11 | 70 | Culture/society/communities | parent:P+1 | — | Social-cultural population context. |
| + | C12 | 38 | Publishing/acknowledgements/references | irreducible-semantic | P+0 | Organised information-production relation. |
| − | C0 | 517 | Built/institution/religion/conflict | mixed-unresolved | P-1 | Strong conflict-setting relation but broad physical/institutional content. |
| − | C1 | 464 | Negative/contrastive lexical stems | formal-substrate | — | Morphological form dominates. |
| − | C2 | 418 | Analysis/science/technology/experiments | parent:P-0 | — | Scientific/analytical hub. |
| − | C3 | 378 | Regulation/exclusion/destruction/change | parent:P-1 | — | Adverse/regulatory transformation. |
| − | C4 | 285 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C5 | 153 | Clinical diagnostics/anatomy/pathology | parent:P-0 | — | Clinical analytical domain. |
| − | C6 | 152 | Negative affect/tragedy/fear/vocal expression | parent:P-1 | — | Adverse affect/intensity child. |
| − | C7 | 144 | Personal names + geographic/media entities | formal-substrate | — | Name/entity organisation without one semantic class. |
| − | C8 | 120 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C9 | 115 | Low-level computing/electronics | parent:P-0 | — | Technical-system child with acknowledged code noise. |
| − | C10 | 108 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C11 | 88 | Multilingual words/suffixes/fragments | formal-substrate | — | Morphological/orthographic form. |

Every State 09 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Operational, transactional and interaction systems | C0, C1 | 949 | 31.0% | 46.9% | Moderate / High |
| P+1 | Geographic and social-cultural identity | C4, C11 | 353 | 11.5% | 17.4% | Moderate |
| P-0 | Scientific/clinical analysis and technical systems | C2, C5, C9 | 686 | 23.3% | 39.6% | Moderate / High |
| P-1 | Regulation, destructive change and adverse affect | C3, C6 | 530 | 18.0% | 30.6% | High |

Positive retained parents account for **1,302 nodes**, **42.6% of the positive
population** and **64.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,216 nodes**, **41.3% of the negative
population** and **70.2% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ C3 — operational/scientific relation — High.**
   C0–C3 has **492 edges**, mean cosine **0.09979**, and C1–C3 **443** at
   **0.09408**. Biomedical/scientific content is strongly embedded in
   operational and interaction systems without losing its distinct domain
   identity.

2. **P+0 ↔ P+1 — administration/population relation — Moderate to High.**
   C0–C4 has **162 edges**, C0–C11 **134**, C1–C4 **124** and C1–C11 **60**.
   Administrative and operational systems are strongly contextualised by
   geographic/social populations.

3. **C7 ↔ C3 — living/cultural bridge — Moderate.**
   C3–C7 has **208 edges**, mean cosine **0.09870**. The biological/agricultural
   part of C7 connects strongly to biomedical C3, but travel/literature/culture
   blocks a common parent.

4. **C8 and C12 are operational satellites rather than parent children.**
   Their graph links to C0/C1 support relation without requiring semantic
   collapse.

### Negative-side relations

1. **P-0 ↔ P-1 — analysis and regulatory/adverse-change relation — High.**
   C2–C3 has **565 edges**, mean cosine **0.09682**, and C2–C6 **167** at
   **0.10171**. Scientific/analytical description is tightly coupled to
   regulation, exclusion and adverse-state change.

2. **C0 ↔ P-1 — institutional/material conflict setting — High.**
   C0–C3 has **392 edges** and C0–C6 **205**, supporting a strong secondary
   relation without resolving C0's mixed structure.

3. **P-0 technical hierarchy is hub-like rather than uniformly dense.**
   C2 connects strongly to both C5 and C9, while C5–C9 is much weaker. The
   parent therefore represents a higher-order analytical system centred on C2,
   not a flat homogeneous topic.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

No parent-level cross-side relation is required to explain the State 09
within-side architectures, and no stronger cross-side community evidence was
available that justified promotion.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-0 through technical/operational systems;
- positive C3 and negative P-0 through biomedical/clinical structure;
- positive P+1 and negative C0 through institutional/social context.

These remain correspondences rather than bridge claims.

## Formal/representational substrate

### Positive — 1,035 nodes / 33.8%

- grammar/function words and fragments;
- multilingual/malformed fragments;
- punctuation/formatting;
- numeric strings;
- acronyms/initialisms.

### Negative — 1,209 nodes / 41.1%

- negative/contrastive lexical stems;
- grammar/function words/fragments;
- personal-name/geographic-media entity organisation;
- mathematical/code punctuation;
- numeric strings;
- multilingual morphology.

## Minimal state-level architecture

```text
STATE 09 — BLOCK 8 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 OPERATIONAL / TRANSACTIONAL / INTERACTION SYSTEMS
|   +-- C0 administration/evaluation/finance/task resolution
|   `-- C1 interaction/process + databases/computation
|       |
|       +-- C8 daily work/time/renewal               [secondary; irreducible]
|       `-- C12 publishing/paratext                  [secondary; irreducible]
|
+-- P+1 GEOGRAPHIC & SOCIAL-CULTURAL IDENTITY
|   +-- C4 cities/countries/personal-place names
|   `-- C11 culture/society/communities
|
+-- C3 biomedical/immune/psychiatric/cellular         [irreducible]
+-- C7 travel/food/literature/biological material     [mixed unresolved]
+-- C8 work/daily-life/seasonal renewal               [irreducible]
+-- C12 publishing/acknowledgements/references        [irreducible]
`-- C2,C5,C6,C9,C10                                  [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 SCIENTIFIC / CLINICAL ANALYSIS & TECHNICAL SYSTEMS
|   +-- C2 analysis/science/technology/experiments
|   +-- C5 clinical diagnostics/anatomy/pathology
|   `-- C9 low-level computing/electronics
|
+-- P-1 REGULATION / DESTRUCTIVE CHANGE / ADVERSE AFFECT
|   +-- C3 regulation/exclusion/destruction/change
|   `-- C6 negative affect/tragedy/fear/vocal expression
|       \
|        -- C0 built/institution/religion/conflict  [secondary; mixed]
|
+-- C0 built/institution/religion/conflict            [mixed unresolved]
`-- C1,C4,C7,C8,C10,C11                              [formal/name substrate]
```

The preferred State 09 reconstruction is intentionally less compressed on the
positive side than several nearby state-local reconstructions would be if broad
parents were forced. Two positive parents are retained, while biomedical,
daily-life/time, publishing and the large mixed travel/food/culture community
remain outside them. The negative side supports two higher-order structures:
scientific/clinical/technical analysis and regulation/destructive/adverse
change.

This statement is local to State 09 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. absorb positive C3 into P+0 under a broader
   **operational/scientific systems** parent because C0–C3 and C1–C3 are both
   exceptionally dense;
2. define a biological/living parent from positive C3+C7;
3. restrict negative P-0 to C2+C5 and leave C9 irreducible;
4. absorb negative C0 into P-1 as an institutional/material conflict child.

Each improves compression or graph alignment but weakens semantic
discrimination. The preferred reconstruction therefore retains the narrower
parents and leaves heterogeneous communities unresolved.

## Uncertainty record

- **Positive P+0:** both children are mixed; the parent is supported by the
  strongest positive graph relation but remains Moderate/High rather than pure.
- **Positive P+1:** only 49 direct C4–C11 edges support the child pair, although
  their mean cosine is high and the semantic relation is coherent.
- **Positive C3:** extremely strong graph connectivity to P+0 does not erase
  its distinct biomedical identity.
- **Positive C7:** is the main positive unresolved community because biological,
  cultural, travel and food structures coexist.
- **Negative P-0:** C9 is more weakly coupled to C5 than either is to C2;
  P-0 is therefore a hub hierarchy rather than a homogeneous cluster.
- **Negative C0:** remains unresolved despite high connectivity to P-1 because
  its built, religious/institutional and conflict material cannot be reduced to
  one child role.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **12 / 12**
- Total communities accounted for: **25 / 25**
- Positive node accounting: **3,059 / 3,059**
- Negative node accounting: **2,942 / 2,942**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every State 09 community inspected at underlying R008 community-record level: **yes**
- All State 09 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 09 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 09 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
