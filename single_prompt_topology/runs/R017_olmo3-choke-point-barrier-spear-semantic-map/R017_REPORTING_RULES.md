# R017 reporting rules derived from R014 and R015

## Purpose

R014 and R015 establish the reporting conventions for semantic-topology runs. R017 is a single-prompt OLMo 3 run, so the same evidence discipline applies even though probe, held-out and perturbation fields are not available.

## Output separation

1. **Measured report**
   - Contains only model identity, prompt/capture contract, measured coverage and structural statistics.
   - Does not contain semantic parent labels or topology claims.
   - Remains a frozen record of the measurement stage.

2. **Completeness verification**
   - Verifies expected states, networks, transitions, graph degree, community assignment and file integrity.
   - Does not introduce semantic interpretation.

3. **Independent semantic reconstruction**
   - Begins only after measurement and completeness validation.
   - Reconstructs the smallest defensible parent inventory from community, transition and target-extreme evidence.
   - Records evidence against each parent and relation.
   - Keeps measured facts and interpreted labels visibly separate.

4. **Structured semantic map**
   - Exports semantic parents as a node table.
   - Exports parent relations as an edge table.
   - Exports the same map as JSON.
   - Uses evidence-scope and confidence fields rather than pretending single-prompt evidence has cross-probe support.

5. **Human analysis and recommendation**
   - States the strongest supported result first.
   - Shows the minimum semantic map.
   - Explains development through depth.
   - States negative evidence and artefacts.
   - States invariance status explicitly.
   - Ends with one bounded next experiment and primary-record paths.

## Interpretation constraints

- Positive-head and negative-tail are cosine alignment and anti-alignment in the fixed input-embedding basis. Negative-tail is not automatically suppression, rejection or contradiction.
- Community IDs are local to one state and one sector.
- Repeated parent identity across sectors is an interpretation; no cross-sector graph edge exists unless separately measured.
- State 00 is the uncontextualised newline embedding and is not prompt-semantic evidence.
- State 64 is the final-normalised representation after Block 63 and is not an additional reasoning block.
- Parent labels are downstream descriptions, not model variables.
- A single trajectory cannot establish order, context, neighbouring-concept or cross-model invariance.
- Large lexical, code, multilingual, formatting and named-entity communities remain evidence of the vocabulary basis and must not be smoothed into the prompt-specific map.

## R017-specific substitution for R014/R015 fields

R014/R015 fields such as probe support, held-out reconstruction and cross-probe mean relation support are not applicable to R017. R017 substitutes:

- **trajectory support** — where in transformer depth the family is recovered;
- **sector tendency** — positive, negative or both;
- **evidence scope** — single-state graph, cross-depth trajectory, or cross-sector interpretation;
- **confidence** — strength of the reconstruction given the available evidence;
- **invariance status** — explicitly `not tested`.

## Canonical downstream files

- `R017_SEMANTIC_RECONSTRUCTION.md`
- `R017_SEMANTIC_MAP_NODES.csv`
- `R017_SEMANTIC_MAP_EDGES.csv`
- `R017_SEMANTIC_MAP.json`
- `R017_RUN_ANALYSIS_AND_RECOMMENDATIONS.html`

The original measured exports remain unchanged.
