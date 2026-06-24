# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-maximum-component-cost
# source_path: LeetCode-Solutions-master/Python/minimize-maximum-component-cost.py
# solution_class: Solution
# submission_id: 5f21253485ac97be95ebf5f5a0c06101d9e9a0b1
# seed: 2565671221

# Time:  O(n + eloge)
# Space: O(n)

# backward simulation, union find, sort
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
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        return True

class Solution(object):
    def minCost(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        edges.sort(key=lambda x: x[2])
        cnt = 0
        uf = UnionFind(n)
        for u, v, w in edges:
            if not uf.union_set(u, v):
                continue
            cnt += 1
            if cnt == n-k:
                return w
        return 0