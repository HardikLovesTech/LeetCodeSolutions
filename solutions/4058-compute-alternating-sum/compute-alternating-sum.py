class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count += ((-1)**i)*nums[i]
        return count