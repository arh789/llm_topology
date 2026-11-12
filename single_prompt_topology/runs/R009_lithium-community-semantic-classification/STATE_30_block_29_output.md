# R009 State 30 — block 29 output

## State identity

- R008 state index: `30`
- R008 state label: `block_29_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 11 | 11 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **23** | **23** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 475 | Personal names and geographic/name-like entities | named-entity | Moderate | `Steve`, `Matt`, `Scott`, `Peter`, `Karen`, `Pakistan`, `Jay`, `Meyer`, `Mumbai`, `Krish`; extremes include `Kumar`, `Berlin`, `Jake` and multilingual name-like fragments. |
| C1 | 377 | Characterisation, discussion, acquisition and developmental/social processes | semantic/topic | High | `characterizing`, `conversations`, `introducing`, `acquiring`, `development`, `discussion`, `characterizes`, `justification`, `evolving`, `negotiating`, `yields`, `discussions`; extremes include `motivations`, `debated`, `informed`, `interviews`, `interactions`, `advance`. |
| C2 | 346 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `all`, `am`, with fragments such as `ation`, `ating`, `le`, `ine`; extremes include `triangle`, `propri`, `DATA`, `leq`, `ines`, `med`, `ivated`. |
| C3 | 342 | Entrepreneurship, organisations and employment mixed with media and institutional activity | semantic/topic | Moderate | `entrepreneurs`, `businesses`, `filmmakers`, `recorded`, `business`, `entrepreneur`, `organisations`, `student`, `filmmaker`, `employees`, `understanding`; extremes include `hospital`, `students`, `Business`, `funding`, `readings`, `director`, `claimants`. |
| C4 | 318 | Biomedical/infant-health and theoretical-system concepts mixed with affect and freshness terms | mixed | Moderate | `breastfeeding`, `Food`, `immunostaining`, `Baby`, `phenomenological`, `dopaminergic`, `kissing`, `renormalization`, `neonates`, `dexamethasone`, `baby`; extremes include `refres`, `tension`, `µm`, `salivary`, `dating`, `Fast`, `tornado`, `mitotic`, `patience`. |
| C5 | 248 | Measurement, quantification, transformation and detection | semantic/topic | High | `Measurements`, `Measurement`, `quantification`, `constructions`, `transformation`, `regularization`, `detection`, `results`, `Detection`, `comparisons`; extremes include `measured`, `Observ`, `anchors`, `Stats`, `Activity`. `tumorigenesis` is a biomedical outlier. |
| C6 | 234 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 158 of 234 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings, with minor software-token residue. |
| C7 | 145 | Photography/browser/software terms mixed with biomedical abbreviations | mixed | Moderate | `Photograph`, `Firefox`, `Photo`, `browsers`, `Bitmap`, `Bio`, `Biomed`, `DB`, `browser`, `FB`, `Thermo`; extremes include `Caption`, `Photo`, `ajax`, `markup`, `Bits`, `IE`, `NET`. |
| C8 | 142 | Numeric strings and short coded values | numeric | High | Dominated by `334`, `345`, `265`, `295`, `326`, `297`, `325`, `1941`, `305`, `306`, `596`; extremes include `0023`, `473`, `633`, `12345`, `2004`, `505`. |
| C9 | 130 | Ambiguity, interpretation and uncertainty-related stems | lexical/morphological | Moderate | `misunderstanding`, `inev`, `unpredict`, `Interpret`, `maneu`, `unavoid`, `negot`, `conjug`, `anticip`, `ambig`, `misunder`, `grapp`; extremes include `estim`, `attribut`, `reconst`, `diseng`, `underest`, `contro`. |
| C10 | 130 | Acknowledgement, temporal and evaluative/discourse descriptors | semantic/topic | Moderate | `acknowledges`, `surprisingly`, `Recently`, `Clearly`, `clearer`, `Wednesday`, `suitably`, `gratefully`, `Accordingly`, `Next`, `Similarly`; extremes include `hi`, `Thanks`, `Notable`, `prominent`, `Spring`, `References`, `FIRST`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 472 | Prohibition, negative/intense evaluation and adverse-change language | semantic/topic | High | `prohibiting`, `ridiculous`, `resembled`, `disastrous`, `ruins`, `Sometimes`, `detrimental`, `extremities`, `incredibly`, `spectacular`, `occasionally`; extremes include `submit`, `limbs`, `heavily`, `practicing`, `detriment`, `reflect`, `resigned`. |
| C1 | 469 | Short name-like and technical/code fragments | lexical/morphological | Moderate | `Tah`, `discour`, `Gh`, `Hu`, `Gu`, `Rh`, `M`, `Th`, `GH`, `RA`, `Kh`, `Wu`; extremes include `Chi`, `tetra`, `CI`, `crypt`, `COMP`, `Maur`. |
| C2 | 405 | Administrative characterisation, regulation and constitutional/bureaucratic concepts | semantic/topic | High | `Characteristics`, `recommendations`, `regulations`, `encouragement`, `Constitution`, `Specific`, `representation`, `bureaucracy`, `heterogeneity`, `beneficiaries`, `characteristics`; extremes include `variance`, `password`, `privileges`, `complimentary`, `equilibrium`. |
| C3 | 287 | Vehicles, terrain, vegetation and built/material objects | semantic/topic | Moderate | `circumferential`, `trucks`, `automobiles`, `cylinder`, `gravel`, `Mountains`, `vegetation`, `walls`, `pavement`, `roofs`, `vegetables`; extremes include `dishes`, `uniforms`, `curb`, `oxides`, `shores`, `trailer`. |
| C4 | 222 | Personal names mixed with geographic entities and regions | named-entity | High | `Sarah`, `Laura`, `Alabama`, `Louisiana`, `Martha`, `Michelle`, `Canada`, `Florida`, `Emily`, `Minnesota`, `Chicago`; extremes include `Violet`, `Canada`, `Emily`, `Sierra`, `Clare`. |
| C5 | 216 | Monarchy, empire and mythic/political roles | mixed | Moderate | `dragon`, `warriors`, `emperor`, `cathedral`, `Colonial`, `USSR`, `Universe`, `king`, `kingdom`, `grandmother`, `empire`, `palace`; extremes include `Beast`, `LHC`, `Uncle`, `Spirit`, `conspiracy`, `rituals`, `Stalin`, `dragons`. |
| C6 | 193 | Multilingual words and orthographic/token fragments | lexical/morphological | High | `or`, Cyrillic `или`, `cette`, Arabic fragments, `tiene`, `questa`, `eller`; extremes remain multilingual across Latin, Cyrillic, Arabic and East Asian scripts, with replacement-character residue. |
| C7 | 160 | Cardiovascular disease, malignancy, cytokine biology and pathology | semantic/topic | High | `malignancies`, `atherosclerotic`, `cardiovascular`, `cytokine`, `macrophage`, sclerosis fragment, `gluc`, corticosteroid fragment, `interleukin`, `diseases`, `TNF`, `cerebellar`; extremes include `monocyte`, `physiology`, `thrombosis`, `cranial`, `leukocyte`, `syndrome`. |
| C8 | 106 | Uppercase lexical stems and code/status terms | lexical/morphological | High | `ED`, `ALLY`, `ET`, `ERS`, `ABLE`, `NEVER`, `THIS`, `CODE`, `REAL`, `INE`, `IAL`; extremes include `FORE`, `IMPLIED`, `IRED`, `ITS`, `codec`, `AST`, `Constant`, `Const`, `codes`, `CONF`. |
| C9 | 97 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 79 of 97 tokens are punctuation or symbols; examples include closing delimiters, repeated underscores, percent notation and operator-like strings. |
| C10 | 63 | Numeric strings and quantity words | numeric | High | Dominated by `25`, `178`, `28`, `448`, `hundred`, `78`, `sevent`, `470`, `680`, `018`, `170`, `459`; extremes include `1919`, `1939`, `666`, `sixty`, `eighteen`. |
| C11 | 51 | Rail transport mixed with Unix/developer tooling | mixed | Moderate | `Rails`, `rails`, `train`, `Rail` coexist with `repo`, `SSH`, `Unix`, `CLI`, `UX`, `CPU`, `concat`, `utils`, `sync`; extremes reproduce both rail and developer-tooling vocabulary. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- characterisation, discussion, acquisition and developmental/social processes;
- entrepreneurship, organisations and employment with media/institutional material;
- measurement, quantification, transformation and detection;
- biomedical/infant-health and theoretical-system concepts mixed with affect and freshness;
- photography/browser/software mixed with biomedical abbreviations;
- ambiguity/interpretation/uncertainty stems;
- acknowledgement, temporal and evaluative discourse;
- names and geography;
- common grammar and lexical fragments;
- formatting;
- numeric strings.

Four of eleven communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- prohibition and negative/intense evaluation;
- administrative/regulatory/constitutional concepts;
- vehicles, terrain and material objects;
- cardiovascular/malignancy/cytokine pathology;
- names and geographic regions;
- monarchy/empire/mythic-political roles;
- multilingual and uppercase technical lexical fragments;
- rail transport mixed with Unix/developer tooling;
- formatting;
- numeric strings.

Four of twelve communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, two mixed, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — names dominate but multilingual and lexical outliers remain;
- **positive C3** — entrepreneurship/employment overlaps with media,
  institutional and healthcare terms;
- **positive C4** — biomedical/infant-health and theoretical-system concepts
  overlap with affect/freshness material;
- **positive C7** — software/browser/media concepts overlap with biomedical
  abbreviations;
- **positive C9** — semantic uncertainty/interpretation content is visible, but
  incomplete word form remains a major organising feature;
- **positive C10** — acknowledgement, temporal and evaluative discourse overlap;
- **negative C1** — short name-like and technical/code fragments are interleaved;
- **negative C3** — several physical-world object classes share one broad
  partition;
- **negative C5** — monarchy, empire, political and mythic roles coexist;
- **negative C11** — rail vocabulary and Unix/developer tooling share a small
  but clearly mixed partition.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
