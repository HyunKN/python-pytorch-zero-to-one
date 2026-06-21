import torch
from torch import nn


class FashionCNN(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        raise NotImplementedError("CNN layer를 정의하세요.")

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("CNN forward pass를 구현하세요.")


def count_parameters(model: nn.Module) -> int:
    """학습 가능한 parameter 수를 반환합니다."""
    raise NotImplementedError("Parameter 수 계산을 구현하세요.")
