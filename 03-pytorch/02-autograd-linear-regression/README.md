# 02 — Autograd와 Linear Regression

## 무엇을 배우나

`y = 3x + 2` synthetic data를 이용해 PyTorch 학습의 핵심 순서를 직접 구현합니다.

```text
prediction → loss → zero_grad → backward → optimizer.step
```

## 1. 완성 예제 실행

```powershell
python 03-pytorch/02-autograd-linear-regression/demo.py
```

첫 loss보다 마지막 loss가 크게 감소하고 `x=2` 예측이 8에 가까워지는지 확인합니다.

## 2. 코드 흐름

1. `nn.Linear`가 weight와 bias를 만듭니다.
2. MSE로 prediction과 target 차이를 계산합니다.
3. `backward()`가 gradient를 계산합니다.
4. optimizer가 parameter를 갱신합니다.
5. 다음 epoch 전에 기존 gradient를 초기화합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `train_linear_regression()`을 구현합니다.

```powershell
python 03-pytorch/02-autograd-linear-regression/check.py
```

## 완료 기준

- 다섯 학습 단계를 순서대로 설명
- `zero_grad()`가 필요한 이유 설명
- [notes.md](notes.md)에 loss 변화 기록
