# 12 — Custom Dataset과 DataLoader

직접 구성한 이미지 폴더와 label 정보를 PyTorch `Dataset`으로 읽습니다.

## 구현할 기능

- image path와 label 목록 저장
- `__len__()`과 `__getitem__()` 구현
- Pillow로 RGB 이미지 읽기
- transform 적용
- `DataLoader`에서 batch 확인

## 배울 내용

- `Dataset` protocol
- lazy loading
- transform pipeline
- batch와 shuffle

## 완료 기준

- [ ] image와 label이 정확히 연결됨
- [ ] batch image/label shape 확인
- [ ] train과 validation transform 차이 기록
