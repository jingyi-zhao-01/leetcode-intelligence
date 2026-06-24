# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-grid-satisfies-conditions
# source_path: LeetCode-Solutions-master/Python/check-if-grid-satisfies-conditions.py
# solution_class: Solution
# submission_id: 022166def5b212999f1cb9e9286b22b3af566ff2
# seed: 4019551270

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        return (all(grid[i][j] == grid[i+1][j] for j in xrange(len(grid[0])) for i in xrange(len(grid)-1)) and 
                all(grid[0][j] != grid[0][j+1] for j in xrange(len(grid[0])-1)))