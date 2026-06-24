# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-diameter-endpoints-of-a-tree
# source_path: LeetCode-Solutions-master/Python/find-diameter-endpoints-of-a-tree.py
# solution_class: Solution
# submission_id: 85fa4abbd9eec847fc478f265d95237bb0149d1c
# seed: 89188295

# Time:  O(n)
# Space: O(n)

# tree diameter, bfs

class Solution(object):
    def findSpecialNodes(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: str
        """
        def bfs(u):
            lookup = [False]*len(adj)
            lookup[u] = True
            q = [u]
            new_q = []
            while q:
                new_q = []
                for u in q:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = True
                        new_q.append(v)
                q, new_q = new_q, q
            return new_q
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = ['0']*n
        far = bfs(0)
        for u in far:
            result[u] = '1'
        for u in bfs(far[0]):
            result[u] = '1'
        return "".join(result)