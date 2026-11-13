# R010 State 01 — Block 0 output latent structure

## State identity

- R010 state index: `01`
- R008/R009 state: `block_00_output`
- Analysis model: **GPT-5.6 Sol**
- Protocol: `R010_ANALYSIS_PROTOCOL.md`
- R009 communities: **12 positive-head + 13 negative-tail = 25**
- R008 population: **3,125 positive-head + 2,793 negative-tail = 5,918 nodes**
- Status: Phase-A independent reconstruction complete

This file reconstructs State 01 only. No R010 reconstruction from another state
was inspected or used to shape the parent labels.

## Evidence inventory

For every State 01 community, the reconstruction inspected the underlying R008
community record rather than relying on the HTML summary or R009 prose alone.

Evidence used:

1. `R009/STATE_01_block_00_output.md`;
2. the State 01 entries in `R009_SUMMARY.html`;
3. all 25 State 01 rows in R008 `community_nodes.csv`, including community
   size, internal/boundary edges, mean degree, target-cosine range,
   graph-central representatives, target-extreme tokens and token classes;
4. all State 01 within-side relations in R008 `community_edges.csv`;
5. the State 01 R008 layer packet and compact-network interpretation boundary.

No compressed token-level membership escalation was required for a final
High-confidence parent. Mixed communities used as parent children remain
Moderate confidence where their compact R008 evidence contains genuine
heterogeneity.

## Underlying R008 community inspection

### Positive head

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 402 | 2,066 / 2,041 | 15.36 | +0.03134 | Function words and short grammatical/lexical pieces dominate: `was`, `is`, `have`, `all`, `more`, `am`, plus short fragments. Primarily formal language structure. |
| C1 | 380 | 1,476 / 2,033 | 13.12 | +0.03203 | Database/software/data-system vocabulary is strong: `mysql`, `MySQL`, `sqlite`, `SQL`, `Database`, `db`, `innerHTML`, `Login`; extremes include `Hash`, `CSS`, `nginx`. |
| C2 | 370 | 1,392 / 1,752 | 12.26 | +0.03131 | Personal names dominate, mixed with multilingual/name fragments and replacement characters. No coherent domain of people beyond name-form organisation. |
| C3 | 280 | 1,691 / 629 | 14.33 | +0.03245 | Strongly bounded punctuation/bracket/code-formatting cluster; 205 of 280 tokens are punctuation/symbols. |
| C4 | 279 | 1,075 / 1,611 | 13.48 | +0.03134 | Maintenance, review, recognition, access and information-handling actions: `maintaining`, `reviewing`, `highlighted`, `recognizing`, `documented`, `researching`, `recalling`; extremes include `accessing`, `solved`, `remembers`, `referenced`. |
| C5 | 272 | 1,027 / 1,390 | 12.66 | +0.03201 | Acronyms and short technical/scientific initialisms dominate. Organisation is primarily lexical/formal rather than one semantic domain. |
| C6 | 252 | 1,157 / 1,363 | 14.59 | +0.03194 | Nationality, governance and social-administrative descriptors: `Nigerian`, `Indonesian`, `Pakistani`, `politically`, `administrative`, `Chinese`, `Pakistan`, `Financial`, `bureaucracy`. Psychological/psychosocial terms broaden the community. |
| C7 | 251 | 1,081 / 1,403 | 14.20 | +0.03140 | Evaluative, degree and discourse language: `extraordinarily`, `interesting`, `satisfactory`, `unsatisfactory`, `probably`, `Therefore`, `Subsequently`, `vastly`; extremes retain comparative/temporal/evaluative descriptors. |
| C8 | 191 | 650 / 1,281 | 13.51 | +0.03149 | Biomedical/endocrine/immune/physiological organisation dominates: `immunosuppressive`, `angiotensin`, `infertility`, `hypothalamus`, `lymphocyte`, `rheumatoid`; material/scientific outliers remain. |
| C9 | 180 | 682 / 1,079 | 13.57 | +0.03127 | Food, plants and biological/agricultural life dominate: `vegetation`, `cabbage`, `vegetable`, `chocolate`, `coconut`, `bread`; extremes add `hatch`, `spiders`, `beet`, `worm`, `clutch`. Travel/infrastructure tokens are genuine outliers. |
| C10 | 141 | 471 / 917 | 13.18 | +0.03130 | People, exercise/sport and institutional participation dominate: `athletes`, `adolescents`, `workers`, `exercising`, `Programme`, `Broncos`, `Department`, `discussions`; extremes include `woman`, `games`, `children`, `athlete`, `Exercise`, `chess`. |
| C11 | 127 | 760 / 237 | 13.83 | +0.03000 | Strongly bounded numeric/year cluster. |

