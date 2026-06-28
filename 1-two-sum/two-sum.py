class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}
        
        for i in range(len(nums)):
            find[nums[i]] = i
        for i in range(len(nums)):
            numToFind = target - nums[i]
            if numToFind in find and find[numToFind] != i:
                return [i , find[numToFind]]
        
        return -1