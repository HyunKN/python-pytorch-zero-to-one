import tempfile
from pathlib import Path

import torch
from torch import nn

from exercise import (
    FashionMLP,
    build_synthetic_loader,
    evaluate,
    load_checkpoint,
    save_checkpoint,
    train_one_epoch,
)


def main() -> int:
    try:
        torch.manual_seed(0)
        model = FashionMLP()
        loader = build_synthetic_loader(32, 8)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        loss = train_one_epoch(
            model, loader, nn.CrossEntropyLoss(), optimizer, torch.device("cpu")
        )
        accuracy = evaluate(model, loader, torch.device("cpu"))
        assert loss > 0
        assert 0 <= accuracy <= 1
        assert model(torch.randn(2, 1, 28, 28)).shape == (2, 10)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.pt"
            save_checkpoint(model, path)
            restored = FashionMLP()
            load_checkpoint(restored, path, torch.device("cpu"))
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: FashionMNIST MLP smoke test")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
