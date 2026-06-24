# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-edge-weight-of-graph
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-edge-weight-of-graph.py
# solution_class: Solution2
# submission_id: e8163ba4516f7dd7d414db6436ea303fea82508a
# seed: 4127640500

# Time:  O(nlogn + e)
# Space: O(n + e)

import collections
import heapq


# dijkstra's algorithm

class Solution2(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        def prim():
            best = [float("inf")]*len(adj)
            min_heap = [(0, 0)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if best[u] != float("inf"):
                    continue
                best[u] = curr
                for v, w in adj[u].iteritems():
                    if best[v] != float("inf"):
                        continue
                    heapq.heappush(min_heap, (w, v))
            result = max(best)
            return result if result != float("inf") else -1

        adj = [collections.defaultdict(lambda: float("inf")) for _ in xrange(n)]
        for i, j, w in edges:
            adj[j][i] = min(adj[j][i], w)
        return prim()