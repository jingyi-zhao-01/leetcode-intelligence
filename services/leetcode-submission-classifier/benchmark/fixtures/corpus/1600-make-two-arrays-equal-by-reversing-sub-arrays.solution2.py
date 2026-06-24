# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-two-arrays-equal-by-reversing-sub-arrays
# source_path: LeetCode-Solutions-master/Python/make-two-arrays-equal-by-reversing-sub-arrays.py
# solution_class: Solution2
# submission_id: d066d5f3cfb4d44612babfb8aa8ddf7d91b385a8
# seed: 3563659963

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort(), arr.sort()
        return target == arr