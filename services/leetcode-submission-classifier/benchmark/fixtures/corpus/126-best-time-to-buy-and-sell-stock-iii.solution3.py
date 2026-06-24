# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-iii
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-iii.py
# solution_class: Solution3
# submission_id: a4115e0908910f73a037b52b08cfc30ebbf9ff80
# seed: 3347225445

# Time:  O(n)
# Space: O(1)

class Solution3(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = \
            float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)

        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right,
                                        max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit,
                             max_profits_from_left[i] +
                             max_profits_from_right[i])

        return max_profit