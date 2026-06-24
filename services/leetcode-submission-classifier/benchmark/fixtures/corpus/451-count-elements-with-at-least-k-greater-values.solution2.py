# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-elements-with-at-least-k-greater-values
# source_path: LeetCode-Solutions-master/Python/count-elements-with-at-least-k-greater-values.py
# solution_class: Solution2
# submission_id: 0c38cf3bbc79c25174715e63b52fb883e2a982c8
# seed: 1983332735

# Time:  O(n)
# Space: O(1)

import random


# quick select

class Solution2(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not k:
            return len(nums)
        nums.sort()
        return next((i for i in reversed(xrange(len(nums)-k)) if nums[i] < nums[-k]), -1)+1