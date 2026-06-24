# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-taken-to-mark-all-nodes
# source_path: LeetCode-Solutions-master/Python/time-taken-to-mark-all-nodes.py
# solution_class: Solution
# submission_id: 6a3f55d8f5984b4a20e6c3e0dd825e998e1b224e
# seed: 1375881052

# Time:  O(n)
# Space: O(n)

# tree dp, bfs

class Solution(object):
    def timeTaken(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def topological_traversal():
            p = [-2]*len(adj)
            p[0] = -1
            topological_order = [0]
            for u in topological_order:
                for v in reversed(adj[u]):
                    if p[v] != -2:
                        continue
                    p[v] = u
                    topological_order.append(v)
            for u in reversed(topological_order):
                for v in adj[u]:
                    if v == p[u]:
                        continue
                    curr = [(1+int(v%2 == 0))+dp[v][0][0], v]
                    for i in xrange(len(dp[u])):
                        if curr > dp[u][i]:
                            curr, dp[u][i] = dp[u][i], curr

        def bfs():
            q = [(0, -1, 0)]
            while q:
                new_q = []
                for u, p, curr in q:
                    result[u] = max(dp[u][0][0], curr)
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u, (1+int(u%2 == 0))+max((dp[u][0][0] if dp[u][0][1] != v else dp[u][1][0]), curr)))
                q = new_q
    
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = [[[0, -1] for _ in xrange(2)] for _ in xrange(len(edges)+1)]
        topological_traversal()
        result = [0]*(len(edges)+1)
        bfs()
        return result