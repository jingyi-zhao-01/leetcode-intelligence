# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-v
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-v.py
# solution_class: Solution
# submission_id: 8b600a7056c17fe4f5f089b66243dda853b4297c
# seed: 3380413398

# Time:  O(n * k)
# Space: O(k)

# dp

class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0]*(len(prices)+1)
        result = 0
        for i in xrange(k):
            x, y = float("-inf"), float("-inf")
            new_dp = [float("-inf")]*(len(prices)+1)
            for j in xrange(i, len(prices)):
                x, y = max(x, dp[j]-prices[j]), max(y, dp[j]+prices[j])
                new_dp[j+1] = max(new_dp[j], x+prices[j], y-prices[j])
            dp = new_dp
            result = max(result, dp[-1])
        return result