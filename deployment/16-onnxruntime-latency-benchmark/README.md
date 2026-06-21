# 16 — ONNX Runtime Latency Benchmark

ONNX Runtime inference 시간을 반복 측정하고 median과 p90 latency를 계산합니다.

## 구현할 기능

- ONNX Runtime session 생성
- warm-up과 측정 run 분리
- `perf_counter()`로 latency 측정
- median, p90, min, max 계산
- model size와 실행 환경 기록

## 배울 내용

- benchmark 조건 통제
- warm-up
- latency distribution
- 숫자와 결론을 구분하는 방법

## 완료 기준

- [ ] warm-up을 측정값에서 제외
- [ ] 최소 100회 반복 측정
- [ ] median과 p90 함께 보고
- [ ] device, runtime version, input shape 기록
