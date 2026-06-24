# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-good-pairs-i
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-good-pairs-i.py
# solution_class: Solution2
# submission_id: 99b2073bf98129bb2279bb237d07fa2333ca6c1f
# seed: 2057184546

# Time:  O(rlogr + n + m)
# Space: O(r)

import collections


# number theory, freq table

class Solution2(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        return sum(x%(k*y) == 0 for x in nums1 for y in nums2)