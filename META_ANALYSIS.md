# LLM Topology Meta-analysis

## Agent usage instructions

This file is the chronological interpretive record for the LLM semantic
topology project. Agents working on the project must use it as follows:

1. Before adding an entry, read the canonical operating rules in
   `D:\Sync\zzCodexLearnings\AGENTS.md`, the project `README.md`, this section,
   and the manifest for every run discussed by the entry.
2. Treat existing entries as an append-only historical record. Do not silently
   rewrite, reorder, summarize or remove an earlier entry. Append a dated
   correction that cites the affected entry when a correction is necessary.
3. Assign entries sequential IDs in the form `MA-NNNN`. Never reuse an entry
   ID, including for corrections, failed runs or inconclusive analyses.
4. Timestamp every entry in ISO 8601 format with its UTC offset and record the
   named timezone. Use `Australia/Sydney` unless the project owner directs
   otherwise. If an original post time is unavailable, record the time the
   entry was added and state that limitation.
5. Record the author or source, entry type, related run IDs and preservation
   mode. Content marked `verbatim` must remain exactly as posted.
6. Keep directly observed findings, project-owner thoughts, assistant thoughts,
   limitations, decisions and proposed next steps explicitly separate. Do not
   convert an interpretation into a finding through repetition.
7. Link findings to a run manifest or artifact where possible. Preserve the
   distinction between behavioural observations, model-generated explanation,
   measured internal representations and causal conclusions.
8. Record negative, failed and ambiguous results. Do not allow the file to
   become a success-only narrative.
9. Use neutral run names chosen before results are inspected. When an entry
   reanalyses existing tensors rather than creating a new capture, identify its
   source run explicitly.
10. Keep machine-generated measurements in manifests and artifacts. Use this
    file for chronology, interpretation, disagreement, methodological changes
    and decisions rather than duplicating complete data tables.

## Entries

### MA-0001 — Semantic map of the project thread

- Entry timestamp: `2026-11-12T19:01:12+11:00`
- Timezone: `Australia/Sydney`
- Author: `Codex assistant`
- Entry type: `thread semantic map`
- Related runs: `R001`
- Preservation mode: `verbatim`
- Source: immediately preceding assistant response in the project thread
- Timestamp note: the original UI post time was unavailable; the entry timestamp
  records when this verbatim response was added to the project file

#### Verbatim input

The thread forms a clear progression from broad research theory to a specific measurable object, followed by experimental-governance requirements.

Legend: `[DONE]`, `[DECIDED]`, `[PLANNED]`, `[OPEN]`

