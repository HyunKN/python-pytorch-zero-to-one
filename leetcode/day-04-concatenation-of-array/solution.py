class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans: list[int] = [0] * (len(nums) * 2)
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + len(nums)] = num

        return ans    
        # return nums + nums    가장좋은 답변