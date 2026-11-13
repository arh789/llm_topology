# R010 layer-wise community and latent-parent map

## Purpose

This is a compact index of the completed R010 Phase-A reconstructions.

It answers, for each recorded transformer state:

> Which observed R008 communities are grouped under which higher-order latent parent candidates?

The parent candidates are **inferred semantic structures**, not measured graph nodes or causal transformer features.

Notation:

- `C#` = state-local R008 community ID.
- `P+#` / `P-#` = state-local positive-head / negative-tail latent parent candidate.
- Percentage in brackets = **semantic-eligible coverage on that side**, not percentage of the whole state.
- Parent IDs have **no continuity meaning across states**.
- Formal/tokeniser communities and most irreducible/mixed communities are omitted here for concision; the individual state files retain their complete disposition tables.
- State 00 is the input-embedding baseline.
- States 01–31 are block 0–30 outputs.
- State 32 is the final normalised output after block 31. Raw block 31 is not separately captured.

## Layer-wise map

| State / transformer point | Positive-head latent parent candidates | Negative-tail latent parent candidates |
|---|---|---|
| **S00 — input embedding** | **P+0** Chemical/engineering material composition — C6,C7,C8 (21.8%); **P+1** physical/environmental + electrochemical energy processes — C2,C3 (25.7%); **P+2** biomedical/pharmacological substances + intervention — C0,C9,C11 (26.4%) | **P-0** Symbolic/information interpretation + evaluation — C1,C2,C8 (58.6%) |
| **S01 — block 0** | **P+0** Information systems + information maintenance — C1,C4 (39.4%); **P+1** social/institutional organisation + participation — C6,C10 (23.5%); **P+2** biological/health/living systems — C8,C9 (22.2%) | **P-0** Transformation + interpretive/behavioural constraint — C3,C4 (32.7%) |
| **S02 — block 1** | **P+0** Action/progress appraisal + contextual modulation — C0,C7 (27.3%); **P+1** computational/mathematical-scientific systems — C3,C11 (21.5%); **P+2** geopolitical/civic-social organisation — C4,C6 (22.3%); **P+3** biological/health/cultivated-living systems — C1,C12 (20.8%) | **P-0** Prohibition/transgression/harmful social action — C1,C3 (42.0%); **P-1** scientific/biomedical analysis + controlled transformation — C6,C9 (21.9%) |
| **S03 — block 2** | **P+0** Information access/retrieval/transaction systems — C2,C6 (33.3%); **P+1** social/institutional context + appraisal — C3,C4 (31.8%); **P+2** biological/health/cultivated-living systems — C1,C9 (31.4%) | **P-0** Adverse evaluation/violence/prohibited harm — C1,C8 (25.5%); **P-1** scientific/clinical analysis + interpretation — C2,C6 (26.5%); **P-2** institutional authority + public/social roles — C3,C12 (17.4%) |
| **S04 — block 3** | **P+0** Information/task operations + digital systems — C0,C5 (33.9%); **P+1** biological/molecular/physical-scientific systems — C2,C6 (31.6%); **P+2** geographic/political/institutional-economic organisation — C4,C9 (21.2%) | **P-0** Analytical/clinical description + explanation — C1,C6 (31.6%); **P-1** evaluation/regulation/state change — C4,C5 (25.7%); **P-2** institutional authority/social roles/conflict — C2,C11 (22.4%) |
| **S05 — block 4** | **P+0** Information/task operations + transactional systems — C2,C3 (35.5%); **P+1** geographic/psychological/institutional-social organisation — C5,C6 (30.8%); **P+2** biological/molecular/living-consumption systems — C4,C10 (22.0%) | **P-0** Analysis/interpretation/clinical characterisation — C1,C6 (35.5%); **P-1** adversity/destructive evaluation/institutional conflict — C2,C5 (39.0%) |
| **S06 — block 5** | **P+0** Operational information + task/work systems — C0,C3 (37.8%); **P+1** psychosocial/institutional + territorial organisation — C5,C6 (27.2%); **P+2** biological/physical + organismal living systems — C4,C10 (21.4%) | **P-0** Adverse assessment + destructive-state characterisation — C1,C2 (53.2%); **P-1** institutional authority/conflict + material setting — C5,C6 (30.3%) |
| **S07 — block 6** | **P+0** Operational information + work/process systems — C1,C3 (33.7%); **P+1** social-institutional + territorial organisation — C4,C5 (22.5%); **P+2** biomedical/psychological + molecular/cellular living systems — C0,C8 (30.2%) | **P-0** Analytical constraint + adverse-state evaluation — C0,C4 (45.7%); **P-1** public authority/institutional order + transgression — C5,C7 (21.7%) |
| **S08 — block 7** | **P+0** Work/task operations + information systems — C0,C5 (35.0%); **P+1** political/geographic/organisational-economic activity — C3,C7 (26.9%); **P+2** biomedical/molecular-scientific + organismal systems — C2,C6,C11 (32.8%) | **P-0** Analytical/clinical assessment + characterisation — C1,C8 (21.4%); **P-1** adverse evaluation + destructive/compositional change — C4,C5 (22.1%); **P-2** institutional/public environments + material settings — C2,C6 (24.4%) |
| **S09 — block 8** | **P+0** Operational/transactional/interaction systems — C0,C1 (46.9%); **P+1** geographic + social-cultural identity — C4,C11 (17.4%) | **P-0** Scientific/clinical analysis + technical systems — C2,C5,C9 (39.6%); **P-1** regulation/destructive change/adverse affect — C3,C6 (30.6%) |
| **S10 — block 9** | **P+0** Organised task/transaction/information activity — C0,C1,C5 (52.3%); **P+1** biomedical + interacting physical/biological systems — C2,C10 (23.6%) | **P-0** Evaluative characterisation/constraint/destructive change — C0,C4 (39.2%); **P-1** public/social actors + institutional-material environments — C3,C8 (24.7%) |
| **S11 — block 10** | **P+0** Investigation/evaluation/information-production systems — C0,C2,C9 (46.5%); **P+1** biological + interacting physical-system organisation — C4,C5 (26.0%) | **P-0** Quantitative characterisation/adverse evaluation/destructive constraint — C1,C2,C6 (57.4%); **P-1** civic/institutional authority + social roles — C4,C10 (21.1%) |
| **S12 — block 11** | **P+0** Exploratory activity + social-professional coordination — C1,C2 (39.1%); **P+1** biomedical + interacting physical-system organisation — C4,C5 (27.5%) | **P-0** Quantitative characterisation/adverse evaluation/restrictive-change operations — C0,C3,C6 (60.1%); **P-1** civic/social authority + geographic-public identity — C4,C12 (17.0%) |
| **S13 — block 12** | **P+0** Coordinated inquiry/management/process activity — C4,C6 (22.7%); **P+1** biomedical/developmental/embodied-life organisation — C1,C8 (28.1%) | **P-0** Evaluative constraint/regulation/adverse-state organisation — C0,C6 (35.9%); **P-1** civic/institutional authority + territorial identity — C3,C9 (21.8%); **P-2** scientific/quantitative + clinical systems — C5,C7 (21.5%) |
| **S14 — block 13** | **P+0** Coordinated inquiry/communication/professional action — C1,C5 (47.2%); **P+1** biomedical + interacting physical-system organisation — C3,C9 (31.8%) | **P-0** Characterisation/regulatory constraint/adverse evaluation — C0,C1 (54.3%); **P-1** institutional/familial + territorial order — C5,C9 (14.1%); **P-2** material + technical infrastructure — C6,C7 (15.1%) |
| **S15 — block 14** | **P+0** Inquiry/interaction/analytical process activity — C4,C6 (55.3%) | **P-0** Characterisation/adverse constraint/transformation — C0,C3,C8 (53.1%); **P-1** institutional/familial roles + territorial identity — C4,C11 (19.1%) |
| **S16 — block 15** | **P+0** Transformational process/sequencing/evaluation — C1,C7 (39.6%); **P+1** health/psychosocial/biomedical organisation — C2,C4 (39.4%) | **P-0** Characterisation/evaluative intensity/quantitative consistency — C0,C4,C6 (54.7%); **P-1** civic/territorial authority + social order — C7,C8 (17.6%) |
| **S17 — block 16** | **P+0** Developmental/transformational/evaluative process organisation — C0,C1,C2 (58.7%) | **P-0** Regulatory characterisation/administrative configuration/social organisation — C0,C2 (46.6%); **P-1** institutional/conflict roles + material-embodied environments — C5,C6 (29.1%) |
| **S18 — block 17** | **P+0** Goal-directed development/transformation + quantitative activity — C2,C4 (44.0%); **P+1** mediated learning/communication + software-interface systems — C6,C7 (20.6%) | **P-0** Administrative characterisation/adverse constraint/institutional change — C0,C3,C5 (57.6%); **P-1** institutional/familial authority + territorial identity — C6,C10 (17.0%) |
| **S19 — block 18** | **P+0** Developmental process/transformation + quantitative analysis — C3,C4 (41.5%); **P+1** biomedical health + lived wellbeing — C5,C8 (30.4%) | **P-0** Constitutional/regulatory constraint/administrative characterisation/adverse judgement — C0,C1,C5 (59.4%); **P-1** institutional/social order + material environment — C4,C7 (28.8%) |
| **S20 — block 19** | **P+0** Goal-directed development + quantitative system dynamics — C3,C7 (35.8%); **P+1** mediated creative + professional activity — C2,C8 (33.1%) | **P-0** Characterisation/adverse judgement/institutional change — C0,C5,C7 (53.3%); **P-1** institutional/territorial + material-public environment — C3,C6 (29.9%) |
| **S21 — block 20** | **P+0** Exploratory measurement + evolving system dynamics — C2,C3 (42.0%); **P+1** mediated social/creative activity + interface systems — C5,C7 (27.6%) | **P-0** Administrative/regulatory characterisation/adverse evaluation/controlled change — C0,C3,C4 (54.5%); **P-1** civic/territorial authority + social order — C6,C7 (22.5%) |
| **S22 — block 21** | **P+0** Analytical inquiry + applied research/enterprise activity — C0,C3 (56.2%) | **P-0** Regulatory/adverse intervention + administrative state characterisation — C0,C1 (51.9%); **P-1** territorial/civic authority + social order — C6,C8 (19.4%) |
| **S23 — block 22** | **P+0** Developmental process + quantitative-organisational analysis — C1,C2 (34.7%); **P+1** embodied wellbeing + biomedical health — C6,C7 (27.2%) | **P-0** Regulatory intervention/administrative characterisation/adverse judgement — C1,C4,C7 (50.1%); **P-1** institutional/territorial authority + political order — C6,C10 (19.2%) |
| **S24 — block 23** | **P+0** Developmental process + quantitative system analysis — C0,C7 (38.0%); **P+1** mediated creative/research + professional activity — C3,C8 (28.1%) | **P-0** Administrative characterisation/adverse judgement/controlled change — C1,C2,C3 (53.8%); **P-1** territorial identity + institutional/mythic authority — C5,C8 (19.5%) |
| **S25 — block 24** | **P+0** Developmental/organisational/quantitative inquiry — C1,C4,C6 (57.2%) | **P-0** Administrative/regulatory characterisation/adverse judgement/controlled change — C1,C3,C5 (52.7%); **P-1** institutional/territorial order + material-public environment — C2,C4 (35.2%) |
| **S26 — block 25** | **P+0** Applied inquiry/measurement/developmental change — C0,C6,C8 (49.7%); **P+1** digital interface + mediated information-production systems — C5,C11 (22.2%) | **P-0** Administrative/regulatory characterisation/controlled change/adverse judgement — C1,C2,C9 (46.4%); **P-1** territorial identity + institutional/political authority — C4,C6 (23.3%) |
| **S27 — block 26** | **P+0** Analytical/communicative/professional information activity — C0,C2,C5,C6 (72.1%) | **P-0** Administrative/regulatory characterisation/controlled change/adverse judgement — C1,C2,C7 (51.1%); **P-1** territorial identity + institutional/mythic authority — C6,C9 (17.6%) |
| **S28 — block 27** | **P+0** Analytical inquiry/enterprise/technical information systems — C0,C3,C5 (61.9%); **P+1** embodied health + lived wellbeing — C4,C7 (25.6%) | **P-0** Regulatory characterisation + adverse/prohibitive intervention — C0,C1 (51.2%); **P-1** territorial identity + institutional/mythic authority — C6,C7 (21.9%) |
| **S29 — block 28** | **P+0** Analytical/organisational/technical information systems — C0,C3,C7 (62.8%) | **P-0** Administrative/regulatory characterisation + adverse/prohibitive control — C1,C2 (54.7%); **P-1** territorial identity + institutional/mythic authority — C5,C9 (16.6%) |
| **S30 — block 29** | **P+0** Developmental/organisational/quantitative activity — C1,C3,C5 (62.0%) | **P-0** Regulatory characterisation + adverse/prohibitive intervention — C0,C2 (48.4%); **P-1** territorial identity + institutional/mythic authority — C4,C5 (24.2%) |
| **S31 — block 30** | **P+0** Analytical interpretation + evidential evaluation — C0,C7,C9 (48.5%); **P+1** mediated professional/enterprise/information-production activity — C3,C4 (34.7%) | **P-0** Regulatory characterisation/controlled change/adverse judgement — C0,C3,C8 (52.5%); **P-1** territorial identity + institutional/mythic authority — C2,C11 (20.8%) |
| **S32 — block 31 + final normalisation** | **P+0** Information-processing/state-change/reporting workflow — C2,C4,C7 (51.3%) | **P-0** Structural characterisation/extreme evaluation/destructive-state change — C0,C2,C4 (52.5%); **P-1** ceremonial/civic/institutional authority — C6,C8 (18.9%) |

