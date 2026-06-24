# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subsequence-with-decreasing-adjacent-difference
# source_path: LeetCode-Solutions-master/Python/longest-subsequence-with-decreasing-adjacent-difference.py
# solution_class: Solution2
# submission_id: 3a94b9ad3b149151a59ff34a86dc15e38d9439ff
# seed: 4144792992

# Time:  O(r^2 + n * r), r = max(nums)
# Space: O(r^2)

# dp

class Solution2(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2
        mx = max(nums)
        dp = [[0]*mx for _ in xrange(mx)]
        for x in reversed(nums):
            x -= 1
            for nx in xrange(len(dp[x])):
                d = abs(nx-x)
                dp[x][d] = max(dp[x][d], dp[nx][d]+1)
            for d in xrange(1, len(dp[x])):
                dp[x][d] = max(dp[x][d], dp[x][d-1])
            result = max(result, dp[x][-1])
        return result