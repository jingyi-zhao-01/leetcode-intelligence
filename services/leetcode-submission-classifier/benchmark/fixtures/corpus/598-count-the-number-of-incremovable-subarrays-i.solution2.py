# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-incremovable-subarrays-i
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-incremovable-subarrays-i.py
# solution_class: Solution2
# submission_id: f90963f2a0a39c361fa8591530c03a687bb63c87
# seed: 1892044862

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution2(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((left == 0 or right == len(nums)-1 or nums[left-1] < nums[right+1]) and
                   all(nums[i] < nums[i+1] for i in xrange(left-1)) and
                   all(nums[i] < nums[i+1] for i in xrange(right+1, len(nums)-1))
                   for left in xrange(len(nums)) for right in xrange(left, len(nums)))