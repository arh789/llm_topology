# R020 — semantic map for human usefulness review

**Status:** Provisional reconstruction available for human evaluation. No human usefulness verdict has yet been recorded.

**What is being judged:** Does R020's measured semantic structure expose useful information beyond Pythia 70M's visibly unsuccessful answer? The human reviewer owns that judgement. This is an inspection surface, not a new scientific result.

## 1. Generated response

Prompt: `Why would a city build a bridge across a river?`

~~~text
The city is a bridge that connects the river with the river.

A:

The city is a bridge that connects the river with the river.
~~~

The continuation is circular and repetitive.

## 2. Provisional semantic map

~~~text
INPUT AND EARLY CONTEXTUAL STATES — mainly S00–S02

                 [WATER / WATERWAYS]
                 river, lake, drainage
                          |
                [LANDSCAPE / TERRAIN]
                 valley, coastline
                          |
                 [BUILT ENVIRONMENT]
                bridge, other buildings
                     /           \
                    /             \
          [SETTLEMENTS]       [ROUTES / TRANSPORT]
         city, towns,         highway, railway,
         villages             journeys, travel

Edges here summarise local measured intercommunity token connections;
they do not claim a single persistent graph or a causal model.

LATE STATES — S06/S07

     POSITIVE                       NEGATIVE
 [EVALUATION / INTENSITY]      [OPERATIONS / CONTROL]
          |                       /           \
 [KNOWLEDGE / SCHOLARSHIP]  [BIOLOGY]     [EQUIPMENT]

These late associations are recurrent but predominantly unrelated
to why a city builds a bridge under the provisional community labels.
~~~

## 3. Inspectable evidence

| Decision / state / sector / community | Candidate information | Representative evidence |
|---|---|---|
| `03/S00/positive/C3` | Settlements and locality | `city`, `cities`, `villages`, `towns` |
| `06/S00/positive/C0` | Crossing / bridge | `bridging`, `bridge`, `traverse`, `connections`, `junctions` |
| `06/S00/positive/C9` | Roads and railways | `highway`, `railway`, `roadway`, `streets` |
| `10/S00/positive/C0` | Water and drainage | `water`, `groundwater`, `drainage`, `flow` |
| `10/S00/positive/C1` | Rivers and landscape | `river`, `lake`, `ocean`, `coastal`, `valleys` |
| `10/S01/positive/C3` | Contextual transport | `transport`, `transporting`, `transportation`, `traveled` |
| `10/S02/positive/C1` | Broader transport/change mix | `transported`, `transport`, `switching`, `bundles` |
| `32/S05/positive/C7` | Connections / relationships, mixed | `connections`, `relationship`, `association`, `link`, `danger` |

These are selected examples from the existing analysis, not a new interpretation of the full 6,944-community dataset. Decision numbers are 1-based; S00–S07 are the eight recorded states.

## 4. What the measured analysis currently supports

- A rich associative neighbourhood is observable near the input tokens for city, bridge and river.
- Some transport and movement associations also appear in contextual states S01–S05.
- S06/S07 are strikingly stable between token decisions, but the predominant provisional parent labels are not relevant to the bridge question.
- The conservative semantic screen labels 1,865 of 6,944 communities, leaves 5,046 unresolved and marks 33 mixed or competing.
- The shuffled-label control yields no candidate matches under the **post-hoc lexicon**, which is a sensitivity check rather than independent semantic validation.

**Still unsupported:** That a stable, novel, contextually reconstructed explanation of bridge-building is present internally; that the stable late states carry task-relevant knowledge; or that the semantic associations caused any generated word.

## 5. The human usefulness decision

The key question is simply:

> **Does the reconstructed map reveal useful information about the prompt that the generated response failed to express?**

It is acceptable to conclude that the reported associations are obvious, that the analysis has not yet exposed enough of the possibility space, or that a specific unexpected relationship deserves deeper reconstruction.

If the map is inadequate, the most informative correction is **which relationship was missing, over-compressed or insufficiently explained**. That becomes a constraint for a targeted next reconstruction, not a reason to repeat the whole 32-token measurement.

## 6. Persistent evidence and recovery

- [Detailed semantic reconstruction](R020_SEMANTIC_RECONSTRUCTION_REPORT.md)
- [Interactive report](R020_SEMANTIC_MAP_REPORT.html)
- [State cells and trajectory matches](R020_STATE_CELLS.json)
- [All community annotations: 01–08](R020_COMMUNITIES_01-08.json), [09–16](R020_COMMUNITIES_09-16.json), [17–24](R020_COMMUNITIES_17-24.json), [25–32](R020_COMMUNITIES_25-32.json)
- [Checkpoint and recovery plan](R020_CHECKPOINT_AND_RECOVERY_PLAN.md)
- [Pinned checkpoint ledger](R020_CHECKPOINT_LEDGER.json)
- [Fail-closed verifier](R020_VERIFY_CHECKPOINTS.js)
- [Integrity incident record](R020_CHECKPOINT_AUDIT.md)

**Interpretation boundary:** This packet is drawn from the previously saved provisional reconstruction, which used representative/extreme tokens and candidate labels. It does not claim blinded analysis or independent validation of all community semantics. Its purpose is to present the available structures for the human to judge.
