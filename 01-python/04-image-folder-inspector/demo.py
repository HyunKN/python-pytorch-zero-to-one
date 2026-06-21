import tempfile
from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def inspect_image_folder(folder: Path) -> dict[str, object]:
    """하위 폴더를 포함해 이미지 파일 수를 확장자별로 집계합니다."""
    if not folder.is_dir():
        raise ValueError(f"존재하는 폴더가 아닙니다: {folder}")

    counts: dict[str, int] = {}
    for path in folder.rglob("*"):
        extension = path.suffix.lower()
        if path.is_file() and extension in IMAGE_EXTENSIONS:
            counts[extension] = counts.get(extension, 0) + 1

    ordered_counts = dict(sorted(counts.items()))
    return {"total": sum(ordered_counts.values()), "by_extension": ordered_counts}


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "animals").mkdir()
        (root / "cat.JPG").touch()
        (root / "dog.png").touch()
        (root / "animals" / "bird.jpeg").touch()
        (root / "notes.txt").touch()
        result = inspect_image_folder(root)

    print("이미지 폴더 분석 결과:", result)


if __name__ == "__main__":
    main()
