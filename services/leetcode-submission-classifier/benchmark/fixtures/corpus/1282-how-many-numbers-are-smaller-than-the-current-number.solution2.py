# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: how-many-numbers-are-smaller-than-the-current-number
# source_path: LeetCode-Solutions-master/Python/how-many-numbers-are-smaller-than-the-current-number.py
# solution_class: Solution2
# submission_id: 81ae768531e65aa070b4156d1ec06d0b6c923f40
# seed: 159003425

# Time:  O(n + m), m is the max number of nums
# Space: O(m)

import collections

class Solution2(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        return [bisect.bisect_left(sorted_nums, i) for i in nums]