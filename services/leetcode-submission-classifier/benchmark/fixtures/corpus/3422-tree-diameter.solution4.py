# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tree-diameter
# source_path: LeetCode-Solutions-master/Python/tree-diameter.py
# solution_class: Solution4
# submission_id: d74f11de904acb4916226ff23b286ff151e7f1ac
# seed: 1967694225

# Time:  O(|V| + |E|)
# Space: O(|E|)

# iterative dfs

class Solution4(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
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
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        _, root = bfs(0)
        d, _ = bfs(root)
        return d