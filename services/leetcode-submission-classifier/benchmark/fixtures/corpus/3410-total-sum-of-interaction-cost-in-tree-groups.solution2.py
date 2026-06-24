# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-sum-of-interaction-cost-in-tree-groups
# source_path: LeetCode-Solutions-master/Python/total-sum-of-interaction-cost-in-tree-groups.py
# solution_class: Solution2
# submission_id: 0073b9d4a7c62d31dd6e6dedf98eaef9eefc9d32
# seed: 2341786769

# Time:  O(n * g)
# Space: O(n * g)

# bfs

class Solution2(object):
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
        total = collections.defaultdict(int)
        for x in group:
            total[x] += 1
        result = 0
        order, parent = bfs()
        cnt = [collections.defaultdict(int) for _ in xrange(n)]
        for u in reversed(order):
            cnt[u][group[u]] += 1
            for v in adj[u]:
                if u != parent[v]:
                    continue
                for k, c in cnt[v].iteritems():
                    result += c*(total[k]-c)
                if len(cnt[v]) > len(cnt[u]):
                    cnt[u], cnt[v] = cnt[v], cnt[u]
                for k, c in cnt[v].iteritems():
                    cnt[u][k] += c
                cnt[v].clear()
        return result