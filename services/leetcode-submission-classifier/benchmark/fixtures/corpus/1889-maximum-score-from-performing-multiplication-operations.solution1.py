# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-from-performing-multiplication-operations
# source_path: LeetCode-Solutions-master/Python/maximum-score-from-performing-multiplication-operations.py
# solution_class: Solution
# submission_id: 5b13d65109a94e4a3920ad99a901f9dea363591e
# seed: 1917757518

# Time:  O(m^2)
# Space: O(m)

class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        dp = [0]*(len(multipliers)+1)
        for l, m in enumerate(reversed(multipliers), start=len(nums)-len(multipliers)):
            dp = [max(m*nums[i]+dp[i+1], m*nums[i+l]+dp[i]) for i in xrange(len(dp)-1)]
        return dp[0]