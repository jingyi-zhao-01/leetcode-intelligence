# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: best-time-to-buy-and-sell-stock-iii
# source_path: LeetCode-Solutions-master/Python/best-time-to-buy-and-sell-stock-iii.py
# solution_class: Solution
# submission_id: bf24d34aa639b608e03e0d85d4423f014a36f692
# seed: 1254065462

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            hold1 = max(hold1, -i)
            release1 = max(release1, hold1 + i)
            hold2 = max(hold2, release1 - i)
            release2 = max(release2, hold2 + i)
        return release2