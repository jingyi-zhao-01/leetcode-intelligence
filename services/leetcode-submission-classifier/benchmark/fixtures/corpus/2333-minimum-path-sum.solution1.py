# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-path-sum
# source_path: LeetCode-Solutions-master/Python/minimum-path-sum.py
# solution_class: Solution
# submission_id: b8b29bb9aafcf6b19798103b73ec8215e6d0ad7a
# seed: 3011712547

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        for j in xrange(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]

        for i in xrange(1, len(grid)):
            sum[0] += grid[i][0]
            for j in xrange(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

        return sum[-1]