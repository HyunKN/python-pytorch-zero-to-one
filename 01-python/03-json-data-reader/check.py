import json
import tempfile
from pathlib import Path

from exercise import count_categories, load_records


def main() -> int:
    records = [
        {"name": "apple", "category": "fruit"},
        {"name": "carrot", "category": "vegetable"},
        {"name": "banana", "category": "fruit"},
    ]
    try:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.json"
            path.write_text(json.dumps(records), encoding="utf-8")
            loaded = load_records(path)
        assert loaded == records
        assert count_categories(loaded) == {"fruit": 2, "vegetable": 1}
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: JSON 데이터 읽기")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
