# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-difference-of-two-arrays
# source_path: LeetCode-Solutions-master/Python/find-the-difference-of-two-arrays.py
# solution_class: Solution
# submission_id: 6b7210d4254f9208232465c10aeda25668ef4e5a
# seed: 3548604396

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        lookup = [set(nums1), set(nums2)]
        return [list(lookup[0]-lookup[1]), list(lookup[1]-lookup[0])]