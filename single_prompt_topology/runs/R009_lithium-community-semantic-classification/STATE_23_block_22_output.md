# R009 State 23 — block 22 output

## State identity

- R008 state index: `23`
- R008 state label: `block_22_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 13 | 13 | reconciled |
| negative_tail | 11 | 11 | reconciled |
| **Total** | **24** | **24** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 523 | Personal names, cities and geographic entities | named-entity | High | `Steve`, `Matt`, `Manchester`, `Mitchell`, `Karen`, `Scott`, `Hamburg`, `Pakistan`, `Jake`, `Kashmir`, `Derek`; extremes include `Berlin`, `Kumar`, `Krish` and name fragments. |
| C1 | 326 | Exploration, characterisation, negotiation and developmental/process activity | semantic/topic | High | `exploring`, `characterizing`, `sessions`, `negotiating`, `yields`, `evolves`, `conversations`, `develops`, `explores`, `recorded`, `modeling`, `improves`; extremes include `debated`, `derives`, `developments`, `informed`, `funding`, `interviewing`. |
| C2 | 305 | Measurement, interaction, quantification and computational/organisational analysis | semantic/topic | High | `Measurements`, `interactions`, `quantification`, `interventions`, `Measurement`, `computations`, `renormalization`, `comparisons`, `results`, `organisations`, `interacting`; extremes include `tension`, `anchors`, `interaction`, `sensing`. |
| C3 | 295 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 198 of 295 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `triangle`, `leq` and symbolic fragments. |
| C4 | 283 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `back`, with suffixes/fragments such as `ation`, `ating`, `le`, `ine`, `l`, `ling`; extremes include `ilation`, `ausing`, `oding`, `ines`, `passing`. |
| C5 | 269 | Navigation, software/platform management and size/layout concepts | semantic/topic | Moderate | `navigating`, `size`, `Notification`, `Position`, `manager`, `Writing`, `score`, `platforms`, `managers`, `Size`, `WordPress`, `widths`; extremes include `Manager`, `ajax`, `pages`, `NET`, `markup`, `Device`, `outputs`. |
| C6 | 249 | Food, leisure, shopping, affect and recreational activity | semantic/topic | Moderate | `Food`, `adventures`, `happiness`, `shops`, `discomfort`, `shopping`, `fishing`, `workshops`, `compassion`, `Play`, `aspirations`; extremes include `smiled`, `plays`, `ring`, `Tours`, `battles`, `sprang`. |
| C7 | 246 | Biomedical, pharmacological, infant and healthcare terminology | semantic/topic | High | `dopaminergic`, `breastfeeding`, `tumorigenesis`, `biomedical`, `Baby`, `dexamethasone`, `analges`, `biomed`, `Medical`, `immunostaining`, `therapists`; extremes include `hospital`, `Lung`, `salivary`, `mitotic`, `healthcare`, `neonates`. |
| C8 | 232 | Anticipation/emergence mixed with temporal and evaluative descriptors | semantic/topic | Moderate | `surprisingly`, `anticipated`, `emerging`, `Recently`, `Fresh`, `interesting`, `Clearly`, `fraudulent`, `larger`, `older`; extremes include `dominant`, `dating`, `Good`, `adjustable`, `Fast`, `viable`, `prominent`. |
| C9 | 201 | Prefix/stem families around emergence, freshness, avoidance and reappearance | lexical/morphological | Moderate | Dominated by incomplete forms such as `inev`, `Emer`, `fres`, `unve`, `maneu`, `negot`, `unavoid`, `reappe`, `Rew`, `gener`, `happ`; extremes remain largely partial lexical forms such as `refres`, `sket`, `fluores`, `anticip`, `aberr`. |
| C10 | 182 | Entrepreneurship, research, filmmaking, photography and business/media activity | semantic/topic | High | `entrepreneurs`, `Researchers`, `filmmakers`, `photography`, `filmmaker`, `Animation`, `businesses`, `business`, `entrepreneur`, `Netflix`, `Photo`; extremes include `students`, `director`, `animated`, `recorder`, `Business`, `enroll`. |
| C11 | 139 | Numeric strings and short coded values | numeric | High | Dominated by `296`, `325`, `697`, `596`, `324`, `306`, `597`, `397`, `300`, `97`, `297`, `393`; extremes include `12345`, `473`, `2004`, `0023`, `499`, `530`. |
| C12 | 11 | Acknowledgement, greeting and thanks language | semantic/topic | High | `Acknowled`, `acknow`, `hey`, `hello`, `thanks`, `Thanks`, `hi`, `thank`, `hell`; extremes reproduce the same acknowledgement/greeting cluster. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 8 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 0 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 551 | Personal names and name-like entities mixed with short fragments | named-entity | Moderate | `Laura`, `Sarah`, `Emily`, `Molly`, `Connie`, `Martha`, `Claire` dominate, with short fragments such as `Gh`, `Tah`, `GH`, `Hu`, `Rub`; extremes include `Violet`, `Maur`, `Friedrich`. |
| C1 | 476 | Encouragement, prohibition, removal, legal constraint and adverse evaluation | semantic/topic | High | `encourages`, `prohibiting`, `removing`, `unreasonable`, `Comprehensive`, `encouragement`, `Specific`, `resembled`, `discour`, `jurisdictional`, `discriminatory`; extremes include `affirmative`, `uncommon`, `enactment`, `submit`, `disappearing`. |
| C2 | 429 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `say`, `said`, with fragments `e`, `B`, `ized`, `ra`, `ED`, `ALLY`; extremes include `cette`, `Chi`, Cyrillic fragments, `ITS`, `ALE`, `FORE`. |
| C3 | 315 | Cardiovascular disease, cytokine biology and biomedical pathology | semantic/topic | High | `downregulation`, `cardiovascular`, `macrophage`, `cytokine`, `interleukin`, staphylococcus fragment, `cytokines`, `atherosclerotic`, `lipids`, `lymphocyte`; extremes include `monocyte`, `gluc`, `physiology`, sclerosis fragments. |
| C4 | 315 | Administrative characterisation, configuration and constitutional/regulatory concepts | semantic/topic | High | `Characteristics`, `recommendations`, `characteristics`, `Configuration`, `regulations`, `Constitution`, `circumstances`; extremes include `uniforms`, `codes`, `variance`, `password`, `privileges`, `IMPLIED`. |
| C5 | 304 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `automobiles`, `trucks`, `vegetables`, `furniture`, `roads`, `pavement`, `chassis`, `walls`, `gravel`, `terrace`, `buckets`, `floor`; extremes include `cassette`, `curb`, `rails`, `dishes`, `roofs`, `blankets`, `Gates`. |
| C6 | 289 | Administration and beneficiaries mixed with monarchy, religion and political identity | mixed | Moderate | `administrators`, `beneficiaries`, `palace`, `king`, `warriors`, `emperor`, `chapel`, `liberals`, `Sultan`, `USSR`, `church`, `Americans`; extremes include `Executive`, `Interior`, `Uncle`, `Africans`, `Stalin`. |
| C7 | 222 | Negative/intense evaluation, alarm and detriment | semantic/topic | High | `disastrous`, `revolutionary`, `spectacular`, `incredible`, `detrimental`, `frightening`, `unbelievable`, `alarming`, `stupid`, `disadvantages`, `glorious`, `arrog`; extremes include `harsh`, `insult`, `supreme`, `choked`, `detriment`. |
| C8 | 161 | Multilingual/encoding fragments and punctuation/tokenisation residue | formatting/tokenizer | High | 86 of 161 tokens are punctuation or symbols; Arabic, Chinese, Japanese and replacement-character fragments coexist with bracket/quote strings, underscores and percent notation. |
| C9 | 114 | Numeric strings, especially historical years | numeric | High | Dominated by `170`, `160`, `856`, `1921`, `451`, `1920`, `thousand`, `140`, `1919`, `056`, `447`, `1910`; extremes include `1939`, `1840`, `Forty`, `666`. |
| C10 | 99 | Geographic entities, regions and place-name fragments | named-entity | High | `Alabama`, `Georgia`, `Florida`, `Louisiana`, `Missouri`, `Arkansas`, `Canada`, `Mexico`, `Oklahoma`, `Memphis`; extremes include `Illinois`, `Alabama`, `Georgia`, `Canada`, `Arkansas`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 1 |
| named-entity | 2 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- exploration, characterisation and developmental/process activity;
- measurement, interaction and computational/organisational analysis;
- navigation/software/platform management and layout concepts;
- food/leisure/shopping/affect;
- biomedical/pharmacological/infant-health terminology;
- anticipation/emergence and evaluative descriptors;
- entrepreneurship/research/media/business activity;
- acknowledgement/greeting/thanks language;
- names and geography;
- common grammar and lexical fragments;
- emergence/freshness/reappearance stem families;
- formatting;
- numeric strings.

Eight of thirteen communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, one named-entity, one
formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- names and geographic entities;
- encouragement/prohibition/removal/legal constraint;
- cardiovascular/cytokine biomedical pathology;
- administrative/configuration/constitutional concepts;
- vehicles, roads and physical/material objects;
- administration mixed with monarchy/religion/political identity;
- negative/intense evaluation and detriment;
- grammar and multilingual lexical fragments;
- multilingual/tokenizer residue;
- numeric strings.

Five of eleven communities receive a primary `semantic/topic`
classification. Two are named-entity, one lexical/morphological, one mixed,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C5** — navigation/software-platform terms overlap with dimensions,
  management and writing/interface concepts;
- **positive C6** — food/leisure/retail and affective/recreational vocabulary
  coexist;
- **positive C8** — anticipation/emergence overlaps with temporal and
  evaluative descriptors;
- **positive C9** — semantic stem families are visible, but incomplete word form
  is the dominant organising feature;
- **negative C0** — names dominate but short lexical fragments are substantial;
- **negative C4** — administrative, constitutional and descriptive concepts
  form a broad partition;
- **negative C5** — several physical-world object classes share one broad
  partition;
- **negative C6** — administrative, monarchic, religious and political
  identities coexist;
- **negative C8** — multilingual encoding residue and symbol formatting are
  interleaved.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
