# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-possible-stable-binary-arrays-ii
# source_path: LeetCode-Solutions-master/Python/find-all-possible-stable-binary-arrays-ii.py
# solution_class: Solution
# submission_id: 5b1c295d0bfa2a992a41d53bdee40b98e0ae263e
# seed: 561961241

# Time:  O(n * m)
# Space: O(n * m)

# dp

class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[[0]*2 for _ in xrange(one+1)] for _ in xrange(zero+1)]
        for i in xrange(zero+1):
            dp[i][0][0] = 1 if i <= limit else 0
        for j in xrange(one+1):
            dp[0][j][1] = 1 if j <= limit else 0
        for i in xrange(1, zero+1):
            for j in xrange(1, one+1):
                dp[i][j][0] = (dp[i-1][j][0]+dp[i-1][j][1])%MOD
                dp[i][j][1] = (dp[i][j-1][0]+dp[i][j-1][1])%MOD
                if i-limit-1 >= 0:
                    dp[i][j][0] = (dp[i][j][0]-dp[i-limit-1][j][1])%MOD
                if j-limit-1 >= 0:
                    dp[i][j][1] = (dp[i][j][1]-dp[i][j-limit-1][0])%MOD
        return (dp[-1][-1][0]+dp[-1][-1][1])%MOD