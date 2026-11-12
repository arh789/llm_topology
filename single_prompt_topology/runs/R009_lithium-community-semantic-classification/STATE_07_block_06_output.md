# R009 State 07 — block 6 output

## State identity

- R008 state index: `7`
- R008 state label: `block_06_output`
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
| C0 | 454 | Biomedical, psychological and inflammatory/therapeutic terminology | semantic/topic | High | `immunosuppressive`, `neurodegenerative`, `psychological`, `psychosocial`, `inflammatory`, `glucocortic`, `regenerative`, `emotional`, `anticancer`, `menopausal`; extremes include `mitotic`, `Immun`, `personalized` and `rheumatoid`. |
| C1 | 374 | Work, access, participation and task/process actions | semantic/topic | High | `travelling`, `Working`, `getting`, `accessing`, `having`, `initiating`, `participating`, `originating`, `forms`, `activating`, `researching`; extremes include `seeking`, `solved`, `resolving`, `recognized`, `referenced`. |
| C2 | 367 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `of`, `have`, `is`, `was`, `all`, `A`, `am`, `and`, `like`, with fragments such as `en`, `et`; extremes are likewise short fragments and malformed pieces. |
| C3 | 334 | Databases, transactions and information/software systems | semantic/topic | High | `Database`, `Connection`, `mysql`, `response`, `DB`, `transactions`, `formatted`, `MySQL`; extremes include `Hash`, `Role`, `Entry`, `Server`, `cycle` and `active`. |
| C4 | 244 | Finance, politics, administration and social/community activity | mixed | Moderate | `Financial`, `political`, `cultural`, `administrative`, `reimbursement`, `business`, `financial`, `communities`, `basketball`; extremes include `employment`, `Civil`, `lending`, `Social`, `fellowship`, `franchise`, `games`, `bidding`. |
| C5 | 229 | Cities, nationalities and personal/place names | named-entity | High | `Pakistani`, `Indonesian`, `Cleveland`, `Charlotte`, `Mexican`, `Atlanta`, `Sacramento`, `Laura`, `Charleston`, `Orlando`, `Nigerian`, `California`; extremes include `Thai`, `Salvador`, `London`. |
| C6 | 190 | Multilingual, malformed and fragmentary tokenisation residues | formatting/tokenizer | High | Replacement characters, Thai/Hebrew/Greek fragments and partial forms such as `delic`, `immedi`, `Rel`, `Tra`, `dehy`; extremes remain malformed or fragmentary. |
| C7 | 186 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 134 of 186 tokens are punctuation or symbols; examples include `}})`, `))))`, `)}}`, `))).`, `""))`, repeated equals signs and closing delimiters. |
| C8 | 181 | Molecular and cell-biology abbreviations/signalling terms | semantic/topic | High | `caspase` fragment, `cyclin`, `CDK`, `Bcl`, `BRCA`, `AKT`, plus biochemical/scientific abbreviations; extremes include `Spin`, `nM` and short technical forms. The biological signalling/cell-cycle identity dominates. |
| C9 | 161 | Discourse, temporal and evaluative/adverbial language | semantic/topic | Moderate | `Eventually`, `Alternatively`, `Anyway`, `Subsequently`, `unsatisfactory`, `specific`, `Following`, `different`; extremes include `refreshing`, `OK`, `Thank`, `eventual`, `pertinent`, `Acknowledgements`. |
| C10 | 127 | Food, crops and animals | semantic/topic | High | `food`, `cabbage`, `cakes`, `Chocolate`, `rice`, `chocolate`, `coconut`, `tiger`, `foods`, `fish`, `Veget`, `cat`; extremes include `beet`, `litter`, `pig`, `worm`, `Bear`. |
| C11 | 87 | Numeric strings, including years | numeric | High | Dominated by values such as `574`, `373`, `586`, `84`, `593`, `599`, `404`, `158`, `603`, `379`, `773`; extremes include `2013`, `2019`, `409`, `176`, `173`, `136`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 464 | Analysis, interpretation, recommendation and constraint/regulation | semantic/topic | High | `determination`, `Characteristics`, `analysis`, `recommendations`, `interpretation`, `environments`, `prohibited`, `distinguishes`, `features`, `constructing`, `indistinguishable`; extremes include `displacement`, `composed`, `slated`, `measure`, `departure`, `insist`, `usage`. |
| C1 | 394 | Personal names and name-like entities | named-entity | High | `Thompson`, `Murphy`, `Liz`, `Lucy`, `Smith`, `Hicks`, `Nick`, `Gil`, `Luke`, `Jean`; extremes include `Max`, `Turk`, `Rabbi`, `Violet`, `Kat`, `Kepler`. |
| C2 | 388 | Common grammatical/function words, suffixes and lexical fragments | lexical/morphological | High | Dominated by `not`, fragments `ia`, `ie`, `ized`, `el`, `ian`, `ED`, `als`; extremes include `point`, `que`, `ues`, `iant`, `ORD` and multilingual fragments. |
| C3 | 348 | Clinical diagnostics/anatomy mixed with built-environment and clothing terms | mixed | Moderate | `echocardiography`, `angiography`, `abdomen`, `phenotypes`, `pathophysiology`, `cerebellum`, `erythrocytes`, `biomarkers` coexist with `staircase`, `hallway`, `boats`, `uniforms`, `stair`, `nozzle`, `clad`, `barrel`. |
| C4 | 348 | Negative evaluation, distress, difference and intensity | semantic/topic | High | `disappointment`, `unconstitutional`, `unacceptable`, `terrifying`, `horrific`, `dismay`, `inconsistency`, `differences`, `loud`, `tragedy`; extremes include `conclusive`, `robustness`, `variability`, `louder`, `audible`, `gloom`. |
| C5 | 230 | Religious/institutional roles, public culture and infrastructure | mixed | Moderate | `priest`, `Archbishop`, `priests`, `Constitution`, `concerts`, `theolog`, `Transportation`, `professor`, `physician`, `Cathedral`; extremes include `Chair`, `speakers`, `wireless`, `composer`, `broadcasts`, `officials`, `Laws`, `reactors`. |
| C6 | 175 | Negative/contrastive word stems and incomplete lexical forms | lexical/morphological | High | `unsatisf`, `catast`, `unmist`, `comp`, `env`, `displ`, `Disc`, `establ`, `unequiv`, `demonstr`; extremes include `uncon`, `dis`, `Lit`, `impos`, `Cons`. |
| C7 | 155 | Violence, destruction, crime and threatening/fantastical actors | semantic/topic | High | `destroys`, `destroyed`, `thief`, `guns`, `villain`, `massacre`, `murders`, `killings`, `murdered`, `goddess`; extremes include `Devil`, `shots`, `Delete`, `police`, `pagan`, `serpent`. |
| C8 | 148 | Low-level computing, hardware and abbreviated technical tokens | semantic/topic | Moderate | `hw`, `compiler`, `DAC`, `LED`, `Writer`, `nv`; extremes include `drv`, `compiler`, `sdk`, `Decoder`, `debug`, `png`, `HW`, `pointer`. Short letter pairs add lexical noise. |
| C9 | 145 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 129 of 145 tokens are punctuation or symbols; examples include bracket/operator combinations, percent strings, lambda and repeated mathematical delimiters. |
| C10 | 111 | Numeric strings, especially historical years | numeric | High | `210`, `1882`, `1921`, `1910`, `1900`, `1860`, `610`, `1888`, `1840`, `1886`, `1867`; extremes include `1848`, `1830`, `545` and other values. |
| C11 | 84 | Mathematics: algebra, convergence, eigenvalues and statistical quantities | semantic/topic | High | `omorphisms`, `bigoplus`, `vergence`, `asympt`, `morphisms`, `convergence`, `eigenvalues`, `variance`; extremes include `quotient`, `subset`, `covariance`, `uniform`, `zero`, `reducible`. |

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

