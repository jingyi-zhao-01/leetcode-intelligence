# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-split-into-ones
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-split-into-ones.py
# solution_class: Solution
# submission_id: 42f21dfac2ff2bf451145e8d83f14e4509849385
# seed: 1070133126

# Time:  O(1)
# Space: O(1)

# combinatorics

class Solution(object):
    def minCost(self, n):
        """
        :type n: int
        :rtype: int
        """
        def nC2(n):
            return n*(n-1)//2

        return nC2(n)