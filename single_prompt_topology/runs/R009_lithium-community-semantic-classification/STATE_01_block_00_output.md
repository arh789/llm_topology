# R009 State 01 — block 0 output

## State identity

- R008 state index: `1`
- R008 state label: `block_00_output`
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
| C0 | 402 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Representatives include `was`, `is`, `have`, `all`, `more`, `am`, `work`, alongside fragments such as `i`, `en`, `et`; extremes include `seeking`, `answer`, `IS` and additional fragments. The dominant organisation is lexical/grammatical rather than topical. |
| C1 | 380 | Databases, software, data formatting and computing systems | semantic/topic | High | `mysql`, `MySQL`, `sqlite`, `SQL`, `Database`, `db`, `innerHTML`, `Login`; extremes include `Hash`, `CSS`, `nginx` and `SQL`. |
| C2 | 370 | Personal names mixed with multilingual/name fragments | named-entity | Moderate | Strong name content includes `Anna`, `Katherine`, `Sandy`, `Michelle`, `Barnes`, `Curtis` and `Michael`, but the community also contains multilingual and fragmentary forms such as `ös`, `ori`, `idis` and replacement characters. |
| C3 | 280 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | Dominated by strings such as `}}})`, `})}`, `]))`, `))))`, `}}`, `}))`, with 205 of 280 tokens classified as punctuation or symbols. |
| C4 | 279 | Maintenance, review, recognition and information-handling actions | semantic/topic | Moderate | `maintaining`, `reviewing`, `positioning`, `highlighted`, `ignoring`, `establishes`, `recognizing`, `documented`, `researching`, `recalling`; extremes include `accessing`, `solved`, `remembers`, `referenced` and `formulated`. |
| C5 | 272 | Acronyms, initialisms and short technical/scientific abbreviations | lexical/morphological | High | Dominated by forms such as `IGF`, `SS`, `PC`, `CP`, `IP`, `CS`, `FGF`, `CF`, `NF`; extremes include `CSI`, `FIN`, `BCG`, `NAS`, `ICP`, `ACP` and `HCT`. |
| C6 | 252 | Nationality, governance, social and administrative descriptors | semantic/topic | Moderate | `Nigerian`, `Indonesian`, `Pakistani`, `Chinese`, `Pakistan`, `Ethiop` coexist with `psychological`, `psychosocial`, `politically`, `administrative`, `Financial` and `bureaucracy`; extremes include `Civil`, `Appellate`, `African`, `Thai` and `ethnic`. |
| C7 | 251 | Evaluative, degree and discourse/adverbial language | semantic/topic | Moderate | `extraordinarily`, `interesting`, `satisfactory`, `unsatisfactory`, `professionally`, `probably`, `vastly`, with discourse/time forms `Eventually`, `Therefore`, `Subsequently`; extremes include `refreshing`, `permanent`, `cheaper`, `ideally`, `retrospectively` and `intermittent`. |
| C8 | 191 | Biomedical, endocrine, immune and physiological terminology | semantic/topic | Moderate | `immunosuppressive`, `angiotensin`, `conformational`, `infertility`, `hypothalamus`, `lymphocyte`, `rheumatoid`, `follic`; extremes include `mitotic`, `regeneration`, `saline` and `Carbon`. The biomedical signal dominates despite some material/scientific outliers. |
| C9 | 180 | Food, plants, small animals and biological/agricultural life | mixed | Moderate | `vegetation`, `cabbage`, `vegetable`, `chocolate`, `coconut`, `cakes`, `bread`; extremes include `hatch`, `fry`, `curry`, `spiders`, `beet`, `worm`, `clutch` and `worms`. `travelling`, `infrastructure` and `communities` prevent a clean single-topic label. |
| C10 | 141 | People, sport/exercise and institutional/social activity | mixed | Moderate | `athletes`, `adolescents`, `workers`, `exercising`, `Programme`, `Broncos`, `Department`, `discussions`; extremes include `woman`, `games`, `children`, `athlete`, `Exercise` and `chess`, alongside `Acknowledgements` and `RESULTS`. |
| C11 | 127 | Numeric strings, including years and three-digit values | numeric | High | Dominated by `449`, `14`, `349`, `169`, `149`, `409`, `1975`, `387`, `489`, `379`, `499`, `015`; extremes include `2013`, `754`, `177` and `014`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 401 | Personal names and geographic/name-like entities | named-entity | Moderate | `Murphy`, `Thompson`, `Jeff`, `Nick`, `Nelson`, `Harold`, with extremes including `Max`, `Romania`, `Noah`, `Bell` and `Territory`. Numerous short name fragments reduce purity. |
| C1 | 358 | Biomedical science, biological research and scientific-method terminology | semantic/topic | Moderate | `pathophysiology`, `zebrafish`, `epidemiology`, `methodologies`, `phenotypes`, `anesthesia`, `cerebellum`; extremes include `biomarkers`, `allele`, `assay`, `homozygous` and cancer-related fragments. `unconstitutional`, `technologies` and `thermoplastic` are notable outliers. |
| C2 | 272 | Incomplete word stems, prefixes and lexical fragments | lexical/morphological | High | Dominated by forms such as `enthus`, `comp`, `imposs`, `ingred`, `unequiv`, `clums`, `incomp`, `insign`, `maint`, with extremes including `abol`, `abrog`, `env` and `orig`. |
| C3 | 268 | Transformation, inhibition, increase/decrease and structural change | semantic/topic | High | `transformed`, `transformation`, `transformations`, `Inhibition`, `increase`, `enhancement`, `inhibition`, `displacement`, `distinguishable`; extremes include `bolster`, `begin`, `uniform`, `depart` and `elev`. |
| C4 | 268 | Interpretation, instruction, prohibition, belief and authority | semantic/topic | High | `determination`, `interpretation`, `prohibited`, `instructed`, `explanations`, `recommendations`, `prohibition`, `expectations`, `skepticism`, `argue`; extremes include `Laws`, `beliefs`, `authority`, `approved`, `notions` and `context`. |
| C5 | 257 | Built environment, physical objects, equipment and clothing | mixed | Moderate | `hallway`, `staircase`, `jacket`, `boats`, `guns`, `stairs`, `floors`, `brewery`, `artwork`, `outfits`; extremes include `contractor`, `shots`, `barrel`, `nozzle`, `wireless`, `stones` and `clamp`. The shared physical-object/environment character is clear, but no narrow topic dominates. |
| C6 | 236 | Social titles, occupations, religious/fictional roles and creative figures | mixed | Moderate | `Archbishop`, `producer`, `Professor`, `Rabbi`, `Governor`, `Duchess` occur alongside `monsters`, `demons`, `demon`, `villain`, `prodig`; extremes include `Chair`, `composer`, `Creator`, `Devil`, `pagan`, `Earl` and `cartoon`. |
| C7 | 229 | Common word pieces, suffixes and function-word fragments | lexical/morphological | High | `o`, `if`, `ized`, `B`, `man`, `ian`, `level`, `ad`, `ments`, `led`, `ab`; extremes include `whether`, `unit`, `notes`, `store`, `con`, `ues` and `iece`. |
| C8 | 173 | Emotional, threat, horror and evaluative descriptors | semantic/topic | High | `terrifying`, `monstrous`, `thief`, `madness`, `weird`, `bizarre`, `horrific`, `uncomfortable`, contrasted with `gorgeous`, `magnificent`, `cute`; extremes include `fatal`, `screamed`, `murdered`, `destroyed` and `Fun`. |
| C9 | 104 | Numeric strings | numeric | High | Dominated by values such as `141`, `560`, `841`, `861`, `642`, `641`, `142`, `745`, `281`, `682`, `078` and `630`. |
| C10 | 90 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 88 of 90 tokens are punctuation or symbols; examples include `{(`, `_{(`, `=(\`, `$(`, `(**`, `_{`, `%%` and dash/quote combinations. |
| C11 | 79 | Programming, software tooling and low-level computing terms | semantic/topic | High | `Bitmap`, `addr`, `Plugin`, `compiler`, `cmd`, `plugins`, `hooks`, `Graphics`; extremes include `drv`, `uint`, `Pointer`, `sdk`, `api`, `OID` and `Platform`. |
| C12 | 58 | Multilingual suffixes, language fragments and orthographic forms | lexical/morphological | High | `amente`, `isme`, `ità`, `ierung`, `usamm`, `äsident`, `heeft`, `acional`, `ición`, `GmbH`; extremes include `atus`, `modo`, `zum`, `modal` and `aval`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains several clearly identifiable organising
principles, but it is substantially less dominated by narrow scientific topics
than the State 00 input-embedding baseline. Within this state alone, the
observable structures include:

- computing, databases and data formatting;
- maintenance/review/information-handling actions;
- nationality/governance/social-administrative language;
- evaluative and discourse/adverbial language;
- biomedical/endocrine terminology;
- names;
- acronyms/initialisms;
- food/agricultural/biological material;
- people/sport/institutional activity;
- numbers;
- grammar/word fragments;
- formatting strings.

Five of twelve communities receive a primary `semantic/topic` label. Two are
lexical/morphological, two mixed, one named-entity, one numeric and one
formatting/tokenizer.

This description does not imply that the side has become less coherent through
depth; coherence is outside the R009 first-pass task.

### Negative tail

The negative-tail population also contains multiple recognisable semantic
domains:

- biomedical/scientific research;
- transformation and inhibition;
- interpretation, rules, belief and authority;
- emotional/threat/evaluative language;
- software/programming;
- names;
- physical objects and environments;
- social/fictional/religious roles;
- lexical fragments;
- multilingual morphology;
- numerical and formatting structures.

Five of thirteen communities receive a primary `semantic/topic` label. The
remaining communities are distributed across lexical/morphological,
named-entity, mixed, numeric and formatting/tokenizer categories.

Negative anti-alignment therefore again contains structured semantic material
alongside lexical and tokenizer-driven organisation. No suppression,
contradiction or exclusion interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C2** — personal names dominate, but multilingual/tokenizer
  fragments are substantial;
- **positive C6** — nationality/geographic and social-administrative language
  coexist in one broad community;
- **positive C7** — evaluative language and discourse/adverbial forms overlap;
- **positive C8** — biomedical content dominates, but scientific/material
  outliers remain;
- **positive C9** — food, plants and small-animal/life-cycle terms coexist
  with unrelated travel/infrastructure tokens;
- **positive C10** — people, sport/exercise and institutional language do not
  collapse cleanly to one topic;
- **negative C1** — the biomedical/research signal is strong but not exclusive;
- **negative C5** — physical objects, built environment, equipment and clothing
  form a broad mixed structure rather than one narrow domain;
- **negative C6** — occupational/religious/social titles and fictional/creative
  roles coexist.

These ambiguities are preserved for later coherence analysis rather than
resolved by stronger labels.

## R009 boundary

No comparison with State 00 or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
