"""[Pillow 버전] normalize_image()를 직접 구현하세요.

힌트:
  1. image.astype(np.float32) 로 dtype을 바꿉니다.
  2. 255.0 으로 나누어 픽셀 범위를 [0, 1]로 맞춥니다.
  3. mean과 std를 이용해 (scaled - mean) / std 를 계산합니다.
  4. mean/std shape은 (C,) 이고 image shape은 (H, W, C) 입니다.
     NumPy broadcasting이 어떤 축에서 일어나는지 생각해 보세요.
"""

from numpy import float32
import numpy as np
from PIL import Image


def normalize_image(
    image: np.ndarray, mean: np.ndarray, std: np.ndarray
) -> np.ndarray:
    """HWC uint8 이미지를 float32로 변환하고 channel별로 normalize합니다.

    Args:
        image: (H, W, C) uint8 배열. Pillow로 불러온 RGB 이미지.
        mean:  (C,) float32 배열. 각 channel의 평균.
        std:   (C,) float32 배열. 각 channel의 표준편차. 0이 포함되면 안 됩니다.
        

    Returns:
        (H, W, C) float32 배열. normalize된 이미지.
    """

    if image.ndim != 3:
        raise ValueError("image shape는 (height, width, channels)여야 합니다.")
    if mean.shape != (image.shape[-1],) or std.shape != (image.shape[-1],):
        raise ValueError("mean과 std의 길이는 image 채널 수와 같아야 합니다.")
    if np.any(std == 0):
        raise ValueError("std에는 0이 포함될 수 없습니다.")

    scaled = image.astype(np.float32) / 255.0
    return ((scaled - mean.astype(np.float32)) / std.astype(np.float32)).astype(np.float32)
    
    # raise NotImplementedError("이미지 normalization을 구현하세요.")


def main() -> None:
    # ── 이미지 로드 (수정하지 마세요) ────────────────────────────────────
    pil_image = Image.open("02-numpy/02-image-normalization/sample.png")
    image = np.array(pil_image)          # HWC, uint8, RGB 순서
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    print(f"입력 shape : {image.shape}  dtype: {image.dtype}")
    print(f"첫 번째 픽셀 (R,G,B) : {image[0, 0]}")

    # ── normalize_image()를 구현한 뒤 아래 결과를 확인하세요 ─────────────
    result = normalize_image(image, mean, std)

    print(f"\nnormalize 후 shape : {result.shape}  dtype: {result.dtype}")
    print(f"값 범위  min={result.min():.4f}  max={result.max():.4f}")
    print(f"첫 번째 픽셀 normalize 결과 : {result[0, 0]}")


if __name__ == "__main__":
    main()
