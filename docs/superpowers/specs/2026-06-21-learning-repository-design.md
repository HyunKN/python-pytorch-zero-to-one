# Learning Repository Design

## Purpose

`python-pytorch-zero-to-one`은 Python 문법과 자료구조를 익히고, 이를 PyTorch 기반 Vision 학습과 배포까지 연결하는 구현 중심 학습 저장소다.

설명은 한국어로 작성하고 technical terms와 코드는 English를 유지한다.

## Learning Method

학습은 Top-down 방식으로 진행한다.

1. 작동하는 전체 흐름을 먼저 확인한다.
2. 필요한 Python 문법과 자료구조를 역으로 학습한다.
3. 작은 단위로 직접 구현한다.
4. 다음 날 핵심 코드를 보지 않고 다시 작성한다.
5. 실행 성공과 개념 이해를 구분해 기록한다.

LeetCode는 Python 문법, 자료구조, algorithmic thinking을 연습하는 데 사용한다. PyTorch 실습은 데이터 처리, 모델 학습, 평가, 배포 흐름을 구현하는 데 사용한다.

## Repository Structure

```text
python-pytorch-zero-to-one/
├─ README.md
├─ docs/
│  └─ study-plan.md
├─ leetcode/
│  ├─ day-01-running-sum/
│  │  ├─ README.md
│  │  └─ solution.py
│  ├─ day-02-fizz-buzz/
│  │  ├─ README.md
│  │  └─ solution.py
│  └─ ...
├─ python/
│  └─ 01-prediction-score-analyzer/
└─ pytorch/
   └─ 01-fashion-mnist/
```

## Root README

루트 `README.md`는 저장소의 dashboard 역할을 한다.

- 저장소의 목적
- Top-down 학습 방식
- 일일 학습 순서
- 14일 LeetCode roadmap과 진행 상태
- Python, PyTorch, C++/deployment 학습 범위
- 각 학습 폴더로 이동하는 링크

문제별 상세 설명은 루트 README에 반복하지 않고 해당 Day 폴더에 기록한다.

## LeetCode Records

첫 14일은 다음 순서로 진행한다.

1. Running Sum of 1d Array
2. Fizz Buzz
3. Richest Customer Wealth
4. Concatenation of Array
5. Merge Strings Alternately
6. Two Sum
7. Contains Duplicate
8. Valid Anagram
9. Majority Element
10. Best Time to Buy and Sell Stock
11. Valid Palindrome
12. Valid Parentheses
13. Binary Search
14. Search Insert Position

각 Day 폴더는 다음 두 파일만 기본으로 가진다.

- `README.md`: problem, learned concepts, approach, complexity, mistakes, revisit 기록
- `solution.py`: 해당 문제의 현재 풀이

초기 풀이와 수정 과정은 Git history로 보존하며 `solution-v1.py`, `final.py` 같은 중복 파일은 만들지 않는다.

## Initial Scope

첫 scaffold에서는 다음만 만든다.

- 루트 README와 14일 roadmap
- `docs/study-plan.md`
- `leetcode/day-01-running-sum/`
- `python/01-prediction-score-analyzer/`
- 이후 학습 영역을 설명하는 최소 placeholder README

Day 2 이후 폴더는 실제로 학습을 시작할 때 추가한다. 빈 폴더를 미리 대량 생성하지 않는다.

## Verification

- Markdown link가 저장소 내부 파일을 올바르게 가리키는지 확인한다.
- `solution.py`는 Python syntax check를 통과해야 한다.
- 루트 README의 진행 상태와 실제 생성된 Day 폴더가 일치해야 한다.
- Git diff가 학습 저장소 scaffold 범위만 포함하는지 확인한다.
