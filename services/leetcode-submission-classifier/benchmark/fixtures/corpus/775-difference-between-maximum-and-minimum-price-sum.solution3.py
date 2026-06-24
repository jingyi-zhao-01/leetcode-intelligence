# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: difference-between-maximum-and-minimum-price-sum
# source_path: LeetCode-Solutions-master/Python/difference-between-maximum-and-minimum-price-sum.py
# solution_class: Solution3
# submission_id: bd3f5f5f6a91609ee88808d1e76f2e02e3a16fe9
# seed: 867555963

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution3(object):
    def maxOutput(self, n, edges, price):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :rtype: int
        """
        def iter_dfs():
            dp = [0]*n  # max_sum
            stk = [(1, 0, -1)]
            while stk:
                step, u, p = stk.pop()
                if step == 1:
                    stk.append((2, u, p))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, v, u))
                elif step == 2:
                    dp[u] = price[u]
                    for v in adj[u]:
                        if v == p:
                            continue
                        dp[u] = max(dp[u], dp[v]+price[u])
            return dp
        
        def iter_dfs2():
            result = 0
            stk = [(0, -1, 0)]
            while stk:
                u, p, curr = stk.pop()
                result = max(result, curr, dp[u]-price[u])
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
                    stk.append((v, u, (top2[0][0] if top2[0][1] != v else top2[1][0])+price[u]))
            return result
    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = iter_dfs()
        return iter_dfs2()