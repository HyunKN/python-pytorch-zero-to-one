import torch
from torch import nn
from torchvision.models import ResNet18_Weights, resnet18


def build_resnet(
    num_classes: int, freeze_backbone: bool, pretrained: bool = True
) -> nn.Module:
    """ResNet18 backbone과 새 classifier를 구성합니다."""
    weights = ResNet18_Weights.DEFAULT if pretrained else None
    model = resnet18(weights=weights)

    if freeze_backbone:
        for parameter in model.parameters():
            parameter.requires_grad = False

    input_features = model.fc.in_features
    model.fc = nn.Linear(input_features, num_classes)
    return model


def trainable_parameters(model: nn.Module) -> list[nn.Parameter]:
    return [parameter for parameter in model.parameters() if parameter.requires_grad]


def main() -> None:
    model = build_resnet(num_classes=3, freeze_backbone=True, pretrained=False)
    sample_images = torch.randn(2, 3, 64, 64)
    logits = model(sample_images)

    print("classifier:", model.fc)
    print("output shape:", tuple(logits.shape))
    print("학습 가능한 parameter Tensor 수:", len(trainable_parameters(model)))
    print("실제 fine-tuning에서는 pretrained=True로 실행하세요.")


if __name__ == "__main__":
    main()
