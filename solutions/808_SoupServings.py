class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0  # For large n, the answer converges to 1
        
    # Convert mL to units of 25 mL
        n = (n + 24) // 25
        
        # Memoization dictionary
        memo = {}

        def dp(a, b):
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Check if result is already computed
            if (a, b) in memo:
                return memo[(a, b)]

            # Recursive calls with the four serving options
            result = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

            # Store result in memo
            memo[(a, b)] = result
            return result

        return dp(n, n)
