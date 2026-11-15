# R014 ↔ R015 comparison

## Comparison boundary

R015 was reconstructed independently before this alignment. The purpose of this
document is to determine whether the R014 semantic map persists, deforms,
splits, merges or terminates after every R014 seed is replaced by a measured
neighbour:

```text
laser         -> sensor
city          -> apartment
spatial field -> line
clubs         -> sessions
```

The comparison is parent- and relation-level. Token-level invariance is neither
expected nor required.

Support values in both runs are downstream semantic diagnostics rather than raw
model measurements. R015's published audit uses representative/extreme
community vocabulary and observed community edges, so absolute support
differences should be interpreted conservatively. Relative structure and
recurrence are the primary evidence.

## Parent alignment

| R014 parent | Independently reconstructed R015 family | Result |
|---|---|---|
| technical / sensing | sensing / instrumentation | strong continuity |
| place / environment | built place / locality | strong continuity |
| spatial / structural | spatial / measurement structure | continuity with sector deformation |
| social / group activity | organised group / activity | strong continuity |
| interaction / change | process / comparison / modification | continuity with substantial cross-sector expansion |
| representation / information | reporting / information | strong continuity |

All six R014 parent families therefore have independently reconstructed R015
counterparts. The two families that were not supplied as R015 seeds also recur:
process/change and reporting/information.

This is stronger evidence than simple seed preservation because none of the
four original R014 prompt concepts is required for the corresponding R015
family to reappear.

## Topological alignment

### Positive cluster

R014's strongest positive relation was:

```text
technical / sensing <-> place / environment
```

R015 independently reconstructs:

```text
sensing / instrumentation <-> built place / locality
```

with 4/4 probe support and approximately .94 mean S06-S27 community-summary
support. This remains the dominant positive pair.

The positive relations from sensing/place into spatial structure also persist,
but are weaker in the R015 audit:

| Relation | R014 | R015 | Interpretation |
|---|---:|---:|---|
| sensing/technical ↔ place/locality | .82 | .94 | persistent dominant positive relation |
| sensing/technical ↔ spatial | .54 | .31 | persists but contracts |
| place/locality ↔ spatial | .45 | .30 | persists but contracts |
| sensing/technical ↔ information | .37 | .59 | persists and is more explicit in R015 summaries |

Because the audit procedures are downstream semantic diagnostics, these values
should not be treated as exact effect-size deltas. The defensible statement is
that the same positive backbone survives while spatial coupling is less
prominent in R015.

### Negative chain

R014 recovered:

```text
spatial / structural
        |
        v
social / group activity
        |
        v
interaction / change
```

R015 independently recovers:

```text
spatial / measurement
        |
        v
organised group / activity
        |
        v
process / comparison / change
```

The relation audit is:

| Relation | R014 | R015 | Interpretation |
|---|---:|---:|---|
| spatial ↔ group/activity | .81 | .68 | persistent, somewhat weaker |
| group/activity ↔ process/change | .50 | .70 | persistent, stronger in R015 summaries |
| spatial ↔ process/change | .40 | .51 | persistent |

The negative-chain organisation therefore survives the movement into the
adjacent semantic neighbourhood.

## Main deformation: process/change becomes cross-sector

The most important difference is not disappearance of a parent. It is a change
in how one parent participates in the topology.

R014 described interaction/change as negative-dominant and found only a weak
direct technical ↔ interaction relation.

R015 independently produces two recurrent expressions of the same broader
family:

- negative: manipulation, process/processes, experimentation, extraction,
  creating, comparing, change and interactions;
- positive: enlargement, decreasing, transformations and removal.

The R015 positive audit consequently finds:

```text
sensing / instrumentation <-> process / modification   ~.70
built place / locality     <-> process / modification   ~.67
process / modification     <-> reporting / information  ~.44
```

This is the clearest local deformation. The process/change family persists but
is no longer adequately described as only a negative-side appendage to the
group/activity branch.

## Spatial-family deformation

R014's spatial/structural parent was explicitly a both-sector bridge. R015's
spatial/measurement family still spans both sectors but is more
negative-dominant in the published community summaries.

Across S06-S27, the strong-indicator audit finds spatial-family evidence in
roughly 61-83% of negative networks by probe but only 27-33% of positive
networks.

The bridge therefore persists semantically, but its positive-side expression
contracts in the neighbouring-token window.

## Held-out graph completion

R014 established strong held-out reconstruction for its four seed regions.
R015 repeats the family-level phenomenon but with more uneven literal recovery.

| Run/probe | Held-out concept | Literal result | Family-level result |
|---|---|---|---|
| R015 P1 | sessions | 6/6 orders, 18 states | 6/6, all 28 states |
| R015 P2 | line | 4/6 orders, 2 states in summaries | 6/6, 26 states |
| R015 P3 | apartment | 4/6 orders, 12 states | 6/6, all 28 states |
| R015 P4 | sensor | 6/6 orders, 21 states | 6/6, all 28 states |

The strongest conclusion is therefore not that every neighbouring lexeme is
reconstructed literally. It is that the broader semantic region associated
with every held-out neighbour is reconstructed from the remaining three
concepts across all six orders.

This distinguishes parent-level topology from literal token recurrence.

## What survives across R014 and R015

The following structure survives replacement of every original seed:

```text
                 POSITIVE
                    |
       sensing/instrumentation
          /        |        \
         /         |         \
   locality     spatial     information
      |            |
      |        [cross-sector family]
      |            |
      +------ process/modification
                   |
                 NEGATIVE
                   |
       spatial/measurement
             |
       group/activity
             |
        process/change
```

This diagram intentionally shows the R015 deformation: process/modification has
a positive expression in addition to the preserved negative chain.

## Strongest supported claim

R015 supports the claim that R014 did not merely decompose the literal concepts
`laser`, `city`, `spatial field` and `clubs`.

After all four seeds were replaced by neighbouring concepts, R015 independently
reconstructed counterparts of all six R014 parent families, preserved the
dominant positive sensing-place relation, preserved the negative
spatial-group-process chain, and reconstructed every held-out semantic family
across all six local orders.

The topology is therefore locally continuous but not rigid. It deforms,
especially in the sector participation and connectivity of the process/change
family and in the strength of the spatial family's positive-side expression.

## What this does not establish

R015 does not establish:

- that this topology is global across the model;
- that the six families are universal transformer primitives;
- that the reconstructed parents are causal internal variables;
- that SDA-3 categories have been recovered;
- that numeric support values are directly comparable as effect sizes between
  R014 and R015; or
- that a distant semantic region will show the same organisation.

## Next experiment

The local-continuity question has now produced a positive but non-trivial
answer. The next clean experimental move is a distant-region replication using
the same measurement and independent-reconstruction procedure.

That experiment should test whether the recurrent *kind* of organisation
survives outside this neighbourhood. SDA-3 comparison should remain downstream
of that test so that SDA-3 has a larger independently generated topology
against which it can genuinely succeed or fail.
