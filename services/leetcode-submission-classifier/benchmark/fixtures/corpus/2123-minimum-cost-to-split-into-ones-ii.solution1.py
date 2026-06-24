# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-split-into-ones-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-split-into-ones-ii.py
# solution_class: Solution
# submission_id: 87f62589ece3025a9f36036d821741f8bc052b6f
# seed: 3399530013

# Time:  O(1)
# Space: O(1)

# math, invariant

class Solution(object):
    def minCost(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n*(n-1)//2