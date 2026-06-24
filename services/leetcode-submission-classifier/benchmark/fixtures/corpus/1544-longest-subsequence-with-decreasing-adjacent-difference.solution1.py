# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-subsequence-with-decreasing-adjacent-difference
# source_path: LeetCode-Solutions-master/Python/longest-subsequence-with-decreasing-adjacent-difference.py
# solution_class: Solution
# submission_id: b8b154fd976dadafc921b209a0435f6ccd0a1d01
# seed: 3323006643

# Time:  O(r^2 + n * r), r = max(nums)
# Space: O(r^2)

# dp

class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 2
        mx = max(nums)
        dp = [[0]*mx for _ in xrange(mx)]
        for x in nums:
            x -= 1
            for nx in xrange(len(dp[x])):
                d = abs(nx-x)
                dp[x][d] = max(dp[x][d], dp[nx][d]+1)
            for d in reversed(xrange(len(dp[x])-1)):
                dp[x][d] = max(dp[x][d], dp[x][d+1])
            result = max(result, dp[x][0])
        return result