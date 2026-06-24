# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-ancestors-of-a-node-in-a-directed-acyclic-graph
# source_path: LeetCode-Solutions-master/Python/all-ancestors-of-a-node-in-a-directed-acyclic-graph.py
# solution_class: Solution
# submission_id: c823f9e053c87aaceb80f8a4af96ba53fd7f3867
# seed: 2618047356

# Time:  O(|V| * |E|)
# Space: O(|V| + |E|)

# dfs

class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        def iter_dfs(adj, i, result):
            lookup = [False]*len(adj)
            stk = [i]
            while stk:
                u = stk.pop()
                for v in reversed(adj[u]):
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    stk.append(v)
                    result[v].append(i)
                    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
        result = [[] for _ in xrange(n)]
        for u in xrange(n):
            iter_dfs(adj, u, result)
        return result