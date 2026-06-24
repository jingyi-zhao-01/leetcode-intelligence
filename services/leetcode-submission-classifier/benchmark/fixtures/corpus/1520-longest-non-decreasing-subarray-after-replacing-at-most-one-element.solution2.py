# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-non-decreasing-subarray-after-replacing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-non-decreasing-subarray-after-replacing-at-most-one-element.py
# solution_class: Solution2
# submission_id: 53613f1f6297fdfa725367812b5ac35993330f2b
# seed: 4122174362

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution2(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [1]*len(nums)
        for i in xrange(len(nums)-1):
            if nums[i] <= nums[i+1]:
                left[i+1] = left[i]+1
        right = [1]*len(nums)
        for i in reversed(xrange(len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        result = min(max(left)+1, len(nums))
        for i in xrange(1, len(nums)-1):
            if nums[i-1] <= nums[i+1]:
                result = max(result, left[i-1]+1+right[i+1])
        return result