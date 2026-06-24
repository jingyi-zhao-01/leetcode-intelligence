# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-last-marked-nodes-in-tree
# source_path: LeetCode-Solutions-master/Python/find-the-last-marked-nodes-in-tree.py
# solution_class: Solution
# submission_id: 74809fe2d45eb5565c732e6cb186385f122fff4d
# seed: 257852125

# Time:  O(n)
# Space: O(n)

# bfs

class Solution(object):
    def lastMarkedNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def bfs(root):
            new_root = -1
            dist = [-1]*len(adj)
            dist[root] = 0
            q = [root]
            while q:
                new_root = q[0]
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if dist[v] != -1:
                            continue
                        dist[v] = dist[u]+1
                        new_q.append(v)
                q = new_q
            return dist, new_root
            
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        _, u = bfs(0)
        dist1, v = bfs(u)
        dist2, _ = bfs(v)
        return [u if dist1[w] > dist2[w] else v for w in xrange(len(adj))]