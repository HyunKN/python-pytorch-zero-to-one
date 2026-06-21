import tempfile
from pathlib import Path

import torch
from torch import nn

from exercise import compare_outputs, export_to_onnx, run_onnx


def main() -> int:
    try:
        torch.manual_seed(0)
        model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 3)).eval()
        sample = torch.randn(2, 4)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.onnx"
            export_to_onnx(model, sample, path)
            with torch.no_grad():
                pytorch_output = model(sample).numpy()
            onnx_output = run_onnx(path, sample.numpy())
        comparison = compare_outputs(pytorch_output, onnx_output)
        assert comparison["parity"]
        assert comparison["max_absolute_difference"] < 1e-5
        zero_comparison = compare_outputs(
            torch.zeros(1, 3).numpy(), torch.ones(1, 3).numpy()
        )
        assert zero_comparison["cosine_similarity"] == 0.0
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: ONNX Export와 Parity")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
