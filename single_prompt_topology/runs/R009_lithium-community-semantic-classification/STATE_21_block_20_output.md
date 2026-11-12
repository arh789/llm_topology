# R009 State 21 — block 20 output

## State identity

- R008 state index: `21`
- R008 state label: `block_20_output`
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
| C0 | 435 | Personal names, cities and geographic/name-like entities | named-entity | High | `Steve`, `Scott`, `Matt`, `Peter`, `Karen`, `Josh`, `Manchester`, `Mitchell`, `Nam`, `Jake`, `Kashmir`, `Jay`; extremes include `Berlin`, `Kumar`, `Krish` and name fragments. |
| C1 | 345 | Common grammatical/function words and lexical fragments | lexical/morphological | High | `as`, `at`, `more`, `into`, `making`, with fragments/suffixes such as `ation`, `le`, `ine`, `l`, `it`; extremes include `ilation`, `ausing`, `Sort`, `building`, `outputs`, `Spiel`. |
| C2 | 340 | Exploration, measurement, characterisation, motivation and developmental processes | semantic/topic | High | `exploring`, `Measurements`, `characterizing`, `quantification`, `motivations`, `Measurement`, `anticipated`, `recorded`, `motivation`, `adventures`, `resolving`, `characterize`; extremes include `stake`, `debated`, `recall`, `sensing`, `derives`. |
| C3 | 298 | Interaction, evolution, emergence and theoretical-system concepts | semantic/topic | Moderate | `interactions`, `evolves`, `evolving`, `phenomenological`, `interacting`, `renormalization`, `Emer` coexist with inevitability/reappearance stems such as `inev`, `unavoid`, `unve`, `reappe`; extremes include `tension`, `anchors`, `interaction`, `anticip`, `unpack`. |
| C4 | 276 | Biomedical, psychiatric, immunological and pharmacological terminology | semantic/topic | High | `breastfeeding`, `dopaminergic`, `psychiat`, hospital fragment, `Medical`, `immunostaining`, `Biomed`, `dexamethasone`, diazepam fragment, `tumorigenesis`, `analgesic`, `doxorubicin`; extremes include `hospital`, `fluores`, `Lung`. |
| C5 | 247 | Social/professional, creative and commercial activity mixed with food and travel | mixed | Moderate | `Food`, `sessions`, `entrepreneurs`, `filmmakers`, `interventions`, `conversations`, `shops`, `negotiating`, `Travel`, `filmmaker`, `Animation`, `business`; extremes include `students`, `director`, `interviewing`, `Business`, `pages`. |
| C6 | 246 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 169 of 246 tokens are punctuation or symbols; representatives are dominated by brace/operator and LaTeX-like strings, with extremes including `triangle`, `INTRODUCTION`, `javase`, `mathchoice` and symbolic fragments. |
| C7 | 172 | Media/software/interface terms mixed with size, position and layout concepts | mixed | Moderate | `photography`, `facebook`, `Photo`, `Netflix`, `Notification`, `Address`, `Position`, `Session`, `browsers` coexist with `widths`, `spacing`, `Size`; extremes include `Caption`, `Manager`, `ajax`, `NET`, `IE`, `stdio`, `gradle`. |
| C8 | 124 | Numeric strings and short coded values | numeric | High | Dominated by `296`, `597`, `324`, `297`, `325`, `334`, `596`, `397`, `306`, `97`, `592`, `300`; extremes include `12345`, `473`, `2004`, `0023`, `499`, `530`. |
| C9 | 118 | Temporal, freshness, analytical and evaluative descriptors | semantic/topic | Moderate | `surprisingly`, `fres`, `Fresh`, `Recently`, `analytically`, `clinically`, `Feb`, `intuitive`, `score`, `older`, `Wednesday`; extremes include `Fast`, `Day`, `Spring`, `Winter`, `suitably`, `obvious`. |
| C10 | 69 | Affect, consciousness, sleep, compassion and bodily/social actions | semantic/topic | High | `happiness`, `consciousness`, `discomfort`, `Sleep`, `kissing`, `sleeping`, `Hit`, `swung`, `compassion`, `aspirations`, `pleasure`; extremes include `smiled`, `peace`, `inclination`, `patience`, `kissed`. |
| C11 | 36 | Example-related multilingual words and morphological fragments | lexical/morphological | High | `exempl`, `ejemplo`, `examples`, `Examples`, `Example`, `exem`, `example`, `ario`, `ito`, `ismo`; extremes include `emplo`, Cyrillic fragments, `atas`, `uesta`, `arios`. |

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
| C0 | 580 | Administrative characterisation, recommendations, regulation and constitutional concepts | semantic/topic | Moderate | `Characteristics`, `recommendations`, `administrators`, `Configuration`, `characteristics`, `unconstitutional`, `beneficiaries`, `regulations`, `Constitution`, `encouragement`; extremes include `privileges`, `Executive`, `availability`, `Interior`, `complimentary`. |
| C1 | 407 | Common grammatical/function words mixed with multilingual lexical/token fragments | lexical/morphological | High | `I`, `or`, `said`, `different`, `some`, with short forms `B`, `ED`, `ra`, `ao`, `M`; extremes include `cette`, `Une`, Cyrillic/Asian fragments and replacement characters. |
| C2 | 396 | Short name-like and technical/code abbreviations | lexical/morphological | Moderate | `GH`, `Cl`, `RA`, `Bra`, `Gh`, `Tob`, `Hu`, `Tah`, `Gu`, `Rh`, `Rog`, `TC`; extremes include `CI`, `crypt`, `PROT`, `COMP`, `Maur`, `HF`. |
| C3 | 303 | Downregulation, removal, encouragement, prohibition and verification/change actions | semantic/topic | High | `downregulation`, `removing`, `encourages`, `prohibiting`, `resembled`, `Delete`, `creates`, `prohibited`, `discour`, `prohibits`, `undermined`, `verifying`; extremes include `enactment`, `preceded`, `practicing`, `accorded`. |
| C4 | 277 | Negative/intense evaluation, catastrophe and discrimination | semantic/topic | High | `unreasonable`, `disastrous`, `incredible`, `occasionally`, `stupid`, `spectacular`, `unbelievable`, `discriminatory`, `frightening`, `exceedingly`; extremes include `uncommon`, `excessive`, `harsh`, `supreme`, `heavily`. |
| C5 | 271 | Vehicles, roads, built environment and material/household objects | semantic/topic | Moderate | `trucks`, `automobiles`, `roads`, `circumferential`, `vegetables`, `cylinder`, `gravel`, `pavement`, `chassis`, `firearms`, `Mountains`, `sidewalk`; extremes include `cassette`, `curb`, `rails`, `dishes`, `blankets`, `roofs`. |
| C6 | 246 | Personal names mixed with geographic entities and regions | named-entity | High | `Laura`, `Alabama`, `Sarah`, `Caroline`, `Florida`, `Louisiana`, `Emily`, `Claire`, `Arkansas`, `Canada`; extremes include `Violet`, `Illinois`, `Friedrich`, `Georgia`. |
| C7 | 234 | Monarchy, bureaucracy, religion, family and political/mythic roles | mixed | Moderate | `emperor`, `bureaucracy`, `palace`, `chapel`, `grandmother`, `church`, `Americans`, `mother`, `warriors`, `cathedral`, `Sultan`, `king`; extremes include `USSR`, `conspiracy`, `Africans`, `Beast`, `Stalin`, `Lady`, `Spirit`. |
| C8 | 218 | Cardiovascular disease, cytokine biology and biomedical pathology | semantic/topic | High | `cardiovascular`, `cytokines`, `cytokine`, staphylococcus fragment, `interleukin`, `lipids`, `monocyte`, `gluc`, sclerosis fragment, `lymphocyte`, `atherosclerotic`; extremes include `physiology`, `thrombosis`, `Fc`, `oxides`. |
| C9 | 113 | Numeric strings, especially historical years | numeric | High | Dominated by `10`, `1921`, `25`, `20`, `160`, `140`, `441`, `856`, `448`, `1919`, `451`, `651`; extremes include `1939`, `1840`, `601`. |
| C10 | 110 | Uppercase lexical stems, modal/status terms and code-like fragments | lexical/morphological | High | `CE`, `ERS`, `ABLE`, `NEVER`, `ACK`, `THIS`, `UAL`, `SOME`, `OW`, `ENTS`, `doesnt`; extremes include `ITS`, `codes`, `codec`, `IMPLIED`, `FORE`, `ALE`, `IDENT`, `BLOCK`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 3 |
| named-entity | 1 |
| formatting/tokenizer | 0 |
| mixed | 1 |
| numeric | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- exploration, measurement, characterisation and motivation;
- interaction, evolution and theoretical-system concepts;
- biomedical/psychiatric/pharmacological terminology;
- social/professional/creative/commercial activity;
- media/software/interface and layout concepts;
- temporal/freshness/analytical descriptors;
- affect/consciousness/sleep and bodily/social actions;
- names and geography;
- grammar and lexical fragments;
- example-related multilingual morphology;
- formatting;
- numeric strings.

