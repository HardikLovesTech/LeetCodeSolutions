class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target_count = [0] * 10
        while n > 0:
            digit = n % 10
            target_count[digit] += 1
            n //= 10
        
        for i in range(30):  # From 2^0 to 2^29
            power = 1 << i
            power_count = [0] * 10
            while power > 0:
                digit = power % 10
                power_count[digit] += 1
                power //= 10

            if power_count == target_count:
                return True
        return False

