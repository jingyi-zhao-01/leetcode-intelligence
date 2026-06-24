# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-total-cost-to-make-arrays-unequal
# source_path: LeetCode-Solutions-master/Python/minimum-total-cost-to-make-arrays-unequal.py
# solution_class: Solution
# submission_id: 8324b259668b6f8e2734167c1c07f7b4390e8dbc
# seed: 3824290205

# Time:  O(n)
# Space: O(n)

import collections
import itertools


# greedy

class Solution(object):
    def minimumTotalCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cnt = collections.Counter()
        result = 0
        for i, (x, y) in enumerate(itertools.izip(nums1, nums2)):
            if x != y:
                continue
            cnt[x] += 1
            result += i
        if not cnt:
            return 0
        majority = max(cnt.iterkeys(), key=lambda x: cnt[x])
        remain = cnt[majority]-(sum(cnt.itervalues())-cnt[majority])
        if remain <= 0:
            return result
        for i, (x, y) in enumerate(itertools.izip(nums1, nums2)):
            if x == y or majority in (x, y):
                continue
            result += i
            remain -= 1
            if not remain:
                return result
        return -1