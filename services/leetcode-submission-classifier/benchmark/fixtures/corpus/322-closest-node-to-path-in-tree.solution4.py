# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-node-to-path-in-tree
# source_path: LeetCode-Solutions-master/Python/closest-node-to-path-in-tree.py
# solution_class: Solution4
# submission_id: e7c5f9c78b45a14bd13c5df3d20d1e52e853959d
# seed: 367436006

# Time:  O(n + q)
# Space: O(n + q)

import collections
from functools import partial


# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20H/dependent_events3.py
# Tarjan's Offline LCA Algorithm
class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = range(n)
        self.rank = [0]*n
        self.ancestor = range(n)  # added

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

    def find_ancestor_of_set(self, x):  # added
        return self.ancestor[self.find_set(x)]

    def update_ancestor_of_set(self, x):  # added
        self.ancestor[self.find_set(x)] = x


class TreeInfos(object):  # Time: O(N), Space: O(N + Q), N is the number of nodes
    def __init__(self, children, pairs):
        def preprocess(curr, parent):
            # depth of the node i
            D[curr] = 1 if parent == -1 else D[parent]+1

        def divide(curr, parent):
            stk.append(partial(postprocess, curr))
            for i in reversed(xrange(len(children[curr]))):
                child = children[curr][i]
                if child == parent:
                    continue
                stk.append(partial(conquer, child, curr))
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        def conquer(curr, parent):
            uf.union_set(curr, parent)
            uf.update_ancestor_of_set(parent)

        def postprocess(u):
            lookup[u] = True
            for v in pairs[u]:
                if not lookup[v]:
                    continue
                lca[min(u, v), max(u, v)] = uf.find_ancestor_of_set(v)

        N = len(children)
        D, uf, lca = [0]*N, UnionFind(N), {}
        stk, lookup = [], [False]*N
        stk.append(partial(divide, 0, -1))
        while stk:
            stk.pop()()
        self.D, self.lca = D, lca


# Tarjan's Offline LCA Algorithm

class Solution4(object):
    def closestNode(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        def bfs(adj, root):
            dist = [len(adj)]*len(adj)
            q = [root]
            dist[root] = 0
            d = 0
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if d+1 >= dist[v]:
                            continue
                        dist[v] = d+1
                        new_q.append(v)
                q = new_q
                d += 1
            return dist

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v), adj[v].append(u)
        dist = [bfs(adj, i) for i in xrange(n)]
        result = []
        for start, end, node in query:
            x = end
            while start != end:
                if dist[node][start] < dist[node][x]:
                    x = start
                start = next(u for u in adj[start] if dist[u][end] < dist[start][end])
            result.append(x)
        return result