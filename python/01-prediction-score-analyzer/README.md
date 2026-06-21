# Prediction Score Analyzer

분류 모델의 label과 score를 받아 예측 결과를 요약하는 첫 번째 Python 실전 과제입니다.

## Input

```python
labels = ["gwanghwamun", "gyeongbokgung", "namsan", "bulguksa"]
scores = [0.12, 0.71, 0.10, 0.07]
threshold = 0.50
```

## 구현할 기능

- 가장 높은 score와 해당 label 찾기
- score가 높은 순서대로 Top-3 만들기
- 최고 score가 threshold보다 낮으면 `unknown`으로 판정하기
- 결과를 하나의 `dict`로 반환하기

예상 결과의 형태:

```python
{
    "top1": {"label": "gyeongbokgung", "score": 0.71},
    "top3": [
        {"label": "gyeongbokgung", "score": 0.71},
        {"label": "gwanghwamun", "score": 0.12},
        {"label": "namsan", "score": 0.10},
    ],
    "decision": "gyeongbokgung",
}
```

## 배울 내용

- list와 index
- `for`, `if`
- 함수 parameter와 `return`
- `dict`
- 정렬과 Top-K
- threshold 기반 decision

먼저 순수 Python으로 구현합니다. 완성한 다음 같은 기능을 PyTorch Tensor와 `torch.topk()`로 다시 구현합니다.

## 완료 기준

- [ ] 예시 입력에서 올바른 Top-1을 반환
- [ ] score 순서대로 Top-3를 반환
- [ ] 모든 score가 threshold보다 낮으면 `unknown`을 반환
- [ ] 각 코드 블록의 역할을 설명
- [ ] 다음 날 핵심 함수를 다시 작성
