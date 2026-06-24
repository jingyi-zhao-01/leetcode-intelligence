# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-the-profit-as-the-salesman
# source_path: LeetCode-Solutions-master/Python/maximize-the-profit-as-the-salesman.py
# solution_class: Solution
# submission_id: 8135d51417047caf7f737b7e330a0700270e927e
# seed: 679787463

# Time:  O(n + m), m = len(offers)
# Space: O(n + m)

# dp

class Solution(object):
    def maximizeTheProfit(self, n, offers):
        """
        :type n: int
        :type offers: List[List[int]]
        :rtype: int
        """
        lookup = [[] for _ in xrange(n)]
        for s, e, g in offers:
            lookup[e].append([s, g])
        dp = [0]*(n+1)
        for e in xrange(n):
            dp[e+1] = dp[(e-1)+1]
            for s, g in lookup[e]:
                dp[e+1] = max(dp[e+1], dp[(s-1)+1]+g)
        return dp[-1]