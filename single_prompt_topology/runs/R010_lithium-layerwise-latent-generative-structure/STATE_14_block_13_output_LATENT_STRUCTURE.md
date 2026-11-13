# R010 State 14 — Block 13 output latent structure

## State identity

- R010 state index: `14`
- R008/R009 state: `block_13_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **13 positive-head + 13 negative-tail = 26**
- R008 population: **2,652 positive-head + 2,933 negative-tail = 5,585 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 14 only. Retrieval and graph inspection were
restricted to `state_index=14 / block_13_output`. No later-state evidence was
used.

## Evidence inventory

For every State 14 community, the reconstruction inspected the underlying R008
community record before assigning a disposition or parent.

Evidence used:

1. `R009/STATE_14_block_13_output.md`;
2. all 26 State 14 rows in R008 `community_nodes.csv`, including size,
   internal/boundary edges, mean degree, target-cosine statistics,
   graph-central representatives, target-extreme tokens and token classes;
3. the complete State 14 within-side relation set in
   `R008/community_edges.csv`.

The compressed token-level membership artifact was not decoded through the
available GitHub text connector. No claim is made that complete token-by-token
membership was inspected. Materially heterogeneous communities were retained as
mixed, irreducible or Moderate rather than forced into cleaner parents.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 411 | 1,508 / 2,018 | 12.25 | +0.03183 | Fragmentary action/process terms and heterogeneous lexical residue dominate: remembrance/negotiation/reappearance/happiness/manoeuvre/commission fragments, short name-like forms, replacement characters and multilingual fragments. |
| C1 | 328 | 1,300 / 1,840 | 13.54 | +0.03185 | Resolution, observation, inference and developmental actions dominate: resolving, characterizing, exploring, remembering, initiating, observing, computed, development, inferred, retrieved, develops and evolving. |
| C2 | 321 | 1,512 / 1,680 | 14.65 | +0.03130 | Common grammatical/function words and short lexical fragments dominate. |
| C3 | 287 | 1,105 / 1,641 | 13.42 | +0.03205 | Biomedical, pharmacological, respiratory and reproductive terminology dominates: breastfeeding, dexamethasone, dopaminergic, ventilation, menopausal, analgesic fragments, salivary, diazepam fragments, pulmonary and pneumonia fragments; non-medical outliers remain. |
| C4 | 263 | 1,105 / 1,362 | 13.58 | +0.03256 | Personal names and geographic entities dominate: Manchester, Karen, Maria, Gary, Anne, Hamburg, Mitchell and Jennifer; extremes add Berlin, Krish and Greek. |
| C5 | 259 | 972 / 1,569 | 13.56 | +0.03186 | Social/professional communication, negotiation and intervention dominate: conversations, negotiating, management, discussions, negotiation, psychosocial, interventions, psychiatry fragments, interviews, adventures and platforms. |
| C6 | 250 | 1,365 / 694 | 13.70 | +0.03226 | Strong mathematical/code punctuation and software-formatting structure; 158 of 250 tokens are punctuation/symbols, with software/LaTeX-like residues. |
| C7 | 152 | 416 / 982 | 11.93 | +0.03134 | Software/interface semantics coexist with measurement and technical abbreviations: facebook, Entry, DB, Permission and Amazon alongside size, Radius, Length, volume, PB, PRES, NE, BW and RAW. |
| C8 | 110 | 637 / 227 | 13.65 | +0.03126 | Numeric strings, including years, dominate. |
| C9 | 109 | 364 / 755 | 13.61 | +0.03131 | Interactions, measurements and physical/mathematical system dynamics dominate: interactions, interacting, phenomenological, Measurements, Lagrangian fragment, perturbative, responses, renormalization, transforms and actions. |
| C10 | 79 | 245 / 535 | 12.97 | +0.03354 | Publishing, reading, writing and acknowledgement/paratext language is coherent: Acknowledgements, Working, Books, pamphlet fragment, Read, writers, Writing, Bibliography and References. |
| C11 | 53 | 176 / 298 | 12.26 | +0.03206 | Multilingual suffixes, example-related words and morphological fragments dominate. |
| C12 | 30 | 102 / 217 | 14.03 | +0.03133 | Bodily gestures, affective actions and ringing/sound events form a coherent small semantic cluster: trembling, smiled, shook, kissed, swung, grinned, rings, paused, swallowed, kissing, gripped and squeezing. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 579 | 2,690 / 2,689 | 13.94 | -0.03120 | Characterisation, recommendations, regulation and system/distribution concepts dominate: Characteristics, unconstitutional, characteristics, downregulation, recommendations, encouragement, availability, distribution, circumstances, Constitution and algorithms; extremes include specificity, variance, codes, submit and disadvantages. |
| C1 | 484 | 2,143 / 2,364 | 13.74 | -0.03079 | Catastrophe, discrimination, prohibition/exclusion and intense evaluation dominate: disastrous, circumstantial, catastrophe fragments, discriminatory, unbelievable, prohibiting, incredible, catastrophe, emphasizing, exclude and excluding. |
| C2 | 421 | 1,706 / 1,981 | 12.81 | -0.03138 | Personal names dominate but biomedical/technical fragments such as cytokine/corticosteroid/fluorescence/crypt/glucose/PROT forms are substantial. |
| C3 | 386 | 1,765 / 1,676 | 13.49 | -0.03092 | Common grammatical/function words and lexical fragments dominate. |
| C4 | 237 | 963 / 1,300 | 13.61 | -0.03092 | Cardiovascular disease, trauma, pathology and biomedical morphology are coherent: cardiovascular, atherosclerotic, staphylococcus fragment, immunofluorescence fragment, trauma, sclerosis fragment, interleukin, angiography, colonic, dysfunction and morphology. |
| C5 | 209 | 894 / 1,195 | 14.27 | -0.03070 | Religion, monarchy, family and mythic/fantastical roles coexist: theology, emperor, mother, grandmother, palace, cathedral, church, Empire, queen, King, priest and creature. |
| C6 | 162 | 582 / 1,030 | 13.54 | -0.03172 | Vehicles, roads, natural terrain and household/material objects coexist: uniforms, trucks, automobiles, roadway, cliffs, woods, sidewalk, driveway, mountains, whiskey, vegetables and gravel; extremes add barrel, quilt, cloth, roofs, cassette, ignition and rug. |
| C7 | 134 | 500 / 788 | 13.34 | -0.03105 | Hardware, electronics, appliances and infrastructure equipment form a coherent technical/material domain: chassis, hardware, appliances, Rails, furniture, bulbs and short electronics codes; extremes include SSH, LCD, CPU, lamp and RF. |
| C8 | 120 | 710 / 277 | 14.14 | -0.03014 | Numeric strings, including historical years, dominate. |
| C9 | 67 | 317 / 374 | 15.04 | -0.03188 | Geographic/political entities mixed with legal/historical terms: Pennsylvania, Connecticut, Alabama, Florida, Minnesota, Georgia, province, Louisiana, Arkansas and Colonial, with misdemeanor and USSR/Putin material among extremes. |
| C10 | 66 | 195 / 436 | 12.52 | -0.03085 | Algebra, topology, subsets and continuity form a coherent mathematical domain: comparing, subsets, continuity, continuous, ideals, category, subset and polynomials; extremes include algebra, quotient, topology and polynomial. |
| C11 | 47 | 209 / 145 | 11.98 | -0.02967 | Strong mathematical/code punctuation and symbol-formatting cluster; 44 of 47 tokens are punctuation/symbols. |
| C12 | 21 | 49 / 159 | 12.24 | -0.02809 | Multiplicity/multi- lexical forms coexist with software status/message tokens: Multiple, multiple, multitude, multi, Mult, multif, hundreds with MESSAGE, ERROR, CURRENT, Default and WARN. |

## Population accounting

### Positive head

Total nodes: **2,652**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 983 | 37.1% |
| Formal/name substrate | 1,408 | 53.1% |
| Irreducible semantic | 109 | 4.1% |
| Mixed unresolved | 152 | 5.7% |
| Unclear | 0 | 0.0% |
| **Total** | **2,652** | **100.0%** |

Semantic-eligible denominator: **1,244 nodes**.

### Negative tail

Total nodes: **2,933**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,635 | 55.7% |
| Formal/name substrate | 974 | 33.2% |
| Irreducible semantic | 303 | 10.3% |
| Mixed unresolved | 21 | 0.7% |
| Unclear | 0 | 0.0% |
| **Total** | **2,933** | **100.0%** |

Semantic-eligible denominator: **1,959 nodes**.

## Positive-side reconstruction

### P+0 — Coordinated inquiry, communication and professional action

- **Primary children:** C1, C5
- **Primary nodes:** 587
- **Side-relative coverage:** 22.1%
- **Semantic-eligible coverage:** 47.2%
- **Confidence:** High

**Evidence.** C1 contains resolving, characterising, exploring, remembering,
initiating, observing, computing, development and inference. C5 contains
conversation, negotiation, management, discussion, psychosocial intervention
and interview/professional activity. Their direct relation contains **335 token
edges**, mean cosine **0.10415**, the highest-mean large positive semantic pair
in the state. The common generator is coordinated inquiry and professional
action: observation/inference/process work is carried out through communication,
negotiation and organised intervention.

**Secondary links:** C10 and C7. C1–C10 has **91 edges**, C5–C10 **84**,
supporting a publishing/communication-output relation. C1–C7 has **82** and
C5–C7 **102**, linking technical interfaces to organised work without making
them core children.

**Exclusion boundary.** C1 is process/cognitive-action oriented; C5 is
social/professional and communicative. C10 is publication/paratext rather than
the activity itself. C7 contains substantial measurement/abbreviation structure.

**Alternative.** Include C10 as a third child under a broader
`inquiry, communication and information production` parent. This remains
plausible but would overstate the small publishing community's integration into
the core pair.

### P+1 — Biomedical and interacting physical-system organisation

- **Primary children:** C3, C9
- **Primary nodes:** 396
- **Side-relative coverage:** 14.9%
- **Semantic-eligible coverage:** 31.8%
- **Confidence:** Moderate / High

**Evidence.** C3 supplies biomedical, pharmacological, respiratory and
reproductive terminology. C9 supplies interactions, measurements and
physical/mathematical system dynamics. Their direct relation contains **103
token edges**, mean cosine **0.08955**. The common generator is embodied or
biological systems described through interaction, measurement and dynamic
relations.

**Secondary link:** C5. C3–C5 has **283 edges**, and C5–C9 **138**, showing
strong psychosocial/professional and response-system adjacency without
requiring a broader parent.

**Exclusion boundary.** C3 contains clear clinical/pharmacological semantics;
C9 contains physical/mathematical dynamics. Neither can be collapsed into the
other without losing domain specificity.

**Alternative.** Leave C3 and C9 separate as biomedical and
physical/dynamical-system structures. This is a serious alternative because
their direct edge count is modest; confidence remains Moderate/High rather than
unqualified High.

### Positive irreducible and unresolved structures

- **C7 — mixed-unresolved:** software/interface concepts and
  measurement/technical abbreviations coexist.
- **C10 — irreducible-semantic:** publishing, reading, writing and paratext;
  secondary relation to P+0.
- **C12 — irreducible-semantic:** bodily/affective gestures and ringing/sound
  events.

### Positive formal/name substrate

- C0 — fragmentary process terms and heterogeneous lexical/tokenisation residue
- C2 — grammar/function words/fragments
- C4 — personal names and geographic entities
- C6 — punctuation/software-formatting structure
- C8 — numeric strings
- C11 — multilingual morphology/example fragments

## Negative-side reconstruction

### P-0 — Characterisation, regulatory constraint and adverse evaluation

- **Primary children:** C0, C1
- **Primary nodes:** 1,063
- **Side-relative coverage:** 36.2%
- **Semantic-eligible coverage:** 54.3%
- **Confidence:** High

**Evidence.** C0 contains characterisation, recommendations, regulation,
distribution/system and constitutional concepts. C1 contains catastrophe,
discrimination, prohibition/exclusion and intense evaluation. Their direct
relation is exceptionally strong: **883 token edges**, mean cosine **0.10202**,
by far the largest semantic intercommunity relation in State 14. The common
generator is the characterisation and regulation of problematic, disallowed or
adverse states.

**Secondary links:** C4 and C10. C0–C4 has **334 edges**, C1–C4 **222**,
placing biomedical pathology adjacent to characterisation/adversity. C0–C10
has **143** and C1–C10 **95**, linking formal mathematical structures to
system/characterisation language.

**Exclusion boundary.** C0 includes neutral recommendations, algorithms and
distribution concepts; C1 is much more overtly adverse and prohibitive. The
parent therefore cannot be reduced to “negative evaluation” or “prohibition”.

**Alternative.** Split C0 and C1 into neutral/system characterisation and
adverse/prohibitive evaluation. This is semantically defensible, but the
exceptional direct relation supports the higher-order parent strongly.

### P-1 — Institutional, familial and territorial order

- **Primary children:** C5, C9
- **Primary nodes:** 276
- **Side-relative coverage:** 9.4%
- **Semantic-eligible coverage:** 14.1%
- **Confidence:** Moderate

**Evidence.** C5 contains religion, monarchy, family and mythic/social roles.
C9 contains geographic/political entities and legal/historical terms. Their
direct relation contains **60 token edges**, mean cosine **0.09712**. The common
generator is institutional and social order situated within territorial or
political contexts.

**Secondary link:** C6. C5–C6 has **142 edges**, showing strong adjacency
between social/institutional roles and their material settings.

**Exclusion boundary.** C5 contains family and mythic roles as well as formal
institutions; C9 contains legal/historical entities as well as places. C6 is
not absorbed because roads, terrain and household objects are material
environments rather than institutional order.

**Alternative.** Leave C5 and C9 separate. This remains a serious alternative
because the direct relation is moderate rather than dominant.

### P-2 — Material and technical infrastructure

- **Primary children:** C6, C7
- **Primary nodes:** 296
- **Side-relative coverage:** 10.1%
- **Semantic-eligible coverage:** 15.1%
- **Confidence:** Moderate / High

**Evidence.** C6 contains vehicles, roads, terrain, household/material objects
and physical artefacts. C7 contains hardware, electronics, appliances and
infrastructure equipment. Their direct relation contains **74 token edges**,
mean cosine **0.10295**. The common generator is material/technical
infrastructure and equipment.

**Secondary link:** P-1 through C5–C6 (**142 edges**) and weaker C5–C7
connections, placing infrastructure in institutional/social settings.

**Exclusion boundary.** C6 includes natural terrain and consumable/material
objects, while C7 is more specifically technological equipment. The parent is
therefore not narrowed to “hardware” or broadened to generic physical objects.

**Alternative.** Leave C6 and C7 separate as broad physical-world and technical
equipment communities. This remains plausible; confidence is Moderate/High.

### Negative irreducible and unresolved structures

- **C4 — irreducible-semantic:** cardiovascular disease, trauma, pathology and
  biomedical morphology; secondary relation to P-0.
- **C10 — irreducible-semantic:** algebra, topology, subsets and continuity;
  secondary relation to P-0.
- **C12 — mixed-unresolved:** multiplicity morphology and software
  status/message tokens coexist.

### Negative formal/name substrate

- C2 — personal names plus biomedical/technical fragments
- C3 — grammar/function words/fragments
- C8 — numeric strings
- C11 — mathematical/code punctuation

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 411 | Fragmentary process terms + lexical residue | formal-substrate | — | Morphological/tokenisation organisation dominates. |
| + | C1 | 328 | Resolution/observation/inference/development | parent:P+0 | — | Inquiry/process-action child. |
| + | C2 | 321 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C3 | 287 | Biomedical/pharmacological/respiratory/reproductive | parent:P+1 | — | Biomedical-system child. |
| + | C4 | 263 | Personal names + geography | formal-substrate | — | Name/entity organisation without one semantic domain. |
| + | C5 | 259 | Social/professional communication/intervention | parent:P+0 | — | Coordinated professional-action child. |
| + | C6 | 250 | Maths/code punctuation + formatting/software residue | formal-substrate | — | Formatting/tokeniser organisation dominates. |
| + | C7 | 152 | Software/interface + measurement/abbreviations | mixed-unresolved | P+0 | Technical-semantic and form structures coexist. |
| + | C8 | 110 | Numeric strings/years | formal-substrate | — | Numeric form. |
| + | C9 | 109 | Interactions/measurement/physical dynamics | parent:P+1 | — | Physical/dynamical-system child. |
| + | C10 | 79 | Publishing/reading/writing/paratext | irreducible-semantic | P+0 | Information-output relation without primary absorption. |
| + | C11 | 53 | Multilingual/example morphology | formal-substrate | — | Morphological organisation dominates. |
| + | C12 | 30 | Bodily gestures/affect + ringing/sound | irreducible-semantic | — | Coherent small semantic domain without a sibling parent. |
| − | C0 | 579 | Characterisation/recommendations/regulation/systems | parent:P-0 | — | Characterisation/regulatory child. |
| − | C1 | 484 | Catastrophe/discrimination/prohibition/intensity | parent:P-0 | — | Adverse/prohibitive child. |
| − | C2 | 421 | Personal names + biomedical/technical fragments | formal-substrate | — | Name/form organisation without one semantic class. |
| − | C3 | 386 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| − | C4 | 237 | Cardiovascular/pathology/trauma/biomedical morphology | irreducible-semantic | P-0 | Clinical/pathology relation without primary absorption. |
| − | C5 | 209 | Religion/monarchy/family/mythic roles | parent:P-1 | — | Institutional/familial-role child. |
| − | C6 | 162 | Vehicles/roads/terrain/household objects | parent:P-2 | P-1 | Material-infrastructure child with institutional-setting relation. |
| − | C7 | 134 | Hardware/electronics/appliances/infrastructure | parent:P-2 | — | Technical-infrastructure child. |
| − | C8 | 120 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C9 | 67 | Geographic/political/legal/historical entities | parent:P-1 | — | Territorial/public-order child. |
| − | C10 | 66 | Algebra/topology/subsets/continuity | irreducible-semantic | P-0 | Formal-system relation without semantic collapse. |
| − | C11 | 47 | Maths/code punctuation | formal-substrate | — | Formatting form. |
| − | C12 | 21 | Multiplicity forms + software status/messages | mixed-unresolved | — | Two organising principles coexist. |

Every State 14 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Coordinated inquiry, communication and professional action | C1, C5 | 587 | 22.1% | 47.2% | High |
| P+1 | Biomedical and interacting physical-system organisation | C3, C9 | 396 | 14.9% | 31.8% | Moderate / High |
| P-0 | Characterisation, regulatory constraint and adverse evaluation | C0, C1 | 1,063 | 36.2% | 54.3% | High |
| P-1 | Institutional, familial and territorial order | C5, C9 | 276 | 9.4% | 14.1% | Moderate |
| P-2 | Material and technical infrastructure | C6, C7 | 296 | 10.1% | 15.1% | Moderate / High |

Positive retained parents account for **983 nodes**, **37.1% of the positive
population** and **79.0% of semantic-eligible positive nodes**.

Negative retained parents account for **1,635 nodes**, **55.7% of the negative
population** and **83.5% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — inquiry/social activity and biomedical-system relation — High.**
   C1–C3 has **281 edges**, C1–C9 **137**, C5–C3 **283** and C5–C9 **138**.
   Biomedical/physical-system content is strongly embedded in professional and
   inferential activity without becoming the same generator.

2. **P+0 ↔ C10 — information-production relation — Moderate.**
   C1–C10 has **91 edges** and C5–C10 **84**, supporting a publishing/output
   satellite around inquiry and communication.

3. **P+0 ↔ C7 — interface/tool relation — Moderate.**
   C1–C7 has **82 edges** and C5–C7 **102**. Software/interface systems support
   coordinated activity, but measurement and abbreviation structure prevents
   parent absorption.

4. **P+1 ↔ C7 — technical-system relation — Moderate.**
   C3–C7 has **116 edges** and C9–C7 **64**, showing technical adjacency
   without a common parent.

### Negative-side relations

1. **P-0 ↔ P-1 — regulation/adversity in institutional context — High.**
   C0–C5 has **263 edges**, C1–C5 **239**, C0–C9 **75** and C1–C9 **30**.
   Regulatory/adverse semantics are strongly embedded in institutional,
   familial and territorial contexts.

2. **P-0 ↔ P-2 — regulation/adversity and material systems — Moderate to High.**
   C0–C6 has **211 edges**, C0–C7 **164**, C1–C6 **179** and C1–C7 **46**.
   Physical and technical systems provide material domains in which
   regulatory/adverse relations operate.

3. **P-1 ↔ P-2 — social order and material setting — High.**
   C5–C6 has **142 edges**, mean cosine **0.09744**, with weaker C5–C7 and
   C9-facing relations. Material environments support institutional and
   territorial organisation without collapsing into it.

4. **C4 and C10 are analytical satellites of P-0.**
   Clinical/pathological C4 and mathematical C10 both connect strongly to C0
   and C1 but remain distinct semantic systems rather than children of the
   evaluative/regulatory parent.

## Cross-side bridge candidates

No cross-side parent bridge is retained.

Plausible but unpromoted correspondences include:

- positive P+0 and negative P-0 through characterisation/inference;
- positive P+1 and negative C4 through biomedical/pathological structure;
- positive C7 and negative P-2 through technical/interface infrastructure;
- positive C4 and negative P-1 through geographic/entity context.

No parent-level bridge is promoted without direct cross-side community
evidence sufficient to distinguish semantic structure from lexical proximity.

## Formal/representational substrate

### Positive — 1,408 nodes / 53.1%

- fragmentary action/process and lexical/tokeniser residues;
- grammar/function words and fragments;
- personal-name/geographic entity organisation;
- mathematical/code punctuation and formatting;
- numeric strings;
- multilingual morphology/example fragments.

### Negative — 974 nodes / 33.2%

- personal names plus biomedical/technical fragments;
- grammar/function words/fragments;
- numeric strings;
- mathematical/code punctuation.

## Minimal state-level architecture

```text
STATE 14 — BLOCK 13 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 COORDINATED INQUIRY / COMMUNICATION / PROFESSIONAL ACTION
|   +-- C1 resolution/observation/inference/development
|   `-- C5 social/professional communication/intervention
|       |
|       +-- C10 publishing/reading/writing             [secondary]
|       `-- C7 software/interface/measurement          [secondary; mixed]
|
+-- P+1 BIOMEDICAL & INTERACTING PHYSICAL-SYSTEM ORGANISATION
|   +-- C3 biomedical/pharmacological/respiratory
|   `-- C9 interactions/measurement/physical dynamics
|
+-- C7 software/interface + measurement/abbreviations [mixed unresolved]
+-- C10 publishing/reading/writing/paratext            [irreducible]
+-- C12 bodily gestures/affect + ringing/sound         [irreducible]
`-- C0,C2,C4,C6,C8,C11                               [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 CHARACTERISATION / REGULATORY CONSTRAINT / ADVERSE EVALUATION
|   +-- C0 characterisation/recommendations/regulation/systems
|   `-- C1 catastrophe/discrimination/prohibition/intensity
|       |
|       +-- C4 cardiovascular/pathology                [secondary]
|       `-- C10 algebra/topology                       [secondary]
|
+-- P-1 INSTITUTIONAL / FAMILIAL / TERRITORIAL ORDER
|   +-- C5 religion/monarchy/family/mythic roles
|   `-- C9 geographic/political/legal entities
|       \
|        -- C6 material setting                        [secondary]
|
+-- P-2 MATERIAL & TECHNICAL INFRASTRUCTURE
|   +-- C6 vehicles/roads/terrain/household objects
|   `-- C7 hardware/electronics/appliances
|
+-- C4 cardiovascular/pathology/trauma                 [irreducible]
+-- C10 algebra/topology/continuity                     [irreducible]
+-- C12 multiplicity + software status/messages        [mixed unresolved]
`-- C2,C3,C8,C11                                      [formal/name substrate]
```

The preferred State 14 reconstruction contains two positive and three negative
multi-community parents. The positive side remains relatively selective because
several large populations are form-organised or internally mixed. The negative
side is substantially more compressible, dominated by a very large
characterisation/regulation/adversity parent with separate institutional and
material-infrastructure structures.

This statement is local to State 14 and is not a cross-state trajectory claim.

## Alternative reconstruction

The strongest competing alternatives are:

1. include positive C10 under P+0 as an information-production child;
2. leave positive C3 and C9 separate rather than retaining P+1;
3. split negative P-0 into characterisation/system C0 and
   catastrophe/prohibition C1;
4. leave negative C5 and C9 separate rather than retaining P-1;
5. leave negative C6 and C7 separate rather than retaining P-2.

The third alternative is the most serious semantically, but the **883-edge**
C0–C1 relation makes the higher-order P-0 generator difficult to dismiss.

## Uncertainty record

- **Positive P+1:** biomedical and physical/dynamical systems are related but
  retain strong child-domain differences.
- **Positive C7:** software/interface semantics are real, but measurement and
  abbreviation organisation is substantial.
- **Positive C4:** coherent names/geography are treated as name substrate rather
  than a semantic parent because no common domain beyond entity form is
  established.
- **Negative P-0:** is broad but supported by the strongest semantic
  intercommunity relation in the state.
- **Negative P-1:** the territorial/institutional abstraction is plausible but
  rests on a moderate direct edge count.
- **Negative P-2:** material-world and technical-equipment children remain
  distinguishable, so confidence is Moderate/High.
- **Negative C12:** is genuinely mixed across multiplicity morphology and
  software-status semantics.
- **Full token membership:** the compressed token-level artifact was
  inaccessible through the current GitHub text connector, so ambiguity was
  preserved rather than silently resolved.

## Verification

- Positive communities accounted for: **13 / 13**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **26 / 26**
- Positive node accounting: **2,652 / 2,652**
- Negative node accounting: **2,933 / 2,933**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1**
- Retained negative parent IDs: **P-0, P-1, P-2**
- Every retained parent has an exclusion boundary: **yes**
- Every State 14 community inspected at underlying R008 community-record level: **yes**
- All State 14 within-side community relations inspected: **yes**
- Full token-membership inspection falsely claimed: **no**
- Later-state evidence used in State 14 inference: **no**
- Strict state-isolation source exposure breach during this state: **no**
- Materially ambiguous communities retained as Moderate/mixed/secondary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 14 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
