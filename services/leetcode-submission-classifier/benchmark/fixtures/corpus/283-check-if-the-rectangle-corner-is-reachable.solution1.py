# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-rectangle-corner-is-reachable
# source_path: LeetCode-Solutions-master/Python/check-if-the-rectangle-corner-is-reachable.py
# solution_class: Solution
# submission_id: 077c1c98138d008c97d8eea4c1c292ee7c08fb57
# seed: 2031467573

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution(object):
    def canReachCorner(self, X, Y, circles):
        """
        :type X: int
        :type Y: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        def iter_dfs():
            lookup = [False]*len(circles)
            stk = []
            dst = [False]*len(circles)
            for u in xrange(len(circles)):
                x, y, r = circles[u]
                if x-r <= 0 or y+r >= Y:
                    lookup[u] = True
                    stk.append(u)
                if x+r >= X or y-r <= 0:
                    dst[u] = True
            while stk:
                u = stk.pop()
                if dst[u]:
                    return True
                x1, y1, r1 = circles[u]
                for v in xrange(len(circles)):
                    x2, y2, r2 = circles[v]
                    if lookup[v] or not check(x1, y1, r1, x2, y2, r2):
                        continue
                    lookup[v] = True
                    stk.append(v)
            return False

        return not iter_dfs()