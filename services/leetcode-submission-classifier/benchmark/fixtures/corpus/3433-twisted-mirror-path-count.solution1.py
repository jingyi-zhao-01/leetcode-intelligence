# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: twisted-mirror-path-count
# source_path: LeetCode-Solutions-master/Python/twisted-mirror-path-count.py
# solution_class: Solution
# submission_id: e5ad3c47bd8ffec296c11dfb364864f116c33d46
# seed: 802141454

# Time:  O(m * n)
# Space: O(min(m, n))

# dp

class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        def get(r, c):
            return grid[r][c] if len(grid) > len(grid[0]) else grid[c][r]

        dp = [[0]*2 for _ in xrange(min(len(grid), len(grid[0]))+1)]
        dp[1] = [1]*2
        for r in xrange(max(len(grid), len(grid[0]))):
            for c in xrange(len(dp)-1):
                if get(r, c):
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    dp[c+1] = [(dp[c+1][1]+dp[c][0])%MOD]*2
        return dp[-1][0]