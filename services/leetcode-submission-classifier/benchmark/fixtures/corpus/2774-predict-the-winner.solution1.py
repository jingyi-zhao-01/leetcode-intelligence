# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: predict-the-winner
# source_path: LeetCode-Solutions-master/Python/predict-the-winner.py
# solution_class: Solution
# submission_id: f3c993163e3a7b674a916d08b1cdcf0a1b780321
# seed: 92190941

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        dp = [0] * len(nums)
        for i in reversed(xrange(len(nums))):
            dp[i] = nums[i]
            for j in xrange(i+1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0