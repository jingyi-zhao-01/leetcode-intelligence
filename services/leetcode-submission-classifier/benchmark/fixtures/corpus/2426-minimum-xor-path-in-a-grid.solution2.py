# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-xor-path-in-a-grid
# source_path: LeetCode-Solutions-master/Python/minimum-xor-path-in-a-grid.py
# solution_class: Solution2
# submission_id: 9ad6f75d6e9bafe6bcc17da47e3706d58a9087ab
# seed: 63310444

# Time:  O(m * n * r), r = max(x for row in grid for x in row)
# Space: O(n * r)

# dp

class Solution2(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [set() for _ in xrange(len(grid[0]))]
        dp[0].add(0)
        for i in xrange(len(grid)):
            new_dp = [set() for _ in xrange(len(grid[0]))]
            for j in xrange(len(grid[0])):
                for k in dp[j]|(new_dp[j-1] if j-1 >= 0 else set()):
                    new_dp[j].add(k^grid[i][j])
            dp = new_dp
        return min(dp[-1])