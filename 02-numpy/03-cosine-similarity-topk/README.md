# 03 — Cosine Similarity와 Top-K

## 무엇을 배우나

여러 embedding 중 query 방향과 가장 가까운 항목을 찾습니다. L2 normalization, matrix multiplication, 정렬을 retrieval 흐름으로 연결합니다.

## 1. 완성 예제 실행

```powershell
python 02-numpy/03-cosine-similarity-topk/demo.py
```

`[1, 0]` query와 같은 방향인 `cat`의 score가 `1.0`으로 가장 높아야 합니다.

## 2. 코드 흐름

1. embedding matrix와 query dimension을 확인합니다.
2. 각 vector의 L2 norm을 계산합니다.
3. vector를 norm으로 나눠 단위 vector로 만듭니다.
4. matrix multiplication으로 모든 cosine score를 한 번에 계산합니다.
5. score를 내림차순으로 정렬해 Top-K를 선택합니다.

## 3. 직접 구현과 검증

[exercise.py](exercise.py)의 `cosine_top_k()`를 구현합니다.

```powershell
python 02-numpy/03-cosine-similarity-topk/check.py
```

## 완료 기준

- Python loop 없이 similarity 계산
- Top-K index와 score를 내림차순 반환
- zero vector가 문제인 이유 설명
- [notes.md](notes.md) 작성
