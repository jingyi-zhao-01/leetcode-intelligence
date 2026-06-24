# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-ancestors-of-a-node-in-a-directed-acyclic-graph
# source_path: LeetCode-Solutions-master/Python/all-ancestors-of-a-node-in-a-directed-acyclic-graph.py
# solution_class: Solution3
# submission_id: 621c77c071a7b73eb196036bdecdf3fa18e59cfc
# seed: 1685592549

# Time:  O(|V| * |E|)
# Space: O(|V| + |E|)

# dfs

class Solution3(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [set() for _ in xrange(n)]
        in_degree = [0]*n
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            result[v].add(u)
        q = [u for u, d in enumerate(in_degree) if not d]
        while q:
            new_q = []
            for u in q:
                for v in adj[u]:
                    result[v].update(result[u])
                    in_degree[v] -= 1
                    if not in_degree[v]:
                        new_q.append(v)
            q = new_q
        return [sorted(s) for s in result]