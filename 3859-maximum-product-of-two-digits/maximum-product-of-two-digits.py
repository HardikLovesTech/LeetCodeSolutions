class Solution:
    def maxProduct(self, n: int) -> int:
        Max1, Max2 = -1, -1

        while n != 0:
            Rem = n % 10

            if Max1 <= Rem:
                Max2 = Max1
                Max1 = Rem
            elif Max2 < Rem:
                Max2 = Rem

            n //= 10

        return Max1 * Max2