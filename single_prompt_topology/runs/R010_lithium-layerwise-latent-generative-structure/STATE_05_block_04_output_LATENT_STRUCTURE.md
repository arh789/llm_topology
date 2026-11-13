# R010 State 05 — Block 4 output latent structure

## State identity

- R010 state index: `05`
- R008/R009 state: `block_04_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 14 negative-tail = 27**
- R008 population: **2,886 positive-head + 3,218 negative-tail = 6,104 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 05 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

For every State 05 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_05_block_04_output.md`;
2. State 05 entries in `R009_SUMMARY.html`;
3. all 27 State 05 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token-class
   composition;
4. the full State 05 within-side relation set in
   `R008/community_edges.csv`;
5. the State 05 R008 layer packet and compact cross-side evidence.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 348 | 1,701 / 1,909 | 15.26 | +0.03118 | Function words and short lexical fragments dominate: `is`, `of`, `was`, `have`, `like`, `am`, with short fragments and partial forms. |
| C1 | 335 | 1,243 / 1,673 | 12.41 | +0.03258 | Acronyms, initialisms and short technical abbreviations dominate: `PC`, `SC`, `CA`, `HA`, `SS`, `CP`, `IP`, with `NAS`, `CS`, `ACP`, `LOS` among extremes. |
| C2 | 330 | 1,262 / 1,850 | 13.25 | +0.03180 | Databases, websites, access and software interfaces dominate: `response`, `sites`, `mysql`, `accessing`, `Connection`, `DB`, `Database`, `checking`; extremes include `Views`, `Role`, `CSS`, `Hash`, `Cyber`, `Entry`. |
| C3 | 309 | 1,126 / 1,938 | 13.56 | +0.03220 | Task/process actions dominate but finance and sport are genuine secondary structure: `initiating`, `travelling`, `formatted`, `specializes`, `giving`, `extracted`, `transactions`, with `Financial`, `basketball`, `exercising`. |
| C4 | 296 | 1,273 / 1,640 | 14.14 | +0.03188 | Biomedical/molecular-science content dominates: `immunosuppressive`, `conformational`, `glucocortic`, `inflammatory`, `pituitary`, `metabolic`, `molecule`, `infertility`, `chemical`, `membranes`; physical-science terms such as `renormalization`, `Spin`, `surfaces`, `carbon`, `Gas` remain real. |
| C5 | 284 | 1,272 / 1,270 | 13.43 | +0.03232 | Countries, nationalities and cities dominate: Indonesian, Nigerian, Sacramento, Charleston, California, Chicago, Chinese, Canadian, Charlotte, Orlando, Australian, Swedish. |
| C6 | 271 | 1,031 / 1,721 | 13.96 | +0.03197 | Psychology/social-life and political/administrative structure coexist: `psychological`, `psychosocial`, `emotional`, `Political`, `political`, `administrative`, `parliamentary`, `cultural`, `psychiat`. |
| C7 | 181 | 1,074 / 387 | 14.01 | +0.03239 | Strong punctuation/bracket/code-formatting cluster; 145 of 181 tokens are punctuation/symbols. |
| C8 | 164 | 661 / 920 | 13.67 | +0.03114 | Discourse, temporal and evaluative/adverbial language dominates: `Subsequently`, `Eventually`, `Alternatively`, `Anyway`, `Obviously`, `recalling`, `retrospectively`, `hugely`. |
| C9 | 131 | 420 / 763 | 12.24 | +0.03208 | Multilingual, malformed and encoding/tokenisation fragments dominate. |
| C10 | 100 | 338 / 661 | 13.37 | +0.03334 | Food, nutrition and domestic/agricultural animals form a coherent living/consumption cluster: `cakes`, `rice`, `food`, `bread`, `chocolate`, `Nutrition`, `cats`, with insects/pig/coconut/fry among extremes. |
| C11 | 90 | 508 / 217 | 13.70 | +0.03092 | Strong numeric cluster. |
| C12 | 47 | 223 / 199 | 13.72 | +0.03106 | Calendar years, weekdays and seasons form a coherent time cluster. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 477 | 2,233 / 2,000 | 13.56 | -0.03006 | Personal names and name-like entities dominate: Hayes, Liz, Dav, Thompson, Murphy, Roberts, Hal, Lou, Wheeler, Hicks; no single social domain links them. |
| C1 | 475 | 2,087 / 2,374 | 13.79 | -0.03022 | Analysis, explanation, interpretation, construction and description dominate: `Characteristics`, `analysis`, `explanations`, `descriptions`, `interpretation`, `constructions`, `estimates`, `constructing`, `determined`, `creating`. |
| C2 | 447 | 2,014 / 2,343 | 14.25 | -0.03050 | Negative evaluation, adversity and destruction dominate: `uncomfortable`, `unconstitutional`, `disappointment`, `destroys`, `tragedy`, `massacre`, `annoying`, `unacceptable`, `inconsistency`; extremes include `madness`, `revive`, `reunion`, `shouted`. |
| C3 | 317 | 1,276 / 1,653 | 13.26 | -0.03055 | Built environment, architecture, weapons and objects coexist: staircases/hallways/stairs, boats, guns, palace, balconies, cliffs, sword, tubes; extremes include shots, wireless, reactors, nozzle and spacecraft. |
| C4 | 299 | 1,371 / 1,574 | 14.43 | -0.03045 | Function words, suffixes and fragments dominate. |
| C5 | 294 | 1,296 / 1,597 | 14.25 | -0.03097 | Religious, institutional and authority roles coexist with violent/fantasy terms: `Archbishop`, `Congressman`, `pastor`, `Chairman`, `Rabbi`, `officials`, `CEO`, plus goddess, murders, monsters, Devil and pagan. |
| C6 | 200 | 840 / 1,054 | 13.67 | -0.03066 | Clinical diagnostics, anatomy and pathology are coherent: `echocardiography`, `pathophysiology`, `abdomen`, `angiography`, `skull`, `anesthesia`, `cerebellum`, `microscopy`, `phenotypes`, `arrhythm`. |
| C7 | 186 | 633 / 1,192 | 13.22 | -0.03122 | Negative/contrastive stems and incomplete word forms dominate; semantic suggestiveness remains secondary to morphology. |
| C8 | 138 | 812 / 244 | 13.54 | -0.03060 | Strong mathematical/code punctuation cluster; 127 of 138 tokens are punctuation/symbols. |
| C9 | 110 | 635 / 252 | 13.84 | -0.02952 | Numeric strings, especially historical years, dominate. |
| C10 | 106 | 366 / 533 | 11.93 | -0.03060 | Multilingual suffixes and orthographic fragments dominate. |
| C11 | 75 | 277 / 406 | 12.80 | -0.03142 | Abstract algebra/geometry is coherent: morphisms, commutative, maps, bigoplus, perpendicular, homomorphism, homogeneous, coherent; extremes include reducible, zero, uniform, bounded and quotient. |
| C12 | 74 | 206 / 482 | 12.08 | -0.03127 | Low-level computing/hardware/software runtime terms are coherent: initialization, hw, compiler, runtime, databind, Decoder, sdk, addr, Pointer, png, uint, GPIO. |
| C13 | 20 | 66 / 108 | 12.00 | -0.03026 | Degree, approximation and qualification language is coherent: `seemingly`, `essentially`, `almost`, `solely`, `Half`, `pretty`, `Not`, with `truly`, `officially`, `half`, `Pretty` among extremes. |

