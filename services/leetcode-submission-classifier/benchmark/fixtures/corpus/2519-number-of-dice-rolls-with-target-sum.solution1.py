# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-dice-rolls-with-target-sum
# source_path: LeetCode-Solutions-master/Python/number-of-dice-rolls-with-target-sum.py
# solution_class: Solution
# submission_id: 85ebbf8e678d6b36276ec6d0ebabfb74e2de16b7
# seed: 3292578788

# Time:  O(d * f * t)
# Space: O(t)

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [[0 for _ in xrange(target+1)] for _ in xrange(2)]
        dp[0][0] = 1
        for i in xrange(1, d+1):
            dp[i%2] = [0 for _ in xrange(target+1)]
            for k in xrange(1, f+1):
                for j in xrange(k, target+1):
                    dp[i%2][j] = (dp[i%2][j] + dp[(i-1)%2][j-k]) % MOD
        return dp[d%2][target] % MOD