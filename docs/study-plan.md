# Python · PyTorch 학습 계획

기간: 2026년 6월 21일 ~ 8월 말
방식: Top-down 학습 + 직접 구현

## 최종 목표

Python으로 Vision 모델의 데이터 처리, 학습, 평가를 직접 구현하고 ONNX Runtime으로 변환·검증·측정합니다.

## 1~2주차: Python 기초와 데이터 처리

실습 단계: [01-python](../01-python/)

- [ ] Prediction Score Analyzer
- [ ] List와 Dictionary 요약
- [ ] JSON 데이터 읽기
- [ ] 이미지 폴더 검사
- [ ] LeetCode Array, String, Hash Map 문제 병행

완료 기준:

- list, dict, function, file 처리 코드를 직접 작성할 수 있습니다.
- 데이터의 입력과 반환 구조를 설명할 수 있습니다.
- 다음 날 핵심 함수를 보지 않고 다시 작성할 수 있습니다.

## 3~4주차: NumPy와 PyTorch 계산 기초

실습 단계: [02-numpy](../02-numpy/)와 [03-pytorch 01~02](../03-pytorch/)

- [ ] NumPy array와 shape
- [ ] 이미지 normalization
- [ ] Cosine similarity와 Top-K
- [ ] PyTorch Tensor와 device
- [ ] Autograd와 Linear Regression

완료 기준:

- NumPy array와 Tensor의 차이를 설명할 수 있습니다.
- shape와 dtype을 추적할 수 있습니다.
- prediction, loss, backward, optimizer 순서를 설명할 수 있습니다.

## 5~6주차: FashionMNIST 학습 Pipeline

실습 단계: [03-pytorch 03~04](../03-pytorch/)

- [ ] FashionMNIST MLP 학습
- [ ] FashionMNIST CNN 학습
- [ ] Dataset과 DataLoader 사용
- [ ] training/validation loop 작성
- [ ] checkpoint 저장과 불러오기
- [ ] MLP/CNN 결과 비교

완료 기준:

- batch, epoch, loss, optimizer를 설명할 수 있습니다.
- MLP와 CNN의 출력 shape를 추적할 수 있습니다.
- 같은 validation set에서 두 모델을 비교할 수 있습니다.

## 7~8주차: 실제 Vision 데이터와 Fine-tuning

실습 단계: [03-pytorch 05~07](../03-pytorch/)

- [ ] Custom Dataset과 DataLoader
- [ ] train/validation transform 분리
- [ ] ResNet fine-tuning
- [ ] accuracy와 class별 recall 계산
- [ ] confusion matrix와 실패 사례 분석

완료 기준:

- 실제 이미지 폴더에서 training pipeline을 구성할 수 있습니다.
- pretrained model을 dataset class 수에 맞게 수정할 수 있습니다.
- metric과 실패 사례를 근거로 모델을 설명할 수 있습니다.

## 9~10주차: ONNX 배포와 측정

실습 단계: [04-deployment](../04-deployment/)

- [ ] PyTorch 모델을 ONNX로 export
- [ ] ONNX Runtime Python inference
- [ ] PyTorch와 ONNX 출력 parity 확인
- [ ] warm-up 후 latency 반복 측정
- [ ] median, p90, model size 기록

완료 기준:

- 동일 입력에서 PyTorch와 ONNX 출력 차이를 측정할 수 있습니다.
- benchmark 조건과 수치를 분리해 기록할 수 있습니다.
- 숫자를 근거로 배포 결과와 한계를 설명할 수 있습니다.

## 일일 루틴: 3시간 기준

- Python/CS 개념: 30분
- LeetCode Easy 1문제: 40분
- 현재 curriculum 실습: 90분
- 코드 재작성 및 학습 기록: 20분

## 구현 학습 규칙

1. 먼저 20~30분 직접 시도합니다.
2. 정답 전체보다 오류 원인이나 hint를 먼저 찾습니다.
3. 참고한 코드는 각 부분의 역할을 설명합니다.
4. 다음 날 핵심 코드를 보지 않고 다시 작성합니다.
5. 실행 성공과 개념 이해를 별도로 확인합니다.

## 첫 단계 체크리스트

- [ ] 01단계 README 읽기
- [ ] 예시 입력과 예상 결과를 손으로 확인
- [ ] `analyze_scores()` 직접 구현
- [ ] 최소 세 가지 입력으로 결과 확인
- [ ] `notes.md`에 Approach와 Mistakes 기록
- [ ] 다음 날 함수를 다시 작성
