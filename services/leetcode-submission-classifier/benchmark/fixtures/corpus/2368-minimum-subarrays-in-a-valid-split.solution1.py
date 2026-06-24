# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-subarrays-in-a-valid-split
# source_path: LeetCode-Solutions-master/Python/minimum-subarrays-in-a-valid-split.py
# solution_class: Solution
# submission_id: 99dc89b9c7bb9901405d9f823a47e8f673f20334
# seed: 552964538

# Time:  O(n^2 * logr), r = max(nums)
# Space: O(n)

# dp

class Solution(object):
    def validSubarraySplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        dp = [float("inf")]*(len(nums)+1)  # dp[i]: min number of subarrays in nums[:i]
        dp[0] = 0
        for i in xrange(1, len(nums)+1):
            for j in xrange(i):
                 if gcd(nums[j], nums[i-1]) != 1:
                     dp[i] = min(dp[i], dp[j]+1)
        return dp[-1] if dp[-1] != float("inf") else -1