def analyze_scores(
    labels: list[str], scores: list[float], threshold: float
) -> dict[str, object]:
    """분류 score를 Top-1, Top-3와 최종 decision으로 요약합니다."""
    if not labels:
        raise ValueError("labels는 비어 있을 수 없습니다.")
    if len(labels) != len(scores):
        raise ValueError("labels와 scores의 길이는 같아야 합니다.")

    ranked = sorted(
        zip(labels, scores, strict=True), key=lambda item: item[1], reverse=True
    )
    
    top_items = [
        {"label": label, "score": float(score)} for label, score in ranked[:3]
    ]
    top1 = top_items[0]
    decision = top1["label"] if top1["score"] >= threshold else "unknown"

    return {"top1": top1, "top3": top_items, "decision": decision}


def main() -> None:
    labels = ["cat", "dog", "bird", "rabbit"]
    scores = [0.12, 0.71, 0.10, 0.07]
    result = analyze_scores(labels, scores, threshold=0.50)

    print("입력 labels:", labels)
    print("입력 scores:", scores)
    print("분석 결과:", result)


if __name__ == "__main__":
    main()
