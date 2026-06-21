import tempfile
from collections.abc import Callable
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms


class ImageClassificationDataset(Dataset):
    def __init__(
        self,
        samples: list[tuple[Path, int]],
        transform: Callable[[Image.Image], torch.Tensor],
    ) -> None:
        if not samples:
            raise ValueError("samples는 비어 있을 수 없습니다.")
        self.samples = samples
        self.transform = transform

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, int]:
        path, label = self.samples[index]
        with Image.open(path) as image:
            rgb_image = image.convert("RGB")
            tensor = self.transform(rgb_image)
        return tensor, label


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        first = root / "red.png"
        second = root / "blue.png"
        Image.new("RGB", (16, 16), color="red").save(first)
        Image.new("RGB", (16, 16), color="blue").save(second)

        dataset = ImageClassificationDataset(
            [(first, 0), (second, 1)], transform=transforms.ToTensor()
        )
        loader = DataLoader(dataset, batch_size=2, shuffle=False)
        images, labels = next(iter(loader))

    print("batch image shape:", tuple(images.shape))
    print("batch labels:", labels.tolist())


if __name__ == "__main__":
    main()
