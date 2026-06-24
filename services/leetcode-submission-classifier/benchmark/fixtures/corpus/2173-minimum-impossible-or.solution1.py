# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-impossible-or
# source_path: LeetCode-Solutions-master/Python/minimum-impossible-or.py
# solution_class: Solution
# submission_id: 3e6e7dfc13dd511db5ecb6b0b6c8f8ee94fee22d
# seed: 160864335

# Time:  O(logr)
# Space: O(1)

# hash table, bit manipulations

class Solution(object):
    def minImpossibleOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = set(nums)
        return next(1<<i for i in xrange(31) if 1<<i not in lookup)