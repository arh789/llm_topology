"""Locked prompt specification for the R015 overlapping-context run."""

from __future__ import annotations


RUN_ID = "R015_qwen-adjacent-neighbourhood-expansion"
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
MODEL_REVISION = "a09a35458c702b33eeacc393d103063234e8bc28"
ANCHOR_TEXT = "\n"

CONCEPTS = {
    "A": "sensor",
    "B": "apartment",
    "C": "line",
    "D": "sessions",
}

PROBES = {
    "P1": ("A", "B", "C"),
    "P2": ("A", "B", "D"),
    "P3": ("A", "C", "D"),
    "P4": ("B", "C", "D"),
}

LOCAL_PERMUTATIONS = ("ABC", "ACB", "BAC", "BCA", "CAB", "CBA")
LOCAL_INDEX = {"A": 0, "B": 1, "C": 2}


def build_prompt_specs() -> dict[str, dict[str, object]]:
    specs: dict[str, dict[str, object]] = {}
    for probe_id, probe_keys in PROBES.items():
        for local_permutation in LOCAL_PERMUTATIONS:
            concept_key_order = tuple(
                probe_keys[LOCAL_INDEX[position]]
                for position in local_permutation
            )
            concept_order = tuple(CONCEPTS[key] for key in concept_key_order)
            prompt_id = f"{probe_id}_{local_permutation}"
            specs[prompt_id] = {
                "prompt_id": prompt_id,
                "probe_id": probe_id,
                "local_permutation": local_permutation,
                "probe_concept_keys": probe_keys,
                "probe_concepts": tuple(CONCEPTS[key] for key in probe_keys),
                "concept_key_order": concept_key_order,
                "concept_order": concept_order,
                "raw_prompt": "".join(f"{concept}\n" for concept in concept_order),
            }
    return specs


PROMPT_SPECS = build_prompt_specs()
PROMPT_IDS = tuple(PROMPT_SPECS)
PROBE_PROMPT_IDS = {
    probe_id: tuple(
        f"{probe_id}_{local_permutation}"
        for local_permutation in LOCAL_PERMUTATIONS
    )
    for probe_id in PROBES
}

assert len(PROMPT_IDS) == 24
assert all(len(prompt_ids) == 6 for prompt_ids in PROBE_PROMPT_IDS.values())
assert all(
    str(spec["raw_prompt"]).endswith(ANCHOR_TEXT)
    for spec in PROMPT_SPECS.values()
)
