# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-path-with-teleportations
# source_path: LeetCode-Solutions-master/Python/minimum-cost-path-with-teleportations.py
# solution_class: Solution2
# submission_id: 99d47bf4c503e7ed78f796ccb045682783e0aea7
# seed: 3785081218

# Time:  O(k * (m * n + r))
# Space: O(m * n + r)

# dp, prefix sum

class Solution2(object):
    def minCost(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [[float("inf")]*len(grid[0]) for _ in xrange(len(grid))]
        dp[-1][-1] = 0
        mx = max(max(row) for row in grid)
        prefix = [float("inf")]*(mx+1)
        for i in xrange(k+1):
            for r in reversed(xrange(len(grid))):
                for c in reversed(xrange(len(grid[0]))):
                    if r+1 < len(grid):
                        dp[r][c] = min(dp[r][c], dp[r+1][c]+grid[r+1][c])
                    if c+1 < len(grid[0]):
                        dp[r][c] = min(dp[r][c], dp[r][c+1]+grid[r][c+1])
                    dp[r][c] = min(dp[r][c], prefix[grid[r][c]])
            for r in xrange(len(grid)):
                for c in xrange(len(grid[0])):
                    prefix[grid[r][c]] = min(prefix[grid[r][c]], dp[r][c])
            for i in xrange(len(prefix)-1):
                prefix[i+1] = min(prefix[i+1], prefix[i])
        return dp[0][0]