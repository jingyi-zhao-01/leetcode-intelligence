# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: min-cost-climbing-stairs
# source_path: LeetCode-Solutions-master/Python/min-cost-climbing-stairs.py
# solution_class: Solution
# submission_id: 96fcba8b013d89a1414369490454fc00446cad9c
# seed: 1587766851

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * 3
        for i in reversed(xrange(len(cost))):
            dp[i%3] = cost[i] + min(dp[(i+1)%3], dp[(i+2)%3])
        return min(dp[0], dp[1])