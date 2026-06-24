# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-good-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-good-pairs.py
# solution_class: Solution
# submission_id: 01fa853ceec5e301b5c0b88626dd05f396b86c37
# seed: 339782545

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(c*(c-1)//2 for c in collections.Counter(nums).itervalues())