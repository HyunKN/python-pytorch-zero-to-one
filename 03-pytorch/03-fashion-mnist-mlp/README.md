# 03 — FashionMNIST MLP

## 무엇을 배우나

Dataset, DataLoader, MLP, training loop, validation, checkpoint를 하나의 실행 가능한 pipeline으로 연결합니다.

## 1. 빠른 전체 흐름 실행

기본 실행은 network download 없이 synthetic image를 사용합니다.

```powershell
python 03-pytorch/03-fashion-mnist-mlp/demo.py
```

실제 FashionMNIST:

```powershell
python 03-pytorch/03-fashion-mnist-mlp/demo.py --full-data --epochs 2
```

## 2. 코드 흐름

1. DataLoader가 `(batch, 1, 28, 28)` image와 label을 제공합니다.
2. `Flatten`이 image를 784개 값으로 펼칩니다.
3. MLP가 10개 class logit을 출력합니다.
4. Cross Entropy Loss를 계산하고 backward합니다.
5. validation에서는 `eval()`과 `no_grad()`를 사용합니다.
6. 학습한 `state_dict`를 checkpoint로 저장합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 모델, loader, train, evaluate, checkpoint 함수를 구현합니다.

```powershell
python 03-pytorch/03-fashion-mnist-mlp/check.py
```

## 완료 기준

- input `(N,1,28,28)`과 output `(N,10)` 설명
- train/eval mode 차이 설명
- checkpoint 저장·복원 성공
- [notes.md](notes.md)에 loss와 accuracy 기록
