# 09 — Autograd와 Linear Regression

작은 선형 데이터를 이용해 prediction, loss, backward, weight update 흐름을 구현합니다.

## 구현할 기능

- `nn.Linear` 모델 생성
- Mean Squared Error 계산
- `loss.backward()`로 gradient 계산
- optimizer로 weight update
- epoch별 loss 기록

## 배울 내용

- computation graph
- gradient와 `autograd`
- loss와 optimizer
- `zero_grad()`, `backward()`, `step()`

## 완료 기준

- [ ] 학습 전후 loss 비교
- [ ] 각 학습 단계의 순서 설명
- [ ] gradient 초기화가 필요한 이유 기록
