class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = [x//k for x in nums1 if x%k == 0]
        return sum(x%y == 0 for x, y in product(nums1, nums2))
