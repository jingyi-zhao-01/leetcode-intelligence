# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-operations-to-make-network-connected
# source_path: LeetCode-Solutions-master/Python/number-of-operations-to-make-network-connected.py
# solution_class: Solution2
# submission_id: 17751ab4e1e08f54ee400440d1bb8791afe11295
# seed: 2681694112

# Time:  O(|E| + |V|)
# Space: O(|V|)

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

class Solution2(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        def dfs(i, lookup):
            if i in lookup:
                return 0
            lookup.add(i)
            if i in G:
                for j in G[i]:
                    dfs(j, lookup)
            return 1

        if len(connections) < n-1:
            return -1
        G = collections.defaultdict(list)
        for i, j in connections:
            G[i].append(j)
            G[j].append(i)
        lookup = set()
        return sum(dfs(i, lookup) for i in xrange(n)) - 1