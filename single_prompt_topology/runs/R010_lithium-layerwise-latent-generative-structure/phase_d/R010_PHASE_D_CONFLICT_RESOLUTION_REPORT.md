# R010 Phase D — conflict-resolution report

## Status

**CONFLICT-RESOLUTION ANALYSIS COMPLETE FOR THE CURRENT R010 CAPTURE**

Primary question:

> **How does the transformer handle conflicting information while constructing the representation used for next-token prediction?**

## Executive answer

The strongest evidence does **not** support a simple model in which conflicting information is resolved by immediately suppressing one alternative.

Instead, the trajectory repeatedly follows:

~~~text
PRESERVE COMPETING INFORMATION
        ↓
ATTEMPT A STRUCTURAL ORGANISATION
        ↓
IF NECESSARY, PASS THROUGH A HIGH-DIFFICULTY STATE
        ↓
RE-PARTITION / RE-DIFFERENTIATE
        ↓
SELECT, ABSORB OR ASSIGN DIFFERENT ROLES
        ↓
INTEGRATE COMPATIBLE FUNCTIONS
        ↓
LEAVE NON-ESSENTIAL MATERIAL OUTSIDE THE CORE
~~~

The key principle is:

> **Conflict is often resolved by changing the relationship between surviving structures rather than deleting one of them.**

## 1. Negative-side conflict resolves earlier into a control architecture

Negative coherence difficulty:

~~~text
S07  0.844
S08  0.865
S09  0.792
S10  0.885   ← maximum negative difficulty
S11  0.219
~~~

During the same region, Phase B reconstructs initially separated strands:

- scientific/clinical characterisation;
- evaluation;
- prohibition/regulation;
- adverse or destructive change.

S09→S10 has high negative geometric curvature (**0.710**) and extremely high negative partition curvature (**0.863**).

Yet S10 is more difficult, not less.

Then S10→S11 again has strong negative partition curvature (**0.847**) and negative difficulty collapses from **0.885 to 0.219**.

The resulting T-C architecture integrates:

~~~text
CHARACTERISE
      ↓
EVALUATE
      ↓
CONSTRAIN / REGULATE
      ↓
CONTROL / CHANGE
~~~

The first reorganisation therefore does not immediately solve the conflict. It produces an intermediate high-conflict state; the next layer stabilises the competing functions as complementary parts of one control relation.

**Resolution mechanism: integration after a transient high-conflict state.**

## 2. Compression can make conflict worse

Positive difficulty:

~~~text
S14  0.365
S15  0.667
S16  0.495
~~~

At S14 the positive side retains separate inquiry/professional and biomedical/physical structures.

S14→S15 compresses this into one inquiry/analytical parent, but S15 leaves approximately **44.7%** of semantic-eligible positive material mixed-unresolved.

S15→S16 then produces the largest positive partition curvature in the run (**0.919**). A separate health/biomedical parent reappears and positive coherence difficulty falls from **0.667 to 0.495**.

**Resolution mechanism: re-differentiation after over-compression.**

## 3. S21→S23 is the cleanest abstraction-conflict episode

At S21→S22:

- positive geometric curvature = **0.054**;
- positive semantic curvature = **0.731**;
- positive difficulty rises from **0.401 to 0.745**.

Phase B changes from:

~~~text
development / measurement
+
mediated professional/interface activity
~~~

to one broad:

~~~text
analytical inquiry / research-enterprise
~~~

without substantial neighbourhood replacement.

Then S22→S23:

- positive partition curvature = **0.831**;
- positive semantic curvature = **0.796**;
- health/wellbeing reappears as a separate parent;
- positive difficulty falls from **0.745 to 0.432**.

This sequence is:

~~~text
same underlying semantic material
        ↓
broader abstraction attempted
        ↓
coherence becomes harder
        ↓
community repartition
        ↓
health/wellbeing separated again
        ↓
coherence improves
~~~

**Resolution mechanism: abstraction attempt → conflict → re-partitioning.**

## 4. Integration can resolve the core without resolving all residual conflict

S26→S27 is the strongest positive semantic-curvature transition:

- positive semantic curvature = **0.898**;
- positive geometric curvature = **0.204**.

The architecture changes from:

~~~text
applied inquiry / measurement / development
+
digital interface / information production
~~~

to one parent covering **72.1%** of semantic-eligible positive material:

~~~text
analytical + communicative + professional information activity
~~~

Yet positive coherence difficulty changes only modestly:

~~~text
S26  0.719
S27  0.672
~~~

At S27 roughly **27.9%** of semantic-eligible positive material remains mixed-unresolved.

Then S27→S28 produces a much larger improvement:

~~~text
0.672 → 0.302
~~~

