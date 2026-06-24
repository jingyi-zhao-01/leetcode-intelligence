# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-two-arrays-equal-by-reversing-sub-arrays
# source_path: LeetCode-Solutions-master/Python/make-two-arrays-equal-by-reversing-sub-arrays.py
# solution_class: Solution
# submission_id: 731d0985e900872b3a25eba94ed5a98a5f3fc9e4
# seed: 3820741413

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return collections.Counter(target) == collections.Counter(arr)