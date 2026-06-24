# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-path-cost-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-path-cost-in-a-grid.py
# solution_class: Solution
# submission_id: 8213b40efd9b8fe77dfff6b20fa0815a45effc81
# seed: 1747777328

# Time:  O(m * n^2)
# Space: O(n)

# dp

class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(grid[0]) for _ in xrange(2)]
        dp[0] = [grid[0][j] for j in xrange(len(grid[0]))]
        for i in xrange(len(grid)-1):
            for j in xrange(len(grid[0])):
                dp[(i+1)%2][j] = min(dp[i%2][k]+moveCost[x][j] for k, x in enumerate(grid[i]))+grid[i+1][j]
        return min(dp[(len(grid)-1)%2])