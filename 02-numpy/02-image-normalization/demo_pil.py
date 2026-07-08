"""Pillow로 이미지를 불러와서 channel별 normalization을 수행합니다."""

import numpy as np
from PIL import Image


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
    pil_image = Image.open("02-numpy/02-image-normalization/sample.png")
    image = np.array(pil_image)  # Pillow는 자동으로 RGB 순서로 불러옵니다

    print("=== [Pillow 버전] ===")
    print(f"이미지 shape : {image.shape}  (H, W, C)")
    print(f"dtype        : {image.dtype}")
    print(f"첫 번째 픽셀 (R,G,B) : {image[0, 0]}")

    # ── 2. ImageNet 표준 mean / std 적용 ──────────────────────────────────
    # 딥러닝 모델에서 가장 널리 쓰이는 ImageNet 통계값입니다.
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

    result = normalize_image(image, mean, std)

    print(f"\nnormalize 후 shape : {result.shape}")
    print(f"normalize 후 dtype : {result.dtype}")
    print(f"값 범위  min={result.min():.4f}  max={result.max():.4f}")
    print(f"첫 번째 픽셀 normalize 결과 : {result[0, 0]}")

    # ── 3. 중간값 확인 (픽셀 값 → 스케일 → normalize 흐름) ────────────────
    print("\n[첫 번째 픽셀 변환 흐름]")
    raw   = image[0, 0]
    scaled = raw / 255.0
    normed = (scaled - mean) / std
    print(f"  원본 uint8  : {raw}")
    print(f"  ÷255 scaled : {scaled.round(4)}")
    print(f"  normalize   : {normed.round(4)}")


if __name__ == "__main__":
    main()
