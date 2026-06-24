# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-game-ii
# source_path: LeetCode-Solutions-master/Python/flip-game-ii.py
# solution_class: Solution2
# submission_id: f3cb81ee8e744669eb72d93e993246c83dba717b
# seed: 3829422159

# Time:  O(n + c^2)
# Space: O(c)

import itertools
import re


# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/problems/flip-game-ii/discuss/73954/theory-matters-from-backtracking128ms-to-dp-0ms

class Solution2(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}

        def canWinHelper(consecutives):                                         # O(2^c) time
            consecutives = tuple(sorted(c for c in consecutives if c >= 2))     # O(clogc) time
            if consecutives not in lookup:
                lookup[consecutives] = any(not canWinHelper(consecutives[:i] + (j, c-2-j) + consecutives[i+1:])  # O(c) time
                                           for i, c in enumerate(consecutives)  # O(c) time
                                           for j in xrange(c - 1))              # O(c) time
            return lookup[consecutives]                                         # O(c) time

        # re.findall: O(n) time, canWinHelper: O(c) in depth
        return canWinHelper(map(len, re.findall(r'\+\++', s)))