import torch
from torch import nn
from torch.utils.data import DataLoader


class FashionMLP(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        raise NotImplementedError("MLP layer를 정의하세요.")

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError("Forward pass를 구현하세요.")


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> float:
    """한 epoch의 평균 loss를 반환합니다."""
    raise NotImplementedError("Training loop를 구현하세요.")
