# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-make-columns-strictly-increasing
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-make-columns-strictly-increasing.py
# solution_class: Solution
# submission_id: c051c83fa7ea7507cd7266cf075a1d194bac9e64
# seed: 382227080

# Time:  O(m * n)
# Space: O(1)

# greedy

class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)-1):
            for j in xrange(len(grid[0])):
                if grid[i][j]+1 <= grid[i+1][j]:
                    continue
                result += (grid[i][j]+1)-grid[i+1][j]
                grid[i+1][j] = grid[i][j]+1
        return result