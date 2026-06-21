# 10 — FashionMNIST MLP

FashionMNIST 이미지를 flatten한 뒤 MLP로 분류하는 전체 training pipeline을 구현합니다.

## 구현할 기능

- dataset download와 `DataLoader`
- MLP 모델 정의
- training loop
- validation accuracy 계산
- checkpoint 저장

## 배울 내용

- `Dataset`, `DataLoader`, batch
- `nn.Module`과 `forward()`
- Cross Entropy Loss
- train/eval mode

## 완료 기준

- [ ] batch input/output shape 기록
- [ ] epoch별 train loss와 validation accuracy 출력
- [ ] 저장한 checkpoint 다시 불러오기
