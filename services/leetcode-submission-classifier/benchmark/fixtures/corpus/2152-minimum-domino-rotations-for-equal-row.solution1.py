# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-domino-rotations-for-equal-row
# source_path: LeetCode-Solutions-master/Python/minimum-domino-rotations-for-equal-row.py
# solution_class: Solution
# submission_id: 2161ef365adc8af83083e849ab8447e2c0e9a61e
# seed: 765172597

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        intersect = reduce(set.__and__, [set(d) for d in itertools.izip(A, B)])
        if not intersect:
            return -1
        x = intersect.pop()
        return min(len(A)-A.count(x), len(B)-B.count(x))