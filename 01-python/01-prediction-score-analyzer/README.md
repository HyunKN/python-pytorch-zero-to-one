# 01 — Prediction Score Analyzer

## 무엇을 배우나

분류 모델이 출력한 label과 score를 정렬해 Top-1, Top-3와 threshold 기반 decision을 만듭니다. `list`, `dict`, 함수, 정렬을 하나의 실제 처리 흐름으로 연결합니다.

## 1. 완성 예제 실행

저장소 루트에서 실행합니다.

```powershell
python 01-python/01-prediction-score-analyzer/demo.py
```

출력에서 `dog`가 Top-1이고 decision도 `dog`인지 확인합니다.

## 2. 코드 흐름

1. `zip()`으로 label과 score를 묶습니다.
2. score를 기준으로 내림차순 정렬합니다.
3. 앞의 세 항목을 Top-3 `dict`로 바꿉니다.
4. 가장 높은 score가 threshold 이상인지 확인합니다.
5. threshold 미만이면 `unknown`을 반환합니다.

## 3. 직접 구현

[exercise.py](exercise.py)의 `analyze_scores()`를 구현합니다. 함수 이름과 parameter, 반환 구조는 바꾸지 않습니다.

반환 형태:

```python
{
    "top1": {"label": "dog", "score": 0.71},
    "top3": [
        {"label": "dog", "score": 0.71},
        {"label": "cat", "score": 0.12},
        {"label": "bird", "score": 0.10},
    ],
    "decision": "dog",
}
```

## 4. 검증

```powershell
python 01-python/01-prediction-score-analyzer/check.py
```

`PASS`가 나오면 [notes.md](notes.md)에 정렬 과정과 threshold 판단을 설명합니다.

## 완료 기준

- Top-3가 score 내림차순
- 낮은 score 입력에서 `unknown` 반환
- 입력과 반환 구조를 말로 설명 가능
- 다음 날 함수 재구현
