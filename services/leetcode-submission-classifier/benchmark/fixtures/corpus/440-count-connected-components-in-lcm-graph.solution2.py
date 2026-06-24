# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-connected-components-in-lcm-graph
# source_path: LeetCode-Solutions-master/Python/count-connected-components-in-lcm-graph.py
# solution_class: Solution2
# submission_id: 6a7db5cc3f085b03feba7398a47d9faf392bd81b
# seed: 1318871221

# Time:  O(n + tlogt), t = threshold
# Space: O(t)

# union find, number theory
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

class Solution2(object):
    def countComponents(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        uf = UnionFind(threshold)
        lookup = [-1]*threshold
        for x in nums:
            if x-1 >= threshold:
                continue
            for i in xrange(x+x, threshold+1, x):
                uf.union_set(i-1, x-1)
        return sum(x-1 >= threshold or uf.find_set(x-1) == x-1 for x in nums)