## Population accounting

### Positive head

Total nodes: **2,886**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,590 | 55.1% |
| Formal substrate | 1,085 | 37.6% |
| Irreducible semantic | 211 | 7.3% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,886** | **100.0%** |

Semantic-eligible denominator: **1,801 nodes**.

### Negative tail

Total nodes: **3,218**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,416 | 44.0% |
| Formal/name substrate | 1,316 | 40.9% |
| Irreducible semantic | 169 | 5.3% |
| Mixed unresolved | 317 | 9.9% |
| Unclear | 0 | 0.0% |
| **Total** | **3,218** | **100.0%** |

Semantic-eligible denominator: **1,902 nodes**.

## Positive-side reconstruction

### P+0 — Information/task operations and transactional systems

- **Primary children:** C2, C3
- **Primary nodes:** 639
- **Side-relative coverage:** 22.1%
- **Semantic-eligible coverage:** 35.5%
- **Confidence:** High

**Evidence.** C2 supplies databases, websites, information access and software
interfaces. C3 supplies task/process operations including initiating,
formatting, giving, extracting, transactions and resolving. Their direct
relation is the strongest positive semantic pair in the state:
**399 token edges**, mean cosine **0.09784**.

**Secondary links:** C6 and C8. C3–C6 has **315 edges** and C3–C8 **177**,
showing that task activity is strongly embedded in social/institutional and
evaluative contexts.

