# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-moves-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-moves-in-a-grid.py
# solution_class: Solution2
# submission_id: 7fa7f53c162ed329e5223c17ed55fa14cab367b0
# seed: 602811724

# Time:  O(m * n)
# Space: O(m)

# dp

class Solution2(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0]*len(grid)
        for c in reversed(xrange(len(grid[0])-1)):
            new_dp = [0]*len(grid)
            for r in xrange(len(grid)):
                if grid[r][c] < grid[r][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r]+1)
                if r-1 >= 0 and grid[r][c] < grid[r-1][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r-1]+1)
                if r+1 < len(grid) and grid[r][c] < grid[r+1][c+1]:
                    new_dp[r] = max(new_dp[r], dp[r+1]+1)
            dp = new_dp
        return max(dp)