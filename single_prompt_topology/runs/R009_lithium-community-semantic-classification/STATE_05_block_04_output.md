# R009 State 05 — block 4 output

## State identity

- R008 state index: `5`
- R008 state label: `block_04_output`
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
| C0 | 348 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | `is`, `of`, `was`, `have`, `like`, `am` occur with fragments such as `ate`, `en`, `et`; extremes are likewise dominated by short forms and fragments. |
| C1 | 335 | Acronyms, initialisms and short technical abbreviations | lexical/morphological | High | Dominated by `PC`, `SC`, `CA`, `HA`, `SS`, `CP`, `IP`, `NAS`, `CS`, `ACP`, `LOS` and similar short forms. |
| C2 | 330 | Databases, websites, information access and software-interface systems | semantic/topic | High | `response`, `sites`, `mysql`, `accessing`, `Connection`, `DB`, `Database`, `checking`; extremes include `Views`, `Role`, `CSS`, `Hash`, `Cyber`, `Response` and `Entry`. |
| C3 | 309 | Task/process actions mixed with finance and sport/activity | mixed | Moderate | `initiating`, `travelling`, `formatted`, `specializes`, `giving`, `extracted`, `transactions`, `financing`, `resolving` coexist with `Financial`, `basketball`, `exercising` and `games`. |
| C4 | 296 | Biomedical and molecular science mixed with physical-science concepts | mixed | Moderate | `immunosuppressive`, `conformational`, `glucocortic`, `inflammatory`, `pituitary`, `metabolic`, `molecule`, `infertility`, `chemical`, `membranes` coexist with `renormalization`, `Spin`, `surfaces`, `carbon`, `Gas`. |
| C5 | 284 | Countries, nationalities, cities and personal/place names | named-entity | High | `Indonesian`, `Nigerian`, `Sacramento`, `Charleston`, `California`, `Chicago`, `Chinese`, `Canadian`, `Charlotte`, `Orlando`, `Australian`, `Swedish`; extremes include `Thai` and place-name fragments. |
| C6 | 271 | Psychology, social life, politics and administration | mixed | Moderate | `psychological`, `psychosocial`, `emotional`, `Political`, `political`, `administrative`, `parliamentary`, `cultural`, `psychiat`; extremes include `Civil`, `civic`, `Brothers`, `Home`, `active`. |
| C7 | 181 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 145 of 181 tokens are punctuation or symbols; examples include `]))`, `}})`, `""))`, `))))`, `))).`, `]))`, `))); ` and long repeated-symbol strings. |
| C8 | 164 | Discourse, temporal and evaluative/adverbial language | semantic/topic | Moderate | `Subsequently`, `Eventually`, `subsequent`, `Alternatively`, `Anyway`, `Obviously`, `recalling`, `retrospectively`, `hugely`; extremes include `refreshing`, `remembers`, `OK`, `newest`, `worrying`, `Remember`. |
| C9 | 131 | Multilingual, malformed and encoding/tokenisation fragments | formatting/tokenizer | High | Replacement characters, Thai and Greek/Cyrillic fragments, partial forms such as `dehy`, `delic`, `envis`, `photograp`, and malformed tokens dominate without a stable topic. |
| C10 | 100 | Food, nutrition and domestic/agricultural animals | semantic/topic | High | `cakes`, `rice`, `food`, `Veget`, `bread`, `chocolate`, `Nutrition`, `cats`, `cat`; extremes add `beet`, `worm`, `spiders`, `pig`, `coconut`, `fry`. |
| C11 | 90 | Numeric strings | numeric | High | Dominated by values such as `598`, `599`, `603`, `373`, `149`, `404`, `478`, `136`, `158`, `379`, `614`, `015`. |
| C12 | 47 | Calendar time, years, weekdays and seasons | semantic/topic | High | `1993`, `1992`, `1986`, `1996`, `weekend`, `1981`, `1975`, `January`, `night`, `Sunday`, `1998`, `1997`; extremes include `2013`, `Week`, `2019`, `months`, `today`, `spring`, `Saturday`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 477 | Personal names and name-like entities | named-entity | High | `Hayes`, `Liz`, `Dav`, `Thompson`, `Murphy`, `Roberts`, `Hal`, `Lou`, `Wheeler`, `Hicks`; extremes include `Max`, `Turk`, `Claud`, `Kepler`, `Bell`, `Sebast`. |
| C1 | 475 | Analysis, explanation, interpretation and construction/description | semantic/topic | High | `Characteristics`, `analysis`, `explanations`, `descriptions`, `interpretation`, `constructions`, `estimates`, `constructing`, `determined`, `creating`; extremes include `covariance`, `visions`, `authority` and `note`. |
| C2 | 447 | Negative evaluation, adversity, destruction and distress | semantic/topic | High | `uncomfortable`, `unconstitutional`, `disappointment`, `destroys`, `tragedy`, `massacre`, `annoying`, `unacceptable`, `indistinguishable`, `inconsistency`, `annoyed`; extremes include `madness`, `audible`, `revive`, `reunion`, `shouted`. |
| C3 | 317 | Built environment, architecture, weapons and physical objects | mixed | Moderate | `staircase`, `hallway`, `stairs`, `boats`, `guns`, `palace`, `balcon`, `cliffs`, `sword`, `tubes`; extremes include `shots`, `wireless`, `reactors`, `nozzle`, `spacecraft`, `glue`. |
| C4 | 299 | Common grammatical/function words, suffixes and lexical fragments | lexical/morphological | High | `if`, `not`, `or`, `case`, `by`, with fragments such as `ia`, `ie`, `ized`, `ian`, `als`; extremes include `que`, `omes`, `blk`, `unit`, `ues`. |
| C5 | 294 | Religious, institutional and authority roles mixed with violence/fantasy | mixed | Moderate | `Archbishop`, `theolog`, `Congressman`, `pastor`, `technicians`, `Chairman`, `Rabbi`, `officials`, `CEO` coexist with `goddess`, `murders`, `monsters`, `Devil`, `pagan`. |
| C6 | 200 | Clinical diagnostics, anatomy and pathology | semantic/topic | High | `echocardiography`, `pathophysiology`, `abdomen`, `angiography`, `skull`, `anesthesia`, `cerebellum`, `microscopy`, `phenotypes`, `arrhythm`; extremes include `biomarkers`, `NRAS`, `epidermis`, `allele`, carcinoma-related fragments. |
| C7 | 186 | Negative/contrastive word stems and incomplete lexical forms | lexical/morphological | High | `catast`, `discour`, `comp`, `unsatisf`, `incomp`, `abol`, `unden`, `unmist`, `abrog`; extremes include `uncon`, `conspic`, `abol`, `displ` and target fragment `lith`. |
| C8 | 138 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 127 of 138 tokens are punctuation or symbols; examples include `(`, `}{(`, `{(`, `)$(,`, `) }$,`, `) }(`, operator and bracket combinations. |
| C9 | 110 | Numeric strings, especially historical years | numeric | High | `1867`, `560`, `1884`, `282`, `861`, `1900`, `841`, `1882`, `1860`, `870`, `320`, `1870`; extremes include `1848`, `1830` and other numbers. |
| C10 | 106 | Multilingual suffixes and orthographic fragments | lexical/morphological | High | Accented and multilingual forms such as `vý`, `ść`, `está`, `mé`, `ável`, `usamm`, `cz`, `emente`, `sí`, `stadt`; extremes include `ić`, `modo`, `avait`, `č`, `lado`, `ş`. |
| C11 | 75 | Abstract algebra, geometry and mathematical notation | semantic/topic | High | `omorphisms`, `uniforms`, `commutative`, `morphism`, `maps`, `bigoplus`, `perpendicular`, `homomorphism`, `morphisms`, `homogeneous`, `coherent`; extremes include `reducible`, `zero`, `diag`, `bounded`, `quotient`. |
| C12 | 74 | Low-level computing, hardware/software and runtime systems | semantic/topic | High | `initialization`, `hw`, `FFFF`, `compiler`, `runtime`, `databind`, `nv`, `Decoder`, `Draw`, `sdk`, `addr`; extremes include `drv`, `Pointer`, `png`, `uint`, `GPIO`. |
| C13 | 20 | Degree, approximation and qualification language | semantic/topic | High | `seemingly`, `essentially`, `almost`, `solely`, `Almost`, `Half`, `pretty`, `Not`; extremes include `Seems`, `truly`, `officially`, `half`, `Pretty`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains identifiable structures spanning:

