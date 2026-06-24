# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-non-decreasing-subarray-after-replacing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-non-decreasing-subarray-after-replacing-at-most-one-element.py
# solution_class: Solution
# submission_id: 5e0e2ac3ebc4da334cc58d71cd9d9aab1f881428
# seed: 3583543090

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [1]*len(nums)
        for i in reversed(xrange(len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        result = min(max(right)+1, len(nums))
        left = 1
        for i in xrange(1, len(nums)-1):
            if nums[i-1] <= nums[i+1]:
                result = max(result, left+1+right[i+1])
            if nums[i-1] <= nums[i]:
                left += 1
            else:
                left = 1
        return result