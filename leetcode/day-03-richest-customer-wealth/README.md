# Day 03 — Richest Customer Wealth

- Status: Accepted

## 직접 기록

# Python Richest Customer Wealth 핵심 정리

## Point 1. 최댓값 변수는 for문 **밖**에서 초기화한다

for문 **안**에서 초기화하면 고객 한 명을 볼 때마다 최댓값이 다시 0으로 돌아간다.

```python
# 잘못된 예
for account in accounts:
    max_wealth = 0  # 매번 0으로 초기화됨
    ...
```

```python
# 올바른 예
max_wealth = 0  # for문 밖에서 한 번만 초기화

for account in accounts:
    ...
```

---

## Point 2. for문에서 매개변수 이름을 써야 한다

`List`는 타입 힌트이고 실제 데이터가 담긴 변수는 함수가 받은 매개변수이다.

```python
# 잘못된 예
for list in List:
    ...
```

```python
# 올바른 예
for account in accounts:
    ...
```

---

## Point 3. `list`, `max`는 변수명으로 쓰지 않는다

`list`와 `max`는 파이썬 기본 내장 함수 이름이다.
변수명으로 쓰면 기본 기능을 덮어써서 예상치 못한 오류가 생긴다.

```python
# 나쁜 예
list = []
max = 0
```

```python
# 좋은 예
account = []
max_wealth = 0
```

---

## Point 4. 두 가지 풀이 방식

### 방식 1. 이중 for문 (명시적)

```python
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            total = 0

            for money in account:
                total += money

            if total > max_wealth:
                max_wealth = total

        return max_wealth
```

### 방식 2. `sum()` + `max()` (간결)

```python
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(account) for account in accounts)
```

---

## Point 5. 한 줄 풀이 분석 — `max(sum(account) for account in accounts)`

한 줄처럼 보이지만 안쪽부터 세 단계로 작동한다.

### 단계 1. `for account in accounts` — 고객 한 명씩 꺼내기

`accounts`의 각 원소(고객의 잔고 리스트)를 `account`에 하나씩 담는다.

```python
accounts = [[1, 2, 3], [3, 2, 1], [5, 5]]

# account가 순서대로 취하는 값
account = [1, 2, 3]
account = [3, 2, 1]
account = [5, 5]
```

### 단계 2. `sum(account)` — 고객 한 명의 총 자산 계산

`sum()`은 리스트 안의 숫자를 전부 더한다.
이중 for문으로 직접 더하던 것을 `sum()`이 대신한다.

```python
sum([1, 2, 3])  # -> 6
sum([3, 2, 1])  # -> 6
sum([5, 5])     # -> 10
```

### 단계 3. `max(...)` — 가장 큰 값 반환

`max()`는 여러 값 중 가장 큰 값을 반환한다.
`sum(account) for account in accounts` 전체가 `max()`에 넘겨지는 값의 묶음이다.

```python
max(6, 6, 10)  # -> 10
```

### 괄호 안의 `... for ... in ...` — 제너레이터 표현식

`sum(account) for account in accounts`는 **제너레이터 표현식**이다.
리스트를 미리 만들지 않고 값을 하나씩 계산해서 `max()`에 넘긴다.

```python
# 리스트로 바꿔서 보면 이렇게 이해할 수 있다
[sum(account) for account in accounts]  # -> [6, 6, 10]
max([6, 6, 10])                         # -> 10
```

### 전체 흐름 요약

```text
accounts의 각 account에 대해
  → sum(account)로 총 자산을 계산하고
  → max()로 그 중 가장 큰 값을 반환한다
```

---

## 흐름 예시

```python
accounts = [[1, 2, 3], [3, 2, 1], [5, 5]]
```

각 고객의 합:

```text
[1, 2, 3] -> 6
[3, 2, 1] -> 6
[5, 5]    -> 10
```

최댓값은 `10`.

---

## 최종 기억

```text
최댓값 변수는 for문 밖에서 만들기
각 리스트의 합은 for문 안에서 계산하기
마지막에 return 하기
파이썬 내장 함수 이름(list, max)은 변수명으로 쓰지 않기
```
