# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-operations-to-satisfy-conditions
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-operations-to-satisfy-conditions.py
# solution_class: Solution2
# submission_id: 59ff8bec0832f2e21050ad345e1b0a27d04ae7a5
# seed: 2102939375

# Time:  O(n * (m + 10))
# Space: O(10)

# dp

class Solution2(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        INF = float("inf")
        MAX_VALUE = 9
        dp = [0]*(MAX_VALUE+1)
        for j in xrange(len(grid[0])):
            new_dp = [INF]*(MAX_VALUE+1)
            cnt = [0]*(MAX_VALUE+1)
            for i in xrange(len(grid)):
                cnt[grid[i][j]] += 1
            for i in xrange(MAX_VALUE+1):
                new_dp[i] = min(new_dp[i], min(dp[k] for k in xrange(MAX_VALUE+1) if k != i)+(len(grid)-cnt[i]))
            dp = new_dp
        return min(dp)