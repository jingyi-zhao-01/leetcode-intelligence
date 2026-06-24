# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-path-exists-in-graph
# source_path: LeetCode-Solutions-master/Python/find-if-path-exists-in-graph.py
# solution_class: Solution2
# submission_id: 069f1c417ecc607d12c8d682f27e5f2a907e9971
# seed: 196275035

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# bi-bfs solution

class Solution2(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
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

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bfs(adj, start, end) >= 0