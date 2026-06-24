# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-earn-points
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-earn-points.py
# solution_class: Solution2
# submission_id: 572a204f00c445abd74b2a10cd4bef548e1b2d38
# seed: 1366050567

# Time:  O(n * t * c)
# Space: O(t)

# knapsack dp

class Solution2(object):
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
            new_dp = [0]*(target+1)
            for i in xrange(target+1):
                for j in xrange(min((target-i)//m, c)+1):
                    new_dp[i+j*m] = (new_dp[i+j*m]+dp[i])%MOD
            dp = new_dp
        return dp[-1]