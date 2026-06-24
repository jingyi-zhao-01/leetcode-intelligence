# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: surface-area-of-3d-shapes
# source_path: LeetCode-Solutions-master/Python/surface-area-of-3d-shapes.py
# solution_class: Solution
# submission_id: 22c052547562547bba35c4bd0607480a82ba838d
# seed: 324612205

# Time:  O(n^2)
# Space: O(1)

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid)):
                if grid[i][j]:
                    result += 2 + grid[i][j]*4
                if i:
                    result -= min(grid[i][j], grid[i-1][j])*2
                if j:
                    result -= min(grid[i][j], grid[i][j-1])*2
        return result