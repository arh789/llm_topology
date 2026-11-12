# R009 State 02 — block 1 output

## State identity

- R008 state index: `2`
- R008 state label: `block_01_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 14 | 14 | reconciled |
| negative_tail | 13 | 13 | reconciled |
| **Total** | **27** | **27** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 390 | Development, activation, evaluation and task/progress actions | semantic/topic | Moderate | Representatives include `development`, `activates`, `initiating`, `established`, `recognizing`, `Quantitative`, `extracted`, alongside evaluative terms `interesting`, `enjoyable`, `satisfactory`, `unsatisfactory`; extremes include `solved`, `accessing`, `promot`, `recognized` and `Accept`. |
| C1 | 383 | Biomedical, endocrine, physiological and psychological terminology | semantic/topic | Moderate | `angiotensin`, `conformational`, `psychological`, `adolescents`, `glucocortic`, `hypothal`, `pituitary`, `infertility`, `menstrual`, `IGF`; extremes include `mitotic`, `regeneration` and corticosteroid-related fragments. Some unrelated biological/lexical outliers remain. |
| C2 | 382 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `is`, `was`, `have`, `more`, `work`, `like`, `down`, `am`, together with fragments such as `en`, `et`, `g`; extremes include `seeking`, `remembers`, `working`, `Remember` and additional fragments. |
| C3 | 379 | Databases, software and computing abbreviations | semantic/topic | High | `mysql`, `DB`, `MySQL`, `CS`, `SQL`, `Database`, `TS`, `sqlite`, `PC`, `txt`; extremes include `NAS`, `CSS`, `ACP`, `nginx` and `LOS`. |
| C4 | 280 | Countries, nationalities, cities and geographic names | named-entity | High | `Nigerian`, `Indonesian`, `California`, `Ethiop`, `Sacramento`, `Chinese`, `Canadian`, `Philippines`, `Egyptian`, `Sri`, `Charleston`; extremes include `African`, `Thai` and geographic/name fragments. |
| C5 | 254 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | Dominated by `}}})`, `]))`, `))))`, `""))`, `))); `, `]))`, with 186 of 254 tokens classified as punctuation or symbols. |
| C6 | 208 | Politics, administration and civic institutions mixed with sport/social terms | mixed | Moderate | `politically`, `political`, `Political`, `bureaucracy`, `administrative`, `democratic`, `parliamentary`, `Financial`, `service` coexist with `psychosocial`, `athletes`, `basketball`; extremes include `Civil`, `Appellate`, `Legislative`, `civic`, `Exercise` and `games`. |
| C7 | 206 | Adverbial, temporal, affective and contextual modifiers | semantic/topic | Moderate | `Subsequently`, `Eventually`, `professionally`, `emotional`, `Therefore`, `emotionally`, `subsequent`, `culturally`, `inevitably`, `environmentally`, `retrospectively`; extremes include `intermittent`, `ideally`, `urgently` and `Further`. |
| C8 | 146 | Multilingual, encoding and word-fragment residues | formatting/tokenizer | High | Representatives contain replacement characters, Thai and European-language fragments such as `iten`, `isten`, `ieren`, `ksen`, `ellen`; extremes include additional malformed or fragmentary forms such as `idis`, `ös`, `ppen`, `ensch`. |
| C9 | 118 | Form/structure and measurement concepts mixed with interface/technical tokens | mixed | Moderate | `forms`, `form`, `densities`, `complexes`, `batches`, `Pressure`, `pressure`, `forming`, `Height` coexist with `Group`, `Login`, `Hash`, `Views`, `Entry`, `Role`; `injection`, `hatch` and `cycle` broaden the structure further. |
| C10 | 96 | Numeric strings | numeric | High | Dominated by values such as `169`, `149`, `489`, `499`, `409`, `387`, `146`, `289`, `173`, `388`, `449`, `599`. |
| C11 | 91 | Mathematical physics, computation and dynamical systems | semantic/topic | High | `renormalization`, `stochastic`, `Lorentz`, `logarithmic`, `computational`, `dimensional`, `simulations`, `dynamical`, `algebraic`; extremes include `Spin`, `coherence`, `electronic`, `Carbon` and `Gas`. |
| C12 | 71 | Food, crops, vegetation and gardening | semantic/topic | High | `cabbage`, `gardening`, `rice`, `chocolate`, `vegetation`, `cakes`, `landsc`, `forest`, `bread`; extremes include `curry`, `fry`, `flowering`, `coconut` and `Veget`. |
| C13 | 59 | Calendar time, years, weekdays and seasons | semantic/topic | High | `September`, `1988`, `Sunday`, `1992`, `2009`, `Monday`, `weekend`, `Season`, `1975`, `1961`, `2012`, `2011`; extremes include `2019`, `months`, `Week`, `August`, `weeks` and `spring`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 8 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 426 | Personal names and geographic/name-like entities | named-entity | Moderate | `Luke`, `Nick`, `Hicks`, `Jeff`, `Murphy`, `Lucas`, `Clay`, `McConnell`; extremes include `Max`, `Rabbi`, `Romania`, `Noah`, `Sebast`, `Tanz` and `Turk`. Name fragments and non-name outliers reduce purity. |
| C1 | 379 | Interpretation, prohibition, law, constraints and institutional judgement | semantic/topic | High | `determination`, `prohibiting`, `interpretation`, `prohibited`, `visualization`, `transformation`, `unconstitutional`, `prohibition`, `unacceptable`, `discriminatory`, `envisioned`; extremes include `Laws`, `approved`, `authority`, `conclusive` and `visions`. |
| C2 | 292 | Common word pieces, suffixes and grammatical fragments | lexical/morphological | High | Dominated by short forms such as `o`, `if`, `ia`, `ized`, `man`, `ED`, `ian`, `ad`; extremes include `unit`, `que`, `ues`, `iant`, `note` and punctuation. |
| C3 | 275 | Violence, killing, crime and tragedy | semantic/topic | High | `murdered`, `massacre`, `murders`, `thief`, `murder`, `killings`, `killing`, `tragedy`, `madness`, `terrifying`, `kill`; extremes include `arrest`, `fatal` and `news`. |
| C4 | 232 | Built environment, weapons, clothing and physical objects | mixed | Moderate | `hallway`, `staircase`, `guns`, `sidewalk`, `Transportation`, `jacket`, `gown`, `rifles`, `cliffs`, `brewery`, `outfits`, `sword`; extremes include `shots`, `Street`, `nozzle`, `barrel`, `wireless` and `equip`. |
| C5 | 218 | Occupations, titles, authority figures and fictional/social roles | mixed | Moderate | `producer`, `physician`, `technician`, `Archbishop`, `Duchess`, `Chairman`, `officer` coexist with `goddess`, `monsters`, `villain`, `warriors`; extremes include `Chair`, `Devil`, `Batman`, `composer`, `Creator`. |
| C6 | 179 | Scientific transformation, inhibition, optimisation and analysis processes | semantic/topic | High | `inhibition`, `Experiments`, `enhancement`, `stabilization`, `initialization`, `detectors`, `minimization`, `Analyses`, `increase`, `decrease`; extremes include `bolster`, `reducible`, `bounded`, `covariance` and mathematical fragments. |
| C7 | 169 | Incomplete word stems, prefixes and lexical fragments | lexical/morphological | High | `imposs`, `abrog`, `incomp`, `abol`, `insign`, `incred`, `ingred`, `incapable`, `comp`, `discl`, `unequiv`; extremes include `dilig`, `abol`, `abrog`, `parad`, `conspic` and `uncon`. |
| C8 | 165 | Multilingual, encoding and orthographic fragments | formatting/tokenizer | High | Mixes accented and non-Latin fragments (`vé`, `amente`, `ità`, Chinese/Japanese characters, `isme`, `déc`, `usamm`) with `FFFF`, `AAAAAAAA`, replacement characters and punctuation. |
| C9 | 162 | Biomedical diagnostics, pathology and clinical science | semantic/topic | High | `pathophysiology`, `echocardiography`, `epidemiology`, `phenotypes`, `angiography`, `biomarkers`, `erythrocytes`, `anesthesia`, `pathogen`, `neuropath`, `microscopy`; extremes include `allele`, `dysplasia`, `edema`. |
| C10 | 113 | Technology, digital media, creative tools and workspace systems | semantic/topic | Moderate | `technologies`, `artwork`, `Electronics`, `video`, `Generator`, `annotations`, `workspace`, `Photography`, `gallery`; extremes include `plugins`, `sdk`, `Monitor`, `transducer`, `Decoder`, `Devices`, `installer`. |
| C11 | 106 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | Dominated by bracket and operator strings such as `{(`, `=(`, `_{(`, `$(`, `)}(`, `**`; 85 of 106 tokens are punctuation or symbols. |
| C12 | 100 | Numeric strings | numeric | High | Dominated by `10`, `141`, `841`, `861`, `534`, `30`, `281`, `560`, `142`, `428`, `423`, with extremes including `924`, `705`, `760` and `1830`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 2 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains a broad mixture of semantic domains and
non-topical organising structures. Identified content includes:

- development/evaluation/task actions;
- biomedical and physiological terminology;
- databases and computing;
- geography and nationalities;
- politics and administration;
- adverbial/contextual modifiers;
- mathematical physics and dynamical systems;
- food, crops and vegetation;
- calendar/time structure;
- grammar and lexical fragments;
- multilingual/tokenizer residues;
- formatting strings;
- numeric structure.

Eight of fourteen communities receive a primary `semantic/topic`
classification. Two are mixed, two formatting/tokenizer, one named-entity, one
lexical/morphological and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn from this
distribution.

### Negative tail

The negative-tail population contains several strongly recognisable semantic
domains alongside lexical and tokenizer organisation:

- law, prohibition and institutional judgement;
- violence, crime and tragedy;
- scientific transformation/optimisation processes;
- biomedical diagnostics and pathology;
- technology/digital-media systems;
- names;
- physical objects and environments;
- occupations and fictional/social roles;
- lexical stems;
- multilingual/tokenizer fragments;
- mathematical formatting;
- numeric strings.

Five of thirteen communities receive a primary `semantic/topic` label, with
the remainder distributed across lexical/morphological, named-entity,
formatting/tokenizer, mixed and numeric categories.

Negative anti-alignment again contains structured semantic material; no
suppression or opposition interpretation is assigned in R009.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — development/action and evaluation language overlap;
- **positive C1** — biomedical/endocrine content is dominant but includes
  heterogeneous biological and lexical outliers;
- **positive C6** — political/administrative and sport/social terms coexist;
- **positive C7** — several kinds of adverbial/contextual modifiers share the
  community without one narrow subject;
- **positive C9** — form/measurement/structure concepts coexist with interface
  and unrelated process terms;
- **negative C0** — personal names dominate but geographic and fragmentary
  forms are substantial;
- **negative C4** — built-environment, weapon, clothing and object terms form a
  broad mixed structure;
- **negative C5** — occupations/titles and fictional/social-role terms coexist;
- **negative C10** — technology, media and creative/workspace terminology form
  a broad rather than narrow domain.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
