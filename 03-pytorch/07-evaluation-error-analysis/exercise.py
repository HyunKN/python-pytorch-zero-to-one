import torch
from torch import nn
from torch.utils.data import DataLoader


def evaluate_classifier(
    model: nn.Module, loader: DataLoader, device: torch.device, num_classes: int
) -> dict[str, object]:
    """Accuracy, class별 recall과 confusion matrix를 반환합니다."""
    raise NotImplementedError("Classifier 평가를 구현하세요.")


def collect_misclassified(
    model: nn.Module, loader: DataLoader, device: torch.device
) -> list[dict[str, object]]:
    """오분류 sample 정보를 반환합니다."""
    raise NotImplementedError("Error analysis용 sample 수집을 구현하세요.")
