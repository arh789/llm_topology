# R009 State 25 — block 24 output

## State identity

- R008 state index: `25`
- R008 state label: `block_24_output`
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
| C0 | 324 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `making`, with suffixes/fragments such as `ation`, `le`, `ine`, `l`, `ling`; extremes include `ilation`, `tmp`, `oding`, `ines`, `Sort`, `plays`. |
| C1 | 312 | Exploration, development, anticipation and evolving/process activity | semantic/topic | High | `exploring`, `resolving`, `development`, `anticipated`, `evolves`, `happiness`, `builds`, `develops`, `growing`, `characterizes`, `anticip`; extremes include `debated`, `recall`, `derives`, `unpack`, `anchors`, `developments`. |
| C2 | 309 | Personal names and geographic/name-like entities | named-entity | Moderate | `Karen`, `Matt`, `Mitchell`, `Gary`, `Josh`, `Nam`, `Bennett`, `Kashmir`, `Scott`, `Jay`; extremes include `Berlin`, `Kumar`, `Krish`, `Jake`, `Arnold`, `Dover`. `terrorists` is a semantic outlier. |
| C3 | 298 | Media production, publishing, writing and digital-platform/software activity | semantic/topic | High | `recorded`, `filmmakers`, `Writing`, `filmmaker`, `PhysRev`, `browsers`, `Notification`, `eLife`, `publishing`, `Netflix`, `Bitmap`, `writers`; extremes include `Caption`, `Manager`, `Photo`, `markup`, `director`, `ajax`. |
| C4 | 296 | Entrepreneurship, negotiation and social/business activity mixed with healthcare | mixed | Moderate | `entrepreneurs`, `negotiating`, `sessions`, `interventions`, `adventures`, hospital fragment, `business`, `justification`, `interactions`, `businesses`, `conversations`, `motivation`; extremes include `hospital`, `students`, `funding`, `healthcare`, `interacting`. |
| C5 | 291 | Prefix/stem families around inevitability, interpretation, regeneration and reappearance | lexical/morphological | Moderate | Dominated by incomplete or variant forms such as `inev`, `Interpret`, `fres`, `reappe`, `regener`, `gener`, `regeneration`, `Emer`, `diseng`; extremes include `refres`, `estim`, multilingual fragments and replacement characters. |
| C6 | 245 | Measurement and quantification mixed with example-related morphology and theoretical-science terms | mixed | Moderate | `Measurements`, `characterizing`, `quantification`, `Measurement`, `quantified`, `renormalization`, `gravitational` coexist with `Examples`, `exempl`, `ejemplo`, `examples`; extremes include `example`, `Geometry`, `outputs`. |
| C7 | 204 | Biomedical/pharmacological and infant-health material mixed with food/agricultural terms | mixed | Moderate | `breastfeeding`, `Baby`, `dexamethasone`, `dopaminergic`, `periodontal`, `Ebola`, `doxorubicin`, `fluorescent`, mosquito fragment coexist with `Food`; extremes include `soybean`, `salivary`, `mitotic`, `Lung`, `neonates`. |
| C8 | 191 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 163 of 191 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter and LaTeX-like strings. |
| C9 | 136 | Temporal, evaluative and comparative/descriptive discourse language | semantic/topic | Moderate | `Recently`, `surprisingly`, `Clearly`, `upcoming`, `Again`, `happier`, `Now`, `elderly`, `Day`, `clinically`; extremes include `dominant`, `prominent`, `Notable`, `Winter`, `modest`, `customary`, `smallest`. |
| C10 | 107 | Numeric strings and short coded values | numeric | High | Dominated by `597`, `397`, `297`, `325`, `334`, `324`, `300`, `306`, `607`, `596`, `97`; extremes include `12345`, `473`, `0023`, `2004`, `1234`, `499`, `505`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 3 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 488 | Short name-like, technical and code-like fragments | lexical/morphological | Moderate | `Gh`, `TC`, `RA`, `Tah`, `Rh`, `GH`, `Kh`, `Lah`, `Gu`, `TA`, `Bra`; extremes include `CI`, `crypt`, `ocr`, `ITS`, `Maur`, `FORE`, `BLOCK`, `PROT`. |
| C1 | 391 | Administrative characterisation, recommendations, constitutional/legal and regulatory concepts | semantic/topic | High | `Characteristics`, `recommendations`, `administrators`, `jurisdictional`, `characteristics`, `Constitution`, `beneficiaries`, `administrator`, `Configuration`, `regulations`, `establishment`; extremes include `variance`, `submit`, `conspiracy`, `Executive`, `enactment`, `codes`. |
| C2 | 361 | Personal/geographic entities mixed with monarchy, religion and political/social roles | mixed | Moderate | `Laura`, `Florida`, `Canada`, `Alabama`, `Sarah`, `Louisiana`, `grandmother`, `Martha` coexist with `warriors`, `emperor`, `church`; extremes include `USSR`, `Uncle`, `Guardian`, `Stalin`, `Africans`, `rituals`. |
| C3 | 290 | Negative/intense evaluation, discrimination and distress | semantic/topic | High | `disastrous`, `discour`, `incredible`, `discriminatory`, `unbelievable`, `brutal`, `frightening`, `inconsistent`, `extremities`; extremes include `affirmative`, `Beast`, `complimentary`, `excessive`, `detriment`, `harsh`, `choked`. |
| C4 | 266 | Vehicles, roads, terrain and material/household objects | semantic/topic | Moderate | `trucks`, `automobiles`, `Mountains`, `roads`, `terrace`, `pavement`, `cylinder`, `Rails`, `lamp`, `boats`, `blanket`, `driveway`; extremes include `cassette`, `dishes`, `curb`, `rails`, `roofs`, `shores`, `Gates`. |
| C5 | 258 | Regulation/change actions mixed with qualification, frequency and lexical stems | mixed | Moderate | `downregulation`, `encouragement`, `Specific`, `resembled`, `prohibiting`, `participated`, `activates` coexist with `occasionally`, `Sometimes`, `ALLY`, `ABLE`; extremes include `uncommon`, `multiplied`, `preceded`, `heavily`, `practicing`, `stable`. |
| C6 | 215 | Cardiovascular disease, cytokine biology, immunology and pathology | semantic/topic | High | `cardiovascular`, `macrophage`, `cytokine`, staphylococcus fragment, `circumferential`, `interleukin`, `erythrocytes`, `atherosclerotic`, `archaeological`, `gluc`, `lipids`, cytokine fragment; extremes include `monocyte`, `physiology`, `thrombosis`, `Fc`, `equilibrium`. |
| C7 | 173 | Grammar/function fragments mixed with punctuation and tokenisation residue | formatting/tokenizer | Moderate | Representatives include apostrophe, `or`, `ED`, `said`, numerals, `M`, `ra`, `ars`, `ao`, `some`; 75 tokens are punctuation or symbols, and extremes include replacement characters, `displaystyle`, repeated underscores, percent notation and operator-like strings. |
| C8 | 169 | Multilingual words, suffixes and orthographic fragments | lexical/morphological | High | `или`, `cette`, `questa`, `mucho`, `estaba`, `oder`, `Une`, Greek `και`/`την`, `eller`, `emente`; extremes remain multilingual across Latin, Cyrillic and East Asian scripts. |
| C9 | 88 | Numeric strings, especially historical years and quantity words | numeric | High | Dominated by `1921`, `160`, `178`, `448`, `056`, `451`, `082`, `856`, `hundred`, `1860`, `0059`, `40`; extremes include `1919`, `Forty`, `1939`, `666`, `1840`, `651`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 0 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- exploration/development/anticipation processes;
- media/publishing/software activity;
- entrepreneurship/social/business activity mixed with healthcare;
- measurement/quantification mixed with example morphology;
- biomedical/infant-health material mixed with food/agricultural terms;
- temporal/evaluative/comparative descriptors;
- names and geography;
- common grammar and lexical fragments;
- regeneration/reappearance stem families;
- formatting;
- numeric strings.

