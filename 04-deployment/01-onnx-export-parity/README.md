# 01 — ONNX Export와 Parity

## 무엇을 배우나

PyTorch 모델을 fixed input shape의 ONNX로 export하고 ONNX Runtime에서 같은 입력을 실행해 두 output이 충분히 가까운지 확인합니다.

## 1. 완성 예제 실행

```powershell
python 04-deployment/01-onnx-export-parity/demo.py
```

`artifacts/demo_model.onnx`가 생성되고 다음 값이 출력됩니다.

- PyTorch/ONNX output shape
- max absolute difference
- cosine similarity
- tolerance 기준 parity 결과

## 2. 코드 흐름

1. 모델을 `eval()` mode로 바꿉니다.
2. sample input과 input/output name을 지정해 ONNX로 export합니다.
3. ONNX Runtime CPU session을 만듭니다.
4. 같은 값을 PyTorch와 ONNX Runtime에 입력합니다.
5. max difference, cosine similarity, `allclose` 결과를 비교합니다.

이 입문 예제는 이해하기 쉬운 fixed shape를 사용합니다. Dynamic shape는 exporter의 `dynamic_shapes` API를 별도 학습한 뒤 추가합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 export, ONNX inference, output 비교 함수를 구현합니다.

```powershell
python 04-deployment/01-onnx-export-parity/check.py
```

## 완료 기준

- 실제 ONNX 파일 생성
- ONNX checker와 Runtime 실행 성공
- max difference와 cosine similarity 의미 설명
- [notes.md](notes.md)에 tolerance와 결과 기록
