# Learning Repository Scaffold Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the initial documented learning repository with a root dashboard, study plan, 14-day LeetCode roadmap, and Day 1 implementation exercises.

**Architecture:** The root README acts as the navigation and progress dashboard. Durable plans live under `docs/`, while each exercise keeps its problem statement, learning notes, and code in one focused folder. Only active exercises receive folders; future roadmap items remain links in the dashboard until started.

**Tech Stack:** Markdown, Python 3, Git, GitHub

---

## File Map

- `README.md`: repository purpose, learning method, daily workflow, roadmap, and progress dashboard
- `docs/study-plan.md`: ten-week Python, PyTorch, Vision, C++, and deployment schedule
- `leetcode/day-01-running-sum/README.md`: Day 1 problem and learning-record template
- `leetcode/day-01-running-sum/solution.py`: runnable starter for the Day 1 implementation
- `python/01-prediction-score-analyzer/README.md`: first practical Python exercise specification
- `python/01-prediction-score-analyzer/score_analyzer.py`: runnable starter for that exercise
- `pytorch/README.md`: scope and entry condition for the PyTorch section

### Task 1: Create the repository dashboard

**Files:**
- Create: `README.md`

- [ ] **Step 1: Add the repository purpose and learning method**

Write a concise Korean README that keeps technical terms in English and states the Top-down workflow:

```text
전체 흐름 확인 → 필요한 개념 학습 → 직접 구현 → 다음 날 재작성 → 기록
```

- [ ] **Step 2: Add the 14-day LeetCode roadmap**

Create one table with Day, Problem, Topic, and Status columns. Link Day 1 to its local folder and link every problem name to the corresponding LeetCode page.

- [ ] **Step 3: Add the repository navigation**

Link to `docs/study-plan.md`, the Day 1 LeetCode folder, the Python score analyzer, and the PyTorch section.

### Task 2: Save the durable study plan

**Files:**
- Create: `docs/study-plan.md`

- [ ] **Step 1: Add the ten-week schedule**

Document these phases with checklist items and completion criteria:

```text
Weeks 1-2: Python basics and first training run
Weeks 3-4: CNN and data processing
Weeks 5-6: Custom image classifier
Weeks 7-8: C++ basics
Weeks 9-10: ONNX deployment
```

- [ ] **Step 2: Add the daily routine and implementation rules**

Record the three-hour routine and the rule to attempt, inspect, rewrite, and explain code.

### Task 3: Create the first LeetCode learning unit

**Files:**
- Create: `leetcode/day-01-running-sum/README.md`
- Create: `leetcode/day-01-running-sum/solution.py`

- [ ] **Step 1: Write the Day 1 learning document**

Include the problem link, today’s concepts (`list`, `for`, accumulator), implementation steps, and sections for approach, complexity, mistakes, and revisit.

- [ ] **Step 2: Create a runnable starter**

Use this exact function signature and intentionally leave the exercise body for the learner:

```python
def running_sum(nums: list[int]) -> list[int]:
    """Return the cumulative sum for each position in nums."""
    raise NotImplementedError("Implement Day 1: Running Sum")
```

- [ ] **Step 3: Verify Python syntax**

Run:

```powershell
python -m py_compile leetcode/day-01-running-sum/solution.py
```

Expected: exit code 0 with no output.

### Task 4: Create the first practical Python unit

**Files:**
- Create: `python/01-prediction-score-analyzer/README.md`
- Create: `python/01-prediction-score-analyzer/score_analyzer.py`

- [ ] **Step 1: Document the exercise contract**

Require the learner to return Top-1, Top-3, and `unknown` when the highest score is below a threshold. List the Python concepts exercised without providing the completed algorithm.

- [ ] **Step 2: Create a runnable starter**

Use explicit type hints and a deliberate `NotImplementedError`:

```python
def analyze_scores(
    labels: list[str], scores: list[float], threshold: float
) -> dict[str, object]:
    """Summarize prediction scores as Top-1, Top-3, and a decision."""
    raise NotImplementedError("Implement the prediction score analyzer")
```

- [ ] **Step 3: Verify Python syntax**

Run:

```powershell
python -m py_compile python/01-prediction-score-analyzer/score_analyzer.py
```

Expected: exit code 0 with no output.

### Task 5: Add the PyTorch section boundary

**Files:**
- Create: `pytorch/README.md`

- [ ] **Step 1: Describe the section scope**

State that the section will begin with FashionMNIST and progress through Tensor shapes, `Dataset`, `DataLoader`, training, evaluation, and model export. Do not create unused project files yet.

### Task 6: Verify and publish

**Files:**
- Verify: all files listed above

- [ ] **Step 1: Check Python syntax**

Run:

```powershell
python -m compileall -q leetcode python
```

Expected: exit code 0.

- [ ] **Step 2: Check Markdown links and roadmap state**

Run a local script that extracts relative Markdown links from `README.md` and confirms every linked local path exists. Confirm Day 1 is marked as not completed because its implementation still raises `NotImplementedError`.

- [ ] **Step 3: Check repository scope**

Run:

```powershell
git status --short
git diff --check
```

Expected: only the documented scaffold files appear, and `git diff --check` reports no errors.

- [ ] **Step 4: Commit and push**

Stage only the scaffold files, commit with `docs: scaffold learning roadmap`, and push `main` to `origin` because this is the initial content of an empty user-created repository.
