# R009 State 17 — block 16 output

## State identity

- R008 state index: `17`
- R008 state label: `block_16_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 13 | 13 | reconciled |
| negative_tail | 10 | 10 | reconciled |
| **Total** | **23** | **23** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 350 | Anticipation, development, observation, outcomes and motivation | semantic/topic | High | `anticipated`, `Measurements`, `anticipation`, `development`, `evolving`, `recorded`, `happiness`, `observed`, `yields`, `ignored`, `motivation`, `develops`; extremes include `informed`, `recall`, `debated`, `derives`, `bridging`. |
| C1 | 315 | Exploration, inevitability/re-emergence and evaluative change | semantic/topic | Moderate | `exploring`, inevitability/unavoidability fragments, `discuss`, `resolving`, `Emer`, `explores`, `Fresh`, `reappe`, `controvers`; extremes include `travers`, `beaut`, `trans`, `estim` and `sal`. |
| C2 | 287 | Transformation, interaction, coupling and analytical/relational structure | semantic/topic | High | `transformations`, `determinations`, `interactions`, `characterizing`, `values`, `coupling`, `partnerships`, `results`, `perturbative`, `interacting`, `interventions`; extremes include `interaction`, `tension`, `Manager`, `Query`. |
| C3 | 280 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `am`, with suffixes/fragments such as `ation`, `ating`, `le`, `ine`, `it`, `l`, `id`; extremes include `ausing`, `ilation`, `ines`, `ivated`. |
| C4 | 280 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 180 of 280 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `Caption`, `javase`, `mathchoice`, `INTRODUCTION`. |
| C5 | 248 | Business/social activity mixed with food, health, media and institutional terms | mixed | Moderate | `entrepreneurs`, `Food`, `breastfeeding`, `conversations`, `businesses`, `adventures`, `negotiating`, `filmmakers`, `sleeping`, `terrorists`, `Medical`; extremes include `students`, `resorts`, `interviewing`, `neonates`, `Tours`, `funding`. |
| C6 | 224 | Cities, regions and personal/geographic names | named-entity | High | `Manchester`, `Matt`, `Bristol`, `Kashmir`, `Hamburg`, Switzerland fragment, `Stockholm`, Pakistan fragment, `Jay`, `Karen`, `Krish`; extremes include `Berlin`, `Kumar`, `Gary`, `Karn`. |
| C7 | 218 | Biomedical imaging, psychiatry, respiratory medicine and pharmacology | semantic/topic | High | `dexamethasone`, `psychiat`, `imaging`, `analgesic`, `pulmonary`, `pneum`, `ventilation`, `dopaminergic`, `designing`, `scanned`, `analges`; extremes include `airborne`, `fluores`, `µm`, `sensing`, `mitotic`, `Lung`. |
| C8 | 176 | Discourse, sequencing, evaluation and contextual modifiers | semantic/topic | Moderate | `Next`, `surprisingly`, `Using`, `More`, `Having`, `Clearly`, `Wednesday`, `Estim`, `With`, `interesting`, `illuminating`; extremes include `dominant`, `busy`, `Coming`, `Spring`, `Day`. |
| C9 | 148 | Example-related multilingual words and orthographic/tokenisation fragments | lexical/morphological | High | `exempl`, `ejemplo`, `Example`, `exem`, `Examples` mixed with replacement characters and multilingual fragments; extremes include `example`, `emplo`, `wij`, `ün`, `界`, Cyrillic and Hebrew forms. |
| C10 | 122 | Numeric strings and short coded values | numeric | High | Dominated by `324`, `306`, `297`, `325`, `334`, `304`, `296`, `597`, `697`, `97`, `305`, `587`; extremes include `505`, `499`, `508`, `633`, `12345`, `0023`. |
| C11 | 56 | Short technical/scientific abbreviations and measurement/medical codes | lexical/morphological | Moderate | `NI`, `PK`, `fp`, `NE`, `DB`, `RI`, `dp`, `ROI`, `BW`, `EE`, `EP`; extremes include `DX`, `BA`, `BMD`, `CRM`, `Kin`, alongside `sedentary`. |
| C12 | 29 | Learning, reading, writing and play | semantic/topic | High | `Learning`, `Read`, `plays`, `Play`, `games`, `Writing`, `readings`, `Reading`, `playful`, `learning`; extremes remain centred on reading, writing and play. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 522 | Regulation, adverse evaluation, recommendation and constraint language | semantic/topic | High | `circumstantial`, `disproportionate`, `unconstitutional`, `recommendations`, `encouragement`, `downregulation`, `discriminatory`, `unbelievable`, `prohibiting`, `incredible`, `Specific`; extremes include `harsh`, `affirmative`, `enactment`, `disadvantages`, `excessive`, `submit`, `supreme`. |
| C1 | 475 | Personal names mixed with lexical/technical fragments | named-entity | Moderate | `Caroline`, `Laura`, `Connie`, `Sarah`, `Claire`, `Emily`, `Maur` coexist with fragments such as `Gh`, `Tob`, `Tah`, `crypt`, `ocr`, `heter`, `ocy`, `Comp`. |
| C2 | 380 | Administrative/configuration concepts mixed with family/social-role vocabulary | mixed | Moderate | `Characteristics`, `Configuration`, `administrators`, `representation`, `administrator`, `regulations`, `distribution`, `characteristics` coexist with `mother`, `grandmother`; extremes include `Uncle`, `individual`, `specificity`, `variance`, `Executive`. |
| C3 | 346 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `different`, `WHAT`, `THIS`, `some`, `two`, with fragments `ED`, `ra`, short numerals and multilingual forms such as `cette`, `Une`, Cyrillic fragments. |
| C4 | 342 | Cardiovascular disease, cytokine biology, immunology and pathology | semantic/topic | High | `cardiovascular`, `atherosclerotic`, `cytokines`, `cytokine`, `macrophage`, sclerosis fragment, `monocyte`, `IGF`, `epidemiological`, staphylococcus fragment, `phenotype`; extremes include `physiology`, `gluc`, `algebra`, `ideals` as outliers. |
| C5 | 290 | Monarchy, government, geography and mythic/conflict roles | mixed | Moderate | `palace`, `emperor`, `Alabama`, `king`, `Constitution`, `empire`, `dragon`, `Chicago`, `queen`, `warriors`, `goddess`; extremes include `Beast`, `conspiracy`, `Interior`, `Illinois`, `Africans`. |
| C6 | 274 | Vehicles/material objects mixed with anatomy, weapons and distress terms | mixed | Moderate | `automobiles`, `trucks`, `circumferential`, `vegetables`, `gravel`, `pavement`, `extremities`, `furniture`, `firearms`, `screamed`, `chassis`, `disgrace`; extremes include `curb`, `cassette`, `barrel`, `dishes`, `roofs`, `cloth`. |
| C7 | 129 | Technical/infrastructure abbreviations mixed with Soviet/political entities | mixed | Moderate | `TC`, `TG`, `GGT`, `Rails`, `ACC`, `SSH`, `IG`, `EC`, `CCT` coexist with `USSR`; extremes include `LCD`, `CPU`, `PLC`, `Putin`, `Stalin`, `rails`. |
| C8 | 113 | Numeric strings, especially historical years | numeric | High | Dominated by `272`, `451`, `1921`, `651`, `1860`, `448`, `1920`, `1910`, `441`, `856`; extremes include `1890`, `1919`, `1866`, `666`, `Years`. |
| C9 | 67 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 52 of 67 tokens are punctuation or symbols; examples include closing delimiters, percent notation, repeated punctuation, underscores and operator-like strings. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 2 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- anticipation/development/observation and motivation;
- exploration and re-emergence/evaluative change;
- transformations, interactions and coupling;
- biomedical imaging, psychiatry and respiratory medicine;
- discourse/sequencing and contextual modifiers;
- learning/reading/writing/play;
- business/social activity mixed with food, health and media;
- names and geography;
- grammar and lexical fragments;
- multilingual example-related forms;
- technical abbreviations;
- formatting;
- numeric strings.

Six of thirteen communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- regulation/adverse evaluation and constraint;
- cardiovascular/cytokine/immunological pathology;
- administrative/configuration concepts mixed with family roles;
- monarchy/government/geography/mythic material;
- vehicles/material objects mixed with anatomy/weapons/distress;
- technical/infrastructure abbreviations mixed with Soviet/political entities;
- names;
- grammar/multilingual lexical fragments;
- formatting;
- numeric strings.

Two of ten communities receive a primary `semantic/topic`
classification. Four are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — exploration, inevitability/re-emergence and evaluative
  change share a broad partition;
- **positive C2** — analytical/physical interaction language overlaps with
  organisational terms;
- **positive C5** — business/social activity, food, health and media terms
  coexist;
- **positive C8** — discourse/sequencing and evaluative/contextual language
  overlap;
- **positive C11** — short technical forms dominate, but measurement and
  medical-code semantics are also visible;
- **negative C1** — names dominate but technical/lexical fragments remain
  substantial;
- **negative C2** — administrative/configuration vocabulary overlaps with
  family/social-role terms;
- **negative C5** — monarchy, government, geography and mythic/conflict roles
  coexist;
- **negative C6** — several physical-world, anatomical and violent/distress
  domains share a community;
- **negative C7** — technical/infrastructure abbreviations coexist with
  Soviet/political entities.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
