# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-matrix-is-x-matrix
# source_path: LeetCode-Solutions-master/Python/check-if-matrix-is-x-matrix.py
# solution_class: Solution
# submission_id: 36183e3d22773c4450c37544d5ae763a30a0da4f
# seed: 1495939611

# Time:  O(n^2)
# Space: O(1)

# array

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        return all((i-j == 0 or i+j == len(grid)-1) == (grid[i][j] != 0) for i in xrange(len(grid)) for j in xrange(len(grid[0])))