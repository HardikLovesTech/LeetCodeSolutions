class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        i = 1
        while n // (5 ** i) > 0:
            total += n // (5 ** i)
            i += 1
        return total
