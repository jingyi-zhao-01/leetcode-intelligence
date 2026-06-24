# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-two-arrays-ii
# source_path: LeetCode-Solutions-master/Python/intersection-of-two-arrays-ii.py
# solution_class: Solution
# submission_id: 9f6664f8cf8393caeaaaf7e9869360161c445f41
# seed: 4011859316

# If the given array is not sorted and the memory is unlimited:
#   - Time:  O(m + n)
#   - Space: O(min(m, n))
# elif the given array is already sorted:
#   if m << n or m >> n:
#     - Time:  O(min(m, n) * log(max(m, n)))
#     - Space: O(1)
#   else:
#     - Time:  O(m + n)
#     - Soace: O(1)
# else: (the given array is not sorted and the memory is limited)
#     - Time:  O(max(m, n) * log(max(m, n)))
#     - Space: O(1)

import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()  # O(max(m, n) * log(max(m, n)))

        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1

        return res