#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[value] = index
        return []
# Explanation:
# 1. We create a dictionary to store the indices of the numbers we have seen so far.
# 2. For each number in the list, we calculate its complement (the number needed to reach the target).
# 3. If the complement is already in the dictionary, we return the indices of the complement and the current number.
# 4. If not, we add the current number and its index to the dictionary.
# This approach runs in O(n) time and uses O(n) space, where n is the number of elements in the input list.
# This solution assumes that there is exactly one solution and does not handle cases where no solution exists.
# This solution is efficient and works well for the problem constraints.
