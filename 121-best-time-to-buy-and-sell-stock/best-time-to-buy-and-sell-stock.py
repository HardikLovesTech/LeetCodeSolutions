class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricing = prices[0]
        profit = 0

        for p in prices[1:]:
            if pricing > p:
                pricing = p
            profit = max(profit , p - pricing)
    
        return profit