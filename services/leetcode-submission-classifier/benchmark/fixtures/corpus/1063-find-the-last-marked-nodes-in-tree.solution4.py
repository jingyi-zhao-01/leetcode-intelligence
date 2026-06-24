# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-last-marked-nodes-in-tree
# source_path: LeetCode-Solutions-master/Python/find-the-last-marked-nodes-in-tree.py
# solution_class: Solution4
# submission_id: 02fb3f825bedf4ac93b0014ab9039ec3aee8ba97
# seed: 2058021371

# Time:  O(n)
# Space: O(n)

# bfs

class Solution4(object):
    def lastMarkedNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def increase(x):
            return (x[0]+1, x[1])

        def iter_dfs1():
            dp = [[(0, u)]*2 for u in xrange(len(adj))]
            stk = [(1, (0, -1))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p = args
                    stk.append((2, (u, p, 0)))
                elif step == 2:
                    u, p, i = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, i+1)))
                    v = adj[u][i]
                    if v == p:
                        continue
                    stk.append((3, (v, u)))
                    stk.append((1, (v, u)))
                elif step == 3:
                    v, u = args
                    curr = increase(dp[v][0])
                    for i in xrange(len(dp[u])):
                        if curr > dp[u][i]:
                            curr, dp[u][i] = dp[u][i], curr
            return dp

        def iter_dfs2():
            result = [-1]*len(adj)
            stk = [(0, -1, (0, -1))]
            while stk:
                u, p, curr = stk.pop()
                result[u] = max(dp[u][0], curr)[1]
                for v in reversed(adj[u]):
                    if v == p:
                        continue
                    stk.append((v, u, increase(max(dp[u][dp[u][0][1] == dp[v][0][1]], curr))))
            return result
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dp = iter_dfs1()
        return iter_dfs2()