# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-integer-added-to-array-ii
# source_path: LeetCode-Solutions-master/Python/find-the-integer-added-to-array-ii.py
# solution_class: Solution3
# submission_id: a0e1725439c9eaa6de730a7ebaedfe91d213bdd3
# seed: 1690566062

# Time:  O(n)
# Space: O(n)

import heapq
import collections


# partial sort, freq table

class Solution3(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        for i in xrange(3):
            d = nums2[-1]-nums1[~i]
            cnt = 0
            for j in xrange(len(nums2)):
                while j+cnt < len(nums1) and nums1[j+cnt]+d != nums2[j]:
                    cnt += 1
            if cnt <= 2:
                return d
        return -1