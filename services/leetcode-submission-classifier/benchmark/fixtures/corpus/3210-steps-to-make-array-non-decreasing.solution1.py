# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: steps-to-make-array-non-decreasing
# source_path: LeetCode-Solutions-master/Python/steps-to-make-array-non-decreasing.py
# solution_class: Solution
# submission_id: ac59e970c8db2e5c0accd2400e6735fa53fe03d4
# seed: 2880403632

# Time:  O(n)
# Space: O(n)

# mono stack, dp

class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)  # dp[i]: number of rounds for nums[i] to remove all the covered elements
        stk = []
        for i in reversed(xrange(len(nums))):
            while stk and nums[stk[-1]] < nums[i]:
                dp[i] = max(dp[i]+1, dp[stk.pop()])
            stk.append(i)
        return max(dp)