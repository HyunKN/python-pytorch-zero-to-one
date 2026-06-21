from pathlib import Path

import numpy as np
import onnxruntime as ort
import torch
from torch import nn


def export_to_onnx(
    model: nn.Module, sample_input: torch.Tensor, output_path: Path
) -> None:
    """PyTorch 모델을 ONNX 파일로 export합니다."""
    raise NotImplementedError("ONNX export를 구현하세요.")


def compare_outputs(
    pytorch_output: np.ndarray,
    onnx_output: np.ndarray,
    absolute_tolerance: float = 1e-5,
) -> dict[str, float | bool]:
    """두 출력의 차이를 metric으로 반환합니다."""
    raise NotImplementedError("Output parity 계산을 구현하세요.")


def run_onnx(model_path: Path, input_array: np.ndarray) -> np.ndarray:
    """ONNX Runtime inference 결과를 반환합니다."""
    raise NotImplementedError("ONNX Runtime inference를 구현하세요.")