**Exclusion boundary.** Finance/sport material in C3 is preserved as
heterogeneity rather than used to broaden the parent into “all activity”. C1 is
technical abbreviation form rather than a semantic system.

**Alternative.** Absorb C8 into a broader
`information/task processing and evaluation` parent. Rejected because C8's
general temporal/discourse content is not specific to information systems.

### P+1 — Geographic, psychological and institutional-social organisation

- **Primary children:** C5, C6
- **Primary nodes:** 555
- **Side-relative coverage:** 19.2%
- **Semantic-eligible coverage:** 30.8%
- **Confidence:** Moderate

**Evidence.** C5 supplies geographic/nationality entities; C6 supplies
psychological, psychosocial, political, administrative and cultural descriptors.
Their direct relation contains **193 token edges**, mean cosine **0.08925**.
Together they describe social populations and their institutional/psychological
context.

**Secondary link:** C3. C3–C6 has **315 edges**, and finance/sport terms in C3
fit social/institutional activity without dominating that community.

**Exclusion boundary.** C8 is general discourse/evaluation rather than a social
domain. C12 is literal calendar time.

**Alternative.** Treat C5 as a geographic entity island and C6 as an
irreducible social/political community. This remains serious because C6 is
internally broad; parent confidence is therefore Moderate.

### P+2 — Biological, molecular and living/consumption systems

- **Primary children:** C4, C10
- **Primary nodes:** 396
- **Side-relative coverage:** 13.7%
- **Semantic-eligible coverage:** 22.0%
- **Confidence:** Moderate

**Evidence.** C4 supplies biomedical, molecular and metabolic terminology. C10
supplies food, nutrition, domestic/agricultural animals and other living-system
terms. Their direct relation contains **131 token edges**, mean cosine
**0.08990**. The common structure is biological/living systems and substances.

**Secondary link:** C6. C4–C6 has **306 edges**, reflecting psychological and
health overlap, but C6 is primarily social/institutional.

**Exclusion boundary.** Physical-science terms in C4 and ordinary food/animal
terms in C10 are preserved rather than collapsed into a narrowly biomedical
parent.

**Alternative.** Leave C4 and C10 separate as biomedical/molecular and
food/animal structures. This remains plausible; P+2 is therefore Moderate.

### Positive irreducible structures

- **C8 — irreducible-semantic:** discourse, temporal and evaluative/adverbial
  language; secondary links to P+0 and P+1.
- **C12 — irreducible-semantic:** calendar years, weekdays and seasons.

### Positive formal substrate

- C0 — grammar/function words/fragments
- C1 — acronyms/initialisms
- C7 — punctuation/formatting
- C9 — multilingual/tokenisation fragments
- C11 — numeric strings

## Negative-side reconstruction

### P-0 — Analysis, interpretation and clinical characterisation

- **Primary children:** C1, C6
- **Primary nodes:** 675
- **Side-relative coverage:** 21.0%
- **Semantic-eligible coverage:** 35.5%
- **Confidence:** High

**Evidence.** C1 centres on analysis, explanation, interpretation,
description, construction and estimation. C6 centres on clinical diagnostics,
pathology and anatomy. Their direct relation contains **175 token edges**, mean
cosine **0.10157**. The common structure is analytical characterisation of
systems, especially biological/clinical ones.

**Secondary links:**
- **C11:** abstract mathematics supplies formal analytical structure;
  C1–C11 has **87 edges**, mean cosine **0.09682**.
- **C12:** computing/runtime systems supply technical infrastructure;
  C1–C12 has **95 edges**.
- **P-1:** C1–C2 has **700 edges**, the strongest relation in the state.

**Exclusion boundary.** C11 is mathematical abstraction rather than
description itself. C12 is infrastructure rather than analysis. C2 is adverse
evaluation/destruction rather than neutral characterisation.

