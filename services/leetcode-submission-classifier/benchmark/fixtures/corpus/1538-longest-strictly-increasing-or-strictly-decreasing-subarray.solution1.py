# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-strictly-increasing-or-strictly-decreasing-subarray
# source_path: LeetCode-Solutions-master/Python/longest-strictly-increasing-or-strictly-decreasing-subarray.py
# solution_class: Solution
# submission_id: 346a39ece0e168dc0c36bd089a5e95f1c79769db
# seed: 373781769

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cnt = 1 if len(nums) == 1 or cmp(nums[0], nums[1]) == 0 else 2
        for i in xrange(2, len(nums)):
            cnt = 1 if cmp(nums[i-1], nums[i]) == 0 else cnt+1 if cmp(nums[i-2], nums[i-1]) == cmp(nums[i-1], nums[i]) else 2
            result = max(result, cnt)
        return result