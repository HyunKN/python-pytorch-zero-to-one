# 15 — ONNX Export와 Parity

PyTorch 모델을 ONNX로 변환하고 두 runtime의 출력이 충분히 가까운지 확인합니다.

## 구현할 기능

- sample input 준비
- `torch.onnx.export()` 실행
- ONNX Runtime inference
- PyTorch/ONNX output의 max absolute difference 계산
- tolerance 기준 parity 판정

## 배울 내용

- model export
- input/output name과 shape
- eval mode
- numerical parity와 tolerance

## 완료 기준

- [ ] ONNX 파일 생성
- [ ] 동일한 입력으로 두 runtime 실행
- [ ] max absolute difference와 cosine similarity 기록
- [ ] parity 기준과 결과 설명
