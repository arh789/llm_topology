# R009 State 32 — final normalization after block 31

## State identity

- R008 state index: `32`
- R008 state label: `final_norm_after_block_31`
- R008 state type: `final_normalized_output`
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
| C0 | 473 | Common grammatical/function words, punctuation-adjacent forms and lexical fragments | lexical/morphological | High | `s`, `er`, `that`, `as`, `is`, `be`, `at`, numerals and punctuation dominate; extremes include `find`, `roll`, `ines`, `charge`, `catch`, `link`, `choice`. |
| C1 | 386 | Biomedical, psychological, materials/physical-science and systems terminology | mixed | Moderate | `ferromagnetic`, `microorganisms`, antidepressant fragment, `psychosocial`, `decentralized`, `dopaminergic`, `renormalization`, antioxidant fragment, `rotation`, `conductivity`, `echocardiography`; extremes include `magnetic`, `CNT`, `social`, `periodontal`, pulmonary and biochemical fragments. |
| C2 | 366 | Data, testing, measurement, problem-solving and process/interface concepts | semantic/topic | High | `data`, `detecting`, `manager`, `problem`, `Size`, `test`, `Measurement`, `process`, `problems`, `tests`, `Manager`, `mask`; extremes include `Tests`, `DATA`, `imaging`, `resolve`, `memory`, `exit`, `pages`, `height`. |
| C3 | 271 | Numeric strings and coded numeric values | numeric | High | Dominated by `0033`, `389`, `0013`, `442`, `0032`, `0024`, `797`, `793`, `0014`, `393`, `0037`; extremes remain numeric strings such as `3333`, `532`, `422`, `517`, `510`, `0009`, `524`. |
| C4 | 250 | Reporting, acknowledgement, recording, video/photo and paratext/publishing activity | semantic/topic | High | `Acknowledgements`, `reported`, `acknowledges`, `explained`, `recorded`, `Acknowledgments`, advertisement fragment, video fragment, `acknowledge`, `Video`, `bibliography`, `photos`; extremes include `listed`, `Reading`, `recorder`, `recording`, `stereo`, `Photo`, `Images`. |
| C5 | 243 | Mathematical/code punctuation and symbolic formatting | formatting/tokenizer | High | 220 of 243 tokens are punctuation or symbols; representatives and extremes are dominated by brace/operator, delimiter, separator and repeated-rule strings. |
| C6 | 242 | Geographic entities and multilingual/name morphology | mixed | Moderate | `Bangladesh`, `Brazil`, `Pakistan`, `Mumbai`, `Brisbane` coexist with Portuguese/Italian/Spanish-like suffixes and fragments such as `ação`, `ações`, `izione`, `iones`, `ções`, `ución`; extremes include surname/name fragments. |
| C7 | 230 | Acquisition, retrieval, insertion, transfer, extraction and rejection/change operations | semantic/topic | High | `withdrawing`, `retrieved`, `inserting`, `transfer`, `acquisition`, `extracting`, `frustration`, `acquiring`, `rejecting`; extremes include `retrieved`, `interactions`, `omitted`, exchange fragment and `Protect`. |
| C8 | 225 | Computing hardware, networking, storage and software/platform terminology | semantic/topic | High | Kubernetes fragment, `MySQL`, `wifi`, `SSD`, `install`, `FD`, `Debian`, `80211`; extremes include `inode`, `install`, `rpm`, `HD` and additional hardware/software abbreviations. |
| C9 | 192 | Children/family, education and organisational/participant-management concepts | semantic/topic | Moderate | `breastfeeding`, `baby`, `preschool`, `instructors`, `girls`, `petitioners`, `Participants`, `manager`, `adolescents`, `management`, `supported`, `children`; extremes include `newborn`, `family`, `vacation`, `bidding`, `betting`. |
| C10 | 30 | Historical/calendar years and wartime references | numeric | High | `1966`, `1959`, `1942`, `1996`, `1994`, `1944`, `1948`, `1941`, `1952`, `1981`, `1978`, `wartime`; extremes include `1913`, `2016`, `1943`, `1995`, `1897`, `1934`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 5 |
| lexical/morphological | 1 |
| named-entity | 0 |
| numeric | 2 |
| formatting/tokenizer | 1 |
| mixed | 2 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 427 | Characterisation, differences, assessment and structural/category descriptors | semantic/topic | Moderate | `Characteristics`, `recommendations`, `characteristics`, `brutality`, `singularities`, `differences`, `alterations`, `assessments`, `Architecture`, `complexities`, `categories`; extremes include `Meaning`, `correlated`, `variant`, `grades`, `equilibrium`, `maturity`, `weights`. |
| C1 | 405 | Personal names and name-like entities | named-entity | High | `Diana`, `Maggie`, `Emily`, `Molly`, `Carrie`, `Smith`, `Diane`, `Rober`, `Jon`, `Harris`, `Eleanor`, `Connie`; extremes include `Peggy`, `Sierra`, `Hammond` and a few lexical/noise fragments. |
| C2 | 308 | Extreme evaluation, tragedy, splendour and distress/intensity language | semantic/topic | High | `extraordinarily`, `tragedy`, `spectacular`, `glorious`, brilliance/magnificence fragments, `ridiculous`, `realities`, `particularly`, `incredibly`, `desperately`; extremes include `agony`, `detriment`, `jeopard`, `enthusiastic`, `severe`. |
| C3 | 304 | Short action/institutional stems and technical lexical fragments | lexical/morphological | Moderate | `discour`, `Exper`, `Cro`, `encour`, `Comp`, `incor`, `Sp`, `TA`, `perpet`, `WOR`, `Tra`, `contem`; extremes include `CI`, `tetra`, `multif`, `conv`, `VER`, `Stra`, `legis` and malformed fragments. |
| C4 | 299 | Deterioration, increase/decrease, destruction and attempted/compelled change actions | semantic/topic | High | `dropped`, `screamed`, `deteriorated`, `increased`, `altering`, `destroying`, `detrimental`, `resembling`, `attempting`, `dropping`, `constituted`; extremes include `compelled`, `prohibiting`, `mandatory`, `Injury`, `collaborated`. |
| C5 | 268 | Inflammation, pathology, hypersensitivity and disease mechanisms | semantic/topic | High | `abnormalities`, `proinflammatory`, `pathophysiology`, `inflammation`, `hypersensitivity`, `pathology`, `physiology`, `responsiveness`, `pathogenesis`, `arthritis`, `cytotoxicity`; extremes include `preclinical`, `edema`, `hyperplasia`, `lesions`, `dementia`, `COX`. |
| C6 | 224 | Monarchy, religion, prophecy and ceremonial/mythic roles | semantic/topic | High | `emperor`, `King`, `palace`, `righteousness`, `Emperor`, `Princess`, `warriors`, `Sultan`, `cathedral`, `dragon`, prophecy fragment, `ceremonies`; extremes include `Duke`, `Lion`, `repent`, `dragons`, `preach`, `throne`, `statue`, `honors`. |
| C7 | 205 | Built environment, clothing, terrain and material/household objects | semantic/topic | Moderate | `walls`, `automobiles`, `robes`, `buildings`, `clothing`, `mountains`, `vegetables`, `furniture`, `roads`, `garments`, `hills`; extremes include `bolts`, `cliffs`, `dishes`, `firearms`, `coat`, `palms`, `flange`. |
| C8 | 149 | Civic/government roles, local administration and social hierarchy | semantic/topic | High | `governor`, `Mayor`, `neighbourhood`, `poverty`, `legislature`, `sheriff`, `experts`, `captain`, `mayor`, `chairman`, `Stalin`; extremes include `Chairman`, `officials`, `advisor`, `elites`, `Nixon`, `consultant`, `Putin`, `money`. |
| C9 | 139 | Multilingual suffixes, function words and orthographic fragments | lexical/morphological | High | English suffixes `ity`, `ance`, `ability` coexist with `cette`, `durante`, German `wenn`/`nicht`/`werden`, `Die`, `cual`, `Jeg`, `comme` and other multilingual fragments. |
| C10 | 123 | Mathematical/code punctuation, operators and tokenizer residue | formatting/tokenizer | High | 60 of 123 tokens are punctuation or symbols; representatives include delimiter/operator strings, `implies`, `subseteq`, template syntax and multilingual encoding residue; extremes include rule strings, `syscall`, `rfloor` and symbol-heavy fragments. |
| C11 | 91 | Scientific/geographic/cognitive and identity-related descriptors | mixed | Moderate | `architectural`, `heterosexual`, `scientifically`, `geographical`, `scientific`, `intellect`, athlete fragment, `intelligence`, `cognition`, embodied fragment; extremes include `territorial`, `Persian`, `Chemistry`, `architectural`, `geographical`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 7 |
| lexical/morphological | 2 |
| named-entity | 1 |
| numeric | 0 |
| formatting/tokenizer | 1 |
| mixed | 1 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains:

