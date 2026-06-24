# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: 01-matrix
# source_path: LeetCode-Solutions-master/Python/01-matrix.py
# solution_class: Solution2
# submission_id: 6bd213ee9a1a75558d9a3fc8931e33dff1aad61c
# seed: 380644468

# Time:  O(m * n)
# Space: O(1)

# dp solution

class Solution2(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dp = [[float("inf")]*len(matrix[0]) for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i < len(matrix)-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                    if j < len(matrix[i])-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
        return dp