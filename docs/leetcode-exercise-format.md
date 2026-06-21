# LeetCode Exercise Format

모든 LeetCode Day는 동일한 세 파일 구조를 사용합니다.

```text
leetcode/day-XX-problem-name/
├─ README.md
├─ solution.py
└─ check.py
```

## `solution.py`

사용자가 수정하는 파일입니다.

- 문제에서 요구한 함수의 본문만 작성합니다.
- IDE의 Python Run 버튼을 누르면 checker를 실행합니다.
- test case나 expected output은 직접 작성하지 않습니다.

```python
def solution(values):
    # Write your answer here.
    ...


if __name__ == "__main__":
    from check import run_tests

    raise SystemExit(0 if run_tests(solution) else 1)
```

## `check.py`

자동 검증을 담당하며 문제를 푸는 동안 수정하지 않습니다.

- 여러 test input을 정답 함수에 전달
- Expected Output과 Your Output 비교
- 각 test의 PASS/FAIL 출력
- exception을 잡아서 학습자가 확인할 수 있게 출력
- 전체 test가 통과하면 exit code `0`, 실패하면 `1` 반환

## `README.md`

문제와 학습 기록을 담당합니다.

- 문제 링크와 요구사항
- 배울 문법과 자료구조
- 실행 방법
- Approach
- Time/Space Complexity
- Mistakes
- Revisit 결과

## 실행 방법

IDE에서는 `solution.py`를 열고 Python Run 버튼을 누릅니다.

터미널에서는 해당 Day 폴더에서 다음 명령을 실행합니다.

```powershell
python solution.py
```

`check.py`도 직접 실행할 수 있지만, 기본 학습 흐름에서는 `solution.py`를 실행합니다.
