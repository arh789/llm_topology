# R009 State 03 — block 2 output

## State identity

- R008 state index: `3`
- R008 state label: `block_02_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 11 | 11 | reconciled |
| negative_tail | 15 | 15 | reconciled |
| **Total** | **26** | **26** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 510 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Representatives include `of`, `is`, `was`, `have`, `more`, `am`, `work`, together with fragments such as `en`, `ate`, `et`; extremes are likewise dominated by partial forms and short lexical pieces. |
| C1 | 480 | Biomedical science mixed with physical-science terminology | mixed | Moderate | `immunosuppressive`, `angiotensin`, `conformational`, `IGF`, `glucocortic`, `testicular`, `infertility`, `menstrual` form a biomedical core, while `Phosph`, `renormalization`, `Spin`, `carbon`, `electronic` and `coherence` introduce a distinct physical-science component. |
| C2 | 399 | Information access, retrieval, recognition and task actions | semantic/topic | High | `accessing`, `giving`, `forgotten`, `formatted`, `ascertained`, `retrieving`, `response`, `extracted`, `recognizing`, `initiating`; extremes include `seeking`, `solved`, `remembers`, `Remember`, `working` and `Response`. |
| C3 | 319 | Evaluative, affective and discourse/adverbial language | semantic/topic | Moderate | `psychosocial`, `extraordinarily`, `electronically`, `Eventually`, `emotional`, `Subsequently`, `qualitatively`, `Therefore`, `inevitable`, `interesting`; extremes include `refreshing`, `Active`, `permanent`, `whole`, `OK` and `cheaper`. |
| C4 | 318 | Geography/nationality mixed with political, administrative and financial descriptors | mixed | Moderate | `Indonesian`, `Nigerian`, `Finnish`, `Australian`, `Ethiop`, `Guatem`, `Orlando`, `Charleston` coexist with `Financial`, `Political`, `administrative`, `parliamentary`, `Civil` and `civic`. |
| C5 | 278 | Acronyms, initialisms and short technical/scientific abbreviations | lexical/morphological | High | Dominated by forms such as `PC`, `TS`, `txt`, `SC`, `DB`, `MM`, `GA`, `SS`, `CP`, `HS`; extremes include `NAS`, `CS`, `ACP`, `BCG` and `CF`. |
| C6 | 267 | Websites, databases, forms, transactions and connection/service systems | semantic/topic | High | `sites`, `mysql`, `forms`, `transactions`, `SQL`, `Connection`, `Database`, `MySQL`, `Service`; extremes include `Form`, `Role`, `CSS`, `Forms`, `Views` and `Hash`. |
| C7 | 225 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | Dominated by strings such as `}})`, `]))`, `""))`, `)));`, `))))`, `]))`, `))).`; 182 of 225 tokens are punctuation or symbols. |
| C8 | 151 | Numeric strings | numeric | High | Dominated by values such as `373`, `144`, `379`, `138`, `349`, `168`, `289`, `359`, `14`, `169`, `647`; extremes are likewise primarily numbers. |
| C9 | 148 | Food/agriculture and biological life mixed with sport | mixed | Moderate | `rice`, `cakes`, `cabbage`, `gardening`, `bread`, `Veget`, `food`, `vegetation`, `chocolate`, `beet` coexist with `athletes` and `basketball`; extremes add `insects`, `worms`, `hatch` and `worm`. |
| C10 | 72 | Calendar time, years, weekdays and seasons | semantic/topic | High | `Mar`, `2012`, `2011`, `2009`, `Sunday`, `weekend`, `2014`, `2015`, `1992`, `2016`, `Monday`, `1988`; extremes include `2019`, `2013`, `months`, `seasonal`, `Week`, `August` and `Holiday`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 0 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 355 | Personal names, titles and name-like entities | named-entity | Moderate | `Nick`, `Alex`, `Jeff`, `Alan`, `Josh`, `Jean`, `Kat`, `Thompson`, `Luke`; extremes include `Rabbi`, `Max`, `Turk`, `Bell` and `Tanz`. `theolog` and fragments reduce purity. |
| C1 | 335 | Negative evaluation, rejection, adversity and discomfort | semantic/topic | Moderate | `unconstitutional`, `discour`, `unacceptable`, `indistinguishable`, `catast`, `tragedy`, `disproportion`, `uncomfortable`, `annoying`, `disappro`, `disgust`; extremes include `conclusive`, `madness` and several fragments. |
| C2 | 322 | Analysis, interpretation, scientific description and methodology | semantic/topic | High | `determination`, `visualization`, `epidemiology`, `interpretation`, `descriptions`, `phenotypes`, `stabilization`, `technologies`, `explanations`, `methodologies`, `constructions`, `Experiments`; extremes include `covariance`, `displacement` and `mandate`. |
| C3 | 259 | Occupations, authority titles and fictional/social roles | mixed | Moderate | `technician`, `Archbishop`, `professor`, `Chairman`, `Congressman`, `officer`, `leaders`, `CEO`, `Princess` coexist with `goddess`, `warriors`, `villain`; extremes include `Chair`, `Devil`, `officials`, `composer`. |
| C4 | 256 | Built environment, weapons, devices and physical objects | mixed | Moderate | `hallway`, `staircase`, `guns`, `smartphones`, `sidewalk`, `outfits`, `Transportation`, `sculptures`, `firearms`, `devices`, `gown`, `sword`; extremes include `wireless`, `shots`, `nozzle`, `barrel` and `wavelength` fragment. |
| C5 | 233 | Common word pieces, suffixes and grammatical fragments | lexical/morphological | High | Dominated by `ia`, `ized`, `als`, `ED`, `T`, `by`, `led`, `ology`, with short function words and fragmentary extremes such as `que`, `ues`, `omes`. |
| C6 | 182 | Clinical medicine, diagnostics, anatomy and pathology | semantic/topic | High | `echocardiography`, `pathophysiology`, `anesthesia`, `pathogens`, `medications`, `therapies`, `skull`, `biomarkers`, `abdomen`, `cerebellum`, `angiography`; extremes include `allele`, `epidermis`, `NRAS` and `diagnoses`. |
| C7 | 152 | Multilingual, encoding and orthographic fragments | formatting/tokenizer | High | Mixes non-Latin characters, replacement characters, accented forms and fragments such as `vé`, `amente`, `emente`, Arabic, Czech and East Asian characters; no stable topical centre is evident. |
| C8 | 149 | Violence, killing, crime and prohibition | semantic/topic | High | `prohibited`, `murdered`, `massacre`, `murder`, `murders`, `uprising`, `kill`, `destroyed`, `prohibition`, `killing`, `thief`, `slain`; extremes include `arrest`, `indicted` and `fatal`. |
| C9 | 136 | Programming, software tooling, data and document systems | semantic/topic | High | `detectors`, `addr`, `databind`, `Generator`, `manuscripts`, `Decoder`, `blog`, `compiler`, `plugins`; extremes include `drv`, `sdk`, `Monitor`, `uint`, `Pointer` and `address`. |
| C10 | 134 | Physical actions, movement and vocal/sound events | semantic/topic | Moderate | `pulled`, `screamed`, `removed`, `dropped`, `loud`, `hugged`, `snatched`, `shout`, `scream`, `shouted`, `yelled`; extremes include `applause`, `shuffle`, `swear`, `clip` and `sign`. |
| C11 | 102 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 93 of 102 tokens are punctuation or symbols; examples include bracket/operator combinations such as `}{(`, `{(`, `[]{}(`, `^*(`, `=(\`, `_{(`, `$(`. |
| C12 | 71 | Government, law and geographic/public-institution entities | mixed | Moderate | `legislature`, `Constitution`, `Congress`, `Laws`, `Statutes`, `governmental`, `statute`, `enactment` coexist with `Newcastle`, `Calgary`, `Vancouver`, `Australia`, `province`, `borough` and `CBC`. |
| C13 | 66 | Numeric strings | numeric | High | Dominated by `30`, `440`, `560`, `10`, `751`, `630`, `231`, `130`, `142`, `841`, `536`, `141`; extremes are likewise predominantly numeric. |
| C14 | 57 | Abstract algebra, category theory and mathematical notation | semantic/topic | High | `omorphisms`, `commutative`, `bigoplus`, `homogeneous`, `functor`, `morphism`, `homomorphism`, `morphisms`, `equival`; extremes include `reducible`, `zero`, `uniform`, `bounded`, `nonzero`, `subset` and `tikz`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 7 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains several recognisable semantic domains
alongside lexical, numeric and formatting organisation. Identified structures
include:

- information access/retrieval and task actions;
- evaluative/affective/discourse language;
- database and service systems;
- calendar/time structure;
- biomedical and physical-science terminology;
- geography/nationality plus administration/finance;
- food/agriculture/biological life plus sport;
- acronyms and short technical abbreviations;
- common grammatical fragments;
- numeric strings;
- punctuation and formatting strings.

Four of eleven communities receive a primary `semantic/topic`
classification, three are mixed, two lexical/morphological, one numeric and one
formatting/tokenizer.

No conclusion about coherence or trajectory is drawn from this composition.

### Negative tail

The negative-tail population contains a comparatively large number of
recognisable semantic structures:

- negative evaluation and adversity;
- analysis/interpretation/methodology;
- clinical medicine and diagnostics;
- violence/crime/prohibition;
- software/programming systems;
- physical actions and vocal events;
- abstract algebra/category theory;
- names;
- authority/fictional roles;
- built environment and physical objects;
- government/law/geography;
- lexical fragments;
- multilingual/tokenizer fragments;
- formatting;
- numbers.

Seven of fifteen communities receive a primary `semantic/topic`
classification. The remainder are mixed, lexical/morphological, named-entity,
formatting/tokenizer and numeric.

Negative anti-alignment again contains structured semantic material as well as
non-semantic organisation. No suppression or opposition interpretation is
assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — biomedical and physical-science terminology coexist strongly
  enough that `mixed` is retained;
- **positive C3** — evaluative, affective and discourse/adverbial terms overlap;
- **positive C4** — geographic/nationality and political/financial/
  administrative structures coexist;
- **positive C9** — food/agriculture and biological-life terms coexist with
  sport;
- **negative C0** — names dominate but titles, demonyms and fragments are
  substantial;
- **negative C1** — negative evaluation/adversity is clear but legally and
  lexically heterogeneous;
- **negative C3** — occupations and authority roles overlap with fictional and
  religious figures;
- **negative C4** — multiple classes of physical objects share the community;
- **negative C10** — movement, interaction and vocal/sound actions overlap;
- **negative C12** — law/government and geographic/public-institution structure
  coexist.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
