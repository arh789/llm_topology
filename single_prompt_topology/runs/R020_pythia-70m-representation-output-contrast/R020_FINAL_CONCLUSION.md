## The broadest semantic map inferred from R020

**The strongest reconstruction is a recurring functional network connecting human settlements, built environments, inhabitants, movement, routes and crossings.**

It is broader than the concepts in the prompt, but narrower than a complete, consistently maintained explanation of why a city builds a bridge.

The latest R020 analysis has reconstructed all 32 generated-token decisions and independently audited their supporting community relationships. It finds **intermittent reactivation of a common semantic field**, with changes in emphasis and connectivity as generation proceeds.

### 1. The central semantic network

<text color="secondary" size="xs">Numbers indicate how many of the 32 generation decisions contain a qualifying relationship in contextual transformer states S01–S05. They are recurrence counts, not probabilities or causal strengths.</text>

<box border="lg" padding={3} gap={2}>
  <svg viewBox="0 0 350 300" width="100%" xmlns="http://www.w3.org/2000/svg">
    {#each [
      [104,43,83,132],[246,43,267,132],
      [104,43,246,43],
      [83,132,175,215],[267,132,175,215],
      [175,215,175,277],
      [104,43,175,277]
    ] as e,i}
      <line key={i} x1={e[0]} y1={e[1]} x2={e[2]} y2={e[3]} stroke="currentColor" opacity={i===6?0.25:0.38} strokeWidth={i===6?1.2:1.8} strokeDasharray={i===6?"4 5":"none"}/>
    {/each}
    <rect x="37" y="18" width="134" height="49" rx="9" fill="#23689b"/>
    <rect x="190" y="18" width="132" height="49" rx="9" fill="#23689b"/>
    <rect x="12" y="111" width="142" height="50" rx="9" fill="#23689b"/>
    <rect x="195" y="111" width="143" height="50" rx="9" fill="#23689b"/>
    <rect x="106" y="189" width="138" height="50" rx="9" fill="#146b62"/>
    <rect x="100" y="262" width="150" height="36" rx="9" fill="#146b62"/>
    <g fontSize="12" fill="#ffffff" fontWeight="600" textAnchor="middle">
      <text x="104" y="38">INHABITANTS</text><text x="104" y="53">People</text>
      <text x="256" y="38">SETTLEMENTS</text><text x="256" y="53">Cities, towns</text>
      <text x="83" y="131">BUILT PLACES</text><text x="83" y="146">Buildings, streets</text>
      <text x="266" y="131">COMMERCE</text><text x="266" y="146">Markets, businesses</text>
      <text x="175" y="208">MOVEMENT</text><text x="175" y="224">Routes, transport</text>
      <text x="175" y="284">CROSSING / CONNECTION</text>
    </g>
    <g fontSize="10" fontWeight="600" textAnchor="middle">
      <rect x="161" y="24" width="22" height="17" rx="7" fill="#ffffff"/><text x="172" y="36" fill="#155c8b">6</text>
      <rect x="51" y="77" width="23" height="17" rx="7" fill="#ffffff"/><text x="62" y="89" fill="#155c8b">7</text>
      <rect x="200" y="91" width="23" height="17" rx="7" fill="#ffffff"/><text x="211" y="103" fill="#155c8b">11</text>
      <rect x="119" y="170" width="22" height="17" rx="7" fill="#ffffff"/><text x="130" y="182" fill="#155c8b">7</text>
      <rect x="205" y="169" width="22" height="17" rx="7" fill="#ffffff"/><text x="216" y="181" fill="#155c8b">3</text>
      <rect x="185" y="243" width="22" height="17" rx="7" fill="#ffffff"/><text x="196" y="255" fill="#155c8b">8</text>
    </g>
  </svg>
  <caption>Conceptual layout of the strongest recurrent families. The measured evidence supports additional connections, including settlements–crossings (5 decisions) and built places–crossings (2 decisions). The layout is not a graph of causal direction.</caption>
</box>

The most important relationship is **settlement ↔ movement**, appearing in 11 decisions, followed by **movement ↔ crossing**, appearing in eight. These connect the prompt's geographical objects to a functional possibility: moving people through an inhabited environment by connecting places.

This is especially interesting because the generated response never explains that function. It merely repeats an incorrect equivalence between city, bridge and river.

Source: <Link url="https://github.com/arh789/llm_topology/blob/main/single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md" title="R020 generation-wide semantic reconstruction"/>.

### 2. The wider semantic neighbourhood

Beyond the strongest recurrent relationships, the pipeline exposes several additional domains. Some have measured connections to the central field, while others appear only in particular states.

