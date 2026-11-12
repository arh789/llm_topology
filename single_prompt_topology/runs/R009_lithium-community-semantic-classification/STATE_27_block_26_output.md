# R009 State 27 — block 26 output

## State identity

- R008 state index: `27`
- R008 state label: `block_26_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 10 | 10 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **22** | **22** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 515 | Characterisation, measurement, quantification, testing and developmental processes | semantic/topic | High | `characterizing`, `Measurements`, `quantification`, `testing`, `recorded`, `acquiring`, `Measurement`, `anticipated`, `characterize`, `develops`, `resolving`, `motivations`; extremes include `stake`, `funding`, `tension`, `debated`, `recall`, `interactions`, `informed`. |
| C1 | 432 | Personal names and geographic/name-like entities | named-entity | Moderate | `Steve`, `Matt`, `Karen`, `Gary`, `Krish`, `Nam`, `Pakistan`, `Bennett`, `Mitchell`, `Scott`; extremes include `Berlin`, `Kumar`, `Krish` and multilingual name-like fragments. `terrorists` is a semantic outlier. |
| C2 | 330 | Film/media, photography, reading and digital-interface/publishing systems | semantic/topic | Moderate | `filmmakers`, `Notification`, `filmmaker`, `Photograph`, `Photo`, `browsers`, `PhysRev`, `Reading`, `Bitmap`, `Address`, `manager`, `photo`; extremes include `Caption`, `Manager`, `Photo`, `markup`, `recorder`, `gradle`, `Stats`. |
| C3 | 321 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, with fragments such as `le`, `ine`, `am`, `l`, `id`, `ling`; extremes include `triangle`, `ilation`, `leq`, `ines`, `choice`, `Sort`. |
| C4 | 303 | Biomedical/pharmacological and infant-health material mixed with food, sleep and regenerative/freshness terms | mixed | Moderate | `breastfeeding`, `Food`, `Baby`, `dopaminergic`, `dexamethasone`, `doxorubicin`, `Sleep`, analgesic fragment, `tumorigenesis`; extremes include `recycled`, `mitotic`, `tornado`, `µm`, `salivary`, `soybean`, `neonates`, `Lung`, `recycling`. |
| C5 | 230 | Entrepreneurship/business and institutional/social activity mixed with healthcare, retail and travel | mixed | Moderate | `entrepreneurs`, `entrepreneur`, `businesses`, `interventions`, hospital fragment, `business`, `Medical`, `shops`, `students`, `fishermen`, `collaborators`; extremes include `hospital`, `students`, `Tours`, `Business`, `bridges`, `nurs`, `healthcare`, `tour`, `budgets`. |
| C6 | 223 | Communication/interview activity mixed with misunderstanding, uncertainty and reappearance/avoidance stems | mixed | Moderate | `misunderstanding`, `inev`, `conversations`, `unve`, `negotiating`, `reappe`, `interviewing`, `discussions`, `interviews`, `puzz`, `fraudulent`, `maneu`; extremes include `interviews`, `Rew`, `undis`, `quest`, `diseng`, `peace`, `cease`. |
| C7 | 208 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 169 of 208 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings. |
| C8 | 200 | Example-related morphology mixed with temporal, evaluative and freshness descriptors | mixed | Moderate | `exempl`, `surprisingly`, `Fresh`, `examples`, `Clearly`, `Example`, `Feb`, `ejemplo`, `elderly`, `Recently`; extremes include `example`, `dating`, `dominant`, `Fast`, `More`, `Spring`. |
| C9 | 132 | Numeric strings and short coded values | numeric | High | Dominated by `297`, `597`, `324`, `325`, `306`, `334`, `300`, `534`, `1989`, `295`, `697`; extremes include `473`, `12345`, `0023`, `624`, `2016`, `2004`, `1301`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 2 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 423 | Personal names and name-like fragments | named-entity | Moderate | `Sarah`, `Laura`, `Martha`, `Connie`, `Emily`, `Ruth` dominate, with short fragments such as `Tah`, `Gh`, `Gu`, `Hu`, `Sty`, `Rh`; extremes include `Violet`, `Maur`, `Chi` and technical fragments. |
| C1 | 417 | Encouragement, prohibition, creation/removal and activation/change actions | semantic/topic | High | `encourages`, `discour`, `prohibiting`, `resembled`, `created`, `creates`, `activates`, `removed`, `participated`, `activate`; extremes include `submit`, `multiplied`, `enactment`, `preceded`, `practicing`, `resigned`. |
| C2 | 364 | Administrative characterisation, downregulation, recommendations and regulatory concepts | semantic/topic | High | `Characteristics`, `downregulation`, `recommendations`, `administrators`, `discriminatory`, `Comprehensive`, `regulations`, `Configuration`, `characteristics`, `administrative`, `beneficiaries`; extremes include `variance`, `Executive`, `Instruction`, `password`, `privileges`, `availability`. |
| C3 | 350 | Vehicles, agriculture, built environment and material/household objects | semantic/topic | Moderate | `trucks`, `automobiles`, `agriculture`, `furniture`, `Mountains`, `pavement`, `chassis`, `cylinder`, `Rails`, `decorations`, `sidewalk`; extremes include `dishes`, `uniforms`, `cassette`, `rails`, `curb`, `Gates`, `roofs`. |
| C4 | 325 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `some`, with fragments `ED`, `M`, `ra`, `ars`, `ao`; multilingual forms include Cyrillic `или`, Arabic fragments, `cette`, `tiene`; extremes remain multilingual and fragmentary. |
| C5 | 270 | Cardiovascular disease, malignancy, cytokine biology and pathology | semantic/topic | High | `cardiovascular`, `atherosclerotic`, `circumferential`, `macrophage`, `cytokine`, `malignancies`, staphylococcus fragment, `lipids`, sclerosis fragment, `epithelium`, `interleukin`; extremes include `monocyte`, `thrombosis`, `physiology`, `algebra` and `uclidean` as outliers. |
| C6 | 233 | Monarchy, religion, political identity and mythic/fantastical roles | mixed | Moderate | `emperor`, `palace`, `warriors`, `USSR`, `church`, `cathedral`, `Africans`, `king`, `kingdom`, `dragon`, `liberals`; extremes include `Beast`, `conspiracy`, `Uncle`, `Stalin`, `Spirit`, `rituals`, `throne`. |
| C7 | 230 | Negative/intense evaluation, frequency and detriment/harm language | semantic/topic | High | `spectacular`, `incredibly`, `incredible`, `stupid`, `Sometimes`, `occasionally`, `unreasonable`, `Specific`, `detrimental`, `unbelievable`, `harmful`; extremes include `uncommon`, `excessive`, `detriment`, `polish`, `heavily`. |
| C8 | 191 | Uppercase lexical stems and technical/code-like abbreviations | lexical/morphological | High | `ERS`, `ALLY`, `CE`, `RA`, `ABLE`, `TC`, `TU`, `AND`, `INE`, `ET`, `TA`; extremes include `CI`, `BLOCK`, `ITS`, `AST`, `ALE`, `PLC`, `IMPLIED`, `IRED`. |
| C9 | 116 | Geographic entities and regions | named-entity | High | `Florida`, `Alabama`, `Northwestern`, `Canada`, `Louisiana`, `Chicago`, `Minnesota`, `Arkansas`, `Mexico`, `Georgia`, `Missouri`; extremes include `Interior`, `Canada`, `Georgia`, `Rouge`, `Illinois`. |
| C10 | 102 | Numeric strings and quantity words | numeric | High | Dominated by `10`, `170`, `25`, `160`, `440`, `20`, `451`, `178`, `056`, `28`, `78`, `214`; extremes include `1919`, `Forty`, `100000`, `666`, `1939`. |
| C11 | 99 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 80 of 99 tokens are punctuation or symbols; examples include closing delimiters, repeated underscores, percent notation and operator-like strings. |

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

- characterisation, measurement, quantification and developmental processes;
- film/media, photography, reading and digital-interface activity;
- biomedical/infant-health material mixed with food, sleep and regeneration;
- entrepreneurship/business/social activity mixed with healthcare and travel;
- communication/interview activity mixed with uncertainty and reappearance stems;
- example-related morphology mixed with temporal/evaluative descriptors;
- names and geography;
- common grammar and lexical fragments;
- formatting;
- numeric strings.

Two of ten communities receive a primary `semantic/topic`
classification. Four are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- names and geographic entities;
- encouragement/prohibition/creation-removal/change actions;
- administrative/downregulation/regulatory concepts;
- vehicles, agriculture and material objects;
- cardiovascular/malignancy/cytokine pathology;
- monarchy/religion/political/mythic roles;
- negative/intense evaluation and detriment;
- grammar/multilingual fragments;
- uppercase technical/code-like fragments;
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

- **positive C1** — names dominate but semantic and multilingual outliers remain;
- **positive C2** — media/publishing semantics overlap with software/interface
  tooling;
- **positive C4** — biomedical/infant-health material overlaps with food, sleep,
  freshness and regenerative terms;
- **positive C5** — entrepreneurship/business overlaps with healthcare, retail
  and travel;
- **positive C6** — communication/interview concepts overlap with uncertainty,
  lexical stems and reappearance language;
- **positive C8** — example morphology overlaps with temporal/evaluative and
  freshness descriptors;
- **negative C0** — names dominate but short technical fragments are substantial;
- **negative C3** — several physical-world object classes share one broad
  partition;
- **negative C5** — biomedical pathology contains a small mathematical outlier
  set;
- **negative C6** — monarchy, religion, political identity and mythic roles
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
