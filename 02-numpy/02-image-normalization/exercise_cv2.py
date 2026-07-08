"""[OpenCV 버전] normalize_image()를 직접 구현하세요.

힌트:
  1. image.astype(np.float32) 로 dtype을 바꿉니다.
  2. 255.0 으로 나누어 픽셀 범위를 [0, 1]로 맞춥니다.
  3. mean과 std를 이용해 (scaled - mean) / std 를 계산합니다.
  4. mean/std shape은 (C,) 이고 image shape은 (H, W, C) 입니다.
     NumPy broadcasting이 어떤 축에서 일어나는지 생각해 보세요.

OpenCV 주의사항:
  - cv2.imread()는 채널을 BGR 순서로 불러옵니다.
  - ImageNet mean/std는 RGB 기준이므로, normalize 전에 BGR→RGB 변환이 필요합니다.
  - 변환 방법: cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
"""

import cv2
import numpy as np


def normalize_image(
    image: np.ndarray, mean: np.ndarray, std: np.ndarray
) -> np.ndarray:
    """HWC uint8 이미지를 float32로 변환하고 channel별로 normalize합니다.

    Args:
        image: (H, W, C) uint8 배열. BGR→RGB 변환이 완료된 이미지.
        mean:  (C,) float32 배열. 각 channel의 평균.
        std:   (C,) float32 배열. 각 channel의 표준편차. 0이 포함되면 안 됩니다.

    Returns:
        (H, W, C) float32 배열. normalize된 이미지.
    """
    raise NotImplementedError("이미지 normalization을 구현하세요.")


def main() -> None:
    # ── 이미지 로드 (수정하지 마세요) ────────────────────────────────────
    image_bgr = cv2.imread("02-numpy/02-image-normalization/sample.png")
    if image_bgr is None:
        raise FileNotFoundError("sample.png가 없습니다. make_sample.py를 먼저 실행하세요.")

    print(f"imread 직후 shape : {image_bgr.shape}  dtype: {image_bgr.dtype}")
    print(f"첫 번째 픽셀 (B,G,R) : {image_bgr[0, 0]}  ← BGR 순서 확인!")

    # ── BGR→RGB 변환을 구현하세요 ─────────────────────────────────────────
    # image_rgb = ???
    raise NotImplementedError("BGR→RGB 변환을 구현하세요. (cv2.cvtColor 사용)")

    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    print(f"\nBGR→RGB 변환 후 첫 번째 픽셀 (R,G,B) : {image_rgb[0, 0]}")

    # ── normalize_image()를 구현한 뒤 아래 결과를 확인하세요 ─────────────
    result = normalize_image(image_rgb, mean, std)

    print(f"\nnormalize 후 shape : {result.shape}  dtype: {result.dtype}")
    print(f"값 범위  min={result.min():.4f}  max={result.max():.4f}")
    print(f"첫 번째 픽셀 normalize 결과 : {result[0, 0]}")


if __name__ == "__main__":
    main()
