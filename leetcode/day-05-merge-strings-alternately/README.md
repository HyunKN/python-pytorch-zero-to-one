# Day 05 — Merge Strings Alternately

## Problem

- LeetCode: [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)
- 두 문자열 `word1`과 `word2`가 주어졌을 때, 두 문자열의 문자를 번갈아가며 결합하여 새로운 문자열을 생성합니다. 한쪽 문자열이 더 길면 남은 문자열을 뒤에 그대로 붙입니다.

## 오늘 배울 내용

- String, Index

## 구현 순서

1. `word1`과 `word2` 중 더 긴 길이를 찾아 반복문의 횟수(`strSize`)로 설정합니다.
2. `range(strSize)`를 사용하여 0부터 `strSize - 1`까지 반복합니다.
3. 인덱스 `i`가 `word1`의 길이보다 작다면 `word1[i]`를 결과 문자열 `merged`에 더합니다.
4. 인덱스 `i`가 `word2`의 길이보다 작다면 `word2[i]`를 결과 문자열 `merged`에 더합니다.
5. 루프가 끝난 후 `merged` 문자열을 반환합니다.

검증은 LeetCode에서 수행하고 Accepted된 답을 [solution.py](solution.py)에 저장합니다.

## 풀이 결과

- Status: ✅

## 직접 기록

### Approach

두 문자열의 최대 길이를 기준으로 루프를 돌며, 인덱스 `i`가 각 문자열의 길이 범위 내에 있을 때만 번갈아 가며 결과 문자열 `merged`에 문자를 이어붙여 나갑니다.

### Complexity

- Time: $O(N + M)$ (각 문자열을 한 번씩 훑으므로 단어 길이의 합에 비례)
- Space: $O(N + M)$ (결과 문자열을 저장하는 공간)

### Mistakes

- **`len()` 사용**: 파이썬에서도 `len()` 함수를 사용하여 문자열의 길이(size)를 얻을 수 있습니다.
- **`range()`의 역할**: 정수(int)는 직접 반복(iterable)에 사용할 수 없으므로 루프를 돌릴 때는 `range()`를 활용해야 합니다.
  - `for i in strSize:` (X - int 객체는 iterable 하지 않음)
  - `for i in range(strSize):` (O)
- **인덱스 아웃 오브 바운드 에러**: 파이썬에서 문자열 인덱싱(`word1[i]`) 호출 시 해당 자리에 문자가 없으면(범위를 벗어나면) `IndexError` 에러가 발생합니다. 따라서 `i < len(word1)` 조건으로 미리 안전하게 체크해야 합니다.

### Revisit

- 다음 날 재풀이:
- 코드를 보지 않고 작성했는가:
- 다시 설명하기 어려운 부분:
