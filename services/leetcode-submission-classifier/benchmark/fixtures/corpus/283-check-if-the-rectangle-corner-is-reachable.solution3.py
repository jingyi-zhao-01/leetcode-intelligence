# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-the-rectangle-corner-is-reachable
# source_path: LeetCode-Solutions-master/Python/check-if-the-rectangle-corner-is-reachable.py
# solution_class: Solution3
# submission_id: eea9f153e8919743dbd26b801720aa8736ee33a1
# seed: 4132429125

# Time:  O(n^2)
# Space: O(n)

# iterative dfs

class Solution3(object):
    def canReachCorner(self, X, Y, circles):
        """
        :type X: int
        :type Y: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        def check(x1, y1, r1, x2, y2, r2):
            return (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2

        def iter_dfs(src, dst):
            lookup = [False]*len(adj)
            lookup[src] = True
            stk = [src]
            while stk:
                u = stk.pop()
                if u == dst:
                    return True
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    stk.append(v)
            return False

        adj = [[] for _ in xrange(len(circles)+2)]
        for u in xrange(len(circles)):
            x1, y1, r1 = circles[u]
            if x1-r1 <= 0 or y1+r1 >= Y:
                adj[u].append(len(circles))
                adj[len(circles)].append(u)
            if x1+r1 >= X or y1-r1 <= 0:
                adj[u].append(len(circles)+1)
                adj[len(circles)+1].append(u)
            for v in xrange(u):
                x2, y2, r2 = circles[v]
                if not check(x1, y1, r1, x2, y2, r2):
                    continue
                adj[u].append(v)
                adj[v].append(u)
        return not iter_dfs(len(circles), len(circles)+1)