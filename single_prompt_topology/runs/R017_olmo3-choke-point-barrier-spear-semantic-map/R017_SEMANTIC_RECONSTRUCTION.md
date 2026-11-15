# R017 independent semantic reconstruction

## Purpose

Reconstruct the smallest defensible semantic map from the completed R017 measured exports after measurement and completeness validation.

The source evidence is:

- `chatgpt_layer_packets.md`;
- `chatgpt_community_networks.json`;
- `community_nodes.csv`;
- `community_edges.csv`;
- `community_transition_evidence.csv`;
- `state_transitions.csv`;
- `cutoffs.csv`;
- `prompt_record.json`; and
- `manifest.json`.

No model forward pass, cutoff change, graph reconstruction or community re-detection is performed here.

The reporting boundary follows R014/R015: measured communities remain measured evidence; semantic parents and relations are downstream interpretations.

## Input

```text
choke point
collapsible barrier
spear
```

The final newline is the capture anchor. No chat template, special-token wrapper or response generation was used.

## Prompt-level reconstruction

### R017-A — constrained passage

Recovered material includes point, intersection, bottleneck, narrow, entry, exit, channel, route, location and spatial position.

The family is visible very early: State 3 already contains bottleneck, exit, entry and location. It remains recoverable late through point, intersection, narrow, route and spatial structure.

This is the reconstructed semantic region most directly associated with `choke point`.

### R017-B — deployable obstruction

Recovered material includes collapse, folding, blocking, deploy, deployment, wall, restriction and boundary-related vocabulary.

Collapse appears from State 1. Blocking persists positively across 39 states from State 22. Walls persist negatively across 29 states from State 31. Deploy/deployment becomes especially visible in the terminal representation.

The important reconstruction is not merely “barrier”, but a barrier that can be altered, placed or removed.

### R017-C — reach / piercing force

Recovered material includes spear, lance, knife, sword, blade, stab, pierce, weapon and related attack vocabulary.

At State 5, `spear` is a target-extreme member of a 502-token weapons community. At State 12, knife, spear and piercing/ambush material occupy the same broad weapon/action region. Direct `spear` membership persists across States 4–25.

Later depth retains the function of the object more strongly than the literal object name.

### R017-D — movement / flow

Recovered material includes movement, flow, path, route, exit, approach and channel.

This family changes sector participation through depth. During weapon concretisation it often appears as the spatial/movement counterpart to the positive weapon region; late states integrate flow and movement into the active functional reading.

It is therefore the principal relational bridge between constrained passage and obstruction.

### R017-E — boundary / defence

Recovered material includes wall, restriction, access, guard, guards and defence.

It becomes especially persistent in the later negative-tail topology, while `guards` re-enters the final positive representation.

This family is best treated as the limiting counterpart of the active mechanism, not as evidence that defence or walls are “suppressed”.

### R017-F — attack / interception

Recovered material includes attack, attacked, attacking, ambush, guard and the functional residue of stab/pierce.

This family is not simply a fourth supplied object. It emerges from the relation between the three supplied concepts.

At State 12, ambush and piercing material are already connected to the weapon region. At State 64, attack and intersection occur in the same positive community and are linked to point/guards, narrow and deployment communities.

This is the strongest emergent functional parent in the R017 map.

## Development through depth

| Depth | Dominant measured material | Reconstruction |
|---|---|---|
| State 00 | uncontextualised newline embedding | boundary condition; exclude from prompt-semantic claims |
| States 01–04 | collapse, location, exit, bottleneck, entry, movement, weapons | physical constraint and location selected before weapon structure fully dominates |
| States 05–20 | spear, lance, knife, sword, blade, stab, ambush; intersection begins to recur | concrete weapon/reach structure plus developing passage geometry |
| States 21–30 | weapon material broadens; blocking rises; controls/access appear | transition from object identity towards combined system function |
| States 31–57 | point, folding, blocking, movement, attack; walls/access/location/guard/exit persist | active mechanism differentiates from boundary conditions |
| States 58–63 | point, flow, collapse, attack, intersection, deploy/deployment, narrow; restriction/channel/pierce/guard/defence/wall | strongest integrated functional architecture |
| State 64 | deployment, intersection, narrow, deploy, attack, guards; route/wall/spatial remain negative-tail | terminal recoding preserves operational core and spatial counterpart |

