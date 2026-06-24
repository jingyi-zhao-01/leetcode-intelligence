# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tree-diameter
# source_path: LeetCode-Solutions-master/Python/tree-diameter.py
# solution_class: Solution3
# submission_id: dab4e48e6002fbe7ea22f07dba21245c90d527c8
# seed: 426811130

# Time:  O(|V| + |E|)
# Space: O(|E|)

# iterative dfs

class Solution3(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def bfs():
            result = 0
            dp = [0]*len(adj)
            degree = map(len, adj)
            q = [u for u in xrange(len(degree)) if degree[u] == 1]
            while q:
                new_q = []
                for u in q:
                    if degree[u] == 0:
                        continue
                    degree[u] -= 1
                    for v in adj[u]:
                        if degree[v] == 0:
                            continue
                        result = max(result, dp[v]+(dp[u]+1))
                        dp[v] = max(dp[v], (dp[u]+1))
                        degree[v] -= 1
                        if degree[v] == 1:
                            new_q.append(v)
                q = new_q
            return result
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bfs()