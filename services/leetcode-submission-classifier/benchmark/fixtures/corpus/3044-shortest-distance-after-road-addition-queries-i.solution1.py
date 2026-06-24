# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-after-road-addition-queries-i
# source_path: LeetCode-Solutions-master/Python/shortest-distance-after-road-addition-queries-i.py
# solution_class: Solution
# submission_id: 2717fdcdbd4e860820073000058ce7f33b21a188
# seed: 1132918037

# Time:  O(n^2)
# Space: O(n^2)

# bfs

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def bfs(u, v):
            adj[u].append(v)
            q = [u]
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if dist[u]+1 >= dist[v]:
                            continue
                        dist[v] = dist[u]+1
                        new_q.append(v)
                q = new_q
            return dist[-1]

        adj = [[] for _ in xrange(n)]
        for u in xrange(n-1):
            adj[u].append(u+1)
        dist = range(n)
        return [bfs(u, v) for u, v in queries]