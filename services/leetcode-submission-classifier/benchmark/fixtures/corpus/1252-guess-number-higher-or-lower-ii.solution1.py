# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: guess-number-higher-or-lower-ii
# source_path: LeetCode-Solutions-master/Python/guess-number-higher-or-lower-ii.py
# solution_class: Solution
# submission_id: be759a3af95b7cedc0d2a2b7aa4aa1c314372d65
# seed: 1875246850

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in xrange(n+1)]  # dp[i][j]: min pay in [i+1, j+1)
        for j in xrange(n+1):
            for i in reversed(xrange(j-1)):
                dp[i][j] = min((k+1) + max(dp[i][k], dp[k+1][j]) for k in xrange(i, j))
        return dp[0][n]