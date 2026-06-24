# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-nodes-into-the-maximum-number-of-groups
# source_path: LeetCode-Solutions-master/Python/divide-nodes-into-the-maximum-number-of-groups.py
# solution_class: Solution
# submission_id: 39e138e775d80ac78d97ec9a6c1b50028db5b405
# seed: 1146798489

# Time:  O(n^2)
# Space: O(n)

# iterative dfs, bfs

class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def iter_dfs(u):
            group = []
            stk = [u]
            lookup[u] = 0
            while stk:
                u = stk.pop()
                group.append(u)
                for v in adj[u]:
                    if lookup[v] != -1:
                        if lookup[v] == lookup[u]:  # odd-length cycle, not bipartite
                            return []
                        continue
                    lookup[v] = lookup[u]^1
                    stk.append(v)
            return group

        def bfs(u):
            result = 0
            lookup = [False]*n
            q = [u]
            lookup[u] = True
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q = new_q
                result += 1
            return result
    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        result = 0
        lookup = [-1]*n
        for u in xrange(n):
            if lookup[u] != -1:
                continue
            group = iter_dfs(u)
            if not group:
                return -1
            result += max(bfs(u) for u in group)
        return result