**Alternative.** Expand P-0 to include C11 and C12 under a broad
`formal analytical and computational systems` parent. Rejected because it
would erase the distinction between analytical operations, mathematical
objects and computing infrastructure.

### P-1 — Adversity, destructive evaluation and institutional conflict

- **Primary children:** C2, C5
- **Primary nodes:** 741
- **Side-relative coverage:** 23.0%
- **Semantic-eligible coverage:** 39.0%
- **Confidence:** High / Moderate

**Evidence.** C2 contains negative evaluation, adversity, destruction, tragedy,
massacre and distress. C5 contains institutional/religious authority roles
intermixed with murders, monsters, Devil and other conflict/fantasy material.
Their direct relation contains **246 token edges**, mean cosine **0.09897**.

**Secondary link:** C3. C3–C5 has **299 edges**, mean cosine **0.10482**, and
C2–C3 has **279**. Built settings, weapons and objects plausibly provide the
physical context of conflict/adversity, but C3 is too broad for primary
absorption.

**Exclusion boundary.** C5 contains many non-conflict institutional and
religious roles. C3 includes architecture, transport and general objects not
specific to adverse events.

**Alternative.** Make C3 a third child under a broader
`conflict, authority and physical setting` parent. Rejected because this would
turn a broad object/environment community into a conflict category by
association alone.

### Negative mixed unresolved structure

- **C3 — mixed-unresolved:** built environment, architecture, weapons and
  physical objects; secondary link to P-1.

### Negative irreducible structures

- **C11 — irreducible-semantic:** abstract algebra/geometry; secondary link to
  P-0.
- **C12 — irreducible-semantic:** low-level computing/hardware/runtime systems;
  secondary link to P-0.
- **C13 — irreducible-semantic:** degree, approximation and qualification
  language.

### Negative formal/name substrate

- C0 — personal names
- C4 — grammar/function words/suffixes
- C7 — incomplete negative/contrastive stems
- C8 — mathematical/code punctuation
- C9 — numeric strings
- C10 — multilingual morphology

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 348 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C1 | 335 | Acronyms/initialisms | formal-substrate | — | Abbreviation form dominates. |
| + | C2 | 330 | Databases/websites/access/software | parent:P+0 | — | Information-system infrastructure. |
| + | C3 | 309 | Task/process + finance/sport | parent:P+0 | P+1 | Task/transaction operations dominate; social activity remains secondary. |
| + | C4 | 296 | Biomedical/molecular + physical science | parent:P+2 | — | Biological/molecular core dominates. |
| + | C5 | 284 | Countries/nationalities/cities | parent:P+1 | — | Geographic/social population domain. |
| + | C6 | 271 | Psychology/social/politics/admin | parent:P+1 | P+2 | Social/institutional core; health/psychology overlap retained. |
| + | C7 | 181 | Punctuation/formatting | formal-substrate | — | Formatting/tokeniser organisation. |
| + | C8 | 164 | Discourse/temporal/evaluative language | irreducible-semantic | P+0, P+1 | Cross-domain contextual/evaluative structure. |
| + | C9 | 131 | Multilingual/tokenisation fragments | formal-substrate | — | Orthographic/tokeniser organisation. |
| + | C10 | 100 | Food/nutrition/animals | parent:P+2 | — | Living/consumption-system structure. |
| + | C11 | 90 | Numeric strings | formal-substrate | — | Numeric form. |
| + | C12 | 47 | Calendar time/years/weekdays | irreducible-semantic | — | Coherent time structure. |
| − | C0 | 477 | Personal names | formal-substrate | — | Name-form organisation without one domain. |
| − | C1 | 475 | Analysis/explanation/interpretation | parent:P-0 | — | Analytical characterisation. |
| − | C2 | 447 | Negative evaluation/adversity/destruction | parent:P-1 | — | Adverse/destructive evaluation. |
| − | C3 | 317 | Built environment/weapons/objects | mixed-unresolved | P-1 | Physical conflict-setting relation but broad object content. |
| − | C4 | 299 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C5 | 294 | Religious/institutional roles + violence/fantasy | parent:P-1 | — | Authority/conflict structure, with retained heterogeneity. |
| − | C6 | 200 | Clinical diagnostics/pathology | parent:P-0 | — | Clinical analytical domain. |
| − | C7 | 186 | Negative/contrastive stems | formal-substrate | — | Morphological form dominates. |
| − | C8 | 138 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C9 | 110 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C10 | 106 | Multilingual suffixes/fragments | formal-substrate | — | Morphological/orthographic form. |
| − | C11 | 75 | Abstract algebra/geometry | irreducible-semantic | P-0 | Formal analytical relation. |
| − | C12 | 74 | Low-level computing/runtime | irreducible-semantic | P-0 | Technical-infrastructure relation. |
| − | C13 | 20 | Degree/approximation/qualification | irreducible-semantic | — | Coherent modifier structure without a sibling parent. |

