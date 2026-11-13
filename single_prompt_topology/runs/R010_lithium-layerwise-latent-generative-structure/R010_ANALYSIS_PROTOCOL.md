# R010 analysis protocol: lithium layer-wise latent generative structure

## Run identity

- Run number: `R010`
- Neutral run name: `lithium-layerwise-latent-generative-structure`
- Run type: interpretive structural reconstruction
- Analysis model: **GPT-5.6 Sol**
- Primary interpretive source: `R009_lithium-community-semantic-classification`
- Measurement source: `R008_lithium-chatgpt-readable-split-networks-validated-retry__20261112T200904Z_pythia-6.9b_52ff8f97c2`
- Representation-generating model: `EleutherAI/pythia-6.9b`
- Pythia revision: `c0e3eee36dc47af0c49f361c74cfe459c09f7f23`
- Target token: ` lithium`
- Target token ID: `27747`
- Prompt: `Battery demand, mineral supply, electric vehicles, and energy storage all shape the market for lithium`

R010 does not run Pythia, recalculate scores, alter R004 cutoffs, alter R008
networks or communities, or modify the R009 state-local classifications.

R010 is a higher-order interpretive analysis. It attempts to reconstruct, at
each recorded transformer state independently, the smallest defensible set of
latent parent structures that could explain the observed collection of R009
communities and their R008 graph-central representative tokens.

The inferred parent structures are analytical hypotheses. They are not measured
nodes in R008 and are not causal claims about transformer mechanisms.

## Primary objective

For each transformer state, answer:

> **What minimum set of higher-order latent structures could plausibly generate
> the observed community organisation at this state?**

The unit of analysis is therefore no longer the individual community alone.

The intended abstraction is:

```text
observed R008 community
        +
R009 identity
        +
R008 graph-central representatives
        ↓
candidate first-order parent
        ↓
relations among parent candidates
        ↓
minimal state-level generative structure
```

Only after all 33 states have been reconstructed independently may R010 compare
those state-level structures and ask whether an evolution occurs across the
transformer.

## Research questions

### Phase A — independent state reconstruction

For each state:

1. Which communities are meaningfully semantic rather than primarily formal,
   lexical, numeric or tokenizer-organised?
2. Which higher-order parent candidates can explain multiple communities?
3. Which communities remain irreducible, mixed or ungrouped?
4. What relations exist among the inferred parent candidates?
5. What is the minimum defensible state-level architecture that explains the
   observed organisation without collapsing into vacuous abstractions?
6. How much of the state population does each parent account for?
7. Which alternative reconstruction is most plausible if the preferred one is
   wrong?

### Phase B — cross-state structural evolution

Only after Phase A is complete and verified:

1. Which independently inferred parent structures correspond across states?
2. Which persist, strengthen, weaken, broaden, narrow, split, merge, disappear,
   reappear or change side?
3. Does the layer-level architecture become more or less abstract, differentiated
   or integrated?
4. Is there a coherent developmental trajectory through the transformer?
5. Where are the largest semantic-architectural discontinuities?

### Phase C — comparison with measured R008 topology

Only after Phase B:

1. Do large inferred semantic changes coincide with large measured changes in
   R008 membership Jaccard, edge Jaccard, community ARI or other network
   quantities?
2. Do semantic and measured discontinuities agree at the input-to-block-0 and
   block-30-to-final-normalisation transitions?
3. Where do semantic interpretation and measured topology disagree?

SDA-3 role testing, optimal-layer judgement and curvature/coherence inference
remain outside Phase A and Phase B unless separately authorised after the
structural trajectory is established.

## States

R010 analyses the same 33 recorded states as R009:

- State 00: input embedding
- States 01–31: block 0 through block 30 outputs
- State 32: final normalisation after block 31

Raw block 31 output is not separately captured. State 32 combines the block 31
transformation with final layer normalisation.

## Evidence hierarchy

