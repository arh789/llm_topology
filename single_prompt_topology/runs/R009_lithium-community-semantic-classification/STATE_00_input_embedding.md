# R009 State 00 — input embedding

## State identity

- R008 state index: `0`
- R008 state label: `input_embedding`
- Analysis model: **GPT-5.6 Sol**
- Source run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Classification protocol: `R009_ANALYSIS_PROTOCOL.md`
- Status: first-pass semantic classification complete

## Count reconciliation

| Side | Expected communities | Classified communities | Status |
|---|---:|---:|---|
| positive_head | 12 | 12 | reconciled |
| negative_tail | 10 | 10 | reconciled |
| **Total** | **22** | **22** | **reconciled** |

The state is the static input-embedding baseline. The labels below describe
candidate organising content only. They do not assign SDA-3 roles or establish
semantic coherence.

## Positive-head communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 361 | Medicine, disease and pharmacology | semantic/topic | High | Representatives include `antidepress`, `schizophrenia`, `hepatocellular`, `glucose`, `tuberculosis`, `doxorubicin`; target-extreme examples include `bipolar`, `metformin`, `glutathione` and `cisplatin`. |
| C1 | 262 | Proper names and geography mixed with Li/lithium lexical forms | mixed | Moderate | Representatives include `Iran`, `Liu`, `Kuwait`, `Malaysia`, `Roberto`, `Massachusetts`, while target-extreme tokens include `Li`, `Lith`, `lith`, `li`, `Lithuan` and `Lebanese`. No single topical identity adequately covers both structures. |
| C2 | 230 | Thermal, liquid and environmental physical processes | semantic/topic | Moderate | `Temperature`, `thermally`, `cooling`, `groundwater`, `liquids`, `recharge`, `hydration`, `molten` and `recycling` support a broad physical/environmental-process identity, though the community is heterogeneous. |
| C3 | 206 | Electrochemistry, electricity and energy-storage technology | semantic/topic | High | `electrochemical`, `piezoelectric`, `electromagnetic`, `conductivity`, `capacitance`, `electrodes`, with target-extreme `electrolyte`, `batteries`, `battery`, `cathode` and `silicon`. |
| C4 | 182 | Consumer/digital technology and telecommunications | semantic/topic | High | `cryptocurrencies`, `telecommunications`, `Samsung`, `Bluetooth`, `laptops`, `Apple`, `Bitcoin`, `blockchain`; target-extreme examples include `LTE`, `Tesla`, `Wi`, `solar` and `Nissan`. |
| C5 | 142 | Three-digit numerical tokens | numeric | High | Representatives and extremes are dominated by strings such as `778`, `740`, `732`, `735`, `528`, `535`, `636`, `368`, `770` and `850`. |
| C6 | 139 | Chemical-element symbols and materials notation | semantic/topic | High | `Zn`, `Ti`, `Mg`, `Cu`, `Cd`, `Hg`, `Na`, `Rb`, `Cs`, plus `nanoparticle`, `graphene` and `layered`. The abbreviations are lexical forms, but their shared chemical/material domain is the dominant organising principle. |
| C7 | 127 | Inorganic chemistry, chemical substances and elements | semantic/topic | High | `phosphorus`, `chlor`, `ethanol`, `methyl`, `hydrogen`, `phosphate`, `fluor`, `chloride`, with extremes including `helium`, `alkali`, `carbonate`, `graphite`, `KCl` and `alkaline`. |
| C8 | 105 | Metals, minerals and engineering materials | semantic/topic | High | `aluminum`, `titanium`, `aluminium`, `magnesium`, `copper`, `zinc`, `Silicon`; extremes include `potassium`, `cobalt`, `sodium`, `nickel` and `calcium`. |
| C9 | 66 | Drugs, intoxicants and consumable substances | semantic/topic | High | `methamphetamine`, `alcohol`, `heroin`, `morphine`, `opioid`, `cannabis`, `nicotine`; extremes include `cocaine`, `LSD`, `marijuana` and `asbestos`. |
| C10 | 30 | Fragmentary, multilingual and encoding/tokenisation residues | formatting/tokenizer | High | The sample contains replacement characters and isolated fragments such as `piez`, `reinst`, `neon`, `ос`, `Instit`, `cond`, `matt` and `内`, without a stable topical centre. |
| C11 | 21 | Medical injection, implantation and vascular intervention | semantic/topic | High | `intravenous`, `implants`, `injection`, `injections`, `implantation`, `heparin`, `catheter`, `ablation`, `injecting` and `implanted`. |

### Positive-head type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 9 |
| mixed | 1 |
| numeric | 1 |
| formatting/tokenizer | 1 |
| lexical/morphological | 0 |
| named-entity | 0 |
| unclear | 0 |

## Negative-tail communities

