class Solution:
    def TriSum(self , n : int) -> int:
        return(n * (n + 1)) >> 1
    def totalMoney(self, days: int) -> int:
        nWeeks , rDays = divmod(days , 7)
        return self.TriSum(days) - 42 * self.TriSum(nWeeks - 1) - 6 * nWeeks * rDays