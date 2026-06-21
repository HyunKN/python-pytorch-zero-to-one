# 한국어 실습 Curriculum 설계

## 목표

Python 문법부터 PyTorch Vision 모델 학습과 ONNX Runtime 배포까지 순서대로 진행할 수 있는 16단계 구현 중심 curriculum을 구성한다.

## 범위

- Python 기초와 데이터 처리
- NumPy 배열 연산
- PyTorch Tensor, autograd, 모델 학습
- FashionMNIST와 custom image dataset
- ResNet fine-tuning과 오류 분석
- ONNX export, parity, latency 측정

C++는 이 저장소에서 제외하고 이후 별도 저장소로 분리한다.

## 언어

- 학습 설명과 기록 template은 한국어로 작성한다.
- 코드 identifier와 `Tensor`, `Dataset`, `DataLoader`, `ONNX` 같은 technical terms는 English를 유지한다.
- 예시는 기존 프로젝트와 무관한 동물, 상품, 일반 이미지 데이터를 사용한다.

## 폴더 구조

각 단계는 주제별 상위 폴더 아래에 전체 과정 순번을 유지한다.

```text
python/01~04
numpy/05~07
pytorch/08~14
deployment/15~16
```

각 과제 폴더는 다음 파일을 가진다.

- `README.md`: 목표, 구현 요구사항, 완료 기준
- `starter.py`: 정답 없이 함수와 실행 진입점만 제공
- `notes.md`: Approach, 새로 배운 내용, Mistakes, Revisit 기록

## 진행 방식

루트 README의 1~16 roadmap을 따라간다. 현재 단계를 완료하면 상태를 `✅`로 바꾸고 다음 단계로 이동한다. LeetCode는 별도의 병행 과정으로 유지한다.

## 검증

- 16개 roadmap 링크가 모두 실제 폴더를 가리켜야 한다.
- 모든 `starter.py`가 Python syntax check를 통과해야 한다.
- starter에는 완성된 정답을 넣지 않는다.
- README와 학습 계획에 C++ 단계가 남아 있지 않아야 한다.
