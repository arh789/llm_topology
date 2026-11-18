# R020 checkpoint integrity audit

## Integrity event A001 — Incorrect registered Git blob SHA

- Context: registering and verifying already-produced R020 analysis artefacts under the checkpoint/recovery scheme.
- Stage: `C03` — `R020_COMMUNITIES_17-24.json`.
- Ledger initially recorded SHA: `6b25a09e1647921505be288718a152c9c50875d8a`.
- GitHub directory entry and original analysis manifest record: `6b25a09e1647921505be288718a152c9c50875d8`.
- Cause: a transcription error in the new recovery ledger, not evidence that the original analysis shard changed.
- Consequence: a verifier that correctly compares exact Git blob SHAs must **fail closed** before any status for C03 is trusted.
- Correction: update the ledger to the exact existing blob SHA; preserve this audit entry as the explanation.
- The check detected exactly **one mismatch among ten analysis-file SHA registrations**. Nine other registrations matched their GitHub directory entries. This compares blob identities only; it is not an independent validation of the semantic classifications inside the files.
- The frozen measurement and existing semantic analysis artefacts are unchanged.

## Subsequent verification requirements

1. Reject a SHA that is not exactly 40 hexadecimal characters.
2. Verify the Git blob SHA of each artefact before treating a recorded checkpoint as reusable.
3. Verify expected decision/state/sector coverage separately from blob identity.
4. A failed verification must leave the input files and earlier checkpoint records intact.
5. Do not report an analysis checkpoint as validated solely because the ledger says it is complete.

## Integrity event A002 — Source pinning and remote catalogue check

- The checkpoint ledger was extended to pin thirteen primary measurement/control files plus ten existing analysis artefacts.
- All **23 of 23** registered Git blob SHAs matched GitHub's file metadata after the recorded A001 correction.
- Independently checked compact metadata: `measurement_results.json`, `R020_ANALYSIS_MANIFEST.json`, and `R020_DERIVED_DIAGNOSTICS.json` agree on 32 decisions, 512 networks and 6,944 communities (where those fields apply).
- The read-only `R020_VERIFY_CHECKPOINTS.js` verifier was added. Its JavaScript **syntax** was checked, but it has **not yet been executed against a complete local checkout** in this session. The remote catalogue check is not equivalent to local full-file hashing, shard-by-shard completeness verification, or validation of the correctness of semantic labels.
- A concise human-review packet was saved separately; its publication does not constitute human endorsement of usefulness.
- On a future run, execute `node single_prompt_topology/runs/R020_pythia-70m-representation-output-contrast/analysis/R020_VERIFY_CHECKPOINTS.js` from a complete checkout. **Do not proceed** with a checkpoint that fails this validation.
