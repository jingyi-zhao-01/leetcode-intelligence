# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-acquire-required-items
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-acquire-required-items.py
# solution_class: Solution2
# submission_id: 951633f363254271821f25ef962812fe82b6f94a
# seed: 3473078698

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        mn = min(need1, need2)
        mx = max(need1, need2)
        return min(need1*cost1+need2*cost2, mn*costBoth+(need1-mn)*cost1+(need2-mn)*cost2, mx*costBoth)