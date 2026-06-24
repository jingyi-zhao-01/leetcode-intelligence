# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cherry-pickup-ii
# source_path: LeetCode-Solutions-master/Python/cherry-pickup-ii.py
# solution_class: Solution
# submission_id: f1c15c2ea476b566c5453c14b6ffdf16cd8a7ebc
# seed: 2649012104

# Time:  O(m * n^2)
# Space: O(n^2)

import itertools

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[[float("-inf")]*(len(grid[0])+2) for _ in xrange(len(grid[0])+2)] for _ in xrange(2)]
        dp[0][1][len(grid[0])] = grid[0][0] + grid[0][len(grid[0])-1]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])+1):
                for k in xrange(1, len(grid[0])+1):
                    dp[i%2][j][k] = max(dp[(i-1)%2][j+d1][k+d2] for d1 in xrange(-1, 2) for d2 in xrange(-1, 2)) + \
                                    ((grid[i][j-1]+grid[i][k-1]) if j != k else grid[i][j-1])
        return max(itertools.imap(max, *dp[(len(grid)-1)%2]))