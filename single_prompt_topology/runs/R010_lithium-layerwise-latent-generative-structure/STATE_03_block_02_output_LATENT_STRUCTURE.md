# R010 State 03 — Block 2 output latent structure

## State identity

- R010 state index: `03`
- R008/R009 state: `block_02_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **11 positive-head + 15 negative-tail = 26**
- R008 population: **3,167 positive-head + 2,809 negative-tail = 5,976 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 03 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

For every State 03 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_03_block_02_output.md`;
2. State 03 entries in `R009_SUMMARY.html`;
3. all 26 State 03 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. the full State 03 within-side community relation set in
   `R008/community_edges.csv`;
5. the State 03 R008 layer packet, including strongest intercommunity
   relations and compact cross-side evidence.

The private compressed `nodes.csv.gz` artifact could not be decoded through
the available GitHub text connector in this session. No claim is made that full
token-by-token membership was inspected. Under the R010 protocol, communities
whose compact underlying evidence remained materially heterogeneous were kept
Moderate, mixed, irreducible or secondary rather than being promoted through
unsupported certainty.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 510 | 2,540 / 2,341 | 14.55 | +0.03096 | Function words and lexical fragments dominate: `of`, `is`, `was`, `have`, `more`, `am`, `work`, together with short pieces and partial forms. Primarily formal language structure. |
| C1 | 480 | 2,002 / 2,401 | 13.34 | +0.03074 | Biomedical content is substantial (`immunosuppressive`, `angiotensin`, `IGF`, `glucocortic`, `testicular`, `infertility`, `menstrual`), while `Phosph`, `renormalization`, `Spin`, `carbon`, `electronic`, `coherence` establish a real physical-science component. |
| C2 | 399 | 1,669 / 1,991 | 13.36 | +0.03115 | Information/task operations dominate: `accessing`, `formatted`, `retrieving`, `response`, `extracted`, `recognizing`, `initiating`; extremes include `seeking`, `solved`, `remembers`, `Remember`, `working`. |
| C3 | 319 | 1,429 / 1,623 | 14.05 | +0.03115 | Evaluative, affective and contextual/discourse descriptors dominate: `psychosocial`, `extraordinarily`, `emotional`, `Subsequently`, `qualitatively`, `Therefore`, `inevitable`, `interesting`; some technical/contextual outliers remain. |
| C4 | 318 | 1,413 / 1,539 | 13.73 | +0.03108 | Geographic/nationality and institutional descriptors coexist: `Indonesian`, `Nigerian`, `Finnish`, `Australian`, `Ethiop`, `Charleston`, with `Financial`, `Political`, `administrative`, `parliamentary`, `Civil`, `civic`. |
| C5 | 278 | 1,138 / 1,352 | 13.05 | +0.03101 | Acronyms, initialisms and short technical abbreviations dominate. |
| C6 | 267 | 929 / 1,584 | 12.89 | +0.03159 | Websites, databases, forms, transactions and connection/service systems dominate: `sites`, `mysql`, `forms`, `transactions`, `SQL`, `Connection`, `Database`, `MySQL`, `Service`. |
| C7 | 225 | 1,399 / 384 | 14.14 | +0.03188 | Strongly bounded punctuation/bracket/code-formatting cluster; 182 of 225 tokens are punctuation/symbols. |
| C8 | 151 | 870 / 330 | 13.71 | +0.03027 | Strong numeric cluster. |
| C9 | 148 | 567 / 853 | 13.43 | +0.03249 | Food/agriculture/living-system vocabulary dominates: `rice`, `cakes`, `cabbage`, `gardening`, `bread`, `food`, `vegetation`, `chocolate`, `beet`; `athletes`, `basketball` and exercise/sport material form a genuine secondary component. |
| C10 | 72 | 335 / 300 | 13.47 | +0.03075 | Calendar/year/weekday/season structure is coherent: years, Sunday/Monday, weekend, months, seasonality, August and holiday terms. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 355 | 1,597 / 1,668 | 13.70 | -0.03191 | Personal names and titles dominate: `Nick`, `Alex`, `Jeff`, `Alan`, `Josh`, `Jean`, `Kat`, `Thompson`, `Luke`, with title/name fragments. No single social domain links them. |
| C1 | 335 | 1,368 / 1,861 | 13.72 | -0.03193 | Negative evaluation, rejection and adversity dominate: `unconstitutional`, `discour`, `unacceptable`, `catast`, `tragedy`, `uncomfortable`, `annoying`, `disappro`, `disgust`. |
| C2 | 322 | 1,380 / 1,847 | 14.31 | -0.03158 | Analysis, interpretation and scientific description dominate: `determination`, `visualization`, `epidemiology`, `interpretation`, `descriptions`, `phenotypes`, `stabilization`, `technologies`, `methodologies`, `Experiments`; covariance/displacement appear among extremes. |
| C3 | 259 | 1,149 / 1,462 | 14.52 | -0.03234 | Occupations, authority titles and fictional/social roles coexist: `technician`, `Archbishop`, `professor`, `Chairman`, `Congressman`, `officer`, `leaders`, `CEO`, `Princess`, plus goddess/warriors/villain. |
| C4 | 256 | 1,023 / 1,469 | 13.73 | -0.03268 | Built environment, weapons, devices and physical objects coexist: hallways/stairs, guns/firearms, smartphones/devices, clothing, transport, sculptures, cliffs and swords. |
| C5 | 233 | 944 / 1,290 | 13.64 | -0.03138 | Common word pieces, suffixes and grammatical fragments dominate. |
| C6 | 182 | 743 / 992 | 13.62 | -0.03170 | Clinical medicine/diagnostics/pathology is coherent: `echocardiography`, `pathophysiology`, `anesthesia`, `pathogens`, `medications`, `therapies`, `biomarkers`, `abdomen`, `cerebellum`, `angiography`. |
| C7 | 152 | 529 / 730 | 11.76 | -0.03058 | Multilingual, encoding and orthographic fragments dominate. |
| C8 | 149 | 513 / 1,051 | 13.94 | -0.03241 | Violence/crime/prohibition is coherent: `prohibited`, `murdered`, `massacre`, `murder`, `murders`, `uprising`, `kill`, `destroyed`, `prohibition`, `killing`, `slain`; extremes include `arrest`, `indicted`, `fatal`. |
| C9 | 136 | 420 / 794 | 12.01 | -0.03234 | Programming/data/document systems: `detectors`, `addr`, `databind`, `Generator`, `manuscripts`, `Decoder`, `blog`, `compiler`, `plugins`; extremes include `sdk`, `Monitor`, `uint`, `Pointer`. |
| C10 | 134 | 448 / 865 | 13.14 | -0.03227 | Physical action, movement and vocal/sound events: `pulled`, `screamed`, `removed`, `dropped`, `loud`, `hugged`, `snatched`, `shout`, `scream`, `shouted`, `yelled`; positive/neutral actions remain mixed in. |
| C11 | 102 | 577 / 192 | 13.20 | -0.03168 | Strong mathematical/code punctuation cluster; 93 of 102 tokens are punctuation/symbols. |
| C12 | 71 | 255 / 474 | 13.86 | -0.03238 | Government/law/public-institution and geographic entities coexist: `legislature`, `Constitution`, `Congress`, `Laws`, `Statutes`, `governmental`, `statute`, `enactment` alongside Newcastle, Calgary, Vancouver, Australia, province and borough. |
| C13 | 66 | 372 / 165 | 13.77 | -0.03049 | Strong numeric cluster. |
| C14 | 57 | 218 / 310 | 13.09 | -0.03277 | Abstract algebra/category-theory organisation is coherent: `omorphisms`, `commutative`, `bigoplus`, `homogeneous`, `functor`, `morphism`, `homomorphism`, `morphisms`; extremes include reducible, uniform, bounded, nonzero and subset. |

