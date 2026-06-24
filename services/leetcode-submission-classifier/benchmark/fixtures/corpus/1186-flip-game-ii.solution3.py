# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-game-ii
# source_path: LeetCode-Solutions-master/Python/flip-game-ii.py
# solution_class: Solution3
# submission_id: 7d8faa6c873b5d5c2e27429a09fd9ff311e9824a
# seed: 2744571201

# Time:  O(n + c^2)
# Space: O(c)

import itertools
import re


# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/problems/flip-game-ii/discuss/73954/theory-matters-from-backtracking128ms-to-dp-0ms

class Solution3(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        is_win = False
        while not is_win and i < n:                                     # O(n) time
            if s[i] == '+':
                while not is_win and i < n and s[i+1] == '+':           # O(c) time
                     # t(n, c) = c * (t(n, c-1) + n) + n = ...
                     # = c! * t(n, 0) + n * c! * (c + 1) * (1/0! + 1/1! + ... 1/c!)
                     # = n * c! + n * c! * (c + 1) * O(e) = O(c * n * c!)
                    is_win = not self.canWin(s[:i] + '--' + s[i+2:])    # O(n) space
                    i += 1
            i += 1
        return is_win