import json
import tempfile
from pathlib import Path


def load_records(path: Path) -> list[dict[str, object]]:
    """UTF-8 JSON 파일에서 record 목록을 읽습니다."""
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON 최상위 값은 object로 이루어진 list여야 합니다.")
    return data


def count_categories(records: list[dict[str, object]]) -> dict[str, int]:
    """각 record의 category별 개수를 계산합니다."""
    counts: dict[str, int] = {}
    for record in records:
        category = str(record["category"])
        counts[category] = counts.get(category, 0) + 1
    return counts


def main() -> None:
    sample_records = [
        {"name": "apple", "category": "fruit"},
        {"name": "carrot", "category": "vegetable"},
        {"name": "banana", "category": "fruit"},
    ]

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "records.json"
        path.write_text(json.dumps(sample_records), encoding="utf-8")
        loaded = load_records(path)

    print("전체 record 수:", len(loaded))
    print("category별 개수:", count_categories(loaded))


if __name__ == "__main__":
    main()