- databases, websites and software interfaces;
- task/process actions;
- biomedical and molecular science;
- psychology, politics and social-administrative language;
- discourse and evaluative modifiers;
- food, nutrition and animals;
- geography and names;
- acronyms and short technical forms;
- common grammar and word fragments;
- multilingual/tokenizer residues;
- punctuation/formatting;
- numeric strings;
- calendar/time structure.

Four of thirteen communities receive a primary `semantic/topic`
classification. Three are mixed, two lexical/morphological, two
formatting/tokenizer, one named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- analysis/explanation/interpretation;
- adversity, destruction and distress;
- clinical diagnostics and pathology;
- abstract mathematics;
- low-level computing;
- degree/qualification language;
- names;
- built environment and physical objects;
- religious/institutional/fantasy roles;
- grammatical and lexical fragments;
- multilingual morphology;
- mathematical formatting;
- numeric strings.

Six of fourteen communities receive a primary `semantic/topic`
classification. The remainder are lexical/morphological, mixed, named-entity,
formatting/tokenizer and numeric.

Negative anti-alignment again contains structured semantic material alongside
lexical and tokenizer-driven organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C3** — task/process language overlaps with finance and sport;
- **positive C4** — biomedical and physical-science concepts coexist;
- **positive C6** — psychological/social and political/administrative
  structures overlap;
- **positive C8** — discourse, temporal and evaluative adverbial forms overlap;
- **negative C3** — architecture, transport, weapons and technical objects
  coexist;
- **negative C5** — institutional/religious roles overlap with violent and
  fantastical terms;
- **negative C7** — lexical stems are semantically suggestive but are
  predominantly incomplete forms.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
