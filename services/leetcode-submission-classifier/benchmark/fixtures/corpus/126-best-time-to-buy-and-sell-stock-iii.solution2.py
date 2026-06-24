# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-iii
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-iii.py
# solution_class: Solution2
# submission_id: 1afb25619fdf561c6d9ba32d99a057a93d4e421c
# seed: 3643739231

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def maxAtMostKPairsProfit(prices, k):
            max_buy = [float("-inf") for _ in xrange(k + 1)]
            max_sell = [0 for _ in xrange(k + 1)]
            for i in xrange(len(prices)):
                for j in xrange(1, k + 1):
                    max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                    max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
            return max_sell[k]

        return maxAtMostKPairsProfit(prices, 2)