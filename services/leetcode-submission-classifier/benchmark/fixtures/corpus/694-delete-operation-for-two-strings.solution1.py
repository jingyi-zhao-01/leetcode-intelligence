# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-operation-for-two-strings
# source_path: LeetCode-Solutions-master/Python/delete-operation-for-two-strings.py
# solution_class: Solution
# submission_id: 40ea748c1011646f5b171c5808c04c848cb5bfbc
# seed: 3376488429

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in xrange(2)]
        for i in xrange(m):
            for j in xrange(n):
                dp[(i+1)%2][j+1] = max(dp[i%2][j+1], \
                                       dp[(i+1)%2][j], \
                                       dp[i%2][j] + (word1[i] == word2[j]))
        return m + n - 2*dp[m%2][n]