For the state currently under analysis, use evidence in this order.

### Mandatory evidence

Every community must be inspected at the underlying R008 level before its R010
disposition or parent assignment is finalised.

For the state currently under analysis, use:

1. The corresponding R009 state file.
2. The same state's records in `R009_SUMMARY.html`, including:
   - broad identity;
   - structure type;
   - confidence;
   - community size;
   - side;
   - top ten R008 graph-degree representative tokens.
3. The corresponding state-side communities in
   `R008/chatgpt_community_networks.json`.
4. The underlying R008 community membership in `R008/nodes.csv.gz`.
5. The underlying within-side graph evidence in `R008/edges.csv.gz` and/or
   `R008/community_edges.csv` as needed to understand the community's
   organisation and relation to other communities.
6. `R008/cross_side_edges.csv.gz` when evaluating a proposed cross-side bridge.

The HTML report and R009 prose are indexing and interpretive aids. They are not
sufficient evidence by themselves for a final R010 parent assignment.

For **every** community, the analyst must inspect its underlying membership
rather than relying only on the broad identity or top-ten representatives.
Where the full community is large, inspection may use systematic membership
slices or summaries, but those must derive from the complete R008 membership,
not only from the compact R009/R008 representative samples.

The R009 broad identity is evidence, not ground truth. Where the R009 prose
identity conflicts with the underlying membership or graph-central
representative evidence, the discrepancy must be recorded and the parent
inference must follow the stronger underlying evidence.

The R009 broad identity is evidence, not ground truth. Where the R009 prose
identity conflicts with the representative-token evidence, the discrepancy
must be recorded and the parent inference must follow the stronger underlying
evidence.

## Meaning of representative tokens

The ten summary tokens are the first ten R008 `representative_tokens`, ranked
by descending node degree inside the undirected state-side community graph, with
token ID as deterministic tie-breaker.

They are therefore evidence of **within-community structural centrality**.

They are not:

- the ten highest positive target-cosine tokens;
- the ten lowest negative target-cosine tokens;
- direct measures of semantic importance to the target;
- sufficient by themselves to establish a community identity.

Target-extreme tokens may be inspected separately when needed but must not be
confused with graph-central representatives.

## Latent parent definition

A **latent parent candidate** is an inferred higher-order semantic or relational
structure that explains why two or more observed communities could belong to a
larger organised system at the same state.

Examples of the form of a valid parent include:

- knowledge formation;
- biological/health systems;
- control and constraint;
- physical/material systems;
- social/organisational activity;
- transformation and change.

These examples are illustrative only. They must not be treated as a fixed
taxonomy or searched for in every state.

A parent candidate is not an R008 node and is not assumed to exist internally
as an explicit transformer feature.

## Parent eligibility rules

A candidate parent should be retained only when all of the following hold:

1. **Explanatory scope** — it explains at least two observed communities, unless
   a single exceptionally large coherent community is explicitly retained as an
   irreducible state-level structure rather than promoted to a parent.
2. **Shared organising relation** — the child communities share more than a
   superficial word or domain overlap.
3. **Discriminative value** — the parent excludes meaningful alternatives. A
   label such as `system`, `things`, `process` or `information` is too
   broad unless further qualified.
4. **Evidence support** — the R009 identities and/or graph-central
   representative tokens support the proposed relation.
5. **Compression** — the parent reduces descriptive complexity by explaining
   multiple communities with one higher-order structure.
6. **Non-forcing** — communities that do not fit cleanly remain ungrouped or
   mixed rather than being absorbed to maximise coverage.

The preferred reconstruction should use the smallest set of parents that
preserves meaningful distinctions.

## Anti-vacuity rule

R010 must not maximise compression by creating abstractions so broad that they
could explain most arbitrary communities.

For each parent candidate, record:

- what it explains;
- what it deliberately does **not** explain;
- why a broader label would lose discriminative value.

