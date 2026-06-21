# 04 — FashionMNIST CNN

## 무엇을 배우나

같은 image classification 문제를 CNN으로 학습하고 MLP와 구조를 비교합니다.

## 1. 완성 예제 실행

```powershell
python 03-pytorch/04-fashion-mnist-cnn/demo.py
```

실제 FashionMNIST는 `--full-data --epochs 2`를 추가합니다.

## 2. Shape 흐름

```text
(N, 1, 28, 28)
→ Conv/Pool: (N, 16, 14, 14)
→ Conv/Pool: (N, 32, 7, 7)
→ Flatten
→ class logits: (N, 10)
```

## 3. 직접 구현과 검증

[exercise.py](exercise.py)에서 CNN layer, forward, parameter 계산, synthetic loader와 training loop를 구현합니다.

```powershell
python 03-pytorch/04-fashion-mnist-cnn/check.py
```

## 완료 기준

- 각 layer의 channel/height/width 설명
- MLP와 CNN parameter 및 구조 비교
- [notes.md](notes.md)에 shape와 결과 기록
