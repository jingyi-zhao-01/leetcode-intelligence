# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-game-ii
# source_path: LeetCode-Solutions-master/Python/flip-game-ii.py
# solution_class: Solution
# submission_id: 67991651166c7fc2d9fabc19a2c7ff2a7ab8072b
# seed: 2788103651

# Time:  O(n + c^2)
# Space: O(c)

import itertools
import re


# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/problems/flip-game-ii/discuss/73954/theory-matters-from-backtracking128ms-to-dp-0ms

class Solution(object):
    def canWin(self, s):
        g, g_final = [0], 0
        for p in itertools.imap(len, re.split('-+', s)):
            while len(g) <= p:
                # Theorem 2: g[game] = g[subgame1]^g[subgame2]^g[subgame3]...
                # and find first missing number.
                g += min(set(xrange(p)) - {x^y for x, y in itertools.izip(g[:len(g)/2], g[-2:-len(g)/2-2:-1])}),
            g_final ^= g[p]
        return g_final > 0  # Theorem 1: First player must win iff g(current_state) != 0