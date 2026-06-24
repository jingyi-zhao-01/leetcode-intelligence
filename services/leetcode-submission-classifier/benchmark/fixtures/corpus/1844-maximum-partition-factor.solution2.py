# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-partition-factor
# source_path: LeetCode-Solutions-master/Python/maximum-partition-factor.py
# solution_class: Solution2
# submission_id: 4024df019902bedca91d51e99f4cd1a55d4a612a
# seed: 3272306338

# Time:  O(n^2 * logn)
# Space: O(n^2)

# greedy, sort, union find with parity

class Solution2(object):
    def maxPartitionFactor(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
            def __init__(self, n):
                self.set = range(n)
                self.rank = [0]*n

            def find_set(self, x):
                stk = []
                while self.set[x] != x:  # path compression
                    stk.append(x)
                    x = self.set[x]
                while stk:
                    y = stk.pop()
                    self.set[y] = x
                return x

            def union_set(self, x, y):
                x, y = self.find_set(x), self.find_set(y)
                if x == y:
                    return False
                if self.rank[x] > self.rank[y]:  # union by rank
                    x, y = y, x
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                self.set[x] = self.set[y]
                return True

        def dist(u, v):
            return abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])

        sorted_dists = sorted((dist(u, v), u, v) for u in xrange(len(points)) for v in xrange(u+1, len(points)))
        uf = UnionFind(len(points))
        lookup = [-1]*len(points)
        for d, u, v in sorted_dists:
            if uf.find_set(u) == uf.find_set(v):
                return d
            if lookup[u] != -1:
                uf.union_set(lookup[u], v)
            else:
                lookup[u] = v
            if lookup[v] != -1:
                uf.union_set(lookup[v], u)
            else:
                lookup[v] = u
        return 0