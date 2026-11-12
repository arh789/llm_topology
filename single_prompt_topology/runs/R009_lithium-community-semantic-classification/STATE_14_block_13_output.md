# R009 State 14 — block 13 output

## State identity

- R008 state index: `14`
- R008 state label: `block_13_output`
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
| C0 | 411 | Fragmentary action/process terms and heterogeneous lexical residues | lexical/morphological | Moderate | Representatives include partial forms such as `remem`, `negot`, `reappe`, `happ`, `unve`, `maneu`, `Commiss`, alongside short name-like forms and replacement characters; extremes remain dominated by fragments such as `travers`, `sket`, `propri`, `prem`, `estim`. |
| C1 | 328 | Resolution, observation, inference and developmental process actions | semantic/topic | High | `resolving`, `characterizing`, `exploring`, `remembering`, `initiating`, `observing`, `computed`, `development`, `inferred`, `retrieved`, `develops`, `evolving`; extremes include `informed`, `recording`, `derives`, `noticing`, `recorder`, `Done`. |
| C2 | 321 | Common grammatical/function words and short lexical fragments | lexical/morphological | High | `as`, `at`, `back`, `making`, `right`, `found`, with suffixes/fragments such as `ation`, `ating`, `ling`, `ide`, `ne`; extremes include `ausing`, `ivated`, `tmp`, `met`, `systems`. |
| C3 | 287 | Biomedical, pharmacological, respiratory and reproductive terminology | semantic/topic | Moderate | `breastfeeding`, `dexamethasone`, `dopaminergic`, `ventilation`, `menopausal`, analgesic fragment, `salivary`, diazepam fragment, `pulmonary`, `pneum`; extremes include `fluores`, `airborne`, `mitotic`, `µm`, `dating` and `beet`. |
| C4 | 263 | Personal names and geographic entities | named-entity | High | `Manchester`, `Karen`, `Maria`, `Gary`, `Anne`, `Hamburg`, `Mitchell`, `Jennifer`; extremes include `Berlin`, `Krish`, `Gary`, `Greek` and name fragments. |
| C5 | 259 | Social/professional communication, negotiation and intervention | semantic/topic | Moderate | `conversations`, `negotiating`, `management`, `discussions`, `negotiation`, `psychosocial`, `interventions`, `psychiat`, `interviews`, `adventures`, `platforms`; extremes include `business`, `talks`, `director`, `Psychological`. |
| C6 | 250 | Mathematical/code punctuation and software-formatting strings | formatting/tokenizer | High | 158 of 250 tokens are punctuation or symbols; representatives include brace/operator strings and LaTeX-like fragments, with extremes such as `sizeof`, `mathchoice`, `javase`, `gradle`, `getElementById`. |
| C7 | 152 | Software/interface concepts mixed with measurement and technical abbreviations | mixed | Moderate | `facebook`, `Entry`, `DB`, `Permission`, `Amazon` coexist with `size`, `Radius`, `Length`, `volume`, and abbreviations such as `PB`, `PRES`, `NE`, `BW`, `RAW`, `BA`. |
| C8 | 110 | Numeric strings, including years | numeric | High | Dominated by `324`, `596`, `624`, `96`, `604`, `496`, `597`, `334`, `796`, `1986`, `295`, `504`; extremes include `505`, `1997`, `2019`, `737`, `0023`. |
| C9 | 109 | Interactions, measurements and physical/mathematical system dynamics | semantic/topic | High | `interactions`, `interacting`, `phenomenological`, `Measurements`, Lagrangian fragment, `perturbative`, `responses`, `renormalization`, `transforms`, `interaction`, `actions`; extremes include `Spin`, `Phase`, `magnetic`, `sensing`. |
| C10 | 79 | Publishing, reading, writing and acknowledgement/paratext language | semantic/topic | High | `Acknowledgements`, `Working`, `Books`, pamphlet fragment, `Read`, `writers`, `Writing`, `Bibliography`, `References`; extremes include `Posted`, `Caption`, `quoted`, `Thanks`, `Reading`, `Appendix`, `Springer`. |
| C11 | 53 | Multilingual suffixes, example-related words and morphological fragments | lexical/morphological | High | `exem`, `ejemplo`, `Para`, `ución`, `ados`, `iques`, `iera`; extremes include `example`, `uesta`, `ivos`, `arios` and Cyrillic/Spanish-like fragments. |
| C12 | 30 | Bodily gestures, affective actions and ringing/sound events | semantic/topic | High | `trembling`, `smiled`, `shook`, `kissed`, `swung`, `grinned`, `rings`, `paused`, `swallowed`, `kissing`, `gripped`, `squeezing`; extremes include `rang`, `struck`, `ring`, `ringing`, `shake`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 579 | Characterisation, recommendations, regulation and system/distribution concepts | semantic/topic | Moderate | `Characteristics`, `unconstitutional`, `characteristics`, `downregulation`, `recommendations`, `encouragement`, `availability`, `distribution`, `circumstances`, `Constitution`, `algorithms`; extremes include `specificity`, `variance`, `codes`, `submit`, `disadvantages`. |
| C1 | 484 | Catastrophe, discrimination, prohibition/exclusion and intense evaluation | semantic/topic | High | `disastrous`, `circumstantial`, `catast`, `discriminatory`, `unbelievable`, `prohibiting`, `incredible`, `catastrophe`, `emphasizing`, `exclude`, `excluding`; extremes include `harsh`, `heavily`, `supreme`, `excessive`, `malware`. |
| C2 | 421 | Personal names mixed with biomedical/technical fragments | named-entity | Moderate | `Caroline`, `Jess`, `Claude`, `Claud`, `Connie`, `Betty`, `Molly` coexist with fragments such as `cytok`, `cortic`, `fluor`, `crypt`, `gluc`, `PROT`. |
| C3 | 386 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `not`, `I`, `or`, `than`, with fragments `e`, `ized`, `ian`, `ED`, `ta`; extremes include `WHAT`, `HOW`, `ALLY`, multilingual fragments and an empty token. |
| C4 | 237 | Cardiovascular disease, trauma, pathology and biomedical morphology | semantic/topic | High | `cardiovascular`, `atherosclerotic`, staphylococcus fragment, immunofluorescence fragment, `trauma`, sclerosis fragment, `interleukin`, `angiography`, `colonic`, `dysfunction`, `morphology`; extremes include `physiology`, `monocyte`, `dimer`. |
| C5 | 209 | Religion, monarchy, family and mythic/fantastical roles | mixed | Moderate | `theology`, `emperor`, `mother`, `grandmother`, `palace`, `cathedral`, `church`, `Empire`, `queen`, `King`, `priest`, `creature`; extremes include `Uncle`, `throne`, `Beast`, `wedding`, `heavens`, `saint`, `serpent`. |
| C6 | 162 | Vehicles, roads, natural terrain and household/material objects | mixed | Moderate | `uniforms`, `trucks`, `automobiles`, `roadway`, `cliffs`, `woods`, `sidewalk`, `driveway`, `mountains`, `whiskey`, `vegetables`, `gravel`; extremes include `barrel`, `quilt`, `cloth`, `roofs`, `cassette`, `ignition`, `rug`. |
| C7 | 134 | Hardware, electronics, appliances and infrastructure equipment | semantic/topic | High | `chassis`, `hardware`, `appliances`, `Rails`, `furniture`, `bulbs`, with abbreviations such as `TG`, `ACC`, `EC`, `TC`, `SL`; extremes include `SSH`, `LCD`, `CPU`, `lamp`, `RF`, `Rail`. |
| C8 | 120 | Numeric strings, including historical years | numeric | High | Dominated by `448`, `1860`, `1890`, `952`, `451`, `1880`, `856`, `1870`, `160`, `140`; extremes include `1840`, `1866`, `407`, `001`, `Years`. |
| C9 | 67 | Geographic/political entities mixed with legal/historical terms | mixed | Moderate | `Pennsylvania`, `Connecticut`, `Alabama`, `Florida`, `Minnesota`, `Georgia`, `province`, `Louisiana`, `Arkansas`, `Colonial` coexist with `misdemeanor`; extremes include `Canada`, `Territory`, `Montreal`, `Putin`, `USSR`. |
| C10 | 66 | Algebra, topology, subsets and continuity | semantic/topic | High | `comparing`, `subsets`, `continuity`, `continuous`, `Continuous`, `ideals`, `category`, `subset`, `polynomials`; extremes include `algebra`, `quotient`, `diag`, `topology`, `polynomial`. |
| C11 | 47 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 44 of 47 tokens are punctuation or symbols; examples include percent notation, closing delimiters, repeated underscores and operator strings. |
| C12 | 21 | Multiplicity/multi- lexical forms mixed with software status/message tokens | mixed | Moderate | `Multiple`, `multiple`, `multitude`, `multi`, `Mult`, `multif`, `hundreds` coexist with `MESSAGE`, `ERROR`, `CURRENT`, `Current`; extremes include `Default`, `DEFAULT`, `WARN`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 1 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 4 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- resolution, observation, inference and developmental actions;
- biomedical/pharmacological and respiratory terminology;
- social/professional communication and intervention;
- physical/mathematical interactions and measurements;
- publishing/reading/writing language;
- bodily/affective actions;
- personal names and geography;
- software/interface mixed with measurement concepts;
- grammar and lexical fragments;
- multilingual morphology;
- formatting;
- numeric strings.

