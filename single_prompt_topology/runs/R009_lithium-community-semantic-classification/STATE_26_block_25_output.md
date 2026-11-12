# R009 State 26 — block 25 output

## State identity

- R008 state index: `26`
- R008 state label: `block_25_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 12 | 12 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **24** | **24** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 388 | Entrepreneurship, research and social/business activity mixed with media and healthcare | mixed | Moderate | `entrepreneurs`, `Researchers`, `adventures`, `businesses`, `negotiating`, `conversations`, `entrepreneur`, hospital fragment, `filmmakers`, `happiness`, `justification`, `Training`; extremes include `hospital`, `students`, `funding`, `director`, `battles`. |
| C1 | 353 | Biomedical/pharmacological and infant-health material mixed with food, affect and freshness terms | mixed | Moderate | `Food`, `breastfeeding`, `dopaminergic`, `dexamethasone`, `Fresh`, analgesic fragment, `psychosocial`, `fluorescent`, `rides`, `kissing`, `neonates`, `doxorubicin`; extremes include `recycled`, `tornado`, `µm`, `mitotic`, `salivary`, `soybean`, `Lung`. |
| C2 | 337 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `am`, `id`, with fragments such as `le`, `ine`, `l`, `it`; extremes include `triangle`, `ilation`, `leq`, `ines`, `Sort`, `choice`. |
| C3 | 324 | Personal names and geographic/name-like entities | named-entity | Moderate | `Brian`, `Steve`, `Karen`, `Matt`, `Krish`, `Rick`, `Manchester`, `Gary`, `Mitchell`, `Scott`; extremes include `Berlin`, `Kumar`, `Jake` and name fragments. `Baby` and `terrorists` are semantic outliers. |
| C4 | 306 | Prefix/stem families around inevitability, discrepancy, regeneration and temporal markers | lexical/morphological | Moderate | `inev`, `discrep`, `maneu`, `disproportion`, `Rew`, `Jan`, `Feb`, `puzz`, `regener`, `degener`; extremes include `propri`, `trans`, `wieder`, `attribut`, `anchored` and multilingual fragments. |
| C5 | 273 | Navigation, software/interface systems and dimensional/spatial concepts | semantic/topic | High | `size`, `navigating`, `Bitmap`, `Notification`, `Address`, `Size`, `browsers`, `FB`, `widths`, `Radius`, `score`, `maps`; extremes include `Manager`, `markup`, `gradle`, `javase`, `Stats`, `PBX`, `ajax`. |
| C6 | 254 | Measurement/quantification and interaction mixed with example morphology and theoretical-science concepts | mixed | Moderate | `characterizing`, `quantification`, `Measurements`, `Measurement`, `recorded`, `characterize`, `results`, `quantified`, `gravitational`, `computations`, `interactions` coexist with `exempl`; extremes include `example`, `Geometry`, `measured`, `actions`, `exem`. |
| C7 | 246 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 182 of 246 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings. |
| C8 | 184 | Anticipation, prediction, acquisition and developmental change | semantic/topic | High | `anticipated`, `predicting`, `development`, `acquiring`, `develops`, `Using`, `Development`, `assumed`, `advancing`, with `unve` and `reappe`; extremes include `advance`, `derives`, `informed`, `developments`, `Advance`. |
| C9 | 130 | Numeric strings and short coded values | numeric | High | Dominated by `324`, `325`, `397`, `297`, `697`, `597`, `596`, `300`, `393`, `306`, `334`; extremes include `473`, `12345`, `0023`, `2004`, `499`, `624`, `505`. |
| C10 | 114 | Temporal, evaluative and comparative/descriptive discourse language | semantic/topic | Moderate | `surprisingly`, `Recently`, `Clearly`, `elderly`, `Old`, `Day`, `clinically`, `Similarly`, `clearer`, `suitably`; extremes include `modest`, `obvious`, `Next`, `thicker`, `smallest`, `Previously`. |
| C11 | 96 | Film, photography, reading, writing and publishing/media activity | semantic/topic | High | `Animation`, `filmmaker`, `Reading`, `Photo`, `publishing`, `Photograph`, `Movie`, `Writing`, `Netflix`, video fragment, `episodes`, `facebook`; extremes include `Caption`, `Photo`, `recorder`, `quote`, `animated`, `Bibliography`, `readings`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 639 | Short name-like, technical and code-like fragments | lexical/morphological | Moderate | `discour`, `Gh`, `Rh`, `Tah`, `Rub`, `GH`, `Kh`, `Hu`, `Gu`, `RA`, `Maur`, `Cl`; extremes include `Chi`, `crypt`, `tetra`, `CI`, `ocr`, `heter`, `PROT`. |
| C1 | 518 | Administrative characterisation, recommendations, regulation and constitutional concepts | semantic/topic | High | `Characteristics`, `downregulation`, `recommendations`, `administrators`, `administrative`, `characteristics`, `Constitution`, `encouragement`, `beneficiaries`, `bureaucracy`, `regulations`; extremes include `variance`, `conspiracy`, `enactment`, `Executive`, `detriment`. |
| C2 | 337 | Encouragement, prohibition, removal, activation and suppression/change actions | semantic/topic | High | `encourages`, `resembled`, `prohibiting`, `removed`, `activates`, `prohibited`, `created`, `creates`, `received`, `suppresses`, `regulate`; extremes include `submit`, `preceded`, `resigned`, `stable`, `insult`. |
| C3 | 264 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `e`, `I`, `or`, `said`, with fragments `ized`, `ED`, `ra`, `M`, numerals and `cette`; extremes include `или`, `Une`, Cyrillic and other multilingual fragments. |
| C4 | 262 | Monarchy, religion, family and political/mythic roles | mixed | Moderate | `emperor`, `Sultan`, `palace`, `king`, `warriors`, `believers`, `cathedral`, `USSR`, `church`, `Muslims`, `grandmother`, `liberals`; extremes include `Beast`, `Uncle`, `rituals`, `Spirit`, `Africans`, `Stalin`. |
| C5 | 257 | Vehicles, transport, built environment and physical/material objects | semantic/topic | Moderate | `trucks`, `automobiles`, `Rails`, `cylinder`, `furniture`, `pavement`, `decorative`, `chassis`, `extremities`, `roads`, `vegetables`, `boats`; extremes include `cassette`, `dishes`, `curb`, `rails`, `roofs`, `limbs`, `Gates`. |
| C6 | 252 | Personal names mixed with geographic entities and regions | named-entity | High | `Florida`, `Laura`, `Alabama`, `Sarah`, `Louisiana`, `Northwestern`, `Minnesota`, `Emily`, `Americans`, `Georgia`, `Arkansas`; extremes include `Violet`, `Interior`, `Canada`, `Friedrich`, `Ivy`. |
| C7 | 215 | Cardiovascular disease, vascular biology, cytokines and pathology | semantic/topic | High | `cardiovascular`, `macrophage`, `cytokine`, `atherosclerotic`, `cytokines`, staphylococcus fragment, `endothelium`, thrombus fragment, `interleukin`, `antioxidants`, `epithelium`, `lipids`; extremes include `monocyte`, `physiology`, `thrombosis`, `oxides`. |
| C8 | 196 | Qualification/frequency language mixed with uppercase lexical and code/status fragments | mixed | Moderate | `Specific`, `occasionally`, `Sometimes`, `generally`, `particularly`, `successively`, `Continuous` coexist with `ABLE`, `ERS`, `NEVER`, `AND`; extremes include `BLOCK`, `ITS`, `FORE`, `AST`, `IMPLIED`, `Const`, `codes`, `ALE`. |
| C9 | 170 | Negative/intense evaluation, alarm and threat | semantic/topic | High | `ridiculous`, `incredible`, `spectacular`, `unreasonable`, `unbelievable`, `stupid`, `disastrous`, `glorious`, `frightening`, `alarming`, `sinister`; extremes include `excessive`, `harsh`, `shattered`, `supreme`, `Ultra`. |
| C10 | 110 | Numeric strings, especially historical years and quantity words | numeric | High | Dominated by `170`, `20`, `160`, `140`, `440`, `451`, `1920`, `178`, `hundred`, `209`, `214`, `1921`; extremes include `1919`, `Forty`, `1939`, `666`, `100000`, `980`. |
| C11 | 93 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 80 of 93 tokens are punctuation or symbols; examples include closing delimiters, percent notation, repeated underscores and operator-like strings. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- entrepreneurship/research/social-business activity mixed with media and healthcare;
- biomedical/pharmacological/infant-health material mixed with food, affect and freshness;
- navigation/software-interface and dimensional concepts;
- measurement/quantification mixed with example morphology and theoretical science;
- anticipation/prediction/developmental change;
- temporal/evaluative/comparative descriptors;
- film/photography/reading/writing/publishing;
- names and geography;
- grammar and lexical fragments;
- regeneration/discrepancy stem families;
- formatting;
- numeric strings.

Four of twelve communities receive a primary `semantic/topic`
classification. Three are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative/regulatory/constitutional concepts;
- encouragement/prohibition/removal/suppression actions;
- monarchy/religion/family/political roles;
- vehicles, transport and material objects;
- cardiovascular/vascular/cytokine pathology;
- negative/intense evaluation;
- names and geographic regions;
- grammatical and short technical lexical fragments;
- qualification/frequency mixed with code/status fragments;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — entrepreneurship/research/social activity overlaps with
  healthcare and media;
- **positive C1** — biomedical/pharmacological terms overlap with food, affect,
  freshness and physical-process material;
- **positive C3** — names dominate but semantic outliers remain;
- **positive C4** — semantic stem families are visible, but incomplete word form
  is the stronger organising feature;
- **positive C6** — measurement/quantification overlaps with example morphology
  and theoretical-science terms;
- **negative C0** — short name-like, technical and code fragments are interleaved;
- **negative C4** — monarchy, religion, family and political/mythic roles coexist;
- **negative C5** — several physical-world object classes share one broad
  partition;
- **negative C6** — personal names and geographic entities are both substantial;
- **negative C8** — qualification/frequency language overlaps with uppercase
  lexical and code/status fragments.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
