# R009 State 16 — block 15 output

## State identity

- R008 state index: `16`
- R008 state label: `block_15_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 11 | 11 | reconciled |
| negative_tail | 12 | 12 | reconciled |
| **Total** | **23** | **23** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 544 | Personal names and geographic/name-like entities with lexical residue | named-entity | Moderate | Strong name/place content includes `Manchester`, `Jay`, `Mitchell`, `Karen`, `Hamburg`, `Berlin`, `Krish`, alongside partial forms such as `remem`, `Portug`, `Compan`, `prem` and multilingual fragments. |
| C1 | 419 | Transformations, interactions, exploration and developmental/measurement processes | semantic/topic | High | `transformations`, `interactions`, `exploring`, `anticipated`, `development`, `Measurements`, `resolving`, `characterizing`, `discuss`, `ignored`, `evolving`, `recorded`; extremes include `informed`, `recall`, `bridging`. |
| C2 | 294 | Food/health and affective-social experience mixed with interviews and interventions | mixed | Moderate | `Food`, `breastfeeding`, `happiness`, `adventures`, `negotiating`, `discomfort`, `interviews`, `conversations`, `compassion`, `remembering`, `mindfulness`, `interventions`; extremes include `business`, `resorts`, `kissed`, `students`. |
| C3 | 264 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `into`, `back`, `making`, `right`, with suffixes/fragments such as `ation`, `ating`, `ine`, `le`, `ling`; extremes include `ausing`, `ilation`, `ines`, `ivated`. |
| C4 | 243 | Biomedical, respiratory, imaging and analgesic/psychiatric terminology | semantic/topic | High | `dexamethasone`, `pulmonary`, `fibers`, `analgesic`, `imaging`, `pneum`, `designing`, `ventilation`, `psychiat`, `analges`, `Bio`; extremes include `airborne`, `µm`, `sensing`, `mitotic`, `lact`. |
| C5 | 192 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 161 of 192 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `leq`, bracket fragments and repeated symbolic operators. |
| C6 | 177 | Management/platform/software and technical publishing/interface terms | mixed | Moderate | `management`, `Notification`, `platforms`, `Length`, `PhysRev`, `Resolver`, `javase`, `setlength`, `Address`; extremes include `sizeof`, `mathchoice`, `pages`, `Manager`, `director`, `gradle`, `Query`, `pcbi`. |
| C7 | 121 | Temporal/discourse sequencing, evaluation and action language | semantic/topic | Moderate | `Next`, `Got`, `With`, `adopting`, `More`, `Clearly`, `Now`, `Wednesday`, `Working`; extremes include `Coming`, `obvious`, `True`, `thank`. |
| C8 | 110 | Reappearance, renewal/transformation and bodily/sound actions | mixed | Moderate | `reappe`, `unve`, `reconst`, `fres`, `Fresh`, `diseng`, `rings`, `Hit`, `swung`, `conjug`, `maneu`, `recycling`; extremes include `recycled`, `refres`, `sprang`, `rang`, `ring`. |
| C9 | 109 | Numeric strings and short coded values | numeric | High | Dominated by `334`, `306`, `597`, `324`, `325`, `624`, `295`, `604`, `0024`, `616`, `87`; extremes include `505`, `12345`, `633`, `1947`, `0023`, `1997`. |
| C10 | 77 | Example-related multilingual words and morphological fragments | lexical/morphological | High | `exempl`, `ejemplo`, `exem`, `Example`, `quando`, `wir`; extremes include `example`, `wij`, `emplo`, `nuest`, `där`, `bij`, `wieder`, `Para`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 3 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 3 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 522 | Characterisation, configuration, regulation and recommendation language | semantic/topic | Moderate | `Characteristics`, `circumstantial`, `downregulation`, `unconstitutional`, `Configuration`, `recommendations`, `discriminatory`, `encouragement`, `regulations`, `prohibiting`, `Comprehensive`; extremes include `specificity`, `enactment`, `Executive`, `availability`, `Insurance`. |
| C1 | 408 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `they`, `WHAT`, `THIS`, `some`, with fragments `ized`, `ED`, `ra`, `ABLE`; extremes include `cette`, `Une`, Cyrillic/other multilingual fragments and short codes. |
| C2 | 314 | Personal names mixed with lexical fragments | named-entity | Moderate | `Claire`, `Caroline`, `Theod`, `Betty`, `Connie`, `Sarah`, `Claude` coexist with fragments such as `catast`, `GH`, `Kh`; extremes include `Violet`, `Maur` and multilingual fragments. |
| C3 | 253 | Cardiovascular disease, immunology, epidemiology and pathology | semantic/topic | High | `cardiovascular`, `atherosclerotic`, `macrophage`, `erythrocytes`, `epidemiological`, sclerosis/staphylococcus fragments, `monocyte`, `morphology`, `lymphocytes`, `fractures`; extremes include `physiology`, `epithelial`, `derm`. |
| C4 | 215 | Evaluative intensity, catastrophe and degree/frequency language | semantic/topic | High | `disproportionate`, `unbelievable`, `disastrous`, `incredible`, `catastrophic`, `Excellent`, `Sometimes`, `occasionally`, `enthusiastic`, `fortunately`, `brutal`; extremes include `harsh`, `heavily`, `excessive`, `intense`, `logically`. |
| C5 | 201 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `circumferential`, `trucks`, `chassis`, `gravel`, `automobiles`, `roadway`, `vegetables`, `Rails`, `cylinder`, `driveway`, `terrace`; extremes include `curb`, `dishes`, `ignition`, `barrel`, `cassette`, `roofs`. |
| C6 | 160 | Distribution, uniformity, probability and mathematical/statistical relations | semantic/topic | High | `representation`, `distribution`, `uniforms`, `uniformity`, `perpendicular`, `distributions`, `contradictory`, `probability`, `improper`, `inconsistent`; extremes include `variance`, `algebra`, `ideals`, `lottery`, `multiplied`, `equitable`. |
| C7 | 159 | Geography, civic institutions and national/political identity | semantic/topic | Moderate | `Constitution`, `Alabama`, `Philadelphia`, `Louisiana`, `Florida`, `Americans`, `Chicago`, `Iowa`, `Edinburgh`, `nationalist`; extremes include `Illinois`, `Interior`, `Africans`, `USSR`. |
| C8 | 130 | Monarchy, religion, family and mythic/fantastical roles | mixed | Moderate | `emperor`, `queen`, `cathedral`, `palace`, `Sultan`, `church`, `Empire`, `grandmother`, `dragon`, `prince`, `goddess`, `mother`; extremes include `Beast`, `Guardian`, `wedding`, `saint`, `rituals`, `heavens`, pharaoh fragment. |
| C9 | 120 | Technical/computing abbreviations and code-like fragments | lexical/morphological | Moderate | Dominated by `TG`, `TC`, `GGT`, `ACC`, `COMP`, `LG`, `Comp`, `LCD`, `SCC`, `comp`; extremes include `crypt`, `codec`, `SSH`, `codes`, `CPU`, `PROT`, `IMPLIED`. |
| C10 | 104 | Numeric strings, especially historical years | numeric | High | Dominated by `451`, `272`, `1860`, `448`, `441`, `1890`, `856`, `128`, `1920`, `1919`; extremes include `980`, `1866`, `082`, `001`, `Years`. |
| C11 | 57 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 45 of 57 tokens are punctuation or symbols; examples include bracket/percent strings, repeated punctuation, long dash strings, quotation residues and operator-like forms. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- transformation, interaction, exploration and development processes;
- biomedical/respiratory/imaging terminology;
- temporal/discourse sequencing;
- management/software/platform and technical publishing material;
- food/health/social-experience material;
- reappearance/renewal and bodily/sound actions;
- personal names and geography;
- common grammar and lexical fragments;
- example-related multilingual fragments;
- formatting;
- numeric strings.

Three of eleven communities receive a primary `semantic/topic`
classification. Three are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- characterisation/configuration/regulation language;
- cardiovascular/immunological pathology;
- evaluative intensity and catastrophe;
- vehicles, roads and material objects;
- distribution/probability/mathematical relations;
- geography/civic/national identity;
- monarchy/religion/family/mythic roles;
- personal names;
- grammatical and technical lexical fragments;
- formatting;
- numeric strings.

Six of twelve communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — name/geographic structure is strong but lexical residue is
  substantial;
- **positive C2** — food/health and affective-social/intervention language
  coexist;
- **positive C6** — management/platform/software and technical-publishing
  concepts overlap;
- **positive C7** — temporal sequencing, evaluation and action language share
  one broad partition;
- **positive C8** — renewal/transformation and bodily/sound-action terms
  coexist;
- **negative C0** — regulatory, descriptive and administrative concepts
  overlap;
- **negative C2** — names dominate but lexical fragments remain substantial;
- **negative C5** — several physical-world object classes share one broad
  partition;
- **negative C7** — geographic, civic and national/political identity terms
  overlap;
- **negative C8** — monarchy, religion, family and mythic roles coexist;
- **negative C9** — technical semantics are evident but abbreviated form is
  the dominant organising feature.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
