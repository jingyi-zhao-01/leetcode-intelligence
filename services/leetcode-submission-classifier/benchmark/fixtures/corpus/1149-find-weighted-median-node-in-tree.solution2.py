# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-weighted-median-node-in-tree
# source_path: LeetCode-Solutions-master/Python/find-weighted-median-node-in-tree.py
# solution_class: Solution2
# submission_id: 41fe4954483155c10b187ca3e4fff02b9aca3374
# seed: 553535746

# Time:  O(n + qlogh)
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


def binary_search(left, right, check):
    while left <= right:
        mid = left+(right-left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left


# iterative dfs, Tarjan's Offline LCA Algorithm, binary search, prefix sum

class Solution2(object):
    def findMedian(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u):
            for i in lookup2[u]:
                if queries[i][0] == queries[i][1]:
                    lca[i] = u
                    continue
                result[i] += dist[u]
                for x in queries[i]:
                    if lookup[x]:
                        lca[i] = ancestor[uf.find_set(x)]
                        result[i] -= 2*dist[lca[i]]
            lookup[u] = True
            for v, w in adj[u]:
                if lookup[v]:
                    continue
                dist[v] = dist[u]+w
                depth[v] = depth[u]+1
                dfs(v)
                uf.union_set(v, u)
                ancestor[uf.find_set(u)] = u
    
        def dfs2(u):
            path.append(u)
            for i, t in lookup3[u]:
                d = depth[u]-depth[lca[i]]
                if t == 0:
                    j = binary_search(0, d, lambda x: 2*(dist[u]-dist[path[-(x+1)]]) >= result[i])
                    result2[i] = path[-(j+1)]
                else:
                    l = dist[queries[i][0]]-dist[lca[i]]
                    j = binary_search(0, d-1, lambda x: 2*(l+(dist[path[-((d-1)+1)+x]]-dist[lca[i]])) >= result[i])
                    result2[i] = path[-((d-1)+1)+j]
            for v, w in adj[u]:
                if len(path) >= 2 and path[-2] == v:
                    continue
                dfs2(v)
            path.pop()
    
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
        depth = [0]*len(adj)
        result = [0]*len(queries)
        lca = [-1]*len(queries)
        dfs(0)
        result2 = [0]*len(queries)
        lookup3 = [[] for _ in xrange(len(adj))]
        for i, (u, v) in enumerate(queries):
            if 2*(dist[u]-dist[lca[i]]) >= result[i]:
                lookup3[u].append((i, 0))
            else:
                lookup3[v].append((i, 1))
        path = []
        dfs2(0)
        return result2