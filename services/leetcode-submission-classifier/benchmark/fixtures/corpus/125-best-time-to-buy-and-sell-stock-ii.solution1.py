# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-ii
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-ii.py
# solution_class: Solution
# submission_id: 8378d6a7709dc7b69a425ed315bc3d89103eafcc
# seed: 1926216211

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxProfit2(self, prices):
        return sum(map(lambda x: max(prices[x + 1] - prices[x], 0),
                       xrange(len(prices[:-1]))))