## Population accounting

### Positive head

Total nodes: **3,167**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,931 | 61.0% |
| Formal substrate | 1,164 | 36.8% |
| Irreducible semantic | 72 | 2.3% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,167** | **100.0%** |

Semantic-eligible denominator: **2,003 nodes**.

### Negative tail

Total nodes: **2,809**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,318 | 46.9% |
| Formal/name substrate | 908 | 32.3% |
| Irreducible semantic | 327 | 11.6% |
| Mixed unresolved | 256 | 9.1% |
| Unclear | 0 | 0.0% |
| **Total** | **2,809** | **100.0%** |

Semantic-eligible denominator: **1,901 nodes**.

## Positive-side reconstruction

### P+0 — Information access, retrieval and transactional systems

- **Primary children:** C2, C6
- **Primary nodes:** 666
- **Side-relative coverage:** 21.0%
- **Semantic-eligible coverage:** 33.3%
- **Confidence:** High

**Evidence.** C2 contains accessing, retrieving, formatting, recognising and
task-response operations. C6 contains websites, databases, forms, transactions,
connections and services. Their direct relation contains **288 token edges**,
mean cosine **0.09655**. One community describes information operations; the
other supplies the systems on which those operations act.

**Exclusion boundary.** C3 concerns evaluation/context rather than information
infrastructure. C5 contains technical-looking abbreviations but is
form-organised. C1 contains scientific content rather than information-system
operations.

