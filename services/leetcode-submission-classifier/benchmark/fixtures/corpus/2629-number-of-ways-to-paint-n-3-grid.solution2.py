# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-paint-n-3-grid
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-paint-n-3-grid.py
# solution_class: Solution2
# submission_id: 5a3dbafc59c0ec3a88f4e218fb8d301f108e7c39
# seed: 1557643782

# Time:  O(logn)
# Space: O(1)

import itertools

class Solution2(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        aba, abc = 6, 6
        for _ in xrange(n-1):
            aba, abc = (3*aba%MOD + 2*abc%MOD)%MOD, \
                       (2*abc%MOD + 2*aba%MOD)%MOD
        return (aba+abc)%MOD