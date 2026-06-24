# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-if-path-exists-in-graph
# source_path: LeetCode-Solutions-master/Python/find-if-path-exists-in-graph.py
# solution_class: Solution
# submission_id: cc6b0b3d06db441d2b3f4fdb43caabc6b8ca2343
# seed: 2359376422

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# bi-bfs solution

class Solution(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        def bi_bfs(adj, start, target):
            left, right = {start}, {target}
            lookup = set()
            steps = 0
            while left:
                for pos in left:
                    lookup.add(pos)
                new_left = set()
                for pos in left:
                    if pos in right: 
                        return steps
                    for nei in adj[pos]:
                        if nei in lookup:
                            continue
                        new_left.add(nei)
                left = new_left
                steps += 1
                if len(left) > len(right): 
                    left, right = right, left
            return -1

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return bi_bfs(adj, start, end) >= 0