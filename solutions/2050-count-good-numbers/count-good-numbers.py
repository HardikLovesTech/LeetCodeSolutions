class Solution:
    def countGoodNumbers(self, n: int) -> int:
        #I Love Elementary Number Theory
        mod = 7 + (10 ** 9)
        Even = (n+1) // 2
        Odd = n // 2
        return (pow(5 , Even , mod)*pow(4 , Odd , mod)) % mod