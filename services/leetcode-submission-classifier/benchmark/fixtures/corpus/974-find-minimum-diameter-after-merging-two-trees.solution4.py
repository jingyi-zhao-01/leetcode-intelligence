# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-minimum-diameter-after-merging-two-trees
# source_path: LeetCode-Solutions-master/Python/find-minimum-diameter-after-merging-two-trees.py
# solution_class: Solution4
# submission_id: 7e2b448097fe7ffe212a8b32f80f2a2a84daa22d
# seed: 1804208490

# Time:  O(n + m)
# Space: O(n + m)

# iterative dfs, tree diameter

class Solution4(object):
    def minimumDiameterAfterMerge(self, edges1, edges2):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//2
    
        def tree_diameter(edges):
            def bfs(root):
                d = new_root = -1
                lookup = [False]*len(adj)
                lookup[root] = True
                q = [root]
                while q:
                    d, new_root = d+1, q[0]
                    new_q = []
                    for u in q:
                        for v in adj[u]:
                            if lookup[v]:
                                continue
                            lookup[v] = True
                            new_q.append(v)
                    q = new_q
                return d, new_root
            
            adj = [[] for _ in xrange(len(edges)+1)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            _, root = bfs(0)
            d, _ = bfs(root)
            return d
        
        d1 = tree_diameter(edges1)
        d2 = tree_diameter(edges2)
        return max(ceil_divide(d1, 2)+1+ceil_divide(d2, 2), d1, d2)