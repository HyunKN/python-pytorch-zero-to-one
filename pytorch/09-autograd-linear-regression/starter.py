import torch
from torch import nn


def train_linear_regression(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    epochs: int,
    learning_rate: float,
) -> tuple[nn.Module, list[float]]:
    """Linear regression 모델과 epoch별 loss를 반환합니다."""
    raise NotImplementedError("Linear regression 학습을 구현하세요.")