- biomedical/psychological and inflammatory terminology;
- work/access/task actions;
- database and transaction systems;
- molecular and cell-biology signalling terms;
- discourse/evaluative modifiers;
- food/crops/animals;
- finance/politics/social activity;
- cities and nationalities;
- common grammar and fragments;
- multilingual/tokenizer residues;
- punctuation/formatting;
- numeric strings.

Six of twelve communities receive a primary `semantic/topic`
classification. The remainder are lexical/morphological, named-entity,
formatting/tokenizer, mixed and numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- analysis/interpretation/regulation;
- negative evaluation and distress;
- violence/crime/destruction;
- low-level computing;
- mathematics and quantitative structure;
- names;
- clinical/anatomical terms mixed with built-environment terms;
- religious/institutional/cultural material;
- lexical fragments;
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

- **positive C4** — finance/politics/administration and community/sport terms
  coexist;
- **positive C8** — molecular/cell-biology terms are strong, but short acronym
  structure is also substantial;
- **positive C9** — discourse, temporal and evaluative forms overlap;
- **negative C3** — clinical/anatomical and built-environment/clothing
  structures coexist;
- **negative C4** — negative evaluation overlaps with quantitative
  difference/robustness language;
- **negative C5** — religious/institutional, cultural/media and infrastructure
  terms coexist;
- **negative C8** — computing semantics are evident but abbreviated letter
  tokens introduce lexical noise.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
