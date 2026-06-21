import numpy as np

from exercise import summarize_array


def main() -> int:
    try:
        result = summarize_array(np.array([[1, 2, 3], [4, 5, 6]]))
        assert result["shape"] == (2, 3)
        assert result["ndim"] == 2
        assert result["minimum"] == 1.0
        assert result["maximum"] == 6.0
        assert result["mean"] == 3.5
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: NumPy Array와 Shape")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
