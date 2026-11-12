# R009 State 10 — block 9 output

## State identity

- R008 state index: `10`
- R008 state label: `block_09_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 13 | 13 | reconciled |
| negative_tail | 14 | 14 | reconciled |
| **Total** | **27** | **27** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 408 | Psychology/social relations mixed with politics, transactions and employment | mixed | Moderate | `psychological`, `psychosocial`, `conversations`, `motivational`, `environmentally`, `professionally`, `culturally` coexist with `transactions`, `determinations`, `Political`; extremes include `employment`, `fellowship`, `stake`, `bidding`, `Business`, `games`. |
| C1 | 388 | Investigation, research, management and task/process actions | semantic/topic | High | `making`, `investigations`, `Working`, `management`, `resolving`, `investigative`, `initiating`, `requesting`, `research`, `getting`, `walking`, `researching`; extremes include `seeking`, `uploads`, `keeping`, `solved`, `travelled`. |
| C2 | 361 | Biomedical, immune, cellular and pharmacological terminology | semantic/topic | High | `immunosuppressive`, `immunodef`, `biodegrad`, `conformational`, `glucocortic`, `intracellular`, `antipsych`, `dexamethasone`, `inflammatory`, `transmembrane`, `proliferative`; extremes include `mitotic`, `antifungal`, `rheumatoid`, `regeneration`. |
| C3 | 360 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `is`, `at`, `have`, `A`, `am`, `and`, `a`, `where`, `found`, together with fragments such as `ir`, `ines`; extremes remain mainly short fragments and malformed forms. |
| C4 | 254 | Cities, countries, nationalities and personal/place names | named-entity | High | `Charleston`, `Stockholm`, `Springfield`, `Atlanta`, `Mumbai`, `Brooklyn`, `Berlin`, `Nigerian`, `Sri`, `Indonesian`, `Egyptian`, `Sacramento`; extremes include `Salvador`, `Gary`, `metropolitan`. |
| C5 | 242 | Telecommunications, databases, web/UI and software systems | semantic/topic | High | `telecommunications`, `mysql`, `DB`, `MySQL`, `createElement`, `findViewById`, `BytePtrFromString`; extremes include `sizeof`, `Entry`, `Views`, `getElementById`, `Permission`, `Forms`, `Hash`. |
| C6 | 190 | Short technical/scientific abbreviations and measurement tokens | lexical/morphological | High | Dominated by short forms such as `µm`, `HA`, `Tri`, `MH`, `NE`, `HS`, `KC`, `BE`; extremes include `BD`, `NAS`, `nM`, `CRM`, `WN` and `BOX`. |
| C7 | 178 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 134 of 178 tokens are punctuation or symbols; examples include `""))`, `))))`, `)}}`, `))).`, closing delimiters and repeated equals-sign strings. |
| C8 | 163 | Multilingual, malformed and fragmentary tokenisation residues | formatting/tokenizer | High | Replacement characters, multilingual fragments and short partial forms such as `remem`, `delic`, `fet`, `prem`, `exem`, `Indust`; extremes remain malformed or fragmentary. |
| C9 | 141 | Food/cuisine mixed with literature, leisure and biological material | mixed | Moderate | `coffee`, `rice`, `Coca`, `foods`, `literary`, `washing`, `theat`, `culinary`, Shakespeare fragment, `fungal`; extremes include `resorts`, `breakfast`, `Casino`, `calorie`, `Chocolate`, `mating`. |
| C10 | 108 | Interactions, coupling and dynamical/physical-system relations | semantic/topic | High | `interactions`, `renormalization`, `interacting`, `coupling`, `relations`, `activities`, `response`, `responses`, `actions`, `Lagrangian`; extremes include `Spin`, `active`, `corrections`, `cyclo`, `answer`. |
| C11 | 86 | Numeric strings, including years | numeric | High | Dominated by `596`, `598`, `597`, `574`, `714`, `595`, `599`, `603`, `796`, `586`, `79`, `373`; extremes include `1997`, `2019`, `737`, `614`, `537`. |
| C12 | 84 | Temporal/sequential, freshness and comparative descriptors | semantic/topic | Moderate | `Following`, `Day`, `Alternatively`, `Using`, `Having`, `sprang`, `Next`, `freshly`, `Subsequently`, `Fresh`, `Afterwards`, `wider`; extremes include `refreshing`, `seasonal`, `Week`, `oldest`, `cheaper`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 492 | Characteristics/evaluation mixed with adversity, constraints and quantitative description | mixed | Moderate | `Characteristics`, `unconstitutional`, `horrific`, `environments`, `catast`, `unreasonable`, `disappointing`, `concepts`, `discriminatory`, `disast`; extremes include `Features`, `variability`, `covariance`, `circumstance`, `departure`, `conclusive`. |
| C1 | 363 | Personal names mixed with geographic/media/name-like entities | named-entity | Moderate | `Lucy`, `Luc`, `Murphy`, `Jon`, `Claud`, `Hicks`, `Dav` coexist with `province`; extremes include `Violet`, `Turk`, `Lucas`, `Telegraph`, `Mirror`, `borough`. |
| C2 | 328 | Common grammatical/function words, punctuation and lexical fragments | lexical/morphological | High | `not`, `or`, `say`, plus fragments and symbols such as `o`, `ized`, `up`, `B`; extremes include `WHAT`, `que`, `HOW`, `ancers`, `asked`, `measure`. |
| C3 | 317 | Built environment, geography, religion/institutions and conflict | mixed | Moderate | `Cathedral`, `hallway`, `sidewalk`, `priest`, `mountains`, `Archbishop`, `trucks`, `fireplace`, `automobiles`, `Constitution` coexist with `warriors`, `disasters`; extremes include `Devil`, `Territory`, `creature`, `roads`, `Highway`, `Empire`. |
| C4 | 261 | Prohibition, exclusion, destruction and removal | semantic/topic | High | `prohibiting`, `eliminating`, `destroyed`, `prohibit`, `destroys`, `includes`, `exclude`, `kill`, `prohibited`, `prohibits`, `murders`, `depicts`; extremes include `Delete`, `shots`, `creates`, `reject`, `CLUDE`. |
| C5 | 233 | Software, compiler, interface and low-level technical systems | semantic/topic | High | `notification`, `compiler`, `initialization`, `dashboard`, `Sig`, `Hex`; extremes include `CI`, `signal`, `glyph`, `HW`, `logs`, `DP`, plus short technical codes. |
| C6 | 222 | Negative/contrastive word stems and multilingual lexical fragments | lexical/morphological | High | `discour`, `comp`, `abol`, `disg`, `cont`, `obliter`, `abrog`, `incomp`; extremes include `crypt`, `Lith`, `png`, multilingual fragments and short stems. |
| C7 | 161 | Numeric strings, especially historical years | numeric | High | Dominated by `1884`, `1880`, `1882`, `1890`, `1921`, plus shorter values; extremes include `1840`, `1890`, `1100`, `900`, `841`, `490`. |
| C8 | 157 | Users, consumers, passengers and social/authority roles | semantic/topic | Moderate | `customers`, `guards`, `users`, `passengers`, `subscriber`, `consume`, `enthusiasts`, `thieves`, `officials`, `captain`; extremes include `Chair`, `broadcasts`, `aides`, `buyer`, `subscribers`, `hazards`. |
| C9 | 149 | Mathematics/geometry mixed with technical/physical objects | mixed | Moderate | `geometry`, `algebra`, `anisotropy`, `subset` coexist with `emitter`, `LED`, `rifles`, `cartridges`, `colors`, `barrel`; extremes include `quotient`, `cylinder`, `zero`, `codec`, `emit`, `quadrant`. |
| C10 | 132 | Clinical diagnostics, anatomy and pathology | semantic/topic | High | `echocardiography`, `angiography`, `pelvis`, `dysfunction`, `epithelium`, `thighs`, `physiology`, `forearm`, `neuropath`, `torso`; extremes include `erythrocytes`, `femur`, `NRAS`, `embryo`. |
| C11 | 102 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 94 of 102 tokens are punctuation or symbols; examples include bracket/operator strings, ellipses, percent/dollar notation and repeated mathematical delimiters. |
| C12 | 93 | Astronomy/cosmology mixed with multilingual world-language terms | mixed | Moderate | `Universe`, `universe`, `photometric`, `planets` coexist with multilingual forms `sempre`, `guerra`, `mundo`, `monde`, `apenas`, `jamais`; extremes include `Kepler`, `spacecraft`, `Jupiter` fragment and `Universe`. |
| C13 | 85 | Intensity, shouting, screaming and manner adverbs | semantic/topic | High | `drastically`, `screams`, `effectively`, `scream`, `violently`, `shouted`, `yelled`, `loudly`; extremes include `louder`, `speakers`, `screamed`, `audible`, `speaker`, `shine`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- psychological/social and institutional/economic material;
- investigation/research/task actions;
- biomedical/immune/cellular terminology;
- telecommunications and software systems;
- interactions/coupling/physical-system relations;
- temporal/sequential and comparative descriptors;
- geography and names;
- food/culture/biological material;
- grammar and word fragments;
- short technical/scientific abbreviations;
- multilingual/tokenizer residues;
- formatting;
- numeric strings.

Five of thirteen communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, two
formatting/tokenizer, one named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- prohibition/exclusion/destruction;
- software/compiler/technical systems;
- users/consumers and social roles;
- clinical diagnostics and anatomy;
- intensity/vocal-expression language;
- evaluation/constraint/quantitative description;
- built environment/religion/conflict;
- mathematics mixed with technical objects;
- astronomy mixed with multilingual language;
- names;
- lexical fragments;
- formatting;
- numeric strings.

Five of fourteen communities receive a primary `semantic/topic`
classification. Four are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — psychological/social, political, transactional and
  employment material coexist;
- **positive C1** — interaction/process, software and physical-science
  structures overlap;
- **positive C9** — food/cuisine, literature/leisure and biological terms
  coexist;
- **positive C12** — temporal/sequential and comparative/freshness language
  overlap;
- **negative C0** — evaluative/adverse and quantitative/characteristic
  structures coexist;
- **negative C1** — personal names coexist with geographic/media entities;
- **negative C3** — built environment, religion/institutions and conflict
  coexist;
- **negative C8** — user/consumer and authority-role terms overlap;
- **negative C9** — mathematical and technical/physical-object structures
  coexist;
- **negative C12** — astronomy/cosmology and multilingual lexical material
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
