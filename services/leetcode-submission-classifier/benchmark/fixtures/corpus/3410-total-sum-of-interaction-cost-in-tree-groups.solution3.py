# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-sum-of-interaction-cost-in-tree-groups
# source_path: LeetCode-Solutions-master/Python/total-sum-of-interaction-cost-in-tree-groups.py
# solution_class: Solution3
# submission_id: 8cd03eb7bb5e1899121023190204dbabc04c7e16
# seed: 2502911215

# Time:  O(n * g)
# Space: O(n * g)

# bfs

class Solution3(object):
    def interactionCosts(self, n, edges, group):
        """
        :type n: int
        :type edges: List[List[int]]
        :type group: List[int]
        :rtype: int
        """
        def dfs(u, p):
            cnt = collections.defaultdict(int)
            cnt[group[u]] += 1
            for v in adj[u]:
                if v == p:
                    continue
                new_cnt = dfs(v, u)
                for k, c in new_cnt.iteritems():
                    result[0] += c*(total[k]-c)
                if len(new_cnt) > len(cnt):
                    cnt, new_cnt = new_cnt, cnt
                for k, c in new_cnt.iteritems():
                    cnt[k] += c
            return cnt

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = collections.defaultdict(int)
        for x in group:
            total[x] += 1
        result = [0]
        dfs(0, -1)
        return result[0]