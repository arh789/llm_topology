# R010 State 00 — input embedding latent structure

## State identity

- R010 state index: `00`
- R008/R009 state: `input_embedding`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 10 negative-tail = 22**
- R008 population: **1,871 positive-head + 1,316 negative-tail = 3,187 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 00 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

The reconstruction used:

1. `R009/STATE_00_input_embedding.md`;
2. State 00 records in `R009_SUMMARY.html`;
3. the underlying State 00 rows in R008 `community_nodes.csv`;
4. State 00 intercommunity graph relations in R008 `community_edges.csv` and
   `chatgpt_layer_packets.md`;
5. the R008 graph-central representative tokens and target-extreme tokens for
   every one of the 22 communities;
6. the R008 token-class composition, internal-edge counts, boundary-edge counts,
   mean degree and target-cosine ranges for every community.

The R009 identity labels were treated as hypotheses. Parent assignments were
made only after checking the underlying R008 community evidence.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 361 | 2,103 / 1,270 | 15.17 | +0.06135 | Degree-central and extreme members converge on pharmacology, disease and biomedical chemistry: `antidepress`, `glutathione`, `schizophrenia`, `glucose`, `doxorubicin`, `metformin`, `cisplatin`. |
| C1 | 262 | 1,406 / 773 | 13.68 | +0.05993 | The community is genuinely mixed: personal/geographic names (`Iran`, `Kuwait`, `Malaysia`, `Massachusetts`) coexist with exceptionally target-proximal `Li`/`Lith` forms. No single semantic parent is defensible. |
| C2 | 230 | 908 / 1,191 | 13.07 | +0.05804 | Thermal/liquid/environmental process vocabulary dominates: `Temperature`, `thermally`, `cooling`, `groundwater`, `liquids`, with extreme `recharge`, `molten`, `hydration`, `recycling`. |
| C3 | 206 | 1,025 / 948 | 14.55 | +0.06099 | Electrochemical/electrical-energy organisation is strong: `electrochemical`, `conductivity`, `capacitance`, `electrodes`; extremes include `electrolyte`, `battery`, `cathode`. |
| C4 | 182 | 808 / 883 | 13.73 | +0.05902 | Consumer/digital/network technology dominates: `cryptocurrencies`, `telecommunications`, `Samsung`, `Bluetooth`, `laptops`, `Apple`, `Bitcoin`, with `LTE`, `Tesla`, `solar` among extremes. |
| C5 | 142 | 905 / 112 | 13.54 | +0.05721 | Exceptionally internally bounded numeric cluster; members are overwhelmingly three-digit strings. This is representational form, not a semantic parent. |
| C6 | 139 | 589 / 669 | 13.29 | +0.05763 | Element/material notation: `Zn`, `Ti`, `Mg`, `Cu`, `Cd`, `Hg`, `Na`, with `graphene`, `nanoparticle` and `layered`. |
| C7 | 127 | 644 / 603 | 14.89 | +0.06893 | Inorganic substances and elemental chemistry: `phosphorus`, `hydrogen`, `phosphate`, `chloride`, `hydroxide`; extremes include `helium`, `alkali`, `carbonate`, `KCl`. |
| C8 | 105 | 491 / 588 | 14.95 | +0.08106 | Metals/minerals/engineering materials: `aluminum`, `titanium`, `magnesium`, `copper`, `zinc`, with extreme `cobalt`, `sodium`, `nickel`, `calcium`. |
| C9 | 66 | 273 / 375 | 13.95 | +0.06189 | Psychoactive/pharmacological and consumable substances: `methamphetamine`, `alcohol`, `heroin`, `morphine`, `opioid`, `cannabis`, `nicotine`; food/drink terms remain a real secondary component. |
| C10 | 30 | 70 / 194 | 11.13 | +0.05570 | Replacement characters, multilingual fragments and tokenizer residue dominate. |
| C11 | 21 | 80 / 134 | 14.00 | +0.06082 | Small but coherent intervention cluster: `intravenous`, `implants`, `injection`, `implantation`, `heparin`, `ablation`, `catheter`. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 307 | 1,313 / 1,309 | 12.82 | -0.04351 | Personal names and short name-like fragments dominate (`Ted`, `Fred`, `Ron`, `Rick`, `Wesley`, `Vernon`), but there is no common social/domain identity beyond naming form. |
| C1 | 222 | 887 / 1,088 | 12.89 | -0.04333 | Text/dialogue/interface processing: `Session`, `writer`, `Reader`, `Dialog`, `Context`, `Parser`, `handler`, with `Menu`, `Wrapper`, `Cursor` at the extreme. |
| C2 | 172 | 653 / 1,012 | 13.48 | -0.04292 | Comprehension/literature/entertainment/evaluation: `fascinating`, Shakespeare fragment, `comprehend`, `acquainted`, `entertain`, with `circus`, `obscure`, `vague`. |
| C3 | 138 | 511 / 745 | 12.80 | -0.04199 | Heterogeneous action/change/representation vocabulary: `negotiated`, `depicting`, `altered`, `finishing`, `knew`; extremes include `specified`, `overlapping`, `uncover`. |
| C4 | 116 | 401 / 736 | 13.26 | -0.04288 | Word endings and fragments dominate. This is morphological form rather than semantic organisation. |
| C5 | 115 | 447 / 692 | 13.79 | -0.04305 | Coherent domestic-animal/pet-care cluster: `birds`, `horses`, `Dog`, veterinary fragments, `ducks`, `bred`, `owners`. |
| C6 | 77 | 402 / 259 | 13.81 | -0.04152 | Strongly bounded punctuation/whitespace/formatting cluster; 58 of 77 tokens are punctuation or symbols. |
| C7 | 74 | 252 / 512 | 13.73 | -0.04577 | Police/security/military personnel and ranks: `Officers`, `Capt`, `Sgt`, `Sergeant`, `detective`, `Patrol`, `cops`, `guards`. |
| C8 | 69 | 208 / 452 | 12.58 | -0.04163 | Evaluation/statistics/reporting/administration: `Evaluation`, `quantified`, `overview`, `stats`, `experimentation`, `committee`, `Statistical`, `Administrative`. |
| C9 | 26 | 143 / 87 | 14.35 | -0.04323 | Small, internally bounded numeric-string cluster. |

