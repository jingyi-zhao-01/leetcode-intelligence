# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-greatest-value-in-each-row
# source_path: LeetCode-Solutions-master/Python/delete-greatest-value-in-each-row.py
# solution_class: Solution
# submission_id: 0cc918045881ac54cad6c6cb94c742449e71a3cc
# seed: 3310285740

# Time:  O(m * nlogn)
# Space: O(1)

# array

class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in grid:
            row.sort()
        return sum(max(grid[i][j] for i in xrange(len(grid))) for j in xrange(len(grid[0])))