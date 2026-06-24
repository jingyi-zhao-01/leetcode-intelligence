# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-diameter-after-merging-two-trees
# source_path: LeetCode-Solutions-master/Python/find-minimum-diameter-after-merging-two-trees.py
# solution_class: Solution3
# submission_id: 793a3fde41da850e5cb79a415f5612dcba198bfe
# seed: 2655224198

# Time:  O(n + m)
# Space: O(n + m)

# iterative dfs, tree diameter

class Solution3(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
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
            
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return bfs()

        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)