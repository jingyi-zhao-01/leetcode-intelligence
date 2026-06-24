# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finish-time-of-tasks-i
# source_path: LeetCode-Solutions-master/Python/finish-time-of-tasks-i.py
# solution_class: Solution
# submission_id: a3b9bdaefc809f0327428e1ece833a1ac5e39ce8
# seed: 144231393

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution(object):
    def finishTime(self, n, edges, baseTime):
        """
        :type n: int
        :type edges: List[List[int]]
        :type baseTime: List[int]
        :rtype: int
        """
        POS_INF, NEG_INF = float("inf"), float("-inf")
        def iter_dfs():
            dp = [0]*n
            stk = [(1, 0)]
            while stk:
                step, u = stk.pop()
                if step == 1:
                    stk.append((2, u))
                    for v in reversed(adj[u]):
                        stk.append((1, v))
                elif step == 2:
                    mx, mn = NEG_INF, POS_INF
                    for v in adj[u]:
                        mx, mn = max(mx, dp[v]), min(mn, dp[v])
                    dp[u] = ((2*mx-mn) if mx is not NEG_INF else 0)+baseTime[u]
            return dp[0]
    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
        return iter_dfs()