# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-swaps-to-arrange-a-binary-grid
# source_path: LeetCode-Solutions-master/Python/minimum-swaps-to-arrange-a-binary-grid.py
# solution_class: Solution
# submission_id: b03b6ca6c56fe21555ab58f238d27bdf2d4dfbba
# seed: 1750814195

# Time:  O(n^2)
# Space: O(1)

import itertools

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for target in reversed(xrange(1, len(grid))):
            row_idx = len(grid)-1-target
            while row_idx < len(grid):
                row = grid[row_idx]
                if not sum(itertools.islice(row, len(row)-target, len(row))):
                    break
                row_idx += 1
            else:
                return -1
            while row_idx != len(grid)-1-target:
                grid[row_idx], grid[row_idx-1] = grid[row_idx-1], grid[row_idx]
                result += 1
                row_idx -= 1
        return result