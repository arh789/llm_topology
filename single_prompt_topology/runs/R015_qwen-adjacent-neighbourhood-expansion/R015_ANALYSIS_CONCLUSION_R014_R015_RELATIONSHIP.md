**R015 is a controlled continuation of R014.** R014 established a candidate local semantic topology; R015 tested whether that topology survives when the observation window moves to neighbouring concepts.

The relationship is fundamentally one of **discovery → independent replication → continuity testing**.

## 1. Experimental relationship

<box border radius="lg" padding={3} gap={2}>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    <text color="secondary" weight="medium" size="xs">R014 — Initial topology</text>
    **Discover higher-order semantic structure**

    Seeds: `laser`, `city`, `spatial field`, `clubs`
  </box>
  <row justify="center" align="center" gap={2}>
    <icon name="arrow-down" color="secondary" size="lg"/>
    <text color="secondary" size="xs">Move the observation window</text>
  </row>
  <box background="surface-secondary" radius="md" padding={3} gap={1}>
    <text color="secondary" weight="medium" size="xs">R015 — Adjacent-neighbourhood replication</text>
    **Reconstruct the topology independently**

    Seeds: `sensor`, `apartment`, `line`, `sessions`
  </box>
  <row justify="center">
    <icon name="arrow-down" color="secondary" size="lg"/>
  </row>
  <box border radius="md" padding={3} gap={1} align="center">
    **Compare the resulting semantic maps**

    <text color="secondary" size="sm" textAlign="center">Which parent structures and relationships survive, disappear or change?</text>
  </box>
</box>

The substitutions were:

| R014 | R015 |
|---|---|
| laser | sensor |
| city | apartment |
| spatial field | line |
| clubs | sessions |

The experimental methodology was preserved, making the shift in semantic context the principal intended difference.

R015 therefore addresses an alternative explanation for R014's findings: perhaps the apparent higher-order structures were merely consequences of the four original prompt concepts.

If those structures reappear after every concept is replaced, that narrow explanation becomes less convincing.

## 2. What R015 preserved from R014

All six higher-order parent families identified in R014 had independently reconstructed counterparts in R015.

| R014 parent | R015 parent | Finding |
|---|---|---|
| Technical / sensing | Sensing / instrumentation | Strong continuity |
| Place / environment | Built place / locality | Strong continuity |
| Spatial / structural | Spatial / measurement | Continuity with deformation |
| Social / group activity | Organised group / activity | Strong continuity |
| Interaction / change | Process / comparison / modification | Continuity with expansion |
| Representation / information | Reporting / information | Strong continuity |

Crucially, **process/change and reporting/information reappeared despite neither being supplied directly as an R015 seed**.

The two dominant relational structures also survived:

<box border radius="lg" padding={3} gap={2}>
  <text weight="medium" color="secondary" size="xs">PERSISTENT POSITIVE RELATION</text>
  <row align="center" justify="center" gap={2}>
    <box background="rgba(38,132,91,0.09)" radius="md" padding={3} flex={1} align="center">
      <text weight="medium" textAlign="center">Sensing</text>
    </box>
    <icon name="arrow-left-right" color="success" size="lg"/>
    <box background="rgba(38,132,91,0.09)" radius="md" padding={3} flex={1} align="center">
      <text weight="medium" textAlign="center">Place</text>
    </box>
  </row>
  <text color="secondary" size="xs" textAlign="center">Present in both runs; remains the dominant positive pair</text>
  <divider spacing={2}/>
  <text weight="medium" color="secondary" size="xs">PERSISTENT NEGATIVE-SECTOR CHAIN</text>
  <col align="center" gap={1}>
    <box background="surface-secondary" padding={2} radius="md" width="70%" align="center">Spatial structure</box>
    <icon name="arrow-down" color="secondary"/>
    <box background="surface-secondary" padding={2} radius="md" width="70%" align="center">Group / activity</box>
    <icon name="arrow-down" color="secondary"/>
    <box background="surface-secondary" padding={2} radius="md" width="70%" align="center">Process / change</box>
  </col>
  <text color="secondary" size="xs" textAlign="center">The same relational organisation recurs in R015</text>
</box>

The positive and negative designations here refer to the experiment's signed semantic sectors, not favourable and unfavourable meanings.

## 3. What changed between R014 and R015

The topology did not simply repeat identically.

<text weight="medium">Reported relation-support diagnostics</text>

| Relationship | R014 | R015 |
|---|---:|---:|
| Sensing ↔ place | 0.82 | 0.94 |
| Sensing ↔ spatial | 0.54 | 0.31 |
| Spatial ↔ group | 0.81 | 0.68 |
| Group ↔ process | 0.50 | 0.70 |

These are downstream community-summary diagnostics, not raw transformer measurements. Their numerical differences should not be interpreted as precise effect sizes.

The most consequential change was the **process/change family**. In R014 it was predominantly associated with the negative sector. In R015, it developed substantial positive-sector relationships with sensing, place and information.

Meanwhile, the spatial family remained a bridge between sectors, but became more negative-dominant.

This means R015 found both *structural invariance* and *local deformation*.

## 4. What the relationship establishes

The important distinction is between three claims:

| Claim | Assessment |
|---|---|
| The same literal concepts recur | Not required; literal held-out recovery varied |
| Higher-order parent structures recur | Supported across all six families |
| The relationships between those structures recur | Supported, with measurable deformation |

R015 recovered every held-out concept's broader semantic family in all six prompt orders for each probe, even when exact lexical recovery was weak.

This is more informative than simply discovering similar token clusters.

However, the two experiments are not fully independent tests of a universal topology: the R015 concepts were deliberately chosen as semantic neighbours of R014. Similar meanings, shared measurement procedures and the semantic reconstruction method could contribute to the recurrence.

Consequently, the strongest defensible conclusion is:

**R014 identified a candidate semantic topology. R015 demonstrated that the candidate topology is locally continuous under controlled semantic displacement, rather than depending exclusively on R014's original four literal seeds.**

It does not yet establish that these six structures are universal properties of the transformer, or that they correspond directly to causal internal representations.

## 5. Implication for the project

The combined result changes the experimental question:

- **Before R015:** Does a stable semantic structure exist beyond individual prompt permutations?
- **After R015:** How far can the observation window move before the reconstructed structure deforms, fragments or disappears?

The next logical experiment is a genuinely distant semantic region, measured and reconstructed independently using the same procedure.

R014 and R015 together establish a candidate *local topology*. A distant-region replication would begin determining whether the project is observing a more general organising principle or a structure specific to this particular semantic neighbourhood.

The detailed evidence is recorded in the <Link url="https://github.com/arh789/chatgpt-analysis/blob/main/projects/llm-topology/single_prompt_topology/runs/R015_qwen-adjacent-neighbourhood-expansion/R014_R015_COMPARISON.md" title="R014–R015 comparison record"/>.