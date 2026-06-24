# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: calculate-amount-paid-in-taxes
# source_path: LeetCode-Solutions-master/Python/calculate-amount-paid-in-taxes.py
# solution_class: Solution
# submission_id: 57d49c2660af0effab4a74c0594edd8828286120
# seed: 328426778

# Time:  O(n)
# Space: O(1)

# simulation

class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        result = prev = 0
        for u, p in brackets:
            result += max((min(u, income)-prev)*p/100.0, 0.0)
            prev = u
        return result