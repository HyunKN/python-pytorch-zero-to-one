# 03 — JSON 데이터 읽기

## 무엇을 배우나

JSON 파일을 Python 자료구조로 읽고 category별 개수를 집계합니다. 파일 I/O와 데이터 처리를 서로 다른 함수로 분리합니다.

## 1. 완성 예제 실행

```powershell
python 01-python/03-json-data-reader/demo.py
```

demo는 임시 JSON 파일을 직접 생성하므로 별도 data가 필요하지 않습니다.

예상 출력:

```text
전체 record 수: 3
category별 개수: {'fruit': 2, 'vegetable': 1}
```

## 2. 코드 흐름

1. `Path.open()`과 UTF-8 encoding으로 파일을 엽니다.
2. `json.load()`로 Python list를 만듭니다.
3. 각 record의 `category`를 읽습니다.
4. `dict.get()`으로 기존 개수를 가져와 1을 더합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `load_records()`와 `count_categories()`를 구현합니다.

```powershell
python 01-python/03-json-data-reader/check.py
```

## 완료 기준

- 파일 읽기와 집계 함수가 분리됨
- JSON list와 dict 구조를 설명 가능
- category가 처음 등장할 때의 처리를 설명 가능
- [notes.md](notes.md) 작성
