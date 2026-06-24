# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-division
# source_path: LeetCode-Solutions-master/Python/evaluate-division.py
# solution_class: Solution2
# submission_id: a73cb0c4ab7377aa272372f4ad9640459403d6cd
# seed: 334241199

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

class Solution2(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        adj = collections.defaultdict(dict)
        for (a, b), k in itertools.izip(equations, values):
            adj[a][b] = k
            adj[b][a] = 1.0/k

        def bfs(adj, a, b, lookup):
            if a not in adj or b not in adj:
                return -1.0
            if (a, b) in lookup:
                return lookup[a, b]
            visited = {a}
            q = collections.deque([(a, 1.0)])
            while q:
                u, val = q.popleft()
                if u == b:
                    lookup[a, b] = val
                    return val
                for v, k in adj[u].iteritems():
                    if v in visited:
                        continue                    
                    visited.add(v)
                    q.append((v, val*k))
            lookup[a, b] = -1.0
            return -1.0

        lookup = {}
        return [bfs(adj, a, b, lookup) for a, b in queries]