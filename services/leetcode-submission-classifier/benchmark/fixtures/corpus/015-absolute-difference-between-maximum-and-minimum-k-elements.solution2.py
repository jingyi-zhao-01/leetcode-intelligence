# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: absolute-difference-between-maximum-and-minimum-k-elements
# source_path: LeetCode-Solutions-master/Python/absolute-difference-between-maximum-and-minimum-k-elements.py
# solution_class: Solution2
# submission_id: 08333e7b4d060f49950340eff63828137e6faa33
# seed: 3438672031

# Time:  O(n)
# Space: O(1)

import random


# quick select

class Solution2(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return abs(sum(nums[i] for i in xrange(k))-sum(nums[~i] for i in xrange(k)))