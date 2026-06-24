# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-last-marked-nodes-in-tree
# source_path: LeetCode-Solutions-master/Python/find-the-last-marked-nodes-in-tree.py
# solution_class: Solution2
# submission_id: 960ea9935ecebbc39583d3b4f22bf134d333a515
# seed: 1637371828

# Time:  O(n)
# Space: O(n)

# bfs

class Solution2(object):
    def lastMarkedNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def increase(x):
            return (x[0]+1, x[1])

        def bfs():
            dp = [[(0, u)]*2 for u in xrange(len(adj))]
            new_root = -1
            degree = map(len, adj)
            q = [u for u in xrange(len(degree)) if degree[u] == 1]
            while q:
                new_q = []
                for u in q:
                    if degree[u] == 0:
                        new_root = u
                        continue
                    degree[u] -= 1
                    for v in adj[u]:
                        if degree[v] == 0:
                            continue
                        curr = increase(dp[u][0])
                        for i in xrange(len(dp[v])):
                            if curr > dp[v][i]:
                                curr, dp[v][i] = dp[v][i], curr
                        degree[v] -= 1
                        if degree[v] == 1:
                            new_q.append(v)
                q = new_q
            return dp, new_root

        def bfs2(root):
            result = [-1]*len(adj)
            q = [(root, -1, (0, -1))]
            while q:
                new_q = []
                for u, p, curr in q:
                    result[u] = max(dp[u][0], curr)[1]
                    for v in adj[u]:
                        if v == p:
                            continue
                        new_q.append((v, u, increase(max(dp[u][dp[u][0][1] == dp[v][0][1]], curr))))
                q = new_q
            return result

        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp, u = bfs()
        return bfs2(u)