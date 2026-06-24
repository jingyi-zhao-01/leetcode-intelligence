# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: out-of-boundary-paths
# source_path: LeetCode-Solutions-master/Python/out-of-boundary-paths.py
# solution_class: Solution
# submission_id: bbb94a16b5d51f1873fbe0fc75fdd6c58d475547
# seed: 1824744934

# Time:  O(N * m * n)
# Space: O(m * n)

class Solution(object):
    def findPaths(self, m, n, N, x, y):
        """
        :type m: int
        :type n: int
        :type N: int
        :type x: int
        :type y: int
        :rtype: int
        """
        M = 1000000000 + 7
        dp = [[[0 for _ in xrange(n)] for _ in xrange(m)] for _ in xrange(2)]
        for moves in xrange(N):
            for i in xrange(m):
                for j in xrange(n):
                    dp[(moves + 1) % 2][i][j] = (((1 if (i == 0) else dp[moves % 2][i - 1][j]) + \
                                                  (1 if (i == m - 1) else dp[moves % 2][i + 1][j])) % M + \
                                                 ((1 if (j == 0) else dp[moves % 2][i][j - 1]) + \
                                                  (1 if (j == n - 1) else dp[moves % 2][i][j + 1])) % M) % M
        return dp[N % 2][x][y]