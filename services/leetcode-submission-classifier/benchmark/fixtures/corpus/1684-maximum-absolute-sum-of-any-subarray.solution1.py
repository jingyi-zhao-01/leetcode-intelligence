# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-absolute-sum-of-any-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-absolute-sum-of-any-subarray.py
# solution_class: Solution
# submission_id: 36644b742f34eb4c8237ced5d2ab690f2c09eaa3
# seed: 390162091

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = mx = mn = 0
        for num in nums:
            curr += num
            mx = max(mx, curr)
            mn = min(mn, curr)
        return mx-mn