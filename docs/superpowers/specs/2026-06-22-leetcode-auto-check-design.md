# LeetCode Auto-Check Design

## Goal

사용자는 각 문제의 `solution.py`에서 정답 함수만 작성하고 IDE의 Python Run 버튼을 누른다. 별도 입력 없이 여러 예제 입력이 자동으로 전달되며, 각 test의 Input, Expected Output, Your Output, PASS/FAIL을 확인할 수 있어야 한다.

## Structure

```text
leetcode/day-XX-problem-name/
├─ README.md
├─ solution.py
└─ check.py
```

- `solution.py`: 사용자가 수정하는 정답 함수와 Run 진입점
- `check.py`: test cases, 비교, 결과 출력
- `README.md`: 문제 링크, 실행법, 학습 기록

## Runtime Flow

1. 사용자가 `solution.py`의 정답 함수 본문을 작성한다.
2. `solution.py`를 연 상태로 IDE의 Python Run 버튼을 누른다.
3. `solution.py`가 `check.run_tests()`를 호출한다.
4. checker가 각 입력을 정답 함수에 전달한다.
5. checker가 Expected Output과 Your Output을 비교하고 결과를 출력한다.
6. 모든 test가 통과하면 process exit code `0`, 하나라도 실패하면 `1`을 반환한다.

## Output Contract

```text
Test 1: PASS
Input:           [1, 2, 3, 4]
Expected Output: [1, 3, 6, 10]
Your Output:     [1, 3, 6, 10]

3/3 tests passed
```

함수에서 exception이 발생하면 checker가 중단되지 않고 `Your Output`에 exception type과 message를 표시한다.

## Scope

- Day 1 Running Sum에 먼저 적용한다.
- 별도 package 설치 없이 Python standard library만 사용한다.
- GitHub Actions는 이번 변경에 포함하지 않는다.
- 이후 Day 폴더에도 같은 세 파일 구조를 적용한다.

## Verification

- 올바른 함수는 모든 test를 통과해야 한다.
- 잘못된 함수는 Expected Output과 Your Output을 함께 보여줘야 한다.
- exception을 발생시키는 함수도 모든 test 결과를 출력하고 실패로 종료해야 한다.
- 미구현 상태의 `solution.py`를 실행하면 친절한 실패 결과가 출력돼야 한다.
