# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-edge-weight-of-graph
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-edge-weight-of-graph.py
# solution_class: Solution
# submission_id: d503f70cb45954a7d5e15d888268d769ea13b131
# seed: 1706392348

# Time:  O(nlogn + e)
# Space: O(n + e)

import collections
import heapq


# dijkstra's algorithm

class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        def dijkstra():
            best = [float("inf")]*len(adj)
            best[0] = 0
            min_heap = [(best[0], 0)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr != best[u]:
                    continue
                for v, w in adj[u].iteritems():
                    if not (max(curr, w) < best[v]):
                        continue
                    best[v] = max(curr, w)
                    heapq.heappush(min_heap, (best[v], v))
            result = max(best)
            return result if result != float("inf") else -1

        adj = [collections.defaultdict(lambda: float("inf")) for _ in xrange(n)]
        for i, j, w in edges:
            adj[j][i] = min(adj[j][i], w)
        return dijkstra()