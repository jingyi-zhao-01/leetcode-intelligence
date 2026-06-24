# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distance-to-a-cycle-in-undirected-graph
# source_path: LeetCode-Solutions-master/Python/distance-to-a-cycle-in-undirected-graph.py
# solution_class: Solution
# submission_id: 8264fce97db5cc134eda11c24ae77cd11fe6b5c5
# seed: 966564818

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

# graph, dfs, bfs

class Solution(object):
    def distanceToCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def cycle(parent, v, u):
            result = [parent[v], v]
            while u != parent[v]:
                result.append(u)
                u = parent[u]
            return result
    
        def iter_dfs(adj):
            stk = [0]
            parent = [-2]*len(adj)
            parent[0] = -1
            while stk:
                u = stk.pop()
                for v in reversed(adj[u]):
                    if parent[v] != -2:
                        if v == parent[u]:
                            continue
                        return cycle(parent, v, u)
                    parent[v] = u
                    stk.append(v)

        def bfs(adj, q):
            result = [-1]*n
            for x in q:
                result[x] = 0
            d = 1
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if result[v] != -1:
                            continue
                        result[v] = d
                        new_q.append(v)
                q = new_q
                d += 1
            return result
    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bfs(adj, iter_dfs(adj))