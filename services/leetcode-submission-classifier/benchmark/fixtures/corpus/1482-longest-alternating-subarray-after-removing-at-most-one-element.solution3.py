# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-alternating-subarray-after-removing-at-most-one-element
# source_path: LeetCode-Solutions-master/Python/longest-alternating-subarray-after-removing-at-most-one-element.py
# solution_class: Solution3
# submission_id: 2149b40fa0cdcc4190055f6b015c6ed636120f9a
# seed: 2563024168

# Time:  O(n)
# Space: O(1)

# dp

class Solution3(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [1]*len(nums)
        for i in xrange(1, len(nums)):
            diff = cmp(nums[i-1], nums[i])
            if not diff:
                continue
            left[i] = left[i-1]+1 if i-2 >= 0 and cmp(nums[i-2], nums[i-1]) == -diff else 2
        right = [1]*len(nums)
        for i in reversed(xrange(len(nums)-1)):
            diff = cmp(nums[i], nums[i+1])
            if not diff:
                continue
            right[i] = right[i+1]+1 if i+2 < len(nums) and cmp(nums[i+1], nums[i+2]) == -diff else 2
        result = max(left)
        for i in xrange(1, len(nums)-1):
            diff = cmp(nums[i-1], nums[i+1])
            if not diff:
                continue
            l = (left[i-1] if i-2 >= 0 and cmp(nums[i-2], nums[i-1]) == -diff else 1)
            r = (right[i+1] if i+2 < len(nums) and cmp(nums[i+1], nums[i+2]) == -diff else 1)
            result = max(result, l+r)
        return result