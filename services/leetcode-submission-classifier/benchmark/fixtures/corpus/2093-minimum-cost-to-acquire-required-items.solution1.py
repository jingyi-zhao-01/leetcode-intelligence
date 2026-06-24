# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-acquire-required-items
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-acquire-required-items.py
# solution_class: Solution
# submission_id: 36ae13c45fb5c3d786690331ce20cc5f54d261d5
# seed: 240503451

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
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
        return mn*min(cost1+cost2, costBoth)+min((need1-mn)*cost1+(need2-mn)*cost2, (mx-mn)*costBoth)