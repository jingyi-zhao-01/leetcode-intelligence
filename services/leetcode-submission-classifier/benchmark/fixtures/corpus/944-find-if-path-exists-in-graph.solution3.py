# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-path-exists-in-graph
# source_path: LeetCode-Solutions-master/Python/find-if-path-exists-in-graph.py
# solution_class: Solution3
# submission_id: 63c5eefe90cb7ac2f0c49a091f933725c7f77e3a
# seed: 349932743

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# bi-bfs solution

class Solution3(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        def dfs(adj, start, target):
            stk = [start]
            lookup = set(stk)
            while stk:
                pos = stk.pop()
                if pos == target:
                    return True
                for nei in reversed(adj[pos]):
                    if nei in lookup:
                        continue
                    lookup.add(nei)
                    stk.append(nei)
            return False 

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return dfs(adj, start, end)