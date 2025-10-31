class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = []
        l1 = nums[:n]
        l2 = nums[n:]
        
        for i in range(n):
            l.append(l1[i])
            l.append(l2[i])
        
        return l
