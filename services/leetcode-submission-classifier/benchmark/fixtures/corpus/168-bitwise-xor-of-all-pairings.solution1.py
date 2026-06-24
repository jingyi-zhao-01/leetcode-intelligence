# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-xor-of-all-pairings
# source_path: LeetCode-Solutions-master/Python/bitwise-xor-of-all-pairings.py
# solution_class: Solution
# submission_id: 4854bc77b1f6313312e6d4c3bf3c3949c5552fb2
# seed: 1780651071

# Time:  O(n)
# Space: O(1)

import operator


# bit manipulation

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return (reduce(operator.xor, nums1) if len(nums2)%2 else 0) ^ \
               (reduce(operator.xor, nums2) if len(nums1)%2 else 0)