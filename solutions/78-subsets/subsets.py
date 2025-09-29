import itertools
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1):
            result.extend(list(itertools.combinations(nums, i)))
        return result