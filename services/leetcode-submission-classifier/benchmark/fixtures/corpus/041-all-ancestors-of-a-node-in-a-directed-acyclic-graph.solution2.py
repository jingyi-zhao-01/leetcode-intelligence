# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-ancestors-of-a-node-in-a-directed-acyclic-graph
# source_path: LeetCode-Solutions-master/Python/all-ancestors-of-a-node-in-a-directed-acyclic-graph.py
# solution_class: Solution2
# submission_id: 52680f7edd9349f290238675dd30a155df5cc291
# seed: 4034775667

# Time:  O(|V| * |E|)
# Space: O(|V| + |E|)

# dfs

class Solution2(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(adj, i, result):
            lookup = [False]*len(adj)
            q = [i]
            lookup[i] = True
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                        result[i].append(v)
                q = new_q
            result[i].sort()

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[v].append(u)
        result = [[] for _ in xrange(n)]
        for u in xrange(n):
            bfs(adj, u, result) 
        return result