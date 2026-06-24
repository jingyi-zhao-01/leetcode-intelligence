# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: visit-array-positions-to-maximize-score
# source_path: LeetCode-Solutions-master/Python/visit-array-positions-to-maximize-score.py
# solution_class: Solution
# submission_id: 7b0252bd83dd9037136f17d7792905ea737a5859
# seed: 3834399571

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        dp = [float("-inf")]*2
        dp[nums[0]%2] = nums[0]
        for i in xrange(1, len(nums)):
            dp[nums[i]%2] = max(dp[nums[i]%2], dp[(nums[i]+1)%2]-x)+nums[i]
        return max(dp)