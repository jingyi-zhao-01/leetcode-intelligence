# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-an-hourglass
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-an-hourglass.py
# solution_class: Solution
# submission_id: e4ee8b320e5134bc9799d511bc9d6bf7b2dcf8c6
# seed: 3630901398

# Time:  O(m * n)
# Space: O(1)

# brute force

class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def total(i, j):
            return (grid[i][j]+grid[i][j+1]+grid[i][j+2]+
                               grid[i+1][j+1]+
                    grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])

        return max(total(i, j) for i in xrange(len(grid)-2) for j in xrange(len(grid[0])-2))