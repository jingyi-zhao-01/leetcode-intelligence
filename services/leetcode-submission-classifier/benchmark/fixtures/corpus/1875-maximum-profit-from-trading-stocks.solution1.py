# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-profit-from-trading-stocks
# source_path: LeetCode-Solutions-master/Python/maximum-profit-from-trading-stocks.py
# solution_class: Solution
# submission_id: aeffe79163b38b1a4eda84ed048ccb39fb37664b
# seed: 2980916183

# Time:  O(n * b)
# Space: O(b)

import itertools


# dp, optimized from solution2

class Solution(object):
    def maximumProfit(self, present, future, budget):
        """
        :type present: List[int]
        :type future: List[int]
        :type budget: int
        :rtype: int
        """
        dp = [0]*(budget+1)
        for i, (p, f) in enumerate(itertools.izip(present, future)):
            if f-p < 0:
                continue
            for b in reversed(xrange(p, budget+1)):
                dp[b] = max(dp[b], dp[b-p]+(f-p))
        return dp[-1]