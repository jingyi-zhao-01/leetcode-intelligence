# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: difference-between-ones-and-zeros-in-row-and-column
# source_path: LeetCode-Solutions-master/Python/difference-between-ones-and-zeros-in-row-and-column.py
# solution_class: Solution
# submission_id: 86411539f5433015761f27368e386bcd02d59023
# seed: 461022953

# Time:  O(m * n)
# Space: O(m + n)

# array

class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = [sum(grid[i][j] for j in xrange(len(grid[0]))) for i in xrange(len(grid))]
        cols = [sum(grid[i][j] for i in xrange(len(grid))) for j in xrange(len(grid[0]))]
        return [[rows[i]+cols[j]-(len(grid)-rows[i])-(len(grid[0])-cols[j]) for j in xrange(len(grid[0]))] for i in xrange(len(grid))]