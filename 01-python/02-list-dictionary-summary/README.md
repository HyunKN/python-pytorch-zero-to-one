# 02 — List와 Dictionary 요약

## 무엇을 배우나

여러 상품 `dict`를 순회하며 전체 재고, 최고가 상품, 재고 부족 상품을 계산합니다. 반복할 때 어떤 변수를 계속 갱신해야 하는지 배웁니다.

## 1. 완성 예제 실행

```powershell
python 01-python/02-list-dictionary-summary/demo.py
```

예상 핵심 결과:

```text
total_stock: 18
most_expensive: mug
low_stock: [mug]
```

## 2. 코드 흐름

1. 전체 재고를 저장할 accumulator를 만듭니다.
2. 각 상품의 `name`, `price`, `stock`을 꺼냅니다.
3. 재고를 더하고 지금까지의 최고 가격과 비교합니다.
4. 재고가 기준 이하이면 이름을 별도 list에 추가합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `summarize_products()`를 구현한 뒤 실행합니다.

```powershell
python 01-python/02-list-dictionary-summary/check.py
```

## 완료 기준

- 입력 list를 수정하지 않음
- 세 집계 결과가 정확함
- 반복마다 갱신되는 변수를 설명 가능
- [notes.md](notes.md) 작성
