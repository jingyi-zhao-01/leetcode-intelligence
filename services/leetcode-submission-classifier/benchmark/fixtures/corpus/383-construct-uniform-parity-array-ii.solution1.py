# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-uniform-parity-array-ii
# source_path: LeetCode-Solutions-master/Python/construct-uniform-parity-array-ii.py
# solution_class: Solution
# submission_id: 1da042a4f11ef9c295525b1982fe9040c16df27d
# seed: 3515576323

# Time:  O(n)
# Space: O(1)

# constructive algorithms

class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        return min(nums1)%2 == 1 or all(x%2 == 0 for x in nums1)