# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-after-road-addition-queries-i
# source_path: LeetCode-Solutions-master/Python/shortest-distance-after-road-addition-queries-i.py
# solution_class: Solution2
# submission_id: 19b5ebb0cde2320872bbddfb61aec441a60788fc
# seed: 2498676427

# Time:  O(n^2)
# Space: O(n^2)

# bfs

class Solution2(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def dijkstra(u, v):
            adj[u].append((v, 1))
            min_heap = [(dist[u], u)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > dist[u]:
                    continue
                for v, w in adj[u]:
                    if curr+w >= dist[v]:
                        continue
                    dist[v] = curr+w
                    heapq.heappush(min_heap, (dist[v], v))
            return dist[-1]

        adj = [[] for _ in xrange(n)]
        for u in xrange(n-1):
            adj[u].append((u+1, 1))
        dist = range(n)
        return [dijkstra(u, v) for u, v in queries]