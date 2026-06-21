# Python · PyTorch Zero to One

직접 구현하며 Python과 PyTorch 기본기를 처음부터 다시 쌓는 학습 저장소입니다.

> Building Python and PyTorch fundamentals from scratch through hands-on implementation.

## 학습 목표

Python 문법을 외우는 데서 끝나지 않고, 데이터를 처리하고 모델을 학습·평가한 뒤 실제 inference 환경까지 연결하는 것을 목표로 합니다.

```text
Python과 자료구조
→ NumPy와 Tensor
→ PyTorch 학습
→ Computer Vision
→ ONNX와 C++ inference
```

전체 일정과 단계별 완료 기준은 [학습 계획](docs/study-plan.md)에 기록합니다.

## 학습 방식

Top-down 방식으로 학습합니다.

1. 작동하는 전체 흐름을 먼저 확인합니다.
2. 코드에서 필요한 Python 문법과 자료구조를 찾습니다.
3. 작은 단위로 직접 구현합니다.
4. 다음 날 핵심 코드를 보지 않고 다시 작성합니다.
5. 실행 성공과 개념 이해를 구분해서 기록합니다.

문제를 풀 때는 다음 순서를 지킵니다.

```text
20분 직접 시도
→ 필요한 hint 확인
→ 단순한 풀이 완성
→ 다른 풀이와 complexity 비교
→ 다음 날 다시 구현
```

LeetCode는 Python 문법, 자료구조, algorithmic thinking을 연습하는 데 사용합니다. Python과 PyTorch 프로젝트에서는 데이터 처리, 학습, 평가, 배포 과정을 구현합니다.

## Daily Routine

하루 3시간을 기준으로 합니다.

- Python/CS 개념: 30분
- LeetCode Easy 1문제: 40분
- Python 또는 PyTorch 구현: 90분
- 코드 재작성 및 학습 기록: 20분

## 14-Day LeetCode Roadmap

| Day | Problem | Topic | Status |
|---:|---|---|:---:|
| 01 | [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) · [기록](leetcode/day-01-running-sum/) | Array, Loop | ⬜ |
| 02 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Condition | ⬜ |
| 03 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Nested List, Loop | ⬜ |
| 04 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Array | ⬜ |
| 05 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | String, Index | ⬜ |
| 06 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash Map | ⬜ |
| 07 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Set | ⬜ |
| 08 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Map, String | ⬜ |
| 09 | [Majority Element](https://leetcode.com/problems/majority-element/) | Counting | ⬜ |
| 10 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | State Update | ⬜ |
| 11 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | String, Two Pointers | ⬜ |
| 12 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack | ⬜ |
| 13 | [Binary Search](https://leetcode.com/problems/binary-search/) | Binary Search | ⬜ |
| 14 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Binary Search | ⬜ |

`⬜`는 아직 완료하지 않았다는 뜻입니다. 문제를 풀고 다음 날 다시 구현할 수 있을 때 `✅`로 변경합니다.

## Repository Structure

```text
.
├─ README.md
├─ docs/
│  └─ study-plan.md
├─ leetcode/
│  └─ day-01-running-sum/
├─ python/
│  └─ 01-prediction-score-analyzer/
└─ pytorch/
```

- [LeetCode Day 01](leetcode/day-01-running-sum/)
- [Prediction Score Analyzer](python/01-prediction-score-analyzer/)
- [PyTorch 학습 영역](pytorch/)

Day 폴더는 실제 학습을 시작할 때 하나씩 추가합니다. 빈 폴더를 미리 만들지 않고, 각 폴더의 `README.md`에 접근 방식과 실수, complexity, 재풀이 결과를 기록합니다.
