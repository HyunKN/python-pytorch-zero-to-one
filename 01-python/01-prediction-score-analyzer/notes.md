# 학습 기록
26.06.22
## 접근 방식
demo를 보고 모르는 함수들을 검색 후 사용
## 새로 배운 내용
```text
zip() = 같은 위치끼리 묶기
for문 = 하나씩 꺼내 반복하기
List Comprehension = for문으로 리스트 만들기
sorted() = 정렬된 새 리스트 만들기
key=lambda x: x[n] = n번째 값을 정렬 기준으로 사용, lambda의 의미
threshold = 통과 여부를 판단하는 기준값으로 사용됨
```

### `zip()`
- **입력**: 여러 리스트 (list1, list2, list3.....)
- **리턴**: 같은 위치끼리 묶은 `zip` 객체
- **이유**: `label`과 `score`를 한 쌍으로 묶기 위해

```python
list(zip(labels, scores))
# [("cat", 0.9), ("dog", 0.7)]
```

### `for`
- **입력**: 반복 가능한 데이터
- **리턴**: 없음
- **이유**: 값을 하나씩 꺼내 처리하기 위해

```python
for label, score in ranked:
```

### List Comprehension
- **입력**: 반복문 + 만들 값
- **리턴**: 새 리스트
- **이유**: 리스트를 짧게 만들기 위해

```python
[item for item in data]
```

### `sorted()`
- **입력**: (정렬할 데이터, 기준, 순서)
- **리턴**: 정렬된 새 리스트
- **이유**: 점수 순으로 정렬하기 위해

```python
sorted(data, key=..., reverse=True)
```

### `key=lambda x: x[n]`
- **입력**: 원소 하나 `x`
- **리턴**: 정렬 기준값
- **이유**: n번째 값을 기준으로 정렬하기 위해

```python
key=lambda x: x[1]
```

## 실수와 해결

## 다시 구현

- 다시 구현한 날짜:
- 코드를 보지 않고 작성했는가:
