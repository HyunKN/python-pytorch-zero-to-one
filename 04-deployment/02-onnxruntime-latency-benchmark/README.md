# 02 — ONNX Runtime Latency Benchmark

## 무엇을 배우나

ONNX Runtime inference를 반복 측정해 median, p90, min, max latency를 계산하고 재현에 필요한 환경 정보를 함께 기록합니다.

## 1. 완성 예제 실행

```powershell
python 04-deployment/02-onnxruntime-latency-benchmark/demo.py
```

demo는 작은 ONNX 모델을 자동으로 생성하고 CPU provider에서 10회 warm-up 후 100회 측정합니다.

## 2. 코드 흐름

1. warm-up run은 runtime 초기화 영향을 제거하기 위해 측정값에서 제외합니다.
2. 각 inference 전후의 `perf_counter()` 차이를 millisecond로 바꿉니다.
3. 여러 측정값에서 median과 p90을 계산합니다.
4. model size, provider, ONNX Runtime version, input shape를 함께 기록합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 model 생성, benchmark, report 함수를 구현합니다.

```powershell
python 04-deployment/02-onnxruntime-latency-benchmark/check.py
```

## 완료 기준

- warm-up과 measured run 분리
- 100회 이상 측정
- median과 p90 차이 설명
- device/runtime/input shape/model size 기록
- [notes.md](notes.md)에 결과와 한계 작성
