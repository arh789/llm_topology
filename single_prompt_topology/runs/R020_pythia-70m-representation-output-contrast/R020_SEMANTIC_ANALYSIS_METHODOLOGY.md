# R020 semantic analysis methodology — layer-by-layer and token-by-token reconstruction

**Status:** Post-measurement semantic-analysis procedure; analysis not yet performed.

**Relationship to the existing experiment:** This document records the proposed ChatGPT analysis of R020's completed measurement exports. It supplements, and does not alter, the frozen [R020_RUN_METHODOLOGY.md](R020_RUN_METHODOLOGY.md), the original prompt, recorded measurements, validation decisions or experimental controls.

I will analyse R020 as a **two-dimensional semantic reconstruction**: how the model's representation changes through transformer layers, and how it changes as each new token is generated.

The purpose is to discover what semantic structures are present internally, which relationships survive, and what the model fails to express in its output.

## 1. The analysis grid

R020 contains 32 generated-token decisions, each with eight recorded states and two semantic-network sectors.

| Analysis dimension | Count |
|---|---:|
| Generated-token decisions | 32 |
| Recorded states per decision | 8 |
| Cosine sectors per state | 2 |
| Semantic networks in total | 512 |

Each position in the grid represents the internal state used to predict a particular generated token.

~~~text
                    TRANSFORMER DEPTH
                   S0  S1  S2  S3  S4  S5  S6  S7
                   --------------------------------
Token 01: The      [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 02: city     [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 03: is       [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 04: a        [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 05: bridge   [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 06: that     [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
Token 07: connects [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
...
Token 32: .        [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
~~~

An important distinction: the states in the `bridge` row are those that predicted *bridge*. The model has not yet consumed that generated word. Its effects on the representation appear in subsequent rows.

## 2. How each state will be analysed

For every one of the 256 state snapshots, I will apply the same procedure:

1. **Inspect the communities.** Examine representative tokens, broader membership, internal connections and positive/negative cosine sectors. Identify semantic content, lexical patterns, mixed communities and uninterpretable material.
2. **Reconstruct candidate parent structures.** Determine which higher-order concepts best explain the relationships between communities. Preserve competing interpretations rather than forcing every community into a parent.
3. **Identify relationships between parents.** Establish which structures connect, overlap, constrain or remain separate, using the recorded graph evidence.
4. **Record the reconstruction.** Save each proposed parent, its constituent communities, supporting tokens, relationships, confidence and unresolved evidence.

This produces one semantic reconstruction per state, with both cosine sectors analysed separately.

Crucially, I will not simply use the 50 highest-ranked tokens as a topic list. They are evidence for interpreting the larger community structure.

## 3. How semantic changes will be identified

There are two comparisons.

**A. Across layers, for each generated token**

For each decision, compare State 00 through State 07.

~~~text
TOKEN DECISION 05: "bridge"

S00  Input embedding
 |
 v
S01  Block 0
 |
 v
S02  Block 1
 |
 v
S03  Block 2
 |
 v
S04  Block 3
 |
 v
S05  Block 4
 |
 v
S06  Block 5
 |
 v
S07  Final normalised state
~~~

At each transition I will examine which semantic parents appear, persist, strengthen, weaken, split, merge or disappear.

**B. Across generation decisions, at the same state**

I will then track the reconstructed structures as the model generates further tokens.

For example, does a relationship already exist before the model generates *bridge*? Does it persist after *bridge* becomes part of the input? Does it disappear when the model begins repeating itself?

This allows us to distinguish semantic structures that were already available from structures introduced or reorganised as the model consumes its own output.

## 4. How the results will be presented

Rather than present 6,944 individual community descriptions, I will consolidate them into a semantic map showing:

~~~text
R020 — RECONSTRUCTED SEMANTIC NETWORK
|
+-- CORE SEMANTIC PARENTS
|   +-- Parent identities
|   +-- Constituent communities
|   '-- Evidence-backed relationships
|
+-- ADJACENT STRUCTURES
|   +-- Additional semantic families
|   +-- Relationships to the core
|   '-- Context-dependent associations
|
+-- TRANSFORMER EVOLUTION
|   +-- Present at input
|   +-- Recruited through layers
|   +-- Persistent
|   '-- Decaying / transformed
|
+-- GENERATION EVOLUTION
|   +-- Present before expression
|   +-- Expressed in the output
|   +-- Persistent but unexpressed
|   '-- Lost or displaced during generation
|
'-- UNRESOLVED STRUCTURES
    +-- Mixed communities
    +-- Competing parent interpretations
    '-- Unexplained associations
~~~

Every meaningful parent and relationship will retain its supporting decision, state, sector and community identifiers.

The maps will be constructed from the evidence, not from the expected subjects of bridges, engineering or transport.

## 5. The critical analytical distinction

**A change in token membership does not necessarily mean a change in semantic structure.**

Different tokens may express the same higher-order relationship. Conversely, similar tokens may be organised into different relationships across layers.

Therefore, the principal object to track is the **semantic parent and its relationships**, not merely the appearance or disappearance of individual tokens.

The analysis will preserve those distinctions rather than impose a coherent developmental story.

## 6. Final deliverable

I propose two complementary outputs:

1. **A compact semantic network** showing the central, adjacent and unexplained structures recovered across all 32 decisions and eight states.
2. **A layer-by-layer, token-by-token reconstruction** preserving the intermediate evidence so that you can investigate any interesting relationship without requiring the entire analysis to be repeated.

The first gives you something to judge. The second explains where each finding came from.

**My responsibility is to reconstruct and expose the semantic information. Your responsibility is to decide whether that information is useful.**

That is the division of labour we established, applied directly to R020.

## Data sources and analysis boundary

Use the existing R020 evidence: `chatgpt_community_networks.json`, `chatgpt_layer_packets.md`, `community_nodes.csv`, `community_edges.csv`, `top_tokens_by_step_and_state.csv`, `state_transitions.csv`, `generation_transitions.csv` and the relevant control exports.

Do not rerun or modify measurement. Preserve traceability from reconstructed semantic parent to decision, state, sector, community and token evidence. Distinguish observations from interpretations. The analysis must not claim an independently blinded first pass if the continuation or anticipated adjacent topics have already been seen; record that limitation.

This document defines the analysis to perform, not the conclusions to obtain.
