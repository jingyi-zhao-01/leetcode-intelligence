# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-maximum-edge-weight-of-graph
# source_path: LeetCode-Solutions-master/Python/minimize-the-maximum-edge-weight-of-graph.py
# solution_class: Solution3
# submission_id: 3e7eb46e3537efbd2472994defe0c7ffb5041358
# seed: 875126701

# Time:  O(nlogn + e)
# Space: O(n + e)

import collections
import heapq


# dijkstra's algorithm

class Solution3(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(x):
            cnt = len(adj)
            lookup = [False]*len(adj)
            lookup[0] = True
            cnt -= 1
            q = [0]
            while q:
                new_q = []
                for u in q:
                    for v, w in adj[u].iteritems():
                        if w > x or lookup[v]:
                            continue
                        lookup[v] = True
                        cnt -= 1
                        new_q.append(v)
                q = new_q
            return cnt == 0
    
        adj = [collections.defaultdict(lambda: float("inf")) for _ in xrange(n)]
        for i, j, w in edges:
            adj[j][i] = min(adj[j][i], w)
        left, right = min(w for _, _, w in edges), max(w for _, _, w in edges)
        result = binary_search(left, right, check)
        return result if result <= right else -1