while the health/wellbeing branch reappears.

**Resolution mechanism: core integration followed by peripheral role separation.**

## 5. The terminal state does not minimise conflict

Late positive difficulty:

~~~text
S29  0.594
S30  0.594
S31  0.547
S32  0.604
~~~

At S30→S31 the broad positive structure splits into:

- analytical/evidential interpretation;
- professional/information-production activity.

Positive semantic curvature is high (**0.720**) while positive partition curvature is extremely low (**0.065**).

At S31→S32 the neighbourhood undergoes a massive reset:

- positive geometric curvature = **0.946**.

The final representation becomes:

~~~text
DATA / TESTING / MEASUREMENT
        ↓
ACQUISITION / TRANSFER / STATE CHANGE
        ↓
REPORTING / RECORDING / PUBLISHING
~~~

But positive coherence difficulty increases slightly, from **0.547 to 0.604**.

The final workflow parent covers **51.3%** of semantic-eligible positive material.

The final state is therefore not the state of maximum global semantic coherence. It appears to construct a sufficiently coherent **functional pathway** while leaving non-essential semantic material outside that pathway.

**Resolution mechanism: functional-core extraction and sequencing.**

## 6. Conflict predicts re-partitioning better than curvature predicts resolution

Across internal transitions, combined source coherence difficulty correlates with the next transition's:

- geometric curvature: **ρ = 0.243**
- partition curvature: **ρ = 0.502**
- semantic curvature: **ρ = 0.233**

The strongest relationship is:

> **Hard-to-compress states tend to be followed by community repartitioning.**

By contrast, curvature → immediate coherence resolution is weak:

- geometric: **ρ = 0.005**
- partition: **ρ = 0.287**
- semantic: **ρ = −0.137**

Structural change is therefore not automatically corrective. Some reorganisations create a new conflict that must be resolved later.

## 7. Positive and negative conflict follow different trajectories

### Negative side

Internal source difficulty versus following curvature:

- geometric: **ρ = 0.353**
- partition: **ρ = 0.369**
- semantic: **ρ = 0.487**

Negative conflict tends to provoke structural reorganisation, after which the control architecture becomes comparatively stable.

### Positive side

Internal source difficulty versus following curvature:

- geometric: **ρ = −0.089**
- partition: **ρ = 0.105**
- semantic: **ρ = 0.288**

The positive side remains more plastic and continues to carry alternative generative organisations much later.

~~~text
NEGATIVE SIDE
stabilise boundaries / constraints relatively early

POSITIVE SIDE
continue exploring alternative generative organisations
until functional roles become clear
~~~

## 8. Inferred conflict-resolution operations

The full trajectory supports the following descriptive operations:

1. **Preserve** — competing structures can coexist for multiple layers.
2. **Partition** — incompatible structures are separated when one parent is too broad.
3. **Compress** — related communities are integrated when a discriminative shared relation exists.
4. **Re-differentiate** — an absorbed domain can reappear when compression leaves unresolved heterogeneity.
5. **Reassign function** — material can survive while changing from domain to satellite, constraint, analytical function or production function.
6. **Integrate only the necessary core** — the dominant structure need not absorb every semantic community.
7. **Sequence complementary functions** — late conflict can be resolved by placing different structures at different positions in one procedure.

## Main conclusion

~~~text
CONFLICT
= multiple plausible organisations of represented information

        ↓

TRANSFORMER RESPONSE

preserve alternatives
→ test broader organisation
→ repartition if necessary
→ assign distinct roles
→ integrate compatible roles
→ sequence functions
→ isolate a functional core
~~~

The critical finding is:

> **The transformer appears to resolve conflicting information primarily by discovering a higher-order organisation in which the useful parts of competing structures can coexist, while material that cannot be integrated is left peripheral rather than necessarily erased.**

This is more precise than saying the model chooses the most coherent interpretation. It frequently passes through less coherent intermediate states, and the final state itself is not globally maximally coherent.

What matters appears to be **functional sufficiency, not total semantic unification**.

## Curvature judgement

A single curvature-density score is not adequate for conflict analysis.

Keep separate:

- geometric curvature;
- partition curvature;
- semantic curvature.

The most informative conflict signature is often:

~~~text
high semantic curvature
+
low geometric curvature
+
rising coherence difficulty
        ↓
abstraction conflict

followed by

high partition curvature
+
falling coherence difficulty
        ↓
re-differentiation / resolution
~~~

S21→S23 is the clearest example.

## Boundary

These findings are descriptive reconstructions from R008–R010. They do not establish a literal symbolic conflict-resolution algorithm or reveal private natural-language thoughts.

The result concerns how the measured/inferred representation changes across transformer depth.
