# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-all-ones-with-row-and-column-flips
# source_path: LeetCode-Solutions-master/Python/remove-all-ones-with-row-and-column-flips.py
# solution_class: Solution
# submission_id: 9beaea6fb6de0ef9ce2b48f65ac5390e53354061
# seed: 4197998334

# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        return all(grid[i] == grid[0] or all(grid[i][j] != grid[0][j] for j in xrange(len(grid[0]))) for i in xrange(1, len(grid)))