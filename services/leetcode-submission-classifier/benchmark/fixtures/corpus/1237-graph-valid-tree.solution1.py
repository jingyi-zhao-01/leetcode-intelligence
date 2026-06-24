# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: graph-valid-tree
# source_path: LeetCode-Solutions-master/Python/graph-valid-tree.py
# solution_class: Solution
# submission_id: 781c16a567c4da92c5bf787398792fa17f52f306
# seed: 1490532914

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# BFS solution. Same complexity but faster version.

class Solution(object):
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        if len(edges) != n - 1:  # Check number of edges.
            return False

        # init node's neighbors in dict
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # BFS to check whether the graph is valid tree.
        q = collections.deque([0])
        visited = set([0])
        while q:
            curr = q.popleft()
            for node in neighbors[curr]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)

        return len(visited) == n