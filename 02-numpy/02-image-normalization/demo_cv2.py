"""OpenCV로 이미지를 불러와서 channel별 normalization을 수행합니다.

OpenCV 주의사항:
  - cv2.imread()는 이미지를 BGR 순서로 불러옵니다 (RGB가 아님).
  - mean/std를 ImageNet 기준(RGB)으로 적용하려면 반드시 BGR→RGB 변환이 필요합니다.
"""

import cv2
import numpy as np


def normalize_image(
    image: np.ndarray, mean: np.ndarray, std: np.ndarray
) -> np.ndarray:
    """HWC uint8 이미지를 float32로 변환하고 channel별로 normalize합니다."""
    if image.ndim != 3:
        raise ValueError("image shape는 (height, width, channels)여야 합니다.")
    if mean.shape != (image.shape[-1],) or std.shape != (image.shape[-1],):
        raise ValueError("mean과 std 길이는 image channel 수와 같아야 합니다.")
    if np.any(std == 0):
        raise ValueError("std에는 0이 포함될 수 없습니다.")

    scaled = image.astype(np.float32) / 255.0
    return ((scaled - mean.astype(np.float32)) / std.astype(np.float32)).astype(
        np.float32
    )


def main() -> None:
    # ── 1. 이미지 불러오기 ────────────────────────────────────────────────
    image_bgr = cv2.imread("02-numpy/02-image-normalization/sample.png")

    if image_bgr is None:
        raise FileNotFoundError("sample.png를 찾을 수 없습니다. make_sample.py를 먼저 실행하세요.")

    print("=== [OpenCV 버전] ===")
    print(f"imread 직후 shape   : {image_bgr.shape}  (H, W, C)")
    print(f"dtype               : {image_bgr.dtype}")
    print(f"첫 번째 픽셀 (B,G,R) : {image_bgr[0, 0]}  ← OpenCV는 BGR 순서!")

    # ── 2. BGR → RGB 변환 (필수!) ─────────────────────────────────────────
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    print(f"\nBGR→RGB 변환 후 첫 번째 픽셀 (R,G,B) : {image_rgb[0, 0]}")

    # ── 3. ImageNet 표준 mean / std 적용 ──────────────────────────────────
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    result = normalize_image(image_rgb, mean, std)

    print(f"\nnormalize 후 shape : {result.shape}")
    print(f"normalize 후 dtype : {result.dtype}")
    print(f"값 범위  min={result.min():.4f}  max={result.max():.4f}")
    print(f"첫 번째 픽셀 normalize 결과 : {result[0, 0]}")

    # ── 4. BGR 변환을 빠뜨리면 어떻게 되는지 비교 ─────────────────────────
    result_wrong = normalize_image(image_bgr, mean, std)  # BGR에 RGB mean 적용 (잘못된 예)
    print("\n[주의] BGR→RGB 변환 없이 normalize하면 결과가 달라집니다!")
    print(f"  올바른 결과 (RGB→norm) : {result[0, 0].round(4)}")
    print(f"  잘못된 결과 (BGR→norm) : {result_wrong[0, 0].round(4)}")


if __name__ == "__main__":
    main()
