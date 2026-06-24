# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-log-transportation-cost
# source_path: LeetCode-Solutions-master/Python/find-minimum-log-transportation-cost.py
# solution_class: Solution
# submission_id: 37126c3428190172ec11e7b0e026d57c785217a2
# seed: 3400787828

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        return k*max(n-k, m-k, 0)