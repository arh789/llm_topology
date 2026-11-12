# R009 State 18 — block 17 output

## State identity

- R008 state index: `18`
- R008 state label: `block_17_output`
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
| C0 | 526 | Personal names, cities and national/geographic entities | named-entity | High | `Manchester`, `Scott`, `Hamburg`, `Mitchell`, `Karen`, `Matt`, `Josh`, `Amsterdam`, `Germany`, `Jay`; extremes include `Berlin`, `Krish` and name-like fragments. |
| C1 | 421 | Food, hospital/medical and health-related terms mixed with retail/lifestyle and freshness language | mixed | Moderate | `Food`, `breastfeeding`, hospital fragments, `pneum`, `psychiat`, `shoppers`, `hospital`, `shops`, `Sleep`, `Medical` coexist with `Fresh`; extremes include `airborne`, `µm`, `fluores`, `tornado`, `mars`. |
| C2 | 392 | Exploration, entrepreneurship, negotiation and motivational/business activity | semantic/topic | High | `exploring`, `entrepreneurs`, `anticipated`, `negotiating`, `explores`, `motivations`, `yields`, `motivation`, `anticipation`, `discuss`, `business`, `adventures`; extremes include `stake`, `debated`, `recall`, `tension`, `bridging`. |
| C3 | 318 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `am`, with suffixes/fragments such as `ation`, `ating`, `le`, `ine`, `it`, `l`; extremes include `ausing`, `ilation`, `med`, `ivated`. |
| C4 | 298 | Transformations, measurements, interactions and quantitative/computational analysis | semantic/topic | High | `transformations`, `determinations`, `interactions`, `Measurements`, `characterizing`, `Measurement`, `size`, `evolving`, `imaging`, `computations`, `evolves`, `values`; extremes include `sensing`, `interaction`, `renormalization`, `Stats`. |
| C5 | 292 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 203 of 292 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `mathchoice`, `javase`, `INTRODUCTION` and symbolic fragments. |
| C6 | 178 | Film/media, learning, interviews, photography and workshop activity | semantic/topic | High | `conversations`, `filmmakers`, `filmmaker`, `Learning`, `interviews`, `photography`, `interventions`, `Play`, `workshops`, `facebook`, `interviewing`, `therapists`; extremes include `students`, `recorder`, `director`, `Photo`. |
| C7 | 145 | Browser, search, session and software/interface systems | semantic/topic | High | `Notification`, `browsers`, `Firefox`, `Resolver`, `animation`, `Query`, `Session`, `manager`, `Search`; extremes include `sizeof`, `Manager`, `animated`, `EXPORT`, `ajax`, `NET`, `getElementById`. |
| C8 | 135 | Quantitative/evaluative adverbs and discourse/context modifiers | semantic/topic | Moderate | `surprisingly`, `numerically`, `analytically`, `Having`, `With`, `More`, `elderly`, `Now`, `larger`, `Next`, `Clearly`; extremes include `dominant`, `busy`, `Coming`, `Wednesday`, `Day`. |
| C9 | 120 | Numeric strings and short coded values | numeric | High | Dominated by `325`, `324`, `306`, `597`, `534`, `297`, `697`, `334`, `587`, `67`, `1986`, `54`; extremes include `12345`, `505`, `2004`, `633`, `737`, `0023`. |
| C10 | 115 | Prefix/stem families around inevitability, reappearance, reconstruction and interpretation | lexical/morphological | Moderate | Dominated by incomplete forms such as `inev`, `unavoid`, `controvers`, `unve`, `reappe`, `conjug`, `maneu`, `grapp`, `reconst`, `negot`, `interpre`, `lur`; extremes remain mostly lexical stems. |
| C11 | 75 | Example-related multilingual words and morphological fragments | lexical/morphological | High | `exempl`, `ejemplo`, `Example`, `exem`, `Examples`, `examples`, `quando`; extremes include `example`, `emplo`, `wij`, `nuest`, `wieder`, `Para`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 512 | Administrative characterisation, configuration and recommendation systems | semantic/topic | High | `Characteristics`, `administrators`, `superintendent`, `characteristics`, `Configuration`, `administrator`, `recommendations`, `representation`, `Superintendent`, `beneficiaries`; extremes include `variance`, `specificity`, `Executive`, `availability`, `identifier`. |
| C1 | 424 | Personal names and name-like entities | named-entity | High | `Laura`, `Emily`, `Sarah`, `Caroline`, `Catherine`, `Connie`, `Claire`, `Jess`, `Nicolas`; extremes include `Violet`, `Friedrich` and additional name-like fragments. |
| C2 | 366 | Short technical/computing abbreviations and code-like fragments | lexical/morphological | Moderate | `WHAT`, `RA`, `TG`, `GH`, `TC`, `GGT`, `Enc`, `Cl`, `CE`; extremes include `crypt`, `CI`, `SSH`, `PROT`, `ITS`, `IDENT`, `LCD`, `IMPLIED`. |
| C3 | 349 | Adverse evaluation, legal/jurisdictional constraint and intensity | semantic/topic | High | `circumstantial`, `unconstitutional`, `discriminatory`, `circumstances`, `incredible`, `jurisdictional`, `unbelievable`, `stupid`, `brutal`; extremes include `affirmative`, `harsh`, `heavily`, `disadvantages`, `excessive`, `supreme`. |
| C4 | 335 | Cardiovascular disease, cytokine biology, immunology and pathology | semantic/topic | High | `cardiovascular`, `cytokine`, `atherosclerotic`, `epidemiological`, `cytokines`, `macrophage`, `interleukin`, inflammatory fragment, `monocyte`, `gluc`, `hypertension`; extremes include `physiology`, `thrombosis`, `derm`. |
| C5 | 326 | Regulation, encouragement, activation, deletion and institutional/change actions | semantic/topic | High | `downregulation`, `prohibiting`, `encourages`, `resembled`, `encouragement`, `received`, `activate`, `Delete`, `establishment`, `excluding`, `prohibits`; extremes include `enactment`, `submit`, `practicing`, `composed`, `preceded`. |
| C6 | 269 | Family, monarchy, government and mythic/conflict roles | mixed | Moderate | `grandmother`, `Constitution`, `palace`, `emperor`, `mother`, `church`, `dragon`, `Sultan`, `queen`, `warriors`, `king`, `Americans`; extremes include `Uncle`, `Guardian`, `Beast`, `conspiracy`, `USSR`. |
| C7 | 241 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `said`, `different`, `some`, `two`, with fragments `e`, `ED`, `ra`, `ao`; extremes include `cette`, `Une`, Cyrillic/Arabic fragments and other incomplete forms. |
| C8 | 189 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `automobiles`, `trucks`, `terrace`, `vegetables`, `gravel`, `roads`, `cylinder`, `uniforms`, `pavement`, `furniture`, `stones`, `firearms`; extremes include `curb`, `dishes`, `roofs`, `ignition`, `blankets`, `barrel`, `rails`. |
| C9 | 124 | Numeric strings, especially historical years | numeric | High | Dominated by `1921`, `448`, `451`, `441`, `856`, `1860`, `1910`, `1867`, `1920`, `651`; extremes include `1919`, `1890`, `980`, `1939`, `40`. |
| C10 | 82 | Geographic entities and regions | named-entity | High | `Pennsylvania` fragment, `Alabama`, `Florida`, `Louisiana`, Barcelona fragment, `Mexico`, `Minnesota`, `Georgia`, `Argentina`, `Orleans`, `Arkansas`; extremes include `Illinois`, `Canada`, `Rouge`. |
| C11 | 74 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 62 of 74 tokens are punctuation or symbols; examples include closing delimiters, percent notation, repeated punctuation, underscores and operator-like strings. |

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

- exploration, entrepreneurship and motivational/business activity;
- transformations, measurements and quantitative/computational analysis;
- film/media, learning, interviews and photography;
- browser/search/software systems;
- quantitative/evaluative discourse modifiers;
- food/medical/retail/lifestyle material;
- names and geography;
- grammar and lexical fragments;
- example-related multilingual morphology;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative/configuration/recommendation systems;
- adverse/legal/evaluative language;
- cardiovascular/cytokine/immunological pathology;
- regulation/encouragement/activation/deletion;
- vehicles, roads and material objects;
- family/monarchy/government/mythic roles;
- names and geographic regions;
- grammatical and technical lexical fragments;
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

- **positive C1** — medical/health, retail/lifestyle and freshness language
  coexist;
- **positive C2** — exploration/motivation overlaps with entrepreneurship and
  business activity;
- **positive C8** — quantitative/evaluative adverbs and general discourse
  modifiers overlap;
- **positive C10** — semantic stems are evident, but incomplete word form is
  the dominant organising feature;
- **negative C2** — technical semantics are evident, but abbreviated form is
  the dominant organising feature;
- **negative C6** — family, monarchy, government and mythic/conflict roles
  coexist;
- **negative C8** — multiple physical-world object classes share one broad
  partition.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
