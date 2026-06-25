import tempfile
import json
from pathlib import Path


def load_records(path: Path) -> list[dict[str, object]]:
    """JSON 파일에서 record 목록을 읽습니다."""
    # raise NotImplementedError("JSON 파일 읽기를 구현하세요.")
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("JSON 최상위 값은 object로 이루어진 list여야 합니다.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON 리스트의 모든 요소는 딕셔너리(dict) 형식이어야 합니다.")
    return data

def count_categories(records: list[dict[str, object]]) -> dict[str, int]:
    """record의 category별 개수를 반환합니다."""
    # raise NotImplementedError("category 집계를 구현하세요.")
    counts: dict[str, int] = {}
    for record in records:
        category = str(record["category"])
        counts[category] = counts.get(category, 0) + 1
    return counts