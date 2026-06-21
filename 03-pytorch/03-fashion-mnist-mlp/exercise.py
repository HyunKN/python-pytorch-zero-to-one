from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


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


def build_synthetic_loader(sample_count: int, batch_size: int) -> DataLoader:
    """Network 없이 pipeline을 확인할 synthetic DataLoader를 만듭니다."""
    raise NotImplementedError("Synthetic DataLoader를 구현하세요.")


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    """전체 sample의 accuracy를 반환합니다."""
    raise NotImplementedError("Validation loop를 구현하세요.")


def save_checkpoint(model: nn.Module, path: Path) -> None:
    raise NotImplementedError("Checkpoint 저장을 구현하세요.")


def load_checkpoint(model: nn.Module, path: Path, device: torch.device) -> None:
    raise NotImplementedError("Checkpoint 불러오기를 구현하세요.")
