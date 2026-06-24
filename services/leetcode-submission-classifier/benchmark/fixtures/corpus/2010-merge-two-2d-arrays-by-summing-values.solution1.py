# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: merge-two-2d-arrays-by-summing-values
# source_path: LeetCode-Solutions-master/Python/merge-two-2d-arrays-by-summing-values.py
# solution_class: Solution
# submission_id: 79e30b5c8aae0dad2686fed53a97ad731f77b9fc
# seed: 1976604167

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if j == len(nums2) or (i < len(nums1) and nums1[i][0] < nums2[j][0]):
                if result and result[-1][0] == nums1[i][0]:
                    result[-1][1] += nums1[i][1]
                else:
                    result.append(nums1[i])
                i += 1
            else:
                if result and result[-1][0] == nums2[j][0]:
                    result[-1][1] += nums2[j][1]
                else:
                    result.append(nums2[j])
                j += 1
        return result