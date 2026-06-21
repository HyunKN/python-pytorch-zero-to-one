import argparse
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms


class FashionMLP(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes),
        )

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        return self.layers(images)


def build_synthetic_loader(sample_count: int, batch_size: int) -> DataLoader:
    """Network 없이 pipeline을 확인하기 위한 고정 synthetic dataset을 만듭니다."""
    generator = torch.Generator().manual_seed(0)
    images = torch.randn(sample_count, 1, 28, 28, generator=generator)
    labels = torch.randint(0, 10, (sample_count,), generator=generator)
    return DataLoader(TensorDataset(images, labels), batch_size=batch_size, shuffle=True)


def build_fashion_mnist_loaders(
    data_dir: Path, batch_size: int
) -> tuple[DataLoader, DataLoader]:
    """FashionMNIST train/test loader를 만들며 최초 실행 시 data를 download합니다."""
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
        logits = model(images)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        batch_size = labels.size(0)
        loss_sum += float(loss.item()) * batch_size
        sample_count += batch_size

    return loss_sum / sample_count


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    sample_count = 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        predictions = model(images).argmax(dim=1)
        correct += int((predictions == labels).sum().item())
        sample_count += labels.size(0)

    return correct / sample_count


def save_checkpoint(model: nn.Module, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), path)


def load_checkpoint(model: nn.Module, path: Path, device: torch.device) -> None:
    state_dict = torch.load(path, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full-data",
        action="store_true",
        help="Synthetic data 대신 FashionMNIST를 download해 학습합니다.",
    )
    parser.add_argument("--epochs", type=int, default=1)
    args = parser.parse_args()

    torch.manual_seed(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if args.full_data:
        train_loader, validation_loader = build_fashion_mnist_loaders(
            Path("data"), batch_size=64
        )
    else:
        train_loader = build_synthetic_loader(128, batch_size=32)
        validation_loader = build_synthetic_loader(64, batch_size=32)

    model = FashionMLP().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    for epoch in range(1, args.epochs + 1):
        loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        accuracy = evaluate(model, validation_loader, device)
        print(f"epoch={epoch} loss={loss:.4f} validation_accuracy={accuracy:.4f}")

    checkpoint = Path("artifacts/fashion_mlp.pt")
    save_checkpoint(model, checkpoint)
    print("checkpoint 저장:", checkpoint)


if __name__ == "__main__":
    main()
