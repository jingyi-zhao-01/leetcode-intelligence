# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-array-length-after-pair-removals
# source_path: LeetCode-Solutions-master/Python/minimum-array-length-after-pair-removals.py
# solution_class: Solution
# submission_id: 31dd2d7faa36ed352f856c075c07dac50cc5f8a2
# seed: 2467507425

# Time:  O(n)
# Space: O(n)

import collections


# freq table, constructive algorithms

class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = max(collections.Counter(nums).itervalues())
        return mx-(len(nums)-mx) if mx > (len(nums)-mx) else len(nums)%2