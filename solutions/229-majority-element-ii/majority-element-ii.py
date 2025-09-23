class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = int(len(nums)/3)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        Req = []
        for key,values in freq.items():
            if values > count:
               Req.append(key)

        return Req