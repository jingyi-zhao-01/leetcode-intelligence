# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: max-increase-to-keep-city-skyline
# source_path: LeetCode-Solutions-master/Python/max-increase-to-keep-city-skyline.py
# solution_class: Solution
# submission_id: e873737a85c8160d669d29345c4d0ab6e17af20d
# seed: 991284607

# Time:  O(n^2)
# Space: O(n)

import itertools

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in itertools.izip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c])-val \
                   for r, row in enumerate(grid) \
                   for c, val in enumerate(row))