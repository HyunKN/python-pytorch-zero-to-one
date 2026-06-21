import tempfile
from pathlib import Path

from PIL import Image
from torchvision import transforms

from exercise import ImageClassificationDataset


def main() -> int:
    try:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.png"
            Image.new("RGB", (8, 8), color="red").save(path)
            dataset = ImageClassificationDataset(
                [(path, 0)], transform=transforms.ToTensor()
            )
            image, label = dataset[0]
        assert len(dataset) == 1
        assert image.shape == (3, 8, 8)
        assert label == 0
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: Custom Dataset과 DataLoader")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
