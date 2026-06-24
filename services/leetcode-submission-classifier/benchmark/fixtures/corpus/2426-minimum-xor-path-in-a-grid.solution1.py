# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-xor-path-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-xor-path-in-a-grid.py
# solution_class: Solution
# submission_id: c134246ade42c75885a3362fb911d7d36a453a34
# seed: 2001472910

# Time:  O(m * n * r), r = max(x for row in grid for x in row)
# Space: O(n * r)

# dp

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mx = max(x for row in grid for x in row)
        l = 1<<mx.bit_length()
        dp = [[False]*l for _ in xrange(len(grid[0]))]
        dp[0][0] = True
        for i in xrange(len(grid)):
            new_dp = [[False]*l for _ in xrange(len(grid[0]))]
            for j in xrange(len(grid[0])):
                for k in xrange(l):
                    if dp[j][k] or (j-1 >= 0 and new_dp[j-1][k]):
                        new_dp[j][k^grid[i][j]] = True
            dp = new_dp
        return next(i for i in xrange(l) if dp[-1][i])