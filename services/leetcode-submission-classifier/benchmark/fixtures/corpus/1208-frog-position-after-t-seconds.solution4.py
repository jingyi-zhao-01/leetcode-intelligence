# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frog-position-after-t-seconds
# source_path: LeetCode-Solutions-master/Python/frog-position-after-t-seconds.py
# solution_class: Solution4
# submission_id: 2cd5ac5ffa0778d4a0276750b8b18233447b331e
# seed: 1074614550

# Time:  O(n)
# Space: O(n)

import collections


# bfs solution with better precision

class Solution4(object):
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
                return float(node == target)
            for child in G[node]:
                if child == parent:
                    continue
                result = dfs(G, target, t-1, child, node)
                if result:
                    break
            return result/(len(G[node])-(parent != 0))
        
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        return dfs(G, target, t, 1, 0)