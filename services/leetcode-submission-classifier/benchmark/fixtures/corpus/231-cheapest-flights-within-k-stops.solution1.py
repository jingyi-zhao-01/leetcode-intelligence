# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cheapest-flights-within-k-stops
# source_path: LeetCode-Solutions-master/Python/cheapest-flights-within-k-stops.py
# solution_class: Solution
# submission_id: d3e4d1c9dcb247f619920857be90856d88a252fb
# seed: 2661919105

# Time:  O((|E| + |V|) * log|V|) = O(|E| * log|V|),
#        if we can further to use Fibonacci heap, it would be O(|E| + |V| * log|V|)
# Space: O(|E| + |V|) = O(|E|)

import collections
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        best = collections.defaultdict(lambda: collections.defaultdict(lambda: float("inf")))
        best[src][K+1] = 0
        min_heap = [(0, src, K+1)]
        while min_heap:
            result, u, k = heapq.heappop(min_heap)
            if k < 0 or best[u][k] < result:
                continue
            if u == dst:
                return result
            for v, w in adj[u]:
                if result+w < best[v][k-1]:
                    best[v][k-1] = result+w                    
                    heapq.heappush(min_heap, (result+w, v, k-1))
        return -1