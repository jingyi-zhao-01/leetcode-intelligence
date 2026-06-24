# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-number-is-majority-element-in-a-sorted-array
# source_path: LeetCode-Solutions-master/Python/check-if-a-number-is-majority-element-in-a-sorted-array.py
# solution_class: Solution
# submission_id: 1ce75c8148e10d52f992f5ca817772b84175d4b2
# seed: 2123185871

# Time:  O(logn)
# Space: O(1)

import bisect

class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) % 2:
            if nums[len(nums)//2] != target:
                return False
        else:
            if not (nums[len(nums)//2-1] == nums[len(nums)//2] == target):
                return False

        left = bisect.bisect_left(nums, target)
        right= bisect.bisect_right(nums, target)
        return (right-left)*2 > len(nums)