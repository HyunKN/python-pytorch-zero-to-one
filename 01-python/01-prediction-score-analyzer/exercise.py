import collections
def analyze_scores(
    labels: list[str], scores: list[float], threshold: float
) -> dict[str, object]:
    """Top-1, Top-3와 최종 판정을 반환합니다."""
    # raise NotImplementedError("점수 분석기를 구현하세요.")
    if not labels:
        raise ValueError("라벨이 비어있습니다.")
    if len(labels) != len(scores):
        raise ValueError("라벨 수와 스코어의 수가 일치하지 않습니다.")

    ranked = sorted(
        zip(labels, scores), key=lambda x: x[1], reverse=True
    )

    top_items= [{"label" : label, "score" : score} for label, score in ranked[:3] ]
    
    top1 = top_items[0]

    decision = top1["label"] if top1["score"] >= threshold else "unknown"

    return {"top1": top1, "top3": top_items, "decision": decision}


if __name__ == "__main__":
    sample_labels = ["cat", "dog", "bird", "rabbit"]
    sample_scores = [0.12, 0.71, 0.10, 0.07]
    print(analyze_scores(sample_labels, sample_scores, threshold=0.50))
