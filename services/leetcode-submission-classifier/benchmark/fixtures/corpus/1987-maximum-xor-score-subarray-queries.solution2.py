# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-score-subarray-queries
# source_path: LeetCode-Solutions-master/Python/maximum-xor-score-subarray-queries.py
# solution_class: Solution2
# submission_id: 2e951bd0537afd463394819a4c2000185a184293
# seed: 1669714073

# Time:  O(n^2 + q)
# Space: O(n^2)

# dp

class Solution2(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [[nums[i] if i == j else 0 for j in xrange(len(nums))] for i in xrange(len(nums))]
        for i in reversed(xrange(len(nums))):
            for j in xrange(i+1, len(nums)):
                dp[i][j] = dp[i][j-1]^dp[i+1][j]
        for i in reversed(xrange(len(nums))):
            for j in xrange(i+1, len(nums)):
                dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i+1][j])
        return [dp[i][j] for i, j in queries]