# R009 State 19 — block 18 output

## State identity

- R008 state index: `19`
- R008 state label: `block_18_output`
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
| C0 | 474 | Personal names and geographic/name-like entities | named-entity | Moderate | `Scott`, `Manchester`, `Karen`, `Matt`, `Mitchell`, `Hamburg`, `Jay`, `Ben`, `Josh`, `Bennett`; extremes include `Berlin`, `Kumar`, `Krish` and name fragments. `terrorists` is a notable semantic outlier. |
| C1 | 364 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `am`, with suffixes/fragments such as `ation`, `ating`, `le`, `ine`, `it`, `l`, `id`; extremes include `ausing`, `ilation`, `med`, `Sort`, `Back`. |
| C2 | 339 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 201 of 339 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `mathchoice`, `javase`, `Caption`, `leq` and symbolic fragments. |
| C3 | 311 | Exploration, anticipation, development and inferential/process actions | semantic/topic | High | `exploring`, `characterizing`, `anticipated`, `evolves`, `discuss`, `adventures`, `explores`, `development`, `yields`, `anticipation`, `builds`; extremes include `informed`, `recall`, `derives`, `sensing`, `anticip`. |
| C4 | 281 | Transformations, measurements, interactions and quantitative/computational analysis | semantic/topic | High | `transformations`, `Measurements`, `interactions`, `sessions`, `Measurement`, `conversations`, `quantification`, `computations`, `interviews`, `negotiating`, `results`, `simulations`; extremes include `interaction`, `interacting`, `Geometry`, `tension`. |
| C5 | 278 | Biomedical, hospital, psychiatric and pharmacological terminology | semantic/topic | High | `breastfeeding`, hospital fragments, `dexamethasone`, `psychiat`, `periodontal`, `hospital`, `Medical`, `dopaminergic`, `mosquitoes`, `salivary`; extremes include `µm`, `fluores`, `Lung`, `airborne`, `Bio`. |
| C6 | 254 | Media, creative work, business and online-platform activity | semantic/topic | Moderate | `entrepreneurs`, `filmmakers`, `Notification`, `photography`, `filmmaker`, `business`, `Netflix`, pamphlet fragment, `collaborators`, `facebook`, `fishermen`, `writers`; extremes include `recorder`, `director`, `ajax`, `Bibliography`. |
| C7 | 180 | Prefix/stem families around inevitability, regeneration, reappearance and interpretation | lexical/morphological | Moderate | Dominated by incomplete forms such as `inev`, `unavoid`, `controvers`, `unve`, `maneu`, `reappe`, `conjug`, `Numer`, `Estim`; extremes remain mostly partial lexical forms such as `estim`, `aberr`, `nuest`, `prem`. |
| C8 | 156 | Wellbeing, affect, consumption and hospitality/lifestyle concepts | semantic/topic | Moderate | `Food`, `motivation`, `shoppers`, `mindfulness`, `happiness`, `discomfort`, `celebrating`, `shops`, `compassion`, `hospitality`, `rooms`, `consciousness`; extremes include `Tours`, `resorts`, `camping`, `booking`. |
| C9 | 140 | Numeric strings and short coded values | numeric | High | Dominated by `302`, `296`, `298`, `597`, `297`, `306`, `325`, `324`, `697`, `334`; extremes include `12345`, `473`, `2004`, `505`, `633`, `0023`. |
| C10 | 75 | Evaluative, analytical and qualification/adverbial language | semantic/topic | Moderate | `surprisingly`, `analytically`, `Clearly`, `numerically`, `experimenting`, `famously`, `clinically`, `peaceful`, `fraudulent`, `questionable`, `suitably`; extremes include `customary`, `obvious`, `Notable`. |
| C11 | 72 | Comparative size, age, freshness and physical-dimension descriptors | semantic/topic | High | `fres`, `Fresh`, `larger`, `older`, `clearer`, `wider`, `Size`, `happier`, `widths`, `Length`; extremes include `fresh`, `smallest`, `heating`, `illuminating`. |
| C12 | 43 | Example-related words and morphological fragments | lexical/morphological | High | `exempl`, `ejemplo`, `Examples`, `Example`, `examples`, `exem`, `Samples`, `exemplified`; extremes include `example`, `emplo`, `outputs`, `atas`, `uesta`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 7 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 0 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 403 | Constitutional/regulatory constraint and adverse evaluative language | semantic/topic | High | `circumstantial`, `unconstitutional`, `circumstances`, `encouragement`, `Constitution`, `discriminatory`, `prohibiting`, `circumferential`, `resembled`, `Comprehensive`, `occasionally`; extremes include `affirmative`, `enactment`, `disadvantages`, `submit`, `discour`. |
| C1 | 362 | Administrative characterisation, configuration and recommendation systems | semantic/topic | High | `Characteristics`, `recommendations`, `downregulation`, `Configuration`, `administrators`, `characteristics`, `Specific`, `representation`, `regulations`, `administrator`; extremes include `variance`, `Executive`, `privileges`, `availability`, `specificity`. |
| C2 | 345 | Personal names and name-like entities | named-entity | High | `Laura`, `Caroline`, `Sarah`, `Catherine`, `Claire`, `Emily`, `Connie`, `Tah`; extremes include `Violet`, `Maur`, `Friedrich`, with several short lexical fragments. |
| C3 | 284 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `different`, `THIS`, with fragments `ED`, `ra`, `ET`, `RA`, `CE`, `ABLE`, `ALLY`; extremes include `cette`, `Une`, Cyrillic fragments and `HOW`. |
| C4 | 280 | Government/monarchy, geography and family/social institutions | mixed | Moderate | `palace`, `cathedral`, `Alabama`, `grandmother`, `emperor`, `warriors`, `archaeological`, `bureaucracy`, `Florida`, `king`, `Americans`; extremes include `Uncle`, `USSR`, `Universe`, `Africans`. |
| C5 | 212 | Negative/intense evaluation, fear, incompetence and accusation | semantic/topic | High | `incredible`, `disastrous`, `unbelievable`, `stupid`, `brutal`, `screamed`, `frightening`, `incompetent`, `sinister`, `contradictory`, `accusation`; extremes include `harsh`, `supreme`, `excessive`, `choked`, `Excellent`. |
| C6 | 195 | Cardiovascular disease, cytokine biology and biomedical pathology | semantic/topic | High | `cardiovascular`, `cytokine`, `atherosclerotic`, `interleukin`, sclerosis fragment, `epidemiological`, `erythrocytes`, `supernatant`, `TNF`, `Zn`, `lipids`; extremes include `monocyte`, `gluc`, `thrombosis`, `Fc`. |
| C7 | 194 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `trucks`, `chassis`, `cylinder`, `automobiles`, `roads`, `vegetables`, `gravel`, `uniforms`, `furniture`, `Mountains`, `sidewalk`, `pavement`; extremes include `curb`, `dishes`, `roofs`, `ignition`, `blankets`, `pickup`. |
| C8 | 164 | Short technical/computing abbreviations and code-like fragments | lexical/morphological | Moderate | `TC`, `TG`, `Rails`, `GH`, `COMP`, `ACC`, `LCD`, `Enc`, `Disc`; extremes include `crypt`, `CI`, `cassette`, `SSH`, `PROT`, `CPU`, `rails`. |
| C9 | 145 | Multilingual/encoding fragments and punctuation/tokenisation residue | formatting/tokenizer | High | Dominated by Arabic, Japanese, Chinese and replacement-character fragments mixed with bracket/quote strings; 73 tokens are punctuation or symbols. Extremes include `displaystyle`, repeated underscores, percent notation and multilingual characters. |
| C10 | 85 | Numeric strings, especially historical years | numeric | High | Dominated by `1921`, `441`, `178`, `448`, `175`, `451`, `1860`, `476`, `651`, `0059`, `160`; extremes include `1919`, `1939`, `1890`, `1840`, `1957`, `666`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- exploration/anticipation/development processes;
- transformations, measurements and quantitative/computational analysis;
- biomedical/hospital/psychiatric terminology;
- media, creative work and online/business activity;
- wellbeing, affect, consumption and hospitality;
- evaluative/analytical modifiers;
- comparative size/freshness descriptors;
- names and geography;
- grammar and lexical fragments;
- example-related morphology;
- formatting;
- numeric strings.

Seven of thirteen communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one named-entity, one
formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- constitutional/regulatory and adverse evaluative language;
- administrative/configuration/recommendation systems;
- negative/intense evaluation and fear;
- cardiovascular/cytokine biomedical pathology;
- vehicles, roads and material objects;
- government/monarchy/geography/family institutions;
- names;
- grammatical and technical lexical fragments;
- multilingual/tokenizer residue;
- numeric strings.

Five of eleven communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, one named-entity, one mixed,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — names dominate but a few semantic and fragmentary outliers
  remain;
- **positive C6** — media/creative, business and software/publishing terms
  overlap;
- **positive C8** — affect/wellbeing overlaps with consumption, hospitality and
  travel/lifestyle vocabulary;
- **positive C10** — analytical/evaluative adverbs overlap with ethical/legal
  descriptors;
- **negative C2** — names dominate but short fragments remain substantial;
- **negative C4** — government, monarchy, geography and family/social
  institutions coexist;
- **negative C7** — multiple physical-world object classes share one broad
  partition;
- **negative C8** — technical semantics are evident but abbreviated form is the
  dominant organising feature;
- **negative C9** — multilingual encoding residue and symbol formatting are
  interleaved.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