- data, testing, measurement and problem-solving/process concepts;
- reporting, acknowledgement, recording and media/paratext activity;
- acquisition/retrieval/insertion/extraction/change operations;
- computing hardware, networking, storage and software/platform terminology;
- children/family, education and participant-management concepts;
- biomedical/psychological/materials-science terminology;
- geographic entities mixed with multilingual/name morphology;
- common grammar and lexical fragments;
- formatting;
- numeric strings and historical years.

Five of eleven communities receive a primary `semantic/topic`
classification. Two are mixed, two numeric, one lexical/morphological and one
formatting/tokenizer.

No conclusion about coherence, layer quality or trajectory is drawn.

### Negative tail

The negative-tail population contains:

- characterisation, assessment and structural/category descriptors;
- extreme evaluation, tragedy and distress/intensity language;
- deterioration/destruction and attempted/compelled change;
- inflammatory/pathological disease mechanisms;
- monarchy/religion/prophecy/ceremonial roles;
- built environment, clothing, terrain and material objects;
- civic/government roles and social hierarchy;
- personal names;
- multilingual and technical lexical fragments;
- formatting/tokenizer residue;
- mixed scientific/geographic/cognitive/identity descriptors.

Seven of twelve communities receive a primary `semantic/topic`
classification. Two are lexical/morphological, one named-entity, one mixed and
one formatting/tokenizer.

Negative anti-alignment contains substantial structured semantic material
alongside lexical and formatting organisation. No suppression or opposition
interpretation is assigned.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — biomedical, psychological, materials-science and physical
  concepts coexist;
- **positive C6** — geographic entities coexist with multilingual morphology
  and surname/name fragments;
- **positive C9** — children/family and educational concepts overlap with
  organisational/participant-management terms;
- **negative C0** — structural description, assessment and category language
  form a broad partition;
- **negative C3** — incomplete action/institutional stems and technical fragments
  are interleaved;
- **negative C7** — multiple physical-world object classes coexist;
- **negative C11** — scientific, geographic, cognitive and identity-related
  descriptors share one mixed partition.

These ambiguities remain explicit for later coherence analysis.

## R009 boundary

No comparison with earlier states, persistence claim, emergence claim, SDA-3
role, coherence judgement, optimal-layer judgement or curvature interpretation
is made in this file.
