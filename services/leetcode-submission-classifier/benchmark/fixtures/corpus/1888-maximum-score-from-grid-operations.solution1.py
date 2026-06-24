# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-from-grid-operations
# source_path: LeetCode-Solutions-master/Python/maximum-score-from-grid-operations.py
# solution_class: Solution
# submission_id: 27d29b42c641d4de0d84b90b76cef42557cb533d
# seed: 1533927526

# Time:  O(n^3)
# Space: O(n)

# prefix sum, dp

class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prefix = [0]*(len(grid)+1)
        for i in xrange(len(grid)):
            prefix[i+1] = prefix[i]+grid[i][0]
        result = 0
        # dp[0][i]: the maximum score from 0 to the current column, and the current column has i black cells, without scoring the white cells of the current column
        # dp[1][i]: the maximum score from 0 to the current column, and the current column has i black cells, with scoring the white cells of the current column
        dp = [[0]*(len(grid)+1) for _ in xrange(2)]
        for j in xrange(1, len(grid[0])):
            new_prefix = [0]*(len(grid)+1)
            for i in xrange(len(grid)):
               new_prefix[i+1] = new_prefix[i]+grid[i][j]
            new_dp = [[0]*(len(grid)+1) for _ in xrange(2)]
            for i in xrange(len(grid)+1):
                for k in xrange(i+1):
                    new_dp[0][i] = max(new_dp[0][i], (prefix[i]-prefix[k])+dp[0][k])
                new_dp[0][i] = max(new_dp[0][i], max(dp[1]))
                for k in xrange(i+1, len(grid)+1):
                    new_dp[1][i] = max(new_dp[1][i], dp[1][k]+(new_prefix[k]-new_prefix[i]))
                new_dp[1][i] = max(new_dp[1][i], new_dp[0][i])
            dp, prefix = new_dp, new_prefix
        return max(dp[1])