### Negative tail

| Community | Size | Internal / boundary edges | Mean degree | Mean target cosine | Underlying inspection |
|---|---:|---:|---:|---:|---|
| C0 | 401 | 1,775 / 1,829 | 13.41 | -0.03172 | Personal names and geographic/name-like fragments dominate. No single social class or domain links the names. |
| C1 | 358 | 1,565 / 1,825 | 13.84 | -0.03111 | Biomedical science/research dominates: `pathophysiology`, `zebrafish`, `epidemiology`, `methodologies`, `phenotypes`, `anesthesia`, `cerebellum`; extremes include `biomarkers`, `allele`, `assay`, `homozygous`. |
| C2 | 272 | 892 / 1,600 | 12.44 | -0.03187 | Incomplete stems, prefixes and fragments dominate; primarily lexical form. |
| C3 | 268 | 1,049 / 1,576 | 13.71 | -0.03168 | Transformation, inhibition, increase/enhancement and displacement: `transformed`, `transformation`, `Inhibition`, `increase`, `enhancement`, `displacement`, mathematical transformation fragments. |
| C4 | 268 | 1,055 / 1,656 | 14.05 | -0.03222 | Interpretation, instruction, prohibition, recommendation, belief and authority: `interpretation`, `prohibited`, `instructed`, `recommendations`, `prohibition`, `expectations`, `skepticism`; extremes include `Laws`, `beliefs`, `authority`, `approved`. |
| C5 | 257 | 1,067 / 1,392 | 13.72 | -0.03228 | Broad physical/built object world: hallways, stairs, clothing, boats, guns, floors, brewery, artwork, tools/equipment and material objects. |
| C6 | 236 | 917 / 1,436 | 13.86 | -0.03182 | Social/religious/occupational and fictional roles: `Archbishop`, `producer`, `Professor`, `Rabbi`, `Governor`, `Duchess`, plus monsters/demons/villains and creative roles. |
| C7 | 229 | 944 / 1,354 | 14.16 | -0.03168 | Common suffixes, function fragments and word pieces; primarily formal. |
| C8 | 173 | 642 / 1,157 | 14.11 | -0.03235 | Strong affective/evaluative and threat/horror vocabulary: `terrifying`, `monstrous`, `madness`, `weird`, `horrific`, with positive-intensity terms such as `gorgeous`, `magnificent`, `cute`; extremes include `fatal`, `screamed`, `murdered`, `destroyed`. |
| C9 | 104 | 607 / 245 | 14.03 | -0.03109 | Strong numeric cluster. |
| C10 | 90 | 514 / 163 | 13.23 | -0.03072 | Extremely pure mathematical/code punctuation cluster; 88 of 90 tokens are punctuation/symbols. |
| C11 | 79 | 220 / 498 | 11.87 | -0.03251 | Programming/software tooling: `Bitmap`, `Plugin`, `compiler`, `cmd`, `plugins`, `hooks`, `Graphics`; extremes include `uint`, `Pointer`, `sdk`, `api`, `Platform`. |
| C12 | 58 | 151 / 383 | 11.81 | -0.03158 | Multilingual suffixes and orthographic forms; primarily lexical/morphological. |

## Population accounting

### Positive head

Total nodes: **3,125**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 1,423 | 45.5% |
| Formal/name substrate | 1,451 | 46.4% |
| Irreducible semantic | 251 | 8.0% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **3,125** | **100.0%** |

Semantic-eligible denominator: **1,674 nodes**.

### Negative tail

Total nodes: **2,793**

