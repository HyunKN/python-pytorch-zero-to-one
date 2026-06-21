def analyze_scores(
    labels: list[str], scores: list[float], threshold: float
) -> dict[str, object]:
    """Top-1, Top-3와 최종 판정을 반환합니다."""
    raise NotImplementedError("점수 분석기를 구현하세요.")


if __name__ == "__main__":
    sample_labels = ["cat", "dog", "bird", "rabbit"]
    sample_scores = [0.12, 0.71, 0.10, 0.07]
    print(analyze_scores(sample_labels, sample_scores, threshold=0.50))