**Alternative.** Absorb C3 into a broader
`information handling, response and evaluation` parent. This is rejected
because C3's affective, cultural, professional and general discourse content is
not specific to information systems.

### P+1 — Social/institutional context and appraisal

- **Primary children:** C3, C4
- **Primary nodes:** 637
- **Side-relative coverage:** 20.1%
- **Semantic-eligible coverage:** 31.8%
- **Confidence:** Moderate

**Evidence.** C3 centres on psychosocial, emotional, professional, cultural and
evaluative/contextual descriptors. C4 centres on nationalities/geography plus
political, administrative and financial descriptors. Their direct relation
contains **159 token edges**, mean cosine **0.09449**. The common structure is
social/institutional context being described and appraised.

**Exclusion boundary.** C10 is literal calendar time, not contextual appraisal.
C2 is operational/task language. C9 concerns food/agriculture/biological life
and sport rather than institutional description.

**Alternative.** Leave C3 and C4 as separate irreducible structures. This
remains plausible because both communities are broad and C4 is explicitly
mixed.

### P+2 — Biological, health and cultivated-living systems

- **Primary children:** C1, C9
- **Primary nodes:** 628
- **Side-relative coverage:** 19.8%
- **Semantic-eligible coverage:** 31.4%
- **Confidence:** Moderate

**Evidence.** C1 contains a strong biomedical/physiological core; C9 contains
food, crops, vegetation and other biological-life terms. Their direct relation
contains **191 token edges**, mean cosine **0.08943**. The shared parent is
living/biological systems, with health on one side and cultivated/embodied life
on the other.

**Exclusion boundary.** C1's physical-science terms and C9's sport terms are
real secondary components, so the parent is not treated as a pure biomedical
cluster. C4's social geography and C6's database systems are excluded.

**Alternative.** Keep C1 and C9 separate as mixed communities. This alternative
would be favoured if full membership showed that C1's physical-science
component or C9's sport component is comparable in weight to their biological
cores.

### Positive irreducible and formal structures

- **C10 — irreducible-semantic:** calendar years, weekdays and seasons.
- **C0, C5, C7, C8 — formal-substrate:** grammar/fragments, acronyms,
  punctuation/formatting and numerics.

## Negative-side reconstruction

### P-0 — Adverse evaluation, violence and prohibited harm

- **Primary children:** C1, C8
- **Primary nodes:** 484
- **Side-relative coverage:** 17.2%
- **Semantic-eligible coverage:** 25.5%
- **Confidence:** High

**Evidence.** C1 contains rejection, adversity, unacceptability, catastrophe,
tragedy and discomfort. C8 contains murder, killing, crime, prohibition,
destruction and arrest/indictment. Their relation contains **249 token edges**,
mean cosine **0.09879**. The shared higher-order structure is socially or
affectively adverse/harmful action and its rejection.

**Secondary links:**
- **C10:** physical/vocal actions connect to the enacted-action component;
  C1–C10 has **159 edges** at **0.10352**, C8–C10 **93** at **0.09193**.
- **C3:** authority and social roles connect actors to harmful/prohibited
  action; C3–C8 has **138 edges** at **0.10391**.
- **C4:** weapons and physical settings provide an event/material context;
  C4–C8 has **95 edges**.

**Exclusion boundary.** C10 also contains neutral/positive actions such as
hugging and applause. C3 includes many occupations and fictional roles
unrelated to harm. C4 includes general clothing, transport and devices.

**Alternative.** Absorb C10 as a third primary child under a broader
`adverse action and event` parent. This is not preferred because its physical
and vocal-action membership is not consistently adverse.

### P-1 — Scientific/clinical analysis and interpretation

