# Python · PyTorch Zero to One

완성된 예제를 먼저 실행하고 같은 기능을 직접 다시 구현하며 Python, NumPy, PyTorch, Vision, ONNX Runtime을 배우는 한국어 학습 저장소입니다.

## 최종 목표

```text
Python으로 데이터 처리
→ NumPy로 수치 연산
→ PyTorch로 모델 학습
→ Vision pipeline 구성
→ ONNX로 변환·검증·측정
```

문법 암기보다 다음 능력을 만드는 데 초점을 둡니다.

- 작은 프로그램의 입력·처리·출력을 설명하기
- 빈 함수의 핵심 로직을 직접 구현하기
- Tensor shape와 학습 흐름을 추적하기
- 모델을 export하고 output parity와 latency를 측정하기

## 처음 시작하기

검증 환경은 Python 3.12와 Windows PowerShell입니다.

```powershell
git clone https://github.com/HyunKN/python-pytorch-zero-to-one.git
cd python-pytorch-zero-to-one
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

PyTorch GPU 환경을 사용하려면 [PyTorch 공식 설치 안내](https://pytorch.org/get-started/locally/)에서 자신의 CUDA 환경에 맞는 명령을 사용합니다. 이 저장소의 `requirements.txt`는 재현 가능한 CPU 학습 환경을 기준으로 합니다.

## 한 단계의 학습 순서

모든 자체 실습 폴더는 같은 구조입니다.

```text
README.md    문제와 코드 흐름 설명
demo.py      먼저 실행하는 완성 코드
exercise.py  직접 구현하는 코드
check.py     exercise 자동 검증
notes.md     학습 기록
```

진행 순서:

1. `README.md`에서 목표와 예상 출력을 확인합니다.
2. `demo.py`를 실행해 전체 흐름을 관찰합니다.
3. demo를 닫고 `exercise.py`의 핵심 함수를 구현합니다.
4. `check.py`를 실행해 결과를 검증합니다.
5. `notes.md`를 작성하고 다음 날 다시 구현합니다.

자세한 방법은 [Top-down 학습 방법](docs/learning-method.md)을 참고합니다.

## Curriculum

상위 폴더 번호는 학습 영역의 순서이며, 내부 번호는 그 영역 안의 진행 순서입니다.

| 전체 단계 | 영역 | 실습 | 핵심 내용 | 상태 |
|---:|---|---|---|:---:|
| 01 | Python | [01. Prediction Score Analyzer](01-python/01-prediction-score-analyzer/) | list, dict, Top-K | ✅ |
| 02 | Python | [02. List와 Dictionary 요약](01-python/02-list-dictionary-summary/) | 반복문, 집계 | ⬜ |
| 03 | Python | [03. JSON 데이터 읽기](01-python/03-json-data-reader/) | file, JSON | ⬜ |
| 04 | Python | [04. 이미지 폴더 검사](01-python/04-image-folder-inspector/) | pathlib, filtering | ⬜ |
| 05 | NumPy | [01. Array와 Shape](02-numpy/01-array-and-shape/) | shape, dtype, axis | ⬜ |
| 06 | NumPy | [02. 이미지 Normalization](02-numpy/02-image-normalization/) | broadcasting, dtype | ⬜ |
| 07 | NumPy | [03. Cosine Similarity와 Top-K](02-numpy/03-cosine-similarity-topk/) | vector norm, retrieval | ⬜ |
| 08 | PyTorch | [01. Tensor 기초](03-pytorch/01-tensor-basics/) | Tensor, device | ⬜ |
| 09 | PyTorch | [02. Autograd와 Linear Regression](03-pytorch/02-autograd-linear-regression/) | gradient, optimizer | ⬜ |
| 10 | PyTorch | [03. FashionMNIST MLP](03-pytorch/03-fashion-mnist-mlp/) | training pipeline | ⬜ |
| 11 | PyTorch | [04. FashionMNIST CNN](03-pytorch/04-fashion-mnist-cnn/) | convolution, shape | ⬜ |
| 12 | Vision | [05. Custom Dataset과 DataLoader](03-pytorch/05-custom-dataset-dataloader/) | image loading, transform | ⬜ |
| 13 | Vision | [06. ResNet Fine-tuning](03-pytorch/06-resnet-finetuning/) | transfer learning | ⬜ |
| 14 | Vision | [07. 평가와 Error Analysis](03-pytorch/07-evaluation-error-analysis/) | metric, failure case | ⬜ |
| 15 | Deployment | [01. ONNX Export와 Parity](04-deployment/01-onnx-export-parity/) | export, output comparison | ⬜ |
| 16 | Deployment | [02. ONNX Runtime Latency](04-deployment/02-onnxruntime-latency-benchmark/) | warm-up, median, p90 | ⬜ |

진행 상태는 `⬜ 시작 전`, `🟨 구현 중`, `✅ 완료 기준 충족`으로 표시합니다.

전체 일정은 [10주 학습 계획](docs/study-plan.md)에 정리되어 있습니다.

구현과 실행을 검증한 범위, 실제 측정값, 검증하지 않은 항목은 [검증 보고서](docs/verification-report.md)에 분리해 기록합니다.

## LeetCode 병행 과정

LeetCode는 Python 문법, 자료구조, algorithmic thinking을 연습하는 별도 과정입니다. 검증은 LeetCode의 test와 hidden test를 사용하고 Accepted된 답만 저장합니다.

| Day | Problem | Topic | Status |
|---:|---|---|:---:|
| 01 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · [기록](leetcode/day-01-running-sum/) | Array, Loop | ✅ |
| 02 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Condition | ⬜ |
| 03 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Nested List, Loop | ⬜ |
| 04 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Array | ⬜ |
| 05 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | String, Index | ⬜ |
| 06 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash Map | ⬜ |
| 07 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Set | ⬜ |
| 08 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Map, String | ⬜ |
| 09 | [Majority Element](https://leetcode.com/problems/majority-element/) | Counting | ⬜ |
| 10 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | State Update | ⬜ |
| 11 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | String, Two Pointers | ⬜ |
| 12 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | ⬜ |
| 13 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | ⬜ |
| 14 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Binary Search | ⬜ |

## 저장소 전체 검증

먼저 구조, local link, check/exercise API, Python syntax를 확인합니다.

```powershell
python scripts/verify_repository.py
```

그다음 완성 demo의 unit/smoke test를 한 번에 실행합니다.

```powershell
python -m unittest discover -s tests -v
```

이 검증은 완성 예제의 동작을 확인합니다. 학습자가 작성하는 `exercise.py`는 각 폴더의 `check.py`로 별도 검증합니다.

정적 검사까지 재현하려면 다음을 실행합니다.

```powershell
python -m pip install -r requirements-dev.txt
ruff check . --exclude .venv --exclude exercise.py
```
