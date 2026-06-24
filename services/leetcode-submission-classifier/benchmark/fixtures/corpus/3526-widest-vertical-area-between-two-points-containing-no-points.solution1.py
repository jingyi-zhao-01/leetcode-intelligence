# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: widest-vertical-area-between-two-points-containing-no-points
# source_path: LeetCode-Solutions-master/Python/widest-vertical-area-between-two-points-containing-no-points.py
# solution_class: Solution
# submission_id: 94527a029387678ebf3879b40e3776360cc6d9a4
# seed: 4269823679

# Time:  O(nlogn)
# Space: O(n)

import itertools

class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_x = sorted({x for x, y in points})
        return max([b-a for a, b in itertools.izip(sorted_x, sorted_x[1:])] + [0])