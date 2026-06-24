# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profit-from-trading-stocks-with-discounts
# source_path: LeetCode-Solutions-master/Python/maximum-profit-from-trading-stocks-with-discounts.py
# solution_class: Solution2
# submission_id: 1b67577f5851480b29dd2436f3bf570c2afd3e95
# seed: 81493859

# Time:  O(n * b)
# Space: O(n + b)

import collections


# iterative dfs, tree dp

class Solution2(object):
    def maxProfit(self, n, present, future, hierarchy, budget):
        """
        :type n: int
        :type present: List[int]
        :type future: List[int]
        :type hierarchy: List[List[int]]
        :type budget: int
        :rtype: int
        """
        def dfs(u):
            dp = [collections.defaultdict(int) for _ in xrange(2)]
            dp[0][0] = dp[1][0] = 0
            for v in adj[u]:
                new_dp = dfs(v)
                for i in xrange(2):
                    for j1, v1 in dp[i].items():
                        for j2, v2 in new_dp[i].iteritems():
                            if j1+j2 <= budget:
                                dp[i][j1+j2] = max(dp[i][j1+j2], v1+v2)
            result = [collections.defaultdict(int) for _ in xrange(2)]
            for i in xrange(2):
                for j, v in dp[0].iteritems():
                    result[i][j] = max(result[i][j], v)
                cost = present[u]>>i
                if cost > budget:
                    continue
                profit = future[u]-cost
                for j, v in dp[1].iteritems():
                    if j+cost <= budget:
                        result[i][j+cost] = max(result[i][j+cost], v+profit)
            return result  # result[i][j]: max profit for budget j with i discount

        adj = [[] for _ in xrange(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1)
        return max(dfs(0)[0].itervalues())