class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(n, b):
            res = ""
            while n > 0:
                res = str(n % b) + res
                n //= b
            return res
        
        for base in range(2, n - 1):
            converted = to_base(n, base)
            if converted != converted[::-1]:
                return False
        return True
 