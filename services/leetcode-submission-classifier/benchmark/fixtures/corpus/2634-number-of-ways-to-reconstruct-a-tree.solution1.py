# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-reconstruct-a-tree
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-reconstruct-a-tree.py
# solution_class: Solution
# submission_id: ae31e33182fae29f5d31280b3102813fcf06043e
# seed: 1179494552

# Time:  O(nlogn)
# Space: O(n)

import collections

class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        adj = collections.defaultdict(set)
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        n, mul = len(adj), False
        lookup = set()
        for node in sorted(adj.iterkeys(), key=lambda i: len(adj[i]), reverse=True):
            lookup.add(node)
            parent = 0
            for x in adj[node]:
                if x not in lookup:
                    continue
                if parent == 0 or len(adj[x]) < len(adj[parent]):
                    parent = x
            if parent:
                if any(True for x in adj[node] if x != parent and x not in adj[parent]):
                    return 0
                mul |= len(adj[parent]) == len(adj[node])
            elif len(adj[node]) != n-1:
                return 0
        return 1 + mul