Six of thirteen communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- characterisation, recommendation and regulation/system concepts;
- catastrophe, discrimination and prohibition;
- cardiovascular/pathology concepts;
- hardware/electronics and infrastructure;
- algebra/topology and continuity;
- names mixed with biomedical/technical fragments;
- religion/monarchy/family/mythic roles;
- vehicles/terrain/household-object material;
- geographic/political/legal/historical material;
- multiplicity plus software-status language;
- grammar/lexical fragments;
- formatting;
- numeric strings.

Five of thirteen communities receive a primary `semantic/topic`
classification. Four are mixed, one lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — fragmentary process vocabulary and heterogeneous lexical
  residue coexist;
- **positive C3** — biomedical terminology dominates but several non-medical
  outliers remain;
- **positive C5** — social/professional communication overlaps with
  psychosocial and platform-related language;
- **positive C7** — software/interface and measurement/technical-abbreviation
  structures coexist;
- **negative C0** — characterisation, regulatory and distribution/system
  concepts overlap;
- **negative C2** — names dominate but biomedical/technical fragments are
  substantial;
- **negative C5** — religion, monarchy, family and mythic roles coexist;
- **negative C6** — vehicles/terrain and household/material objects share a
  broad physical-world partition;
- **negative C9** — geographic entities overlap with political/legal/historical
  terms;
- **negative C12** — multi-/multiplicity morphology overlaps with software
  status/message tokens.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