Every State 05 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information/task operations and transactional systems | C2, C3 | 639 | 22.1% | 35.5% | High |
| P+1 | Geographic, psychological and institutional-social organisation | C5, C6 | 555 | 19.2% | 30.8% | Moderate |
| P+2 | Biological, molecular and living/consumption systems | C4, C10 | 396 | 13.7% | 22.0% | Moderate |
| P-0 | Analysis, interpretation and clinical characterisation | C1, C6 | 675 | 21.0% | 35.5% | High |
| P-1 | Adversity, destructive evaluation and institutional conflict | C2, C5 | 741 | 23.0% | 39.0% | High / Moderate |

Positive retained parents account for **1,590 nodes**, **55.1% of the positive
population** and **88.3% of semantic-eligible positive nodes**.

Negative retained parents account for **1,416 nodes**, **44.0% of the negative
population** and **74.4% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — transactional/social activity relation — High.**
   C3–C6 has **315 edges**, C2–C6 **245**, C3–C5 **122** and C2–C5 **106**.
   Information/task operations are strongly embedded in social, financial and
   institutional contexts.

2. **P+0 ↔ P+2 — information/science relation — Moderate to High.**
   C2–C4 has **256 edges** and C3–C4 **220**. Technical/information operations
   strongly connect to scientific/biological material.

3. **P+1 ↔ P+2 — psychosocial/health relation — High.**
   C4–C6 has **306 edges**, one of the strongest semantic relations in the
   state; C5–C10 has **93** and C6–C10 **60**. Psychological/social structure
   overlaps biological and health domains without making them one parent.

4. **C8 is an evaluative/contextual bridge-like irreducible structure.**
   C3–C8 has **177 edges**, C6–C8 **167**, and C2–C8 **109**.

### Negative-side relations

1. **P-0 ↔ P-1 — analysis/adverse-evaluation coupling — Very High.**
   C1–C2 has **700 edges**, mean cosine **0.10034**, by far the strongest
   intercommunity relation in State 05. C1–C5 adds **311** edges. The graph
   strongly couples analytical description with adverse/destructive judgement,
   but the semantic functions remain discriminable.

2. **P-1 ↔ C3 — conflict/physical-setting relation — High.**
   C3–C5 has **299 edges** and C2–C3 **279**. Built environments, weapons and
   objects are tightly coupled to the conflict/adversity parent but remain too
   broad for primary inclusion.

3. **P-0 ↔ formal analytical/technical satellites — Moderate.**
   C1–C11 has **87 edges** and C1–C12 **95**, supporting secondary relations to
   mathematics and computing without promoting them into the parent.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

The strongest compact State 05 cross-side relations are largely lexical,
case-form or near-form correspondences such as `various`/ `Various`,
`video`/ `Video`, and mathematical stem variants. They do not establish a
parent-level semantic bridge.

Plausible but unpromoted correspondences include:

- positive P+0 and negative C12 through computing/information systems;
- positive P+2 and negative P-0 through biomedical/clinical structure;
- positive P+1 and negative P-1 through institutional/social material.

The available cross-side evidence does not justify promoting these.

## Formal/representational substrate

### Positive — 1,085 nodes / 37.6%

- grammar/function words and fragments;
- acronyms/initialisms;
- punctuation/formatting;
- multilingual/tokenisation fragments;
- numeric strings.

### Negative — 1,316 nodes / 40.9%

