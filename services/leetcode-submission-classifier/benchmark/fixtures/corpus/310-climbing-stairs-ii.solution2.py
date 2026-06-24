# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: climbing-stairs-ii
# source_path: LeetCode-Solutions-master/Python/climbing-stairs-ii.py
# solution_class: Solution2
# submission_id: 712d6f71a2a2829346c4216f19a78f77bb569a85
# seed: 1736659463

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in xrange(n):
            dp[i+1] = costs[i]+min(dp[i-j]+(j+1)**2 for j in xrange(min(3, i+1)))
        return dp[n]