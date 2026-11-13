# R010 Phase D — curvature and coherence measurement protocol

## Status

**PROTOCOL FROZEN BEFORE PHASE-D CALCULATION**

This file defines the Phase-D measurement procedure before any Phase-D rankings or composite results are calculated.

Phase D consumes the already-frozen R008 measured topology, R009 community classifications, R010 Phase-A state reconstructions, R010 Phase-B semantic trajectory and R010 Phase-C comparison. It does not rerun Pythia, alter R004 cut-offs, alter R008 graphs or communities, or revise Phase-A/B/C conclusions to improve Phase-D fit.

## Primary question

> **Where across transformer depth does the representation become hardest to compress into a coherent higher-order structure, and what kind of structural change resolves that difficulty?**

## Units of analysis

Two units are kept separate.

### Transition-level

32 adjacent transitions:

- S00→S01 through S31→S32.

These are used for curvature.

### State-level

33 recorded states:

- S00 through S32.

These are used for coherence difficulty.

Positive-head and negative-tail sectors are calculated separately first. A combined value may then be formed as the unweighted arithmetic mean of the two side-specific values.

The endpoint transitions S00→S01 and S31→S32 are retained, but all rankings are also reported for the 30 internal transitions so endpoint resets cannot hide internal structure.

## Data sources

### R008 measured topology

Primary fields:

- membership Jaccard;
- edge Jaccard;
- community adjusted Rand index (ARI);
- population size;
- community count.

Secondary diagnostic only:

- modularity;
- clustering;
- target cosine and other network-index fields.

### R010 Phase A

Per-state community dispositions:

- parent:<id>;
- mixed-unresolved;
- irreducible-semantic;
- formal-substrate;
- unclear.

Per-parent fields:

- semantic-eligible coverage;
- node count;
- confidence;
- alternative reconstruction.

### R010 Phase B

Frozen cross-state semantic interpretation:

- retained-parent counts;
- dominant semantic-parent coverage;
- explicit split / merge / appearance / disappearance / reappearance / absorption / replacement / reconfiguration events.

### R010 Phase C

Used only as an already-existing comparison record and later cross-check. Phase-C judgements are not used to define Phase-D scores.

---

# 1. Geometric curvature

Geometric curvature measures how strongly the target-relative selected neighbourhood itself changes across an adjacent transition.

For each side and transition:

### Membership disruption

```text
G_membership = 1 - membership_jaccard
```

### Edge disruption

```text
G_edge = 1 - edge_jaccard
```

### Population displacement

Use symmetric proportional change:

```text
G_population = 2 * |N_t - N_(t-1)| / (N_t + N_(t-1))
```

This avoids asymmetric percentage-change treatment of increases versus decreases.

### Geometric-curvature score

The three raw components are retained separately.

For ranking only, each component is converted to a percentile rank within the relevant side across all 32 transitions. The side-specific geometric-curvature score is the unweighted mean of those three percentile ranks.

No component receives a hand-selected weight.

---

# 2. Partition curvature

Partition curvature measures reorganisation of community assignment within the selected neighbourhood.

For each side and transition:

### Community-assignment disruption

```text
P_ARI = 1 - community_adjusted_rand
```

### Community-count displacement

```text
P_count = 2 * |K_t - K_(t-1)| / (K_t + K_(t-1))
```

where K is the measured R008 community count for that side.

### Partition-curvature score

Both raw components are retained.

For ranking only, each component is converted to a side-specific percentile rank across all 32 transitions and averaged with equal weight.

Modularity change is reported as a secondary diagnostic and is not included in the primary partition score.

---

# 3. Semantic curvature

Semantic curvature measures how strongly the inferred higher-order organisation changes across a transition.

It is intentionally distinct from geometric and partition curvature.

For each side and transition:

### Parent-count change

```text
S_parent_count = |R_t - R_(t-1)|
```

where R is the number of retained Phase-A semantic parents on that side.

### Dominant-parent coverage change

```text
S_coverage = |C_t - C_(t-1)|
```

where C is the largest retained parent's semantic-eligible coverage.

### Explicit semantic-event load

Use only explicit Phase-B transition descriptions already frozen before Phase D.

Count the presence of the following event classes on each side:

- split;
- merge / compression / recombination;
- appearance / reappearance;
- disappearance / loss of parent status / absorption;
- replacement / reconfiguration.

Multiple synonymous words for the same event class count once within a side-transition. Pure persistence, local relabelling, broadening/narrowing or emphasis change do not count as discontinuity events unless Phase B explicitly also records one of the event classes above.

The raw event count is retained.

### Semantic-curvature score

Parent-count change, dominant-parent coverage change and semantic-event load are converted independently to side-specific percentile ranks across all transitions and averaged with equal weight.

The event score is interpretive but auditable because its source is the already-frozen Phase-B transition log rather than a new Phase-D judgement.

---

# 4. State-local coherence difficulty

Coherence difficulty must be independent of transition curvature. It therefore uses only information available within one state.

The primary concept is not "how many parents exist?" Multiple high-confidence parents can represent genuine plural structure rather than failed coherence.

Instead Phase D measures how much semantic material resists confident compression.

For each side and state:

## 4.1 Mixed ambiguity load

```text
C_mixed = mixed-unresolved nodes / semantic-eligible nodes
```

## 4.2 Residual semantic load

```text
C_residual =
(mixed-unresolved nodes + irreducible-semantic nodes)
/
semantic-eligible nodes
```

This is the proportion of semantic-eligible material not absorbed into a retained higher-order parent.

## 4.3 Parent-confidence ambiguity

Each retained parent receives a fixed uncertainty penalty:

