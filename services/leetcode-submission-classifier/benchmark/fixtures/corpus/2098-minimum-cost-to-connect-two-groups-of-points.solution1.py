# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-connect-two-groups-of-points
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-connect-two-groups-of-points.py
# solution_class: Solution
# submission_id: 8b0f25d055cea9253a17deea5c149a6993753908
# seed: 4283000369

# Time:  O(m * n * 2^n)
# Space: O(2^n)

# dp with rolling window

class Solution(object):
    def connectTwoGroups(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        total = 2**len(cost[0])
        dp = [[float("inf")]*total for _ in xrange(2)]
        dp[0][0] = 0
        for i in xrange(len(cost)):
            dp[(i+1)%2] = [float("inf")]*total
            for mask in xrange(total):
                base = 1
                for j in xrange(len(cost[0])):
                    dp[i%2][mask|base] = min(dp[i%2][mask|base], cost[i][j]+dp[i%2][mask])
                    dp[(i+1)%2][mask|base] = min(dp[(i+1)%2][mask|base], cost[i][j]+dp[i%2][mask])
                    base <<= 1
        return dp[len(cost)%2][-1]