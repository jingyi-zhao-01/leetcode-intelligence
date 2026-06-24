# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-division
# source_path: LeetCode-Solutions-master/Python/evaluate-division.py
# solution_class: Solution3
# submission_id: 6cd6bc3c93b62ca469f7adf6e15a15d733b94ad2
# seed: 663974826

# Time:  O((e + q) * α(n)) ~= O(e + q), using either one of "path compression" and "union by rank" results in amortized O(logn)
#                                     , using  both results in α(n) ~= O(1)
# Space: O(n)

import collections
import itertools


class UnionFind(object):
    def __init__(self):
        self.set = {}
        self.rank = collections.Counter()

    def find_set(self, x):
        xp, xr = self.set.setdefault(x, (x, 1.0))
        if x != xp:
            pp, pr = self.find_set(xp)  # path compression.
            self.set[x] = (pp, xr*pr)  # x/pp = xr*pr
        return self.set[x]

    def union_set(self, x, y, r):
        (xp, xr), (yp, yr) =  map(self.find_set, (x, y))
        if xp == yp:
            return False
        if self.rank[xp] < self.rank[yp]:  # union by rank
            # to make x/yp = r*yr and merge xp into yp
            # => since x/xp = xr, we can merge with xp/yp = r*yr/xr 
            self.set[xp] = (yp, r*yr/xr)
        elif self.rank[xp] > self.rank[yp]:
            # to make y/xp = 1/r*xr and merge xp into yp
            # => since y/yp = yr, we can merge with yp/xp = 1/r*xr/yr 
            self.set[yp] = (xp, 1.0/r*xr/yr)
        else:
            # to make y/xp = 1/r*xr and merge xp into yp
            # => since y/yp = yr, we can merge with yp/xp = 1/r*xr/yr 
            self.set[yp] = (xp, 1.0/r*xr/yr)
            self.rank[xp] += 1 
        return True

    def query_set(self, x, y):
        if x not in self.set or y not in self.set:
            return -1.0
        (xp, xr), (yp, yr) = map(self.find_set, (x, y))
        return xr/yr if xp == yp else -1.0


class UnionFindPathCompressionOnly(object):
    def __init__(self):
        self.set = {}

    def find_set(self, x):
        xp, xr = self.set.setdefault(x, (x, 1.0))
        if x != xp:
            pp, pr = self.find_set(xp)  # path compression.
            self.set[x] = (pp, xr*pr)  # x/pp = xr*pr
        return self.set[x]

    def union_set(self, x, y, r):
        (xp, xr), (yp, yr) =  map(self.find_set, (x, y))
        if xp == yp:
            return False
        # to make x/yp = r*yr and merge xp into yp
        # => since x/xp = xr, we can merge with xp/yp = r*yr/xr 
        self.set[xp] = (yp, r*yr/xr)
        return True

    def query_set(self, x, y):
        if x not in self.set or y not in self.set:
            return -1.0
        (xp, xr), (yp, yr) = map(self.find_set, (x, y))
        return xr/yr if xp == yp else -1.0

class Solution3(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = collections.defaultdict(dict)
        for (a, b), k in itertools.izip(equations, values):
            adj[a][a] = adj[b][b] = 1.0
            adj[a][b] = k
            adj[b][a] = 1.0/k
        for k in adj:
            for i in adj[k]:
                for j in adj[k]:
                    adj[i][j] = adj[i][k]*adj[k][j]
        return [adj[a].get(b, -1.0) for a, b in queries]