| Disposition class | Nodes | Side share |
|---|---:|---:|
| Retained semantic parents | 536 | 19.2% |
| Formal/name substrate | 1,154 | 41.3% |
| Irreducible semantic | 1,103 | 39.5% |
| Mixed unresolved | 0 | 0.0% |
| Unclear | 0 | 0.0% |
| **Total** | **2,793** | **100.0%** |

Semantic-eligible denominator: **1,639 nodes**.

## Positive-side reconstruction

### P+0 — Information systems and information maintenance

- **Primary children:** C1, C4
- **Primary nodes:** 659
- **Side-relative coverage:** 21.1%
- **Semantic-eligible coverage:** 39.4%
- **Confidence:** High

**Evidence.** C1 provides databases, data formatting and software/interface
systems. C4 provides maintenance, review, access, recognition, documentation,
research and recall operations acting on information. Their State 01
intercommunity relation contains **300 token edges**, mean cosine **0.09551**.

**Exclusion boundary.** C7 contains evaluative/discourse modifiers rather than
information systems or maintenance operations. C11 is numeric form, and C5 is
acronym form despite technical-looking tokens.

**Secondary link:** C7. C4–C7 is especially strong at **277 edges**, mean cosine
**0.09873**, consistent with evaluation modifying review/maintenance activity,
but C7 is too general to make evaluation a primary information-system child.

**Alternative.** Broaden P+0 to `information processing, maintenance and
evaluation` and absorb C7. This is plausible, but rejected because C7's
temporal, degree and discourse-adverbial content extends well beyond
information handling.

### P+1 — Social/institutional organisation and participation

- **Primary children:** C6, C10
- **Primary nodes:** 393
- **Side-relative coverage:** 12.6%
- **Semantic-eligible coverage:** 23.5%
- **Confidence:** Moderate

**Evidence.** C6 organises nationalities, political/administrative descriptors,
bureaucracy and financial/social descriptors. C10 organises people,
workers/adolescents, sport/exercise, programmes, departments and discussions.
C6–C10 has **151 token edges**, mean cosine **0.09306**.

**Exclusion boundary.** C7 describes evaluation/discourse rather than people or
institutions. C9 concerns biological/agricultural life rather than social
organisation.

**Secondary link:** C7. C6–C7 has **146 edges**, mean cosine **0.09968**, so
evaluation/discourse appears locally coupled to social/institutional
description without being reducible to it.

**Alternative.** Treat C6 and C10 as separate irreducible structures. That is
favoured if the underlying C6 population proves primarily nationality/geography
rather than institutional/social organisation.

### P+2 — Biological, health and living systems

- **Primary children:** C8, C9
- **Primary nodes:** 371
- **Side-relative coverage:** 11.9%
- **Semantic-eligible coverage:** 22.2%
- **Confidence:** Moderate

**Evidence.** C8 provides biomedical/endocrine/immune physiology; C9 provides
plants, foods, agricultural life and small animals/life-cycle terms. C8–C9 has
**126 token edges**, mean cosine **0.09056**. The common parent is living and
biological systems rather than one narrow biomedical topic.

**Exclusion boundary.** C10 includes adolescents/exercise but is primarily
human/social/institutional. C6 contains psychological terms but is dominated by
nationality/administrative organisation.

**Alternative.** Keep C8 irreducible biomedical and C9 mixed-unresolved. This
becomes preferable if C9's travel/infrastructure content is found to be
substantial enough to defeat the living-systems interpretation.

### Positive irreducible structure

- **C7 — irreducible-semantic:** evaluative, degree and discourse/adverbial
  language. It has secondary relations to P+0 and P+1 but remains too broadly
  modifier-like to be primarily absorbed into either.

### Positive formal/name substrate

- C0 — grammar/function words and fragments
- C2 — names and multilingual/name fragments
- C3 — punctuation/formatting
- C5 — acronyms/initialisms
- C11 — numeric strings/years

## Negative-side reconstruction

### P-0 — Transformation and interpretive/behavioural constraint

- **Primary children:** C3, C4
- **Primary nodes:** 536
- **Side-relative coverage:** 19.2%
- **Semantic-eligible coverage:** 32.7%
- **Confidence:** High

