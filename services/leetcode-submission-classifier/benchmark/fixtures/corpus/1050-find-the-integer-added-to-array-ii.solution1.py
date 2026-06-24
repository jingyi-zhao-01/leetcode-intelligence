# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-integer-added-to-array-ii
# source_path: LeetCode-Solutions-master/Python/find-the-integer-added-to-array-ii.py
# solution_class: Solution
# submission_id: f66fbc670924bd3a3b6bcb3e515637937ed58485
# seed: 205840359

# Time:  O(n)
# Space: O(n)

import heapq
import collections


# partial sort, freq table

class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        def check(cnt2, cnt1):
            # return cnt2 <= cnt1  # for python3
            return all(cnt1.get(k, 0)-v >= 0 for k, v in cnt2.iteritems())  # for python2
            
        mx = max(nums2)
        cnt2 = collections.Counter(nums2)
        return next(d for d in [mx-x for x in heapq.nlargest(3, nums1)] if check(cnt2, collections.Counter(x+d for x in nums1)))