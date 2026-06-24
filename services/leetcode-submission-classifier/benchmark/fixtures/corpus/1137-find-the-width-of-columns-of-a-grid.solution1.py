# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-width-of-columns-of-a-grid
# source_path: LeetCode-Solutions-master/Python/find-the-width-of-columns-of-a-grid.py
# solution_class: Solution
# submission_id: b02298db21651f6a8c112e3cc9e4a107f358993d
# seed: 2275759213

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        def length(x):
            l = 1
            if x < 0:
                x = -x
                l += 1
            while x >= 10:
                x //= 10
                l += 1
            return l

        return [max(length(grid[i][j]) for i in xrange(len(grid))) for j in xrange(len(grid[0]))]