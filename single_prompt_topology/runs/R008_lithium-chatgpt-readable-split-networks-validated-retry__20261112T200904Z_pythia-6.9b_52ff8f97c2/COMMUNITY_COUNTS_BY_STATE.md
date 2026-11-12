# R008 community counts by state and sector

- Added: `2026-11-13T07:36:57+11:00`
- Timezone: `Australia/Sydney`
- Source artifact: `network_index.csv`
- Source field: `community_count`
- Method: state-side-local Louvain graph partition
- Status: `post-run derived summary; not part of the validated R008 manifest`

## Interpretation boundary

These are measured counts of state-local geometric graph communities. They are
not counts of verified semantic topics or persistent community families.
Community identifiers are local to one state and sector, so similarly numbered
communities in different rows must not be treated as the same community.

## Counts

| State index | Recorded state | Positive-head communities | Negative-tail communities | Combined |
|---:|---|---:|---:|---:|
| 0 | Input embedding | 12 | 10 | 22 |
| 1 | Block 0 output | 12 | 13 | 25 |
| 2 | Block 1 output | 14 | 13 | 27 |
| 3 | Block 2 output | 11 | 15 | 26 |
| 4 | Block 3 output | 12 | 13 | 25 |
| 5 | Block 4 output | 13 | 14 | 27 |
| 6 | Block 5 output | 13 | 13 | 26 |
| 7 | Block 6 output | 12 | 12 | 24 |
| 8 | Block 7 output | 13 | 12 | 25 |
| 9 | Block 8 output | 13 | 12 | 25 |
| 10 | Block 9 output | 13 | 14 | 27 |
| 11 | Block 10 output | 14 | 12 | 26 |
| 12 | Block 11 output | 11 | 13 | 24 |
| 13 | Block 12 output | 12 | 13 | 25 |
| 14 | Block 13 output | 13 | 13 | 26 |
| 15 | Block 14 output | 9 | 13 | 22 |
| 16 | Block 15 output | 11 | 12 | 23 |
| 17 | Block 16 output | 13 | 10 | 23 |
| 18 | Block 17 output | 12 | 12 | 24 |
| 19 | Block 18 output | 13 | 11 | 24 |
| 20 | Block 19 output | 12 | 11 | 23 |
| 21 | Block 20 output | 12 | 11 | 23 |
| 22 | Block 21 output | 11 | 12 | 23 |
| 23 | Block 22 output | 13 | 11 | 24 |
| 24 | Block 23 output | 12 | 12 | 24 |
| 25 | Block 24 output | 11 | 10 | 21 |
| 26 | Block 25 output | 12 | 12 | 24 |
| 27 | Block 26 output | 10 | 12 | 22 |
| 28 | Block 27 output | 11 | 10 | 21 |
| 29 | Block 28 output | 9 | 12 | 21 |
| 30 | Block 29 output | 11 | 12 | 23 |
| 31 | Block 30 output | 11 | 13 | 24 |
| 32 | Final normalization after block 31 | 11 | 12 | 23 |
|  | **All state-local instances** | **392** | **400** | **792** |

## Summary

- Positive-head range per state: 9–14 communities.
- Negative-tail range per state: 10–15 communities.
- Combined range per state: 21–27 communities.
- Positive-head state-local instances across all states: 392.
- Negative-tail state-local instances across all states: 400.
- Total state-local community instances: 792.

The capture does not contain raw block 31 output separately. The final row
therefore combines the block 31 transformation with final layer normalization.

Determining how many of these partitions are semantically coherent requires a
separate content audit. Determining how many persistent community families
exist requires cross-state matching rather than summing these rows.
