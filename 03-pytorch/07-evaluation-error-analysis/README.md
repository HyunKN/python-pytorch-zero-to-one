# 07 — 평가와 Error Analysis

## 무엇을 배우나

전체 accuracy만 보지 않고 confusion matrix, class별 recall, confidence가 높은 오답을 함께 분석합니다.

## 1. 완성 예제 실행

```powershell
python 03-pytorch/07-evaluation-error-analysis/demo.py
```

예제의 accuracy는 `0.75`이고, true class 1을 class 0으로 예측한 오답이 한 개입니다.

## 2. 코드 흐름

1. `eval()`과 `no_grad()`로 evaluation mode를 설정합니다.
2. true/predicted pair를 confusion matrix에 누적합니다.
3. diagonal 합으로 accuracy를 계산합니다.
4. 각 행의 합으로 class별 recall을 계산합니다.
5. 오답의 prediction과 confidence를 저장해 높은 순서로 정렬합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 평가와 오분류 수집 함수를 구현합니다.

```powershell
python 03-pytorch/07-evaluation-error-analysis/check.py
```

## 완료 기준

- confusion matrix의 행과 열 의미 설명
- accuracy와 class recall 차이 설명
- 최소 10개 실제 실패 사례에 대한 가설 기록
- [notes.md](notes.md) 작성
