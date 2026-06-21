from exercise import analyze_scores


def main() -> int:
    try:
        result = analyze_scores(
            ["cat", "dog", "bird", "rabbit"], [0.12, 0.71, 0.10, 0.07], 0.50
        )
        assert result["top1"] == {"label": "dog", "score": 0.71}
        assert [item["label"] for item in result["top3"]] == ["dog", "cat", "bird"]
        assert result["decision"] == "dog"
        assert analyze_scores(["cat", "dog"], [0.2, 0.3], 0.5)["decision"] == "unknown"
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: Prediction Score Analyzer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
