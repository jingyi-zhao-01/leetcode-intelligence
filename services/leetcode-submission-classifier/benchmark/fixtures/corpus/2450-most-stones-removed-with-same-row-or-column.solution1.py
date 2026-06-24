# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-stones-removed-with-same-row-or-column
# source_path: LeetCode-Solutions-master/Python/most-stones-removed-with-same-row-or-column.py
# solution_class: Solution
# submission_id: 2bb83b13f5d17f1348d3bfa6d6badc2bf1c29f15
# seed: 714836294

# Time:  O(n)
# Space: O(n)

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        MAX_ROW = 10000
        union_find = UnionFind(2*MAX_ROW)
        for r, c in stones:
            union_find.union_set(r, c+MAX_ROW)
        return len(stones) - len({union_find.find_set(r) for r, _ in stones})