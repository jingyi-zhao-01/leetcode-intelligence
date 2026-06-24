# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-maximize-last-elements-in-arrays
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-maximize-last-elements-in-arrays.py
# solution_class: Solution
# submission_id: fcef5a86c6c983b5104078907cda3b08faa18be9
# seed: 2559474182

# Time:  O(n)
# Space: O(1)

import itertools


# simulation

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        cnt = [0]*2
        for x, y in itertools.izip(nums1, nums2):
            if not (min(x, y) <= min(nums1[-1], nums2[-1]) and max(x, y) <= max(nums1[-1], nums2[-1])):
                return -1
            if not (x <= nums1[-1] and y <= nums2[-1]):
                cnt[0] += 1
            if not (x <= nums2[-1] and y <= nums1[-1]):
                cnt[1] += 1
        return min(cnt)