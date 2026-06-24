# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-length-of-a-good-subsequence-i
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-length-of-a-good-subsequence-i.py
# solution_class: Solution
# submission_id: 863e833e67fcd2149d5018bf86b971e05b55a491
# seed: 2603628334

# Time:  O(n * k)
# Space: O(n * k)

import collections


# dp

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0]*(k+1) for _ in xrange(len(nums))]
        result = 0
        for i in xrange(len(nums)):
            dp[i][0] = 1
            for l in xrange(k+1):
                for j in xrange(i):
                    dp[i][l] = max(dp[i][l], dp[j][l]+1 if nums[j] == nums[i] else 1, dp[j][l-1]+1 if l-1 >= 0 else 1)
                result = max(result, dp[i][l])
        return result