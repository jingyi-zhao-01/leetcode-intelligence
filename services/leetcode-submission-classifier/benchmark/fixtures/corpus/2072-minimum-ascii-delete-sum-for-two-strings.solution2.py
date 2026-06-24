# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-ascii-delete-sum-for-two-strings
# source_path: LeetCode-Solutions-master/Python/minimum-ascii-delete-sum-for-two-strings.py
# solution_class: Solution2
# submission_id: 43b7b5348ad223b5fdf0762ac39c3ded1615de92
# seed: 2088789539

# Time:  O(m * n)
# Space: O(n)

class Solution2(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in xrange(len(s1)+1)]
        for i in xrange(len(s1)):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for j in xrange(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), \
                                       dp[i+1][j] + ord(s2[j]))

        return dp[-1][-1]