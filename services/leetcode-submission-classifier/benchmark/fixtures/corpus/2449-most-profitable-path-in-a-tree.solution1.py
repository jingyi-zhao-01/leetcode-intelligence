# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-profitable-path-in-a-tree
# source_path: LeetCode-Solutions-master/Python/most-profitable-path-in-a-tree.py
# solution_class: Solution
# submission_id: 1d6a1043d3ac137a124d9606d430a628665ef08c
# seed: 1249590680

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        def iter_dfs():
            lookup = [[float("-inf"), float("inf")] for _ in xrange(len(adj))]
            stk = [(1, (0, -1, 0))]
            while stk:
                step, (u, p, ah) = stk.pop()
                if step == 1:
                    stk.append((2, (u, p, ah)))
                    for v in adj[u]:
                        if v == p:
                            continue
                        stk.append((1, (v, u, ah+1)))
                elif step == 2:
                    if len(adj[u])+(u == 0) == 1:
                        lookup[u][0] = 0
                    if u == bob:
                        lookup[u][1] = 0
                    for v in adj[u]:
                        if v == p:
                            continue
                        lookup[u][0] = max(lookup[u][0], lookup[v][0])
                        lookup[u][1] = min(lookup[u][1], lookup[v][1])
                    if ah == lookup[u][1]:
                        lookup[u][0] += amount[u]//2
                    elif ah < lookup[u][1]:
                        lookup[u][0] += amount[u]
                    lookup[u][1] += 1
            return lookup[0][0]

        adj = [[] for _ in xrange(len(edges)+1)]
        lookup = [False]*len(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()