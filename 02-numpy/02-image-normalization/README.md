# 02 — 이미지 Normalization

## 무엇을 배우나

`uint8` 이미지 픽셀을 `float32`로 변환하고 channel별 mean과 std를 적용합니다.
NumPy broadcasting이 실제 이미지 전처리에 어떻게 쓰이는지 확인합니다.

## 1. 완성 예제 실행

### 가상 배열로 확인 (기본)

```powershell
python 02-numpy/02-image-normalization/demo.py
```

입력 픽셀 `[0, 127, 255]`는 mean과 std가 모두 `0.5`일 때 대략 `[-1.0, -0.0039, 1.0]`이 됩니다.

### 실제 이미지 파일로 확인

먼저 샘플 이미지를 생성합니다.

```powershell
python 02-numpy/02-image-normalization/make_sample.py
```

**Pillow 버전** — 채널이 RGB 순서로 로드됩니다.

```powershell
python 02-numpy/02-image-normalization/demo_pil.py
```

**OpenCV 버전** — 채널이 BGR 순서로 로드되므로, RGB로 변환 후 normalize합니다.

```powershell
python 02-numpy/02-image-normalization/demo_cv2.py
```

## 2. 코드 흐름

1. image shape가 HWC인지 확인합니다.
2. `float32`로 바꾸고 255로 나눕니다.
3. shape `(channels,)`인 mean과 std를 HWC image에 broadcasting합니다.
4. 원본 image는 수정하지 않고 새 array를 반환합니다.

## 3. Pillow vs OpenCV

| | Pillow | OpenCV |
|---|---|---|
| 채널 순서 | **RGB** | **BGR** ← 주의 |
| 변환 필요 여부 | 없음 | `cv2.cvtColor(img, COLOR_BGR2RGB)` 필수 |
| 주요 사용처 | 일반 이미지 처리 | 컴퓨터 비전, 실시간 영상 |

BGR→RGB 변환을 빠뜨리면 R과 B 채널의 normalize 값이 뒤바뀝니다.

## 4. 직접 구현과 검증

[exercise.py](exercise.py)의 `normalize_image()`를 구현합니다.

```powershell
python 02-numpy/02-image-normalization/check.py
```

## 완료 기준

- 출력 dtype이 `float32`
- 입력과 출력 shape가 같음
- broadcasting되는 axis를 설명 가능
- OpenCV에서 BGR→RGB 변환이 필요한 이유를 설명 가능
- [notes.md](notes.md) 작성