## Parent relations

### Constrained passage → movement / flow

The passage family is repeatedly defined through route, exit, channel, point and intersection vocabulary. The defensible interpretation is that the constrained location organises movement rather than merely describing a place.

### Deployable obstruction → constrained passage

Late positive evidence directly links deployment to the constrained-point communities. At State 64:

- attack + intersection occupy C0;
- point + guards occupy C1;
- narrow occupies C4;
- deployment + deploy occupy C11.

Measured intercommunity token-edge counts include:

- C0 ↔ C11: 198;
- C1 ↔ C11: 190;
- C4 ↔ C11: 43.

This supports an obstruction/deployment mechanism attached to the constrained passage.

### Deployable obstruction → boundary / defence

Blocking/deployment is predominantly active/positive late, while wall, restriction, access, guard and defence are predominantly negative-tail.

The parent relation is supported by cross-depth sector pairing, but no positive-to-negative graph edge is claimed.

### Reach / piercing force → attack / interception

The literal spear/weapon family is strongest in early and middle layers. Later layers retain attack, pierce, guard and ambush-like function.

This is an object-to-function trajectory: the model increasingly represents what the spear does in the arrangement rather than the supplied noun alone.

### Constrained passage → attack / interception

At State 64, attack and intersection occur in the same positive community. That community is strongly linked to point/guards and narrow:

- C0 ↔ C1: 610 token edges;
- C0 ↔ C4: 157 token edges;
- C1 ↔ C4: 128 token edges.

The strongest supported interpretation is that attack/interception is situated at the constrained point.

### Movement / flow → attack / interception

This relation is higher-order rather than a single-state edge claim. Across depth, movement/flow is repeatedly organised by the passage and obstruction families, while attack/interception is increasingly attached to the resulting point of contact.

## Minimum semantic map

```text
                         CONSTRAINED PASSAGE
             point / intersection / narrow / channel / route
                                  │
                                  │ organises
                                  ▼
                         MOVEMENT / FLOW
                    path / entry / exit / approach
                                  │
                         shaped / blocked by
                                  ▼
                      DEPLOYABLE OBSTRUCTION
                 collapse / folding / blocking / deploy
                         │                 │
                         │                 └──── defines ────┐
                         │                                   ▼
                         │                         BOUNDARY / DEFENCE
                         │                    wall / restriction / guard
                         │
                 creates a controlled
                   point of contact
                         │
                         ▼
                    REACH / PIERCING FORCE
             spear / lance / blade / stab / pierce / weapon
                         │
                         ▼
                 ATTACK / INTERCEPTION
```

Compressed reading:

```text
CHANNEL MOVEMENT → DEPLOY BARRIER → NARROW APPROACH → INTERCEPT WITH REACH
```

## Strongest supported claim

R017 supports a coherent **single-trajectory tactical-interception map**. The model does not preserve the prompt merely as three adjacent nouns. It resolves the supplied concepts into geometry, movement, deployable obstruction and reach force, then increasingly compresses them into a functional relation in which movement is constrained, the passage is shaped or blocked, and force is applied at the resulting point of contact.

## Invariance status

Not tested.

R017 contains:

- one prompt;
- one concept order;
- one surrounding context;
- one model.

It therefore does not establish order invariance, context invariance, neighbouring-concept continuity or cross-model invariance.

## Interpretation boundary

- Positive and negative are cosine alignment and anti-alignment, not semantic approval and suppression.
- Parent names are post-measurement descriptions.
- Repeated family identity across sectors does not create a measured cross-sector edge.
- Large lexical, code, formatting, multilingual and named-entity communities remain present and are not part of the minimum prompt-specific map.
- State 00 and State 64 are boundary representations and are interpreted separately from ordinary intermediate states.
