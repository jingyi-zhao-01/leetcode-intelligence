# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-common-elements-between-two-arrays
# source_path: LeetCode-Solutions-master/Python/find-common-elements-between-two-arrays.py
# solution_class: Solution
# submission_id: c6271341ae96e0afd5acb8864a98e2515e6dc75e
# seed: 18082862

# Time:  O(n + m)
# Space: O(n + m)

# hash table

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lookup1, lookup2 = set(nums1), set(nums2)
        return [sum(x in lookup2 for x in nums1), sum(x in lookup1 for x in nums2)]