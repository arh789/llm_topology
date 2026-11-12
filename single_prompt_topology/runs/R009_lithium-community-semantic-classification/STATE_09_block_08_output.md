# R009 State 09 — block 8 output

## State identity

- R008 state index: `9`
- R008 state label: `block_08_output`
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
| C0 | 500 | Administration, evaluation, finance and task-resolution language | mixed | Moderate | `determinations`, `administrative`, `acceptable`, `Financial`, `Political`, `satisfactory`, `resolving`, `initiating`, `unsatisfactory`, `management`; extremes include `employment`, `fellowship`, `threatened`, `solved`, `Managed`, `mediation`. |
| C1 | 449 | Interaction/process concepts mixed with databases, computation and physical-science terms | mixed | Moderate | `interactions`, `activities`, `renormalization`, `createElement`, `development`, `transactions`, `DB`, `forms`, `actions`, `interacting`, `coupling`, `mysql`; extremes include `Spin`, `Hash`, `uploads`, `lengths`. |
| C2 | 421 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | Dominated by `of`, `is`, `have`, `at`, `A`, `a`, `and`, `found`, together with fragments such as `ir`, `ines`; extremes are largely fragments and malformed short forms. |
| C3 | 398 | Biomedical, immune, psychiatric and cellular terminology | semantic/topic | High | `immunosuppressive`, `neurodegenerative`, `psychosocial`, `conformational`, `glucocortic`, `psychological`, `immunodef`, `psychiatric`, `biodegrad`, `intracellular`; extremes include `mitotic`, `rheumatoid`, `regeneration`, `antifungal`, `overweight`. |
| C4 | 283 | Cities, countries and personal/place names | named-entity | High | `Atlanta`, `Indonesian`, `Charleston`, `Springfield`, `Nigerian`, `Terry`, `Anne`, `Orlando`, `Bradley`, `Mumbai`, `Sacramento`; extremes include `Salvador`, `Gary`, `London`. |
| C5 | 204 | Multilingual, malformed and fragmentary tokenisation residues | formatting/tokenizer | High | Replacement characters, Greek/Japanese fragments and short partial forms such as `Inter`, `Rel`, `Costa`, `Coca`, `Emer`, `McKin`; extremes remain malformed or fragmentary with no stable topic. |
| C6 | 195 | Closing punctuation, brackets and code/text formatting strings | formatting/tokenizer | High | 146 of 195 tokens are punctuation or symbols; examples include `}})`, `""))`, `))))`, `))).`, `}$)`, closing delimiters and repeated equals-sign strings. |
| C7 | 157 | Travel, food, literature/culture and biological/agricultural material | mixed | Moderate | `travelling`, `rice`, `literary`, `culinary`, `theatre`, `fibres`, `cafe`, `randomised`, Shakespeare fragment, `fungal`, `feeding`; extremes include `games`, `resort`, `Casino`, `fry`, `flowering`. |
| C8 | 129 | Work, daily life, seasonal/time and renewal actions | semantic/topic | Moderate | `Working`, `Day`, `living`, `working`, `keeping`, `walking`, `freshly`, `winter`, `January`, `Halloween`, `sprang`; extremes include `Week`, `seasonal`, `laying`, `nodded`, `renew`, `shook`. |
| C9 | 115 | Numeric strings, including years | numeric | High | Dominated by `373`, `598`, `239`, `596`, `599`, `603`, `399`, `595`, `136`, `389`, `499`; extremes include `1997`, `2019`, `2013`, `737`, `614`, `274`. |
| C10 | 100 | Acronyms, initialisms and short technical/biomedical abbreviations | lexical/morphological | High | Dominated by `DA`, `HS`, `MH`, `PC`, `CS`, `HA`, `AA`, `LA`, `BD`, `VC`; extremes include `CRM`, `Sr`, `WN`, `dm`, with `antid` fragments mixed in. |
| C11 | 70 | Culture, society, communities and social/environmental descriptors | semantic/topic | High | `cultural`, `culturally`, `professionally`, `electronically`, `communities`, `environmentally`, `socially`, `civilized`, `societal`, `nationality`; extremes include `Civil`, `Social`, `Cultural`, `Cyber`, `Online`. |
| C12 | 38 | Publishing, acknowledgements, references and review/paratext language | semantic/topic | High | `Acknowledgements`, `Thank`, `Bibliography`, `Acknowled`, `Publishing`, `praised`, `thanks`, `Books`, `advertising`; extremes include `References`, `Penguin`, `Dear`, `Review`, `FONT`. |

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
| C0 | 517 | Built environment, institutions/religion and violence/conflict | mixed | Moderate | `hallway`, `Cathedral`, `Constitution`, `palace`, `uniforms`, `trucks` coexist with `murders`, `disasters`, `priest`, `massacre`, `Archbishop`; extremes include `shots`, `Chair`, `Devil`, `speakers`, `thief`, `Territory`, `roads`. |
| C1 | 464 | Negative/contrastive lexical stems and incomplete word forms | lexical/morphological | High | `catast`, `anec`, `disast`, `comp`, `brilli`, `gluc`, `diss`, `cont`, `whis`; extremes include `crypt`, `sig`, `Lith`, `neglig`, `Cons` and other fragments. |
| C2 | 418 | Analysis, scientific description, technology and experimental concepts | semantic/topic | High | `environments`, `Characteristics`, `technologies`, `analysis`, `recommendations`, `Analyses`, `concepts`, `Experiments`, `hardware`, `circumstance`; extremes include `Features`, `variability`, `robustness`, `quotient`, `uniform`, `codec`. |
| C3 | 378 | Regulation, exclusion, destruction and compositional change | semantic/topic | High | `unconstitutional`, `destroys`, `requirement`, `unreasonable`, `exclude`, `inconsistent`, `precluded`, `creates`, `eliminated`, `Remove`, `combines`, `indistinguishable`; extremes include `Delete`, `reject`, `authority`, `composed`. |
| C4 | 285 | Common grammatical/function words, suffixes and lexical fragments | lexical/morphological | High | Dominated by `not`, `or`, `say`, with fragments `ia`, `ized`, `led`; extremes include `WHAT`, `HOW`, `omes`, `ancers`, `point`, `asked`. |
| C5 | 153 | Clinical diagnostics, anatomy and pathology | semantic/topic | High | `echocardiography`, `angiography`, `cerebellum`, `phenotypes`, `abdomen`, `epithelium`, `pelvis`, `symptoms`, `physiology`, `torso`, `epidermis`; extremes include `erythrocytes`, `allele`, `therapy`, `gait`. |
| C6 | 152 | Negative affect, tragedy, fear and loud/vocal expression | semantic/topic | High | `horrific`, `incredible`, `tragedy`, `stunning`, `disappointing`, `screamed`, `sadness`, `terrifying`, `furious`, `loud`, `scream`; extremes include `gloom`, `harsh`, `dissent`, `alarmed`, `audible`, `shouted`. |
| C7 | 144 | Personal names mixed with geographic/media entities | named-entity | Moderate | `Nick`, `Hicks`, `Smith`, `Lucy`, `Molly`, `Luke`, `Murphy`, `Palmer`, `Calgary`, `John`, `Kate`; extremes include `Violet`, `Telegraph`, `Mirror`, `Gates`, `borough`. |
| C8 | 120 | Mathematical/code punctuation and bracket formatting | formatting/tokenizer | High | 110 of 120 tokens are punctuation or symbols; examples include bracket/operator strings, percent notation, repeated punctuation and mathematical delimiters. |
| C9 | 115 | Low-level computing/electronics abbreviations and hardware tokens | semantic/topic | Moderate | `GCC`, `emitter`, `LED`, `GPIO`, `FFFF`, with extremes including `CI`, `HW`, `DP`, `LLP`; numerous short letter codes add lexical noise. |
| C10 | 108 | Numeric strings, especially historical years | numeric | High | `1884`, `1882`, `1890`, `1921`, `1900`, `1910`, `1870` plus shorter numeric values; extremes include `1840`, `407`, `0070`, `1100`. |
| C11 | 88 | Multilingual words, suffixes and orthographic fragments | lexical/morphological | High | `como`, `vý`, `cosa`, `sempre`, `apenas`, `que`, `amente`, `durante`, `guerra`, `cia`; extremes include `fazer`, `lado`, `acional` and accented fragments. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- administrative/evaluative/financial process language;
- interaction/process, software and physical-science material;
- biomedical/immune/psychiatric terminology;
- cities and names;
- daily work/time/renewal concepts;
- social/cultural/community descriptors;
- publishing and paratext language;
- travel/food/literature/biological material;
- grammar and lexical fragments;
- technical abbreviations;
- multilingual/tokenizer residues;
- formatting;
- numeric strings.

Four of thirteen communities receive a primary `semantic/topic`
classification. Three are mixed, two lexical/morphological, two
formatting/tokenizer, one named-entity and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- analysis/scientific description and technology;
- regulation/exclusion/compositional change;
- clinical diagnostics and anatomy;
- negative affect and vocal expression;
- low-level computing/electronics;
- names and geographic/media entities;
- built-environment/institutional/conflict material;
- grammatical and lexical fragments;
- multilingual morphology;
- mathematical formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — administration/evaluation, finance and task-resolution
  language overlap;
- **positive C1** — interaction/process, software and physical-science terms
  coexist;
- **positive C7** — travel, food, literature/culture and biological material
  share one broad partition;
- **positive C8** — daily work and seasonal/time concepts overlap;
- **negative C0** — built environment, institutional/religious and
  violence/conflict structures coexist;
- **negative C2** — analysis/scientific concepts overlap with technology and
  mathematical terms;
- **negative C7** — personal names dominate but geographic/media entities are
  substantial;
- **negative C9** — computing/electronics semantics are clear, but short
  letter-code structure remains strong.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
