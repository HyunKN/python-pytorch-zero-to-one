from pathlib import Path

import numpy as np
import onnxruntime as ort
import torch
from torch import nn


def export_to_onnx(
    model: nn.Module, sample_input: torch.Tensor, output_path: Path
) -> None:
    """PyTorch 모델을 dynamic batch를 지원하는 ONNX로 export합니다."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    model.eval()
    torch.onnx.export(
        model,
        sample_input,
        str(output_path),
        export_params=True,
        opset_version=18,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
    )


def run_onnx(model_path: Path, input_array: np.ndarray) -> np.ndarray:
    """ONNX Runtime CPU provider로 inference한 첫 번째 output을 반환합니다."""
    session = ort.InferenceSession(
        str(model_path), providers=["CPUExecutionProvider"]
    )
    input_name = session.get_inputs()[0].name
    return session.run(None, {input_name: input_array.astype(np.float32)})[0]


def compare_outputs(
    pytorch_output: np.ndarray,
    onnx_output: np.ndarray,
    absolute_tolerance: float = 1e-5,
) -> dict[str, float | bool]:
    """두 output의 max difference, cosine similarity와 parity를 반환합니다."""
    if pytorch_output.shape != onnx_output.shape:
        raise ValueError("두 output shape가 같아야 합니다.")

    first = pytorch_output.astype(np.float64).ravel()
    second = onnx_output.astype(np.float64).ravel()
    first_norm = np.linalg.norm(first)
    second_norm = np.linalg.norm(second)
    denominator = first_norm * second_norm
    if denominator == 0:
        cosine_similarity = 1.0 if first_norm == 0 and second_norm == 0 else 0.0
    else:
        cosine_similarity = float(first @ second / denominator)
    max_difference = float(np.max(np.abs(first - second)))
    parity = bool(np.allclose(first, second, atol=absolute_tolerance, rtol=1e-5))
    return {
        "max_absolute_difference": max_difference,
        "cosine_similarity": cosine_similarity,
        "parity": parity,
    }


def main() -> None:
    torch.manual_seed(0)
    model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 3)).eval()
    sample = torch.randn(2, 4)
    output_path = Path("artifacts/demo_model.onnx")
    export_to_onnx(model, sample, output_path)

    with torch.no_grad():
        pytorch_output = model(sample).numpy()
    onnx_output = run_onnx(output_path, sample.numpy())
    comparison = compare_outputs(pytorch_output, onnx_output)

    print("ONNX 파일:", output_path)
    print("PyTorch output shape:", pytorch_output.shape)
    print("ONNX output shape:", onnx_output.shape)
    print("Parity 결과:", comparison)


if __name__ == "__main__":
    main()
