class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}
        for i,num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]
            seen[num] = i


# 더 빠른 방식으로는 딕셔너리를 쓰면 된다.

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 8, 7]
    target = 9
    print("--- 디버깅 시작 ---")
    result = sol.twoSum(nums, target)
    print("최종 결과:", result)