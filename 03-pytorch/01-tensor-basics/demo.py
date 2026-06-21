import torch


def summarize_tensor(tensor: torch.Tensor) -> dict[str, object]:
    """Tensor의 구조, device와 기본 통계값을 반환합니다."""
    if tensor.numel() == 0:
        raise ValueError("빈 Tensor는 요약할 수 없습니다.")

    numeric = tensor.float()
    return {
        "shape": tuple(tensor.shape),
        "ndim": tensor.ndim,
        "dtype": str(tensor.dtype),
        "device": str(tensor.device),
        "minimum": float(numeric.min().item()),
        "maximum": float(numeric.max().item()),
        "mean": float(numeric.mean().item()),
    }


def matrix_product(left: torch.Tensor, right: torch.Tensor) -> torch.Tensor:
    """두 Tensor의 matrix multiplication 결과를 반환합니다."""
    if left.ndim != 2 or right.ndim != 2:
        raise ValueError("두 입력은 모두 2D Tensor여야 합니다.")
    if left.shape[1] != right.shape[0]:
        raise ValueError("left의 열 수와 right의 행 수가 같아야 합니다.")
    return left @ right


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    left = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
    right = torch.eye(2, device=device)

    print("사용 device:", device)
    print("Tensor 요약:", summarize_tensor(left))
    print("Matrix product:\n", matrix_product(left, right))


if __name__ == "__main__":
    main()
