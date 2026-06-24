# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-for-contradictions-in-equations
# source_path: LeetCode-Solutions-master/Python/check-for-contradictions-in-equations.py
# solution_class: Solution
# submission_id: 5ec59abfdb83ba1c06c5d48cae26f9e6d1397b7e
# seed: 2128980895

# Time:  O(e + q)
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


# Time:  O(e + q)
# Space: O(n)
import itertools


# union find

class Solution(object):
    def checkContradictions(self, equations, values):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :rtype: bool
        """
        EPS = 1e-5
        uf = UnionFind()
        return any(not uf.union_set(a, b, k) and abs(uf.query_set(a, b)-k) >= EPS for (a, b), k in itertools.izip(equations, values))