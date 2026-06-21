from pathlib import Path

import numpy as np
import torch
from torch import nn


def export_to_onnx(
    model: nn.Module, sample_input: torch.Tensor, output_path: Path
) -> None:
    """PyTorch 모델을 ONNX 파일로 export합니다."""
    raise NotImplementedError("ONNX export를 구현하세요.")


def compare_outputs(
    pytorch_output: np.ndarray, onnx_output: np.ndarray
) -> dict[str, float]:
    """두 출력의 차이를 metric으로 반환합니다."""
    raise NotImplementedError("Output parity 계산을 구현하세요.")
