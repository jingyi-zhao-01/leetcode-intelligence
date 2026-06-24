# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-earn-points
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-earn-points.py
# solution_class: Solution
# submission_id: c4a968f3d98e9e050daed8425d11d1c789489dd7
# seed: 1580483168

# Time:  O(n * t * c)
# Space: O(t)

# knapsack dp

class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(target+1)
        dp[0] = 1
        for c, m in types:
            for i in reversed(xrange(1, target+1)):
                for j in xrange(1, min(i//m, c)+1):
                    dp[i] = (dp[i]+dp[i-j*m])%MOD
        return dp[-1]