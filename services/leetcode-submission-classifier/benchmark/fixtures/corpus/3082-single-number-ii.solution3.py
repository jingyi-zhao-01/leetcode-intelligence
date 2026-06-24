# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-ii
# source_path: LeetCode-Solutions-master/Python/single-number-ii.py
# solution_class: Solution3
# submission_id: 0d4019ab0e6bed84bcae9ba6467235b64b1efc30
# seed: 1255303986

# Time:  O(n)
# Space: O(1)

import collections

class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (collections.Counter(list(set(nums)) * 3) - collections.Counter(nums)).keys()[0]