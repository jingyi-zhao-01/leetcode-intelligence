# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-number-ii
# source_path: LeetCode-Solutions-master/Python/single-number-ii.py
# solution_class: Solution4
# submission_id: b4a4d5e02299ff5a26fa3547889d76562529a661
# seed: 3705283418

# Time:  O(n)
# Space: O(1)

import collections

class Solution4(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2