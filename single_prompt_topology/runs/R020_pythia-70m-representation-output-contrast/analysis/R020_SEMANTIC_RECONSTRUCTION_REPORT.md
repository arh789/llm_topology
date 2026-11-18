# R020 — Reconstructed semantic network and generation-trajectory analysis

**Status:** Semantic screening and evidence-backed reconstruction completed; usefulness judgement belongs to the human reviewer. This report does not mark the frozen measurement manifest complete.

**Governing question:** Does Pythia 70M expose topic-relevant semantic organisation through its internal layer-state networks that is not successfully articulated in its generated response?

## 1. What the model actually said

Prompt: `Question: Why would a city build a bridge across a river?` followed by `Answer:`.

```text
The city is a bridge that connects the river with the river.

A:

The city is a bridge that connects the river with the river.
```

The continuation is repetitive and does not adequately answer why the bridge would be built. This is an observed output property, not evidence by itself that the internal semantic structure is useful.

## 2. Scope, coverage and analysis method

- All **32 next-token decisions**, **8 recorded states**, **2 cosine sectors**: **512 networks**, **6,944 measured communities**.
- Provisional lexical-semantic candidate labels in **1,865** communities; **33** have competing labels; **5,046** remain unresolved, primarily because the available representative tokens do not justify a confident label.
- The **same post-hoc candidate labelling rule** returns **0** labelled communities in the globally shuffled-label control. Because the lexicon was curated after inspecting the original evidence, this is a useful sensitivity check, **not independent proof of meaning or prompt dependence**.
- All communities are retained in `analysis/R020_COMMUNITIES_*.json`, including unresolved ones. Every positive claim below refers to a decision, state, sector and community ID. Exact memberships of all 1.42 million selected tokens are not contained in the compact GitHub community summaries; this analysis uses their representative/extreme tokens, class counts, community-level edge evidence and measured transition summaries.
- The output and possible adjacent concepts had already been exposed in this conversation before reconstruction. This was **not a blinded semantic interpretation**. No causal explanation, active belief state or literal training-data source is inferred from projection geometry.

## 3. Reconstructed semantic maps

### A. Input and early contextual states: recognisable question-related neighbourhood

```text
INPUT / EARLY REPRESENTATIONS (mainly S00–S02, positive cosine)
         [WATERWAYS / WATER]          [LANDSCAPE]
          river, lake, water           forest, valley
                |                           |
                +----------+----------------+
                           |
                   [BUILT ENVIRONMENTS]
                 bridge, courtyard, buildings
                        /        \
                       /          \
         [SETTLEMENTS]----[ROUTES / TRANSPORT]
       cities, towns       railway, highway, travel
                          transport, crossings

Note: lines describe measured *intercommunity token edges* at
particular decision/state/sector snapshots, not causal links or
a single invariant graph persisting through the model.
```

Observable examples:
- **Decision 03, S00, positive:** the input-word neighbourhood for *city* contains settlements (`city / cities / villages / towns`), buildings (`hotels / buildings / shops / house`) and transport (`highway / railway / roadway / airport`).
- **Decision 06, S00, positive:** the input-word neighbourhood for *bridge* includes bridge/bridging, boats/ships, journeys/travel, roads/railways and built places; it is informative associative content, but its presence in the **embedding baseline** alone is not evidence of contextual reasoning.
- **Decision 10, S00, positive:** the input-word neighbourhood for *river* includes river/lake/ocean, water/drainage, towns/countryside, built structures and roads/railways. This network recurs when *river* is again the current token.
- **Decision 10, S01–S02, positive:** transport/travel and movement clusters appear in contextual states (S01 C3; S02 C0/C1). This is a plausible internal reorganisation, but neither semantic usefulness nor independence from word-level associations can be inferred without examining the specific supporting communities.

### B. Late states: stable, but not question-specific under the recorded candidate identities

