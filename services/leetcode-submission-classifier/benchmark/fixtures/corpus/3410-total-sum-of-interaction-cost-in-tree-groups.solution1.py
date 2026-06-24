# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-sum-of-interaction-cost-in-tree-groups
# source_path: LeetCode-Solutions-master/Python/total-sum-of-interaction-cost-in-tree-groups.py
# solution_class: Solution
# submission_id: 4d780d9351fafd5a6bf0951ba64452dae692cdcb
# seed: 2625983724

# Time:  O(n * g)
# Space: O(n * g)

# bfs

class Solution(object):
    def interactionCosts(self, n, edges, group):
        """
        :type n: int
        :type edges: List[List[int]]
        :type group: List[int]
        :rtype: int
        """
        def bfs():
            order, parent = [0], [-1]*len(adj)
            for u in order:
                for v in adj[u]:
                    if v == parent[u]:
                        continue
                    parent[v] = u
                    order.append(v)
            return order, parent

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        mx = max(group)
        total = [0]*mx
        for x in group:
            total[x-1] += 1
        result = 0
        order, parent = bfs()
        cnt = [[0]*mx for _ in xrange(n)]
        for u in reversed(order):
            cnt[u][group[u]-1] += 1
            for v in adj[u]:
                if u != parent[v]:
                    continue
                for k in xrange(len(cnt[v])):
                    result += cnt[v][k]*(total[k]-cnt[v][k])
                    cnt[u][k] += cnt[v][k]
        return result