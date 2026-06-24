# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-iv
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-iv.py
# solution_class: Solution2
# submission_id: 9097c5e7383f79cb334abc0d7af5902cc2c69f30
# seed: 3644054237

# Time:  O(n) on average, using Median of Medians could achieve O(n) (Intro Select)
# Space: O(n)

import random

class Solution2(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def maxAtMostNPairsProfit(sprices):
            profit = 0
            for i in xrange(len(prices) - 1):
                profit += max(0, prices[i + 1] - prices[i])
            return profit

        def maxAtMostKPairsProfit(prices, k):
            max_buy = [float("-inf") for _ in xrange(k + 1)]
            max_sell = [0 for _ in xrange(k + 1)]
            for i in xrange(len(prices)):
                for j in xrange(1, k + 1):
                    max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                    max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
            return max_sell[k]

        if k >= len(prices) // 2:
            return maxAtMostNPairsProfit(prices)

        return maxAtMostKPairsProfit(prices, k)