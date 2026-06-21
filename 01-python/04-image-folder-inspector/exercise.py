from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def inspect_image_folder(folder: Path) -> dict[str, object]:
    """이미지 전체 개수와 확장자별 개수를 반환합니다."""
    raise NotImplementedError("이미지 폴더 검사를 구현하세요.")