**Evidence.** C3 contains transformation, inhibition, increase/enhancement and
structural change. C4 contains interpretation, instruction, prohibition,
recommendation, expectations, laws/beliefs and authority. Their direct
intercommunity relation is the strongest semantic pair on the negative side:
**347 token edges**, mean cosine **0.10018**. The parent captures changing a
system/state and constraining or directing allowable state/action.

**Exclusion boundary.** C1 is biomedical/scientific research, not itself a
control/constraint structure. C8 is affective/intensity evaluation rather than
instructional or structural constraint.

**Secondary links:**
- **C1:** C1–C3 has **330 edges** at **0.10007** and C1–C4 **252** at
  **0.10105**. Biomedical/scientific mechanisms are strongly coupled to this
  transformation/constraint structure but are not reducible to it.
- **C8:** C4–C8 has **231 edges** at **0.09997** and C3–C8 **184** at
  **0.09313**. Threat/intensity evaluation is coupled to prohibition/change
  without becoming the same structure.

**Alternative.** Expand P-0 to include C1 under a broader
`system characterisation, transformation and regulation` parent. It is not
preferred because the biomedical/research community has a strong domain identity
that the broader parent would erase.

### Negative irreducible semantic structures

- **C1:** biomedical science, biological research and scientific-method
  terminology; secondary link to P-0.
- **C5:** built environment, equipment, clothing and physical objects.
- **C6:** social/religious/occupational and fictional roles.
- **C8:** affective/threat/intensity evaluation; secondary link to P-0.
- **C11:** programming/software tooling.

### Negative formal/name substrate

- C0 — names/geographic/name fragments
- C2 — incomplete lexical stems
- C7 — suffix/function fragments
- C9 — numbers
- C10 — punctuation/code formatting
- C12 — multilingual morphology

## Community disposition table

| Side | Community | Size | R009 identity | Primary disposition | Secondary links | Reason |
|---|---|---:|---|---|---|---|
| + | C0 | 402 | Grammar/function words/fragments | formal-substrate | — | Formal linguistic organisation. |
| + | C1 | 380 | Databases/software/data systems | parent:P+0 | — | Information-system infrastructure. |
| + | C2 | 370 | Personal names + fragments | formal-substrate | — | Name-form organisation without one domain. |
| + | C3 | 280 | Closing punctuation/formatting | formal-substrate | — | Formatting/tokeniser structure. |
| + | C4 | 279 | Maintenance/review/info handling | parent:P+0 | — | Operations acting on information/system state. |
| + | C5 | 272 | Acronyms/initialisms | formal-substrate | — | Lexical/abbreviation form dominates. |
| + | C6 | 252 | Nationality/governance/social/admin | parent:P+1 | — | Social/institutional organisation. |
| + | C7 | 251 | Evaluative/discourse language | irreducible-semantic | P+0, P+1 | Modifier/evaluation structure overlaps both parents without belonging wholly to either. |
| + | C8 | 191 | Biomedical/endocrine/immune | parent:P+2 | — | Biological/health systems. |
| + | C9 | 180 | Food/plants/animals/agricultural life | parent:P+2 | — | Living/agricultural systems, with acknowledged outliers. |
| + | C10 | 141 | People/sport/institutional activity | parent:P+1 | — | Human/social/institutional participation. |
| + | C11 | 127 | Numeric strings/years | formal-substrate | — | Numeric form. |
| − | C0 | 401 | Names/geographic entities | formal-substrate | — | Name-form organisation. |
| − | C1 | 358 | Biomedical science/research | irreducible-semantic | P-0 | Coherent scientific domain strongly coupled to transformation/constraint. |
| − | C2 | 272 | Incomplete stems/fragments | formal-substrate | — | Lexical morphology. |
| − | C3 | 268 | Transformation/inhibition/change | parent:P-0 | — | System/state transformation. |
| − | C4 | 268 | Interpretation/prohibition/authority | parent:P-0 | — | Instructional/normative constraint. |
| − | C5 | 257 | Built environment/objects/equipment | irreducible-semantic | — | Coherent physical-world domain, no defensible sibling parent. |
| − | C6 | 236 | Social/religious/fictional roles | irreducible-semantic | — | Coherent role-domain island. |
| − | C7 | 229 | Word pieces/suffixes | formal-substrate | — | Morphological form. |
| − | C8 | 173 | Threat/horror/intense evaluation | irreducible-semantic | P-0 | Affective/intensity structure coupled to constraint/change. |
| − | C9 | 104 | Numeric strings | formal-substrate | — | Numeric form. |
| − | C10 | 90 | Code/maths punctuation | formal-substrate | — | Formatting form. |
| − | C11 | 79 | Software/programming tooling | irreducible-semantic | — | Distinct technical domain. |
| − | C12 | 58 | Multilingual suffixes/fragments | formal-substrate | — | Morphological/orthographic form. |

