# R009 analysis protocol: lithium community semantic classification

## Run identity

- Run number: `R009`
- Neutral run name: `lithium-community-semantic-classification`
- Run type: interpretive semantic analysis
- Analysis model: **GPT-5.6 Sol**
- Measurement source: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Representation-generating model: `EleutherAI/pythia-6.9b`
- Pythia revision: `c0e3eee36dc47af0c49f361c74cfe459c09f7f23`
- Target token: ` lithium`
- Target token ID: `27747`
- Prompt: `Battery demand, mineral supply, electric vehicles, and energy storage all shape the market for lithium`

R009 does not run Pythia, recalculate scores, alter R004 cutoffs, alter R008
communities, or create new measured network evidence. It is a state-by-state
semantic interpretation of the 792 state-local Louvain community instances
exported by R008.

## Objective

For every community at every recorded state, answer the first-order descriptive
question:

> **What is this community?**

The purpose of this pass is to determine whether R008's geometric communities
can be assigned defensible broad identities before any attempt is made to infer
their SDA-3 structural role.

This is intentionally prior to analysing coherence, persistence, emergence,
suppression or cross-layer trajectories.

## States

R009 analyses all 33 R008 states, one state at a time:

- State 00: input embedding
- States 01–31: block 0 through block 30 outputs
- State 32: final normalisation after block 31

Raw block 31 output is not separately captured. State 32 therefore combines
the block 31 transformation with final layer normalisation.

## Primary evidence

Use the successful R008 artifacts, principally:

1. `community_nodes.csv`
2. `chatgpt_layer_packets.md`
3. `chatgpt_community_networks.json`
4. `community_edges.csv`
5. complete node/edge evidence when compact evidence is insufficient

`COMMUNITY_COUNTS_BY_STATE.md` is used to reconcile expected community counts.

Representative and target-extreme tokens are evidence samples, not complete
definitions of a community. When those samples do not support a stable
interpretation, inspect broader membership or relationships before assigning a
topic. If a defensible identity still cannot be established, classify the
community as unclear rather than forcing a semantic label.

## Required procedure for each state

1. Reconcile the expected positive-head and negative-tail community counts.
2. Inspect every community on both sides.
3. Examine representative tokens, target-extreme tokens and, where necessary,
   broader membership and internal relationships.
4. Assign the broadest defensible community identity.
5. Assign one structure type from the fixed taxonomy below.
6. Assign confidence.
7. Record brief evidence supporting the classification.
8. Complete a state-level descriptive summary.
9. Verify that every expected community has exactly one classification.
10. Stop. Do not inspect the next state until the project owner instructs
    `proceed`.

## Fixed classification taxonomy

Each community receives one primary structure type:

- **semantic/topic** — membership is predominantly organised around a
  recognisable subject, concept or domain;
- **lexical/morphological** — organisation is predominantly word-form,
  affix, spelling or morphological similarity;
- **named-entity** — organisation is predominantly people, places,
  organisations or comparable proper names;
- **numeric** — organisation is predominantly numbers or numeric strings;
- **formatting/tokenizer** — organisation is predominantly punctuation,
  whitespace, encoding fragments or tokenizer artefacts;
- **mixed** — more than one organising principle is materially present and no
  single permitted type adequately describes the community;
- **unclear** — available evidence does not support a defensible identity.

A short secondary descriptor may be added when useful, but the primary type
must remain one of these categories throughout R009.

## Confidence

- **High** — the sampled and supporting evidence strongly converges on one
  identity.
- **Moderate** — a plausible dominant identity exists but substantial
  heterogeneity or ambiguity remains.
- **Low** — the proposed identity is weak and should be treated as provisional.

`Unclear` is preferred to a low-confidence semantic label when no meaningful
organising principle can be established.

## Required community record

Every state file must record, for every community:

| Field | Requirement |
|---|---|
| State | R008 state index and label |
| Side | `positive_head` or `negative_tail` |
| Community ID | R008 state-local community ID |
| Size | R008 community size |
| Broad identity | Plain-language answer to “what is this community?” |
| Structure type | One fixed taxonomy category |
| Confidence | High / Moderate / Low |
| Evidence | Concise representative evidence and qualification |

Community IDs are state-local. The same ID at another state must never be
treated as the same community without a later cross-state correspondence
analysis.

## Interpretation boundaries

During the state-by-state classification pass, do **not**:

- label a community SDA-3 Central, Suppressed, Adjacent, HCU or Emerging;
- assume positive alignment means semantic centrality or coherence;
- assume negative anti-alignment means suppression, contradiction, rejection
  or exclusion;
- treat Louvain modularity as semantic coherence;
- infer that communities at different states persist merely because their IDs
  match;
- infer cross-layer emergence, disappearance, splitting or merging;
- identify an optimal layer;
- infer curvature density;
- reinterpret R008 measurements to make them fit SDA-3;
- use later states to retroactively force earlier state classifications.

The positive/negative side is retained as measured provenance but is not itself
a semantic label.

## SDA-3 relationship

R009 is designed to create the descriptive substrate required to test SDA-3,
not to validate SDA-3 by construction.

The intended analytical order is:

```text
WHAT each community is
        ↓
WHICH communities are semantically coherent
        ↓
HOW coherent structures change across states
        ↓
WHAT structural roles those structures occupy
        ↓
DO those roles correspond to SDA-3?
```

Only after all 33 states are classified and checked for schema consistency
should cross-state synthesis begin.

## Completion criteria

The first-pass R009 classification is complete only when:

- all 33 state files exist;
- all 792 R008 state-local community instances have exactly one classification;
- per-state positive and negative counts reconcile with R008;
- the fixed taxonomy and confidence scheme have been applied consistently;
- no SDA-3 role has been assigned during the descriptive pass;
- ambiguities and tokenizer artefacts remain visible rather than being
  rewritten as semantic topics.

A synthesis file should be created only after these conditions are met.
