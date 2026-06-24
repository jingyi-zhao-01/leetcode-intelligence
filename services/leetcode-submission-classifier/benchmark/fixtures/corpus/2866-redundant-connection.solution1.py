# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: redundant-connection
# source_path: LeetCode-Solutions-master/Python/redundant-connection.py
# solution_class: Solution
# submission_id: adef357e04cebf36b9b167ae605a4aa4641d5cfe
# seed: 389437898

# Time:  O(nlog*n) ~= O(n), n is the length of the positions
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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union_find = UnionFind(len(edges)+1)
        for edge in edges:
            if not union_find.union_set(*edge):
                return edge
        return []