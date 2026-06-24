# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-reach-destination-in-time
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-reach-destination-in-time.py
# solution_class: Solution
# submission_id: 22d8549ecee0f51747ea49773926077e3b22eaaa
# seed: 3119502792

# Time:  O((|E| + |V|) * log|V|) = O(|E| * log|V|),
#        if we can further to use Fibonacci heap, it would be O(|E| + |V| * log|V|)
# Space: O(|E| + |V|) = O(|E|)

import collections
import heapq


# Dijkstra's algorithm

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """        
        adj = [[] for i in xrange(len(passingFees))]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        best = collections.defaultdict(lambda:float("inf"))
        best[0] = 0
        min_heap = [(passingFees[0], 0, 0)]
        while min_heap:
            result, u, w = heapq.heappop(min_heap)
            if w > maxTime:  # state with best[u] < w can't be filtered, which may have less cost
                continue
            if u == len(passingFees)-1:
                return result
            for v, nw in adj[u]:
                if w+nw < best[v]:  # from less cost to more cost, only need to check state with less time
                    best[v] = w+nw
                    heapq.heappush(min_heap, (result+passingFees[v], v, w+nw))
        return -1