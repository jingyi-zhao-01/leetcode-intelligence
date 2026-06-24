# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-balanced-shipments
# source_path: LeetCode-Solutions-master/Python/maximum-balanced-shipments.py
# solution_class: Solution
# submission_id: 01ce17eff4f68f4ad73885aa357f73b8f76506af
# seed: 225330038

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxBalancedShipments(self, weight):
        """
        :type weight: List[int]
        :rtype: int
        """
        result = mx = 0
        for x in weight:
            if x < mx:
                mx = 0
                result += 1
            else:
                mx = x
        return result