# R010 Phase C — semantic trajectory versus measured topology

## Status

**PHASE C COMPARISON: COMPLETE**

Phase C compares the frozen R010 Phase-B semantic trajectory with the pre-existing R008 measured topology.

It does not rerun Pythia, alter R004 cut-offs, modify R008 communities, or revise the Phase-A state reconstructions.

It also does not assign SDA-3 roles, identify an optimal transformer layer, or infer curvature/coherence.

## Evidence

Semantic evidence:

- `R010_PHASE_B_STRUCTURAL_EVOLUTION.md`
- `R010_LAYERWISE_COMMUNITY_PARENT_MAP.md`
- frozen Phase-A state reconstructions

Measured evidence:

- R008 `state_transitions.csv`
- R008 `network_index.csv`
- R008 `findings.md`
- R008 `COMMUNITY_COUNTS_BY_STATE.md`

R008 measures state-local static-embedding neighbourhoods selected by the moving target representation. The vocabulary geometry itself is fixed. Therefore measured layer-wise change means **change in target-relative membership and relations among selected vocabulary tokens**, not contextual movement of every vocabulary token.

## R008 baseline

Across all adjacent-state transitions:

### Positive head

- median membership Jaccard: **0.7537**
- median edge Jaccard: **0.5344**
- median community ARI: **0.3749**

### Negative tail

- median membership Jaccard: **0.7582**
- median edge Jaccard: **0.5371**
- median community ARI: **0.3986**

Interpretation:

- lower membership Jaccard = greater token-population turnover;
- lower edge Jaccard = greater change in within-side neighbourhood relations;
- lower ARI = greater reorganisation of community assignment;
- population and community-count changes provide additional structural evidence.

## Executive result

**Semantic evolution and measured topology correspond, but only partially.**

Three distinct change modes occur:

```text
1. GLOBAL TOPOLOGICAL RESET
   membership changes
   + edges change
   + communities reorganise
   + semantic architecture changes

2. COMMUNITY RE-PARTITIONING
   membership largely persists
   + edges largely persist
   + community organisation changes
   + semantic parent architecture changes

3. SEMANTIC ABSTRACTION WITH GEOMETRIC STABILITY
   membership largely persists
   + edges largely persist
   + communities may remain similar
   + inferred higher-order semantic organisation changes anyway
```

The main consequence is that **R010 semantic parent evolution cannot be reduced to R008 token turnover or community turnover**.

Some of the strongest Phase-B semantic transitions are topologically dramatic. Others occur inside a highly stable measured network.

## Endpoint transitions

### S00 → S01 — strongest agreement

Phase B identified S00→S01 as the largest conceptual replacement.

Measured evidence strongly confirms this.

Averaged across positive and negative sides:

- membership Jaccard: **0.029**
- edge Jaccard: **0.002**
- mean ARI: **0.255**
- maximum side-specific population change: **112.2%**

Ranks among all 32 transitions:

- membership disruption: **1st**
- edge disruption: **1st**
- ARI disruption: **1st**

Positive population rises from 1,871 to 3,125; negative population rises from 1,316 to 2,793.

This is not merely semantic relabelling. The input-embedding neighbourhood is almost completely replaced by the first contextual transformer state.

**Phase-C judgement: very strong semantic/topological agreement.**

### S31 → S32 — second strongest agreement

Phase B identified S31→S32 as a terminal merge/reconfiguration into an explicit information-processing → state-change → reporting workflow.

Measured topology again confirms a genuine reset.

Averaged across sides:

- membership Jaccard: **0.210**
- edge Jaccard: **0.059**
- mean ARI: **0.322**
- maximum population change: **14.7%**

Ranks:

- membership disruption: **2nd**
- edge disruption: **2nd**
- ARI disruption: **2nd** by averaged transition rank

Side-specific values:

- positive membership Jaccard: **0.204**
- negative membership Jaccard: **0.216**
- positive edge Jaccard: **0.055**
- negative edge Jaccard: **0.062**

Positive modularity also rises sharply from **0.5087 to 0.5558**, while negative modularity falls from **0.5175 to 0.4961**.

State 32 combines raw block-31 transformation with final normalisation, so the source of the discontinuity cannot be decomposed further from this capture.

**Phase-C judgement: very strong semantic/topological agreement.**

## Comparison of Phase-B semantic discontinuities

