# R009 State 06 — block 5 output

## State identity

- R008 state index: `6`
- R008 state label: `block_05_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 13 | 13 | reconciled |
| negative_tail | 13 | 13 | reconciled |
| **Total** | **26** | **26** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 409 | Databases, data handling, transactions and information systems | semantic/topic | High | `mysql`, `DB`, `formatted`, `transactions`, `Database`, `MySQL`, `BytePtrFromString`, `response`; extremes include `Form`, `Role`, `Views`, `Hash`, `Forms` and `spacing`. |
| C1 | 347 | Multilingual, malformed and fragmentary lexical residues | formatting/tokenizer | High | Replacement characters, Thai script and short fragments such as `immedi`, `Rel`, `neo`, `Ar`, `Par`, `Car`, `Tra`; extremes are likewise malformed or fragmentary. |
| C2 | 346 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | `of`, `is`, `was`, `have`, `all`, `and`, `like`, `am` mixed with fragments such as `en`, `et`, `ro`; extremes are predominantly fragments and short forms. |
| C3 | 306 | Task, access, work and information-handling actions | semantic/topic | High | `travelling`, `initiating`, `accessing`, `Working`, `Having`, `giving`, `extracted`, `maintaining`, `withdrawing`, `Using`; extremes include `seeking`, `solved`, `resolving`, `recognized`, `referenced`. |
| C4 | 306 | Biomedical science mixed with physical-science concepts | mixed | Moderate | `immunosuppressive`, `neurodegenerative`, `conformational`, `glucocortic`, `inflammatory`, `metabolic`, `substances`, `rheumatoid` coexist with `renormalization`, `Spin`, `carbon`, `surfaces`, `Gas`, `coherence`. |
| C5 | 278 | Psychology/social life mixed with politics, finance and sport | mixed | Moderate | `psychosocial`, `psychological`, `political`, `communities`, `emotional`, `parliamentary`, `financial`, `reimbursement`, `basketball`, `psychiat`; extremes include `administrative`, `Civil`, `employment`, `Social`, `games`, `lending`. |
| C6 | 237 | Cities, countries, nationalities and personal/place names | named-entity | High | `Indonesian`, `Nigerian`, `Chicago`, `Atlanta`, `Sacramento`, `Laura`, `Orlando`, `California`, `Charleston`, `Cleveland`, `Charlotte`, `Chinese`; extremes include `Thai`, `Canadian`, `Salvador`, `Sri`. |
| C7 | 230 | Discourse, temporal and evaluative/adverbial language | semantic/topic | Moderate | `Subsequently`, `Eventually`, `Alternatively`, `Anyway`, `professionally`, `Active`, `unsatisfactory`, `Following`; extremes include `refreshing`, `OK`, `active`, `Under`, `nationally`, `HOWEVER`. |
| C8 | 168 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 134 of 168 tokens are punctuation or symbols; examples include `}})`, `))).`, `))))`, `""))`, repeated equals signs and other closing-format strings. |
| C9 | 111 | Acronyms, initialisms and short technical/scientific abbreviations | lexical/morphological | High | Dominated by `PC`, `SC`, `HA`, `BA`, `NF`, `HS`, `CS`, `MC`, `CP`, `DA`, `OC`, `DF`; extremes include `NAS`, `BD`, `ACP`, `LOS`, `NS`. |
| C10 | 99 | Food, nutrition and domestic/agricultural animals | semantic/topic | High | `food`, `feeding`, `cakes`, `Chocolate`, `rice`, `chocolate`, `cabbage`, `foods`, `calorie`, `cat`; extremes add `beet`, `litter`, `worm`, `curry`, `pig`, `coconut`. |
| C11 | 85 | Numeric strings | numeric | High | Dominated by values such as `373`, `598`, `404`, `339`, `599`, `138`, `695`, `499`, `593`, `586`, `84`; extremes are likewise primarily numeric. |
| C12 | 29 | Calendar time, years, weekdays and seasons | semantic/topic | High | `2012`, `January`, `night`, `1993`, `1992`, `1997`, `1975`, `2009`, `1986`; extremes include `2013`, `Week`, `2019`, `months`, `today`, `spring`, `Saturday`. |

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
| C0 | 472 | Personal names and name-like entities | named-entity | High | `Hayes`, `Liz`, `Thompson`, `Murphy`, `Hicks`, `Shapiro`, `Luke`, `Dav`, `John`, `Nick`, `Lucy`; extremes include `Max`, `Turk`, `Claud`, `Kepler`, `Violet`, `Kat`. |
| C1 | 464 | Negative evaluation, adversity, destruction and distress | semantic/topic | High | `disappointment`, `destroys`, `unconstitutional`, `unacceptable`, `destroyed`, `tragedy`, `terrifying`, `indistinguishable`, `Delete`; extremes include `conclusive`, `authority`, `madness`, `sturdy`, `fault`, `news`. |
| C2 | 446 | Analysis and assessment mixed with clinical diagnostics | mixed | Moderate | `Characteristics`, `assessments`, `analysis`, `interpretation`, `descriptions`, `manifestations`, `constructions` coexist with `echocardiography`, `pathophysiology`, `angiography`; extremes include `robustness`, `variability`, `biomarkers`, `covariance`. |
| C3 | 332 | Common grammatical/function words, suffixes and lexical fragments | lexical/morphological | High | `if`, `not`, `or`, `case`, `up`, together with fragments `ia`, `ie`, `el`, `ized`; extremes include `que`, `ues`, `iant`, `omes`. |
| C4 | 311 | Negative/contrastive word stems and incomplete lexical forms | lexical/morphological | High | `brilli`, `catast`, `comp`, `unmist`, `discontin`, `unsatisf`, `arrog`, `imposs`, `abol`, `discour`, `unambig`; extremes include `dilig`, `displ`, `uncon`, `abol`. |
| C5 | 291 | Religious/institutional roles mixed with crime, authority and places | mixed | Moderate | `Archbishop`, `priest`, `priests`, `theolog`, `Constitution`, `technicians`, `officer`, `Palace` coexist with `goddess`, `thief`, `Devil`, `Rabbi`, `officials`, `composer`. |
| C6 | 228 | Built environment and transport mixed with weapons and violence | mixed | Moderate | `staircase`, `hallway`, `boats`, `cliffs`, `guns`, `stair`, `sword`, `stairs`, `trucks`, `corridor` coexist with `murders`, `kill`, `shots`, `barrel`, `nozzle`. |
| C7 | 138 | Anatomy and clinical biology mixed with clothing/body-surface terms | mixed | Moderate | `abdomen`, `cerebellum`, `skull`, `epidermis`, `erythrocytes`, `gluc`, `abdom`, `GFP`, `cardi`, `torso` coexist with `uniforms`, `robe`, `clad`; extremes include `allele`, `SBP`. |
| C8 | 137 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 128 of 137 tokens are punctuation or symbols; examples include bracket/operator strings, `percent`, repeated punctuation and mathematical delimiters. |
| C9 | 106 | Numeric strings, especially historical years | numeric | High | `1882`, `1900`, `1867`, `1860`, `1938`, `1888`, `1870`, plus shorter values; extremes include `1848`, `1830`, `1850` and other numbers. |
| C10 | 95 | Programming, low-level computing and data-stream systems | semantic/topic | High | `hw`, `FFFF`, `compiler`, `databind`, `logs`, `blog`, `Decoder`, `Writer`, `io`, `DAC`, `Stream`; extremes include `drv`, `sdk`, `debug`, `png`, `HW`, `src`. |
| C11 | 83 | Multilingual suffixes and orthographic fragments | lexical/morphological | High | `vý`, `emente`, `qué`, `usamm`, `amente`, `cia`, `ición`, `GmbH`; extremes include `ić`, `lado`, `modo`, `avait`, `č`, `ş`, `î`, `ungs`. |
| C12 | 49 | Abstract algebra and mathematical notation | semantic/topic | High | `omorphisms`, `bigoplus`, `commutative`, `functor`, `homomorphism`, `morphisms`, `subset`, `setminus`, `homogeneous`; extremes include `orphism`, `diag`, `uniform`, `zero`, `quotient`, `bounded`, `nonzero`, `tikz`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 3 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains identifiable structures spanning:

- databases, data handling and transactions;
- task/work/information-handling actions;
- biomedical and physical science;
- psychology, politics, finance and social relations;
- geography and names;
- discourse/evaluative modifiers;
- food, nutrition and animals;
- common grammar and word fragments;
- technical acronyms;
- multilingual/tokenizer residues;
- formatting;
- numeric strings;
- calendar/time structure.

Five of thirteen communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, two
formatting/tokenizer, one named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- adversity and destruction;
- assessment/analysis plus clinical diagnostics;
- programming and low-level computing;
- abstract algebra;
- names;
- religious/institutional/criminal roles;
- built environment plus violence;
- anatomy plus clothing/body-surface terms;
- grammar and lexical fragments;
- multilingual morphology;
- mathematical formatting;
- numeric strings.

Three of thirteen communities receive a primary `semantic/topic`
classification. Four are mixed, three lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C4** — biomedical and physical-science concepts coexist;
- **positive C5** — psychological/social, political, financial and sport terms
  overlap;
- **positive C7** — discourse, temporal and evaluative forms overlap;
- **negative C2** — assessment/analysis and clinical-diagnostic content
  coexist;
- **negative C5** — religious, institutional, authority and crime-related
  structures overlap;
- **negative C6** — built environment/transport and violence/weapons overlap;
- **negative C7** — anatomical/clinical and clothing/body-surface terms
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
