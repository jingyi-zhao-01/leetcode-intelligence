# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-spread-stones-over-grid
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-spread-stones-over-grid.py
# solution_class: Solution
# submission_id: bdc516669a02a634cc085c5b3caaad291345c0f2
# seed: 1557140745

# Time:  O(max(x^2 * y)) = O(n^3), n = len(grid)*len(grid[0]), y = len(zero), x = n-y
# Space: O(max(x^2)) = O(n^2)

# weighted bipartite matching solution

class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Template translated from:
        # https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/WeightedMatching.h
        def hungarian(a):  # Time: O(n^2 * m), Space: O(n + m)
            if not a:
                return 0, []
            n, m = len(a)+1, len(a[0])+1
            u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
            for i in xrange(1, n):
                p[0] = i
                j0 = 0  # add "dummy" worker 0
                dist, pre = [float("inf")]*m, [-1]*m
                done = [False]*(m+1)
                while True:  # dijkstra
                    done[j0] = True
                    i0, j1, delta = p[j0], None, float("inf")
                    for j in xrange(1, m):
                        if done[j]:
                            continue
                        cur = a[i0-1][j-1]-u[i0]-v[j]
                        if cur < dist[j]:
                            dist[j], pre[j] = cur, j0
                        if dist[j] < delta:
                            delta, j1 = dist[j], j
                    for j in xrange(m):
                        if done[j]:
                            u[p[j]] += delta
                            v[j] -= delta
                        else:
                            dist[j] -= delta
                    j0 = j1
                    if not p[j0]:
                        break
                while j0:  # update alternating path
                    j1 = pre[j0]
                    p[j0], j0 = p[j1], j1
            for j in xrange(1, m):
                if p[j]:
                    ans[p[j]-1] = j-1
            return -v[0], ans  # min cost

        def dist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        src, dst = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]-1 >= 0:
                    src.extend([(i, j)]*(grid[i][j]-1))
                else:
                    dst.append((i, j))
        adj = [[dist(src[i], dst[j]) for j in xrange(len(dst))] for i in xrange(len(src))]
        return hungarian(adj)[0]