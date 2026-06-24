# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-length-of-semi-decreasing-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-length-of-semi-decreasing-subarrays.py
# solution_class: Solution
# submission_id: e0c1372abbdff08e48f58c5b1a7c1849187923ee
# seed: 1776405888

# Time:  O(n)
# Space: O(n)

# mono stack

class Solution(object):
    def maxSubarrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stk = []
        for i in reversed(xrange(len(nums))):
            if not stk or nums[stk[-1]] > nums[i]:
                stk.append(i)
        result = 0
        for left in xrange(len(nums)):
            while stk and nums[stk[-1]] < nums[left]:
                result = max(result, stk.pop()-left+1)
        return result