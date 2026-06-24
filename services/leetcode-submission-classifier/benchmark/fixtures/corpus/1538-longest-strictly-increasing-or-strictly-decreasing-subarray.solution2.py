# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-strictly-increasing-or-strictly-decreasing-subarray
# source_path: LeetCode-Solutions-master/Python/longest-strictly-increasing-or-strictly-decreasing-subarray.py
# solution_class: Solution2
# submission_id: 1c3a31106dadad01ac2de18ab1f96730c67b2fa2
# seed: 837739859

# Time:  O(n)
# Space: O(1)

# array

class Solution2(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt1 = cnt2 = 1
        for i in xrange(1, len(nums)):
            cnt1 = cnt1+1 if nums[i-1] < nums[i] else 1
            cnt2 = cnt2+1 if nums[i-1] > nums[i] else 1
            result = max(result, cnt1, cnt2)
        return result