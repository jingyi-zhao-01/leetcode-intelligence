# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: projection-area-of-3d-shapes
# source_path: LeetCode-Solutions-master/Python/projection-area-of-3d-shapes.py
# solution_class: Solution
# submission_id: 5a70d198ec32be716ed8b1439e0b12a213894bb7
# seed: 4145863456

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)):
            max_row, max_col = 0, 0
            for j in xrange(len(grid)):
                if grid[i][j]:
                    result += 1
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            result += max_row + max_col
        return result