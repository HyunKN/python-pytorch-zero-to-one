import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


@torch.no_grad()
def evaluate_classifier(
    model: nn.Module, loader: DataLoader, device: torch.device, num_classes: int
) -> dict[str, object]:
    """Accuracy, class별 recall과 confusion matrix를 계산합니다."""
    model.eval()
    confusion = torch.zeros((num_classes, num_classes), dtype=torch.int64)

    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        predictions = model(inputs).argmax(dim=1)
        for true_label, predicted_label in zip(labels, predictions, strict=True):
            confusion[int(true_label), int(predicted_label)] += 1

    correct = int(confusion.diag().sum().item())
    total = int(confusion.sum().item())
    class_totals = confusion.sum(dim=1)
    class_recall = confusion.diag().float() / class_totals.clamp_min(1)
    return {
        "accuracy": correct / total,
        "class_recall": class_recall,
        "confusion_matrix": confusion,
    }


@torch.no_grad()
def collect_misclassified(
    model: nn.Module, loader: DataLoader, device: torch.device
) -> list[dict[str, object]]:
    """Confidence가 포함된 오분류 sample 정보를 수집합니다."""
    model.eval()
    mistakes: list[dict[str, object]] = []

    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        probabilities = model(inputs).softmax(dim=1)
        confidence, predictions = probabilities.max(dim=1)

        for index in range(len(labels)):
            if predictions[index] != labels[index]:
                mistakes.append(
                    {
                        "input": inputs[index].cpu(),
                        "true_label": int(labels[index].item()),
                        "predicted_label": int(predictions[index].item()),
                        "confidence": float(confidence[index].item()),
                    }
                )

    return sorted(mistakes, key=lambda item: item["confidence"], reverse=True)


def main() -> None:
    logits = torch.tensor(
        [[4.0, 1.0], [1.0, 4.0], [3.0, 2.0], [1.0, 5.0]]
    )
    labels = torch.tensor([0, 1, 1, 1])
    loader = DataLoader(TensorDataset(logits, labels), batch_size=2)
    model = nn.Identity()
    device = torch.device("cpu")

    metrics = evaluate_classifier(model, loader, device, num_classes=2)
    mistakes = collect_misclassified(model, loader, device)
    print("accuracy:", metrics["accuracy"])
    print("class recall:", metrics["class_recall"].tolist())
    print("confusion matrix:\n", metrics["confusion_matrix"])
    print("오분류 개수:", len(mistakes))


if __name__ == "__main__":
    main()
