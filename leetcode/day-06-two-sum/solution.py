class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            if(nums[i] > target):
                continue
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]


#  더 빠른 방식으로는 딕셔너리를 쓰면 된다.