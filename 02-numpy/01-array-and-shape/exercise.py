import numpy as np


def summarize_array(array: np.ndarray) -> dict[str, object]:
    """Array 구조와 기본 통계를 반환합니다."""
    # raise NotImplementedError("Array 요약을 구현하세요.")
    
    return{
            'shape' : array.shape,
            'ndim'  : array.ndim,
            'dtype' : str(array.dtype),
            'minimum'   : int(array.min()),
            'maximum'   : int(array.max()),
            'mean'      : float(array.mean())
    }

if __name__ == "__main__":
    sample = np.array([[1, 2, 3], [4, 5, 6]])
    print(summarize_array(sample))
