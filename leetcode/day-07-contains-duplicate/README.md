# Day 07 — Contains Duplicate

## Problem

- LeetCode: [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- 정수 배열 `nums`가 주어졌을 때, 어떤 값이 배열에 최소 두 번 이상 나타나면 `True`를, 모든 원소가 서로 다르면 `False`를 반환합니다.

## 오늘 배울 내용

- Set (집합)

## 구현 순서

1. `seen = set()`으로 빈 Set을 만든다.
2. `for num in nums:`로 앞에서부터 한 번만 돈다.
3. `if num in seen:`이면 중복이므로 `return True`.
4. 없으면 `seen.add(num)`으로 기록한다.
5. 끝까지 돌았는데 중복이 없으면 `return False`.

검증은 LeetCode에서 수행하고 Accepted된 답을 [solution.py](solution.py)에 저장합니다.

## 풀이 결과

- Status: ✅ Accepted

## 직접 기록

### Approach

Day 06에서 배운 **"이미 본 것을 해시에 기록해두고 탐색"** 아이디어를 이 문제에 응용했다.

Day 06은 인덱스 반환이 목적이라 `seen[num] = i`처럼 value가 필요했는데, 이 문제는 "본 적 있는가?"만 알면 되므로 value 자리에 의미 없는 `True`를 넣었다.

```python
seen = {}
for num in nums:
    if num in seen:
        return True
    seen[num] = True
```

이럴 때 Set을 쓰면 된다. key만 저장하고 value가 없는 구조다.

```diff
-seen = {}
+seen = set()

-seen[num] = True
+seen.add(num)
```

### 딕셔너리 vs Set — 기술적 비교

두 자료구조 모두 내부적으로 **해시 테이블**을 쓴다. 탐색·삽입 모두 평균 `O(1)`로 동일하다.

| | 딕셔너리 `dict` | Set `set` |
|---|---|---|
| 내부 구조 | hash(key) → (key, value) 저장 | hash(value) → value만 저장 |
| 빈 것 만들기 | `seen = {}` | `seen = set()` |
| 값 추가 | `seen[num] = True` | `seen.add(num)` |
| 값 확인 | `if num in seen` | `if num in seen` |
| 탐색·삽입 | 평균 `O(1)` | 평균 `O(1)` |
| 메모리 | key + value 쌍을 저장 | key만 저장 → 더 적음 |

주의: `{}`은 빈 딕셔너리다. 빈 Set은 반드시 `set()`으로 만든다.

### 더 나은 방법이 있는가?

**Set 한 줄 풀이:**

```python
return len(nums) != len(set(nums))
```

`set(nums)`는 중복을 자동 제거한다. 길이가 달라지면 중복이 있다는 뜻이다.

간결하지만 **항상 전체를 순회**한다. 앞에 중복이 있어도 끝까지 도는 것이다.

for문 방식은 중복 발견 즉시 `return True`로 끝낼 수 있어서 최선의 경우 `O(1)`에 가깝다.

```text
한 줄 풀이:  항상 O(N) — 조기 종료 없음
for문 풀이: 최선 O(1), 최악 O(N) — 조기 종료 있음
```

실용적으로는 둘 다 Accepted. 단, **조기 종료가 중요한 상황**이면 for문이 낫다.

### Day 06과의 차이

```text
Day 06: value(인덱스)가 필요  → 딕셔너리
Day 07: value가 필요 없음     → Set
```

### Complexity

- Time: `O(N)` — 한 번만 순회, `in` 탐색은 `O(1)`
- Space: `O(N)` — 최악의 경우 모든 값을 저장

### Mistakes

- Day 06 아이디어를 응용해 딕셔너리로 풀었는데, value(`True`)가 의미 없다는 걸 코드를 쓰면서 알아챘다.
- `{}`이 빈 Set인 줄 알았는데 빈 딕셔너리다. 빈 Set은 `set()`.

### Revisit

- 다음 날 재풀이:
- 코드를 보지 않고 작성했는가:
- 다시 설명하기 어려운 부분:
