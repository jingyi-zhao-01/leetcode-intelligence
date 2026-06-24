# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-fertile-pyramids-in-a-land
# source_path: LeetCode-Solutions-master/Python/count-fertile-pyramids-in-a-land.py
# solution_class: Solution2
# submission_id: b4dd9f72b8954e4146fc18c04dc6b316c49f36ff
# seed: 3226700103

# Time:  O(m * n)
# Space: O(n)

class Solution2(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count(grid):
            dp = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
            for i in xrange(1, len(grid)):
                for j in xrange(1, len(grid[0])-1):
                    if grid[i][j] == grid[i-1][j-1] == grid[i-1][j] == grid[i-1][j+1] == 1:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+1
            return sum(sum(row) for row in dp)
        
        return count(grid) + count(grid[::-1])