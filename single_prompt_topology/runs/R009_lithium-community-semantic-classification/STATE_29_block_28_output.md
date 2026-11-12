# R009 State 29 — block 28 output

## State identity

- R008 state index: `29`
- R008 state label: `block_28_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 9 | 9 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **21** | **21** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 486 | Quantification, measurement, characterisation and developmental/interpretive processes | semantic/topic | High | `quantification`, `conversations`, `characterizing`, `Measurements`, `Measurement`, `testing`, `recorded`, `evolves`, `development`, `results`, `characterizes`, `Interpret`; extremes include `motivations`, `tension`, `debated`, `advance`, `measured`, `recorder`, `example`. |
| C1 | 464 | Personal names and geographic/name-like entities | named-entity | High | `Brian`, `Steve`, `Karen`, `Matt`, `Jay`, `Peter`, `Mumbai`, `Scott`, `Bennett`, `Richard`, `Thomas`; extremes include `Kumar`, `Krish`, `Berlin` and name-like multilingual fragments. |
| C2 | 428 | Biomedical/pharmacological and theoretical-system concepts mixed with uncertainty/anticipation stems | mixed | Moderate | `misunderstanding`, `inev`, `unpredict`, `immunostaining`, `analges`, `antidepress`, `dopaminergic`, `renormalization`, `phenomenological`, `dexamethasone`, `anticip`; extremes include `salivary`, `mitotic`, `tornado`, `estim`, `unpack`, `anchored`, `Lung`. |
| C3 | 426 | Entrepreneurship/business activity mixed with media, healthcare and organisational terms | mixed | Moderate | `entrepreneurs`, `Food`, `business`, `businesses`, `interventions`, `filmmakers`, `entrepreneur`, `constructions`, hospital fragment, `adventures`, `Photo`, `organisations`; extremes include `hospital`, `Caption`, `students`, `Business`, `Photo`, `funding`. |
| C4 | 392 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `all`, `into`, with suffixes/fragments such as `ation`, `ating`, `le`, `ine`, `am`; extremes include `ilation`, `ines`, `choice`, `ivated`, `med`. |
| C5 | 258 | Infant/age and freshness concepts mixed with evaluative, comparative and emergence language | mixed | Moderate | `breastfeeding`, `Baby`, `baby`, `neonates`, `boy`, `newborns` coexist with `suitably`, `less`, `surprisingly`, `Fresh`, `last`, `emerging`; extremes include `refres`, `Fast`, `More`, `dominant`. |
| C6 | 257 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 177 of 257 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings. |
| C7 | 246 | Software/interface, browser and dimensional/layout concepts | semantic/topic | High | `Length`, `Bitmap`, `Notification`, `manager`, `browsers`, `buffer`, `Position`, `managers`, `Size`, `dialog`; extremes include `sizeof`, `Manager`, `markup`, `DATA`, `ajax`, `EXPORT`, `gradle`, `IE`, `mem`. |
| C8 | 148 | Numeric strings and short coded values | numeric | High | Dominated by `334`, `345`, `325`, `265`, `295`, `1986`, `324`, `326`, `297`, `305`, `306`; extremes include `473`, `12345`, `0023`, `2004`, `2016`, `508`, `633`, `505`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 2 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 545 | Personal names and name-like fragments | named-entity | Moderate | `Sarah`, `Emily`, `Michelle`, `Martha`, `Laura` dominate alongside short forms such as `Gu`, `Tah`, `Gh`, `Rh`; extremes include `Violet`, `Maur`, `Chi`, with technical fragments such as `COMP`. |
| C1 | 535 | Administrative characterisation, regulation, up/down-regulation and consequence concepts | semantic/topic | High | `Characteristics`, `downregulation`, `recommendations`, `differences`, `consequences`, `regulations`, `upregulation`, `characteristics`, `Constitution`, `administrators`, `representation`; extremes include `variance`, `password`, `Instruction`, `resigned`. |
| C2 | 484 | Negative/intense evaluation, prohibition and adverse-change language | semantic/topic | High | `ridiculous`, `disastrous`, `incredible`, `discour`, `prohibiting`, `Sometimes`, `incredibly`, `spectacular`, `detrimental`, `resembled`; extremes include `submit`, `practicing`, `detriment`, `disappearing`, `harsh`, `excessive`. |
| C3 | 297 | Vehicles, agriculture, vegetation and built/material objects | semantic/topic | Moderate | `automobiles`, `trucks`, `cylinder`, `Mountains`, `vegetables`, `agriculture`, `vegetation`, `Rails`, `pavement`, `extremities`, `walls`; extremes include `dishes`, `rails`, `curb`, `cassette`, `shores`, `limbs`, `Gates`. |
| C4 | 224 | Cardiovascular disease, malignancy, cytokine biology and pathology | semantic/topic | High | `cardiovascular`, `atherosclerotic`, `macrophage`, `malignancies`, `cytokine`, `gluc`, `antioxidants`, `circumferential`, sclerosis fragment, staphylococcus fragment, `dysfunction`, corticosteroid fragment; extremes include `monocyte`, `thrombosis`, `physiology`, `cranial`. |
| C5 | 223 | Monarchy, religion, empire and mythic/political roles | mixed | Moderate | `dragon`, `emperor`, `palace`, `empire`, `church`, `kingdom`, `warriors`, `cathedral`, `Greeks`, `king`, `Queen`, `chapel`; extremes include `Beast`, `rituals`, `USSR`, `conspiracy`, `Spirit`, `Stalin`, `altar`, `throne`. |
| C6 | 220 | Multilingual words and orthographic fragments mixed with modal/status tokens | lexical/morphological | High | `cette`, Cyrillic `или`, Arabic fragments, `NEVER`, `questa`, `doesnt`, `votre`, `THIS`, Greek `την`, `tiene`; extremes include `Une`, `tho`, `FORE`, `ITS` and multilingual script fragments. |
| C7 | 109 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 89 of 109 tokens are punctuation or symbols; representatives and extremes are dominated by brackets, delimiters, repeated underscores, percent notation and operator-like strings. |
| C8 | 108 | Uppercase technical and lexical abbreviations | lexical/morphological | High | `ED`, `TC`, `RA`, `ERS`, `ET`, `TG`, `CE`, `INE`, `ABLE`, `TA`, `EC`; extremes include `CI`, `PLC`, `IRED`, `ALE`, `PROT`, `LLY`, `AST`, `COR`. |
| C9 | 86 | Geographic entities and regions | named-entity | High | `Alabama`, `Louisiana`, `Florida`, `Minnesota`, `Canada`, `Northwestern`, `Missouri`, `Arkansas`, `Chicago`, `Memphis`, `Mexico`; extremes include `Georgia`, `Orleans`, `Rouge`, `Yankees`. |
| C10 | 74 | Numeric strings and quantity words | numeric | High | Dominated by `25`, `178`, `059`, `28`, `018`, `056`, `061`, `hundred`, `448`, `680`, `sevent`, `170`; extremes include `1919`, `1939`, `40`, `666`, `sixty`, `601`, `980`. |
| C11 | 13 | Unix, Git and command-line/developer tooling | semantic/topic | High | Entire small community is coherent around `SSH`, `CLI`, `repo`, `command`, `sudo`, `Git`, `Unix`, `RPC`, `git`, `syscall`; extremes reproduce the same tooling set. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 2 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- quantification, measurement, characterisation and developmental/interpretive processes;
- software/interface/browser and dimensional concepts;
- biomedical/pharmacological and theoretical-system material mixed with uncertainty stems;
- entrepreneurship/business activity mixed with media and healthcare;
- infant/age and freshness concepts mixed with evaluation and emergence;
- names and geography;
- grammar and lexical fragments;
- formatting;
- numeric strings.

Two of nine communities receive a primary `semantic/topic`
classification. Three are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative regulation and up/down-regulation;
- negative/intense evaluation and prohibition;
- vehicles, agriculture and material objects;
- cardiovascular/malignancy/cytokine pathology;
- monarchy/religion/empire/mythic roles;
- names and geographic entities;
- multilingual and uppercase technical lexical fragments;
- Unix/Git/command-line tooling;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, two named-entity, one mixed,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C2** — biomedical/pharmacological and theoretical-system concepts
  overlap with uncertainty and anticipation stems;
- **positive C3** — entrepreneurship/business overlaps with media, healthcare
  and organisational concepts;
- **positive C5** — infant/age and freshness concepts overlap with evaluative,
  comparative and emergence language;
- **negative C0** — personal names dominate but short technical fragments remain;
- **negative C3** — several physical-world and biological object classes share
  one broad partition;
- **negative C5** — monarchy, religion, empire and mythic/political roles coexist;
- **negative C6** — multilingual morphology overlaps with modal/status tokens.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
