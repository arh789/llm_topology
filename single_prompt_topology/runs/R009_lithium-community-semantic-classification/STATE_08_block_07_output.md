# R009 State 08 — block 7 output

## State identity

- R008 state index: `8`
- R008 state label: `block_07_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 13 | 13 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **25** | **25** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 446 | Work, management, access and task/process actions | semantic/topic | High | `travelling`, `Working`, `initiating`, `management`, `accessing`, `formatted`, `researching`, `giving`, `withdrawing`, `walking`; extremes include `seeking`, `Reading`, `solved`, `recognized`, `resolving`, `remembers`, `Managed`. |
| C1 | 429 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `is`, `of`, `have`, `at`, `A`, `all`, `am`, `and`, `like`, together with fragments such as `en`, `et`; extremes include short abbreviations and fragments. |
| C2 | 377 | Biomedical, psychological, immune and inflammatory terminology | semantic/topic | High | `immunosuppressive`, `neurodegenerative`, `psychosocial`, `Psychological`, `psychological`, `immunodef`, `angiotensin`, `inflammatory`, `psychiatric`, `glucocortic`, `emotional`, `antipsych`; extremes include `mitotic`, `rheumatoid`, `regeneration`. |
| C3 | 364 | Geography and nationality mixed with politics, culture and sport | mixed | Moderate | `Pakistani`, `Indonesian`, `Atlanta`, `Sacramento`, `Charleston`, `Nigerian`, `Mumbai`, `Australian` coexist with `Political`, `cultural`, `basketball`; extremes include `Civil`, `Social`, `Cultural`, `Championships`, `games`. |
| C4 | 330 | Multilingual, malformed and fragmentary tokenisation residues | formatting/tokenizer | High | Replacement characters, short fragments and multilingual pieces such as `enen`, `Inter`, `Lif`, `Ju`, `Gö`, `Tra`; extremes remain fragmentary or malformed with no stable topic. |
| C5 | 305 | Databases, data processing and software/information systems | semantic/topic | High | `DB`, `Database`, `mysql`, `MySQL`, `Connection`, `Processing`, `SQL`, `BytePtrFromString`, `Relations`; extremes include `Hash`, `Entry`, `connections`, `Cyber` and `sizeof`. |
| C6 | 237 | Molecular/physical science, dynamical systems and structural form | semantic/topic | Moderate | `conformational`, `renormalization`, `molecule`, `dynamical`, `hierarchical`, `chemical`, `loop`, `interacting`, `complexes`; extremes include `Spin`, `cycle`, `carbon`, `Forms`, `spacing`. |
| C7 | 213 | Finance, employment, business and organisational activity | semantic/topic | High | `Financial`, `activities`, `Employment`, `Employ`, `development`, `organizing`, `lending`, `business`, `financial`; extremes include `employment`, `fellowship`, `fellows`, `Role`, `response`. |
| C8 | 174 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 148 of 174 tokens are punctuation or symbols; examples include `}})`, `""))`, `))).`, `)}}`, `))))`, repeated equals signs and long whitespace strings. |
| C9 | 115 | Social, cultural, temporal and discourse/adverbial language | semantic/topic | Moderate | `emotionally`, `Eventually`, `culturally`, `Anyway`, `Alternatively`, `electronically`, `Subsequently`, `socially`, `professionally`; extremes include `OK`, `personalized`, `Thank`, `References`, `HOWEVER`, `inevitable`. |
| C10 | 107 | Numeric strings, including years | numeric | High | Dominated by values such as `373`, `598`, `593`, `603`, `599`, `173`, `586`, `1993`, `1969`, `574`, `595`; extremes include `2013`, `2019`, `409`, `176`, `573`, `12345`. |
| C11 | 89 | Food, crops, cuisine and animals | semantic/topic | High | `rice`, `food`, `foods`, `Veget`, `chocolate`, `coconut`, `Chocolate`, `culinary`, `spinach`, `cabbage`, `insects`, `pig`; extremes include `beet`, `curry`, `mating`, `Bear`, `worm`, `breakfast`. |
| C12 | 28 | Prefixes and opposition/novelty word-form families | lexical/morphological | High | Dominated by `Anti`, `anti`, `antid`, `antib`, `antis`, `neo`, `pseudo`, `cyber`, plus `counter`, `cis`, `multid` and related partial forms. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 7 |
| lexical/morphological | 2 |
| named-entity | 0 |
| formatting/tokenizer | 2 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 632 | Personal names mixed with negative/contrastive lexical stems | mixed | Moderate | Strong name content includes `Nick`, `Liz`, `Lucy`, `Sarah`, `Freder`, `Alex`, `Brad`, while `catast`, `brilli`, `disast`, `unmist`, `gluc` and extremes such as `displ`, `comp`, `neglig` form a substantial lexical-stem component. |
| C1 | 415 | Analysis, assessment, scientific description and recommendations | semantic/topic | High | `determination`, `assessments`, `Characteristics`, `analysis`, `manifestations`, `environments`, `phenotypes`, `technologies`, `recommendations`, `Notification`, `prohibited`; extremes include `variability`, `robustness`, `Features`, `covariance`, `usage`. |
| C2 | 412 | Religious, institutional, cultural and fictional/social roles/places | mixed | Moderate | `Archbishop`, `priest`, `Cathedral`, `concerts`, `Constitution`, `Palace`, `Princess`, `Smith`, `producer`, `monsters`; extremes include `Chair`, `Devil`, `speakers`, `thief`, `officials`, `creature`, `broadcasts`, `Rabbi`, `police`. |
| C3 | 382 | Common grammatical/function words, suffixes and lexical fragments | lexical/morphological | High | Dominated by `not`, `if`, `or`, `up`, with fragments `ia`, `ie`, `ized`, `el`; extremes include `que`, `WHAT`, `HOW`, `ues`, `omes`, `unit`. |
| C4 | 304 | Negative evaluation, distress, tragedy and intense affect | semantic/topic | High | `disappointment`, `unconstitutional`, `tragedy`, `horrific`, `unacceptable`, `indistinguishable`, `stunning`, `scream`, `discriminatory`, `sadness`, `terrifying`; extremes include `gloom`, `screamed`, `shouted`, `audible`, `yelled`. |
| C5 | 266 | Destruction, removal, construction and compositional change | semantic/topic | High | `destroys`, `destroyed`, `removed`, `dropped`, `murders`, `creating`, `eliminated`, `murdered`, `depicts`, `contains`, `combines`, `constructing`; extremes include `Delete`, `displacement`, `creates`, `independent`. |
| C6 | 220 | Built environment, terrain, transport, weapons and physical objects | semantic/topic | Moderate | `hallway`, `staircase`, `stairs`, `guns`, `mountains`, `trucks`, `corridor`, `gown`, `cliffs`, `boats`, `tube`, `wavelengths`; extremes include `barrel`, `nozzle`, `spacecraft`, `roads`, `tiles`, `Gates`. |
| C7 | 143 | Low-level computing, hardware and abbreviated technical tokens | semantic/topic | Moderate | `GCC`, `compiler`, `LED`, `hw`, `GPIO`, `FFFF`; extremes include `drv`, `png`, `sdk`, `compiler`, `Decoder`, `HW`, `debug`, alongside short letter codes. |
| C8 | 138 | Clinical diagnostics, anatomy and pathology | semantic/topic | High | `echocardiography`, `pathophysiology`, `abdomen`, `angiography`, `microscopy`, `cerebellum`, `pelvis`, `physician`; extremes include `erythrocytes`, `allele`, `NRAS`, `torso`, `dysplasia`, `therapy`, `degeneration`. |
| C9 | 134 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 121 of 134 tokens are punctuation or symbols; examples include bracket/operator strings, percent notation, repeated punctuation and mathematical delimiters. |
| C10 | 110 | Numeric strings, especially historical years | numeric | High | `1882`, `1900`, `1880`, `1890`, `1860`, `1870` plus three- and four-digit values; extremes include `1848`, `1850`, `1840`, `0070`. |
| C11 | 55 | Abstract algebra and mathematical notation | semantic/topic | High | `omorphisms`, `bigoplus`, `homomorphism`, `maps`, `homogeneous`, `algebra`, `diag`, `morphisms`, `uniform`, `bigcup`; extremes include `quotient`, `subset`, `zero`, `nonzero`, `bounded`, `periodic`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 7 |
| lexical/morphological | 1 |
| named-entity | 0 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- work, management and task/process actions;
- biomedical/psychological/immune terminology;
- databases and software/data processing;
- molecular and physical science;
- finance, employment and business;
- social/cultural/discourse language;
- food, crops and animals;
- geography/nationality plus political/cultural/sport material;
- grammar and lexical fragments;
- prefix/word-form families;
- multilingual/tokenizer residues;
- formatting;
- numeric strings.

Seven of thirteen communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, two formatting/tokenizer, one
mixed and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- analysis/assessment/scientific description;
- negative affect and tragedy;
- destruction/removal/compositional change;
- built environment and physical objects;
- low-level computing;
- clinical diagnostics and anatomy;
- abstract algebra;
- names mixed with lexical stems;
- religious/institutional/fictional roles;
- grammatical fragments;
- formatting;
- numeric strings.

Seven of twelve communities receive a primary `semantic/topic`
classification. Two are mixed, one lexical/morphological, one
formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C3** — geography/nationality, politics/culture and sport coexist;
- **positive C6** — molecular/physical-science and structural/form terms span a
  broad domain;
- **positive C9** — social, cultural, temporal and discourse/adverbial forms
  overlap;
- **negative C0** — names and negative/contrastive lexical stems are both
  substantial;
- **negative C2** — religious, institutional, cultural and fictional/social
  roles coexist;
- **negative C6** — built-environment, terrain, weapons and technical objects
  share a broad physical-world structure;
- **negative C7** — computing semantics are evident but short letter-code
  structure adds lexical noise.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