| Transition | Phase-B semantic event | Avg membership Jaccard | Avg edge Jaccard | Avg ARI | Additional measured evidence | Phase-C judgement |
|---|---|---:|---:|---:|---|---|
| **S00→S01** | domain ontology replaced by contextual information/social/living organisation | 0.029 | 0.002 | 0.255 | population +67% positive, +112% negative | **Very strong agreement** |
| **S08→S09** | positive compression; biological parent loses independent status | 0.667 | 0.427 | 0.362 | both membership and edge similarity below run medians | **Strong/partial agreement** |
| **S14→S15** | major positive compression from two parents to one | 0.757 | 0.534 | 0.396 | positive measured community count drops **13→9** | **Partial agreement: partition-count compression, not wholesale turnover** |
| **S16→S17** | health parent absorbed into broad developmental/process architecture | 0.805 | 0.598 | 0.357 | community counts change +2 positive, −2 negative | **Community re-partitioning within relatively stable membership** |
| **S21→S22** | two positive parents merge into broad analytical inquiry/research-enterprise structure | 0.897 | 0.767 | 0.428 | among the most stable membership/edge transitions in the run | **Strong semantic/topological divergence** |
| **S22→S23** | health/wellbeing parent reappears | 0.871 | 0.706 | 0.363 | positive population +17%; positive ARI **0.327** | **Side-specific re-partitioning; partial agreement** |
| **S23→S24** | health dissolves; mediated professional branch reappears | 0.822 | 0.609 | 0.351 | negative population −20%; negative ARI **0.339** | **Moderate agreement, concentrated on negative topology/population** |
| **S26→S27** | applied inquiry + mediated information production merge into 72.1% positive parent | 0.869 | 0.710 | 0.368 | positive community count 12→10; otherwise high membership/edge stability | **Semantic integration inside stable geometry** |
| **S30→S31** | broad positive activity splits into analytical/evidential and professional-information parents | 0.808 | 0.608 | 0.464 | positive population −12.2%; community counts nearly unchanged | **Semantic re-differentiation with unusually stable community assignment** |
| **S31→S32** | terminal functional workflow reorganisation | 0.210 | 0.059 | 0.322 | large edge replacement and positive modularity increase | **Very strong agreement** |

## What each disagreement means

### S21 → S22 — strongest semantic change with almost no measured turnover

Measured values are exceptionally stable:

- positive membership Jaccard **0.894**
- negative membership Jaccard **0.900**
- positive edge Jaccard **0.761**
- negative edge Jaccard **0.773**
- negative ARI **0.469**

Yet Phase B reconstructs a positive semantic merge into one broad analytical inquiry/applied research-enterprise parent.

This means the semantic change is not primarily caused by replacement of vocabulary tokens or their nearest-neighbour edges. The same measured neighbourhood can support a different higher-order interpretation because relationships among already-present communities become compressible under a broader parent.

**Interpretation: abstraction/compression without geometric reset.**

### S26 → S27 — strongest late integration under stable topology

Phase B identifies S26→S27 as a major late merge. The dominant positive parent reaches **72.1%** semantic-eligible coverage.

Measured values remain highly stable:

- positive membership Jaccard **0.866**
- positive edge Jaccard **0.709**
- negative membership Jaccard **0.872**
- negative edge Jaccard **0.711**

Positive community count falls only from 12 to 10.

The inference is therefore not "the network changed completely". It is that **existing semantic components became interpretable as one larger relational system**.

**Interpretation: semantic integration over a stable substrate.**

### S30 → S31 — semantic split without community split

Phase B identifies a late re-differentiation into:

- analytical/evidential interpretation;
- mediated professional/information-production activity.

But measured community assignment is unusually stable:

- positive ARI **0.467**
- negative ARI **0.461**

These are among the highest ARIs in the transition series.

Positive population does contract by **12.2%**, and edge Jaccard falls to **0.588**, so some geometric change occurs, but the semantic split is much stronger than the community-partition change.

**Interpretation: semantic role differentiation among largely persistent measured communities.**

## Measured discontinuities not initially ranked as major Phase-B discontinuities

Phase C also identifies transitions where R008 topology changes strongly even though Phase B did not place them in its highest-discontinuity list.

### S01 → S02

Averaged measured values:

- membership Jaccard approximately **0.617**
- edge Jaccard approximately **0.371**

This is the strongest internal transition after excluding S00→S01 and S31→S32 by membership/edge turnover.

Phase B describes this as differentiation of early contextual structure: operational information broadens/splits into action-appraisal and computational/scientific functions while social and biological structures persist.

**Interpretation: strong geometric contextualisation within a semantically recognisable early architecture.**

### S09 → S10

Averaged values:

- membership Jaccard **0.660**
- edge Jaccard **0.418**
- ARI **0.344**

This transition is among the strongest internal measured changes.

Crucially, Phase B also says that on the negative side the previously separated assessment and adverse/change strands **merge into the T-C control backbone**.

Therefore S09→S10 should be elevated as a strong **measured support point for consolidation of the negative control architecture**, even though it was not in the original shortlist of largest semantic discontinuities.

