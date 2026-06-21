import torch


def summarize_tensor(tensor: torch.Tensor) -> dict[str, object]:
    """Tensor의 shape, dtype, device와 기본 통계를 반환합니다."""
    raise NotImplementedError("Tensor 요약을 구현하세요.")


def matrix_product(left: torch.Tensor, right: torch.Tensor) -> torch.Tensor:
    """두 Tensor의 matrix multiplication 결과를 반환합니다."""
    raise NotImplementedError("Matrix multiplication을 구현하세요.")
