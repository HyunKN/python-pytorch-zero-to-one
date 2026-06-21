# 13 — ResNet Fine-tuning

pretrained ResNet의 마지막 classifier를 교체하고 custom dataset에 맞게 fine-tuning합니다.

## 구현할 기능

- pretrained weight 불러오기
- classifier를 class 수에 맞게 교체
- feature extractor freeze/unfreeze 비교
- optimizer에 학습 가능한 parameter만 전달

## 배울 내용

- transfer learning
- pretrained weights
- feature extractor와 classifier
- fine-tuning 전략

## 완료 기준

- [ ] 교체 전후 classifier 구조 확인
- [ ] freeze된 parameter 확인
- [ ] scratch model과 validation 결과 비교
