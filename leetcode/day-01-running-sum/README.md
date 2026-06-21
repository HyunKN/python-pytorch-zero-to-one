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
- `for` loop
- accumulator variable
- `append()`
- 함수 parameter와 `return`

## 구현 순서

1. `total`을 `0`으로 시작합니다.
2. 입력 `nums`의 숫자를 앞에서부터 하나씩 확인합니다.
3. 현재 숫자를 `total`에 더합니다.
4. 갱신된 `total`을 결과 list에 추가합니다.
5. 완성된 결과를 반환합니다.

정답 코드를 먼저 보지 말고 [solution.py](solution.py)의 `running_sum()`을 직접 구현합니다.

## 실행 및 자동 검증

사용자는 `solution.py`의 `running_sum()` 함수 본문만 수정합니다. `check.py`는 수정하지 않습니다.

1. IDE에서 `solution.py`를 엽니다.
2. Python Run 버튼을 누릅니다.
3. 네 개의 예제 입력이 자동으로 함수에 전달됩니다.
4. Input, Expected Output, Your Output과 PASS/FAIL을 확인합니다.

터미널에서는 다음 명령으로 동일하게 실행할 수 있습니다.

```powershell
python solution.py
```

출력 형식:

```text
Test 1: PASS
Input:           [1, 2, 3, 4]
Expected Output: [1, 3, 6, 10]
Your Output:     [1, 3, 6, 10]

4/4 tests passed
```

하나라도 다르면 해당 test는 `FAIL`로 표시됩니다. 실행 중 error가 발생하면 `Your Output`에 error 종류와 message가 출력됩니다.

## 직접 기록

### Approach

풀이 후 내가 사용한 절차를 문장으로 작성합니다.

### Complexity

- Time:
- Space:

### Mistakes

막힌 문법, 잘못 예상한 출력, 수정한 이유를 기록합니다.

### Revisit

- 다음 날 재풀이:
- 코드를 보지 않고 작성했는가:
- 다시 설명하기 어려운 부분:
