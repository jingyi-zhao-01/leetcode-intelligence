# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: xor-after-range-multiplication-queries-i
# source_path: LeetCode-Solutions-master/Python/xor-after-range-multiplication-queries-i.py
# solution_class: Solution2
# submission_id: c5270a90d81a271e1d70e58bd62686762b2fdfa7
# seed: 3651112398

# Time:  O(qlogm + (q + n) * sqrt(n))
# Space: O(n * sqrt(n))

import collections


# sqrt decomposition, difference array, fast exponentiation

class Solution2(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7

        for l, r, k, v in queries:
            for i in xrange(l, r+1, k):
                nums[i] = (nums[i]*v)%MOD
        return reduce(lambda accu, x: accu^x, nums, 0)