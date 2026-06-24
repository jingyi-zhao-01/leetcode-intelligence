# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-weighted-subgraph-with-the-required-paths-ii
# source_path: LeetCode-Solutions-master/Python/minimum-weighted-subgraph-with-the-required-paths-ii.py
# solution_class: Solution2
# submission_id: 40fe9fbddf1b90e5a77e93bb80757293719d94b6
# seed: 3930611974

# Time:  O(n + q)
# Space: O(n + q)

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


# iterative dfs, Tarjan's Offline LCA Algorithm

class Solution2(object):
    def minimumWeight(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u):
            for i in lookup2[u]:
                result[i] += dist[u]
                for x in queries[i]:
                    if lookup[x]:
                        result[i] -= dist[ancestor[uf.find_set(x)]]
            lookup[u] = True
            for v, w in adj[u]:
                if lookup[v]:
                    continue
                dist[v] = dist[u]+w
                dfs(v)
                uf.union_set(v, u)
                ancestor[uf.find_set(u)] = u
            
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        lookup = [False]*len(adj)
        lookup2 = [[] for _ in xrange(len(adj))]
        for i, q in enumerate(queries):
            for x in q:
                lookup2[x].append(i)
        uf = UnionFind(len(adj))
        ancestor = range(len(adj))
        dist = [0]*len(adj)
        result = [0]*len(queries)
        dfs(0)
        return result