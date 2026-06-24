# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-update-after-k-th-largest-insertion-ii
# source_path: LeetCode-Solutions-master/Python/power-update-after-k-th-largest-insertion-ii.py
# solution_class: Solution
# submission_id: 36accdb657e31ba50f0ef6dd3511852228d78297
# seed: 194385453

# Time:  O((n + q) * log(n * q) + q * logr)
# Space: O(n + q)

from sortedcontainers import SortedList


# sorted list, fast exponentiation

class Solution(object):
    def powerUpdate(self, nums, p, queries):
        """
        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9+7
        sl = SortedList(nums)
        result = []
        for x, k in queries:
            sl.add(x)
            p = pow(p, sl[-k], MOD)
            result.append(p)
        return result