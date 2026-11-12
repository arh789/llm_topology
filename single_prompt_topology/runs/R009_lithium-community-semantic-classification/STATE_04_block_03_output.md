# R009 State 04 — block 3 output

## State identity

- R008 state index: `4`
- R008 state label: `block_03_output`
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
| C0 | 404 | Information retrieval, participation and task/process actions | semantic/topic | High | `initiating`, `participating`, `retrieving`, `extracted`, `recognizing`, `formatted`, `determining`, `maintaining`, `accessing`, `formulated`, `withdrawing`; extremes include `seeking`, `solved`, `recognized`, `Response`, `Views` and `Role`. |
| C1 | 373 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `of`, `was`, `is`, `have`, `am`, `A`, plus fragments such as `ate`, `en`, `et`, `ite`; extremes are likewise largely fragments and short word pieces. |
| C2 | 372 | Biomedical/biological terminology mixed with food/agricultural terms | mixed | Moderate | `immunosuppressive`, `glucocortic`, `Phosph`, `infertility`, `evolutionary`, `obesity`, `phyt`, `Bcl` coexist with `rice`, `cakes`, `beet`; extremes include `mitotic`, `polys`, `carbon` and `BCG`. |
| C3 | 330 | Multilingual, encoding and fragmentary lexical residues | formatting/tokenizer | High | Representatives include replacement characters, Thai script and short fragments such as `Bo`, `Ext`, `De`, `Rel`, `La`, `akespe`; extremes include further malformed or partial forms. No stable topic is evident. |
| C4 | 264 | Cities, countries, nationalities and personal/place names | named-entity | High | `Nigerian`, `Charlotte`, `Indonesian`, `Orlando`, `Sandy`, `Sacramento`, `Charleston`, `Egyptian`, `Chicago`, `Sydney`, `California`, `Finnish`; extremes include `Thai`, `African` and place-name fragments. |
| C5 | 262 | Databases, software and technical abbreviations | semantic/topic | High | `Database`, `mysql`, `MySQL`, `Django`, `DB`, `TS`, `IP`, `txt`, together with technical abbreviations; extremes include `NAS`, `ACP`, `CSS`, `mong` and `NS`. |
| C6 | 248 | Molecular/physical science mixed with computing/server terminology | mixed | Moderate | `conformational`, `renormalization`, `molecule`, `molecules`, `cyclin`, `cationic`, `interacting`, `roelectric` coexist with `Server`, `server`, `Hash`, `Entry`; extremes include `Spin`, `surfaces`, `bind`, `electronic`. |
| C7 | 247 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | Dominated by strings such as `""))`, `))))`, `))).`, `! )`, `?)`, `)));`; 165 of 247 tokens are punctuation or symbols. |
| C8 | 190 | Affective, evaluative and discourse/adverbial language | semantic/topic | Moderate | `emotional`, `emotionally`, `Eventually`, `Subsequently`, `culturally`, `subsequent`, `interesting`, `obviously`, `environmentally`, `bitterly`; extremes include `refreshing`, `remembers`, `OK`, `shaken`, `urgently` and `romantic`. |
| C9 | 153 | Finance, politics, administration and institutional/social relations | semantic/topic | High | `Financial`, `Political`, `parliamentary`, `transactions`, `Goldman`, `Legislative`, `financial`, `administrative`, `familial`; extremes include `Civil`, `civic`, `financing`, `bidding`, `Appellate`, `stake`, `lending`, `employment`. |
| C10 | 139 | Numeric strings | numeric | High | Dominated by values such as `173`, `479`, `373`, `379`, `599`, `758`, `359`, `177`, `499`, `104`, `165`, `134`; extremes are likewise primarily numeric. |
| C11 | 72 | Calendar time, years and leisure/performance scheduling | mixed | Moderate | `1986`, `1993`, `1992`, `Sunday`, `weekend`, `1978`, `2012`, `morning`, `Saturday`, `1997` coexist with `theatre`, `cinema`, `theater`; extremes include `2013`, `2019`, `seasonal`, `months`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 551 | Personal names mixed with lexical stems/fragments | named-entity | Moderate | `Thompson`, `Liz`, `Luke`, `Sullivan`, `Murphy`, `Palmer`, with extremes including `Max`, `Turk`, `Kepler`, `Sebast`, `Tanz`; numerous fragments such as `comp`, `clums`, `disg` reduce purity. |
| C1 | 380 | Analysis, scientific description, estimation and explanation | semantic/topic | High | `Characteristics`, `analysis`, `descriptions`, `estimates`, `pathophysiology`, `recommendations`, `messages`, `Experiments`, `epidemiology`, `concepts`, `explanations`; extremes include `biomarkers`, `covariance`, `measure`, `departure`. |
| C2 | 346 | Authority, institutional and religious/social roles mixed with law | mixed | Moderate | `unconstitutional`, `Archbishop`, `Congressman`, `Chairman`, `leaders`, `professor`, `Officers`, `technician`, `Rabbi`, `theolog`; extremes include `Laws`, `officials`, `Chair`, `contractor`, `Creator`. `goddess` and `sculptures` broaden the structure. |
| C3 | 288 | Common grammatical/function words, suffixes and fragments | lexical/morphological | High | `not`, `if`, `or`, `by`, `level`, together with fragments `ia`, `ized`, `ian`, `als`; extremes include `que`, `omes`, `ues`, `iant` and `unit`. |
| C4 | 261 | Negative evaluation, discomfort, threat and perceptual descriptors | semantic/topic | High | `uncomfortable`, `unacceptable`, `terrifying`, `annoying`, `indistinguishable`, `horrific`, `impressive`, `tragedy`, `gorgeous`; extremes include `conclusive`, `audible`, `madness`, `uniform`, `yelled`, `cracked`. |
| C5 | 233 | Change, construction, increase/decrease and regulation actions | semantic/topic | High | `pulled`, `decrease`, `alteration`, `dropped`, `constructing`, `prohibited`, `determined`, `dropping`, `Increase`, `improve`, `reported`; extremes include `Beginning`, `begin`, `bolster`, `revive`, `mandate`, `composed`. |
| C6 | 226 | Clinical/biological terminology mixed with fantasy/conflict roles | mixed | Moderate | `hospitalization`, `echocardiography`, `angiography`, `pathogens`, `anesthesia`, `cerebellum`, `skull`, `epidermis`, `biopsy`, `allele` coexist with `warriors`, `monsters`, `villain`, `Devil`. |
| C7 | 214 | Built environment, weapons, transport and physical objects | mixed | Moderate | `hallway`, `stairs`, `staircase`, `guns`, `cliffs`, `trucks`, `floors`, `sidewalk`, `rifles`, `outfits`; extremes include `shots`, `wireless`, `nozzle`, `snow`, `appliances`, `rail`. |
| C8 | 176 | Abstract mathematics mixed with software/programming concepts | mixed | Moderate | `omorphisms`, `commutative`, `morphism`, `functor`, `bigoplus`, `maps`, `morphisms` coexist with `databind`, `addr`, `compiler`, `plugins`, `Decoder`, `sdk`, `Pointer`, `uint`, `Generator`. |
| C9 | 137 | Multilingual and orthographic fragments | formatting/tokenizer | High | `está`, `mé`, `že`, `vý`, `emente`, `usamm`, `amente`, Cyrillic and accented fragments, with additional language fragments in the extremes. |
| C10 | 124 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 117 of 124 tokens are punctuation or symbols; examples include bracket/operator combinations such as `(`, `}{(`, `{(`, `}=(`, `=(\`, `$(`, `%%`. |
| C11 | 83 | Violence, killing, crime and destruction | semantic/topic | High | `murdered`, `kill`, `murders`, `massacre`, `killing`, `murder`, `thief`, `uprising`, `destroyed`, `slaughter`; extremes include `remand`, `arrest`, `indicted`, `doomed`. |
| C12 | 81 | Numeric strings, especially historical years and three-digit values | numeric | High | `1882`, `1867`, `1860`, `560`, `1830`, `1870`, `1868`, `142`, `282`, `861`, `428`; extremes are likewise predominantly numeric. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains identifiable structures spanning:

- information retrieval and task/process actions;
- software/databases and technical systems;
- affective/evaluative/discourse language;
- finance, politics and administration;
- geography and names;
- biomedical and agricultural/biological material;
- molecular/physical science plus computing;
- grammar and lexical fragments;
- multilingual/tokenizer residues;
- formatting;
- numeric strings;
- calendar/time plus leisure/performance terms.

Five of twelve communities receive a primary `semantic/topic` classification.
Two are mixed, two formatting/tokenizer, one lexical/morphological, one
named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- analysis/scientific reporting;
- negative evaluation and threat;
- change/construction/regulation;
- violence/crime/destruction;
- authority/religious/social roles;
- clinical biology mixed with fantasy/conflict roles;
- built environment and physical objects;
- abstract mathematics mixed with software;
- names;
- grammatical fragments;
- multilingual/tokenizer structure;
- mathematical formatting;
- numeric strings.

Four of thirteen communities receive a primary `semantic/topic` label. Four
are mixed, two formatting/tokenizer, one lexical/morphological, one
named-entity and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C2** — biomedical and food/agricultural terms coexist;
- **positive C6** — molecular/physical-science and computing/server terms
  coexist;
- **positive C8** — affective, evaluative and discourse/adverbial language
  overlap;
- **positive C11** — calendar/time and theatre/cinema terms coexist;
- **negative C0** — personal names dominate but lexical fragments are
  substantial;
- **negative C2** — authority, law, religion and social roles overlap;
- **negative C6** — clinical/biological terminology coexists with
  fantasy/conflict roles;
- **negative C7** — multiple physical-object and built-environment domains
  coexist;
- **negative C8** — abstract mathematical and programming structures coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
