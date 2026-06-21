# 01 — Tensor 기초

## 무엇을 배우나

Tensor의 shape, dtype, device를 확인하고 matrix multiplication을 수행합니다. NumPy array와 비슷하지만 accelerator에서 계산할 수 있다는 차이를 확인합니다.

## 1. 완성 예제 실행

```powershell
python 03-pytorch/01-tensor-basics/demo.py
```

출력에서 사용 device, `(2, 2)` shape, matrix product를 확인합니다.

## 2. 코드 흐름

1. Tensor를 만들며 device를 지정합니다.
2. `shape`, `dtype`, `device`를 읽습니다.
3. 통계 계산을 위해 numeric Tensor로 변환합니다.
4. `@` 연산자로 matrix multiplication을 수행합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 두 함수를 구현합니다.

```powershell
python 03-pytorch/01-tensor-basics/check.py
```

## 완료 기준

- shape와 matrix multiplication 조건 설명
- CPU와 GPU device 이동 방식 설명
- [notes.md](notes.md)에 shape 기록
