class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        nums = list(range(1, n + 1))   # remaining digits
        k -= 1                          # convert k to 0-based index
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(str(nums.pop(index)))
            k %= fact

        return "".join(result)
