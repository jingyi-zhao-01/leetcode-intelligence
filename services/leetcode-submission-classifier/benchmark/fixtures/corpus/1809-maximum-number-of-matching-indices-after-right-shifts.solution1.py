# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-matching-indices-after-right-shifts
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-matching-indices-after-right-shifts.py
# solution_class: Solution
# submission_id: 6937e96c69e2a65f62fc0a86c45c3ecf2bfba5e9
# seed: 2137216741

# Time:  O(n^2)
# Space: O(1)

# brute force

class Solution(object):
    def maximumMatchingIndices(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return max(sum(nums2[j] == nums1[(i+j)%len(nums1)] for j in xrange(len(nums2))) for i in xrange(len(nums1)))