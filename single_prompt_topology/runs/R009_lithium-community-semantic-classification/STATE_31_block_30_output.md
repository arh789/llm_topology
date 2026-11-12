# R009 State 31 — block 30 output

## State identity

- R008 state index: `31`
- R008 state label: `block_30_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 11 | 11 | reconciled |
| negative_tail | 13 | 13 | reconciled |
| **Total** | **24** | **24** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 415 | Characterisation, measurement, quantification and developmental/social processes | semantic/topic | High | `characterizing`, `Measurement`, `Measurements`, `introducing`, `quantification`, `acquiring`, `development`, `discussion`, `interventions`, `conversations`, `results`, `characterizes`; extremes include `measured`, `tension`, `debated`, `interactions`, `interviews`, `motivations`, `summarized`. |
| C1 | 379 | Personal names and geographic/name-like entities | named-entity | Moderate | `Mitchell`, `Krish`, `Jay`, `Bennett`, `Mik`, `Mumbai`, `Pakistan`, `Karen` dominate alongside name-like fragments; extremes include `Berlin`, `Krish`, `Kumar` and multilingual fragments. |
| C2 | 292 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `all`, `into`, `am`, `id`, with suffixes/fragments such as `ation`, `ating`, `l`; extremes include `triangle`, `ilation`, `charge`, `choice`, `rolling`, `leq`. |
| C3 | 270 | Film/media production and software/interface systems | semantic/topic | High | `filmmakers`, `Photograph`, `Play`, `Notification`, `filmmaker`, `Bitmap`, `Output`, `buffer`, `Video`, `manager`, `Position`; extremes include `Photo`, `recorder`, `Caption`, `pages`, `DATA`, `Manager`, `markup`, `ajax`. |
| C4 | 257 | Entrepreneurship/business and retail activity mixed with healthcare, reading and family terms | mixed | Moderate | `entrepreneurs`, `breastfeeding`, `organisations`, `businesses`, `business`, `Reading`, `shops`, `entrepreneur`, `therapists`, `Food`, `shoppers`, `Baby`; extremes include `hospital`, `students`, `Tours`, `director`, `claimants`, `neonates`, `readings`. |
| C5 | 206 | Mathematical/code punctuation and symbolic formatting with acknowledgement/paratext residue | formatting/tokenizer | High | 154 of 206 tokens are punctuation or symbols; representatives are dominated by brace/operator strings, with `Acknowledgments` and `acknowledges`; extremes include `INTRODUCTION`, `Bibliography` and symbolic delimiters. |
| C6 | 193 | Biomedical, psychological and theoretical-system concepts | mixed | Moderate | `periodontal`, `renormalization`, `phenomenological`, `pulmonary`, `dopaminergic`, `centrifug`, `psychosocial`, `analytically`, `Psychological`, `dexamethasone`, `fluorescent`; extremes include `salivary`, `mitotic`, `lung`, `Lung`, `Flow`, `soybean`. |
| C7 | 188 | Interpretation, uncertainty, discrepancy, dispute and regeneration concepts | semantic/topic | Moderate | `Interpret`, `unavoid`, `unpredict`, `discrepancies`, `challenge`, `inev`, `disputes`, `puzz`, `regeneration`, `undisputed`; extremes include `unpack`, `attribut`, `reconst`, `militant`, with `kissing` and `snar` as outliers. |
| C8 | 142 | Numeric strings and short coded values | numeric | High | Dominated by `334`, `345`, `265`, `295`, `1941`, `127`, `297`, `325`, `134`, `326`, `393`; extremes include `473`, `0023`, `633`, `575`, `2016`, `97`. |
| C9 | 133 | Evaluative, commercial and evidential descriptors | semantic/topic | High | `interesting`, `profitable`, `ignored`, `sustainable`, `Next`, `surprisingly`, `intuitive`, `evident`, `fraudulent`, `questionable`; extremes include `stake`, `informed`, `funding`, `noticed`, `budgets`, `Notable`, `viable`, `modest`. |
| C10 | 61 | Freshness, selection and comparative/action descriptors | mixed | Moderate | `Fresh`, `Draw`, `fres`, `pick`, `fresh`, `underest`, `thicker`, `Select`, `Fast`, `sket`; extremes include `refres`, `smallest`, `mars`, `Add`, `picks`, `atten`, `watch`. |

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
| C0 | 499 | Administrative characterisation, regulation and consequence/heterogeneity concepts | semantic/topic | High | `Characteristics`, `recommendations`, `characteristics`, `heterogeneity`, `beneficiaries`, `consequences`, `regulations`, `upregulation`, `representation`, `Specific`; extremes include `variance`, `Interior`, `detriment`, `practicing`, `privileges`, `password`, `equilibrium`. |
| C1 | 314 | Short name-like and technical/code fragments | lexical/morphological | Moderate | `Tah`, `M`, `Th`, `Rh`, `Gh`, `ET`, `RA`, `TG`, `Hu`, `Gu`, `GH`; extremes include `Chi`, `tetra`, `CI`, `COMP`, `crypt`, `PLC`, `Maur`. |
| C2 | 290 | Monarchy, empire, religion and mythic/political roles | mixed | Moderate | `emperor`, `dragon`, `cathedral`, `warriors`, `Empire`, `palace`, `dragons`, `king`, `grandmother`, `Greeks`, `Colonial`, `heavenly`; extremes include `Beast`, `Duke`, `conspiracy`, `Spirit`, `USSR`, `throne`, `Mountains`. |
| C3 | 255 | Prohibition, disappearance, creation and attempted/assisted change actions | semantic/topic | High | `prohibiting`, `resembled`, `disappeared`, `discour`, `encourages`, `prohibits`, `created`, `attempting`, `attempted`, `prohibited`, `creator`, `Creator`; extremes include `submit`, `assist`, `reflect`, `preceded`, `disappearing`. |
| C4 | 253 | Personal names and name-like entities | named-entity | High | `Sarah`, `Martha`, `Laura`, `Emily`, `Michelle`, `Catherine`, `Ruth`, `Stephanie`, `Charlotte`; extremes include `Violet`, `Emily`, `Sierra`, `Ivy`, `Nicolas`, with a few lexical fragments. |
| C5 | 236 | Cardiovascular disease, vascular biology and pathology | semantic/topic | High | `macrophage`, `atherosclerotic`, `cytokine`, `cardiovascular`, `diseases`, bacterial fragment, sclerosis fragment, `endothelium`, `CRP`, `gluc`, thrombus fragment; extremes include `monocyte`, `oxides`, `thrombosis`, `leukocyte`, `cranial`. |
| C6 | 228 | Multilingual words and orthographic/token fragments | lexical/morphological | High | `or`, Arabic fragments, `Sty`, `eller`, Cyrillic `или`, `cette`, `fant`; extremes remain multilingual across Latin, Cyrillic, Arabic and East Asian scripts, with replacement-character residue. |
| C7 | 228 | Built environment, vehicles, agriculture and material/household objects | semantic/topic | Moderate | `walls`, `cylinder`, `trucks`, `automobiles`, `vegetables`, `gravel`, `agriculture`, `extremities`, `roofs`, `firearms`, `chassis`, `roads`; extremes include `dishes`, `limbs`, `Rails`, `Gates`, `curb`, `Sauce`, `cassette`, `coat`, `spice`. |
| C8 | 156 | Negative/intense evaluation and frequency/degree language | semantic/topic | High | `ridiculous`, `glorious`, `disastrous`, `particularly`, `Sometimes`, `occasionally`, `incredibly`, `spectacular`, `brutal`, `fortunately`; extremes include `excessive`, `heavily`, `harsh`, `Ultra`, `uncommon`. |
| C9 | 95 | Uppercase lexical stems and code/status terms | lexical/morphological | High | `ED`, `ABLE`, `some`, `NEVER`, `THIS`, `REAL`, `SOME`, `INE`, `LIKE`, `CODE`, `ARE`; extremes include `IRED`, `FORE`, `ITS`, `BLOCK`, `ANY`, `DEFAULT`, `codec`, `codes`. |
| C10 | 91 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 75 of 91 tokens are punctuation or symbols; examples include closing delimiters, repeated underscores, percent notation and operator-like strings. |
| C11 | 70 | Geographic entities and regions | named-entity | High | `Alabama`, `Utah`, `Memphis`, `Florida`, `Georgia`, `Minnesota`, `Missouri`, Cleveland fragment, `Africans`, `Northwestern`, `Houston`; extremes include `Canada`, `Springs`, `Rouge`, `Yankees`, `cities`. |
| C12 | 65 | Numeric strings and quantity words | numeric | High | Dominated by `272`, `28`, `hundred`, `25`, `two`, `178`, `170`, `196`, `448`, `082`, `680`, `eighty`; extremes include `1939`, `666`, `40`, `sevent`, `1919`, `sixty`, `601`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 2 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- characterisation, measurement, quantification and developmental/social processes;
- film/media production and software/interface systems;
- entrepreneurship/business/retail mixed with healthcare and family terms;
- biomedical/psychological/theoretical-system concepts;
- interpretation/uncertainty/dispute and regeneration concepts;
- evaluative/commercial/evidential descriptors;
- freshness/selection/comparative descriptors;
- names and geography;
- common grammar and lexical fragments;
- formatting;
- numeric strings.

Four of eleven communities receive a primary `semantic/topic`
classification. Three are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative characterisation/regulation/consequence concepts;
- prohibition/disappearance/creation/change actions;
- cardiovascular/vascular pathology;
- built environment, vehicles and material objects;
- negative/intense evaluation and frequency/degree language;
- monarchy/empire/religion/mythic roles;
- personal names and geographic regions;
- multilingual and uppercase technical lexical fragments;
- formatting;
- numeric strings.

Five of thirteen communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, two named-entity, one mixed,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — names dominate but lexical and multilingual outliers remain;
- **positive C4** — business/retail concepts overlap with healthcare, reading and
  family material;
- **positive C6** — biomedical, psychological and theoretical-system concepts
  coexist;
- **positive C7** — interpretation/uncertainty semantics overlap with several
  lexical and bodily outliers;
- **positive C10** — freshness, selection, comparison and lexical-stem material
  coexist;
- **negative C1** — short name-like and technical/code fragments are interleaved;
- **negative C2** — monarchy, empire, religion and mythic/political roles coexist;
- **negative C7** — several physical-world object classes share one broad
  partition;
- **negative C11** — geographic entities include a few social and lexical
  outliers.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
