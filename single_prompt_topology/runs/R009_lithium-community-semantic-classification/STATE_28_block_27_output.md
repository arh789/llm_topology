# R009 State 28 — block 27 output

## State identity

- R008 state index: `28`
- R008 state label: `block_27_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 11 | 11 | reconciled |
| negative_tail | 10 | 10 | reconciled |
| **Total** | **21** | **21** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 471 | Characterisation, quantification, testing and developmental/analytical processes | semantic/topic | High | `misunderstanding`, `characterizing`, `quantification`, `Measurements`, `testing`, `characterize`, `justification`, `recorded`, `results`, `develops`, `acquiring`, `motivations`; extremes include `stake`, `debated`, `tension`, `advance`, `informed`, `recall`, `anchored`. |
| C1 | 464 | Personal names and geographic/name-like entities | named-entity | Moderate | `Matt`, `Steve`, `Brian`, `Karen`, `Scott`, `Peter`, `Bennett`, `Gary`, `Mumbai`, `Derek`; extremes include `Berlin`, `Kumar`, `Krish` and multilingual name-like fragments. `terrorists` is a semantic outlier. |
| C2 | 325 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `all`, `into`, with fragments such as `ation`, `le`, `ine`, `l`, `am`, `id`; extremes include `ilation`, `ines`, `leq`, `choice`, `Good`, `More`. |
| C3 | 292 | Entrepreneurship/business and social activity mixed with media and healthcare | mixed | Moderate | `entrepreneurs`, `conversations`, `interventions`, `entrepreneur`, `negotiating`, `businesses`, `adventures`, `filmmaker`, hospital fragment, `filmmakers`, `business`, `businessman`; extremes include `hospital`, `students`, `Caption`, `Photo`, `funding`, `Business`, `interviews`. |
| C4 | 288 | Biomedical/pharmacological and infant-health material mixed with freshness/regenerative terms | mixed | Moderate | `breastfeeding`, `Baby`, `neonates`, `dexamethasone`, `Medical`, analgesic fragment, `Fresh`, `dopaminergic`, pulmonary fragments, `salivary`; extremes include `recycled`, `refres`, `mitotic`, `tornado`, `µm`, `fluores`, `neonates`. |
| C5 | 263 | Navigation, search, software/interface and dimensional/imaging concepts | semantic/topic | High | `navigating`, `size`, `Notification`, `Search`, `browsers`, `widths`, `Bitmap`, `imaging`, `Length`, `DB`, `RGB`, `spacing`; extremes include `sizeof`, `pages`, `markup`, `ajax`, `gradle`, `stdio`, `DATA`, `Flow`. |
| C6 | 226 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 157 of 226 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings. |
| C7 | 136 | Food, sleep, affect and recreational/leisure activity | semantic/topic | Moderate | `Food`, `Sleep`, `Draw`, `discomfort`, `camping`, `kissing`, `fishermen`, `consciousness`, `fishing`, `compassion`, `tours`; extremes include `patience`, `smiled`, `Tours`, `tour`, `inclination`, `frowned`, `lunch`. |
| C8 | 119 | Numeric strings and short coded values | numeric | High | Dominated by `300`, `297`, `325`, `597`, `265`, `306`, `334`, `596`, `2016`, `1986`, `295`; extremes include `473`, `12345`, `0023`, `2004`, `1301`, `633`, `624`, `508`. |
| C9 | 118 | Temporal, evaluative and comparative/descriptive discourse language | semantic/topic | Moderate | `Feb`, `surprisingly`, `Recently`, `suitably`, `clearly`, `elderly`, `Day`, `clinically`, `Clearly`, `thicker`, `oddly`, `Next`; extremes include `dating`, `Spring`, `viable`, `modest`, `deaths`, `smallest`, `Winter`. |
| C10 | 90 | Example-related morphology mixed with inevitability/reappearance and interpretive stems | mixed | Moderate | `inev`, `exempl`, `reappe`, `Example`, `Interpret`, `ejemplo`, `conjug`, `unve`, `maneu`, `examples`, `defe`; extremes include `example`, `emplo`, `undis`, `eup`, `prem`, `exem`, `depos`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 475 | Administrative characterisation, regulation and up/down-regulation concepts | semantic/topic | High | `Characteristics`, `downregulation`, `recommendations`, `regulations`, `upregulation`, `administrators`, `jurisdictional`, `encouragement`, `beneficiaries`, `consequences`; extremes include `affirmative`, `variance`, `complimentary`, `password`, `Instruction`, `Interior`, `Executive`. |
| C1 | 429 | Negative/intense evaluation, prohibition and adverse-change language | semantic/topic | High | `incredible`, `prohibiting`, `Sometimes`, `spectacular`, `disastrous`, `resembled`, `alarming`, `unbelievable`, `occasionally`, `detrimental`; extremes include `submit`, `uncommon`, `practicing`, `multiplied`, `disappearing`, `preceded`, `excessive`, `heavily`. |
| C2 | 417 | Common grammatical/function words and multilingual/uppercase lexical fragments | lexical/morphological | High | `or`, `ED`, numerals, `ars`, `ao`, `RA`, `ERS`, `ities`, `ALLY`, `M`, `ABLE`; extremes include `или`, `cette`, `CI`, `BLOCK`, `Une` and Cyrillic fragments. |
| C3 | 344 | Short name-like and technical/code fragments | lexical/morphological | Moderate | `Tah`, `Rh`, `Gh`, `Maur`, `Gu`, `Kh`, `GH`, `Bra`, `Herm`, `Hu`, plus `discour`; extremes include `tetra`, `crypt`, `COMP`, `wt`, `cro`, `Ga`. |
| C4 | 259 | Vehicles, agriculture, built environment and material/household objects | semantic/topic | Moderate | `trucks`, `automobiles`, `cylinder`, `Mountains`, `pavement`, `walls`, `roads`, `agriculture`, `chassis`, `vegetables`, `Rails`, `decorations`; extremes include `dishes`, `uniforms`, `curb`, `cassette`, `rails`, `shores`, `roofs`, `Gates`. |
| C5 | 216 | Cardiovascular disease, malignancy, cytokine biology and pathology | semantic/topic | High | `cardiovascular`, `macrophage`, `malignancies`, `atherosclerotic`, `cytokine`, `extremities`, sclerosis fragment, `lymphocytes`, staphylococcus fragment, `dysfunction`, corticosteroid fragment, `interleukin`; extremes include `monocyte`, `thrombosis`, `physiology`, `cranial`, `extremities`. |
| C6 | 206 | Monarchy, religion, bureaucracy and mythic/political roles | mixed | Moderate | `emperor`, `warriors`, `goddess`, `cathedral`, `dragon`, `church`, `believers`, `rituals`, `Colonial`, `bureaucracy`, `King`, `kingdom`; extremes include `Beast`, `USSR`, `conspiracy`, `Uncle`, `Spirit`, `Stalin`, `Guardian`, `throne`. |
| C7 | 180 | Personal names mixed with geographic entities and regions | named-entity | High | `Alabama`, `Sarah`, `Laura`, `Martha`, `Florida`, `Emily`, `Mexico`, `Minnesota`, `Utah`, `Betty`; extremes include `Violet`, `Canada`, `Africans`, `Ivy`, `Sandra`, `Georgia`. |
| C8 | 123 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 83 of 123 tokens are punctuation or symbols; examples include closing delimiters, percent notation, repeated underscores, `displaystyle` and multilingual symbol residue. |
| C9 | 81 | Numeric strings and quantity words | numeric | High | Dominated by `440`, `178`, `448`, `160`, `056`, `sevent`, `hundred`, `0059`, `40`, `018`, `170`; extremes include `1919`, `1939`, `666`, `100000`, `980`, `601`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- characterisation, quantification, testing and developmental analysis;
- entrepreneurship/business/social activity mixed with media and healthcare;
- biomedical/infant-health material mixed with freshness/regenerative terms;
- navigation/search/software-interface and dimensional concepts;
- food/sleep/affect/recreational activity;
- temporal/evaluative/comparative descriptors;
- example morphology mixed with inevitability/reappearance stems;
- names and geography;
- grammar and lexical fragments;
- formatting;
- numeric strings.

Four of eleven communities receive a primary `semantic/topic`
classification. Three are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative regulation and up/down-regulation;
- negative/intense evaluation and prohibition;
- vehicles, agriculture and material objects;
- cardiovascular/malignancy/cytokine pathology;
- monarchy/religion/bureaucracy/mythic roles;
- names and geographic regions;
- grammatical and short technical lexical fragments;
- formatting;
- numeric strings.

Four of ten communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — names dominate but semantic and multilingual outliers remain;
- **positive C3** — entrepreneurship/business overlaps with media and healthcare;
- **positive C4** — biomedical/infant-health material overlaps with freshness
  and regenerative terms;
- **positive C5** — navigation/software-interface terms overlap with dimensional,
  imaging and layout concepts;
- **positive C10** — example morphology overlaps with inevitability,
  reappearance and interpretive stems;
- **negative C2** — grammar, multilingual and uppercase/code-like fragments are
  interleaved;
- **negative C3** — short name-like and technical fragments are interleaved;
- **negative C4** — several physical-world object classes share one broad
  partition;
- **negative C6** — monarchy, religion, bureaucracy and mythic/political roles
  coexist;
- **negative C7** — personal names and geographic entities are both substantial.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
