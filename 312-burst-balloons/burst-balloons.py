from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # i = 1
        # j = len(nums)
        # coins = 0
        # while(len(nums) >= 3):
        #     if(j == 3):
        #         nums[j] = 1
        #         j -= 1
        #     coins += (nums[i+1] * nums[i] * nums[i-1])
        #     nums.pop(i)
        #     if(len(nums) == 2):
        #         nums[j] = 1
        nums = [1] + nums + [1]

        # return coins
        @lru_cache(None)
        def IDK(left: int , right: int)-> int:
            if left+1 == right:
                return 0
            MaxCoins = 0
            for i in range(left+1 , right):
                coins = (nums[left] * nums[i] * nums[right])
                coins += IDK(left , i) + IDK(i , right)
                MaxCoins = max(coins ,MaxCoins)
            return MaxCoins
        return IDK(0 , len(nums) - 1)
