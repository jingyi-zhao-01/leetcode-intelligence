# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-subarrays-with-exactly-one-peak
# source_path: LeetCode-Solutions-master/Python/valid-subarrays-with-exactly-one-peak.py
# solution_class: Solution
# submission_id: cba2d5022fd675baebadf4b1f8f634567adcef3d
# seed: 2389435130

# Time:  O(n)
# Space: O(1)

# combinatorics, two pointers

class Solution(object):
    def validSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, left, l = 0, -1, 0
        for right in xrange(1, len(nums)-1):
            if not nums[right-1] < nums[right] > nums[right+1]:
                continue
            r = min(right-left, k+1)
            result += l*r
            left, l = right, r
        result += l*min(len(nums)-left, k+1)
        return result