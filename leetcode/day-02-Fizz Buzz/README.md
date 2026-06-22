# Day 02 — Fizz Buzz

- Status: Accepted

## 직접 기록

# Python FizzBuzz 핵심 정리

## Point 1. 파이썬의 리스트는 “빈 바구니”다

파이썬 리스트는 처음부터 크기를 정하지 않아도 된다.

```python
answer = []
```

이렇게 빈 리스트를 만들고, 값을 하나씩 뒤에 추가한다.

```python
answer.append(값)
```

주의할 점:

```python
answer[i] = 값
```

이 방식은 이미 해당 위치에 값이 있을 때만 가능하다.
빈 리스트에는 바로 인덱스로 넣을 수 없다.

---

## Point 2. `range(시작, 끝)`의 종료 조건

파이썬의 `range()`는 끝 숫자 바로 직전까지만 반복한다.

```python
range(0, n)
```

→ `0`부터 `n-1`까지 반복

```python
range(1, n + 1)
```

→ `1`부터 `n`까지 반복

반복 횟수 공식:

```text
끝 숫자 - 시작 숫자
```

예시:

```python
range(1, 4)
```

→ `1, 2, 3`
→ 총 `4 - 1 = 3번` 반복

---

## Point 3. `-> List[str]`의 의미

```python
def fizzBuzz(n: int) -> List[str]:
```

여기서 `-> List[str]`는 타입 힌트이다.

의미:

```text
이 함수는 문자열(str)이 담긴 리스트(List)를 반환한다.
```

즉, 최종 결과에는 숫자 그대로가 아니라 문자열로 변환해서 넣어야 한다.

```python
answer.append(str(i))
```

---

## Point 4. `if` vs `elif`

### `if-if-if`

```python
if 조건1:
    ...
if 조건2:
    ...
if 조건3:
    ...
```

각 조건을 전부 검사한다.

그래서 하나의 숫자에 대해 여러 값이 중복으로 들어갈 수 있다.

---

### `if-elif-else`

```python
if 조건1:
    ...
elif 조건2:
    ...
elif 조건3:
    ...
else:
    ...
```

위에서 조건 하나가 만족되면 아래 조건은 검사하지 않는다.

FizzBuzz처럼 하나의 숫자에 하나의 결과만 넣어야 할 때는
`if-elif-else` 구조를 사용해야 한다.

---

## 최종 기억

```text
빈 리스트 만들기 → answer = []
값 추가하기 → answer.append(값)
1부터 n까지 반복 → range(1, n + 1)
문자열 리스트 반환 → List[str]
중복 조건 방지 → if-elif-else
```


