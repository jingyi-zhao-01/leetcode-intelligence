# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-earliest-moment-when-everyone-become-friends
# source_path: LeetCode-Solutions-master/Python/the-earliest-moment-when-everyone-become-friends.py
# solution_class: Solution
# submission_id: 5205438df06a912bb9e59b5eab5b9c5c1fde7b76
# seed: 2519566730

# Time:  O(nlogn)
# Space: O(n)

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        self.count -= 1
        return True

class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort()
        union_find = UnionFind(N)
        for t, a, b in logs:
            union_find.union_set(a, b)
            if union_find.count == 1:
                return t
        return -1