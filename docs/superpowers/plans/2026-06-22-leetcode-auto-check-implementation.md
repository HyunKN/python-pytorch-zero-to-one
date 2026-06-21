# LeetCode Auto-Check Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Day 1 run LeetCode-style test cases automatically when `solution.py` is executed from an IDE.

**Architecture:** `solution.py` owns only the learner function and delegates execution to `check.py`. The checker owns immutable test cases, compares actual values with expected values, prints readable diagnostics, and returns one boolean used as the process exit status.

**Tech Stack:** Python 3 standard library, `unittest`, Markdown

---

### Task 1: Specify checker behavior with tests

**Files:**
- Create: `tests/test_day01_checker.py`
- Create: `leetcode/day-01-running-sum/check.py`

- [ ] Write tests proving correct, incorrect, and exception-producing functions are reported appropriately.
- [ ] Run `python -m unittest tests/test_day01_checker.py -v` and verify RED because `check.py` does not exist.
- [ ] Implement `run_tests(solution)` with Day 1 test cases and readable output.
- [ ] Run the same command and verify all tests pass.

### Task 2: Connect the learner solution to the checker

**Files:**
- Modify: `leetcode/day-01-running-sum/solution.py`

- [ ] Replace the single-example `print()` entrypoint with `run_tests(running_sum)`.
- [ ] Preserve the learner-owned function body and return exit code `0` or `1` from the checker result.
- [ ] Execute the current learner solution and verify Input, Expected Output, Your Output, and PASS/FAIL are printed.

### Task 3: Document the reusable exercise format

**Files:**
- Modify: `README.md`
- Modify: `leetcode/day-01-running-sum/README.md`
- Create: `docs/leetcode-exercise-format.md`

- [ ] Explain that the user edits only the function in `solution.py`.
- [ ] Explain IDE Run-button behavior and command-line fallback.
- [ ] Record the three-file structure for future Day folders.

### Task 4: Verify and publish

**Files:**
- Verify all files above

- [ ] Run `python -m unittest discover -s tests -v`.
- [ ] Run `python -m compileall -q leetcode tests`.
- [ ] Run the Day 1 learner solution and confirm all four current examples pass.
- [ ] Check internal Markdown links and `git diff --check`.
- [ ] Commit only this feature and push `main` to `origin`.
