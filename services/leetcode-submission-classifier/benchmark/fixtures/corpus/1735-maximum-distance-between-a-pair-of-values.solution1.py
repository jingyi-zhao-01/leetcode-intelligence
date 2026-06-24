# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-distance-between-a-pair-of-values
# source_path: LeetCode-Solutions-master/Python/maximum-distance-between-a-pair-of-values.py
# solution_class: Solution
# submission_id: 3e62a7166d139ecc9a73587ccd0f7aecb7afbdc1
# seed: 2633486697

# Time:  O(n + m)
# Space: O(1)

class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                result = max(result, j-i)
                j += 1
        return result