"""CLI for configuration-driven semantic-topology measurement."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from topology_engine import load_and_validate_config, measure, recover_validation, verify


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("validate-config", "measure", "recover-validation", "verify")
    )
    parser.add_argument("--config", required=True, type=Path)
    arguments = parser.parse_args()
    context = load_and_validate_config(arguments.config)
    if arguments.action == "validate-config":
        print(
            json.dumps(
                {
                    "status": "valid",
                    "run_id": context.config["run_id"],
                    "prompt_ids": list(context.prompt_ids),
                    "expected": context.config["expected"],
                    "run_directory_exists": context.run_dir.exists(),
                },
                indent=2,
            )
        )
    elif arguments.action == "measure":
        measure(context)
    elif arguments.action == "recover-validation":
        print(json.dumps(recover_validation(context), indent=2))
    else:
        print(json.dumps(verify(context), indent=2))


if __name__ == "__main__":
    main()
