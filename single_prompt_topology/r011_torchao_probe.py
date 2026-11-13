from __future__ import annotations

import argparse
import json
import platform
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify CPU int4 execution and Transformers integration for R011."
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = {
        "probe": "torchao_cpu_int4_transformers_integration",
        "status": "running",
        "started_at": datetime.now(timezone.utc).isoformat(),
        "completed_at": None,
        "python": sys.version,
        "platform": platform.platform(),
        "model_loaded": False,
        "supports_intermediate_hidden_states": None,
    }

    try:
        import torch
        import torchao
        import transformers
        from torchao.dtypes import Int4CPULayout
        from torchao.quantization import Int4WeightOnlyConfig, quantize_
        from transformers import TorchAoConfig

        torch.manual_seed(11)
        module = torch.nn.Sequential(torch.nn.Linear(128, 128, bias=False)).eval()
        quant_type = Int4WeightOnlyConfig(group_size=128, layout=Int4CPULayout())
        quantize_(module, quant_type)

        sample = torch.randn(2, 128, dtype=torch.float32)
        with torch.inference_mode():
            output = module(sample)

        transformers_config = TorchAoConfig(quant_type=quant_type)
        quantized_weight = module[0].weight
        finite = bool(torch.isfinite(output).all().item())
        report.update(
            {
                "status": "successful" if finite else "failed",
                "torch": torch.__version__,
                "torchao": torchao.__version__,
                "transformers": transformers.__version__,
                "quantization": {
                    "config": type(quant_type).__name__,
                    "layout": type(quant_type.layout).__name__,
                    "group_size": quant_type.group_size,
                    "weight_type": type(quantized_weight).__name__,
                    "weight_shape": list(quantized_weight.shape),
                },
                "forward": {
                    "input_shape": list(sample.shape),
                    "output_shape": list(output.shape),
                    "output_dtype": str(output.dtype),
                    "finite": finite,
                },
                "transformers_config": type(transformers_config).__name__,
                "interpretation": (
                    "CPU int4 execution and Transformers quantization configuration "
                    "succeeded; a same-architecture model capture is still required."
                ),
            }
        )
    except Exception as error:
        report.update(
            {
                "status": "failed",
                "error_type": type(error).__name__,
                "error": str(error),
                "traceback": traceback.format_exc(),
                "interpretation": (
                    "The installed TorchAO fallback did not provide a usable x86 CPU "
                    "int4 execution path; no model was loaded."
                ),
            }
        )

    report["completed_at"] = datetime.now(timezone.utc).isoformat()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["status"] == "successful" else 1


if __name__ == "__main__":
    raise SystemExit(main())