## Population accounting

### Positive head

Total nodes: **1,871**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,255 | 67.1% |
| Formal substrate | 172 | 9.2% |
| Irreducible semantic | 182 | 9.7% |
| Mixed unresolved | 262 | 14.0% |
| Unclear | 0 | 0.0% |
| **Total** | **1,871** | **100.0%** |

Semantic-eligible denominator, excluding formal substrate and unclear:
**1,699 nodes**.

### Negative tail

Total nodes: **1,316**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 463 | 35.2% |
| Formal/name substrate | 526 | 40.0% |
| Irreducible semantic | 327 | 24.8% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **1,316** | **100.0%** |

Semantic-eligible denominator, excluding formal/name substrate and unclear:
**790 nodes**.

The asymmetry is substantive. The positive population admits considerably more
compression into multi-community semantic parents than the negative population.

## Positive-side reconstruction

### P+0 — Chemical and engineering material composition

- **Primary children:** C6, C7, C8
- **Primary nodes:** 371
- **Side-relative coverage:** 19.8%
- **Semantic-eligible coverage:** 21.8%
- **Confidence:** High

**Evidence.** C6 supplies element/material notation, C7 inorganic chemical
substances and C8 metals/minerals/engineering materials. Their underlying graph
relations support a shared material-composition frame: C6–C8 has 64
intercommunity token edges with mean cosine **0.16684**, C7–C8 has 99 edges at
**0.12803**, and C6–C7 has 44 edges at **0.09711**.

**Exclusion boundary.** C2 and C3 are related but primarily describe physical
and electrochemical *processes*, not composition. C0 is biomedical rather than
generic material chemistry.

**Alternative.** Merge P+0 with P+1 into a single physical/material-energy
parent. This becomes preferable only if the process/composition distinction
fails under broader membership inspection.

### P+1 — Physical/environmental and electrochemical energy processes

- **Primary children:** C2, C3
- **Primary nodes:** 436
- **Side-relative coverage:** 23.3%
- **Semantic-eligible coverage:** 25.7%
- **Confidence:** High

**Evidence.** C2 contains thermal, liquid, groundwater, cooling, recharge and
molten/recycling processes. C3 contains electrochemical, electrical,
conductivity, electrodes, electrolytes, batteries and cathodes. C2–C3 is the
strongest positive intercommunity connection by edge count at State 00:
**306 token edges**, mean cosine **0.11224**.

**Exclusion boundary.** C4 is technological but its core is consumer/digital
and telecommunications rather than physical-energy process organisation.
C6–C8 describe materials themselves rather than their transformations.

**Alternative.** A narrower split into thermal/environmental processes and
electrochemical-energy technology would leave both structures as single
communities and would therefore explain less of the observed higher-order
organisation.

