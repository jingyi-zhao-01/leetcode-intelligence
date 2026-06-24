# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: twisted-mirror-path-count
# source_path: LeetCode-Solutions-master/Python/twisted-mirror-path-count.py
# solution_class: Solution2
# submission_id: c98d39e419abfc97401b857a46a6b257bbad6cf9
# seed: 2892676468

# Time:  O(m * n)
# Space: O(min(m, n))

# dp

class Solution2(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0]*2 for _ in xrange(len(grid[0])+1)]
        dp[1] = [1]*2
        for r in xrange(len(grid)):
            for c in xrange(len(dp)-1):
                if grid[r][c]:
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    dp[c+1] = [(dp[c+1][1]+dp[c][0])%MOD]*2
        return dp[-1][0]