A parent that cannot state a meaningful exclusion boundary is not a valid
parent.

## Hierarchical reconstruction

R010 may infer more than one level of abstraction when justified:

```text
community
    ↓
first-order parent
    ↓
higher-order parent
    ↓
state-level architecture
```

Higher-order parents must satisfy the same eligibility and anti-vacuity rules.

Do not force a second level when the first-order parents do not support one.

## Community assignment

Every community receives exactly one **primary disposition**:

- `parent:<parent-id>` — primarily explained by one retained parent;
- `formal-substrate` — primarily lexical/morphological, numeric,
  formatting/tokenizer or other representational-form organisation;
- `irreducible-semantic` — coherent semantic structure not defensibly grouped
  with another community;
- `mixed-unresolved` — materially heterogeneous and not safely assignable;
- `unclear` — evidence insufficient.

A community may additionally receive zero or more **secondary parent links**
when it genuinely bridges structures.

Primary assignment is exclusive so node-weighted coverage remains
interpretable. Secondary links are non-exclusive and are reported separately.

## Treatment of R009 structure types

### semantic/topic

Eligible for semantic parent inference.

### mixed

Eligible only when the relevant organising relation is supported by the
representative tokens or broader evidence. Mixed communities must not be
silently rewritten as coherent semantic nodes.

### named-entity

Do not automatically classify as formal substrate. Determine whether the names
form a meaningful semantic/geographic/social organisation at that state. If not,
retain them as representational/name organisation.

### lexical/morphological, numeric, formatting/tokenizer

Default to `formal-substrate` unless unusually strong evidence establishes a
meaningful semantic organisation beyond form.

### unclear

Default to `unclear`; inspect escalation evidence only if the community is
large enough to materially affect the state reconstruction.

## Positive and negative sides

Positive-head and negative-tail populations are measured R008 provenance, not
semantic roles.

For every state:

1. infer positive-side parent candidates independently;
2. infer negative-side parent candidates independently;
3. only after both side-specific reconstructions are frozen, inspect whether
   higher-order **cross-side bridge candidates** relate them.

Do not assume:

- positive = central, coherent, supported or selected;
- negative = suppressed, contradictory, rejected or excluded;
- a semantic parent found on both sides has the same structural role on each.

A cross-side bridge is a state-local relational hypothesis, not an SDA-3 role.

## Parent identifiers

Within each state:

- positive parents: `P+` followed by a local integer, e.g. `P+0`;
- negative parents: `P-` followed by a local integer, e.g. `P-0`;
- cross-side bridge candidates: `B` followed by a local integer, e.g. `B0`.

Identifiers are state-local.

The same identifier at another state has no continuity meaning.

## Node-weighted coverage

For a retained parent, primary node coverage is:

[
mathrm{coverage}(P)
=
rac{sum_{c in mathrm{primaryChildren}(P)} |c|}
     {sum_{c in mathrm{eligibleStatePopulation}} |c|}
]

Report both:

1. **side-relative coverage** — denominator is the total node count on that side;
2. **semantic-eligible coverage** — denominator excludes communities assigned
   to `formal-substrate` and `unclear`.

Because primary assignments are exclusive, primary coverage values can be
summed without double counting.

Secondary links must never be added into primary coverage totals.

Also report the total proportion of each side assigned to:

- retained semantic parents;
- formal substrate;
- irreducible semantic structures;
- mixed unresolved structures;
- unclear structures.

## Parent record

Every retained parent candidate must record:

| Field | Requirement |
|---|---|
| Parent ID | State-local `P+` or `P-` identifier |
| Parent identity | Broadest defensible higher-order structure |
| Side | positive_head or negative_tail |
| Primary child communities | Exact R008/R009 community IDs |
| Secondary child communities | Optional bridging communities |
| Primary node count | Sum of primary child sizes |
| Side-relative coverage | Percentage of all nodes on that side |
| Semantic-eligible coverage | Percentage of eligible semantic nodes |
| Confidence | High / Moderate / Low |
| Evidence | Identities + graph-central tokens supporting the parent |
| Exclusion boundary | Relevant communities the parent does not explain |
| Alternative parent | Strongest competing interpretation |

