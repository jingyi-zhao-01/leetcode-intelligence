# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-array-state-after-k-multiplication-operations-i
# source_path: LeetCode-Solutions-master/Python/final-array-state-after-k-multiplication-operations-i.py
# solution_class: Solution5
# submission_id: e0e5816c521e848aafeae38b853f19bab558ebb4
# seed: 2936742139

# Time:  O(n + (n + logr) + nlog(logr) + nlogn) = O(nlogn), assumed log(x) takes O(1) time
# Space: O(n)

import math


# sort, two pointers, sliding window, fast exponentiation

class Solution5(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        if multiplier == 1:
            return nums
        for _ in xrange(k):
            i = min(xrange(len(nums)), key=lambda i: nums[i])
            nums[i] *= multiplier
        return nums