- **Primary children:** C2, C6
- **Primary nodes:** 504
- **Side-relative coverage:** 17.9%
- **Semantic-eligible coverage:** 26.5%
- **Confidence:** High

**Evidence.** C2 contains analysis, interpretation, visualisation, epidemiology,
phenotypes, stabilisation, methodology and experiments. C6 contains clinical
diagnostics, pathology, biomarkers, anatomy and treatment. Their direct
relation contains **186 token edges**, mean cosine **0.10240**. The common
structure is analytical description and investigation of biological/clinical
systems.

**Secondary links:**
- **C14:** abstract algebra/category-theory supplies formal analytical
  machinery; C2–C14 has **76 edges**.
- **C9:** programming/data/document systems supply technical infrastructure;
  C2–C9 has **124 edges**, C6–C9 **54**.
- **P-0:** C1–C2 is the strongest negative-side relation at **377 edges**,
  showing strong coupling between adverse judgement and analytical
  interpretation without making them the same parent.

**Exclusion boundary.** C14 is mathematical abstraction rather than
clinical/scientific description. C9 is technical infrastructure rather than
analysis itself. C1 is evaluative/adverse rather than scientific.

**Alternative.** Expand P-1 to include C14 under
`formal scientific and mathematical analysis`. This improves compression but
overstates the biological/clinical relevance of the algebra community.

### P-2 — Institutional authority and public/social roles

- **Primary children:** C3, C12
- **Primary nodes:** 330
- **Side-relative coverage:** 11.7%
- **Semantic-eligible coverage:** 17.4%
- **Confidence:** Moderate

**Evidence.** C3 contains occupations, authority titles and social roles,
including Chairman, Congressman, officer, leaders and CEO. C12 contains
legislature, Constitution, Congress, Laws, Statutes, governmental, statute and
enactment together with public/geographic entities. Their relation contains
**89 token edges**, mean cosine **0.10799**, one of the highest mean
intercommunity similarities in the state.

**Exclusion boundary.** Fictional/religious content inside C3 and geographic
content inside C12 prevent a narrower government-only parent. C0 is merely a
name-form population without one institutional class.

**Alternative.** Leave C3 and C12 separate because both are mixed. This is a
serious alternative; P-2 remains Moderate rather than High.

### Negative irreducible and unresolved structures

- **C9 — irreducible-semantic:** programming, data and document systems;
  secondary link to P-1.
- **C10 — irreducible-semantic:** physical/movement/vocal actions; secondary
  link to P-0.
- **C14 — irreducible-semantic:** abstract algebra/category theory; secondary
  link to P-1.
- **C4 — mixed-unresolved:** built environment, weapons, devices, clothing and
  physical objects; secondary link to P-0.
- **C0, C5, C7, C11, C13 — formal/name substrate:** names, lexical fragments,
  multilingual/encoding fragments, punctuation and numerics.

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 510 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C1 | 480 | Biomedical + physical science | parent:P+2 | — | Biomedical/living-system core dominates, with physical-science heterogeneity retained. |
| + | C2 | 399 | Information access/retrieval/task actions | parent:P+0 | — | Information operations. |
| + | C3 | 319 | Evaluative/affective/discourse language | parent:P+1 | — | Social/contextual appraisal. |
| + | C4 | 318 | Geography + political/admin/financial | parent:P+1 | — | Institutional/social context and geography. |
| + | C5 | 278 | Acronyms/initialisms | formal-substrate | — | Abbreviation form dominates. |
| + | C6 | 267 | Websites/databases/forms/transactions | parent:P+0 | — | Information-system infrastructure. |
| + | C7 | 225 | Closing punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C8 | 151 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C9 | 148 | Food/agriculture/biological life + sport | parent:P+2 | — | Cultivated/living-system core with sport heterogeneity retained. |
| + | C10 | 72 | Calendar/time | irreducible-semantic | — | Coherent time structure without a sibling parent. |
| − | C0 | 355 | Personal names/titles | formal-substrate | — | Name-form organisation without one domain. |
| − | C1 | 335 | Negative evaluation/adversity | parent:P-0 | — | Adverse judgement/rejection. |
| − | C2 | 322 | Analysis/interpretation/methodology | parent:P-1 | — | Scientific/analytical description. |
| − | C3 | 259 | Occupations/authority/fictional roles | parent:P-2 | P-0 | Institutional/social roles dominate, with actor relation to harm. |
| − | C4 | 256 | Built/weapons/devices/objects | mixed-unresolved | P-0 | Threat/event setting is present but not exclusive. |
| − | C5 | 233 | Word pieces/suffixes | formal-substrate | — | Morphological form. |
| − | C6 | 182 | Clinical medicine/diagnostics/pathology | parent:P-1 | — | Clinical analytical domain. |
| − | C7 | 152 | Multilingual/encoding fragments | formal-substrate | — | Orthographic/tokeniser organisation. |
| − | C8 | 149 | Violence/crime/prohibition | parent:P-0 | — | Harmful/prohibited action. |
| − | C9 | 136 | Programming/data/document systems | irreducible-semantic | P-1 | Technical infrastructure adjacent to analysis. |
| − | C10 | 134 | Physical/movement/vocal actions | irreducible-semantic | P-0 | Action/event relation but not consistently adverse. |
| − | C11 | 102 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 71 | Government/law/geography/public entities | parent:P-2 | — | Institutional/public authority structure. |
| − | C13 | 66 | Numeric strings | formal-substrate | — | Numeric form. |
| − | C14 | 57 | Abstract algebra/category theory | irreducible-semantic | P-1 | Formal analytical abstraction adjacent to scientific analysis. |

