# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: interval-list-intersections
# source_path: LeetCode-Solutions-master/Python/interval-list-intersections.py
# solution_class: Solution
# submission_id: 345c13be24f5e1e01c90e38d69a9a509ea47e398
# seed: 1960375629

# Time:  O(m + n)
# Space: O(1)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            left = max(A[i].start, B[j].start)
            right = min(A[i].end, B[j].end)
            if left <= right:
                result.append(Interval(left, right))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return result