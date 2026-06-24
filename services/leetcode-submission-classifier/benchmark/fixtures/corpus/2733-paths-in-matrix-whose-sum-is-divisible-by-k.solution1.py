# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paths-in-matrix-whose-sum-is-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/paths-in-matrix-whose-sum-is-divisible-by-k.py
# solution_class: Solution
# submission_id: 2de8e8606f14cf64c1cfd54b1ab76d29e5de37af
# seed: 3010930722

# Time:  O(m * n * k)
# Space: O(n * k)

# dp

class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in xrange(k)] for _ in xrange(len(grid[0]))]
        dp[0][0] = 1
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                dp[j] = [((dp[j-1][(l-grid[i][j])%k] if j-1 >= 0 else 0)+dp[j][(l-grid[i][j])%k])%MOD for l in xrange(k)]
        return dp[-1][0]