Five of twelve communities receive a primary `semantic/topic`
classification. Two are mixed, two lexical/morphological, one named-entity,
one formatting/tokenizer and one numeric.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- administrative/regulatory/constitutional characterisation;
- downregulation/removal/prohibition/change actions;
- negative/intense evaluation;
- vehicles, roads and material objects;
- cardiovascular/cytokine biomedical pathology;
- names and geographic regions;
- monarchy/bureaucracy/religion/family/political roles;
- grammatical and code-like lexical fragments;
- numeric strings.

Five of eleven communities receive a primary `semantic/topic`
classification. Three are lexical/morphological, one mixed, one named-entity
and one numeric.

Negative anti-alignment again contains structured semantic material alongside
mixed and non-semantic organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C3** — interaction/evolution concepts overlap with emergence,
  inevitability and reappearance stems;
- **positive C5** — social/professional, creative, food, travel and commercial
  concepts coexist;
- **positive C7** — media/software/interface concepts overlap with physical
  layout and dimension terms;
- **positive C9** — temporal/freshness, analytical and evaluative descriptors
  overlap;
- **negative C0** — administrative, regulatory and constitutional concepts
  share a broad partition;
- **negative C2** — short name-like and technical abbreviations are interleaved;
- **negative C5** — several physical-world object classes share one broad
  partition;
- **negative C6** — personal names and geographic entities are both substantial;
- **negative C7** — monarchy, bureaucracy, religion, family and political/mythic
  roles coexist;
- **negative C10** — natural-language stems and code/status abbreviations are
  interleaved.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier or later states, persistence claim, emergence
claim, SDA-3 role, coherence judgement or curvature interpretation is made in
this file.