### S10 → S11

Averaged values:

- membership Jaccard **0.649**
- edge Jaccard **0.412**
- ARI **0.348**

Phase B describes:

- positive operational activity becoming investigation/evaluation/information production;
- negative T-C strengthening into quantitative characterisation + adverse/destructive constraint.

This is another transition where measured turnover and semantic abstraction coincide.

### S12 → S14 region

S12→S13 and S13→S14 both show relatively low membership/edge similarity compared with later layers, while Phase B preserves the same broad inquiry, biological, control and authority families with local narrowing/broadening.

This is the inverse of S21→S22:

- **geometry changes materially;**
- **macro-semantic families remain recognisable.**

**Interpretation: token/community churn under higher-order semantic continuity.**

### S15 → S16

Positive ARI falls to **0.296**, the second-lowest positive ARI in the entire transition series after S00→S01.

Phase B independently identifies the reappearance of a distinct health/biomedical parent at S16.

This is strong evidence for **community re-partitioning associated with semantic re-differentiation**, even though membership and edge Jaccards are only moderately changed.

## Trajectory-level comparison

### Early contextual layers: semantic differentiation accompanies high measured turnover

S01–S14 contains most of the strongest internal membership/edge disruptions.

During the same period Phase B reconstructs multiple coexisting positive parents:

- operational information;
- social/institutional organisation;
- biological/living systems;
- later inquiry/analysis.

The early transformer therefore appears to be dynamically **selecting and reallocating semantic neighbourhoods** while establishing the macro-families that later become more stable.

### Middle and late layers: measured topology stabilises faster than semantic abstraction

From roughly S17 onward, membership and edge Jaccards generally rise substantially.

Examples:

- S18→S19 positive membership **0.871**
- S20→S21 positive membership **0.870**
- S21→S22 positive membership **0.894**
- S25→S26 positive membership **0.858**
- S26→S27 positive membership **0.866**

Yet Phase B continues to identify:

- splits;
- merges;
- reappearances of health/professional branches;
- broadening/narrowing of the dominant positive parent.

Therefore later semantic evolution increasingly happens **within an already stabilised token neighbourhood**.

### Negative architecture: semantic and measured evolution correspond more closely

Phase B found that the negative side converges earlier on:

1. T-C — control/characterisation/adverse change;
2. T-A — authority/territorial/social order.

A coarse exploratory rank-correlation check supports the same asymmetry.

Excluding the special endpoint transitions S00→S01 and S31→S32, Spearman associations between state-to-state changes in R010 summary structure and R008 disruption are:

#### Positive side

Absolute change in retained-parent count versus:

- membership disruption: **ρ = −0.243**
- edge disruption: **ρ = −0.250**
- ARI disruption: **ρ = 0.096**

Absolute change in dominant semantic-parent coverage versus:

- membership disruption: **ρ = −0.212**
- edge disruption: **ρ = −0.194**
- ARI disruption: **ρ = 0.367**

#### Negative side

Absolute change in retained-parent count versus:

- membership disruption: **ρ = 0.478**
- edge disruption: **ρ = 0.496**
- ARI disruption: **ρ = 0.232**

Absolute change in dominant semantic-parent coverage versus:

- membership disruption: **ρ = 0.488**
- edge disruption: **ρ = 0.479**
- ARI disruption: **ρ = 0.346**

These are exploratory descriptive correlations over only 30 internal transitions. No significance test or causal interpretation is assigned.

The useful result is directional: **coarse negative-side semantic restructuring tracks measured membership/edge disruption more closely than positive-side restructuring does**.

That matches Phase B's qualitative finding that the positive side becomes increasingly abstract and can reorganise semantically over a stable measured substrate.

## Intercommunity organisation and modularity

R008 modularity remains within a comparatively narrow range through most contextual states:

- positive overall range: approximately **0.499–0.589**
- negative overall range: approximately **0.469–0.542**

Many large R010 semantic merges therefore do not require a large modularity change.

The most conspicuous terminal exception is S31→S32:

- positive modularity **0.5087 → 0.5558**
- negative modularity **0.5175 → 0.4961**

The two signs therefore respond differently to final normalisation:

- positive network becomes more modular;
- negative network becomes less modular;

while both experience massive membership and edge replacement.

This is consistent with State 32 being a qualitatively reorganised endpoint rather than merely another incremental block-output state.

## Phase-C answers to the protocol questions

### 1. Do large inferred semantic changes coincide with large measured R008 changes?

**Sometimes, but not generally.**

Strong agreements:

- S00→S01;
- S08→S09;
- S09→S10, when considering measured evidence as a refinement of the Phase-B shortlist;
- S15→S16 for community re-partitioning;
- S31→S32.

