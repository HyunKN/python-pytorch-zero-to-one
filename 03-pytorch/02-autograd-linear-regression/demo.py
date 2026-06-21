import torch
from torch import nn


def train_linear_regression(
    inputs: torch.Tensor,
    targets: torch.Tensor,
    epochs: int,
    learning_rate: float,
) -> tuple[nn.Module, list[float]]:
    """`prediction → loss → backward → step` 순서로 선형 모델을 학습합니다."""
    if inputs.ndim != 2 or targets.ndim != 2:
        raise ValueError("inputs와 targets는 (samples, features) 형태여야 합니다.")
    if len(inputs) != len(targets):
        raise ValueError("inputs와 targets의 sample 수가 같아야 합니다.")

    model = nn.Linear(inputs.shape[1], targets.shape[1])
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    losses: list[float] = []

    for _ in range(epochs):
        predictions = model(inputs)
        loss = criterion(predictions, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(float(loss.item()))

    return model, losses


def main() -> None:
    torch.manual_seed(0)
    inputs = torch.linspace(-1, 1, 40).unsqueeze(1)
    targets = 3 * inputs + 2
    model, losses = train_linear_regression(
        inputs, targets, epochs=120, learning_rate=0.1
    )

    with torch.no_grad():
        prediction = model(torch.tensor([[2.0]])).item()

    print(f"첫 loss: {losses[0]:.6f}")
    print(f"마지막 loss: {losses[-1]:.6f}")
    print(f"x=2 예측값: {prediction:.4f} (정답: 8)")


if __name__ == "__main__":
    main()
