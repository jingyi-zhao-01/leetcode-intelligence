# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-missing-non-negative-integer-after-operations
# source_path: LeetCode-Solutions-master/Python/smallest-missing-non-negative-integer-after-operations.py
# solution_class: Solution
# submission_id: e75a7f6d33b30308a84e56d4c100c28a65b5447b
# seed: 955697098

# Time:  O(n)
# Space: O(k), k = value

import collections


# freq table

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        cnt = collections.Counter(x%value for x in nums)
        mn = min((cnt[i], i) for i in xrange(value))[1]
        return value*cnt[mn]+mn