# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-prices-with-a-special-discount-in-a-shop
# source_path: LeetCode-Solutions-master/Python/final-prices-with-a-special-discount-in-a-shop.py
# solution_class: Solution
# submission_id: 669815185c60e5309df1399cfc526dfc2c6506dc
# seed: 979913360

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stk = []
        for i, p in enumerate(prices):
            while stk and prices[stk[-1]] >= p:
                prices[stk.pop()] -= p
            stk.append(i)
        return prices