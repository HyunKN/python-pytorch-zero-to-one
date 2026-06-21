import json
from pathlib import Path


def load_records(path: Path) -> list[dict[str, object]]:
    """JSON 파일에서 record 목록을 읽습니다."""
    raise NotImplementedError("JSON 파일 읽기를 구현하세요.")


def count_categories(records: list[dict[str, object]]) -> dict[str, int]:
    """record의 category별 개수를 반환합니다."""
    raise NotImplementedError("category 집계를 구현하세요.")
