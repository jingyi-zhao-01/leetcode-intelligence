# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-unique-elements
# source_path: LeetCode-Solutions-master/Python/sum-of-unique-elements.py
# solution_class: Solution
# submission_id: b36707f0980d00a62395d25514319fe57ee53df8
# seed: 1313788317

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(x for x, c in collections.Counter(nums).iteritems() if c == 1)