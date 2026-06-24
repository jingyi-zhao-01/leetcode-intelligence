# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-special-subsequences
# source_path: LeetCode-Solutions-master/Python/count-special-subsequences.py
# solution_class: Solution
# submission_id: a362464ffac9d29b01719e9ae042f9faf448d226
# seed: 388482481

# Time:  O(n^2)
# Space: O(n^2)

import collections


# freq table

class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        result = 0
        for r in xrange(4, len(nums)-2):
            q = r-2
            for p in xrange((q-2)+1):
                cnt[float(nums[p])/nums[q]] += 1
            for s in xrange(r+2, len(nums)):
                result += cnt[float(nums[s])/nums[r]]
        return result