"""Configuration-driven Transformer State Topology Pipeline.

TSTP generalises the complete R020 autoregressive measurement workflow while
keeping architecture access behind explicit adapters. Semantic interpretation
remains outside this module.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import platform
import sys
import time
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import networkx as nx
import numpy as np
import pandas as pd
import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

import r020_pythia_generation_topology as measured
import topology_core as topology
from tstp.adapters import ArchitectureAdapter, get_adapter
from tstp.capture import generate_capture


PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
SIDES = measured.SIDES
COMPONENTS = measured.COMPONENTS


@dataclass(frozen=True)
class Context:
    config_path: Path
    config: dict[str, Any]
    run_dir: Path
    raw_dir: Path
    controls_dir: Path
    snapshot_dir: Path
    manifest_path: Path
    settings: topology.TopologySettings
    state_labels: tuple[str, ...]
    adapter: ArchitectureAdapter


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _adapter_name(model: dict[str, Any]) -> str:
    explicit = model.get("adapter")
    if explicit:
        return str(explicit)
    architecture = str(model.get("architecture", ""))
    legacy_defaults = {
        "GPTNeoXForCausalLM": "pythia",
        "Qwen2ForCausalLM": "qwen2",
    }
    try:
        return legacy_defaults[architecture]
    except KeyError as error:
        raise ValueError(
            "model.adapter is required when the architecture has no safe legacy default."
        ) from error


def load_context(config_path: Path) -> Context:
    config_path = config_path.resolve()
    config = load_json(config_path)
    if int(config.get("schema_version", -1)) != 1:
        raise ValueError("TSTP requires configuration schema_version 1.")
    run_number = int(config.get("run_number", -1))
    run_id = str(config.get("run_id", ""))
    if run_number < 1 or not run_id.startswith(f"R{run_number:03d}_"):
        raise ValueError("run_id and run_number do not agree.")
    run_dir = (PROJECT_ROOT / str(config["run_directory"])).resolve()
    expected_runs_root = (PIPELINE_DIR / "runs").resolve()
    if run_dir.parent != expected_runs_root or run_dir.name != run_id:
        raise ValueError("run_directory must be runs/<run_id>.")
    if config_path.parent != run_dir:
        raise ValueError("The TSTP configuration must reside inside its run directory.")

    prompt = str(config["prompt"]["text"])
    if sha256_bytes(prompt.encode("utf-8")) != config["prompt"]["utf8_sha256"]:
        raise ValueError("Prompt UTF-8 hash does not match the configuration.")
    if config["prompt"].get("chat_template_used"):
        raise ValueError("TSTP schema 1 does not permit a chat template.")
    if config["generation"].get("do_sample"):
        raise ValueError("TSTP schema 1 requires deterministic greedy decoding.")
    if config["generation"].get("use_cache"):
        raise ValueError("TSTP requires inspectable full-prefix forwards.")
    max_new_tokens = int(config["generation"]["max_new_tokens"])
    if not 1 <= max_new_tokens <= 256:
        raise ValueError("max_new_tokens must be between 1 and 256.")

    configured_top_count = int(config["topology"]["top_tokens_per_sector"])
    required_overlap = int(
        config["capture"]["reconciliation_required_top_token_overlap"]
    )
    if required_overlap != configured_top_count:
        raise ValueError("The full top-token set must be used for reconciliation.")

    model = config["model"]
    adapter = get_adapter(_adapter_name(model))
    architecture = str(model["architecture"])
    if architecture not in adapter.architecture_names:
        raise ValueError(
            f"Adapter {adapter.name!r} does not support architecture {architecture!r}."
        )
    snapshot_dir = Path(str(model["snapshot_path"])).resolve()
    if not snapshot_dir.is_dir():
        raise FileNotFoundError(f"Frozen model snapshot is missing: {snapshot_dir}")
    if not any(
        (snapshot_dir / name).is_file()
        for name in ("model.safetensors", "model.safetensors.index.json")
    ):
        raise FileNotFoundError("Frozen Safetensors weights or index are missing.")
    model_config = AutoConfig.from_pretrained(snapshot_dir, local_files_only=True)
    observed_architectures = list(model_config.architectures or [])
    if architecture not in observed_architectures:
        raise RuntimeError(f"Unexpected architecture: {observed_architectures}")
    layer_count = int(model_config.num_hidden_layers)
    hidden_width = int(model_config.hidden_size)
    if layer_count != int(model["expected_layer_count"]):
        raise RuntimeError("Model layer count differs from the frozen contract.")
    if hidden_width != int(model["expected_hidden_width"]):
        raise RuntimeError("Model hidden width differs from the frozen contract.")
    state_count = layer_count + 2
    if state_count != int(config["capture"]["expected_state_count"]):
        raise RuntimeError("Recorded-state count differs from the frozen contract.")
    device = str(model["device"])
    if device.startswith("cuda") and not torch.cuda.is_available():
        raise RuntimeError("The configured CUDA device is unavailable.")
    settings = topology.TopologySettings(
        state_count=state_count,
        layer_count=layer_count,
        k_neighbors=int(config["topology"]["k_neighbors"]),
        knn_batch_size=int(config["topology"]["knn_batch_size"]),
        random_seed=int(config["topology"]["random_seed"]),
        louvain_resolution=float(config["topology"]["louvain_resolution"]),
        device=device,
    )
    labels = tuple(topology.state_label(index, settings) for index in range(state_count))
    return Context(
        config_path=config_path,
        config=config,
        run_dir=run_dir,
        raw_dir=run_dir / "local_raw_capture",
        controls_dir=run_dir / "controls",
        snapshot_dir=snapshot_dir,
        manifest_path=run_dir / "manifest.json",
        settings=settings,
        state_labels=labels,
        adapter=adapter,
    )


def _initial_input_names(context: Context) -> set[str]:
    configured = set(map(str, context.config.get("initial_files", [])))
    configured.add(context.config_path.name)
    return configured


def initialize_manifest(context: Context) -> dict[str, Any]:
    if context.manifest_path.exists():
        raise FileExistsError("TSTP manifest already exists; refusing to overwrite the run.")
    allowed = _initial_input_names(context)
    unexpected = [path.name for path in context.run_dir.iterdir() if path.name not in allowed]
    if unexpected:
        raise FileExistsError(f"Stale TSTP output or undeclared input exists: {unexpected}")
    context.raw_dir.mkdir(parents=True, exist_ok=False)
    context.controls_dir.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema_version": 1,
        "pipeline": "Transformer State Topology Pipeline",
        "pipeline_abbreviation": "TSTP",
        "run_id": context.config["run_id"],
        "run_number": int(context.config["run_number"]),
        "started_at": utc_now(),
        "run_status": "running",
        "measurement_status": "running",
        "analysis_required": True,
        "analysis_status": "not_started",
        "config": {
            "relative_path": context.config_path.name,
            "sha256": sha256_file(context.config_path),
        },
        "model": {**context.config["model"], "adapter": context.adapter.name},
        "prompt_sha256": context.config["prompt"]["utf8_sha256"],
        "required_components": list(COMPONENTS),
        "components": {name: {"status": "pending"} for name in COMPONENTS},
        "failure_details": None,
    }
    write_json(context.manifest_path, manifest)
    return manifest


def update_component(
    context: Context,
    name: str,
    started_at: str,
    started: float,
    **details: object,
) -> None:
    manifest = load_json(context.manifest_path)
    manifest["components"][name] = {
        "status": "successful",
        "started_at": started_at,
        "completed_at": utc_now(),
        "elapsed_seconds": time.perf_counter() - started,
        **details,
    }
    write_json(context.manifest_path, manifest)


def fail_measurement(context: Context, component: str, error: BaseException) -> None:
    if not context.manifest_path.exists():
        return
    manifest = load_json(context.manifest_path)
    manifest["run_status"] = "measurement_failed"
    manifest["measurement_status"] = "measurement_failed"
    manifest["analysis_status"] = "not_started"
    manifest["failed_at"] = utc_now()
    manifest["failure_details"] = {
        "component": component,
        "error_type": type(error).__name__,
        "message": str(error),
        "traceback": traceback.format_exc(),
        "memory_at_failure": measured.memory_snapshot(),
    }
    manifest["components"][component] = {
        "status": "failed",
        "completed_at": utc_now(),
        "error_type": type(error).__name__,
        "message": str(error),
    }
    write_json(context.manifest_path, manifest)


def _torch_dtype(name: str) -> torch.dtype:
    values = {
        "float32": torch.float32,
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
    }
    try:
        return values[name]
    except KeyError as error:
        raise ValueError(f"Unsupported model dtype: {name!r}") from error


def load_model(context: Context) -> tuple[Any, Any]:
    tokenizer = AutoTokenizer.from_pretrained(context.snapshot_dir, local_files_only=True)
    options: dict[str, Any] = {
        "local_files_only": True,
        "dtype": _torch_dtype(str(context.config["model"]["dtype"])),
        "trust_remote_code": False,
    }
    if implementation := context.config["model"].get("attn_implementation"):
        options["attn_implementation"] = str(implementation)
    model = AutoModelForCausalLM.from_pretrained(context.snapshot_dir, **options)
    model.to(str(context.config["model"]["device"]))
    model.eval()
    context.adapter.validate_model(model)
    if type(model).__name__ != context.config["model"]["architecture"]:
        raise RuntimeError(f"Loaded unexpected model class: {type(model).__name__}")
    embeddings = model.get_input_embeddings().weight
    output = model.get_output_embeddings().weight
    expected_shape = (
        int(context.config["model"]["expected_embedding_rows"]),
        int(context.config["model"]["expected_hidden_width"]),
    )
    if tuple(embeddings.shape) != expected_shape:
        raise RuntimeError(f"Unexpected input embedding shape: {tuple(embeddings.shape)}")
    if tuple(output.shape) != tuple(embeddings.shape):
        raise RuntimeError("Output head shape differs from the input embedding shape.")
    return model, tokenizer


def model_metadata(context: Context, model: Any, tokenizer: Any) -> dict[str, Any]:
    import huggingface_hub
    import safetensors
    import sklearn
    import transformers

    files = {
        path.name: {"bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in sorted(context.snapshot_dir.iterdir())
        if path.is_file()
    }
    return {
        "schema_version": 1,
        "recorded_at": utc_now(),
        "pipeline": "TSTP",
        "model_id": context.config["model"]["id"],
        "revision": context.config["model"]["revision"],
        "snapshot_path": str(context.snapshot_dir),
        **context.adapter.metadata(model),
        "input_output_embeddings_tied": bool(
            model.get_input_embeddings().weight.data_ptr()
            == model.get_output_embeddings().weight.data_ptr()
        ),
        "tokenizer_class": type(tokenizer).__name__,
        "tokenizer_length": len(tokenizer),
        "tokenizer_special_ids": list(map(int, tokenizer.all_special_ids)),
        "files": files,
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "safetensors": safetensors.__version__,
            "huggingface_hub": huggingface_hub.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "networkx": nx.__version__,
            "sklearn": sklearn.__version__,
            "cuda": torch.version.cuda,
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        },
    }


def capture(context: Context, model: Any, tokenizer: Any) -> dict[str, Any]:
    return generate_capture(
        model,
        tokenizer,
        context.adapter,
        context.config["prompt"]["text"],
        device=str(context.config["model"]["device"]),
        max_new_tokens=int(context.config["generation"]["max_new_tokens"]),
        add_special_tokens=bool(context.config["prompt"].get("add_special_tokens", False)),
    )


def _report_names(context: Context) -> tuple[str, str]:
    prefix = f"R{int(context.config['run_number']):03d}"
    return (
        f"{prefix}_MEASUREMENT_COMPLETENESS_VERIFICATION.md",
        f"{prefix}_MEASUREMENT_REPORT.md",
    )


def write_reports(context: Context, results: dict[str, Any]) -> None:
    verification_name, report_name = _report_names(context)
    verification = [
        f"# {context.config['run_id']} measurement completeness verification",
        "",
        "- Pipeline: **Transformer State Topology Pipeline (TSTP)**",
        "- Measurement status: **PASS**",
        f"- Adapter: `{context.adapter.name}`",
        f"- Generated-token decisions: {results['generated_token_count']}",
        f"- Recorded states per decision: {results['recorded_state_count']}",
        f"- Networks: {results['network_count']}",
        f"- Replay generated tokens exact: {results['replay_generated_tokens_exact']}",
        f"- Replay hidden states exact: {results['replay_hidden_states_exact']}",
        f"- Replay logits exact: {results['replay_logits_exact']}",
        "- Semantic reconstruction remains outside TSTP.",
    ]
    (context.run_dir / verification_name).write_text(
        "\n".join(verification) + "\n", encoding="utf-8"
    )
    report = [
        f"# {context.config['run_id']} TSTP measurement report",
        "",
        "## Outcome",
        "",
        "Intermediate-state capture, deterministic replay, vocabulary projection, topology construction and measured exports completed and validated.",
        "",
        "**Overall run status: awaiting semantic analysis.**",
        "",
        "## Run identity",
        "",
        f"- Model: `{context.config['model']['id']}`",
        f"- Revision: `{context.config['model']['revision']}`",
        f"- Architecture adapter: `{context.adapter.name}`",
        f"- Prompt hash: `{context.config['prompt']['utf8_sha256']}`",
        f"- Generated-token decisions: {results['generated_token_count']}",
        f"- Recorded states per decision: {results['recorded_state_count']}",
        "",
        "## Coverage",
        "",
        f"- Networks: {results['network_count']}",
        f"- Selected token memberships: {results['selected_membership_rows']:,}",
        f"- Directed edges: {results['directed_edge_rows']:,}",
        f"- State-local communities: {results['state_local_community_count']:,}",
        "",
        "## Interpretation boundary",
        "",
        "TSTP measures changing vocabulary neighbourhoods, graph partitions and transitions. It does not assign semantic topics, parent structures or causal interpretations.",
    ]
    (context.run_dir / report_name).write_text(
        "\n".join(report) + "\n", encoding="utf-8"
    )


def measure(context: Context) -> None:
    measured.set_deterministic_runtime(int(context.config["topology"]["random_seed"]))
    initialize_manifest(context)
    component = "model_identity"
    model = None
    tokenizer = None
    normalized_embeddings = None
    try:
        started_at = utc_now()
        started = time.perf_counter()
        torch.cuda.reset_peak_memory_stats()
        model, tokenizer = load_model(context)
        metadata = model_metadata(context, model, tokenizer)
        write_json(context.run_dir / "model_metadata.json", metadata)
        weight_hashes = {
            name: record["sha256"]
            for name, record in metadata["files"].items()
            if name.endswith(".safetensors")
        }
        update_component(
            context,
            component,
            started_at,
            started,
            adapter=context.adapter.name,
            revision=context.config["model"]["revision"],
            weight_file_sha256=weight_hashes,
            state_labels=list(context.state_labels),
            memory_after_load=measured.memory_snapshot(),
        )

        component = "primary_capture"
        started_at = utc_now()
        started = time.perf_counter()
        primary = capture(context, model, tokenizer)
        update_component(
            context,
            component,
            started_at,
            started,
            generated_token_count=len(primary["generated_ids"]),
            stop_reason=primary["stop_reason"],
            decision_state_shape=list(primary["decision_states"].shape),
            full_sequence_state_shape=list(primary["full_sequence_states"].shape),
            peak_gpu_allocated_bytes=int(torch.cuda.max_memory_allocated()),
        )

        component = "deterministic_replay"
        started_at = utc_now()
        started = time.perf_counter()
        replay = capture(context, model, tokenizer)
        validation = measured.write_capture_artifacts(context, tokenizer, primary, replay)
        update_component(context, component, started_at, started, **validation["replay"])

        component = "projection_and_cutoffs"
        started_at = utc_now()
        started = time.perf_counter()
        normalized_embeddings, memberships, vocabulary = measured.project_and_select(
            context, model, tokenizer, primary, replay
        )
        update_component(
            context,
            component,
            started_at,
            started,
            **vocabulary["projection_record"],
            cutoff_rows=len(pd.read_csv(context.run_dir / "cutoffs.csv")),
            top_token_rows=len(
                pd.read_csv(context.run_dir / "top_tokens_by_step_and_state.csv")
            ),
        )
        del primary, replay, model
        model = None
        gc.collect()
        torch.cuda.empty_cache()

        component = "networks_and_communities"
        started_at = utc_now()
        started = time.perf_counter()
        network_details, export_details = measured.construct_networks(
            context, normalized_embeddings, memberships, vocabulary
        )
        update_component(context, component, started_at, started, **network_details)
        update_component(
            context,
            "shuffled_control",
            started_at,
            started,
            mapping_rows=export_details["mapping_rows"],
            mapping_sha256=export_details["mapping_sha256"],
            control_networks=export_details["control_networks"],
            control_json_sha256=export_details["control_json_sha256"],
        )
        update_component(
            context,
            "measured_exports",
            started_at,
            started,
            chatgpt_networks=export_details["chatgpt_networks"],
            chatgpt_json_sha256=export_details["chatgpt_json_sha256"],
            semantic_labels_added=False,
        )

        component = "resource_cleanup"
        started_at = utc_now()
        started = time.perf_counter()
        del normalized_embeddings, memberships, vocabulary, tokenizer
        normalized_embeddings = None
        tokenizer = None
        gc.collect()
        torch.cuda.empty_cache()
        torch.cuda.synchronize()
        update_component(
            context,
            component,
            started_at,
            started,
            memory_after_cleanup=measured.memory_snapshot(),
        )

        component = "completeness_validation"
        started_at = utc_now()
        started = time.perf_counter()
        results = measured.validate_outputs(context, write_reports=False)
        write_json(context.run_dir / "measurement_results.json", results)
        write_reports(context, results)
        update_component(context, component, started_at, started, **results)
        index = measured.build_artifact_index(context)
        manifest = load_json(context.manifest_path)
        for name in COMPONENTS:
            if manifest["components"].get(name, {}).get("status") != "successful":
                raise RuntimeError(f"Required component is not successful: {name}")
        manifest["measurement_status"] = "measurement_successful"
        manifest["analysis_status"] = "not_started"
        manifest["run_status"] = "awaiting_semantic_analysis"
        manifest["measurement_completed_at"] = utc_now()
        manifest["failure_details"] = None
        manifest["results"] = results
        manifest["artifact_index"] = {
            "relative_path": "artifact_index.json",
            "bytes": (context.run_dir / "artifact_index.json").stat().st_size,
            "sha256": sha256_file(context.run_dir / "artifact_index.json"),
            "indexed_artifact_count": len(index["artifacts"]),
        }
        write_json(context.manifest_path, manifest)
    except BaseException as error:
        try:
            if model is not None:
                del model
            if tokenizer is not None:
                del tokenizer
            if normalized_embeddings is not None:
                del normalized_embeddings
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        finally:
            fail_measurement(context, component, error)
        raise


def verify(context: Context) -> dict[str, Any]:
    if not context.manifest_path.is_file():
        raise FileNotFoundError("TSTP manifest is missing.")
    manifest = load_json(context.manifest_path)
    if manifest.get("measurement_status") != "measurement_successful":
        raise RuntimeError("TSTP measurement is not successful.")
    index_path = context.run_dir / "artifact_index.json"
    index = load_json(index_path)
    if sha256_file(index_path) != manifest["artifact_index"]["sha256"]:
        raise RuntimeError("Artifact-index hash differs from the manifest.")
    for relative, record in index["artifacts"].items():
        path = context.run_dir / relative
        if not path.is_file() or path.stat().st_size != int(record["bytes"]):
            raise RuntimeError(f"Indexed artifact changed or is missing: {relative}")
        if sha256_file(path) != record["sha256"]:
            raise RuntimeError(f"Indexed artifact hash changed: {relative}")
    results = measured.validate_outputs(context, write_reports=False)
    if results != manifest["results"]:
        raise RuntimeError("Recomputed completeness results differ from the manifest.")
    return {
        "status": "PASS",
        "pipeline": "TSTP",
        "adapter": context.adapter.name,
        "run_id": context.config["run_id"],
        "artifact_count": len(index["artifacts"]),
        **results,
    }


def preflight(context: Context) -> dict[str, Any]:
    measured.set_deterministic_runtime(int(context.config["topology"]["random_seed"]))
    model, tokenizer = load_model(context)
    try:
        result = generate_capture(
            model,
            tokenizer,
            context.adapter,
            context.config["prompt"]["text"],
            device=str(context.config["model"]["device"]),
            max_new_tokens=1,
            add_special_tokens=bool(
                context.config["prompt"].get("add_special_tokens", False)
            ),
        )
        return {
            "status": "PASS",
            "scientific_evidence_written": False,
            "adapter": context.adapter.name,
            "architecture": type(model).__name__,
            "decision_state_shape": list(result["decision_states"].shape),
            "full_sequence_state_shape": list(result["full_sequence_states"].shape),
            "logit_shape": list(result["decision_logits"].shape),
            "selected_token_id": int(result["generated_ids"][0]),
            "state_labels": list(context.adapter.state_labels(model)),
        }
    finally:
        del model, tokenizer
        gc.collect()
        torch.cuda.empty_cache()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=("validate-config", "preflight", "measure", "verify")
    )
    parser.add_argument("--config", required=True, type=Path)
    arguments = parser.parse_args()
    context = load_context(arguments.config)
    if arguments.action == "validate-config":
        print(
            json.dumps(
                {
                    "status": "valid",
                    "pipeline": "TSTP",
                    "run_id": context.config["run_id"],
                    "adapter": context.adapter.name,
                    "model_revision": context.config["model"]["revision"],
                    "state_labels": list(context.state_labels),
                    "prompt_sha256": context.config["prompt"]["utf8_sha256"],
                    "run_directory_exists": context.run_dir.is_dir(),
                    "manifest_exists": context.manifest_path.exists(),
                },
                indent=2,
            )
        )
    elif arguments.action == "preflight":
        print(json.dumps(preflight(context), indent=2))
    elif arguments.action == "measure":
        measure(context)
    else:
        print(json.dumps(verify(context), indent=2))


if __name__ == "__main__":
    main()
