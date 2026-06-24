# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-score-subarray-queries
# source_path: LeetCode-Solutions-master/Python/maximum-xor-score-subarray-queries.py
# solution_class: Solution
# submission_id: 0fc802b8bac6dd0384cc52dd2bace0340b1ec620
# seed: 3534945555

# Time:  O(n^2 + q)
# Space: O(n^2)

# dp

class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [[nums[i] if j == 0 else 0 for j in xrange(len(nums)-i)] for i in xrange(len(nums))]
        for i in reversed(xrange(len(nums))):
            for l in xrange(1, len(nums)-i):
                dp[i][l] = dp[i][l-1]^dp[i+1][l-1]
        for i in reversed(xrange(len(nums))):
            for l in xrange(1, len(nums)-i):
                dp[i][l] = max(dp[i][l], dp[i][l-1], dp[i+1][l-1])
        return [dp[i][j-i] for i, j in queries]