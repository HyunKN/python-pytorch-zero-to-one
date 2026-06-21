import numpy as np

from exercise import normalize_image


def main() -> int:
    image = np.array([[[0, 127, 255]]], dtype=np.uint8)
    mean = np.array([0.5, 0.5, 0.5], dtype=np.float32)
    std = np.array([0.5, 0.5, 0.5], dtype=np.float32)
    try:
        result = normalize_image(image, mean, std)
        expected = np.array([[[-1.0, -0.00392157, 1.0]]], dtype=np.float32)
        np.testing.assert_allclose(result, expected, atol=1e-6)
        assert result.dtype == np.float32
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: 이미지 Normalization")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