Every State 01 community has exactly one primary disposition.

## Parent coverage table

| Parent | Identity | Children | Nodes | Side-relative | Semantic-eligible | Confidence |
|---|---|---|---:|---:|---:|---|
| P+0 | Information systems and information maintenance | C1, C4 | 659 | 21.1% | 39.4% | High |
| P+1 | Social/institutional organisation and participation | C6, C10 | 393 | 12.6% | 23.5% | Moderate |
| P+2 | Biological, health and living systems | C8, C9 | 371 | 11.9% | 22.2% | Moderate |
| P-0 | Transformation and interpretive/behavioural constraint | C3, C4 | 536 | 19.2% | 32.7% | High |

Positive retained parents account for **1,423 nodes**, **45.5% of the positive
population** and **85.0% of semantic-eligible positive nodes**.

The negative retained parent accounts for **536 nodes**, **19.2% of the
negative population** and **32.7% of semantic-eligible negative nodes**.

## Relations among parents

### Positive-side relations

1. **P+0 ↔ P+1 — information/administration relation — Moderate.**
   Software/information systems and their maintenance sit adjacent to
   institutional/administrative organisation. C1–C6 has 199 edges and C4–C6
   123. The relation is real but does not justify merging the parents.

2. **P+1 ↔ P+2 — human/social relation to biological life — Low to Moderate.**
   C6–C8 has 149 edges, C6–C9 135 and C9–C10 92. These relations support
   contextual coupling but the semantic boundary between social organisation
   and biological/living systems remains meaningful.

3. **C7 is a modifier/evaluation bridge rather than a parent.**
   Its strongest semantic relation is C4–C7 at 277 edges; it also connects to
   C6. The preferred architecture keeps evaluation/discourse as an irreducible
   relational layer rather than creating a broad parent that would absorb
   unrelated domains.

### Negative-side relations

1. **P-0 ↔ C1 — scientific-mechanism relation — Moderate.**
   Biomedical/scientific content is strongly connected to transformation and
   interpretation/constraint, but remains a separate domain.

2. **P-0 ↔ C8 — adverse/normative evaluation relation — Moderate.**
   Threat/intensity vocabulary is strongly connected to prohibition and change,
   but its affective structure remains distinct.

3. **C5 ↔ C6 — human-world context — Low.**
   The two communities have 235 edges at mean cosine 0.09805, but “physical
   environment plus social roles” is too broad to retain as a latent parent.

## Cross-side bridge candidates

**No cross-side parent bridge is retained.**

Potential correspondences exist between:

- positive P+0 and negative C11 through computing/software vocabulary;
- positive P+2 and negative C1 through biomedical/life-science vocabulary;
- positive P+1 and negative C6 through social/institutional roles.

Each candidate has only one retained parent on one side and an irreducible
community on the other. The protocol prohibits creating a parent merely to
manufacture cross-side continuity, so these remain unpromoted correspondences.

## Formal/representational substrate

State 01 contains a large formal/name substrate on both sides.

### Positive — 1,451 nodes / 46.4%

- grammar/function words;
- personal names and multilingual fragments;
- punctuation/formatting;
- acronyms/initialisms;
- numeric strings.

### Negative — 1,154 nodes / 41.3%

- personal names;
- lexical stems;
- suffix/function fragments;
- numeric strings;
- mathematical/code punctuation;
- multilingual morphology.

This substrate is sufficiently large that the state cannot be represented as a
pure semantic ontology.

## Minimal state-level architecture

