# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-knight-tour-configuration
# source_path: LeetCode-Solutions-master/Python/check-knight-tour-configuration.py
# solution_class: Solution
# submission_id: 884a5d4d191cc84f7cb546ed62fe18a18f2eede4
# seed: 180370320

# Time:  O(m * n)
# Space: O(m * n)

# hash table, simulation

class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if grid[0][0]:
            return False
        lookup = [None]*(len(grid)*len(grid[0]))
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                lookup[grid[i][j]] = (i, j)
        return all(sorted([abs(lookup[i+1][0]-lookup[i][0]), abs(lookup[i+1][1]-lookup[i][1])]) == [1, 2] for i in xrange(len(lookup)-1))