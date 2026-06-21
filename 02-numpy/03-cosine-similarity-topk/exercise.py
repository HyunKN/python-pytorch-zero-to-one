import numpy as np


def cosine_top_k(
    embeddings: np.ndarray, query: np.ndarray, k: int
) -> tuple[np.ndarray, np.ndarray]:
    """Top-K index와 cosine similarity score를 반환합니다."""
    raise NotImplementedError("Cosine similarity와 Top-K를 구현하세요.")
