from torch import nn


def build_resnet(
    num_classes: int, freeze_backbone: bool, pretrained: bool = True
) -> nn.Module:
    """pretrained ResNet의 classifier를 교체해 반환합니다."""
    raise NotImplementedError("ResNet fine-tuning 구성을 구현하세요.")


def trainable_parameters(model: nn.Module) -> list[nn.Parameter]:
    """학습 가능한 parameter만 반환합니다."""
    raise NotImplementedError("Trainable parameter filtering을 구현하세요.")
