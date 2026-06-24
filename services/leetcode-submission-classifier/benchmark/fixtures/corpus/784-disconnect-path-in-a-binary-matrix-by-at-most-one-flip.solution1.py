# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: disconnect-path-in-a-binary-matrix-by-at-most-one-flip
# source_path: LeetCode-Solutions-master/Python/disconnect-path-in-a-binary-matrix-by-at-most-one-flip.py
# solution_class: Solution
# submission_id: 41e14e97cd51b3b6bbb5524d4633dcdcdc4d98e2
# seed: 1209357667

# Time:  O(m * n)
# Space: O(m + n)

# dp

class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if (i, j) == (0, 0) or grid[i][j] == 0:
                    continue
                if (i-1 < 0 or grid[i-1][j] == 0) and (j-1 < 0 or grid[i][j-1] == 0):
                    grid[i][j] = 0
        for i in reversed(xrange(len(grid))):
            for j in reversed(xrange(len(grid[0]))):
                if (i, j) == (len(grid)-1, len(grid[0])-1) or grid[i][j] == 0:
                    continue
                if (i+1 >= len(grid) or grid[i+1][j] == 0) and (j+1 >= len(grid[0]) or grid[i][j+1] == 0):
                    grid[i][j] = 0
        cnt = [0]*(len(grid)+len(grid[0])-1)
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                cnt[i+j] += grid[i][j]
        return any(cnt[i] <= 1 for i in xrange(1, len(grid)+len(grid[0])-2))