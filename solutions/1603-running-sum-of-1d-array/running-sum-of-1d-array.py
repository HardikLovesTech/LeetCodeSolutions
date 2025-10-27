class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        result = []
        for num in nums:
            count += num
            result.append(count)

        return result