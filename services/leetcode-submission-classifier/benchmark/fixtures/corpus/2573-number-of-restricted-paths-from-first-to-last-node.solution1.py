# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-restricted-paths-from-first-to-last-node
# source_path: LeetCode-Solutions-master/Python/number-of-restricted-paths-from-first-to-last-node.py
# solution_class: Solution
# submission_id: bbc37e0e3fe792c74f2b81b19081445c205d59a7
# seed: 2865159861

# Time:  O(|E| * log|V|)
# Space: O(|E| + |V|)

import heapq

class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        adj = [[] for _ in xrange(n)]
        for u, v, w in edges:
            adj[u-1].append((v-1, w))
            adj[v-1].append((u-1, w))
        dist = [float("inf")]*n
        dp = [0]*n
        dist[n-1] = 0
        dp[n-1] = 1
        min_heap = [(0, n-1)]
        while min_heap:
            w, u = heapq.heappop(min_heap)
            if w > dist[u]:
                continue
            for v, d in adj[u]:
                if w+d < dist[v]:
                    dist[v] = w+d
                    heapq.heappush(min_heap, (dist[v], v))
                elif w > dist[v]:
                    dp[u] = (dp[u]+dp[v])%MOD
            if u == 0:  # early return
                break
        return dp[0]