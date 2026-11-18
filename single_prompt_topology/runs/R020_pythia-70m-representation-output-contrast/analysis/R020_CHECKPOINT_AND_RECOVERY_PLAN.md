# R020 — checkpointed semantic-analysis and recovery plan

**Purpose:** Make the 32-decision / eight-state / two-sector R020 semantic reconstruction restartable without rerunning validated work.

**Scope:** This is a post-measurement execution and recovery procedure. It does not change the frozen R020 measurement, its configuration, its hypotheses or its analysis methodology. The human reviewer determines usefulness; the agent exposes candidate semantic structure with evidence and unresolved alternatives.

## 1. What already exists

An R020 provisional semantic reconstruction was recorded in the repository before this checkpoint plan was added. Its analysis manifest reports 512 measured networks, 6,944 communities, 1,865 provisionally labelled candidates, 33 mixed/competing cases and 5,046 unresolved cases. A semantic map and reports exist. These are **existing, provisional analysis artefacts**, not a human-endorsed judgement of usefulness.

- Source measurement snapshot: `6d7d6547e04407556b303b1c8b3ce9941daa8138`
- Analysis snapshot inspected for this plan: `40a8498ab66287d5b0ee6ce0827dc2b0708e12b9`
- Existing analysis status: `provisional_semantic_reconstruction_prepared`
- Human usefulness evaluation: `pending`
- Frozen measurement manifest: `../manifest.json` (do not edit to reflect partial analysis)
- Existing analysis manifest: `R020_ANALYSIS_MANIFEST.json` (preserve its recorded claims and limitations)
- Checkpoint ledger: `R020_CHECKPOINT_LEDGER.json`

## 2. Execution stages and persisted outputs

Every stage must finish with a verifiable Git commit **before** the next stage begins. When reconstructing or extending the analysis, use a new versioned output path; do not overwrite frozen evidence or a previous accepted checkpoint.

| Stage | Bounded operation | Persistent checkpoint | Validation / stop condition |
|---|---|---|---|
| C00 | Pin inputs and verify measurement coverage | Source commit, SHA-indexed measurement manifest and inventory | Exactly 32 decisions × eight states × two sectors = 512 networks; 6,944 communities in the recorded measurement |
| C01 | Screen communities for decisions 01–08 | `R020_COMMUNITIES_01-08.json` | Complete communities for 128 state/sector cells; record unresolved and mixed cases |
| C02 | Screen communities for decisions 09–16 | `R020_COMMUNITIES_09-16.json` | As above; no dependence on later decisions |
| C03 | Screen communities for decisions 17–24 | `R020_COMMUNITIES_17-24.json` | As above |
| C04 | Screen communities for decisions 25–32 | `R020_COMMUNITIES_25-32.json` | As above; all 6,944 communities accounted for across shards |
| C05 | Reconstruct within-decision layer changes and between-decision trajectories | `R020_STATE_CELLS.json` | Each retained proposed connection identifies decision, state, cosine sector, communities and evidence; unresolved links remain unresolved |
| C06 | Analyse controls, stability and candidate-parent support | `R020_DERIVED_DIAGNOSTICS.json` | Distinguish measurement from lexical-semantic screening; preserve shuffled-control limitations |
| C07 | Present the consolidated semantic network and accessible detailed evidence | `R020_SEMANTIC_RECONSTRUCTION_REPORT.md` and `R020_SEMANTIC_MAP_REPORT.html` | Map and reports disclose uncertainty, provenance and interpretative limits; not a claim that semantic usefulness is proven |
| C08 | Human evaluates usefulness and supplies any constraints | New dated human-feedback entry when supplied | **Pending**: do not invent user judgements or conclude the comparison on their behalf |
| C09 | Incorporate confirmed corrections and record final interpretation | Versioned final report plus updated analysis lifecycle record | Complete only after C08 and all required evidence/controls are reconciled |

C01–C04 are deliberately independent units. If one eight-decision group fails, the other groups remain available. For a finer-grained rerun, persist each decision as a separate file and roll up to the same four documented groups; never require the whole 32-decision analysis to succeed before saving anything.

## 3. Recovery contract

1. Inspect GitHub `main` and `R020_CHECKPOINT_LEDGER.json` before doing any further analysis.
2. For each stage marked **recorded**, verify that every declared file exists and its Git blob SHA matches the ledger. Report a mismatch instead of silently trusting a path.
3. Skip stages whose artefacts and validation have already been recorded; resume only at the earliest missing, failed or explicitly reopened stage.
4. Write a new stage artefact to a temporary/versioned destination, verify its completeness, **commit it**, and only then update the checkpoint ledger with that immutable file SHA. A crash before ledger update leaves the committed artefact recoverable.
5. If a stage fails, record the failure and the remaining work without touching earlier checkpoints. Preserve original evidence, failed attempts and interpretive residuals.
6. If methodology or labels change, create a **new version**. Do not rewrite a historical screening result to make it appear consistent with a later interpretation.
7. Do not mark the scientific hypothesis as supported merely because the generated continuation is poor, or because a post-hoc lexical labelling rule produces a plausible semantic map.
8. Do not mark R020 scientifically complete until the human has evaluated the map and the outstanding comparison is documented.

## 4. Critical boundaries

- **No model rerun** is needed for semantic interpretation of the existing data.
- **No forced SDA-3, GRD, causal or training-document claims.**
- Preserve community identities and measurable relationships rather than compressing immediately into plausible subject headings.
- The generated continuation and candidate adjacent domains were previously disclosed, so the existing interpretation **cannot be described as blind**.
- The existing semantic analysis used compact community summaries rather than the complete raw 1.42-million-membership dataset. Any stronger raw-membership claim needs its own separately verified stage.
- Human usefulness is the decision boundary: the agent supplies inspectable structures, and the human judges whether they are useful.

## 5. Current status

The existing provisional analysis already contains C01–C07 outputs; this plan registers and preserves them rather than treating them as new work. SHA and presence are recorded in the separate ledger. Their analytic claims remain provisional and have not been independently revalidated in this checkpoint-setting step. C08 (human review) and C09 (final interpretation) remain open.

**Next decision:** Present the existing semantic map to the human reviewer, accept specific usefulness judgements or constraints, and only revisit the stages that the feedback shows to be inadequate.