### P+2 — Biomedical/pharmacological substances and intervention

- **Primary children:** C0, C9, C11
- **Primary nodes:** 448
- **Side-relative coverage:** 23.9%
- **Semantic-eligible coverage:** 26.4%
- **Confidence:** High for C0+C11; Moderate for inclusion of C9

**Evidence.** C0 is strongly biomedical/pharmacological; C11 is directly
medical intervention; C9 is organised around drugs/intoxicants and bioactive
consumables. C0–C9 has **128 edges** at mean cosine **0.12002** and C0–C11 has
**55 edges** at **0.11546**. C11 is only 21 nodes, making that C0 connection
substantial relative to its size.

**Exclusion boundary.** Generic inorganic chemistry in C7 and engineering
materials in C8 are not biomedical merely because they are substances.
Food/drink members inside C9 prevent treating the entire parent as narrowly
clinical.

**Alternative.** Retain C9 as an irreducible consumable/intoxicant community
and define P+2 only from C0+C11. That alternative is favoured if broader C9
membership proves dominated by ordinary consumables rather than psychoactive or
pharmacological substances.

### Positive irreducible and unresolved structures

- **C4 — irreducible-semantic:** applied consumer/digital/network technology.
  It is semantically coherent but no second community shares enough of its
  organising principle to justify a separate parent.
- **C1 — mixed-unresolved:** geographic/personal-name organisation and
  lithium/Li lexical forms genuinely coexist. Promoting it to a semantic parent
  would erase the mixed structure.
- **C5, C10 — formal-substrate:** numeric and tokenizer/encoding organisation.

## Negative-side reconstruction

### P-0 — Symbolic/information interpretation and evaluation

- **Primary children:** C1, C2, C8
- **Primary nodes:** 463
- **Side-relative coverage:** 35.2%
- **Semantic-eligible coverage:** 58.6%
- **Confidence:** Moderate

**Evidence.** C1 concerns text/dialogue/interface processing, C2 concerns
comprehension/literature/entertainment/evaluative interpretation, and C8
concerns evaluation/statistics/reporting/administration. Their graph relations
are mutually present: C1–C2 has **164 token edges** at mean cosine **0.08351**,
C1–C8 has **102** at **0.08167**, and C2–C8 has **76** at **0.07993**. The
common structure is handling, interpreting, describing or evaluating symbolic
information.

**Exclusion boundary.** C3 contains some representation-related terms
(`depicting`, `knew`) but also negotiation, surrender, alteration, hunting
and completion. Absorbing it would make the parent too broad. C7 describes
security personnel rather than information processing.

**Alternative.** Expand P-0 to include C3 under a larger
representation/interpretation/transformation parent. This is a serious
alternative because C2–C3 is the strongest negative intercommunity connection
among semantic communities at **227 edges**, mean cosine **0.08580**. The
preferred reconstruction leaves C3 outside because its underlying membership
is too action-heterogeneous.

### Negative irreducible structures

- **C3 — irreducible-semantic:** action/change/depiction/completion. It has a
  secondary link to P-0 because depiction and knowing overlap symbolic
  processing, but its action semantics prevent primary absorption.
- **C5 — irreducible-semantic:** domestic animals/pets/animal care.
- **C7 — irreducible-semantic:** police/military/security personnel and ranks.

### Negative formal/name substrate

- **C0 — formal-substrate:** personal-name/name-fragment organisation. The
  membership identifies people lexically, but no coherent domain of people is
  present.
