# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-area-rectangle
# source_path: LeetCode-Solutions-master/Python/minimum-area-rectangle.py
# solution_class: Solution
# submission_id: 132d20131c4e80557de777e74a64433e1731afd3
# seed: 1271103727

# Time:  O(n^1.5) on average
#        O(n^2) on worst
# Space: O(n)

import collections

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lookup = {}
        result = float("inf")
        for x in sorted(p):
            p[x].sort()
            for j in xrange(len(p[x])):
                for i in xrange(j):
                    y1, y2 = p[x][i], p[x][j]
                    if (y1, y2) in lookup:
                        result = min(result, (x-lookup[y1, y2]) * (y2-y1))
                    lookup[y1, y2] = x
        return result if result != float("inf") else 0