```text
LATE STATES S06 / S07, RECURRING ACROSS TOKEN DECISIONS

POSITIVE COSINE                    NEGATIVE COSINE
[EVALUATION / INTENSITY]           [OPERATIONS / CONTROL]
          |                         /    |     \
          |                        /     |      \
[KNOWLEDGE / SCHOLARSHIP]     [BIOLOGY] [EQUIPMENT] [NAMES]
                                |          |
                           [FOOD/ANIMALS] [SPORT]

Other branches: morphology, code, multilingual fragments,
and numerous unresolved or competing communities.
```

At S07, positive-sector *evaluation ↔ scholarship* community edges occur in **32/32 decisions**. Negative-sector *operations ↔ biology* edges occur in **31/32**, and *operations ↔ equipment* in **30/32**. These are geometric intercommunity connections. Their recurrence does not make their interpretation relevant to the bridge question, nor does negative cosine imply suppression.

**Critical negative finding:** Under the deliberately conservative representative-token criteria, none of the six question-related families (water, settlements, built structures, transport, engineering and ecology) qualifies as a coherent candidate community in either S06 or S07. This does *not* prove the entire layer contains none of these concepts; it limits what the measured compact community evidence establishes.

## 4. Layerwise evolution across all 32 decisions

| State | All communities | Provisionally labelled | Question-related candidate communities | Most frequent *other* candidate families |
|---|---:|---:|---:|---|
| S00 | 715 | 58 | 50 | Operations / control (2); Clothing / equipment (2); Legal / crime (2) |
| S01 | 874 | 169 | 27 | Evaluation / intensity (24); Place names (23); Food / animals (21) |
| S02 | 880 | 189 | 20 | Evaluation / intensity (30); Biology / medicine (28); Legal / crime (17) |
| S03 | 864 | 200 | 10 | Evaluation / intensity (41); Biology / medicine (26); Operations / control (20) |
| S04 | 873 | 203 | 26 | Evaluation / intensity (56); Sport / competition (25); Place names (21) |
| S05 | 870 | 178 | 22 | Biology / medicine (29); Evaluation / intensity (28); Place names (23) |
| S06 | 938 | 437 | 0 | Evaluation / intensity (76); Knowledge / scholarship (55); Operations / control (49) |
| S07 | 930 | 431 | 0 | Evaluation / intensity (74); Knowledge / scholarship (54); Operations / control (51) |

The table counts communities across **all 32 decisions**, not statistically independent prompts. Many prompts within the run share the same word at the current input position because the generated answer repeats itself.

Measured adjacent-generation membership Jaccard averages show a strong positional contrast:

- **S00 positive:** 0.151; **S00 negative:** 0.081.
- **S06 positive:** 0.740; **S06 negative:** 0.747.
- **S07 positive:** 0.834; **S07 negative:** 0.839.

Thus the representation becomes substantially more similar from one token decision to the next near the output, even though the early-state semantic neighbourhood changes with the current token. This does not mean the late state has superior task-relevant content.

## 5. Selected community-level evidence