## Community disposition record

Every community must appear exactly once in a disposition table:

| Field | Requirement |
|---|---|
| Side | positive_head / negative_tail |
| Community ID | State-local R008/R009 ID |
| Size | R008/R009 size |
| R009 identity | Existing descriptive identity |
| Primary disposition | parent ID or non-parent category |
| Secondary parent links | Optional |
| Reason | Concise assignment rationale |

## Relations among parents

After side-specific parents are inferred, identify only relations supported by
the current state's evidence.

Permitted relation descriptors include:

- contains / specialises;
- overlaps;
- complementary;
- competing;
- process-of;
- object-of;
- regulates / constrains;
- transforms;
- measures / characterises;
- social/institutional relation;
- uncertain relation.

These are descriptive hypotheses, not causal transformer claims.

Do not add a relation merely to make the state graph connected.

## Cross-side bridge record

A bridge candidate should be created only when positive and negative parent
structures appear to participate in a larger discriminative relation.

Record:

| Field | Requirement |
|---|---|
| Bridge ID | State-local `B#` |
| Positive parent(s) | Exact IDs |
| Negative parent(s) | Exact IDs |
| Candidate higher-order relation | Plain-language relation |
| Evidence | Why the structures belong in one larger frame |
| Confidence | High / Moderate / Low |
| Alternative | Strongest non-bridge explanation |

Absence of a defensible cross-side bridge is an acceptable result.

## Minimal state-level architecture

Each state file must conclude with a compact reconstruction showing:

1. retained positive parents;
2. retained negative parents;
3. formal/representational substrate;
4. irreducible or unresolved communities;
5. supported relations among parents;
6. supported cross-side bridges;
7. the smallest higher-order structure that explains the state without
   violating the anti-vacuity rule.

An ASCII tree or graph may be used, but it must preserve uncertainty and must
not imply measured edges between inferred parents.

## Alternative reconstruction

Every state must include at least one serious alternative if the preferred
architecture depends on Moderate- or Low-confidence parent inference.

The alternative must state what evidence would favour it over the preferred
reconstruction.

If all retained parents are High confidence and no meaningful alternative
exists, state that explicitly.

## Required procedure for each state

1. Reconcile the state's R009 community count and R008 community sizes.
2. Inspect only the current state's R009 state file and summary records.
3. Inspect its graph-central representative tokens.
4. Escalate to broader R008 evidence only where needed.
5. Partition formal/representational organisation from semantic candidates.
6. Infer positive-side parent candidates.
7. Freeze the positive-side reconstruction.
8. Infer negative-side parent candidates.
9. Freeze the negative-side reconstruction.
10. Evaluate state-local relations among parents.
11. Evaluate cross-side bridge candidates.
12. Assign every community exactly one primary disposition.
13. Calculate node-weighted coverage.
14. Construct the minimal state-level architecture.
15. Record alternatives and uncertainty.
16. Verify all communities are accounted for exactly once.
17. Write and commit the state file.
18. Fetch and verify the committed file.
19. Stop without inspecting the next state's R010 reconstruction.

## Contamination controls

During Phase A, the analysis of State N must be independent of inferred R010
structures for every other state.

Do **not**:

- inspect another R010 state reconstruction while constructing the current one;
- use a parent found at an earlier state as a template for the current state;
- preserve a parent merely to create apparent continuity;
- rename a current parent to match another state;
- infer persistence, emergence, disappearance, split, merge or polarity change;
- use later states to reinterpret the current state;
- optimise parent labels for future cross-state matching.

The underlying R009 state files necessarily exist for all states, but Phase A
analysis must only inspect the current state's semantic evidence.

