# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock.py
# solution_class: Solution
# submission_id: be8334e761f0b783d9e0e988b073210c0b6e12e6
# seed: 1459815283

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit