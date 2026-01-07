class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        MaxOnes = 0
        Count = 0
        for num in nums:
            if num == 0:
                Count = 0
            if num == 1:
                Count += 1 
            MaxOnes = max(MaxOnes , Count)

        return MaxOnes