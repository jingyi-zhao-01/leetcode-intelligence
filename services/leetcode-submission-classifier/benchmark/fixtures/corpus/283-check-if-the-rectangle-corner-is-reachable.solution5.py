# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-rectangle-corner-is-reachable
# source_path: LeetCode-Solutions-master/Python/check-if-the-rectangle-corner-is-reachable.py
# solution_class: Solution5
# submission_id: 84e4a65fc3893617c3d8ba9b7e643bac41d70b3c
# seed: 1586128754

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution5(object):
    def canReachCorner(self, X, Y, circles):
        """
        :type X: int
        :type Y: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        uf = UnionFind(len(circles)+2)
        for u in xrange(len(circles)):
            x1, y1, r1 = circles[u]
            if x1-r1 <= 0 or y1+r1 >= Y:
                uf.union_set(u, len(circles))
            if x1+r1 >= X or y1-r1 <= 0:
                uf.union_set(u, len(circles)+1)
            for v in xrange(u):
                x2, y2, r2 = circles[v]
                if not check(x1, y1, r1, x2, y2, r2):
                    continue
                uf.union_set(u, v)
        return uf.find_set(len(circles)) != uf.find_set(len(circles)+1)