Partial agreements:

- S14→S15;
- S16→S17;
- S22→S23;
- S23→S24;
- S30→S31.

Strong divergences:

- S21→S22;
- S26→S27.

### 2. Do semantic and measured discontinuities agree at input→block0 and block30→final-normalisation?

**Yes, very strongly.**

They are the first- and second-most disruptive transitions by membership and edge Jaccard on both signs.

This independently validates the Phase-B judgement that both endpoints are qualitatively distinct semantic transitions.

### 3. Where do semantic interpretation and measured topology disagree?

Two disagreement classes occur.

#### A. Large semantic change with stable measured topology

Examples:

- S21→S22;
- S26→S27;
- S30→S31.

This indicates higher-order semantic compression, integration or role differentiation without wholesale neighbourhood replacement.

#### B. Large measured change with persistent macro-semantic families

Examples:

- S01→S02;
- S12→S13;
- S13→S14.

This indicates vocabulary/community turnover underneath a stable higher-order semantic organisation.

## Revised hierarchy of important transitions

Phase C changes the interpretation of importance.

### Tier 1 — semantic and topological resets

1. **S00→S01**
2. **S31→S32**

These are genuine whole-neighbourhood discontinuities.

### Tier 2 — measured topology + meaningful semantic reorganisation

3. **S09→S10** — negative control strands merge into T-C
4. **S10→S11** — T-C strengthens; positive inquiry abstraction advances
5. **S08→S09** — positive architecture compresses; biological parent loses autonomy
6. **S15→S16** — health parent reappears with strong positive community re-partitioning
7. **S23→S24** — substantial negative population/community reorganisation

### Tier 3 — semantic abstraction over stable topology

8. **S21→S22** — positive semantic merge under extreme measured stability
9. **S26→S27** — late positive integration to 72.1% coverage under stable membership/edges
10. **S30→S31** — semantic split with high community-assignment stability

This distinction is more informative than ranking all change on one axis.

## Generative interpretation

The combined R008/R010 evidence supports a two-stage view of transformer development:

```text
EARLY / MID TRANSFORMER

target-relative neighbourhood is still moving substantially
        +
communities repeatedly repartition
        +
semantic macro-families are being established
        ↓
GEOMETRIC SEARCH / CONTEXTUAL SELECTION


LATE TRANSFORMER

target-relative neighbourhood becomes comparatively stable
        +
higher-order parent relations continue to merge/split/reframe
        ↓
SEMANTIC COMPRESSION / RELATIONAL REORGANISATION


FINAL NORMALISATION

neighbourhood itself resets sharply
        +
semantic architecture becomes explicit functional workflow
        ↓
TERMINAL REPRESENTATIONAL REORGANISATION
```

"Geometric search" and "semantic compression" are descriptive labels for the observed pattern, not claims about a known internal causal algorithm.

## Strongest Phase-C conclusions

1. **R010 semantic evolution is real but not reducible to R008 topology change.**
2. **S00→S01 and S31→S32 are independently supported as genuine semantic and measured network resets.**
3. **Early transformer development contains substantially more membership/edge turnover than late development.**
4. **Late positive semantic integration often occurs over highly stable measured neighbourhoods.**
5. **Negative semantic restructuring tracks measured topology more closely than positive restructuring does.**
6. **Community ARI can reveal semantic re-differentiation when membership and edge Jaccards remain high, as at S15→S16 and S16→S17.**
7. **The formation of the persistent negative T-C control backbone around S09→S11 is supported by unusually strong measured topology change.**
8. **The final State 32 workflow is not merely an interpretive relabelling of State 31; it coincides with the second-largest measured neighbourhood reset in the capture.**

## Limitations

- R008 uses a fixed static vocabulary embedding geometry; only target-relative selection changes across states.
- R010 parents are inferred analytical structures, not measured graph nodes.
- The exploratory rank correlations use coarse R010 summaries and only 30 internal transitions after excluding the two endpoint transitions.
- No significance testing is used.
- Raw block 31 is unavailable, so S31→S32 conflates block 31 with final layer normalisation.
- Similarity between semantic parent labels is not proof of a persistent transformer feature.
- Agreement between R008 and R010 does not establish causation.

## Phase-C boundary

Phase C completes the planned R010 sequence:

```text
Phase A
independent state reconstruction
        ↓
Phase B
semantic structural trajectory
        ↓
Phase C
comparison with measured topology
```

The next analyses, if authorised separately, may ask whether the combined evidence supports:

- SDA-3 structural roles;
- layer usefulness or an optimal layer/range;
- coherence or curvature hypotheses.

Those claims are **not** made here.

No SDA-3 role, optimal-layer judgement or curvature/coherence inference is made in this artifact.
