# Day 06 — Two Sum

## Problem

- LeetCode: [1. Two Sum](https://leetcode.com/problems/two-sum/)
- 정수 배열 `nums`와 목표 정수 `target`이 주어졌을 때, 합해서 `target`이 되는 두 숫자의 **인덱스**를 반환합니다.

예시:

```python
nums = [2, 3, 8, 7]
target = 9
```

`2 + 7 = 9`이고, `2`는 `0번 인덱스`, `7`은 `3번 인덱스`이므로 정답은 다음과 같습니다.

```python
[0, 3]
```

---

## 오늘 배울 내용

### 1. `enumerate()` 함수

```python
for i, num in enumerate(nums):
```

`enumerate(nums)`는 `nums`를 순회하면서 **인덱스와 값**을 동시에 꺼내 줍니다.

예를 들어:

```python
nums = [2, 3, 8, 7]
```

이면 `enumerate(nums)`는 다음처럼 동작합니다.

```text
i = 0, num = 2
i = 1, num = 3
i = 2, num = 8
i = 3, num = 7
```

중요한 점:

```text
enumerate는 매번 처음부터 다시 도는 것이 아니다.
nums를 앞에서부터 끝까지 한 번만 순서대로 돈다.
```

즉, 아래 코드와 거의 같은 의미입니다.

```python
for i in range(len(nums)):
    num = nums[i]
```

---

### 2. 딕셔너리 `seen`의 역할

```python
seen = {}
```

`seen`은 **이미 지나온 숫자들을 저장하는 기록장**입니다.

구조는 다음과 같습니다.

```python
seen = {
    숫자: 인덱스
}
```

예를 들어:

```python
seen = {
    2: 0,
    3: 1,
    8: 2
}
```

이 뜻은 다음과 같습니다.

```text
숫자 2는 0번 인덱스에서 봤다.
숫자 3은 1번 인덱스에서 봤다.
숫자 8은 2번 인덱스에서 봤다.
```

중요한 점:

```text
seen은 nums 전체를 처음부터 넣어둔 것이 아니다.
for문을 돌면서 하나씩 직접 넣는다.
```

`seen`에 값을 넣는 코드는 바로 이 줄입니다.

```python
seen[num] = i
```

예를 들어 현재 `num = 2`, `i = 0`이면 실제로는 다음 코드가 실행되는 것입니다.

```python
seen[2] = 0
```

---

### 3. `need`는 무엇인가?

```python
need = target - num
```

현재 숫자 `num`과 더해서 `target`을 만들기 위해 필요한 숫자입니다.

예를 들어:

```python
target = 9
num = 2
```

이면:

```python
need = 9 - 2
need = 7
```

뜻:

```text
현재 숫자가 2니까,
2와 더해서 9가 되려면 7이 필요하다.
```

---

### 4. `if need in seen`의 의미

```python
if need in seen:
```

이 코드는 다음 뜻입니다.

```text
내가 필요한 숫자 need가
이전에 지나온 숫자 기록장 seen 안에 key로 존재하는가?
```

여기서 중요한 점은 `nums` 리스트에서 찾는 것이 아니라는 점입니다.

```python
if need in nums:
```

가 아닙니다.

이 코드는 리스트를 앞에서부터 찾는 방식이 될 수 있습니다.

하지만 실제 풀이에서는:

```python
if need in seen:
```

을 사용합니다.

즉, 딕셔너리의 **key** 중에서 `need`가 있는지 확인합니다.

예를 들어:

```python
seen = {
    2: 0,
    3: 1,
    8: 2
}
```

일 때:

```python
if 2 in seen:
```

은 다음 뜻입니다.

```text
seen 딕셔너리에 key가 2인 값이 있는가?
```

있기 때문에 참입니다.

그리고:

```python
seen[2]
```

의 값은 `0`입니다.

즉:

```text
숫자 2는 0번 인덱스에서 봤다.
```

---

### 5. 딕셔너리가 빠른 이유

리스트에서 어떤 값을 찾으면 앞에서부터 하나씩 확인해야 할 수 있습니다.

```python
if need in nums:
```

이 경우는 대략 다음 느낌입니다.

```text
nums[0] 확인
nums[1] 확인
nums[2] 확인
...
```

하지만 딕셔너리는 내부적으로 **해시 테이블(Hash Table)** 을 사용합니다.

그래서:

```python
if need in seen:
```

은 평균적으로 다음처럼 동작합니다.

```text
need의 해시값 계산
→ 해당 key가 있을 만한 위치로 이동
→ key가 있는지 확인
```

즉, 보통은 딕셔너리 전체를 for문처럼 처음부터 끝까지 다시 돌지 않습니다.

그래서 딕셔너리 key 탐색은 평균적으로 `O(1)`입니다.

---

## 최종 코드

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i
```

---

## 구현 순서

1. `seen = {}`으로 빈 딕셔너리를 만든다.
2. `enumerate(nums)`로 `nums`를 앞에서부터 한 번만 돈다.
3. 현재 숫자 `num`을 기준으로 필요한 짝꿍 숫자 `need = target - num`을 계산한다.
4. `if need in seen:`으로 짝꿍 숫자가 이전에 나온 적 있는지 확인한다.
5. 있다면 `[seen[need], i]`를 반환한다.
6. 없다면 현재 숫자를 나중에 찾을 수 있도록 `seen[num] = i`로 저장한다.
7. 답을 찾으면 `return` 때문에 함수가 즉시 종료된다.
8. 운이 안 좋으면 끝까지 돌 수도 있지만, 그래도 `nums`는 최대 한 번만 돈다.

---

## 디버깅 예시

```python
nums = [2, 3, 8, 7]
target = 9
```

초기 상태:

```python
seen = {}
```

| 반복 | i | num | need = target - num | 확인하는 코드 | seen 상태 | 결과 |
|---:|---:|---:|---:|---|---|---|
| 시작 | - | - | - | - | `{}` | 시작 |
| 1 | 0 | 2 | 7 | `7 in seen` | `{}` | 없음 → `seen[2] = 0` |
| 2 | 1 | 3 | 6 | `6 in seen` | `{2: 0}` | 없음 → `seen[3] = 1` |
| 3 | 2 | 8 | 1 | `1 in seen` | `{2: 0, 3: 1}` | 없음 → `seen[8] = 2` |
| 4 | 3 | 7 | 2 | `2 in seen` | `{2: 0, 3: 1, 8: 2}` | 있음 → `[0, 3]` 반환 |

네 번째 반복에서:

```python
num = 7
need = 9 - 7
need = 2
```

현재 `seen`은 다음과 같습니다.

```python
seen = {
    2: 0,
    3: 1,
    8: 2
}
```

따라서:

```python
if 2 in seen:
```

이 참이 됩니다.

그리고:

```python
seen[2]
```

는 `0`입니다.

현재 인덱스 `i`는 `3`입니다.

그래서 최종 반환은 다음과 같습니다.

```python
return [0, 3]
```

---

## 직접 디버그 출력 코드

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i, num in enumerate(nums):
            print()
            print(f"[반복 시작] i={i}, num={num}")
            print("현재 seen:", seen)

            need = target - num
            print(f"need = target - num = {target} - {num} = {need}")

            print(f"{need}가 seen에 있는지 확인:", need in seen)

            if need in seen:
                print(f"발견! seen[{need}] = {seen[need]}, 현재 i = {i}")
                return [seen[need], i]

            seen[num] = i
            print(f"없으므로 seen[{num}] = {i} 저장")
            print("저장 후 seen:", seen)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 8, 7]
    target = 9

    print("--- 디버깅 시작 ---")
    result = sol.twoSum(nums, target)
    print("최종 결과:", result)
```

예상 출력:

```text
--- 디버깅 시작 ---

[반복 시작] i=0, num=2
현재 seen: {}
need = target - num = 9 - 2 = 7
7가 seen에 있는지 확인: False
없으므로 seen[2] = 0 저장
저장 후 seen: {2: 0}

[반복 시작] i=1, num=3
현재 seen: {2: 0}
need = target - num = 9 - 3 = 6
6가 seen에 있는지 확인: False
없으므로 seen[3] = 1 저장
저장 후 seen: {2: 0, 3: 1}

[반복 시작] i=2, num=8
현재 seen: {2: 0, 3: 1}
need = target - num = 9 - 8 = 1
1가 seen에 있는지 확인: False
없으므로 seen[8] = 2 저장
저장 후 seen: {2: 0, 3: 1, 8: 2}

[반복 시작] i=3, num=7
현재 seen: {2: 0, 3: 1, 8: 2}
need = target - num = 9 - 7 = 2
2가 seen에 있는지 확인: True
발견! seen[2] = 0, 현재 i = 3
최종 결과: [0, 3]
```

---

## 내가 헷갈렸던 부분과 정리

### Q1. `twoSum`은 뭐지?

`twoSum`은 특별한 문법이 아니라 함수 이름입니다.

문제 이름이 Two Sum이라서 함수 이름도 `twoSum`으로 쓰는 것입니다.

---

### Q2. `enumerate`는 나올 때까지 처음부터 다시 도는 건가?

아닙니다.

`enumerate(nums)`는 `nums`를 앞에서부터 끝까지 한 번만 순서대로 돕니다.

```text
0번 인덱스 → 1번 인덱스 → 2번 인덱스 → 3번 인덱스
```

처럼 한 칸씩 넘어갑니다.

---

### Q3. `seen`에는 값이 어떻게 들어가는가?

이 줄 때문에 들어갑니다.

```python
seen[num] = i
```

현재 숫자 `num`을 key로, 현재 인덱스 `i`를 value로 저장합니다.

예:

```python
num = 2
i = 0
seen[num] = i
```

실제로는:

```python
seen[2] = 0
```

입니다.

---

### Q4. `seen`은 바로 전 것만 보는가?

아닙니다.

`seen`은 바로 전 숫자 하나만 저장하는 것이 아니라, **지금까지 지나온 모든 숫자**를 저장합니다.

예를 들어 세 번째 반복이 끝나면:

```python
seen = {
    2: 0,
    3: 1,
    8: 2
}
```

처럼 이전에 봤던 값들이 계속 쌓입니다.

---

### Q5. `if need in seen`은 무슨 코드인가?

이 코드는 `need`가 `seen` 딕셔너리의 key로 존재하는지 확인합니다.

```python
if need in seen:
```

예를 들어:

```python
need = 2
seen = {2: 0, 3: 1, 8: 2}
```

이면 `2`라는 key가 있으므로 참입니다.

---

### Q6. 결국 찾을 때 또 for문을 도는 것 아닌가?

리스트라면 그럴 수 있습니다.

하지만 딕셔너리는 해시 테이블을 사용하기 때문에 평균적으로 전체를 다시 돌지 않고 key를 빠르게 찾습니다.

그래서:

```python
if need in seen:
```

은 평균적으로 `O(1)`입니다.

---

### Q7. 답을 찾으면 어떻게 되는가?

답을 찾으면 이 줄이 실행됩니다.

```python
return [seen[need], i]
```

`return`이 실행되면 함수가 바로 종료됩니다.

따라서 답을 찾은 뒤에는 남은 반복을 더 돌지 않습니다.

---

## Approach

### 1. 브루트 포스

이중 반복문으로 모든 숫자 쌍을 직접 더해보는 방식입니다.

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

이 방식은 이해하기 쉽지만 모든 조합을 확인해야 하므로 시간 복잡도가 `O(N^2)`입니다.

---

### 2. 해시 맵 / 딕셔너리

현재 숫자의 짝꿍이 이전에 나왔는지 딕셔너리에서 확인합니다.

```python
need = target - num

if need in seen:
    return [seen[need], i]

seen[num] = i
```

이 방식은 `nums`를 한 번만 순회하므로 시간 복잡도가 `O(N)`입니다.

---

## Complexity

- Time: `O(N)`
  - `nums`를 최대 한 번만 순회합니다.
  - `need in seen`은 딕셔너리 key 탐색이므로 평균적으로 `O(1)`입니다.
- Space: `O(N)`
  - 최악의 경우 답이 마지막에 발견되거나 없을 때, 많은 값을 `seen`에 저장해야 합니다.

---

## Mistakes

- 처음에는 이중 반복문으로 모든 숫자 쌍을 비교하는 방식만 떠올렸습니다.
- `enumerate()`가 매번 처음부터 다시 도는 것처럼 헷갈렸지만, 실제로는 리스트를 한 번만 순서대로 돕니다.
- `seen`에 `nums` 전체가 처음부터 들어가 있는 것으로 헷갈렸지만, 실제로는 `seen[num] = i` 줄에서 하나씩 저장됩니다.
- `seen`이 바로 전 숫자만 보는 것으로 헷갈렸지만, 실제로는 지금까지 지나온 모든 숫자를 저장합니다.
- `if need in seen`이 `nums` 리스트에서 찾는 것처럼 헷갈렸지만, 실제로는 딕셔너리의 key를 찾는 코드입니다.
- 딕셔너리에서 key를 찾는 것도 결국 for문처럼 전체를 도는 줄 알았지만, 해시 테이블 덕분에 평균적으로 `O(1)`에 찾을 수 있습니다.
- 양수만 있을 것으로 오해하여 `nums[i] > target`일 때 `continue` 하려 했지만, 음수가 포함될 수 있으면 이 방식은 틀릴 수 있습니다.

---

## 핵심 암기 문장

```text
Two Sum 딕셔너리 풀이는
현재 숫자의 짝꿍이 이전에 나온 적 있는지를 seen에서 확인하는 방식이다.
```

```text
seen은 지금까지 지나온 숫자들의 기록장이다.
key는 숫자, value는 인덱스다.
```

```text
if need in seen은 nums에서 찾는 것이 아니라
seen 딕셔너리의 key 중 need가 있는지 확인하는 코드다.
```

---

## Revisit

- 다음 날 재풀이:
  - `seen = {}`을 만들고 시작할 수 있는가?
  - `for i, num in enumerate(nums):`를 직접 쓸 수 있는가?
  - `need = target - num`을 떠올릴 수 있는가?
  - `if need in seen:`을 먼저 확인하고, 없으면 `seen[num] = i`를 저장하는 순서를 기억하는가?
- 코드를 보지 않고 작성했는가:
  - `return [seen[need], i]`에서 왜 `seen[need]`와 `i`를 반환하는지 설명할 수 있어야 한다.
- 다시 설명하기 어려운 부분:
  - `seen[num] = i`가 언제 실행되는가?
  - `if need in seen`은 무엇을 찾는가?
  - 딕셔너리가 왜 리스트 탐색보다 빠른가?
