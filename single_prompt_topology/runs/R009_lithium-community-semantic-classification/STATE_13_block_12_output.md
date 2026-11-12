# R009 State 13 — block 12 output

## State identity

- R008 state index: `13`
- R008 state label: `block_12_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 12 | 12 | reconciled |
| negative_tail | 13 | 13 | reconciled |
| **Total** | **25** | **25** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 629 | Personal names and name-like entities mixed with lexical/tokenisation residue | mixed | Moderate | Strong name content includes `Ken`, `Karen`, `Mitchell`, `Gary`, `Tony`, while `Coca`, `remem`, replacement characters and multilingual fragments prevent a clean named-entity classification. |
| C1 | 503 | Biomedical/health terminology mixed with food, telecommunications and psychosocial language | mixed | Moderate | `dexamethasone`, `breastfeeding`, `dopaminergic`, `pneum`, `neurotrans`, `Salmonella`, `antifungal`, `overweight` coexist with `Food`, `telecommunications`, `motivational`, `psychosocial`, `innovative`. |
| C2 | 382 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | `as`, `at`, `A`, `where`, `am`, `making`, `back`, `found`, `right`, together with fragments such as `ide`, `ne`; extremes remain dominated by short forms and fragments. |
| C3 | 316 | Code/text formatting strings mixed with software and paratext tokens | formatting/tokenizer | High | 185 of 316 tokens are punctuation or symbols; representatives include bracket/brace strings alongside `BytePtrFromString`, `Acknowledgements`, while extremes include `sizeof`, `mathchoice`, `getElementById`, `Thanks`. |
| C4 | 297 | Management, conversation, investigation and business/interview activity | semantic/topic | High | `management`, `conversations`, `investigations`, `experience`, `interviews`, `adventures`, `negotiating`, `businesses`, `discussions`, `interventions`, `interviewing`; extremes include `employment`, `business`, `talks`. |
| C5 | 233 | Physical/computational interactions, coupling and system dynamics | semantic/topic | High | `interactions`, `interacting`, `superconducting`, `size`, `development`, `coupling`, `values`, `change`, `computations`, `perturbative`, Lagrangian fragment, `Forms`; extremes include `renormalization`, `Spin`, `Phase`, `systems`. |
| C6 | 219 | Observation, inference, development and research/process actions | semantic/topic | High | `characterizing`, `initiating`, `remembering`, `exploring`, `observing`, `entering`, `hypothesized`, `inserting`, `developing`, `computed`, `inferred`, `adopting`; extremes include `recording`, `derives`, `estim`. |
| C7 | 182 | Software/web/database terms mixed with technical abbreviations and units | mixed | Moderate | `DB`, `mysql`, `Browser`, `facebook`, `Entry`, `Document`, `WordPress`, Kubernetes fragment coexist with abbreviations and units such as `MH`, `MAR`, `µm`, `PRES`, `BA`, `RAW`. |
| C8 | 136 | Affect, bodily/social actions and infant/neonatal life | semantic/topic | Moderate | `happier`, `smiled`, `sleeping`, `shook`, `newborn`, `grinned`, `gripped`, `shrugged`, `kissed`, `swung`, `swallowed`, `neonates`; extremes include `viable`, `neon`, `foraging`. |
| C9 | 126 | Numeric strings, including years | numeric | High | Dominated by `596`, `324`, `624`, `1993`, `304`, `604`, `603`, `597`, `504`, `697`, `1989`, `295`; extremes include `1997`, `2019`, `737`, `508`, `0023`. |
| C10 | 52 | Cities and geographic entities | named-entity | High | `Manchester`, `Amsterdam`, `Mumbai`, `Berlin`, `Frankfurt`, `Stockholm`, `London`, `Paris`, Heidelberg fragment, `Brooklyn`, `Hamburg`; extremes include `Taiwan`, `Queens`, `Saudi`, `European`. |
| C11 | 24 | Calendar/time terms mixed with distance and everyday-object vocabulary | mixed | Moderate | `Day`, `Wednesday`, `Saturday`, `Week`, `Sunday`, `Previously`, `week`, `months` coexist with `mile`, `Mile`, `miles`, `ft`, `trails` and `shoe`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 512 | Characterisation, regulation/constraint and evaluative-change language | mixed | Moderate | `Characteristics`, `prohibiting`, `unconstitutional`, `circumstantial`, `encouragement`, `downregulation`, `Delete`, `disproportionate`, `discriminatory`, `emphasizing`; extremes include `specificity`, `Features`, `Clause`, `submit`, `composed`. |
| C1 | 436 | Personal names mixed with technical and lexical fragments | named-entity | Moderate | `Claud`, `Jess`, `Dav`, `Emily`, `Molly`, `Freder`, `Claude`, `Crom`, `Lah` coexist with short codes and fragments such as `TG`, `GH`, `crypt`, `CI`, `LCD`, `PROT`. |
| C2 | 425 | Common grammatical/function words, punctuation and lexical fragments | lexical/morphological | High | `I`, `not`, `or`, `than`, `they`, with fragments such as `e`, `ized`, `ES`; extremes include `ORD`, `ED`, `ancers`, `omes` and multilingual fragments. |
| C3 | 372 | Government, royalty, religion and family/social roles | mixed | Moderate | `emperor`, `Constitution`, `palace`, `guards`, `cathedral`, `church`, `Cathedral`, `mother`, `priest`, `grandmother`, `Empire`, `legislature`; extremes include `throne`, `Interior`, `Uncle`, `wedding`, `aunt`, `Queen`, `heavens`. |
| C4 | 336 | Vehicles, built environment, household objects and natural terrain | semantic/topic | Moderate | `circumferential`, `chassis`, `trucks`, `automobiles`, `administrator`, `sidewalk`, `driveway`, `mountains`, `furniture`, `appliances`, `gravel`, `volcano`; extremes include `cylinder`, `barrel`, `curb`, `roofs`, `roads`. |
| C5 | 264 | Distribution, technology, data, algorithms and quantitative/mathematical concepts | mixed | Moderate | `uniforms`, `distributions`, `uniformity`, `technologies`, `concepts`, `distribution`, `database`, `algorithms`, `perpendicular`, `probability`, `dashboard`; extremes include `variance`, `algebra`, `quotient`, `codes`, `variability`, `methodology`. |
| C6 | 250 | Catastrophe, tragedy and negative/intense evaluation | semantic/topic | High | `disasters`, `catast`, `horrific`, `disastrous`, `catastrophe`, `tragedy`, `catastrophic`, `incredible`, `unbelievable`, `discour`, `glorious`; extremes include `harsh`, `supreme`, `bleak`, `ignorant`. |
| C7 | 192 | Biomedical diagnostics, cardiovascular disease and laboratory biology | semantic/topic | High | `immunofluorescence`, `echocardiography`, `cardiovascular`, `atherosclerotic`, `malignancies`, `diseases`, `electrophoresis`, `dysfunction`, `epithelium`, `Experiments`; extremes include `physiology`, `carcinoma`, `angiography`, `erythrocytes`. |
| C8 | 155 | Numeric strings, especially historical years | numeric | High | Dominated by `1884`, `1890`, `1860`, `1881`, `1900`, `1870`, `1880` plus shorter values; extremes include `1840`, `407`, `1830`, `490`. |
| C9 | 91 | Geographic entities and administrative regions | named-entity | High | `Alabama`, `Connecticut`, `province`, `Georgia`, `Minnesota`, `Edinburgh`, `Kerala`, `Illinois`, `Montreal`; extremes include `Canada`, `Adelaide`, `borough` and location-name fragments. |
| C10 | 75 | Adverbial qualification, degree and evaluative emphasis | semantic/topic | High | `particularly`, `occasionally` fragment, `unfortunately`, `essentially`, `fortunately`, `specifically`, `Essentially`, `effectively`, `literally`; extremes include `heavily`, `logically`, `entirely`. |
| C11 | 65 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 53 of 65 tokens are punctuation or symbols; examples include closing delimiters, percent notation, ellipses and repeated operator strings. |
| C12 | 32 | Courtroom, evidence, injury, security and safety | semantic/topic | High | `courtroom`, `testimony`, `injuries`, `security`, `jury`, `court`, `Estate`, `evidence`, `safety`, `TBI`, `harm`; extremes include `Safety`, `hazards`, `testament`, `privacy`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 1 |
| named-entity | 2 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- management, interviews, business and communication;
- observation/inference/research actions;
- physical/computational interactions and system dynamics;
- affective/bodily/social actions and neonatal terms;
- software/web/database material;
- people and geographic entities;
- biomedical/health terms mixed with food and telecommunications;
- grammar and lexical fragments;
- formatting;
- numeric strings;
- time/distance/everyday-object material.

Four of twelve communities receive a primary `semantic/topic`
classification. Four are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- regulation/constraint and characterisation;
- catastrophe/tragedy/intense evaluation;
- biomedical diagnostics and laboratory biology;
- vehicles, physical environment and household objects;
- quantitative/data/mathematical concepts;
- courtroom/evidence/safety language;
- adverbial qualification;
- names and geographic regions;
- government/royalty/religious/social roles;
- grammar and lexical fragments;
- formatting;
- numeric strings.

Five of thirteen communities receive a primary `semantic/topic`
classification. Three are mixed, two named-entity, one lexical/morphological,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — personal names coexist with substantial tokenizer and
  lexical residue;
- **positive C1** — biomedical/health, food, telecommunications and psychosocial
  content coexist;
- **positive C7** — software/web/database terms overlap with abbreviations and
  measurement units;
- **positive C8** — affective/social actions and neonatal terms share one
  community;
- **positive C11** — time/calendar terms overlap with distance and everyday
  object vocabulary;
- **negative C0** — characterisation, regulation and evaluative-change language
  overlap;
- **negative C1** — names dominate but technical fragments are substantial;
- **negative C3** — government, royalty, religion and family/social roles
  coexist;
- **negative C4** — physical-environment and object classes are broad;
- **negative C5** — data/technology and mathematical/statistical concepts
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
