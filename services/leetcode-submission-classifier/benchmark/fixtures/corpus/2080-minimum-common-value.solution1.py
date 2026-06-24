# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-common-value
# source_path: LeetCode-Solutions-master/Python/minimum-common-value.py
# solution_class: Solution
# submission_id: 9bb2301d336d051bd9bfcfc5df1eb2bd749624cb
# seed: 2972313549

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1