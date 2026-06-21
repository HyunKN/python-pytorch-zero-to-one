from collections.abc import Callable


TEST_CASES = [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ([5], [5]),
]


def run_tests(solution: Callable[[list[int]], list[int]]) -> bool:
    """Run the Day 1 examples and print a LeetCode-style result summary."""
    passed_count = 0

    for test_number, (nums, expected) in enumerate(TEST_CASES, start=1):
        try:
            actual = solution(nums.copy())
            passed = actual == expected
            actual_display = repr(actual)
        except Exception as error:
            passed = False
            actual_display = f"{type(error).__name__}: {error}"

        if passed:
            passed_count += 1

        result = "PASS" if passed else "FAIL"
        print(f"Test {test_number}: {result}")
        print(f"Input:           {nums}")
        print(f"Expected Output: {expected}")
        print(f"Your Output:     {actual_display}")
        print()

    print(f"{passed_count}/{len(TEST_CASES)} tests passed")
    return passed_count == len(TEST_CASES)


if __name__ == "__main__":
    from solution import running_sum

    raise SystemExit(0 if run_tests(running_sum) else 1)
