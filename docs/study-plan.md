# Python · PyTorch 학습 계획

기간: 2026년 6월 21일 ~ 8월 말
방식: Top-down 학습 + 직접 구현

## 최종 목표

Python으로 Vision 모델의 데이터 처리, 학습, 평가를 직접 구현하고 일부 inference를 C++로 실행합니다.

## 1~2주차: 작동하는 분류기 분해하기

메인 프로젝트: FashionMNIST MLP 분류기

- [ ] 완성된 PyTorch 코드 실행
- [ ] 변수, `if`, `for`, 함수, list, class 학습
- [ ] Tensor shape 확인
- [ ] 학습 전후 loss와 accuracy 출력
- [ ] 코드를 기능별로 분해
- [ ] training loop 직접 재작성
- [ ] LeetCode Array, String, Hash Map Easy 10문제

완료 기준:

- `train.py`로 모델을 학습할 수 있습니다.
- 각 코드 블록의 역할을 설명할 수 있습니다.
- training loop를 보지 않고 대략 작성할 수 있습니다.

## 3~4주차: CNN과 데이터 처리

메인 프로젝트: FashionMNIST CNN 분류기

- [ ] NumPy와 Tensor 차이 이해
- [ ] 이미지 normalization 적용
- [ ] `Dataset`, `DataLoader` 사용
- [ ] train/validation 분리
- [ ] MLP를 CNN으로 변경
- [ ] checkpoint 저장 및 불러오기
- [ ] 잘못 예측한 이미지 출력
- [ ] LeetCode Stack, Queue, Sorting, Binary Search 연습

완료 기준:

- `train`, `evaluate`, `predict`를 각각 실행할 수 있습니다.
- batch, epoch, loss, optimizer를 설명할 수 있습니다.
- evaluation loop를 직접 구현할 수 있습니다.

## 5~6주차: 실제 이미지 데이터

메인 프로젝트: 소규모 custom image classifier

- [ ] 이미지 폴더와 class 구성
- [ ] Pillow 또는 OpenCV로 데이터 확인
- [ ] augmentation 적용
- [ ] ResNet18 fine-tuning
- [ ] confusion matrix 작성
- [ ] 실패 사례 분석
- [ ] learning rate 실험

완료 기준:

```powershell
python train.py
python evaluate.py
python predict.py --image sample.jpg
```

세 명령을 각각 실행할 수 있습니다.

## 7~8주차: C++ 시작

- [ ] 함수, `vector`, `string`
- [ ] `unordered_map`
- [ ] class와 reference
- [ ] header/source 분리
- [ ] CMake
- [ ] OpenCV로 이미지 읽기
- [ ] Python으로 풀었던 LeetCode 문제 15개를 C++로 재작성

## 9~10주차: 배포까지 연결

- [ ] PyTorch 모델을 ONNX로 export
- [ ] ONNX Runtime Python inference
- [ ] PyTorch와 ONNX 출력 비교
- [ ] 가능하면 C++ ONNX Runtime inference
- [ ] latency와 model size 측정
- [ ] README 작성

## 일일 루틴: 3시간 기준

- Python/CS 개념: 30분
- LeetCode Easy 1문제: 40분
- PyTorch 프로젝트: 90분
- 코드 재작성 및 학습 기록: 20분

## 구현 학습 규칙

1. 먼저 20~30분 직접 시도합니다.
2. 정답 전체보다 오류 원인이나 hint를 먼저 찾습니다.
3. 참고한 코드는 각 부분의 역할을 설명합니다.
4. 다음 날 핵심 코드를 보지 않고 다시 작성합니다.
5. 실행 성공과 개념 이해를 별도로 확인합니다.

## 첫날 체크리스트

- [ ] Running Sum 문제를 손으로 계산
- [ ] `list`, `for`, accumulator 개념 확인
- [ ] `running_sum()` 직접 구현
- [ ] LeetCode 제출
- [ ] 풀이를 보지 않고 다시 작성
- [ ] Day 1 `README.md`에 학습 내용 기록
