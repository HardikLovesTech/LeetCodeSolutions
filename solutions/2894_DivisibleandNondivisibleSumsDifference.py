class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = 0
        undivisible = 0
        for num in range(n+1):
            if num % m == 0:
                divisible += num    
            else:
                undivisible += num

        return (divisible - undivisible)