# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-path-in-a-hidden-grid
# source_path: LeetCode-Solutions-master/Python/shortest-path-in-a-hidden-grid.py
# solution_class: Solution2
# submission_id: bd8a54b5cf0e263e1b8184f3fe9c2ad02edab6f2
# seed: 2722186035

# Time:  O(m * n)
# Space: O(m * n)

class GridMaster(object):
    def canMove(self, direction):
        pass

    def move(self, direction):
        pass

    def isTarget(self):
        pass


import collections

class Solution2(object):
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
                adj[pos].add(nei)
                adj[nei].add(pos)
                if nei in lookup:
                    continue
                master.move(d)
                dfs(nei, target, master, lookup, adj)
                master.move(rollback[d])
                        
        def bfs(adj, start, target):
            q = [start]
            lookup = set(q)
            steps = 0
            while q:
                new_q = []
                for pos in q:
                    if pos == target:
                        return steps
                    for nei in adj[pos]:
                        if nei in lookup:
                            continue
                        lookup.add(nei)
                        new_q.append(nei)
                q = new_q
                steps += 1
            return -1  
        
        start = (0, 0)
        target = [None]
        adj = collections.defaultdict(set)
        dfs(start, target, master, set(), adj)
        if not target[0]:
            return -1
        return bfs(adj, start, target[0])