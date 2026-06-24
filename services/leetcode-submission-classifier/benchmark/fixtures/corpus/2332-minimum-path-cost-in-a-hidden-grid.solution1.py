# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-path-cost-in-a-hidden-grid
# source_path: LeetCode-Solutions-master/Python/minimum-path-cost-in-a-hidden-grid.py
# solution_class: Solution
# submission_id: b4cdd8e268048d0e808eb4086e3b576bfbd25696
# seed: 4088008161

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

class GridMaster(object):
    def canMove(self, direction):
        pass

    def move(self, direction):
        pass

    def isTarget(self):
        pass


import collections
import heapq

class Solution(object):
    def findShortestPath(self, master):
        """
        :type master: GridMaster
        :rtype: int
        """
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        rollback = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

        def dfs(pos, target, master, lookup, adj):
            if target[0] is None and master.isTarget():
                target[0] = pos
            lookup.add(pos)
            for d, (di, dj) in directions.iteritems():
                if not master.canMove(d):
                    continue
                nei = (pos[0]+di, pos[1]+dj)
                if nei in adj[pos]:
                    continue
                adj[pos][nei] = master.move(d)
                if nei not in lookup:
                    dfs(nei, target, master, lookup, adj)
                adj[nei][pos] = master.move(rollback[d])
                        
        def dijkstra(adj, start, target):
            dist = {start:0}
            min_heap = [(0, start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if dist[u] < curr:
                    continue
                for v, w in adj[u].iteritems():
                    if v in dist and dist[v] <= curr+w:
                        continue
                    dist[v] = curr+w
                    heapq.heappush(min_heap, (curr+w, v))
            return dist[target] if target in dist else -1 
        
        start = (0, 0)
        target = [None]
        adj = collections.defaultdict(dict)
        dfs(start, target, master, set(), adj)
        if not target[0]:
            return -1
        return dijkstra(adj, start, target[0])