```text
STATE 01 — BLOCK 0 OUTPUT

POSITIVE-HEAD ORGANISATION
|
+-- P+0 INFORMATION SYSTEMS & MAINTENANCE
|   +-- C1 databases/software/data systems
|   `-- C4 maintenance/review/info-handling actions
|       \
|        -- C7 evaluation/discourse               [secondary relation]
|
+-- P+1 SOCIAL / INSTITUTIONAL ORGANISATION
|   +-- C6 nationality/governance/admin descriptors
|   `-- C10 people/sport/institutional activity
|        \
|         -- C7 evaluation/discourse              [secondary relation]
|
+-- P+2 BIOLOGICAL / HEALTH / LIVING SYSTEMS
|   +-- C8 biomedical/endocrine/immune
|   `-- C9 food/plants/animals/agricultural life
|
+-- C7 evaluative/degree/discourse language         [irreducible]
`-- C0,C2,C3,C5,C11                               [formal/name substrate]


NEGATIVE-TAIL ORGANISATION
|
+-- P-0 TRANSFORMATION & INTERPRETIVE/BEHAVIOURAL CONSTRAINT
|   +-- C3 transformation/inhibition/change
|   `-- C4 interpretation/prohibition/authority
|       |
|       +-- C1 biomedical science/research          [secondary relation]
|       `-- C8 threat/intense evaluation           [secondary relation]
|
+-- C1 biomedical science/research                  [irreducible]
+-- C5 built environment/objects                    [irreducible]
+-- C6 social/religious/fictional roles             [irreducible]
+-- C8 affect/threat/intensity                      [irreducible]
+-- C11 software/programming tools                  [irreducible]
`-- C0,C2,C7,C9,C10,C12                           [formal/name substrate]
```

The smallest defensible State 01 reconstruction therefore contains three
positive multi-community parents but only one negative multi-community parent.
The positive semantic side is highly compressible once formal communities are
removed; the negative semantic side remains substantially more fragmented.

This statement is local to State 01 and is not a comparison with another R010
state.

## Alternative reconstruction

The strongest alternative has two changes:

1. absorb positive C7 into P+0, producing a broader
   **information processing, maintenance and evaluation** parent;
2. absorb negative C1 into P-0, producing a broader
   **scientific system characterisation, transformation and regulation**
   parent.

This alternative improves compression and is supported by strong graph
connectivity.

It is not preferred because both moves erase discriminative semantic
boundaries: C7 contains general temporal/degree/discourse language, and C1 is a
distinct biomedical/scientific domain rather than merely a regulation/change
community.

## Uncertainty record

- **P+1:** C6 is broader than social/institutional organisation because it
  contains nationality, psychology and finance; C10 is also mixed. Parent
  confidence remains Moderate.
- **P+2:** C9 contains genuine travel/infrastructure outliers, so the
  living-systems parent remains Moderate rather than High.
- **C7:** is structurally important but resists primary absorption; its role as
  a cross-parent modifier is the main positive-side ambiguity.
- **Negative C1:** has exceptionally strong graph links to P-0 children but a
  distinct biomedical/scientific identity. It is the main alternative-parent
  boundary.
- **Negative C5/C6:** strong connectivity does not by itself justify the
  vacuous parent “human world”; they remain separate.

## Verification

- Positive communities accounted for: **12 / 12**
- Negative communities accounted for: **13 / 13**
- Total communities accounted for: **25 / 25**
- Positive node accounting: **3,125 / 3,125**
- Negative node accounting: **2,793 / 2,793**
- Duplicate primary dispositions: **0**
- Unassigned communities: **0**
- Retained positive parent IDs: **P+0, P+1, P+2**
- Retained negative parent IDs: **P-0**
- Every retained parent has an exclusion boundary: **yes**
- Every community inspected at underlying R008 community-record level: **yes**
- Cross-state continuity claims: **0**
- SDA-3 role assignments: **0**
- Optimal-layer claims: **0**
- Curvature claims: **0**

## R010 Phase-A boundary

This reconstruction is frozen as an independent State 01 hypothesis. It must
not be retroactively renamed or restructured merely to improve correspondence
with another state.

No persistence, emergence, disappearance, split, merge, polarity change,
optimal-layer, SDA-3 or curvature inference is made here.
