# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frog-position-after-t-seconds
# source_path: LeetCode-Solutions-master/Python/frog-position-after-t-seconds.py
# solution_class: Solution2
# submission_id: 27593d7cb340d94cae61d209477ada268142813e
# seed: 263187673

# Time:  O(n)
# Space: O(n)

import collections


# bfs solution with better precision

class Solution2(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """                
        G = collections.defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        stk = [(t, 1, 0, 1)]
        while stk:
            t, node, parent, choices = stk.pop()
            if not t or not (len(G[node])-(parent != 0)):
                if node == target:
                    return 1.0/choices
                continue
            for child in G[node]:
                if child == parent:
                    continue
                stk.append((t-1, child, node,
                            choices*(len(G[node])-(parent != 0))))
        return 0.0