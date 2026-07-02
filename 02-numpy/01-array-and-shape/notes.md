# 학습 기록

## 접근 방식

`summarize_array` 함수를 직접 구현하면서 각 속성의 역할과 타입 변환 방식을 파악하는 방식으로 학습.

## 새로 배운 내용

### `ndim` — 배열의 차원 수
- **Number of Dimensions**의 약자로, 배열이 **몇 차원인지**를 나타내는 정수 속성.
- `shape` 튜플의 길이(`len`)와 항상 일치함.
  ```python
  a = np.array([[1, 2, 3], [4, 5, 6]])
  a.ndim   # 2  (2차원 배열)
  a.shape  # (2, 3)  →  len((2, 3)) == 2
  ```
- 차원별 정리:
  | ndim | 이름 | 예시 |
  |------|------|------|
  | 0 | 스칼라 | `np.array(5)` |
  | 1 | 벡터 | `np.array([1, 2, 3])` |
  | 2 | 행렬 | `np.array([[1,2],[3,4]])` |
  | 3 | 텐서 | RGB 이미지 등 |

### `shape` — 각 차원의 크기
- `shape`는 **(행의 수, 열의 수)** 순서의 튜플로 배열의 크기를 나타냄.
- `np.array([[1, 2, 3], [4, 5, 6]])` → `shape = (2, 3)` : 2행 3열.
- `shape` 요소를 모두 곱하면 전체 원소 수(`size`)가 됨. (2×3 = 6)

### 통계값에 `float()`을 씌우는 이유
- `array.min()`, `array.max()` 등의 반환값은 파이썬 기본 `int`/`float`가 아니라 **NumPy 전용 타입** (`np.int64`, `np.float64` 등).
- 이 상태로 JSON 변환 시 `TypeError: Object of type int64 is not JSON serializable` 에러가 발생.
- 파이썬 표준 타입인 `int()` 또는 `float()`으로 명시적 변환하면 이 문제를 방지할 수 있음.
- **더 나은 설계:** 원본 `dtype`이 정수형이면 `int()`, 실수형이면 `float()`으로 변환해 타입 일관성 유지.
  ```python
  is_integer = np.issubdtype(array.dtype, np.integer)
  convert = int if is_integer else float
  ```

### 파이썬의 타입 이름은 소문자
- Java/C#에서는 `String`이지만 파이썬의 내장 타입은 모두 **소문자**.
  | 파이썬 | 설명 |
  |--------|------|
  | `str` | 문자열 (String) |
  | `int` | 정수 |
  | `float` | 실수 |
  | `bool` | 불리언 |
  | `list` | 리스트 |
  | `dict` | 딕셔너리 |

## 실수와 해결

### 함수 호출 시 `()` 빠뜨림
- **실수:** `int(array.min)` — 괄호 없이 메서드 이름만 적음.
- **결과:** `minimum` 값에 숫자가 아니라 메서드 객체 자체가 들어감.
  ```
  'minimum': <built-in method min of numpy.ndarray object at 0x...>
  ```
- `int()`로 감쌌을 때는 아예 에러 발생:
  ```
  TypeError: int() argument must be a string ... not 'builtin_function_or_method'
  ```
- **해결:** 반드시 `()`를 붙여 함수를 **실행**한 결과를 사용해야 함.
  ```python
  # ❌ 틀림 — 함수 자체를 가리킴
  int(array.min)

  # ✅ 올바름 — 함수를 실행한 결과(숫자)를 변환
  int(array.min())
  ```

## 다시 구현

- 다시 구현한 날짜:
- 코드를 보지 않고 작성했는가:
