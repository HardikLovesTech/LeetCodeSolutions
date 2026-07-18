class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        for i in range(len(nums)):
            find[nums[i]] = i
        for i in range(len(nums)):
            soln = target - nums[i]
            if soln in find and find[soln] != i:
                return [i , find[soln]]
        
        return -1