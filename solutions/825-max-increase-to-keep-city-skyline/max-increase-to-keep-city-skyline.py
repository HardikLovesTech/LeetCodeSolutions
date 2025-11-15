class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        RowMax = [max(row) for row in grid]
        ColMax = [max(grid[i][j] for i in range(n)) for j in range(n)]
        
        Total = 0
        for i in range(n):
            for j in range(n):
                increase = min(RowMax[i], ColMax[j]) - grid[i][j]
                Total += increase
        return Total