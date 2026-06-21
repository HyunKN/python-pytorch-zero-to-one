# Day 01 — Running Sum of 1d Array

## Problem

- LeetCode: [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)
- 입력 배열의 각 위치까지 누적된 합을 새로운 배열로 반환합니다.

```text
Input:  [1, 2, 3, 4]
Output: [1, 3, 6, 10]
```

## 오늘 배울 내용

- Python `list`
- `range()`와 index
- in-place update
- method parameter와 `return`

## 구현 순서

1. 두 번째 원소부터 마지막 원소까지 index로 순회합니다.
2. 현재 원소에 바로 이전 위치까지의 누적합을 더합니다.
3. 수정된 `nums`를 반환합니다.

검증은 LeetCode에서 수행하고 Accepted된 답을 [solution.py](solution.py)에 저장합니다.

## 풀이 결과

- Status: Accepted

## 직접 기록

### Approach

두 번째 원소부터 순회하며 이전 위치에 저장된 누적합을 현재 원소에 더합니다. 별도의 결과 list를 만들지 않고 입력 list를 직접 수정합니다.

### Complexity

- Time: `O(n)`
- Space: `O(1)` auxiliary space

### Mistakes

막힌 문법, 잘못 예상한 출력, 수정한 이유를 기록합니다.

### Revisit

- 다음 날 재풀이:
- 코드를 보지 않고 작성했는가:
- 다시 설명하기 어려운 부분:
