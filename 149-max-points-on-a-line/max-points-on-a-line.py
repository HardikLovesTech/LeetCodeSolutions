class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        from math import gcd

        n = len(points)
        if n <= 2:
            return n

        result = 1

        for i in range(n):
            slope_count = defaultdict(int)
            duplicates = 0
            local_max = 1

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                # Duplicate point
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # Reduce by gcd
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize slope direction
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:  
                    dy = 1  # Vertical line: slope = "inf"

                slope_count[(dx, dy)] += 1
                local_max = max(local_max, slope_count[(dx, dy)] + 1)

            result = max(result, local_max + duplicates)

        return result
