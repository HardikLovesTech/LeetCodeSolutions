class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = int(float(dividend)/float(divisor))
        if x==2147483648:
            return x - 1
        else:
            return x