Every State 03 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information access, retrieval and transactional systems | C2, C6 | 666 | 21.0% | 33.3% | High |
| P+1 | Social/institutional context and appraisal | C3, C4 | 637 | 20.1% | 31.8% | Moderate |
| P+2 | Biological, health and cultivated-living systems | C1, C9 | 628 | 19.8% | 31.4% | Moderate |
| P-0 | Adverse evaluation, violence and prohibited harm | C1, C8 | 484 | 17.2% | 25.5% | High |
| P-1 | Scientific/clinical analysis and interpretation | C2, C6 | 504 | 17.9% | 26.5% | High |
| P-2 | Institutional authority and public/social roles | C3, C12 | 330 | 11.7% | 17.4% | Moderate |

Positive retained parents account for **1,931 nodes**, **61.0% of the positive
population** and **96.4% of semantic-eligible positive nodes**.

Negative retained parents account for **1,318 nodes**, **46.9% of the negative
population** and **69.3% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — information/action in social context — Moderate.**
   C2–C3 has **441 edges** and C2–C4 **149**; C6–C3 has **144** and C6–C4
   **158**. Information operations and services are strongly embedded in
   contextual/social description without collapsing into it.

2. **P+0 ↔ P+2 — information/science relation — Moderate.**
   C1–C2 has **362 edges**, C1–C6 **255**, and C2–C9 **118**. Biological and
   scientific material is strongly coupled to information operations and
   systems.

3. **P+1 ↔ P+2 — embodied/social-context relation — Moderate.**
   C1–C3 has **388 edges**, C1–C4 **344**, C4–C9 **152**. Biological/embodied
   content and social/institutional context are highly connected, but their
   organising principles remain distinguishable.

The positive state is therefore strongly interconnected even though the
preferred reconstruction retains three separate parents.

### Negative-side relations

1. **P-0 ↔ P-1 — judgement/analysis coupling — High.**
   C1–C2 is the strongest negative-side relation at **377 edges**, mean cosine
   **0.10183**; C2–C8 has **185**. Adverse judgement and analytical
   interpretation are tightly coupled while remaining semantically distinct.

2. **P-0 ↔ P-2 — authority/actor relation — Moderate.**
   C1–C3 has **133 edges**, C8–C3 **138**, and C1–C12 **42**. Institutional
   roles and public authority provide actors and normative context for adverse
   judgement and prohibited harm.

3. **P-1 ↔ P-2 — institutional analysis relation — Moderate.**
   C2–C3 has **179 edges** and C2–C12 **33**. Analysis/methodology relates to
   institutional actors and public structures without becoming the same
   parent.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

State 03 compact cross-side evidence is dominated by near-lexical relations
such as geographic-name variants, travelled/traveled and morphological
variants. These do not establish a parent-level semantic bridge.

Plausible but unpromoted correspondences include:

- positive P+0 and negative C9 through information/data systems;
- positive P+2 and negative P-1 through biomedical/scientific structure;
- positive P+1 and negative P-2 through social/institutional organisation.

The available cross-side evidence does not justify treating these as measured
or state-level bridge structures.

