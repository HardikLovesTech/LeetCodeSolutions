#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
    

    #Explaination:
    # The formula for the sum of the first n natural numbers is n * (n + 1) // 2.
    # We calculate the expected sum of numbers from 0 to n.
    # We then calculate the actual sum of the numbers present in the array.
# The missing number is the difference between the expected sum and the actual sum.
# This approach runs in O(n) time and uses O(1) space.
