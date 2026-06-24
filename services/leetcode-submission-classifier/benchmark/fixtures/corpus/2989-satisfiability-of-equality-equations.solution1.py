# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: satisfiability-of-equality-equations
# source_path: LeetCode-Solutions-master/Python/satisfiability-of-equality-equations.py
# solution_class: Solution
# submission_id: 2d2dc79ec832b45cb65ce41ee01254b4c4ad2f04
# seed: 927680935

# Time:  O(n)
# Space: O(1)

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
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        union_find = UnionFind(26)
        for eqn in equations:
            x = ord(eqn[0]) - ord('a')
            y = ord(eqn[3]) - ord('a')
            if eqn[1] == '=':
                union_find.union_set(x, y)
        for eqn in equations:
            x = ord(eqn[0]) - ord('a')
            y = ord(eqn[3]) - ord('a')
            if eqn[1] == '!':
                if union_find.find_set(x) == union_find.find_set(y):
                    return False
        return True