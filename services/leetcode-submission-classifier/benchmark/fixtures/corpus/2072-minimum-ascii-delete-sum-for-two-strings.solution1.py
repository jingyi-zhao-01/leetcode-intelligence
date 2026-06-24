# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-ascii-delete-sum-for-two-strings
# source_path: LeetCode-Solutions-master/Python/minimum-ascii-delete-sum-for-two-strings.py
# solution_class: Solution
# submission_id: ab941b093e0320020b21a28cafb8ae248bb0f07f
# seed: 477716253

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2)+1) for _ in xrange(2)]
        for j in xrange(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in xrange(len(s1)):
            dp[(i+1)%2][0] = dp[i%2][0] + ord(s1[i])
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j+1] = min(dp[i%2][j+1] + ord(s1[i]), \
                                           dp[(i+1)%2][j] + ord(s2[j]))

        return dp[len(s1)%2][-1]