# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-ways-to-place-houses
# source_path: LeetCode-Solutions-master/Python/count-number-of-ways-to-place-houses.py
# solution_class: Solution2
# submission_id: 5c129633d8bd5a73da05e4b8bc64c3c082a36b73
# seed: 834425378

# Time:  O(logn)
# Space: O(1)

import itertools


# matrix exponentiation

class Solution2(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        prev, curr = 1, 2
        for _ in xrange(n-1):
            prev, curr = curr, (prev+curr)%MOD
        return pow(curr, 2, MOD)