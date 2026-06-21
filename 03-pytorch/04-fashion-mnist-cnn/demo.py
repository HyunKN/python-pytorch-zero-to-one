import argparse
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms


class FashionCNN(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(), nn.Linear(32 * 7 * 7, 64), nn.ReLU(), nn.Linear(64, num_classes)
        )

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        return self.classifier(self.features(images))


def count_parameters(model: nn.Module) -> int:
    return sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad)


def build_synthetic_loader(sample_count: int, batch_size: int) -> DataLoader:
    generator = torch.Generator().manual_seed(0)
    images = torch.randn(sample_count, 1, 28, 28, generator=generator)
    labels = torch.randint(0, 10, (sample_count,), generator=generator)
    return DataLoader(TensorDataset(images, labels), batch_size=batch_size, shuffle=True)


def build_fashion_mnist_loaders(
    data_dir: Path, batch_size: int
) -> tuple[DataLoader, DataLoader]:
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
    )
    train_dataset = datasets.FashionMNIST(
        data_dir, train=True, download=True, transform=transform
    )
    validation_dataset = datasets.FashionMNIST(
        data_dir, train=False, download=True, transform=transform
    )
    return (
        DataLoader(train_dataset, batch_size=batch_size, shuffle=True),
        DataLoader(validation_dataset, batch_size=batch_size),
    )


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> float:
    model.train()
    loss_sum = 0.0
    sample_count = 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        loss = criterion(model(images), labels)
        loss.backward()
        optimizer.step()
        loss_sum += float(loss.item()) * labels.size(0)
        sample_count += labels.size(0)
    return loss_sum / sample_count


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    sample_count = 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        correct += int((model(images).argmax(1) == labels).sum().item())
        sample_count += labels.size(0)
    return correct / sample_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-data", action="store_true")
    parser.add_argument("--epochs", type=int, default=1)
    args = parser.parse_args()

    torch.manual_seed(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if args.full_data:
        train_loader, validation_loader = build_fashion_mnist_loaders(
            Path("data"), batch_size=64
        )
    else:
        train_loader = build_synthetic_loader(64, batch_size=16)
        validation_loader = build_synthetic_loader(32, batch_size=16)

    model = FashionCNN().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    print("학습 가능한 parameter 수:", count_parameters(model))
    for epoch in range(1, args.epochs + 1):
        loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        accuracy = evaluate(model, validation_loader, device)
        print(f"epoch={epoch} loss={loss:.4f} validation_accuracy={accuracy:.4f}")


if __name__ == "__main__":
    main()
