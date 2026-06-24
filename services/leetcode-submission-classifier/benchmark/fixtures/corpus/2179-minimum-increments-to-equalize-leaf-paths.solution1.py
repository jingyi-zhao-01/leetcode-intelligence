# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-increments-to-equalize-leaf-paths
# source_path: LeetCode-Solutions-master/Python/minimum-increments-to-equalize-leaf-paths.py
# solution_class: Solution
# submission_id: 640b243378c1eaab1f28fd555bf7cc960b314129
# seed: 3474890398

# Time:  O(n)
# Space: O(n)

# iterative dfs

class Solution(object):
    def minIncrease(self, n, edges, cost):
        """
        :type n: int
        :type edges: List[List[int]]
        :type cost: List[int]
        :rtype: int
        """
        def iter_dfs():
            result = n-1
            mx = [0]*len(adj)
            stk = [(1, (0, -1))]
            while stk:
                step, (u, p) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p)))
                    for v in reversed(adj[u]):
                        if v != p:
                            stk.append((1, (v, u)))
                elif step == 2:
                    cnt = 0
                    for v in adj[u]:
                        if v == p or mx[v] < mx[u]:
                            continue
                        if mx[v] > mx[u]:
                            mx[u] = mx[v]
                            cnt = 0
                        cnt += 1
                    result -= cnt
                    mx[u] += cost[u]
            return result

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()