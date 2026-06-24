# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: equal-sum-arrays-with-minimum-number-of-operations
# source_path: LeetCode-Solutions-master/Python/equal-sum-arrays-with-minimum-number-of-operations.py
# solution_class: Solution
# submission_id: 7dfdd49304084e3e16d50711f8df67a6dea05333
# seed: 3338800071

# Time:  O(m + n)
# Space: O(1)

import collections

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1)*6 < len(nums2) or len(nums1) > len(nums2)*6:
            return -1
        diff = sum(nums2)-sum(nums1)
        if diff < 0:
            nums1, nums2 = nums2, nums1
            diff = -diff
        count = collections.Counter(6-num for num in nums1)
        count += collections.Counter(num-1 for num in nums2)
        result = 0
        for i in reversed(xrange(1, 6)):
            if not count[i]:
                continue
            cnt = min(count[i], (diff+i-1)//i)
            result += cnt
            diff -= i*cnt
            if diff <= 0:
                break
        return result