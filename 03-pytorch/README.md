# 03 — PyTorch와 Vision

NumPy에서 익힌 shape와 연산을 Tensor, autograd, 모델 학습으로 확장합니다.

## 진행 순서

1. [Tensor 기초](01-tensor-basics/)
2. [Autograd와 Linear Regression](02-autograd-linear-regression/)
3. [FashionMNIST MLP](03-fashion-mnist-mlp/)
4. [FashionMNIST CNN](04-fashion-mnist-cnn/)
5. [Custom Dataset과 DataLoader](05-custom-dataset-dataloader/)
6. [ResNet Fine-tuning](06-resnet-finetuning/)
7. [평가와 Error Analysis](07-evaluation-error-analysis/)

FashionMNIST 단계의 `demo.py`는 기본 실행 시 빠른 synthetic data를 사용합니다. 실제 FashionMNIST를 내려받아 실행하려면 `--full-data`를 추가합니다.

```powershell
python 03-pytorch/03-fashion-mnist-mlp/demo.py --full-data --epochs 2
```
