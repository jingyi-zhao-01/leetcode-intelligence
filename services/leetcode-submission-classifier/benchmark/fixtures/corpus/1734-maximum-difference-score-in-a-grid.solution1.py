# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-score-in-a-grid
# source_path: LeetCode-Solutions-master/Python/maximum-difference-score-in-a-grid.py
# solution_class: Solution
# submission_id: 4f06f2515f39b822bb6cc51014e9f78bd15ba140
# seed: 1539728287

# Time:  O(m * n)
# Space: O(1)

# dp

class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        POS_INF = float("inf")
        NEG_INF = float("-inf")
        result = NEG_INF
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                mn = POS_INF
                if i-1 >= 0:
                    mn = min(mn, grid[i-1][j])
                if j-1 >= 0:
                    mn = min(mn, grid[i][j-1])
                result = max(result, grid[i][j]-mn)
                grid[i][j] = min(grid[i][j], mn)
        return result