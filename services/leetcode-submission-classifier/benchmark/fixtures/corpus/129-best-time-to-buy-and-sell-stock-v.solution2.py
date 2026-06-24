# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-v
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-v.py
# solution_class: Solution
# submission_id: 029f2fd18c9fe81e99877c6246e91927733936cd
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
        bought = [float("-inf")]*k
        sold = [float("-inf")]*k
        result = [0]*(k+1)
        for x in prices:
            for i in reversed(xrange(k)):
                result[i+1] = max(result[i+1], bought[i]+x, sold[i]-x)
                bought[i] = max(bought[i], result[i]-x)
                sold[i] = max(sold[i], result[i]+x)
        return result[-1]