The current state may use global R008 methodological documentation, but not
semantic content from other states as evidence for its parent reconstruction.

## Interpretation boundaries during Phase A

Do **not**:

- assign SDA-3 Central, Suppressed, Adjacent, HCU or Emerging roles;
- assume positive or negative side has a specific semantic role;
- infer cross-state continuity;
- identify an optimal transformer layer;
- infer curvature density;
- claim causal transformer mechanisms;
- treat inferred parents as measured network nodes;
- treat semantic compression as proof of semantic coherence;
- force all communities into one connected ontology.

## Phase A output file

Each state produces:

`STATE_XX_<state-label>_LATENT_STRUCTURE.md`

Required sections:

1. State identity
2. Evidence inventory
3. Population accounting
4. Positive-side reconstruction
5. Negative-side reconstruction
6. Community disposition table
7. Parent coverage table
8. Relations among parents
9. Cross-side bridge candidates
10. Formal/representational substrate
11. Minimal state-level architecture
12. Alternative reconstruction
13. Uncertainty record
14. Verification
15. R010 Phase-A boundary

## Phase A completion criteria

Phase A is complete only when:

- all 33 R010 state files exist;
- every R009 community instance has exactly one primary disposition in the
  corresponding state;
- all 792 R009 community instances are accounted for exactly once;
- primary node coverage reconciles with community sizes;
- side-relative and semantic-eligible coverage calculations reconcile;
- parent identifiers are state-local and contiguous within each side;
- every retained parent has an exclusion boundary;
- Moderate/Low parent structures have alternatives where material;
- no cross-state persistence or evolution has been inferred;
- no SDA-3 role has been assigned;
- no optimal-layer or curvature claim has been made.

## Phase A execution cadence

During Phase A, each project-owner instruction `proceed` advances **exactly
one state**:

1. identify the next unreconstructed state;
2. reconstruct that state under this protocol;
3. write its R010 state file;
4. verify the file and accounting;
5. stop.

No `proceed` during Phase A may silently analyse multiple states.

After State 32 is complete, the next `proceed` changes function and initiates
Phase-A completeness verification.

## Phase B protocol boundary

Phase B must not begin until Phase A completeness verification passes.

Phase B will consume the **frozen independent state reconstructions**, not
reconstruct the states retrospectively.

Its first task will be to infer correspondence among independently derived
parent structures without assuming that state-local parent IDs persist.

The allowed state-to-state trajectory descriptors are:

- persistent;
- strengthening;
- weakening;
- broadening;
- narrowing;
- split;
- merge;
- appearance;
- disappearance;
- reappearance;
- side change;
- uncertain correspondence.

Phase B must preserve competing correspondence hypotheses where the evidence is
ambiguous.

A separate synthesis artifact should be created for Phase B rather than editing
the Phase-A state files.

## Phase C protocol boundary

Only after Phase B establishes a semantic structural trajectory may R010 compare
that trajectory against R008 measured topology.

This comparison should use pre-existing measured quantities rather than
retrofitting the semantic reconstruction to them.

Particular attention should be paid to whether independently inferred semantic
discontinuities coincide with measured discontinuities in:

- membership Jaccard;
- edge Jaccard;
- community ARI;
- population size;
- community count;
- intercommunity organisation.

Agreement is evidence of correspondence between semantic interpretation and
measured topology. Disagreement must remain visible and may be more informative
than agreement.

## SDA-3 and curvature boundary

R010 does not validate SDA-3 by construction.

Only after the independent layer structures, cross-state trajectory and
measured-topology comparison are available should a later authorised analysis
ask whether recurrent structures support the roles:

- Central;
- Suppressed;
- Adjacent;
- Highly Correlated Unrelated;
- Emerging.

Likewise, curvature/coherence claims require a separately defined operational
measure. R010 parent inference alone cannot establish geometric curvature.
