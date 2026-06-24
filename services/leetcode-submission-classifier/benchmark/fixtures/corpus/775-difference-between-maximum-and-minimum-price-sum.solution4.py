# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: difference-between-maximum-and-minimum-price-sum
# source_path: LeetCode-Solutions-master/Python/difference-between-maximum-and-minimum-price-sum.py
# solution_class: Solution4
# submission_id: 1f26e0e010460070e564385f1869b24feaf286ff
# seed: 1663877625

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution4(object):
    def maxOutput(self, n, edges, price):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :rtype: int
        """
        def dfs(u, p):
            dp[u] = price[u]
            for v in adj[u]:
                if v == p:
                    continue
                dp[u] = max(dp[u], dfs(v, u)+price[u])
            return dp[u]
        
        def dfs2(u, p, curr):
            result[0] = max(result[0], curr, dp[u]-price[u])
            top2 = [[curr, p], [0, -1]]
            for v in adj[u]:
                if v == p:
                    continue
                curr = [dp[v], v]
                for i in xrange(len(top2)):
                    if curr > top2[i]:
                        top2[i], curr = curr, top2[i]
            for v in adj[u]:
                if v == p:
                    continue
                dfs2(v, u, (top2[0][0] if top2[0][1] != v else top2[1][0])+price[u])
    
        result = [0]
        dp = [0]*n  # max_sum
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dfs(0, -1)
        dfs2(0, -1, 0)
        return result[0]