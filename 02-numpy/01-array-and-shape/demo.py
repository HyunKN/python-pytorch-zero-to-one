import numpy as np


def summarize_array(array: np.ndarray) -> dict[str, object]:
    """Array의 구조와 전체 원소 기준 통계값을 반환합니다."""
    if array.size == 0:
        raise ValueError("빈 array는 요약할 수 없습니다.")

    return {
        "shape": array.shape,
        "ndim": array.ndim,
        "dtype": str(array.dtype),
        "minimum": float(array.min()),
        "maximum": float(array.max()),
        "mean": float(array.mean()),
    }


def main() -> None:
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("입력 array:\n", array)
    print("요약 결과:", summarize_array(array))


if __name__ == "__main__":
    main()
