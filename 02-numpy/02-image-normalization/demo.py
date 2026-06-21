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
    image = np.array([[[0, 127, 255]]], dtype=np.uint8)
    mean = np.array([0.5, 0.5, 0.5], dtype=np.float32)
    std = np.array([0.5, 0.5, 0.5], dtype=np.float32)

    print("입력 픽셀:", image)
    print("normalize 결과:", normalize_image(image, mean, std))


if __name__ == "__main__":
    main()