| Confidence label | Penalty |
|---|---:|
| Very High / High | 0.00 |
| High/Moderate or Moderate/High | 0.25 |
| Moderate | 0.50 |
| Moderate/Low or Low/Moderate | 0.75 |
| Low | 1.00 |

State-side confidence ambiguity is the parent-node-weighted mean penalty across retained parents.

If a side has no retained parent, confidence ambiguity is 1.00.

## 4.4 Compression fragmentation — diagnostic, not primary difficulty

Construct semantic units from:

- each retained parent as one unit;
- each mixed-unresolved community as its own unit;
- each irreducible-semantic community as its own unit.

Formal-substrate and unclear communities are excluded.

Calculate node-weighted Shannon entropy and normalise it by the maximum entropy for the observed number of semantic units.

This measures how dispersed semantic mass remains after the preferred Phase-A compression.

It is reported separately because several coherent parents can legitimately coexist.

## 4.5 Dominant-parent insufficiency — diagnostic, not primary difficulty

```text
C_dominance = 1 - largest semantic-eligible parent coverage
```

This measures failure of one parent to dominate the side, not necessarily ambiguity.

It is therefore diagnostic rather than part of the primary difficulty score.

## Primary coherence-difficulty score

The following three independent state-local components are percentile-ranked within side across all 33 states:

- mixed ambiguity load;
- residual semantic load;
- parent-confidence ambiguity.

The primary coherence-difficulty score is their unweighted mean.

Alternative-reconstruction text is used afterwards to audit high-ranking states; it is not numerically scored because every Phase-A state was required to include an alternative and the prose strength is not standardised.

---

# 5. Coherence resolution

For transition t-1→t:

```text
resolution = coherence_difficulty_(t-1) - coherence_difficulty_t
```

Positive values mean the destination state is easier to compress coherently than the source state.

Negative values mean coherence difficulty increased.

This quantity is kept separate from curvature scores.

---

# 6. Curvature-density candidate

"Curvature density" is not assumed to exist as one primitive quantity.

Only after geometric, partition and semantic curvature are ranked separately will Phase D test a candidate composite.

### Point composite

Unweighted mean of:

- geometric-curvature percentile;
- partition-curvature percentile;
- semantic-curvature percentile.

### Local density

Three-transition centred rolling mean of the point composite where a full window exists.

Endpoints use no padded values and are reported separately.

The composite is accepted as analytically useful only if inspection shows that it adds information beyond the separate dimensions. Otherwise Phase D retains the three-dimensional description and rejects a single curvature-density score.

---

# 7. Primary analyses

Phase D will answer, in order:

1. Where is geometric curvature highest?
2. Where is partition curvature highest?
3. Where is semantic curvature highest?
4. Where is state-local coherence difficulty highest?
5. Where does coherence improve most strongly?
6. Do high-curvature transitions enter difficult states, leave difficult states, or both?
7. Does semantic curvature relate to coherence differently from geometric curvature?
8. Do positive and negative sectors behave differently?
9. Do independently detected maxima overlap the previously hypothesised regions S14–S17, S21–S24 and S30–S32?

The candidate regions are not used in score construction or ranking.

---

# 8. Association tests

All associations are exploratory and descriptive because adjacent transformer states are not independent observations.

Calculate Spearman rank associations for:

### Curvature entering a state

```text
curvature(t-1→t)  vs  coherence_difficulty(t)
```

### Difficulty preceding reorganisation

```text
coherence_difficulty(t-1)  vs  curvature(t-1→t)
```

### Curvature as resolution

```text
curvature(t-1→t)  vs  resolution(t-1→t)
```

Run these separately for geometric, partition and semantic curvature and for positive and negative sectors.

No causal interpretation is assigned.

---

# 9. Underlying-community inspection

After ranking is complete, inspect the underlying Phase-A/R009 communities for:

- the highest geometric-curvature transitions;
- the highest partition-curvature transitions;
- the highest semantic-curvature transitions;
- the highest coherence-difficulty states;
- the strongest coherence-resolution transitions.

For each, record:

1. which structures compete;
2. which communities resist compression;
3. whether ambiguity is semantic, formal or mixed;
4. which structures merge, split, disappear or acquire a broader parent in the next state;
5. whether the resolution is geometric, partition-level, semantic, or some combination.

No candidate is accepted solely from aggregate scores without this content audit.

---

# 10. Adversarial checks

Phase D must test at least the following competing explanations:

1. apparent low coherence is merely a consequence of formal/tokeniser-heavy states;
2. low dominant-parent coverage reflects genuine plural structure rather than coherence failure;
3. semantic curvature is an artefact of Phase-B parent labelling;
4. ARI/community-count disruption occurs without meaningful semantic change;
5. semantic change occurs over stable geometry and therefore cannot be reduced to neighbourhood turnover;
6. endpoint normalisation effects dominate the run and obscure internal transitions;
7. positive and negative sides require different interpretations.

---

# 11. Reporting requirements

Report raw component values as well as percentile composites.

Report positive and negative sides separately before any combined score.

Report both:

- full-run rankings including S00→S01 and S31→S32;
- internal-transition rankings excluding those two endpoints.

Do not label a state "incoherent". The quantity is **coherence difficulty**: difficulty compressing the observed semantic communities into a confident higher-order organisation.

Do not treat "curvature" as literal differential-geometric curvature unless a later analysis defines and measures such a quantity directly. In Phase D it is a descriptive name for abrupt structural change across transformer depth.

## Frozen boundary

The metric definitions above must not be changed after Phase-D results are inspected merely to improve alignment with previously suspected regions.

If a metric proves defective, record the defect and create a separately versioned sensitivity analysis rather than silently modifying the primary protocol.
