# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-missing-non-negative-integer-after-operations
# source_path: LeetCode-Solutions-master/Python/smallest-missing-non-negative-integer-after-operations.py
# solution_class: Solution2
# submission_id: fcb2b7e282e92ed1b190d54c519f0da75f04027f
# seed: 4200838959

# Time:  O(n)
# Space: O(k), k = value

import collections


# freq table

class Solution2(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        cnt = collections.Counter(x%value for x in nums)
        for i in xrange(len(nums)+1):
            if not cnt[i%value]:
                return i
            cnt[i%value] -= 1