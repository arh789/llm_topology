# ChatGPT analysis instructions for R008

- Added: `2026-11-13T07:27:33+11:00`
- Timezone: `Australia/Sydney`
- Source: `Codex suggestions requested by the project owner`
- Related run: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Status: `post-run analytical companion; not a measured R008 artifact and not part of the validated manifest`

## Role

You are the semantic analyst for the LLM Topology project. Codex has already
measured, validated and exported the networks. Your task is to interpret that
evidence, not redesign the extraction pipeline.

## Repository

The project is published at:

<https://github.com/arh789/chatgpt-analysis/tree/main/projects/llm-topology>

## Context reading order

Read these files in order:

1. `README.md`
2. `PROJECT_HANDOVER.md`
3. `META_ANALYSIS.md`, especially entries MA-0013 through MA-0020
4. `single_prompt_topology/R008_PLAN.md`
5. The successful R008 `manifest.json` and `findings.md`
6. The primary analysis data:
   - `chatgpt_community_networks.json`
   - `chatgpt_layer_packets.md`
7. Supporting tables when required:
   - `community_nodes.csv`
   - `community_edges.csv`
   - `state_transitions.csv`
   - `cross_side_edges.csv.gz`

Do not use `ANALYSIS_BRIEF.md` as a current evidence summary. It predates these
experiments and states that no experimental data exist.

## Measurement definition

- There are 33 recorded states.
- Each state has a positive-head network and a negative-tail network.
- Positive means high cosine alignment between the contextual representation
  of `lithium` and static vocabulary embeddings.
- Negative means geometric anti-alignment.
- The vocabulary embedding geometry is fixed. Layer-wise change comes from
  changing population membership.
- Communities are state-local Louvain partitions. Community IDs do not identify
  the same community across different states.
- Cross-side edges are a secondary subset retained from R005's combined
  10-nearest-neighbour graph. They are not a complete bipartite network.

## Claims that must not be assumed

Do not assume:

- positive means semantically central;
- negative means suppressed, rejected, contradictory or false;
- a Louvain community is necessarily a topic;
- persistence proves semantic importance;
- modularity measures semantic coherence;
- the input-to-block-0 or final-state discontinuities represent curvature;
- the final transition can distinguish block 31 from final normalization.

## Primary analytical task

Determine:

1. What candidate semantic, lexical, morphological, numeric, named-entity and
   tokenizer-driven structures occur within each side?
2. Which structures persist, emerge, disappear, split or merge across states?
3. Are positive and negative networks organized differently, or do they
   contain comparable kinds of structure?
4. Which negative communities are plausible competing interpretations of the
   lithium prompt rather than unrelated geometric anti-alignment?
5. Which cross-side relationships connect similar structures, and which
   suggest genuine differentiation?
6. Where is the structure most stable or unstable?
7. What observations could support later tests of suppression, coherence
   boundaries or competing semantic constraints?
8. What evidence contradicts those interpretations?

For community correspondence across states, infer relationships from token
overlap, representative tokens, membership changes and edge evidence. Do not
match communities merely because they share a community ID.

## Candidate community classification

Classify candidate communities as:

- semantic or topical;
- lexical or morphological;
- named-entity;
- numeric;
- formatting or tokenizer-driven;
- mixed;
- unclear.

Give each interpretation a confidence level and cite the state, side, community
ID and representative tokens supporting it.

## Required output

Produce:

1. A measurement recap.
2. A data-quality and tokenizer-artifact audit.
3. A state-by-state comparison covering all 33 states.
4. Cross-layer trajectories of the strongest candidate structures.
5. A positive-versus-negative comparison.
6. Analysis of the input-to-block-0 and block-30-to-final discontinuities.
7. Candidate suppressed or competing structures, explicitly marked as
   hypotheses.
8. Evidence against the suppression or coherence interpretation.
9. A claims table separating:
   - directly measured;
   - reasonable interpretation;
   - unresolved hypothesis;
   - unsupported claim.
10. Three to five falsifiable predictions for a controlled follow-up
    experiment.

Do not label communities as SDA-3 Central, Suppressed, Adjacent or Emerging
unless you provide explicit evidence and retain the label as provisional.

The goal is not to produce an attractive narrative. It is to identify which
structures are genuinely interpretable, which are tokenizer artifacts, what
changes through depth and what controlled experiment should test the resulting
hypotheses.

## Final note

These instructions are Codex suggestions. Your actual instructions may change
following supervised guidance from the project owner.
