# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-arrays-identical
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-arrays-identical.py
# solution_class: Solution
# submission_id: 044e737617fae751105d7e70acd7c5b869ee9519
# seed: 656536726

# Time:  O(nlogn)
# Space: O(1)

import itertools


# greedy, sort

class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        def cost():
            return sum(abs(x-y) for x, y in itertools.izip(arr, brr))

        result = cost()
        arr.sort()
        brr.sort()
        result = min(result, k+cost())
        return result