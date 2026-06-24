# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: finish-time-of-tasks-i
# source_path: LeetCode-Solutions-master/Python/finish-time-of-tasks-i.py
# solution_class: Solution2
# submission_id: d0ed24ac283acad6605be0a3d99715490aa35399
# seed: 582736813

# Time:  O(n)
# Space: O(n)

# iterative dfs, tree dp

class Solution2(object):
    def finishTime(self, n, edges, baseTime):
        """
        :type n: int
        :type edges: List[List[int]]
        :type baseTime: List[int]
        :rtype: int
        """
        POS_INF, NEG_INF = float("inf"), float("-inf")
        def dfs(u):
            mx, mn = NEG_INF, POS_INF
            for v in adj[u]:
                ret = dfs(v)
                mx, mn = max(mx, ret), min(mn, ret)
            return ((2*mx-mn) if mx is not NEG_INF else 0)+baseTime[u]
    
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
        return dfs(0)