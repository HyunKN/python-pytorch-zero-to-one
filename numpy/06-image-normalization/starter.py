import numpy as np


def normalize_image(
    image: np.ndarray, mean: np.ndarray, std: np.ndarray
) -> np.ndarray:
    """HWC 이미지를 float32로 변환하고 channel별로 normalize합니다."""
    raise NotImplementedError("이미지 normalization을 구현하세요.")
