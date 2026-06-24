# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-last-marked-nodes-in-tree
# source_path: LeetCode-Solutions-master/Python/find-the-last-marked-nodes-in-tree.py
# solution_class: Solution5
# submission_id: 2176ef4be22a1084ff5a6be8e139d2e6c14a3420
# seed: 2210722633

# Time:  O(n)
# Space: O(n)

# bfs

class Solution5(object):
    def lastMarkedNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def increase(x):
            return (x[0]+1, x[1])

        def dfs1(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs1(v, u)
                curr = increase(dp[v][0])
                for i in xrange(len(dp[u])):
                    if curr > dp[u][i]:
                        curr, dp[u][i] = dp[u][i], curr

        def dfs2(u, p, curr):
            for v in adj[u]:
                if v == p:
                    continue
                dfs2(v, u, increase(max(dp[u][dp[u][0][1] == dp[v][0][1]], curr)))
            result[u] = max(dp[u][0], curr)[1]
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = [[(0, u)]*2 for u in xrange(len(adj))]
        dfs1(0, -1)
        result = [-1]*len(adj)
        dfs2(0, -1, (0, -1))
        return result