# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-line-of-consecutive-one-in-matrix
# source_path: LeetCode-Solutions-master/Python/longest-line-of-consecutive-one-in-matrix.py
# solution_class: Solution
# submission_id: 0dd9fe0218605a311e2309dbf0dce4bd73c659d2
# seed: 3583530675

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M: return 0
        result = 0
        dp = [[[0] * 4 for _ in xrange(len(M[0]))] for _ in xrange(2)]
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                dp[i % 2][j][:] = [0] * 4
                if M[i][j] == 1:
                    dp[i % 2][j][0] = dp[i % 2][j - 1][0]+1 if j > 0 else 1
                    dp[i % 2][j][1] = dp[(i-1) % 2][j][1]+1 if i > 0 else 1
                    dp[i % 2][j][2] = dp[(i-1) % 2][j-1][2]+1 if (i > 0 and j > 0) else 1
                    dp[i % 2][j][3] = dp[(i-1) % 2][j+1][3]+1 if (i > 0 and j < len(M[0])-1) else 1
                    result = max(result, max(dp[i % 2][j]))
        return result