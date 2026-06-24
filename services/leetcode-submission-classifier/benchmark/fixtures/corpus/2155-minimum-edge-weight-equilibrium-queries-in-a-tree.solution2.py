# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-edge-weight-equilibrium-queries-in-a-tree
# source_path: LeetCode-Solutions-master/Python/minimum-edge-weight-equilibrium-queries-in-a-tree.py
# solution_class: Solution2
# submission_id: 152912ef961c2d9ccb0fc0337395633bf167ca6d
# seed: 4166907985

# Time:  O(r * (n + q)), r = max(w for _, _, w in edges)
# Space: O(r * n + q)

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
    def __init__(self, adj, pairs):
        def preprocess(u, p, w):  # modified
            # depth of the node i
            D[u] = 1 if p == -1 else D[p]+1
            if w != -1:  # added
                cnt[w] += 1
            CNT[u] = cnt[:]  # added

        def divide(u, p, w):  # modified
            stk.append(partial(postprocess, u, w))  # modified
            for i in reversed(xrange(len(adj[u]))):
                v, nw = adj[u][i]
                if v == p:
                    continue
                stk.append(partial(conquer, v, u))
                stk.append(partial(divide, v, u, nw))  # modified
            stk.append(partial(preprocess, u, p, w))  # modified

        def conquer(u, p):
            uf.union_set(u, p)
            uf.update_ancestor_of_set(p)

        def postprocess(u, w):  # modified
            lookup[u] = True
            for v in pairs[u]:
                if not lookup[v]:
                    continue
                lca[min(u, v), max(u, v)] = uf.find_ancestor_of_set(v)
            if w != -1:  # added
                cnt[w] -= 1

        N = len(adj)
        D, uf, lca = [0]*N, UnionFind(N), {}
        CNT = [[0]*MAX_W for _ in xrange(N)]  # added
        cnt = [0]*MAX_W  # added
        stk, lookup = [], [False]*N
        stk.append(partial(divide, 0, -1, -1))  # modified
        while stk:
            stk.pop()()
        self.D, self.lca = D, lca
        self.CNT = CNT  # added


# Tarjan's Offline LCA Algorithm
MAX_W = 26

class Solution2(object):
    def minOperationsQueries(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in xrange(n)]
        for u, v, w in edges:
            w -= 1
            adj[u].append((v, w))
            adj[v].append((u, w))
        tree_infos = TreeInfos2(adj)
        result = [0]*len(queries)
        for i, (a, b) in enumerate(queries):
            lca = tree_infos.lca(a, b)
            result[i] = (tree_infos.D[a]+tree_infos.D[b]-2*tree_infos.D[lca])-max(tree_infos.CNT[a][w]+tree_infos.CNT[b][w]-2*tree_infos.CNT[lca][w] for w in xrange(MAX_W))
        return result