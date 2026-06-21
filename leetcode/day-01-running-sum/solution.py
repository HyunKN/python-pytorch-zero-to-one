def running_sum(nums: list[int]) -> list[int]:
    """Return the cumulative sum for each position in nums."""
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

if __name__ == "__main__":
    from check import run_tests

    raise SystemExit(0 if run_tests(running_sum) else 1)
