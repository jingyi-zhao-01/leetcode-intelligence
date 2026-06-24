# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-paths-with-the-given-xor-value
# source_path: LeetCode-Solutions-master/Python/count-paths-with-the-given-xor-value.py
# solution_class: Solution
# submission_id: 7df8c3b3a71e8395cc925397516f6862fdc00e7e
# seed: 1747126983

# Time:  O(m * n * r)
# Space: O(n * r)

# dp

class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        MAX_R = 16
        dp = [[0]*MAX_R for _ in xrange(len(grid[0]))]
        dp[0][0] = 1
        for i in xrange(len(grid)):
            new_dp = [[0]*MAX_R for _ in xrange(len(grid[0]))]
            for j in xrange(len(grid[0])):
                for v in range(MAX_R):
                    new_dp[j][grid[i][j]^v] = (dp[j][v]+(new_dp[j-1][v] if j-1 >= 0 else 0)) % MOD
            dp = new_dp
        return dp[-1][k]