## Formal/representational substrate

### Positive — 1,164 nodes / 36.8%

- grammar/function words and fragments;
- acronyms/initialisms;
- punctuation/formatting;
- numeric strings.

### Negative — 908 nodes / 32.3%

- personal names/name-like entities;
- lexical fragments;
- multilingual/encoding fragments;
- mathematical/code punctuation;
- numeric strings.

## Minimal state-level architecture

```text
STATE 03 — BLOCK 2 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION ACCESS / RETRIEVAL / TRANSACTIONAL SYSTEMS
|   +-- C2 access/retrieval/recognition/task operations
|   `-- C6 websites/databases/forms/transactions/services
|
+-- P+1 SOCIAL / INSTITUTIONAL CONTEXT & APPRAISAL
|   +-- C3 evaluative/affective/contextual discourse
|   `-- C4 geography/nationality + politics/admin/finance
|
+-- P+2 BIOLOGICAL / HEALTH / CULTIVATED-LIVING SYSTEMS
|   +-- C1 biomedical + physical-science mixed community
|   `-- C9 food/agriculture/biological life + sport
|
+-- C10 calendar/time                               [irreducible]
`-- C0,C5,C7,C8                                   [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ADVERSE EVALUATION / VIOLENCE / PROHIBITED HARM
|   +-- C1 negative evaluation/adversity
|   `-- C8 violence/crime/prohibition
|       |
|       +-- C10 physical/vocal action              [secondary]
|       +-- C3 authority/social roles              [secondary]
|       `-- C4 weapons/physical setting           [secondary; mixed]
|
+-- P-1 SCIENTIFIC / CLINICAL ANALYSIS & INTERPRETATION
|   +-- C2 analysis/interpretation/methodology
|   `-- C6 clinical diagnostics/pathology
|       |
|       +-- C9 programming/data systems            [secondary]
|       `-- C14 abstract algebra                  [secondary]
|
+-- P-2 INSTITUTIONAL AUTHORITY & PUBLIC/SOCIAL ROLES
|   +-- C3 occupations/authority/fictional roles
|   `-- C12 government/law/public/geographic entities
|
+-- C9 programming/data/document systems           [irreducible]
+-- C10 physical/movement/vocal action              [irreducible]
+-- C14 abstract algebra/category theory            [irreducible]
+-- C4 built/weapons/devices/objects                [mixed unresolved]
`-- C0,C5,C7,C11,C13                              [formal/name substrate]
```

The preferred State 03 reconstruction contains three positive and three
negative multi-community parents. The positive semantic population is highly
compressible into information-system, social-contextual and biological/living
structures. The negative population is organised around adverse/harmful
evaluation, scientific/clinical analysis and institutional authority, while
technical, action, mathematical and physical-object communities remain partly
outside those parents.

This statement is local to State 03 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction makes two broader merges:

1. merge positive P+1 and P+2 into a broad
   **social/biological contextual description** structure, motivated by the
   very strong C1–C3 and C1–C4 relations;
2. merge negative P-0 and P-1 into a broad
   **judgement, interpretation and state evaluation** structure, motivated by
   the 377-edge C1–C2 relation.

Both alternatives improve compression but fail the anti-vacuity test. In the
first, institutional context and biological/health systems lose their
discriminative identities. In the second, adverse social judgement and
scientific/clinical analysis become indistinguishable.

## Uncertainty record

- **Positive P+1:** Moderate because C3 and C4 are broad and C4 is explicitly
  mixed.
- **Positive P+2:** Moderate because C1 contains real physical-science material
  and C9 contains real sport material.
- **Negative P-2:** Moderate because C3 contains fictional/religious roles and
  C12 contains geography as well as governance/law.
- **Negative C4:** remains mixed-unresolved despite strong relations to several
  semantic parents; built environment, weapons, devices and clothing do not
  reduce cleanly to one role.
- **Negative C10:** is related to P-0 but not consistently adverse.
- **Negative C14:** is analytically related to P-1 but is too formally abstract
  to be a primary clinical/scientific child.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **11 / 11**
- Negative communities accounted for: **15 / 15**
- Total communities accounted for: **26 / 26**
- Positive node accounting: **3,167 / 3,167**
- Negative node accounting: **2,809 / 2,809**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1, P-2**
- Every retained parent has an exclusion boundary: **yes**
- Every community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 03 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
