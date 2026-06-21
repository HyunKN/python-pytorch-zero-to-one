# Curriculum 검증 보고서

검증일: 2026-06-22
검증 환경: Windows, Python 3.12.10, CPU

## 검증한 환경

`requirements.txt`를 저장소의 `.venv`에 설치한 뒤 다음을 확인했습니다.

- `pip check`: broken requirement 없음
- NumPy: 2.4.6
- Pillow: 12.2.0
- PyTorch: 2.12.1+cpu
- torchvision: 0.27.1+cpu
- ONNX: 1.22.0
- ONNX Runtime: 1.27.0
- ONNX Script: 0.7.0

## 자동 검증

다음 명령으로 완성 demo의 unit/smoke test를 실행했습니다.

```powershell
python -m unittest discover -s tests -v
```

결과: 17 tests, 17 passed, 0 failed.

검증 범위:

- Python 데이터 처리 4단계
- NumPy 연산 3단계
- PyTorch·Vision 7단계
- ONNX deployment 2단계

## 실제 script 실행

16개 `demo.py`를 각각 Python script로 실행했습니다.

결과: 16개 모두 exit code 0.

이 검증은 import만 확인한 것이 아니라 각 demo의 `main()`과 실제 출력 경로를 실행한 결과입니다.

## 실제 dataset과 pretrained model 검증

### FashionMNIST MLP

```powershell
python 03-pytorch/03-fashion-mnist-mlp/demo.py --full-data --epochs 1
```

- train loss: 0.4995
- validation accuracy: 0.8385
- checkpoint 저장 성공

### FashionMNIST CNN

```powershell
python 03-pytorch/04-fashion-mnist-cnn/demo.py --full-data --epochs 1
```

- trainable parameters: 105,866
- train loss: 0.5067
- validation accuracy: 0.8639

### Pretrained ResNet18

- pretrained weight load 성공
- classifier output class 수를 3으로 교체
- input `(1, 3, 224, 224)` forward output `(1, 3)` 확인
- frozen backbone 상태에서 trainable parameter Tensor 2개 확인

위 accuracy는 한 번의 CPU 실행에서 얻은 reference 값이며 성능 목표나 재현 보장값이 아닙니다.

## ONNX 검증

- 최신 `torch.export` 기반 ONNX exporter 사용
- ONNX file 생성 성공
- ONNX checker 통과
- ONNX Runtime CPU inference 성공
- PyTorch/ONNX max absolute difference: `1.49e-08`
- cosine similarity: `0.999999999999996`
- parity: true

Latency demo는 작은 예제 모델의 benchmark 흐름을 검증하기 위한 것입니다. 측정값을 실제 제품 모델 성능으로 해석하면 안 됩니다.

## 문서와 구조 검증

- 학습 단계: 16개
- 각 단계의 필수 파일: `README.md`, `demo.py`, `exercise.py`, `check.py`, `notes.md`
- 누락된 필수 파일: 0개
- 깨진 local Markdown link: 0개
- README에서 필수 학습 순서가 누락된 단계: 0개
- `check.py`가 요구하는 API와 `exercise.py` API 불일치: 0개

저장소에 포함된 verifier도 통과했습니다.

```powershell
python scripts/verify_repository.py
```

결과: Repository verification PASS.

## 정적 검증

완성 demo, check, test 코드를 Ruff로 검사했습니다.

```powershell
ruff check . --exclude .venv --exclude exercise.py
```

결과: All checks passed.

`exercise.py`는 학습자가 구현하도록 의도적으로 stub과 선행 import를 포함하므로 lint 대상에서는 제외하고 syntax compile만 검사합니다.

## Exercise 검증 흐름

구현 전 16개 `check.py`를 실행해 모두 친절한 `FAIL: NotImplementedError: ...` 메시지와 exit code 1을 반환하는 것을 확인했습니다. 학습자가 `exercise.py`를 구현하면 같은 check가 PASS 여부를 판정합니다.

## 아직 검증하지 않은 범위

- CUDA/GPU 실행
- Linux와 macOS 환경
- 여러 epoch에 대한 model accuracy 안정성
- 대규모 custom image dataset
- 실제 production model의 ONNX 성능

이 항목은 현재 curriculum의 입문 목적을 벗어나므로 완료된 것으로 주장하지 않습니다.
