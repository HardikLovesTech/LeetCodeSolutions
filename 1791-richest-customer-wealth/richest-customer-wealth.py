class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        MaxWealth = 0
        for customer in accounts:
            MaxWealth = max(MaxWealth, sum(customer))
        return MaxWealth