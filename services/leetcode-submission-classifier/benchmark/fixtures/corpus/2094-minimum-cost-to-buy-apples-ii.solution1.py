# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-buy-apples-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-buy-apples-ii.py
# solution_class: Solution
# submission_id: 6dee7eb205044fa1811f4405016f6f0ace64ff18
# seed: 3698758304

# Time:  O(n * (n + elogn))
# Space: O(n + e)

import heapq


# dijkstra's algorithm

class Solution(object):
    def minCost(self, n, prices, roads):
        """
        :type n: int
        :type prices: List[int]
        :type roads: List[List[int]]
        :rtype: List[int]
        """
        INF = float("inf")
        def dijkstra(start, target):
            best = [INF]*len(adj)
            best[start] = 0
            min_heap = [(best[start], start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr != best[u]:
                    continue
                if u == target:
                    return curr
                for v, w in adj[u]:     
                    if best[v] <= curr+w:
                        continue
                    best[v] = curr+w
                    heapq.heappush(min_heap, (best[v], v))
            return INF

        adj = [[] for _ in xrange(2*n)]
        for u, v, c, t in roads:
            adj[u].append((v, c))
            adj[v].append((u, c))
            adj[u+n].append((v+n, c*t))
            adj[v+n].append((u+n, c*t))
        for i in xrange(n):
            adj[i].append((i+n , prices[i]))
        return [dijkstra(i, i+n) for i in xrange(n)]