| Community | Size | Broad identity | Structure type | Confidence | Evidence |
|---|---:|---|---|---|---|
| C0 | 307 | Personal names and name-like fragments | named-entity | Moderate | Representatives include `Ted`, `Fred`, `Ron`, `Rick`, `Sav`; extremes include `Wesley` and `Vernon`. Numerous short fragments (`Sp`, `pl`, `cott`, `Dev`, `ven`) make the community less purely named-entity. |
| C1 | 222 | Text, dialogue and software-interface processing | semantic/topic | High | `Session`, `writer`, `Reader`, `Dialog`, `Context`, `Parser`, `handler`, `Selection`; extremes include `Menu`, `Wrapper`, `Args`, `Cursor` and `Draw`. |
| C2 | 172 | Comprehension, literature and entertainment/evaluative language | semantic/topic | Moderate | `ignorant`, `fascinating`, Shakespeare fragment `akespeare`, `comprehend`, `acquainted`, `entertain`, `comed`; extremes include `circus`, `obscure`, `vague` and `fiddle`. The topical boundary is broad rather than singular. |
| C3 | 138 | Actions involving change, depiction and completion | semantic/topic | Moderate | `negotiated`, `depicting`, `surrendered`, `altered`, `depicted`, `finishing`, `hunted`, `knew`, with extremes including `contest`, `specified`, `overlapping` and `uncover`. The shared identity is process/action oriented but heterogeneous. |
| C4 | 116 | Word endings and lexical fragments | lexical/morphological | High | Dominated by fragments and endings such as `ce`, `achers`, `pe`, `der`, `ars`, `ters`, `lers`, `ps`, `rs`, `men`, `chers`. |
| C5 | 115 | Domestic animals, pets and animal care | semantic/topic | High | `birds`, `horses`, `Dog`, `horse`, `Veter`, `ducks`, `dog`, `veter`; extremes include `bred`, `owners`, `Owner`, `lover`, `bird`. |
| C6 | 77 | Formatting, punctuation and whitespace | formatting/tokenizer | High | Predominantly brackets, dashes, quotation marks, whitespace and malformed mathematical/formatting strings, with 58 of 77 tokens classified as punctuation or symbols. |
| C7 | 74 | Police, military ranks and security personnel | semantic/topic | High | `Officers`, `Capt`, `Sgt`, `Sergeant`, `detective`, `Patrol`, `cops`, `guards`, with rank-related fragments such as `geant` and `alry`. |
| C8 | 69 | Evaluation, statistics, administration and reporting | semantic/topic | Moderate | `Evaluation`, `quantified`, `overview`, `Hist`, `stats`, `Stats`, `experimentation`, `Overview`, `committee`, `Statistical`, `Administrative`; extremes include `Comparing`, `Quant` and `Percent`. |
| C9 | 26 | Numeric strings | numeric | High | Dominated by numeric tokens including `121`, `099`, `061`, `097`, `098`, `118`, `0011`, `502`, `993` and `301`. |

### Negative-tail type count

| Structure type | Communities |
|---|---:|
| semantic/topic | 6 |
| named-entity | 1 |
| lexical/morphological | 1 |
| formatting/tokenizer | 1 |
| numeric | 1 |
| mixed | 0 |
| unclear | 0 |

## State-level descriptive summary

### Positive head

The positive-head population contains a strong concentration of recognisable
scientific and technological domains. The most evident broad structures are:

- medicine and pharmacology;
- electrochemistry and battery technology;
- inorganic chemistry;
- chemical elements and materials notation;
- metals and engineering materials;
- thermal/liquid physical processes;
- consumer and communications technology;
- intoxicants and drugs.

Nine of twelve communities receive a primary `semantic/topic` classification.
The remaining three consist of one mixed proper-name/lithium-form community,
one numeric community and one tokenizer/encoding community.

This is a descriptive observation only. The concentration of lithium-relevant
domains does not by itself establish semantic centrality or coherence.

### Negative tail

The negative-tail population contains recognisable semantic structures but is
more heterogeneous in organising principle. Identified structures include:

- personal names;
- text/software processing;
- comprehension/literature/entertainment language;
- action/process language;
- domestic animals;
- police/rank/security terminology;
- evaluation/statistics/administration;
- morphology;
- formatting;
- numbers.

Six of ten communities receive a primary `semantic/topic` classification;
the others are named-entity, lexical/morphological, formatting/tokenizer and
numeric.

The presence of coherent-looking semantic labels in the negative tail is
important descriptively: negative anti-alignment has **not** produced a
population consisting only of noise or tokenizer artefacts. No suppression or
contradiction interpretation is assigned at this stage.

## Uncertainty record

The classifications most likely to require later content audit are:

- **positive C1** — clearly contains both name/geographic structure and
  lithium/Li lexical forms, so `mixed` is retained rather than forcing a
  single topic;
- **positive C2** — thermal/liquid/environmental processes are evident, but the
  community is broad;
- **negative C0** — personal names are prominent, but short name-like and
  lexical fragments reduce purity;
- **negative C2** — the literature/comprehension/entertainment description is
  broad and may contain multiple substructures;
- **negative C3** — action/process semantics are visible but heterogeneous;
- **negative C8** — evaluation/statistics/administration overlap rather than
  forming one narrow topic.

These uncertainties are preserved for later coherence analysis rather than
resolved by assigning stronger labels.

## R009 boundary

No cross-state comparison, persistence claim, emergence claim, SDA-3 role,
coherence judgement or curvature interpretation is made in this file.
