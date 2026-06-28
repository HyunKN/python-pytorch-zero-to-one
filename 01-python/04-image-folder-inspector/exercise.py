from pathlib import Path


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def inspect_image_folder(folder: Path) -> dict[str, object]:
    """이미지 전체 개수와 확장자별 개수를 반환합니다."""
    # raise NotImplementedError("이미지 폴더 검사를 구현하세요.")
    if not folder.is_dir():
        raise ValueError(f"존재하는 폴더가 아닙니다: {folder}")

    counts: dict[str, int] = {}
    for path in folder.rglob("*"):
        extension = path.suffix.lower() # .을 포함한것을 가져온다(suffix) / lower로 소문자로 바꿔서 가져옴
        if path.is_file() and extension in IMAGE_EXTENSIONS:
            counts[extension] = counts.get(extension, 0 ) + 1
    
    ordered_counts = dict(sorted(counts.items()))
    return {"total": sum(ordered_counts.values()), "by_extension": ordered_counts}