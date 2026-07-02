import collections
import numpy as np


def summarize_array(array: np.ndarray) -> dict[str, object]:
    """Array의 구조와 전체 원소 기준 통계값을 반환합니다."""
    if array.size == 0:
        raise ValueError("빈 array는 요약할 수 없습니다.")

    # 정수 계열 타입인지 확인하여 캐스팅 함수 결정 (int 또는 float)
    is_integer = np.issubdtype(array.dtype, np.integer)
    convert = int if is_integer else float

    return {
        "shape": array.shape,
        "ndim": array.ndim,
        "dtype": str(array.dtype),
        "minimum": convert(array.min()),
        "maximum": convert(array.max()),
        "mean": float(array.mean()),
    }


def main() -> None:
    array = np.array([[1, 2, 3], [4, 5, 6]])
    print("입력 array:\n", array)
    print("요약 결과:", summarize_array(array))


if __name__ == "__main__":
    main()
