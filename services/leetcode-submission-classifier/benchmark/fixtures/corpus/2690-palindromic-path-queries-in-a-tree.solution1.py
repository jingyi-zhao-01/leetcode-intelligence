# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindromic-path-queries-in-a-tree
# source_path: LeetCode-Solutions-master/Python/palindromic-path-queries-in-a-tree.py
# solution_class: Solution
# submission_id: c27dddd32e0274c7a1167afd86fafd469ca76e22
# seed: 1886164121

# Time:  O((n + q) * logn)
# Space: O(n)

# hld, lca, fenwick tree

class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        class BIT(object):  # 0-indexed.
            def __init__(self, n):
                self.__bit = [0]*(n+1)  # Extra one for dummy node.

            def add(self, i, val):
                i += 1  # Extra one for dummy node.
                while i < len(self.__bit):
                    self.__bit[i] ^= val  # modified
                    i += (i & -i)

            def query(self, i):
                i += 1  # Extra one for dummy node.
                ret = 0
                while i > 0:
                    ret ^= self.__bit[i]  # modified
                    i -= (i & -i)
                return ret


        def build_hld(adj, cb):
            parent, depth, size, heavy, head = [-1]*len(adj), [0]*len(adj), [1]*len(adj), [-1]*len(adj), list(range(len(adj)))
            stk = [(1, 0, -1)]
            while stk:
                step, u, p = stk.pop()
                if step == 1:
                    cb(u, p)
                    parent[u], depth[u] = p, (depth[p]+1 if p != -1 else 0)
                    stk.append((2, u, p))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, v, u))
                elif step == 2:
                    for v in adj[u]:
                        if v == parent[u]:
                            continue
                        size[u] += size[v]
                        if heavy[u] == -1 or size[v] > size[heavy[u]]:
                            heavy[u] = v
            idx = -1
            left, right = [-1]*len(adj), [-1]*len(adj)
            stk = [(1, 0, 0)]
            while stk:
                step, u, h = stk.pop()
                if step == 1:
                    idx += 1
                    head[u], left[u] = h, idx
                    stk.append((2, u, h))
                    for v in adj[u]:
                        if v == parent[u] or v == heavy[u]:
                            continue
                        stk.append((1, v, v))
                    if heavy[u] != -1:
                        stk.append((1, heavy[u], h))
                elif step == 2:
                    right[u] = idx
            return parent, depth, head, left, right
    
        def lca(u, v):
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                u = parent[head[u]]
            return u if depth[u] < depth[v] else v

        def callback(u, p):
            prefix[u] = (prefix[p] if p != -1 else 0)^(1<<(ord(s[u])-ord('a')))

        s = list(s)
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        prefix = [0]*n
        parent, depth, head, left, right = build_hld(adj, callback)
        bit = BIT(n+1)
        result = []
        for q in queries:
            args = q.split()
            op = args[0]
            u = int(args[1])
            if op == "update":
                c = args[2]
                diff = (1<<(ord(s[u])-ord('a')))^(1<<(ord(c)-ord('a')))
                if not diff:
                    continue
                s[u] = c
                bit.add(left[u], diff)
                bit.add(right[u]+1, diff)
            else:
                v = int(args[2])
                l = lca(u, v)
                mask = (prefix[u]^bit.query(left[u]))^(prefix[v]^bit.query(left[v]))^(1<<(ord(s[l])-ord('a')))
                result.append((mask&(mask-1)) == 0)
        return result