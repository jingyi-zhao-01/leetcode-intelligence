# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-width-of-columns-of-a-grid
# source_path: LeetCode-Solutions-master/Python/find-the-width-of-columns-of-a-grid.py
# solution_class: Solution2
# submission_id: f3d0b52d50522b170daf9c95f0fa80c2393613f4
# seed: 3992982724

# Time:  O(m * n)
# Space: O(1)

# array

class Solution2(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        return [max(len(str(grid[i][j])) for i in xrange(len(grid))) for j in xrange(len(grid[0]))]