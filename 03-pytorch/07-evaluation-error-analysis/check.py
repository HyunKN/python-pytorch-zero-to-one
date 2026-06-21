import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from exercise import collect_misclassified, evaluate_classifier


def main() -> int:
    try:
        logits = torch.tensor(
            [[4.0, 1.0], [1.0, 4.0], [3.0, 2.0], [1.0, 5.0]]
        )
        labels = torch.tensor([0, 1, 1, 1])
        loader = DataLoader(TensorDataset(logits, labels), batch_size=2)
        metrics = evaluate_classifier(nn.Identity(), loader, torch.device("cpu"), 2)
        mistakes = collect_misclassified(nn.Identity(), loader, torch.device("cpu"))
        assert metrics["accuracy"] == 0.75
        torch.testing.assert_close(
            metrics["confusion_matrix"], torch.tensor([[1, 0], [1, 2]])
        )
        assert len(mistakes) == 1
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: 평가와 Error Analysis")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