Three of eleven communities receive a primary `semantic/topic`
classification. Three are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative/constitutional/regulatory concepts;
- negative/intense evaluation and distress;
- vehicles, roads and physical/material objects;
- cardiovascular/cytokine biomedical pathology;
- personal/geographic material mixed with monarchy/religion/political roles;
- regulation/change mixed with qualification/frequency language;
- short technical/name-like fragments;
- multilingual lexical fragments;
- grammar/punctuation/tokeniser residue;
- numeric strings.

Four of ten communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one
formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C2** — names dominate but several semantic outliers remain;
- **positive C4** — entrepreneurship/social activity overlaps with healthcare;
- **positive C5** — semantic stem families are visible, but incomplete word form
  is the dominant organising feature;
- **positive C6** — measurement/quantification overlaps with example morphology
  and theoretical-science terms;
- **positive C7** — biomedical/infant-health terms overlap with food and
  agricultural material;
- **negative C0** — short name-like, technical and code fragments are interleaved;
- **negative C2** — personal/geographic entities coexist with monarchy,
  religion and political roles;
- **negative C4** — several physical-world object classes share one broad
  partition;
- **negative C5** — regulation/change language overlaps with qualification,
  frequency and lexical-stem material;
- **negative C7** — grammar fragments and punctuation/tokenisation residue
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
