# 06 — 이미지 Normalization

`uint8` 이미지 array를 모델 입력에 사용할 수 있는 `float32` 값으로 변환합니다.

## 구현할 기능

- 픽셀 범위를 `0~255`에서 `0~1`로 변환
- channel별 mean과 std 적용
- 입력과 같은 shape 유지
- `float32` dtype 반환

## 배울 내용

- dtype 변환
- broadcasting
- HWC image shape
- normalization의 목적

## 완료 기준

- [ ] 입력 array를 직접 수정하지 않음
- [ ] 출력 dtype이 `float32`
- [ ] broadcasting이 적용되는 dimension을 설명
