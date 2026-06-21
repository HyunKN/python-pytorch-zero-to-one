import numpy as np


def cosine_top_k(
    embeddings: np.ndarray, query: np.ndarray, k: int
) -> tuple[np.ndarray, np.ndarray]:
    """Query와 cosine similarity가 높은 Top-K index와 score를 반환합니다."""
    if embeddings.ndim != 2 or query.ndim != 1:
        raise ValueError("embeddings는 2D, query는 1D array여야 합니다.")
    if embeddings.shape[1] != query.shape[0]:
        raise ValueError("embedding dimension이 일치해야 합니다.")
    if not 1 <= k <= len(embeddings):
        raise ValueError("k는 1 이상 embedding 개수 이하여야 합니다.")

    embedding_norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    query_norm = np.linalg.norm(query)
    if np.any(embedding_norms == 0) or query_norm == 0:
        raise ValueError("Zero vector의 cosine similarity는 정의할 수 없습니다.")

    normalized_embeddings = embeddings / embedding_norms
    normalized_query = query / query_norm
    scores = normalized_embeddings @ normalized_query
    top_indices = np.argsort(scores)[::-1][:k]
    return top_indices, scores[top_indices]


def main() -> None:
    labels = ["cat", "dog", "bird"]
    embeddings = np.array(
        [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=np.float32
    )
    query = np.array([1.0, 0.0], dtype=np.float32)
    indices, scores = cosine_top_k(embeddings, query, k=2)

    for index, score in zip(indices, scores, strict=True):
        print(f"{labels[index]}: {score:.4f}")


if __name__ == "__main__":
    main()