<box border="lg" padding={3} gap={1}>
  <text weight="medium" size="xs" color="secondary">BROAD SEMANTIC RECONSTRUCTION</text>
  ```text
  INHABITED PHYSICAL ENVIRONMENT
  |
  +-- HUMAN ORGANISATION
  |   +-- Cities, towns, villages
  |   +-- Residents, citizens, people
  |   +-- Buildings, streets, shops
  |   '-- Commerce, markets, businesses
  |
  +-- MOVEMENT AND CONNECTIVITY
  |   +-- Travel, journeys, transport
  |   +-- Roads, railway, highways
  |   +-- Bridges, tunnels, crossings
  |   +-- Boats, waterways
  |   '-- Transfers, links, connections
  |
  +-- PHYSICAL ENVIRONMENT
  |   +-- Rivers, lakes, oceans
  |   +-- Valleys, terrain, landscape
  |   +-- Water, drainage, flow
  |   '-- Floods, storms, disruption
  |
  +-- CONSTRUCTION AND MODIFICATION
  |   +-- Infrastructure, components
  |   +-- Wires, ropes, connectors
  |   +-- Reconstruction, rebuilding
  |   '-- Renovation, restoration
  |
  +-- ABSTRACT RELATIONSHIPS
  |   +-- Connections, associations
  |   +-- Criteria, relationships
  |   '-- Mathematics, geometry
  |       [unresolved attachment]
  |
  '-- RECURRENT BACKGROUND STRUCTURES
      +-- Evaluation / intensity
      +-- Knowledge / scholarship
      +-- Operations / control
      +-- Biology / medicine
      +-- Clothing / equipment
      '-- Other mixed, unresolved domains
  ```

  <caption>This is a map of the observed semantic families, not an assertion that they form one connected network in every state. The strongest task-related relationships are in the first four branches.</caption>
</box>

Two particularly interesting branches were hidden by the earlier compressed summaries.

**Disruption and reconstruction.** At the input state for `bridge`, the bridge community has measured links to disruption, journeys and structural components. Disruption also connects with reconstruction and restoration. That broadens the accessible associations beyond simply travelling over a river, although this branch is not established as a persistent contextual hypothesis.

**Commerce and human activity.** Markets and businesses connect with movement, settlements and built places in several decisions. These are candidate economic and social functions of infrastructure, even though neither is mentioned in the generated response.

A mathematical branch also appears at D32/S05, connected to an abstract relationship community. Its connection is measured, but its meaning remains unresolved.

### 3. How the semantic map changes

| Representation | What the pipeline finds |
|---|---|
| S00 — input embedding | Strong local associations around city, bridge, river and other current tokens |
| S01–S05 — contextual layers | Intermittent reconstruction of movement, settlements, crossings and inhabited places |
| S06–S07 — output-proximal | Highly recurrent structures, predominantly evaluation, scholarship, operations and other off-topic vocabulary under the current projection |

The output-proximal result is particularly important. Evaluation–scholarship connections recur in all 32 S07 positive networks; operations–biology connections occur in 31 of 32 negative networks. These are strongly recurrent structures but do not establish relevance to the bridge question. Negative cosine also does not itself imply semantic suppression.

<grid columns={3} gap={2}>
  <grid-item>
    <box gap={1}>
      <title size="xl" color="default" tabularNums>21/32</title>
      <caption>Decisions with a qualifying contextual task-related relationship</caption>
    </box>
  </grid-item>
  <grid-item>
    <box gap={1}>
      <title size="xl" color="default" tabularNums>6/32</title>
      <caption>Decisions with the same relationship in multiple contextual states</caption>
    </box>
  </grid-item>
  <grid-item>
    <box gap={1}>
      <title size="xl" color="default" tabularNums>11/32</title>
      <caption>Decisions unresolved by the selected relationship threshold</caption>
    </box>
  </grid-item>
</grid>

The same broad relationships also recur during the second, repeated sentence, but with different community identities, connection patterns and transformer states.

**That supports selective reactivation and contextual reorganisation, rather than a single fixed network being replayed or a simple progression of semantic drift.**

### 4. The broadest organising hypothesis

The reconstruction supports this candidate:

> **Human settlements organise their built environment to enable movement and connection between places.**

Extending that hypothesis produces a broader possible system involving inhabitants, transport infrastructure, water and terrain constraints, commerce, and reconstruction after disruption.

However, the critical relationship remains insufficiently integrated:

```text id="rovmnj"
CITY      -- actor / beneficiary
BRIDGE    -- constructed means
RIVER     -- obstacle
CROSSING  -- function / purpose
```

The pipeline repeatedly recovers portions of these relationships, but does not establish that all four roles are consistently bound together.

That offers a possible explanation for the failed answer: **the model can recruit relevant semantic components without reliably organising them into the relationship required to answer the question.**

This is a stronger inference than either claiming that the model possesses a complete hidden explanation or declaring that its semantics disappear when generation deteriorates.

## 5. Where the reconstruction now stands

The latest R020 analysis is substantially further advanced than the previous thread's unfinished task. All 32 candidate decision-level maps now exist; 359 cited relationship examples have been checked against measured edges, with no mismatches. The task of constructing an inspectable candidate map is complete.

The remaining boundary is the semantic completeness and usefulness of that map. The task-specific analysis identified 818 of 6,944 communities through its deliberately limited selection criteria. Consequently, the map above represents the **broadest defensible synthesis of the reconstructed families**, not the full possible topology contained in the unclassified communities.

You can inspect the source outputs:

- <Link url="https://github.com/arh789/llm_topology/blob/main/single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_PER_TOKEN_HYPOTHESIS_MAP.html" title="Interactive 32-token semantic hypothesis map"/>
- <Link url="https://github.com/arh789/llm_topology/blob/main/single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_VERIFIED_CONSOLIDATED_SEMANTIC_MAP.md" title="Fuller community relationships and unexpected associations"/>
- <Link url="https://github.com/arh789/llm_topology/blob/main/single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_V3_INDEPENDENT_RELATION_EVIDENCE_AUDIT.md" title="Independent evidence audit"/>

**The most consequential emerging finding is the separation between semantic availability and semantic integration.** R020 shows that relevant relationships can be reconstructed even when the generated answer is poor. It does not yet demonstrate that the model maintains a complete organising hypothesis and merely fails to express it.

The distinction between those two possibilities is now the central research question exposed by the pipeline.