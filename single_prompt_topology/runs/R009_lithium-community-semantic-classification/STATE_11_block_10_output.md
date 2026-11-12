# R009 State 11 — block 10 output

## State identity

- R008 state index: `11`
- R008 state label: `block_10_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 14 | 14 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **26** | **26** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 437 | Psychology, investigation and social/professional activity | mixed | Moderate | `negotiating`, `psychosocial`, `investigations`, `conversations`, `psychological`, `therapists`, `determinations`, `psychiat`, `management`, `research`; extremes include `employment`, `fellowship`, `talks`, `Business`, `bidding` and `games`. |
| C1 | 386 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `is`, `at`, `all`, `A`, `am`, `where`, `and`, `back`, `found`, with short fragments and malformed multilingual pieces in the extremes. |
| C2 | 358 | Observation, evaluation, emergence and process/cognitive actions | semantic/topic | High | `initiating`, `observing`, `emerging`, `travelling`, `resolving`, `evaluating`, `motivated`, `experiencing`, `remembering`, `interpreting`, `originates`, `overexpressed`; extremes include `seeking`, `solved`, `informed`, `originating`, `grow`. |
| C3 | 296 | Personal names, cities, nationalities and geographic entities | named-entity | High | `Ken`, `Stockholm`, `Palestinian`, `Berlin`, `Brooklyn`, `Karen`, `Hamburg`, `Johannes`, `German`; extremes include `Greek`, `Gary`, `Mumbai`, `Salvador`, `metropolitan`. |
| C4 | 285 | Neuropharmacology, immunity, cellular biology and oxidative processes | semantic/topic | High | `immunosuppressive`, `dopaminergic`, `antipsych`, `biodegrad`, `neurotrans`, `transmembrane`, `dexamethasone`, `intracellular`, `anticancer`, `immunodef`, `mitochondrial`, `oxidative`; extremes include `mitotic`, `fluores`, `regeneration`, `pulmonary`. |
| C5 | 269 | Interactions, fields, regularisation and mathematical/physical-system structure | semantic/topic | High | `interactions`, `forms`, `renormalization`, `coupling`, `actions`, `regularization`, `action`, `interaction`, `fields`, `Lagrangian`, `interacting`; extremes include `Spin`, `Phase`, `spacing`, `formul`. |
| C6 | 232 | Food, leisure, daily activity and biological/health material | mixed | Moderate | `coffee`, `rice`, `grinned`, `laughed`, `washing`, `malaria`, `amusement`, `fishermen`, `stainless`, `cafe`, `champagne`, `sprang`; extremes include `resorts`, `breakfast`, `Casino`, `beet`. |
| C7 | 226 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 176 of 226 tokens are punctuation or symbols; examples include `}})`, `""))`, `))).`, `)}}`, `))))`, repeated equals signs and long whitespace/delimiter strings. |
| C8 | 195 | Multilingual, malformed and fragmentary tokenisation residues | formatting/tokenizer | High | Replacement characters, multilingual fragments and partial forms such as `sä`, `kä`, `prem`, `exem`, `kunnen`, `ación`; extremes remain fragmentary or malformed. |
| C9 | 195 | Web/software, database and publishing/interface systems | semantic/topic | High | `Acknowledgements`, Django fragment, `BytePtrFromString`, `createElement`, `CONTRIBUTORS`, `WordPress`, `findViewById`, `mysql`, Kubernetes fragment, `MySQL`; extremes include `sizeof`, `uploads`, `getElementById`, `Permission`, `Amazon`, `images`. |
| C10 | 126 | Short technical/scientific abbreviations and measurement tokens | lexical/morphological | High | `HA`, `NE`, `BE`, `db`, `DB`, `BD`, `µm`, `MH`, `EE`, `AA`, `HS`; extremes include `CRM`, `nM`, `mM`, `RAW`, `NF`, `kv`. |
| C11 | 98 | Numeric strings, including years | numeric | High | Dominated by `596`, `597`, `689`, `599`, `697`, `1993`, `324`, `239`, `603`, `1969`, `687`, `496`; extremes include `12345`, `1997`, `2019`, `737`, `505`, `1947`. |
| C12 | 32 | Comparative physical, freshness, temperature and price descriptors | semantic/topic | High | `Fresh`, `wider`, `freshly`, `fresh`, `newer`, `thicker`, `Old`, `inexpensive`, `cheapest`, `extra`, `cold`; extremes include `hot`, `oldest`, `safer`, `cheaper`, `largest`. |
| C13 | 26 | Response, answering, listening and feedback language | semantic/topic | High | `response`, `Response`, `responses`, `responding`, `answering`, `answer`, `listening`, `answered`; extremes include `feedback`, `feed`, `resp`, `responses`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 486 | Personal names mixed with lexical/technical fragments | named-entity | Moderate | `Lucy`, `Molly`, `Blair`, `Claud`, `Hicks`, `Dav`; extremes include `Violet`, `Turk`, `Lucas`, while fragments such as `discour`, `Comp`, `crypt`, `glyph`, `gluc` reduce purity. |
| C1 | 405 | Scientific characteristics, distributions, instrumentation and quantitative description | semantic/topic | High | `Characteristics`, `characteristics`, `environments`, `distributions`, `uniforms`, `technologies`, `uniformity`, `instrumentation`, `circumstance`, `methodologies`, `requirement`; extremes include `Features`, `specificity`, `variance`, `covariance`, `quotient`. |
| C2 | 402 | Negative evaluation, catastrophe, discrimination and vocal distress | semantic/topic | High | `unconstitutional`, `unreasonable`, `circumstantial`, `horrific`, `catast`, `discriminatory`, `disasters`, `whispers`, `scream`, `inaccurate`, `screams`, `catastrophe`; extremes include `harsh`, `louder`, `gloom`, `shots`. |
| C3 | 317 | Common grammatical/function words, punctuation and lexical fragments | lexical/morphological | High | Dominated by `not`, `or`, `I`, `up`, single characters/numbers and fragments such as `ized`; extremes include `ED`, `omes`, `WHAT`, `HOW`, `ancers`, `UV`. |
| C4 | 288 | Social roles, royalty, religion and fictional/authority figures | mixed | Moderate | `warriors`, `queen`, `guards`, `princess`, `users`, `priest`, `Cathedral`, `prince`, `chapel`, `goddess`, `customers`, `girls`; extremes include `throne`, `speakers`, `creature`, `Devil`, `Doll`, `Universe`. |
| C5 | 251 | Roads, transport, built environment and natural landscape | semantic/topic | High | `hallway`, `trucks`, `sidewalk`, `automobiles`, `roadway`, `mountains`, `dashboard`, `roads`, `truck`, `lake`, `woods`, `corridor`; extremes include `barrel`, `cylinder`, `roofs`, `shores`, `Highway`, `cliffs`, `fence`, `curb`. |
| C6 | 248 | Prohibition, elimination, destruction and creation/change actions | semantic/topic | High | `prohibiting`, `eliminating`, `destroys`, `Delete`, `includes`, `destroyed`, `prohibited`, `prohibits`, `emphasizing`, `kill`, `Create`, `depicts`; extremes include `Creator`, `creates`, `reject`, `subtracting`. |
| C7 | 181 | Multilingual words, suffixes and orthographic fragments | lexical/morphological | High | `cette`, `questa`, `Qué`, `ça`, `sempre`, `que`, `cela`, `apenas`, `Une`, together with Cyrillic and East Asian fragments; extremes remain multilingual/orthographic. |
| C8 | 155 | Numeric strings, especially historical years | numeric | High | `1884`, `1890`, `1870`, `1850`, `1921`, `1882`, `1860`, `1881` plus shorter values; extremes include `1840`, `1830`, `407`, `448`. |
| C9 | 145 | Clinical diagnostics, cardiovascular medicine and anatomy/pathology | semantic/topic | High | `echocardiography`, `physiology`, `cardiovascular`, `angiography`, `dysfunction`, `epidemiological`, `epithelium`, `carcinoma`, `Disease`, `thighs`; extremes include `femur`, `erythrocytes`, `trunk`, `opathy`. |
| C10 | 99 | Geography, government, law and civic/public entities | mixed | Moderate | `Constitution`, `citizens`, `Edinburgh`, `Scotland`, `Connecticut`, Barcelona fragment, `Newcastle`, `province`, `Montreal`, `Romania`, `provisions`; extremes include `Territory`, `Clause`, `Illinois`, `Herald`, `enactment`. |
| C11 | 83 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 78 of 83 tokens are punctuation or symbols; examples include bracket/operator strings, percent notation, ellipses, repeated symbols and line/dash characters. |

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

- psychology, investigation and social/professional activity;
- observation/evaluation and process/cognitive actions;
- neuropharmacology, immunity and cellular biology;
- interactions, fields and physical/mathematical systems;
- web/software and database systems;
- response/answer/feedback language;
- comparative physical and price descriptors;
- food/leisure/daily-life material;
- names and geography;
- grammar and lexical fragments;
- technical/scientific abbreviations;
- multilingual/tokenizer residues;
- formatting;
- numeric strings.

Six of fourteen communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, two
formatting/tokenizer, one named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- scientific characteristics, instrumentation and quantitative description;
- negative evaluation/catastrophe/vocal distress;
- roads, transport and physical environment;
- prohibition/elimination/destruction;
- clinical diagnostics and cardiovascular medicine;
- names;
- social/religious/royal/fictional roles;
- geography/government/law;
- grammatical and multilingual lexical fragments;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity, one
formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — psychological/research material overlaps with employment,
  business and social activity;
- **positive C6** — food/leisure/daily-life and health/biological terms coexist;
- **positive C9** — software/web/database and publishing/paratext terms overlap;
- **negative C0** — names dominate but lexical and technical fragments are
  substantial;
- **negative C4** — royalty, religion, social roles and fictional figures
  coexist;
- **negative C10** — geographic/civic entities and legal/government concepts
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
