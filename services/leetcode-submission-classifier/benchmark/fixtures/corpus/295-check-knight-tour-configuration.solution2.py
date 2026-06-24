# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-knight-tour-configuration
# source_path: LeetCode-Solutions-master/Python/check-knight-tour-configuration.py
# solution_class: Solution2
# submission_id: 7fdd7f2d334c8137a0f4f3b4cfe9f039a44f09eb
# seed: 1745870487

# Time:  O(m * n)
# Space: O(m * n)

# hash table, simulation

class Solution2(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        lookup = {grid[i][j]:(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0]))}
        return grid[0][0] == 0 and all(sorted([abs(lookup[i+1][0]-lookup[i][0]), abs(lookup[i+1][1]-lookup[i][1])]) == [1, 2] for i in xrange(len(lookup)-1))