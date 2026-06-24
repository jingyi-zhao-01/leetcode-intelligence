# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-there-is-a-valid-parentheses-string-path
# source_path: LeetCode-Solutions-master/Python/check-if-there-is-a-valid-parentheses-string-path.py
# solution_class: Solution
# submission_id: 3b52c4f3b013870ad287cb8dccb3123161dd76f3
# seed: 1814978955

# Time:  O((m * n) * (m + n) / 32)
# Space: O(n * (m + n) / 32)

# dp with bitsets

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        if (len(grid)+len(grid[0])-1)%2:
            return False
        dp = [0]*(len(grid[0])+1)
        for i in xrange(len(grid)):
            dp[0] = int(not i)
            for j in xrange(len(grid[0])):
                dp[j+1] = (dp[j]|dp[j+1])<<1 if grid[i][j] == '(' else (dp[j]|dp[j+1])>>1
        return dp[-1]&1