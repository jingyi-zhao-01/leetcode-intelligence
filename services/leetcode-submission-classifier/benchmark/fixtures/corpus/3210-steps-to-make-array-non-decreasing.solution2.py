# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: steps-to-make-array-non-decreasing
# source_path: LeetCode-Solutions-master/Python/steps-to-make-array-non-decreasing.py
# solution_class: Solution2
# submission_id: 716250a3761ae879c0ff251b25be95eb0718f568
# seed: 2387436870

# Time:  O(n)
# Space: O(n)

# mono stack, dp

class Solution2(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)  # dp[i]: number of rounds for nums[i] to be removed
        stk = []
        for i in xrange(len(nums)):
            curr = 0
            while stk and nums[stk[-1]] <= nums[i]:
                curr = max(curr, dp[stk.pop()])
            if stk:
                dp[i] = curr+1
            stk.append(i)
        return max(dp)