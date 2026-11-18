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
