# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: graph-valid-tree
# source_path: LeetCode-Solutions-master/Python/graph-valid-tree.py
# solution_class: Solution2
# submission_id: 785b92250aec08bdbeb623fcfac28587457e7c1c
# seed: 3011951911

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# BFS solution. Same complexity but faster version.

class Solution2(object):
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        # A structure to track each node's [visited_from, neighbors]
        visited_from = [-1] * n
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # BFS to check whether the graph is valid tree.
        q = collections.deque([0])
        visited = set([0])
        while q:
            i = q.popleft()
            for node in neighbors[i]:
                if node != visited_from[i]:
                    if node in visited:
                        return False
                    else:
                        visited.add(node)
                        visited_from[node] = i
                        q.append(node)
        return len(visited) == n