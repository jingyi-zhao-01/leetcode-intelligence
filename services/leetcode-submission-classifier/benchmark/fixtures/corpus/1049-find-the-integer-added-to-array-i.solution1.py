# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-integer-added-to-array-i
# source_path: LeetCode-Solutions-master/Python/find-the-integer-added-to-array-i.py
# solution_class: Solution
# submission_id: 5d07f78b9c01f5edfc95beea1d1b3df4a116bfeb
# seed: 2990063589

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return max(nums2)-max(nums1)