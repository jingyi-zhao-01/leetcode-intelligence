# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-count-of-positive-integer-and-negative-integer
# source_path: LeetCode-Solutions-master/Python/maximum-count-of-positive-integer-and-negative-integer.py
# solution_class: Solution
# submission_id: 26e189ed05c2ec2c2ec5eabaea65a0115364b29c
# seed: 2515222689

# Time:  O(logn)
# Space: O(1)

import bisect


# binary search

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(bisect.bisect_left(nums, 0)-0, len(nums)-bisect.bisect_left(nums, 1))