- **C4 — formal-substrate:** lexical/morphological endings.
- **C6 — formal-substrate:** punctuation/formatting/whitespace.
- **C9 — formal-substrate:** numeric strings.

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 361 | Medicine, disease and pharmacology | parent:P+2 | — | Coherent biomedical/pharmacological domain. |
| + | C1 | 262 | Names/geography + Li forms | mixed-unresolved | — | Two materially different organising principles. |
| + | C2 | 230 | Thermal/liquid/environmental processes | parent:P+1 | — | Physical-process structure. |
| + | C3 | 206 | Electrochemistry/electricity/storage | parent:P+1 | — | Energy/electrochemical process structure; strongly linked to C2. |
| + | C4 | 182 | Consumer/digital technology | irreducible-semantic | — | Coherent but lacks a second sufficiently similar child. |
| + | C5 | 142 | Three-digit numbers | formal-substrate | — | Numeric form dominates. |
| + | C6 | 139 | Element/material notation | parent:P+0 | — | Material-composition structure. |
| + | C7 | 127 | Inorganic chemistry | parent:P+0 | — | Material/chemical composition. |
| + | C8 | 105 | Metals/minerals/materials | parent:P+0 | — | Engineering/material composition. |
| + | C9 | 66 | Drugs/intoxicants/consumables | parent:P+2 | — | Bioactive/pharmacological substance structure, with consumable heterogeneity retained. |
| + | C10 | 30 | Tokenizer/encoding residue | formal-substrate | — | Representational artefact. |
| + | C11 | 21 | Injection/implantation/vascular intervention | parent:P+2 | — | Biomedical intervention structure. |
| − | C0 | 307 | Personal names/fragments | formal-substrate | — | Name form without a coherent domain-level identity. |
| − | C1 | 222 | Text/dialogue/software interface | parent:P-0 | — | Symbolic/information handling. |
| − | C2 | 172 | Comprehension/literature/entertainment | parent:P-0 | — | Symbolic interpretation/evaluation. |
| − | C3 | 138 | Change/depiction/completion actions | irreducible-semantic | P-0 | Partial representation/interpretation overlap but substantial action heterogeneity. |
| − | C4 | 116 | Word endings/fragments | formal-substrate | — | Morphological form. |
| − | C5 | 115 | Domestic animals/pets | irreducible-semantic | — | Coherent independent semantic island. |
| − | C6 | 77 | Formatting/punctuation | formal-substrate | — | Formatting form. |
| − | C7 | 74 | Police/military/security personnel | irreducible-semantic | — | Coherent independent social-role island. |
| − | C8 | 69 | Evaluation/statistics/admin/reporting | parent:P-0 | — | Information evaluation/reporting. |
| − | C9 | 26 | Numeric strings | formal-substrate | — | Numeric form. |

Every State 00 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Chemical and engineering material composition | C6, C7, C8 | 371 | 19.8% | 21.8% | High |
| P+1 | Physical/environmental and electrochemical energy processes | C2, C3 | 436 | 23.3% | 25.7% | High |
| P+2 | Biomedical/pharmacological substances and intervention | C0, C9, C11 | 448 | 23.9% | 26.4% | High / Moderate |
| P-0 | Symbolic/information interpretation and evaluation | C1, C2, C8 | 463 | 35.2% | 58.6% | Moderate |

Positive retained parents jointly account for **1,255 nodes**, or **67.1% of
the entire positive side** and **73.9% of semantic-eligible positive nodes**.

The negative retained parent accounts for **463 nodes**, or **35.2% of the
entire negative side** and **58.6% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — object/process complementarity — High.**
   P+0 supplies chemical/material substrates; P+1 supplies thermal,
   electrochemical and energy processes acting on or through such substrates.
   The relation is supported both semantically and by substantial
   intercommunity connectivity.

2. **P+0 ↔ P+2 — chemical-substance overlap — Moderate to High.**
   Biomedical/pharmacological organisation necessarily overlaps chemical
   substance organisation. C0 connects strongly to C7 (139 edges, mean cosine
   0.12080), C6 (110, 0.11895) and C8 (108, 0.10853). The exclusion boundary is
   retained because disease/intervention is not reducible to generic chemistry.

3. **P+1 ↔ P+2 — physical/biological process overlap — Moderate.**
   C0–C2 has 230 edges and C0–C3 140, showing that biomedical organisation is
   embedded near physical/process communities without making them one parent.

4. **C4 as an applied-technology satellite to P+1 — Moderate.**
   C3–C4 has 181 edges and C2–C4 150. The relation is real, but C4's digital,
   telecommunications and cryptocurrency centre remains distinct from the
   material-energy parent.

### Negative-side relations

1. **P-0 ↔ C3 — overlap — Moderate.**
   C2–C3 has 227 edges, C1–C3 146 and C3–C8 74. Representation and cognition
   connect the structures, but C3 remains too action-oriented for primary
   absorption.

2. **No second negative parent is retained.**
   Pets/animals and security roles are semantically coherent but do not form a
   defensible common higher-order parent with each other or with P-0.

## Cross-side bridge candidates

**No semantic cross-side bridge is retained at State 00.**

R008's strongest secondary cross-side relations at this state are dominated by
near-lexical or numeric correspondences such as `rules`↔`Rules` and
neighbouring numeric strings. They do not establish a bridge between the
retained semantic parents.

A possible technology/information relation between positive C4 and negative
P-0 is noted but not promoted because positive C4 is an irreducible community,
not a multi-community parent, and the evidence does not justify restructuring
the positive side merely to manufacture a bridge.