## How this identifies within-layer relationships

Each retained parent is a compact relational claim:

```text
community A ─┐
community B ─┼─> inferred latent parent
community C ─┘
```

For example:

- **S24 positive P+0** says communities C0 and C7 are jointly explained by a larger developmental/quantitative-analysis structure.
- **S24 negative P-0** says C1, C2 and C3 form a larger administrative-characterisation / adverse-judgement / controlled-change structure.
- **S32 positive P+0** says C2, C4 and C7 form a functional information-processing → state-change → reporting workflow.

The individual state files retain the supporting intercommunity edge counts, mean cosines, irreducible communities, mixed/unresolved communities, formal substrate and alternative reconstructions.

## What has already been analysed across layers?

Two different things must be separated.

### 1. Measured network evolution — already available in R008

R008 already quantifies adjacent-state changes in the measured networks, including:

- membership Jaccard;
- edge Jaccard;
- community ARI;
- positive/negative population size;
- community count;
- intercommunity organisation.

That analysis established that the network is not static and identified especially large measured discontinuities at the **input embedding → block 0** transition and **block 30 → final normalisation** transition.

### 2. Semantic architectural evolution — not yet performed

R010 Phase A deliberately prohibited cross-state correspondence claims.

Therefore no formal analysis has yet established whether the latent structures in this report:

- persist;
- strengthen or weaken;
- broaden or narrow;
- split or merge;
- appear or disappear;
- reappear;
- change side.

Phase A has now passed completeness verification, so this is the authorised next task for **R010 Phase B**.

The correct Phase-B starting point is not to assume that similarly named parents are identical. It is to infer correspondence among these independently reconstructed state-local structures, preserve ambiguous alternatives, and only then describe the semantic trajectory through the transformer.
