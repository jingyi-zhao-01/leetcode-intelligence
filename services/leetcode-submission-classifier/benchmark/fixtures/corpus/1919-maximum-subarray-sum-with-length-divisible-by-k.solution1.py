# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subarray-sum-with-length-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/maximum-subarray-sum-with-length-divisible-by-k.py
# solution_class: Solution
# submission_id: 78d7d2b1eddd98cf5fee04e9c0b822b3c8f39d01
# seed: 260447358

# Time:  O(n)
# Space: O(k)

# prefix sum, dp

class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [float("inf")]*k
        dp[-1] = 0
        curr = 0
        result = float("-inf")
        for i, x in enumerate(nums):
            curr += x
            result = max(result, curr-dp[i%k])
            dp[i%k] = min(dp[i%k], curr)
        return result