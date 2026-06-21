import numpy as np

from exercise import cosine_top_k


def main() -> int:
    embeddings = np.array(
        [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=np.float32
    )
    query = np.array([1.0, 0.0], dtype=np.float32)
    try:
        indices, scores = cosine_top_k(embeddings, query, k=2)
        np.testing.assert_array_equal(indices, np.array([0, 2]))
        np.testing.assert_allclose(scores, np.array([1.0, 2**-0.5]), atol=1e-6)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: Cosine Similarity와 Top-K")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
