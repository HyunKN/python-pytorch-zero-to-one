# 03 — JSON 데이터 읽기

JSON 파일을 읽어 record 개수와 category별 개수를 계산합니다.

## 구현할 기능

- `pathlib.Path`로 파일 경로 처리
- `json` module로 파일 읽기
- 전체 record 수 계산
- category별 개수를 `dict`로 집계

## 배울 내용

- `with open(...)`
- JSON과 Python 자료구조의 대응
- dict에 없는 key 처리
- 파일 경로와 UTF-8 encoding

## 완료 기준

- [ ] JSON 파일을 UTF-8로 읽음
- [ ] category별 개수를 정확히 반환
- [ ] 파일 읽기와 데이터 집계를 함수로 분리
