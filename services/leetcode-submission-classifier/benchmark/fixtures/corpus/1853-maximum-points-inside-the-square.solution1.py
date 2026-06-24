# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-points-inside-the-square
# source_path: LeetCode-Solutions-master/Python/maximum-points-inside-the-square.py
# solution_class: Solution
# submission_id: 1a31407c3eae6971fdba92811c5c6f1f8ec0a710
# seed: 1214961862

# Time:  O(n + 26)
# Space: O(26)

import itertools


# hash table

class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        """
        :type points: List[List[int]]
        :type s: str
        :rtype: int
        """
        INF = float("inf")
        lookup = [INF for _ in xrange(26)]
        d = INF
        for c, (x, y) in itertools.izip(s, points):
            k = ord(c)-ord('a')
            mn2 = max(abs(x), abs(y))
            if mn2 < lookup[k]:
                mn2, lookup[k] = lookup[k], mn2
            d = min(d, mn2)
        return sum(mn1 < d for mn1 in lookup)