# Minimum Path Sum - Wrong Solution

class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]