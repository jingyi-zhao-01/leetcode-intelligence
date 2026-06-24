# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: graph-connectivity-with-threshold
# source_path: LeetCode-Solutions-master/Python/graph-connectivity-with-threshold.py
# solution_class: Solution
# submission_id: b47de26a412c6b5332b5738d039648a2b967291c
# seed: 3146625164

# Time:  O((nlogn + q) * α(n)) ~= O(nlogn + q)
# Space: O(n)

class UnionFind(object):  # Time: O(n * α(n)), Space: O(n)
    def __init__(self, n):
        self.set = range(n)
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:  # union by rank
            self.set[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1
        return True

class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        union_find = UnionFind(n)
        for i in xrange(threshold+1, n+1):
            # https://stackoverflow.com/questions/25905118/finding-big-o-of-the-harmonic-series
            # sum of harmonic series is O(logn)
            for j in xrange(2*i, n+1, i):  # step by i
                union_find.union_set(i-1, j-1)
        return [union_find.find_set(q[0]-1) == union_find.find_set(q[1]-1) for q in queries]