import torch
from torch import nn

from exercise import FashionCNN, build_synthetic_loader, count_parameters, train_one_epoch


def main() -> int:
    try:
        torch.manual_seed(0)
        model = FashionCNN()
        loader = build_synthetic_loader(16, 8)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        loss = train_one_epoch(
            model, loader, nn.CrossEntropyLoss(), optimizer, torch.device("cpu")
        )
        assert loss > 0
        assert model(torch.randn(2, 1, 28, 28)).shape == (2, 10)
        assert count_parameters(model) > 0
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: FashionMNIST CNN smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