| Exact location | Provisional parent | Community size | Representative tokens (abridged) |
|---|---|---:|---|
| `03/S0/positive/C3` | Settlements / locality | 211 | `city`, `cities`, `provinces`, `villages`, `town`, `locations`, `towns`, `city`, `location` |
| `06/S0/positive/C0` | Transport / passage | 172 | `bridging`, `bridge`, `bridges`, `Bridge`, `traverse`, `connections`, `junctions`, `switch`, `Bridge` |
| `06/S0/positive/C9` | Transport / passage | 87 | `highway`, `Railway`, `railway`, `road`, `roadway`, `highways`, `streets`, `roads`, `trains` |
| `10/S0/positive/C0` | Waterways / water | 201 | `water`, `groundwater`, `water`, `Water`, `drainage`, `flow`, `urine`, `arteries`, `Water` |
| `10/S0/positive/C1` | Waterways / water | 175 | `river`, `lake`, `River`, `ocean`, `lakes`, `cliffs`, `seas`, `coastal`, `valleys` |
| `10/S0/positive/C11` | Transport / passage | 93 | `roadway`, `highway`, `road`, `roads`, `sidewalk`, `Airport`, `railway`, `pavement`, `route` |
| `10/S1/positive/C3` | Transport / passage | 324 | `transport`, `transporting`, `transported`, `getting`, `transportation`, `traveled`, `travelled`, `flung`, `traveling` |
| `10/S2/positive/C1` | Transport / passage | 269 | `transporting`, `transported`, `Surface`, `portation`, `propagation`, `transport`, `switching`, `complexes`, `bundles` |
| `03/S4/positive/C0` | Settlements / locality | 369 | `town`, `city`, `cities`, `towns`, `buildings`, `counties`, `Sports`, `Cup`, `town` |
| `32/S5/positive/C7` | Transport / passage | 227 | `connections`, `criterion`, `connection`, `relationship`, `resem`, `association`, `link`, `danger`, `crisis` |
| `01/S7/positive/C0` | Evaluation / intensity | 423 | `intriguing`, `fascinating`, `talented`, `considerable`, `charming`, `invaluable`, `prominent`, `mysterious`, `unfortunate` |
| `01/S7/positive/C3` | Knowledge / scholarship | 327 | `scholar`, `ologist`, `academics`, `professionals`, `resear`, `professors`, `professor`, `University`, `pathophys` |
| `01/S7/negative/C0` | Operations / control | 438 | `regulates`, `enhances`, `inhibit`, `purchase`, `activated`, `activate`, `slapped`, `destroys`, `inhibits` |
| `01/S7/negative/C1` | Measurement / transformation | 374 | `measurements`, `transformations`, `transformation`, `injections`, `buttons`, `transitions`, `movements`, `assays`, `tags` |
| `01/S7/negative/C3` | Clothing / equipment | 262 | `straps`, `jacket`, `sweater`, `helmet`, `shirt`, `collar`, `strands`, `rods`, `arm` |
| `32/S7/positive/C2` | Evaluation / intensity | 363 | `intriguing`, `unfortunate`, `fascinating`, `mysterious`, `noteworthy`, `ubiquitous`, `crucial`, `prominent`, `intricate` |
| `32/S7/negative/C0` | Operations / control | 485 | `regulates`, `enhances`, `destroyed`, `inhibit`, `flip`, `destroys`, `purchase`, `activate`, `inhibits` |

### Measured parent-level intercommunity connections

| State/sector | Candidate relationship | Distinct decisions | Token edges across those decisions | Example community IDs |
|---|---|---:|---:|---|
| S06/positive | Evaluation / intensity ↔ Knowledge / scholarship | 32/32 | 23,047 | D01: C1–C2 |
| S07/positive | Evaluation / intensity ↔ Knowledge / scholarship | 32/32 | 20,962 | D01: C0–C3 |
| S07/negative | Biology / medicine ↔ Operations / control | 31/32 | 7,335 | D01: C0–C4 |
| S07/negative | Clothing / equipment ↔ Operations / control | 30/32 | 8,787 | D01: C0–C3 |
| S06/negative | Clothing / equipment ↔ Operations / control | 30/32 | 7,815 | D01: C0–C4 |
| S06/negative | Biology / medicine ↔ Operations / control | 29/32 | 7,891 | D01: C0–C3 |
| S03/positive | Biology / medicine ↔ Operations / control | 13/32 | 3,783 | D01: C3–C4 |
| S02/positive | Biology / medicine ↔ Operations / control | 9/32 | 1,506 | D03: C6–C8 |
| S04/negative | Construction / engineering ↔ Evaluation / intensity | 8/32 | 2,005 | D01: C2–C5 |
| S00/positive | Built structures ↔ Transport / passage | 8/32 | 1,532 | D03: C1–C5 |
| S01/negative | Evaluation / intensity ↔ Knowledge / scholarship | 7/32 | 1,367 | D03: C1–C8 |
| S01/positive | Built structures ↔ Transport / passage | 6/32 | 1,539 | D06: C2–C5 |
| S03/negative | Evaluation / intensity ↔ Knowledge / scholarship | 6/32 | 799 | D03: C2–C10 |

The edge totals are accumulated counts of *cross-community token connections in measured networks*, not independent observations or causal strengths.

## 6. Generated answer versus reconstructed structure

