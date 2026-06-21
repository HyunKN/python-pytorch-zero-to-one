import torch

from exercise import train_linear_regression


def main() -> int:
    try:
        torch.manual_seed(0)
        inputs = torch.linspace(-1, 1, 40).unsqueeze(1)
        targets = 3 * inputs + 2
        model, losses = train_linear_regression(inputs, targets, 120, 0.1)
        assert losses[-1] < losses[0] * 0.01
        assert abs(model(torch.tensor([[2.0]])).item() - 8.0) < 0.2
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        return 1
    print("PASS: Autograd와 Linear Regression")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
