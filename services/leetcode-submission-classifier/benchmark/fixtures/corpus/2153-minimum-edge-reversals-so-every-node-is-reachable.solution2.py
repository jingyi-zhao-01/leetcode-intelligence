# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-edge-reversals-so-every-node-is-reachable
# source_path: LeetCode-Solutions-master/Python/minimum-edge-reversals-so-every-node-is-reachable.py
# solution_class: Solution2
# submission_id: 5836221f12c14090b85e5054709cbe5aa3684756
# seed: 844942863

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution2(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs1(u, p):
            return sum(adj[u][v]+dfs1(v, u) for v in adj[u] if v != p)

        def dfs2(u, curr):
            result[u] = curr
            for v in adj[u]:
                if result[v] == -1:
                    dfs2(v, curr-adj[u][v]+adj[v][u])
    
        adj = collections.defaultdict(dict)
        for u, v in edges:
            adj[u][v] = 0
            adj[v][u] = 1
        result = [-1]*n
        dfs2(0, dfs1(0, -1))
        return result