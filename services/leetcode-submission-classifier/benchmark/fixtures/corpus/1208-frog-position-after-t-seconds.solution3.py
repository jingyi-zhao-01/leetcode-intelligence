# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frog-position-after-t-seconds
# source_path: LeetCode-Solutions-master/Python/frog-position-after-t-seconds.py
# solution_class: Solution3
# submission_id: b72c59c5b1ec4f48d3655f09994c79fc968322a6
# seed: 399887329

# Time:  O(n)
# Space: O(n)

import collections


# bfs solution with better precision

class Solution3(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """        
        def dfs(G, target, t, node, parent):
            if not t or not (len(G[node])-(parent != 0)):
                return int(node == target)
            result = 0
            for child in G[node]:
                if child == parent:
                    continue
                result = dfs(G, target, t-1, child, node)
                if result:
                    break
            return result*(len(G[node])-(parent != 0))
        
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        choices = dfs(G, target, t, 1, 0)
        return 1.0/choices if choices else 0.0