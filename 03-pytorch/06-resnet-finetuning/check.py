import torch

from exercise import build_resnet, trainable_parameters


def main() -> int:
    try:
        model = build_resnet(3, freeze_backbone=True, pretrained=False)
        assert model.fc.out_features == 3
        assert model.fc.weight.requires_grad
        assert not model.conv1.weight.requires_grad
        assert model(torch.randn(1, 3, 64, 64)).shape == (1, 3)
        assert trainable_parameters(model)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: ResNet Fine-tuning smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
