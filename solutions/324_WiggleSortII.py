from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        first_half = nums[:half][::-1]  # smaller half, reversed
        second_half = nums[half:][::-1]  # larger half, reversed

        for i in range(n):
            if i % 2 == 0:
                nums[i] = first_half.pop(0)
            else:
                nums[i] = second_half.pop(0)
