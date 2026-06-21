import torch

from exercise import matrix_product, summarize_tensor


def main() -> int:
    try:
        tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
        summary = summarize_tensor(tensor)
        assert summary["shape"] == (2, 2)
        assert summary["mean"] == 2.5
        torch.testing.assert_close(matrix_product(tensor, torch.eye(2)), tensor)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: Tensor 기초")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
