# 06 — ResNet Fine-tuning

## 무엇을 배우나

ResNet18 backbone을 불러오고 마지막 `fc` layer를 새 class 수에 맞게 교체합니다. backbone freeze 여부에 따라 학습 가능한 parameter가 어떻게 달라지는지 확인합니다.

## 1. 완성 예제 실행

```powershell
python 03-pytorch/06-resnet-finetuning/demo.py
```

빠른 demo는 weight download를 피하기 위해 `pretrained=False`를 사용합니다. 실제 fine-tuning에서는 `pretrained=True`를 사용합니다.

## 2. 코드 흐름

1. pretrained 여부에 따라 ResNet18 weight를 선택합니다.
2. freeze할 때 기존 parameter의 `requires_grad`를 끕니다.
3. 기존 `fc.in_features`를 읽습니다.
4. 새 `nn.Linear` classifier를 연결합니다.
5. optimizer에는 `requires_grad=True`인 parameter만 전달합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `build_resnet()`과 `trainable_parameters()`를 구현합니다.

```powershell
python 03-pytorch/06-resnet-finetuning/check.py
```

## 완료 기준

- backbone과 classifier 역할 설명
- freeze된 parameter 확인
- output shape `(N, num_classes)` 확인
- [notes.md](notes.md)에 fine-tuning 설정 기록
