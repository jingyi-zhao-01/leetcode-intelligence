# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-with-transaction-fee
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-with-transaction-fee.py
# solution_class: Solution
# submission_id: 31327f30f334b50a2f6a6941fe7b858ff05eee36
# seed: 3616498079

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for i in xrange(1, len(prices)):
            cash = max(cash, hold+prices[i]-fee)
            hold = max(hold, cash-prices[i])
        return cash