## Formal/representational substrate

The state contains substantial non-parent organisation:

### Positive

- C5 numeric strings: 142 nodes
- C10 tokenizer/encoding residue: 30 nodes
- C1 mixed name/geography + Li lexical forms: 262 nodes, kept separate because
  it combines representational and semantic/target-lexical organisation

### Negative

- C0 personal-name/name-fragment organisation: 307 nodes
- C4 morphology: 116
- C6 formatting: 77
- C9 numeric strings: 26

The negative side therefore contains a much larger formal/name component than
the positive side: **40.0% versus 9.2% formal substrate**, before counting the
positive mixed C1 community.

## Minimal state-level architecture

```text
STATE 00 — INPUT EMBEDDING

POSITIVE-HEAD ORGANISATION
|
+-- PHYSICAL / MATERIAL-ENERGY BRANCH
|   |
|   +-- P+0 Chemical & engineering material composition
|   |   +-- C6 element/material notation
|   |   +-- C7 inorganic chemistry
|   |   `-- C8 metals/minerals/materials
|   |
|   `-- P+1 Physical/environmental & electrochemical energy processes
|       +-- C2 thermal/liquid/environmental processes
|       `-- C3 electrochemistry/electricity/storage
|
+-- P+2 BIOMEDICAL / PHARMACOLOGICAL SUBSTANCE & INTERVENTION
|   +-- C0 medicine/disease/pharmacology
|   +-- C9 drugs/intoxicants/consumables
|   `-- C11 injection/implantation/vascular intervention
|
+-- C4 applied consumer/digital technology             [irreducible]
+-- C1 names/geography + Li lexical forms              [mixed unresolved]
`-- C5 numeric; C10 tokenizer                          [formal substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 SYMBOLIC / INFORMATION INTERPRETATION & EVALUATION
|   +-- C1 text/dialogue/interface processing
|   +-- C2 comprehension/literature/entertainment
|   `-- C8 evaluation/statistics/reporting
|
+-- C3 action/change/depiction                         [irreducible; overlaps P-0]
+-- C5 domestic animals/pets                           [irreducible]
+-- C7 police/military/security roles                  [irreducible]
`-- C0 names; C4 morphology; C6 formatting; C9 numeric
                                                       [formal/name substrate]
```

The smallest defensible reconstruction is therefore **not** a single latent
theme. The positive side is principally organised by an interconnected
physical/material-energy branch plus a biomedical/pharmacological branch,
whereas the negative side is substantially less compressible and contains one
symbolic/information parent surrounded by independent semantic islands and a
large formal/name substrate.

This is a State 00 description only. It is not yet evidence of a transformer
trajectory.

## Alternative reconstruction

The strongest alternative has two changes:

1. merge P+0 and P+1 into one broad **physical/material-energy systems** parent;
2. expand P-0 to absorb negative C3 into a broader
   **representation/interpretation/transformation** parent.

This alternative yields greater compression.

It is not preferred because:

- merging positive composition and process loses a meaningful distinction that
  is separately expressed by the communities;
- absorbing negative C3 requires treating negotiation, surrender, alteration,
  hunting and completion as instances of symbolic processing merely because
  depiction/knowing are also present.

Evidence favouring the alternative would be broader underlying membership
showing that C2/C3/C6/C7/C8 are substantially intermingled around one common
physical-material relation, or that negative C3 is dominated by representation
and cognition rather than general action/change semantics.

## Uncertainty record

- **Positive C1:** remains intentionally unresolved because lithium lexical
  variants and names/geography are both real organising components.
- **Positive P+2 / C9:** the parent is stable, but C9's food/drink component
  makes its biomedical inclusion less certain than C0 or C11.
- **Negative P-0:** the parent is defensible but broad; C1, C2 and C8 occupy
  different kinds of information handling.
- **Negative C3:** is the most consequential boundary decision. Its strong
  graph relation to C2 makes secondary membership in P-0 plausible, but its
  action vocabulary blocks primary assignment.
- **Negative C0:** treating names as formal/name substrate rather than a
  semantic people-parent is deliberate; the community lacks a common social
  class beyond being names.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **10 / 10**
- Total communities accounted for: **22 / 22**
- Positive node accounting: **1,871 / 1,871**
- Negative node accounting: **1,316 / 1,316**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0**
- Every retained parent has an exclusion boundary: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 00 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with later states.

No persistence, emergence, disappearance, split, merge, polarity-change,
optimal-layer, SDA-3 or curvature inference is made here.
