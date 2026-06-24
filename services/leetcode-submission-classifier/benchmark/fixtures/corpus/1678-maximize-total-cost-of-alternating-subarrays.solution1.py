# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-total-cost-of-alternating-subarrays
# source_path: LeetCode-Solutions-master/Python/maximize-total-cost-of-alternating-subarrays.py
# solution_class: Solution
# submission_id: c2f41603826f32f574be15ea4841a369035ae1ec
# seed: 2372378310

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0], float("-inf")]
        for i in xrange(1, len(nums)):
            dp[:] = [max(dp)+nums[i], dp[0]-nums[i]]
        return max(dp)