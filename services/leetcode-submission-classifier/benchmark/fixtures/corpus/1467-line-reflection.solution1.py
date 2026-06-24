# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: line-reflection
# source_path: LeetCode-Solutions-master/Python/line-reflection.py
# solution_class: Solution
# submission_id: 9208b40f0ae1601f8199cfa9f3ed8d4757a1d0bd
# seed: 1137963762

# Time:  O(n)
# Space: O(n)

import collections


# Hash solution.

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        groups_by_y = collections.defaultdict(set)
        left, right = float("inf"), float("-inf")
        for p in points:
            groups_by_y[p[1]].add(p[0])
            left, right = min(left, p[0]), max(right, p[0])
        mid = left + right
        for group in groups_by_y.values():
            for x in group:
                if mid - x not in group:
                    return False
        return True