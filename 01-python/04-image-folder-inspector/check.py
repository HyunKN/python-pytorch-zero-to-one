import tempfile
from pathlib import Path

from exercise import inspect_image_folder


def main() -> int:
    try:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "cat.JPG").touch()
            (root / "dog.png").touch()
            (root / "nested" / "bird.jpeg").touch()
            (root / "notes.txt").touch()
            result = inspect_image_folder(root)
        assert result == {
            "total": 3,
            "by_extension": {".jpeg": 1, ".jpg": 1, ".png": 1},
        }
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: 이미지 폴더 검사")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
