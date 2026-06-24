# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-sum-difference
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-sum-difference.py
# solution_class: Solution
# submission_id: 930cb8d6f5ced1ba1ffc215ba6f3a6efa14264cd
# seed: 3221922745

# Time:  O(nlogn)
# Space: O(n)

import bisect

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        sorted_nums1 = sorted(nums1)
        result = max_change = 0
        for i in xrange(len(nums2)):
            diff = abs(nums1[i]-nums2[i])
            result = (result+diff)%MOD
            if diff < max_change:
                continue
            j = bisect.bisect_left(sorted_nums1, nums2[i])
            if j != len(sorted_nums1):
                max_change = max(max_change, diff-abs(sorted_nums1[j]-nums2[i]))
            if j != 0:
                max_change = max(max_change, diff-abs(sorted_nums1[j-1]-nums2[i]))
        return (result-max_change)%MOD