"""Execute the complete R013 capture-to-evidence production workflow."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


RUN_ID = "R013_qwen-bare-concept-permutation-topology"
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
MODEL_REVISION = "a09a35458c702b33eeacc393d103063234e8bc28"
REQUIRED_COMPONENTS = (
    "plan_lock",
    "environment_probe",
    "anchor_probe",
    "primary_capture",
    "capture_validation",
    "projection_and_cutoffs",
    "split_networks_and_communities",
    "within_permutation_transitions",
    "pairwise_permutation_comparisons",
    "permutation_invariance",
    "chatgpt_exports",
    "completeness_validation",
    "run_report",
)

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PIPELINE_DIR.parent
RUN_DIR = PIPELINE_DIR / "runs" / RUN_ID
PLAN_PATH = PIPELINE_DIR / "R013_PLAN.md"
MANIFEST_PATH = RUN_DIR / "manifest.json"
LOG_PATH = RUN_DIR / "R013_EXECUTION_LOG.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def append_log(title: str, lines: list[str]) -> None:
    prefix = "# R013 execution log\n\n" if not LOG_PATH.exists() else "\n"
    with LOG_PATH.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(prefix)
        handle.write(f"## {utc_now()} — {title}\n\n")
        for line in lines:
            handle.write(f"- {line}\n")


def git_value(*arguments: str) -> str:
    result = subprocess.run(
        ["git", *arguments],
        cwd=PROJECT_DIR,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def initialize_manifest() -> dict:
    import networkx
    import numpy
    import pandas
    import safetensors
    import sklearn
    import torch
    import transformers

    if not PLAN_PATH.is_file():
        raise FileNotFoundError(f"Missing locked R013 plan: {PLAN_PATH}")
    if not torch.cuda.is_available():
        raise RuntimeError("R013 requires CUDA.")

    previous = None
    if MANIFEST_PATH.exists():
        previous = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if previous.get("status") == "successful":
            raise RuntimeError("R013 is already successful; refusing to overwrite it.")

    started_at = utc_now()
    free_bytes, total_bytes = torch.cuda.mem_get_info()
    components = {
        name: {"status": "pending"} for name in REQUIRED_COMPONENTS
    }
    components["plan_lock"] = {
        "status": "successful",
        "completed_at": started_at,
        "path": str(PLAN_PATH.relative_to(PROJECT_DIR)).replace("\\", "/"),
        "sha256": sha256_file(PLAN_PATH),
    }
    components["environment_probe"] = {
        "status": "successful",
        "completed_at": started_at,
        "python": sys.version,
        "executable": sys.executable,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "numpy": numpy.__version__,
        "pandas": pandas.__version__,
        "networkx": networkx.__version__,
        "sklearn": sklearn.__version__,
        "safetensors": safetensors.__version__,
        "gpu_name": torch.cuda.get_device_name(0),
        "gpu_total_bytes": int(total_bytes),
        "gpu_free_bytes": int(free_bytes),
    }
    history = list(previous.get("status_history", [])) if previous else []
    if previous:
        history.append(
            {
                "status": previous.get("status"),
                "started_at": previous.get("started_at"),
                "completed_at": previous.get("completed_at"),
                "failure_details": previous.get("failure_details"),
            }
        )
    manifest = {
        "schema_version": 1,
        "run_id": RUN_ID,
        "status": "running",
        "started_at": started_at,
        "completed_at": None,
        "failure_details": None,
        "source_git_commit": git_value("rev-parse", "HEAD"),
        "source_git_status": git_value("status", "--short"),
        "objective": (
            "Measure order-invariant and order-associated semantic topology for "
            "six bare-concept permutations at a controlled final anchor."
        ),
        "model": {
            "id": MODEL_ID,
            "revision": MODEL_REVISION,
            "precision": "bfloat16",
            "cache_only": True,
        },
        "expected": {
            "permutations": 6,
            "states": 29,
            "hidden_width": 3584,
            "sides": 2,
            "networks": 348,
            "adjacent_state_comparisons": 336,
            "matched_state_pair_comparisons": 870,
        },
        "required_components": list(REQUIRED_COMPONENTS),
        "components": components,
        "artifacts": {},
        "status_history": history,
        "execution_attempts": [
            {"started_at": started_at, "status": "running"}
        ],
        "interpretation_boundary": (
            "R013 produces measured topology and invariance evidence only; semantic "
            "parents, SDA/GRD roles, coherence and semantic curvature are excluded."
        ),
    }
    write_json(MANIFEST_PATH, manifest)
    append_log(
        "run opened",
        [
            "Manifest status set to `running` before model execution.",
            f"Source Git commit: `{manifest['source_git_commit']}`.",
            "The existing uncommitted meta-analysis entries are preserved.",
            f"Production Python: `{sys.executable}`.",
            f"GPU: {torch.cuda.get_device_name(0)}; free bytes before load: {free_bytes:,}.",
            "Model loading is restricted to the existing shared Hugging Face cache.",
        ],
    )
    return manifest


def mark_orchestrator_failure(stage: str, error: BaseException) -> None:
    if not MANIFEST_PATH.exists():
        return
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("status") != "successful":
        completed_at = utc_now()
        manifest["status"] = "failed"
        manifest["completed_at"] = completed_at
        manifest["failure_details"] = {
            "component": stage,
            "error_type": type(error).__name__,
            "message": str(error),
        }
        if manifest.get("execution_attempts"):
            manifest["execution_attempts"][-1].update(
                {
                    "status": "failed",
                    "completed_at": completed_at,
                    "component": stage,
                    "error_type": type(error).__name__,
                    "message": str(error),
                }
            )
        write_json(MANIFEST_PATH, manifest)
    append_log(
        "run failed",
        [f"Stage: `{stage}`.", f"{type(error).__name__}: {error}"],
    )


def run_stage(script_name: str) -> None:
    subprocess.run(
        [sys.executable, str(PIPELINE_DIR / script_name)],
        cwd=PROJECT_DIR,
        check=True,
    )


def main() -> int:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    stage = "initialization"
    try:
        initialize_manifest()
        stage = "capture"
        run_stage("r013_capture_hidden_states.py")
        append_log(
            "capture gate passed",
            [
                "All six anchor-position trajectories and deterministic replays passed.",
                "State 00 is exactly identical across all permutations.",
                "No response generation occurred.",
            ],
        )
        stage = "semantic_topology"
        run_stage("r013_semantic_topology.py")
        final_manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        if final_manifest.get("status") != "successful":
            raise RuntimeError("Topology stage returned without a successful manifest.")
        append_log(
            "run completed",
            [
                "All required capture, topology, invariance and completeness checks passed.",
                "Manifest status: `successful`.",
                "Semantic interpretation was not performed.",
            ],
        )
        print(
            json.dumps(
                {
                    "status": "successful",
                    "run_id": RUN_ID,
                    "manifest": str(MANIFEST_PATH),
                },
                indent=2,
            )
        )
        return 0
    except Exception as error:
        mark_orchestrator_failure(stage, error)
        print(
            json.dumps(
                {
                    "status": "failed",
                    "stage": stage,
                    "error_type": type(error).__name__,
                    "error": str(error),
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