| Observation | What it establishes | What it does not establish |
|---|---|---|
| The final answer repeats a circular sentence | Expressive failure on this prompt | That the internal model has no semantic associations |
| S00 contains routes, water, settlements and built-place communities | Rich lexical neighbourhoods are measurable | That these are newly inferred contextual relationships |
| S01–S05 sometimes contain transport, settlements or engineering families | Some relevant associations remain visible after contextualisation | That they were being used to select an answer or surpass a prompt-only baseline |
| S06/S07 are strongly stable across generated tokens | Output-proximal network geometry is recurrent | That recurrence entails relevance or utility |
| Shuffled labels lose all the provisional multi-term category matches | The labelling result depends on meaningful vocabulary labels | Independent validation of a correct semantic graph or answer usefulness |

**Provisional interpretation:** The tiny model's intermediate networks expose potentially useful neighbouring concepts, particularly routes, buildings and transport, which its generated sentence does not articulate. However, much of the strongest bridge-related structure originates in the current input token's embedding neighbourhood, while the stable output-proximal networks are largely unrelated to the question under this reconstruction. Therefore **the strong R020 hypothesis is not yet established**. The informative result is the separation between recoverable associations, their evolution and failure to become a coherent response.

**Human evaluation question:** Is the accessible early and middle-state information useful beyond the generated text *even if some of it comes from static lexical associations*? That practical judgement belongs to the human operator. If a particular relationship proves useful, the evidence links make it possible to interrogate and reconstruct it further.

## 7. Audit and methodological limitations

- Classification is a transparent deterministic **semantic-candidate screen**, not a validated human-quality interpretation of every one of 6,944 communities. Unresolved or mixed cases are left unresolved; the four community shards make all selections and omissions inspectable.
- Candidate families are not five SDA-3 roles. No Central/Suppressed/Adjacent/HCU/Emerging category is forced onto the measured graph. The cosine-negative sector measures anti-alignment, not conceptual suppression.
- The control uses globally shuffled *labels*, not altered model activity. Its failure to match the post-hoc lexicon is not sufficient to claim prompt-specific semantic intelligence.
- Representative and extreme tokens (12 each per community), class counts and intercommunity edges are available in GitHub; the full individual token membership and token-level edges are not in these compact exports. Any more ambitious token-level reconstruction requires the raw run artefacts, which were not re-executed here.
- Generated continuation and anticipated adjacent domains were known to this analyst before coding; this is not a genuinely blinded human or model judgement.
- Parent matching between adjacent states is based on candidate label consistency and at least three shared representative token IDs; it can miss semantic continuity expressed in different words and can create false links between lexically similar material. The raw matches are retained in `R020_STATE_CELLS.json`.
- S06/S07 candidates include stable but seemingly off-task categories (personal names, sports, equipment). This is *not* proof of absent semantics; it is a limit on this screening method.
- One prompt and one model cannot establish a general advantage for state analysis over generation.

## 8. Analysis artefacts

- [Interactive semantic matrix and network report](analysis/R020_SEMANTIC_MAP_REPORT.html)
- [Derived diagnostics and edge supports](analysis/R020_DERIVED_DIAGNOSTICS.json)
- [All 512 state/sector summaries, 705 depth matches and 961 generation matches](analysis/R020_STATE_CELLS.json)
- [All 6,944 community annotations: decisions 01–08](analysis/R020_COMMUNITIES_01-08.json)
- [Decisions 09–16](analysis/R020_COMMUNITIES_09-16.json)
- [Decisions 17–24](analysis/R020_COMMUNITIES_17-24.json)
- [Decisions 25–32](analysis/R020_COMMUNITIES_25-32.json)
- [Deterministic screening code and lexicon](analysis/R020_ANALYSIS_REPRODUCER.js)
- [Original R020 measurement evidence](chatgpt_community_networks.json)

**Lifecycle boundary:** This analytical package is an inspectable reconstruction offered for human usefulness evaluation. It does not replace the original R020 measurement methodology, modify its frozen outputs or assert that the model's internal representation contains a uniquely correct hidden answer.
