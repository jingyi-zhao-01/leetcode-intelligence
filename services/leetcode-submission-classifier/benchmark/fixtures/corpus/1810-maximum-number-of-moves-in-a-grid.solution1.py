# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-moves-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-moves-in-a-grid.py
# solution_class: Solution
# submission_id: 0ea1c4a9489cd1c0b3ee95886c9a33aeee651302
# seed: 3695917643

# Time:  O(m * n)
# Space: O(m)

# dp

class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [True]*len(grid)
        result = 0
        for c in xrange(len(grid[0])-1):
            new_dp = [False]*len(grid)
            for r in xrange(len(grid)):
                if not dp[r]:
                    continue
                if grid[r][c] < grid[r][c+1]:
                    new_dp[r] = True
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_dp[r-1] = True
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_dp[r+1] = True
            dp = new_dp
            if not sum(dp):
                break
        else:
            c = len(grid[0])-1
        return c