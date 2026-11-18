# R020 — Independent evidence audit of cross-generation semantic hypotheses (v3)

**Scope:** Check the saved v3 decision-level candidate hypothesis maps against R020's immutable measured community-edge export and the second-pass full relational maps. This check concerns *evidence integrity*, not a presumption that selected semantic labels are correct.

**Source:** `single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/community_edges.csv`, original measured network/transition data, `R020_RELATIONAL_MAP_D01-08.json` through `D25-32.json`, and `R020_FUNCTIONAL_HYPOTHESIS_D01-08.json` through `D25-32.json`.

## Verification results

| Check | Result |
|---|---:|
| Distinct generated-token decision maps | **32 / 32** |
| Decision/state/sector evidence cells present in v3 and v2 | **512 / 512** |
| Original measured intercommunity edges indexed | **42,291** |
| Relationship-evidence references checked against the source CSV | **359 / 359 matched** |
| Community exemplar tokens verified against source relational communities | **2,353 / 2,353 matched** |
| Quoted normalised edge affinities recomputed from edge count and community sizes | **359 / 359 matched** |
| Mismatched source edges, exemplar tokens, or affinities | **0** |
| Community-shard Git blob IDs reconciled against saved trajectory index | **4 / 4** |

**Indexing rule:** V3 reports use 1-based decision labels D01–D32. Measurement CSV uses 0-based `decision_index`. References were checked after the corresponding index conversion. For each evidence link, the canonical undirected community pair, transformer state, cosine sector and measured token-edge count agree.

**Coverage:** The four v3 checkpoints account for decisions 01–08, 09–16, 17–24 and 25–32, without missing or duplicate decision labels. This check covers **all cited relationship examples** in the v3 decision files, including task-candidate, background/cross-domain and negative-sector records. It does not establish that the selected examples exhaust the measured 42,291 cross-community edges.

## Research answer, bounded by the evidence

The v3 reconstruction identifies a **recurring functional field connecting settlements, movement/routes, crossings, built environments and inhabitants**, but does **not** recover it as one uninterrupted, fully integrated hypothesis in every generation decision.

- **21/32** decisions contain at least one qualifying task-candidate relation in contextual states S01–S05.
- **6/32** contain the same qualifying relation in more than one contextual state.
- **11/32** lack a qualifying positive contextual relation at the prespecified screen threshold; these are unresolved cases, not demonstrations of absence.
- **0/32** have a qualifying task-candidate positive relation at S06–S07 under this projection and screening procedure.
- The most recurrent contextual edge families are `movement/routes ↔ settlement` (**11 decisions**) and `connection/crossing ↔ movement/routes` (**8 decisions**).

**Test against repeated input words:** In the duplicated continuation, candidate functional relations recur for the same words at different positions, but the specific parent combinations and transformer states often change. This supports **selective reactivation with contextual variation** over identical replay of one fixed graph.

**Role-binding gap:** The existing records do not establish sustained binding of *city as the actor*, *bridge as a constructed means*, *river as an obstacle*, and *crossing as the purpose*. Instead, parts of these relationships are intermittently recoverable, consistent with the malformed generated response. This is a candidate explanatory interpretation, not a proven mechanism.

## What the audit does not establish

1. **Semantic ground truth:** Semantic role families were curated after inspecting R020, and some communities carry more than one role. A measured edge and corroborated exemplars establish the evidence underlying an interpretation, not unique or complete semantic meaning.
2. **Exhaustive latent structure:** The v3 selection contract recognises 818 of 6,944 communities. The rest remain available in the complete v2 relational maps. An absent v3 match is not proof the semantic relationship does not exist.
3. **Causal chain of thought:** The maps describe associated vocabulary communities, not a causal reasoning sequence.
4. **Output-head equivalence:** R020 measures vocabulary projection in the input embedding basis, while the Pythia input/output embedding matrices are untied. The absence of qualified S06–S07 relations cannot establish that the final predictive representation lost the corresponding information.
5. **Human utility:** The research question of whether this reconstruction provides *useful* information beyond the poor generated response remains for the human reviewer.

## Saved analysis products

- [The cross-generation higher-order report](R020_GENERATION_WIDE_SEMANTIC_HYPOTHESIS_REPORT.md).
- [Interactive per-token hypothesis map](R020_PER_TOKEN_HYPOTHESIS_MAP.html).
- [Cross-generation evidence and recurring relationships](R020_CROSS_GENERATION_HYPOTHESIS_TRAJECTORY.json).
- [Decision evidence 01–08](R020_FUNCTIONAL_HYPOTHESIS_D01-08.json), [09–16](R020_FUNCTIONAL_HYPOTHESIS_D09-16.json), [17–24](R020_FUNCTIONAL_HYPOTHESIS_D17-24.json), [25–32](R020_FUNCTIONAL_HYPOTHESIS_D25-32.json).
- [Complete pre-existing community networks](R020_RELATIONAL_SEMANTIC_MAPS.html).

**Operational conclusion:** The requested per-decision and cross-generation *candidate semantic hypothesis maps* are present, recoverable and checked against their cited measured edges. Scientific interpretation remains evidence-bounded; the immediate next action is human inspection of the relationships and unexplained residuals, not another measurement run.
