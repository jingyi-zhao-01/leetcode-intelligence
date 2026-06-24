# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-increasing-subsequence
# source_path: LeetCode-Solutions-master/Python/longest-increasing-subsequence.py
# solution_class: Solution5
# submission_id: c966e41f145aa119e644203a6177d79fdcbd8fd5
# seed: 753233972

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution5(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0