# R009 State 15 — block 14 output

## State identity

- R008 state index: `15`
- R008 state label: `block_14_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 9 | 9 | reconciled |
| negative_tail | 13 | 13 | reconciled |
| **Total** | **22** | **22** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 387 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `back`, `making`, `right`, `used`, with suffixes/fragments such as `ation`, `le`, `ide`, `ling`, `ne`; extremes include `ausing`, `pages`, `systems`, `ines`, `Working`, `met`. |
| C1 | 331 | Personal names, cities and national/geographic fragments | named-entity | Moderate | `Berlin`, `Manchester`, `Mitchell`, `Karen`, `Mumbai`, `Hamburg`, `Amsterdam`, with `Bav` and `Portug` geographic fragments; extremes include `Berlin`, `Krish` and other name-like fragments. |
| C2 | 324 | Mathematical/code punctuation and software-formatting strings | formatting/tokenizer | High | 187 of 324 tokens are punctuation or symbols; representatives are dominated by brace/operator strings and LaTeX-like fragments, with extremes including `sizeof`, `mathchoice` and `javase`. |
| C3 | 317 | Example-related, memory/process and multilingual lexical fragments | lexical/morphological | Moderate | `remem`, `exempl`, `exem`, `ejemplo`, `fres`, `reappe`, `negot`, `instit`; extremes include `example`, `emplo`, `prem`, `trans`, `beaut` and multilingual fragments. |
| C4 | 300 | Exploration, development, memory and motivational/process actions | semantic/topic | High | `exploring`, `characterizing`, `evolving`, `remembering`, `motivations`, `discuss`, `developments`, `retrieved`, `withdrawing`, `happiness`, `develops`, `advancing`; extremes include `informed`, `recall`, `busy`. |
| C5 | 295 | Biomedical/respiratory terminology mixed with affective and bodily-action language | mixed | Moderate | `dexamethasone`, `breastfeeding`, `pulmonary`, `ventilation`, `psychiat`, `pores`, diazepam fragment coexist with `happier`, `kissing`, `Hit`; extremes include `airborne`, `µm`, `psychosocial`, `kissed`, `dating`, `sprang`. |
| C6 | 243 | Communication, interaction, research and analytical/measurement activity | semantic/topic | Moderate | `conversations`, `interactions`, `resolving`, `discussions`, `adventures`, `negotiating`, `management`, `computed`, `Measurements`, `observed`, `interventions`, `perturbative`; extremes include `interacting`, `renormalization`, `bridging`, `talks`, `recorder`. |
| C7 | 144 | Food, business, shopping, healthcare, housing and online-platform terms | mixed | Moderate | `Food`, `business`, `workshops`, `shoppers`, `hospital`, `healthcare`, `shopping`, `hospitals`, `apartments`, `Sleep`, `facebook`; extremes include `resorts`, `Business`, `uploads`, `mars`. |
| C8 | 128 | Numeric strings and short coded values | numeric | High | Dominated by `597`, `624`, `324`, `334`, `397`, `325`, `1986`, `295`, `306`, `603`, `697`; extremes include `505`, `499`, `633` and short codes such as `BA`, `PORT`, `NE`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 2 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 430 | Scientific/administrative characterisation, distributions and recommendations | semantic/topic | Moderate | `Characteristics`, `downregulation`, `recommendations`, `encouragement`, `distributions`, `administrator`, `representation`, `algorithms`, `administrators`, `distribution`; extremes include `variance`, `specificity`, `enactment`, `codes`, `Executive`, `algebra`. |
| C1 | 376 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `they`, `say`, `THIS`, `WHAT`, with fragments `ized`, `ED`, `ian`, `ra`, `ta`, `ao`; extremes include `cette`, Cyrillic/Thai fragments and `HOW`. |
| C2 | 342 | Personal names mixed with biomedical/technical fragments | named-entity | Moderate | `Caroline`, `Jess`, `Claude`, `Claud`, `Connie`, `Betty` coexist with fragments such as `fluor`, `olith`, `ocr`, `ocy`, `phan`; extremes include `Violet`, `Maur`, `Chi`. |
| C3 | 304 | Catastrophe, discrimination, prohibition and intense evaluation | semantic/topic | High | `circumstantial`, `unconstitutional`, `discriminatory`, `unbelievable`, `disastrous`, `prohibiting`, `incredible`, `catastrophe`, `disproportionate`, `jurisdictional`, `catast`; extremes include `harsh`, `heavily`, `supreme`, `intense`, `Clause`. |
| C4 | 261 | Monarchy, religion, family and mythic/fantastical roles | mixed | Moderate | `emperor`, `Constitution`, `palace`, `queen`, `cathedral`, `church`, `Empire`, `Sultan`, `mother`, `grandmother`; extremes include `Uncle`, `Universe`, `Beast`, `Guardian`, `wedding`, `heavens`. |
| C5 | 217 | Cardiovascular disease, immunology and biomedical pathology | semantic/topic | High | `atherosclerotic`, `cardiovascular`, `epidemiological`, `macrophage`, `dysfunction`, `interleukin`, cytokine fragment, immunofluorescence fragment, `monocyte`, `erythrocytes`; extremes include `physiology`, `epithelial`, `derm`, `cranial`. |
| C6 | 187 | Short technical/computing abbreviations and code-like fragments | lexical/morphological | Moderate | Dominated by `TG`, `GGT`, `ACC`, `UU`, `CE`, `RF`, `COMP`, `LG`, `comp`; extremes include `crypt`, `CI`, `SSH`, `glyph`, `PROT`, `LCD`, `CPU`. |
| C7 | 163 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `circumferential`, `uniforms`, `trucks`, `chassis`, `bulbs`, `automobiles`, `sidewalk`, `gravel`, `Rails`, `roadway`, `roads`; extremes include `curb`, `barrel`, `cylinder`, `roofs`, `ignition`, `cloth`, `quilt`. |
| C8 | 139 | Exclusion, deletion, creation and transformation/change actions | semantic/topic | High | `enhances`, `excluding`, `exclude`, `Delete`, `emphasizes`, `created`, `eliminated`, `activate`, `distorted`, `toward`, `creates`, `Remove`; extremes include `composed`, `Creator`, `elevate`, `resembled`, `preceded`, `delet`. |
| C9 | 105 | Numeric strings, especially historical years | numeric | High | Dominated by `1890`, `1860`, `1867`, `1880`, `1921`, `1870` and shorter values; extremes include `980`, `1866`, `001`, `082`, `Stalin`. |
| C10 | 76 | Vocal distress, facial/body actions and anatomy | semantic/topic | High | `screamed`, `extremities`, `glance`, `shouts`, `glances`, `forehead`, `glare`, `scream`, `glared`, `shoulders`, `limbs`; extremes include `choked`, `Face`, `loudly`, `yelling`. |
| C11 | 53 | Geographic entities and regions | named-entity | High | `Alabama`, `Georgia`, `Iowa`, `Arkansas`, `Kerala`, `Florida`, `Minnesota`, `Illinois`, `Nebraska`, `Argentina`; extremes include `Canada`, `Montreal`, `Adelaide`. |
| C12 | 36 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 35 of 36 tokens are punctuation or symbols; examples include closing delimiters, percent notation, repeated exclamation/question marks, ellipses and operator strings. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 2 |
| named-entity | 2 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- exploration/development/memory and motivational process language;
- communication, interaction and analytical activity;
- biomedical/respiratory language mixed with affective/bodily terms;
- food/business/shopping/healthcare/housing/platform material;
- names and geography;
- grammar and lexical fragments;
- multilingual/example-related fragments;
- formatting;
- numeric strings.

Two of nine communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- scientific/administrative characterisation and distributions;
- catastrophe/discrimination/prohibition;
- cardiovascular/immunological pathology;
- vehicles, roads and physical/material objects;
- exclusion/deletion/creation actions;
- vocal/body-action and anatomy language;
- names and geographic regions;
- monarchy/religion/family/mythic roles;
- grammar and technical lexical fragments;
- formatting;
- numeric strings.

Six of thirteen communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, two named-entity, one mixed,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — name/geographic identity is strong but short fragments are
  substantial;
- **positive C3** — memory/process and example-related multilingual fragments
  coexist;
- **positive C5** — biomedical/respiratory and affective/bodily-action terms
  coexist;
- **positive C6** — communication/interaction and analytical/physical terms
  overlap;
- **positive C7** — food, commerce, healthcare, housing and online-platform
  concepts form a broad mixed partition;
- **negative C0** — scientific, administrative and regulatory/distribution
  language overlap;
- **negative C2** — personal names coexist with biomedical/technical fragments;
- **negative C4** — monarchy, religion, family and mythic roles coexist;
- **negative C6** — technical semantics are evident but abbreviated form is
  the dominant organising feature;
- **negative C7** — multiple physical-world object classes share one broad
  partition.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
