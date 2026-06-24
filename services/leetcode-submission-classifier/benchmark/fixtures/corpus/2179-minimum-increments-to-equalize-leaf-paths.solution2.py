# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-increments-to-equalize-leaf-paths
# source_path: LeetCode-Solutions-master/Python/minimum-increments-to-equalize-leaf-paths.py
# solution_class: Solution2
# submission_id: d637928d0c0710a98c7b4f8c860a841d5195e021
# seed: 3644205457

# Time:  O(n)
# Space: O(n)

# iterative dfs

class Solution2(object):
    def minIncrease(self, n, edges, cost):
        """
        :type n: int
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: int
        """
        def dfs(u, p):
            mx = cnt = 0
            for v in adj[u]:
                if v == p:
                    continue
                c = dfs(v, u)
                if c < mx:
                    continue
                if c > mx:
                    mx = c
                    cnt = 0
                cnt += 1
            result[0] -= cnt
            return mx+cost[u]

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [n-1]
        dfs(0, -1)
        return result[0]