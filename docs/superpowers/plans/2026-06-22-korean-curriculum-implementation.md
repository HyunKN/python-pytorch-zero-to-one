# 한국어 실습 Curriculum Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Python부터 PyTorch Vision과 ONNX Runtime까지 이어지는 한국어 16단계 실습 구조를 저장소에 구성한다.

**Architecture:** 주제별 상위 폴더와 전체 과정 순번을 함께 사용한다. 각 단계는 학습 계약을 설명하는 README, 정답이 없는 starter, 회고용 notes로 독립적으로 구성하며 루트 README가 전체 순서와 상태를 관리한다.

**Tech Stack:** Python 3, NumPy, PyTorch, torchvision, Pillow, ONNX, ONNX Runtime, Markdown

---

### Task 1: Python과 NumPy 단계 구성

**Files:**
- Create or modify: `python/01-*` through `python/04-*`
- Create: `numpy/05-*` through `numpy/07-*`

- [ ] Python list, dict, JSON, image folder 처리 과제 4개를 구성한다.
- [ ] NumPy shape, normalization, cosine similarity 과제 3개를 구성한다.
- [ ] 각 단계에 `README.md`, `starter.py`, `notes.md`를 둔다.

### Task 2: PyTorch와 Vision 단계 구성

**Files:**
- Create: `pytorch/08-*` through `pytorch/14-*`

- [ ] Tensor, autograd, MLP, CNN, custom Dataset, ResNet, 오류 분석 과제 7개를 구성한다.
- [ ] 각 starter는 구현할 함수와 실행 순서만 제공하고 정답은 제공하지 않는다.

### Task 3: Deployment 단계 구성

**Files:**
- Create: `deployment/15-*` and `deployment/16-*`

- [ ] ONNX export와 PyTorch/ONNX parity 과제를 구성한다.
- [ ] ONNX Runtime latency benchmark 과제를 구성한다.

### Task 4: Navigation과 학습 계획 갱신

**Files:**
- Modify: `README.md`
- Modify: `docs/study-plan.md`
- Modify: `pytorch/README.md`

- [ ] 루트 README에 16단계 순서, 링크, 상태를 추가한다.
- [ ] C++ 단계를 제거하고 Python/PyTorch/ONNX 10주 과정으로 수정한다.
- [ ] 기존 Landmark 예시를 일반적인 예시로 교체한다.

### Task 5: 검증과 게시

- [ ] `python -m compileall -q python numpy pytorch deployment`를 실행한다.
- [ ] 루트 README의 16개 local link가 모두 존재하는지 확인한다.
- [ ] `rg`로 C++와 기존 Landmark 예시가 curriculum에 남아 있지 않은지 확인한다.
- [ ] `git diff --check`와 diff scope를 확인한다.
- [ ] 관련 파일만 commit하고 `main`에 push한다.
