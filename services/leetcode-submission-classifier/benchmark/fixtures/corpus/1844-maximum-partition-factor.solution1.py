# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-partition-factor
# source_path: LeetCode-Solutions-master/Python/maximum-partition-factor.py
# solution_class: Solution
# submission_id: 394c61b057e4705e45441514c64480ebff2c1c5e
# seed: 2235011824

# Time:  O(n^2 * logn)
# Space: O(n^2)

# greedy, sort, union find with parity

class Solution(object):
    def maxPartitionFactor(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
            def __init__(self, n):
                self.set = range(n)
                self.rank = [0]*n
                self.parity = [0]*n  # added

            def find_set(self, x):
                stk = []
                while self.set[x] != x:  # path compression
                    stk.append(x)
                    x = self.set[x]
                while stk:
                    y = stk.pop()
                    self.parity[y] ^= self.parity[self.set[y]]  # added
                    self.set[y] = x
                return x

            def union_set(self, x, y):
                ox, oy = x, y  # added
                x, y = self.find_set(x), self.find_set(y)
                if x == y:
                    return self.parity[ox] != self.parity[oy]  # modified
                if self.rank[x] > self.rank[y]:  # union by rank
                    x, y = y, x
                    ox, oy = oy, ox  # added
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                self.set[x] = self.set[y]
                self.parity[x] = self.parity[ox]^self.parity[oy]^1  # added
                return True

        def dist(u, v):
            return abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])

        sorted_dists = sorted((dist(u, v), u, v) for u in xrange(len(points)) for v in xrange(u+1, len(points)))
        uf = UnionFind(len(points))
        return next((d for d, u, v in sorted_dists if not uf.union_set(u, v)), 0)