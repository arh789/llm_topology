# R009 State 20 — block 19 output

## State identity

- R008 state index: `20`
- R008 state label: `block_19_output`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 12 | 12 | reconciled |
| negative_tail | 11 | 11 | reconciled |
| **Total** | **23** | **23** | **reconciled** |

The labels below answer only the first-order question, “What is this
community?” They do not assign SDA-3 roles or establish semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 369 | Personal names, cities and geographic/name-like entities | named-entity | Moderate | `Manchester`, `Scott`, `Matt`, `Peter`, `Mitchell`, `Kashmir`, `Karen`, `Hamburg`, Portuguese fragment, `Krish`; extremes include `Berlin`, `Kumar`, `Jake` and name fragments. `terrorists` and `fishermen` are semantic outliers. |
| C1 | 356 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `making`, `out`, with suffixes/fragments such as `ation`, `le`, `ine`, `l`, `it`; extremes include `ausing`, `ilation`, `Sort`, `Fresh`, `pages`. |
| C2 | 285 | Film/media production, photography, animation and online-platform systems | semantic/topic | High | `filmmakers`, `filmmaker`, `Bitmap`, `photography`, `Netflix`, `Notification`, `filming`, `Animation`, `facebook`, `Learning`, `writers`, `Play`; extremes include `Caption`, `Manager`, `animated`, `recorder`, `director`, `ajax`, `Photo`, `gradle`. |
| C3 | 275 | Exploration, entrepreneurship, motivation and emerging/developmental activity | semantic/topic | High | `exploring`, `entrepreneurs`, `motivations`, `motivation`, `happiness`, `anticipated`, `explores`, `discuss`, `yields`, `emerging`, `business`, `modulates`; extremes include `stake`, `dominant`, `recall`, `debated`, `derives`, `anticip`. |
| C4 | 263 | Biomedical, psychiatric, hospital and pharmacological terminology | semantic/topic | High | `breastfeeding`, `psychiat`, hospital fragments, `Sleep`, `dexamethasone`, `biomed`, `Medical`, `tumorigenesis`, `dopaminergic`, `Biomed`, `hospital`; extremes include `Lung`, `fluores`, `salivary` and `soybean` as an outlier. |
| C5 | 245 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 181 of 245 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `µm`, `triangle`, `INTRODUCTION`, `javase`, `mathchoice`. |
| C6 | 221 | Prefix/stem families around emergence, freshness, reappearance and negotiation | lexical/morphological | Moderate | Dominated by incomplete forms such as `inev`, `Emer`, `fres`, `unve`, `unavoid`, `reappe`, `Fres`, `Rele`, `snar`, `happ`, `negot`; extremes remain largely lexical stems such as `estim`, `refres`, `fluores`, `aberr`. |
| C7 | 186 | Interactions, measurements, quantification and system dynamics | semantic/topic | High | `interactions`, `Measurements`, `characterizing`, `Measurement`, `evolves`, `quantification`, `recorded`, `imaging`, `dynamics`, `simulations`, `develops`, `evolving`; extremes include `interaction`, `Geometry`, `sensing`, `outputs`. |
| C8 | 142 | Social/professional interaction mixed with food, retail and travel/leisure terms | mixed | Moderate | `Food`, `conversations`, `sessions`, `negotiating`, `interventions`, `interviews`, `adventures`, `shoppers`, `discussions`, `workshops`, `interviewing`; extremes include `students`, `funding`, `Tours`, `resorts`, `camping`, `Query`. |
| C9 | 138 | Discourse, temporal and comparative physical descriptors | semantic/topic | Moderate | `surprisingly`, `size`, `Recently`, `Clearly`, `Fall`, `larger`, `Next`, `widths`, `spacing`, `Now`, `older`; extremes include `dating`, `Day`, `Spring`, `Winter`, `suitably`, `obvious`. |
| C10 | 126 | Example-related multilingual words and morphological fragments | lexical/morphological | High | `ejemplo`, `exempl`, `Example`, `examples`, `Examples`, `exem`, `exemplified`, `quando`, `example`; extremes include `emplo`, `ün`, `äm`, replacement characters, Cyrillic fragments and `wieder`. |
| C11 | 121 | Numeric strings and short coded values | numeric | High | Dominated by `324`, `306`, `296`, `325`, `297`, `597`, `334`, `97`, `607`, `397`, `304`, `697`; extremes include `12345`, `473`, `2004`, `505`, `0023`, `633`, `499`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 577 | Characterisation, regulation, constitutional constraint and administrative concepts | semantic/topic | Moderate | `Characteristics`, `circumstantial`, `downregulation`, `recommendations`, `unconstitutional`, `encouragement`, `Constitution`, `administrators`, `Configuration`, `characteristics`, `circumstances`; extremes include `affirmative`, `Interior`, `variance`, `Executive`, `disadvantages`, `availability`. |
| C1 | 438 | Short name-like, technical and multilingual lexical fragments | lexical/morphological | Moderate | Dominated by short forms such as `Gh`, `GH`, `Rub`, `Kh`, `Rog`, `Tob`, `Tah`, `Bra`, `LH`, alongside `discour`, `arrog` and Arabic fragments; extremes include `crypt`, `heter`, `PROT`, `Comp`, `disc`. |
| C2 | 398 | Common grammatical/function words and multilingual lexical fragments | lexical/morphological | High | `I`, `or`, `said`, `some`, `different`, with fragments `ED`, `ra`, `RA`, `WHAT`, `TC`; extremes include `cette`, `Une`, Cyrillic fragments, `IMPLIED`, `FORE`, `ALE`. |
| C3 | 342 | Monarchy/religion and family roles mixed with vehicles, built environment and conflict | mixed | Moderate | `emperor`, `palace`, `warriors`, `chapel`, `cathedral`, `church`, `grandmother` coexist with `trucks`, `automobiles`, `chassis`, `gravel`; extremes include `Uncle`, `USSR`, `Beast`, `Universe`, `conspiracy`, `roofs`. |
| C4 | 300 | Cardiovascular disease, cytokine biology, immunology and pathology | semantic/topic | High | `cardiovascular`, `macrophage`, `cytokines`, `cytokine`, `interleukin`, `atherosclerotic`, `circumferential`, `epidemiological`, staphylococcus/sclerosis fragments, `erythrocytes`, `TNF`; extremes include `monocyte`, `gluc`, `physiology`, `thrombosis`. |
| C5 | 295 | Negative/intense evaluation, catastrophe and contradiction | semantic/topic | High | `incredible`, `stupid`, `occasionally`, `disastrous`, `unbelievable`, `brutal`, `frightening`, `spectacular`, `contradictory`, `Sometimes`; extremes include `uncommon`, `harsh`, `excessive`, `heavily`, `supreme`, `disappearing`. |
| C6 | 243 | Personal names mixed with geographic entities and regions | named-entity | High | `Sarah`, `Laura`, `Caroline`, `Emily`, `Connie`, `Jess` coexist with `Florida`, `Alabama`, `Louisiana`, `Mexico`; extremes include `Violet`, `Illinois`, `Canada`, `Friedrich`. |
| C7 | 171 | Encouragement, prohibition, removal, activation and verification/change actions | semantic/topic | High | `encourages`, `prohibiting`, `removing`, `resembled`, `Delete`, `prohibited`, `activates`, `verifying`, `created`, `received`, `creates`, `prohibits`; extremes include `submit`, `practicing`, `preceded`, `accorded`, `reflect`. |
| C8 | 95 | Numeric strings, especially historical years | numeric | High | Dominated by `441`, `1921`, `160`, `178`, `448`, `451`, `856`, `1919`, `651`, `140`; extremes include `1939`, `1840`, `980`, `40`, `fourteen`. |
| C9 | 60 | Mathematical/code punctuation and symbol formatting | formatting/tokenizer | High | 51 of 60 tokens are punctuation or symbols; examples include closing delimiters, percent notation, underscores, repeated exclamation/question marks and operator-like strings. |
| C10 | 29 | Rail transport terms mixed with developer/software tooling | mixed | Moderate | `Rails`, `rails`, `Rail`, `Railroad`, `Steam` coexist with `SSH`, `CLI`, `Ruby`, `Git`, `Unix`, `utils`; extremes add `Ethereum`, `pid` and `Git`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 4 |
| lexical/morphological | 2 |
| named-entity | 1 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- film/media production, photography and animation;
- exploration, motivation, entrepreneurship and emerging activity;
- biomedical/psychiatric/hospital terminology;
- interactions, measurements and quantitative/system dynamics;
- social/professional interaction mixed with food/retail/travel;
- discourse/temporal/comparative descriptors;
- names and geography;
- grammar and lexical fragments;
- emergence/freshness/reappearance stem families;
- example-related multilingual morphology;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- characterisation/regulation/constitutional-administrative concepts;
- cardiovascular/cytokine/immunological pathology;
- negative/intense evaluation;
- encouragement/prohibition/removal/change actions;
- names and geography;
- monarchy/religion/family roles mixed with vehicles and built environment;
- rail transport mixed with software/developer tooling;
- grammatical and fragmentary lexical structures;
- formatting;
- numeric strings.

Four of eleven communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C0** — names/geography dominate but semantic outliers remain;
- **positive C6** — emergence/freshness/reappearance concepts are visible, but
  incomplete word form is the stronger organising feature;
- **positive C8** — social/professional activity overlaps with food, retail and
  travel/leisure concepts;
- **positive C9** — discourse/temporal and comparative physical descriptors
  overlap;
- **negative C0** — characterisation, regulation and administrative concepts
  form a broad partition;
- **negative C1** — short name-like and technical/multilingual fragments are
  interleaved;
- **negative C3** — monarchy/religion/family roles coexist with vehicles,
  built-environment and conflict terms;
- **negative C6** — names and geographic entities are both substantial;
- **negative C10** — rail terminology and software/developer tooling share a
  small but clearly mixed partition.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
