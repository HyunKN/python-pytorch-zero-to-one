# 01 — NumPy Array와 Shape

## 무엇을 배우나

NumPy array의 `shape`, `ndim`, `dtype`을 읽고 전체 원소의 기본 통계를 계산합니다. 이후 Tensor shape를 이해하기 위한 출발점입니다.

## 1. 완성 예제 실행

```powershell
python 02-numpy/01-array-and-shape/demo.py
```

입력은 2행 3열이며 평균은 `3.5`입니다.

## 2. 코드 흐름

1. `array.size`로 빈 array인지 확인합니다.
2. `shape`, `ndim`, `dtype`을 읽습니다.
3. `min()`, `max()`, `mean()`을 호출합니다.
4. NumPy scalar를 일반 Python 숫자로 바꿔 반환합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `summarize_array()`를 구현합니다.

```powershell
python 02-numpy/01-array-and-shape/check.py
```

## 완료 기준

- `(2, 3)` shape가 의미하는 바를 설명 가능
- dtype과 Python type의 차이를 설명 가능
- 1D와 2D array 모두 처리
- [notes.md](notes.md) 작성
