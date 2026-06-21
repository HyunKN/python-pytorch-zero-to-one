# 02 — 이미지 Normalization

## 무엇을 배우나

`uint8` 이미지 픽셀을 `float32`로 변환하고 channel별 mean과 std를 적용합니다. NumPy broadcasting이 실제 이미지 전처리에 어떻게 쓰이는지 확인합니다.

## 1. 완성 예제 실행

```powershell
python 02-numpy/02-image-normalization/demo.py
```

입력 픽셀 `[0, 127, 255]`는 mean과 std가 모두 `0.5`일 때 대략 `[-1.0, -0.0039, 1.0]`이 됩니다.

## 2. 코드 흐름

1. image shape가 HWC인지 확인합니다.
2. `float32`로 바꾸고 255로 나눕니다.
3. shape `(channels,)`인 mean과 std를 HWC image에 broadcasting합니다.
4. 원본 image는 수정하지 않고 새 array를 반환합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `normalize_image()`를 구현합니다.

```powershell
python 02-numpy/02-image-normalization/check.py
```

## 완료 기준

- 출력 dtype이 `float32`
- 입력과 출력 shape가 같음
- broadcasting되는 axis를 설명 가능
- [notes.md](notes.md) 작성