- personal names;
- grammar/function words/suffixes;
- negative/contrastive word stems;
- mathematical/code punctuation;
- numeric strings;
- multilingual morphology.

## Minimal state-level architecture

```text
STATE 05 — BLOCK 4 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION / TASK OPERATIONS & TRANSACTIONAL SYSTEMS
|   +-- C2 databases/websites/access/software
|   `-- C3 task/process/transaction actions
|       \
|        -- C8 evaluative/discourse                  [secondary]
|
+-- P+1 GEOGRAPHIC / PSYCHOLOGICAL / INSTITUTIONAL-SOCIAL ORGANISATION
|   +-- C5 countries/nationalities/cities
|   `-- C6 psychology/social/politics/admin
|       \
|        -- C3 finance/sport/activity                [secondary]
|
+-- P+2 BIOLOGICAL / MOLECULAR / LIVING-CONSUMPTION SYSTEMS
|   +-- C4 biomedical/molecular + physical science
|   `-- C10 food/nutrition/animals
|
+-- C8 discourse/temporal/evaluative language         [irreducible]
+-- C12 calendar/time                                 [irreducible]
`-- C0,C1,C7,C9,C11                                  [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 ANALYSIS / INTERPRETATION / CLINICAL CHARACTERISATION
|   +-- C1 analysis/explanation/interpretation
|   `-- C6 clinical diagnostics/pathology
|       |
|       +-- C11 abstract mathematics                 [secondary]
|       `-- C12 low-level computing                 [secondary]
|
+-- P-1 ADVERSITY / DESTRUCTIVE EVALUATION / INSTITUTIONAL CONFLICT
|   +-- C2 negative evaluation/adversity/destruction
|   `-- C5 religious/institutional roles + violence/fantasy
|       \
|        -- C3 built environment/weapons/objects    [secondary; mixed]
|
+-- C3 built environment/weapons/objects              [mixed unresolved]
+-- C11 abstract algebra/geometry                      [irreducible]
+-- C12 low-level computing/runtime                    [irreducible]
+-- C13 degree/approximation/qualification             [irreducible]
`-- C0,C4,C7,C8,C9,C10                               [formal/name substrate]
```

The preferred State 05 reconstruction contains three positive and two negative
multi-community parents. The positive semantic population is organised around
information/task systems, social/institutional organisation and
biological/living systems. The negative semantic population is dominated by a
strong analytical/clinical structure and an adverse/conflict structure, with a
very dense relation between them but sufficient semantic distinction to keep
them separate.

This statement is local to State 05 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing reconstruction is to merge negative P-0 and P-1 into a
single **analysis, judgement and adverse state characterisation** parent,
motivated by the exceptional **700-edge** C1–C2 relation and strong C1–C5
connection.

This alternative is not preferred because it would make neutral analytical
description, clinical diagnostics, destructive evaluation and
institutional/conflict semantics instances of one overly broad category. The
graph density is real; the semantic collapse is not justified.

A second alternative is to absorb positive C8 into P+0 as a general
evaluation/response component. This improves compression but fails because C8
contains general temporal and discourse modifiers not specific to information
or task systems.

## Uncertainty record

- **Positive P+1:** remains Moderate because geographic entities,
  psychological/social descriptors and political/administrative language form
  a broad common frame rather than a narrow topic.
- **Positive P+2:** remains Moderate because C4 contains physical-science
  material and C10 includes ordinary food/animal terms.
- **Positive C8:** is highly connected but remains irreducible because it
  functions as general contextual/evaluative language.
- **Negative P-1:** C5 contains non-conflict institutional and religious roles,
  so the parent is not interpreted as purely violent.
- **Negative C3:** remains mixed-unresolved despite very strong connectivity to
  P-1; weapons and conflict settings do not account for all of its built,
  transport and object content.
- **Negative P-0/P-1 boundary:** this is the main structural ambiguity because
  their graph coupling is exceptionally strong.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **14 / 14**
- Total communities accounted for: **27 / 27**
- Positive node accounting: **2,886 / 2,886**
- Negative node accounting: **3,218 / 3,218**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0, P-1**
- Every retained parent has an exclusion boundary: **yes**
- Every community inspected at underlying R008 community-record level: **yes**
- Full token-membership inspection falsely claimed: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 05 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