```text
LLM SEMANTIC TOPOLOGY RESEARCH
|
|-- 1. Research foundations
|   |
|   |-- [DONE] Project handover supplied
|   |   |-- Semantic conflict in language models
|   |   |-- Internal representation geometry
|   |   |-- Relationship between behaviour and hidden structure
|   |   `-- Need to separate observation, interpretation and causation
|   |
|   |-- [DONE] Zombie-survival ChatGPT case examined
|   |   |-- Behavioural evidence of unstable/conflicting answers
|   |   |-- Demonstrates limitations of model self-explanation
|   |   |-- Does not directly measure internal representations
|   |   `-- Provides possible controlled stimuli for later experiments
|   |
|   `-- [DONE] External Gemini/Qwen discussion considered as context
|
|-- 2. Central research question
|   |
|   |-- How does a token's semantic neighbourhood change through a transformer?
|   |
|   |-- Initial hypotheses
|   |   |-- Final layer may be especially important
|   |   |-- Intermediate layers may contain more useful structure
|   |   `-- The optimal analytical layer should be tested, not assumed
|   |
|   `-- Intended eventual analysis
|       |-- Identify semantic neighbourhoods
|       |-- Detect topic-like groups
|       |-- Track their development across layers
|       `-- Determine which layers offer the most informative structure
|
|-- 3. Project infrastructure
|   |
|   |-- [DONE] Independent local Git repository
|   |   `-- D:\Sync\Python Projects\llm_topology
|   |
|   |-- [DONE] Published analysis copy
|   |   `-- chatgpt-analysis/projects/llm-topology
|   |
|   |-- [DECIDED] Repository roles
|   |   |-- Local repository = authoritative working project
|   |   `-- GitHub subproject = curated material for ChatGPT analysis
|   |
|   |-- [DONE] Shared model storage established
|   |   `-- D:\AI\cache\huggingface
|   |
|   `-- [DONE] Cross-project model-storage rule documented
|       `-- D:\Sync\zzCodexLearnings\AGENTS.md
|
|-- 4. Model familiarisation
|   |
|   |-- [DONE] Pythia prompt playground created
|   |
|   |-- Model progression
|   |   |-- Pythia 410M
|   |   |   `-- Lightweight initial behavioural baseline
|   |   |
|   |   |-- Pythia 6.9B
|   |   |   `-- Practical balance for representation analysis
|   |   |
|   |   `-- Pythia 12B
|   |       `-- Fits narrowly on the RTX 4090 but limits experimental headroom
|   |
|   |-- [DONE] Notebook made model-switchable
|   |
|   `-- [DECIDED] Smaller models remain scientifically useful
|       |-- Faster iteration
|       |-- More layers/prompts can be examined
|       `-- Greater experimental control
|
|-- 5. Representation-object clarification
|   |
|   |-- Input embedding matrix
|   |   |-- Static vocabulary-scale representation
|   |   `-- Provides interpretable semantic neighbours
|   |
|   |-- Hidden states
|   |   |-- Contextual token representations
|   |   |-- Change through transformer states
|   |   `-- Are not themselves vocabulary embedding matrices
|   |
|   |-- Final predictions
|   |   |-- Generation-facing probabilities
|   |   `-- Must not be treated as equivalent to embedding similarity
|   |
|   `-- [DECIDED] These objects must remain analytically distinct
|
|-- 6. Proof-of-concept scope
|   |
|   |-- [DECIDED] One prompt
|   |   `-- Battery demand, mineral supply, electric vehicles, and
|   |       energy storage all shape the market for lithium
|   |
|   |-- [DECIDED] One target token
|   |   `-- " lithium"
|   |
|   |-- [DECIDED] One model
|   |   `-- EleutherAI/pythia-6.9b
|   |
|   `-- Initial purpose
|       |-- Validate hidden-state capture
|       |-- Inspect available outputs
|       `-- Determine which outputs deserve further development
|
|-- 7. R001: Lithium initial output inspection
|   |
|   |-- [DONE] Successful model execution
|   |   |-- 33 recorded representation states
|   |   |-- 19 prompt tokens
|   |   |-- 4096 hidden dimensions
|   |   `-- Artifact hashes verified
|   |
|   |-- Produced artifacts
|   |   |
|   |   |-- hidden_states.safetensors
|   |   |   `-- Primary captured representation data
|   |   |
|   |   |-- semantic_neighbors.csv
|   |   |   |-- Input-embedding cosine neighbours
|   |   |   `-- Final-prediction probabilities
|   |   |
|   |   |-- target_relationships.csv
|   |   |   `-- Target-to-prompt-token similarities by state
|   |   |
|   |   |-- layer_metrics.csv
|   |   |   `-- Norm, distance and angular diagnostics
|   |   |
|   |   |-- tokens.csv
|   |   |   `-- Tokenization and target-position provenance
|   |   |
|   |   `-- Figures
|   |       |-- Target trajectory
|   |       |-- Target relationships
|   |       `-- Prompt-token similarity by selected state
|   |
|   `-- [DONE] Meaningful run identity assigned
|       `-- R001_lithium-initial-output-inspection__
|           20261112T063540Z_pythia-6.9b_52ff8f97c2
|
|-- 8. Interpretation of R001
|   |
|   |-- Project-owner assessment
|   |   |
|   |   |-- layer_metrics
|   |   |   `-- Not immediately useful as a primary analytical result
|   |   |
|   |   |-- semantic_neighbors
|   |   |   |-- decoded_token is useful
|   |   |   `-- input_embedding results are the most useful output
|   |   |
|   |   |-- target_relationships
|   |   |   |-- Evolution of other_token is interesting
|   |   |   `-- Probably secondary to the wider vocabulary relationships
|   |   |
|   |   `-- tokens.csv
|   |       |-- Interesting for confirming the true target
|   |       `-- Not a primary analytical result
|   |
|   `-- Assistant interpretation
|       |
|       |-- layer_metrics
|       |   |-- Diagnostic rather than semantic
|       |   `-- May reveal architectural boundaries such as final normalization
|       |
|       |-- target_relationships
|       |   `-- Measures prompt-local rather than vocabulary-scale structure
|       |
|       |-- tokens.csv
|       |   `-- Provenance and quality-control evidence
|       |
|       `-- Missing primary object
|           `-- Vocabulary-scale semantic neighbours at every model state
|
|-- 9. Semantic-neighbour cutoff problem
|   |
|   |-- Proposed neighbourhood definition
|   |   `-- Include tokens whose semantic-neighbour score passes a cutoff
|   |
|   |-- Current score meanings
|   |   |-- input_embedding score = cosine similarity
|   |   `-- final_prediction score = probability
|   |
|   |-- [DECIDED] Different metrics cannot be mixed into one cutoff
|   |
|   |-- Raw-score cutoff
|   |   |-- Defines a fixed geometric radius
|   |   |-- Allows neighbourhood expansion and contraction
|   |   `-- Requires sensitivity analysis
|   |
|   |-- Elbow cutoff
|   |   |-- Can be applied to any ranked continuous score distribution
|   |   |-- Must be applied separately by state, source and metric
|   |   |-- Produces an adaptive boundary
|   |   `-- Must be allowed to report "no viable elbow"
|   |
|   `-- Important caveats
|       |-- Current top-20 list is too truncated
|       |-- Lexical fragments may form their own apparent elbow
|       |-- An elbow is mathematical structure, not automatically semantic
|       `-- Cutoff movement must be separated from token-score movement
|
|-- 10. Next analytical experiment
|   |
|   |-- [PLANNED] Calculate full vocabulary score vectors
|   |   |
|   |   |-- For every recorded model state
|   |   |-- Target representation compared with every input embedding
|   |   `-- Approximately 33 x 50,000 scores
|   |
|   |-- [DECIDED] Do not calculate a 50,000 x 50,000 matrix yet
|   |
|   |-- [PLANNED] Determine cutoff viability for every state
|   |   |
|   |   |-- Elbow rank
|   |   |-- Elbow score
|   |   |-- Elbow strength
|   |   |-- Score gap
|   |   `-- Status: viable, weak or none
|   |
|   |-- [PLANNED] Preserve both analytical views
|   |   |-- Adaptive elbow neighbourhood
|   |   `-- Fixed raw-score neighbourhood
|   |
|   `-- [DEFERRED] Relations and topic modelling
|       |-- Token entry and exit
|       |-- Persistence
|       |-- Neighbourhood overlap
|       |-- Token-relation graphs
|       `-- Topic/community evolution
|
`-- 11. Experimental governance
    |
    |-- [DONE] Run-naming convention established
    |   `-- RNNN_<target>-<purpose>__<UTC>_<model>_<prompt-hash>
    |
    |-- [DECIDED] Naming principles
    |   |-- Purpose chosen before inspecting results
    |   |-- No result-biased names
    |   |-- Run numbers never reused
    |   `-- Failed and invalid runs remain part of the sequence
    |
    |-- [PLANNED] Meta-analysis record
    |   |
    |   |-- Findings
    |   |-- Project-owner thoughts
    |   |-- Assistant thoughts
    |   |-- Limitations and confounds
    |   |-- Decisions
    |   `-- Next task
    |
    `-- [OPEN] Meta-analysis design decisions
        |-- Exact file structure
        |-- Run-entry template
        |-- How much verbatim conversation to preserve
        |-- How to distinguish evidence from retrospective interpretation
        `-- How derived analyses should reference their source run
```

The central semantic sequence is:

```text
broad theory
    -> model familiarisation
        -> single-prompt capture
            -> inspection of available outputs
                -> input-embedding neighbours identified as primary
                    -> full-vocabulary layerwise scoring proposed
                        -> cutoff viability becomes the next experiment
                            -> repeated runs require formal meta-analysis
```
