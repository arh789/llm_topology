from __future__ import annotations

import argparse
import inspect
import json
import platform
import sys
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path


def safe_signature(value: object) -> str | None:
    try:
        return str(inspect.signature(value))
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect the installed llama.cpp Python API for intermediate "
            "transformer-state access without loading model weights."
        )
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", type=Path, required=True)
    args = parser.parse_args()

    import llama_cpp
    from llama_cpp import llama_cpp as low_level

    high_level_names = sorted(
        name
        for name in dir(llama_cpp.Llama)
        if any(term in name.lower() for term in ("embed", "eval", "hidden", "state"))
    )
    low_level_names = sorted(
        name
        for name in dir(low_level)
        if any(
            term in name.lower()
            for term in ("embed", "eval", "hidden", "tensor", "callback")
        )
    )

    high_level_api = {
        name: safe_signature(getattr(llama_cpp.Llama, name))
        for name in high_level_names
    }
    low_level_api = {
        name: safe_signature(getattr(low_level, name)) for name in low_level_names
    }

    explicit_intermediate_candidates = sorted(
        name
        for name in set(high_level_names + low_level_names)
        if "hidden" in name.lower()
        or ("layer" in name.lower() and "embed" in name.lower())
        or ("intermediate" in name.lower() and "state" in name.lower())
    )

    model = args.model.resolve()
    report = {
        "probe": "llama_cpp_intermediate_state_api",
        "status": "successful",
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "platform": platform.platform(),
        "llama_cpp_python": metadata.version("llama-cpp-python"),
        "module_path": str(Path(llama_cpp.__file__).resolve()),
        "model": {
            "path": str(model),
            "exists": model.is_file(),
            "bytes": model.stat().st_size if model.is_file() else None,
            "loaded": False,
        },
        "high_level_api": high_level_api,
        "low_level_api": low_level_api,
        "explicit_intermediate_candidates": explicit_intermediate_candidates,
        "supports_intermediate_hidden_states": bool(explicit_intermediate_candidates),
        "interpretation": (
            "An explicit candidate API was found and requires an execution test."
            if explicit_intermediate_candidates
            else "No explicit API for per-layer intermediate hidden states was exposed."
        ),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
