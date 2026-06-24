# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reorder-routes-to-make-all-paths-lead-to-the-city-zero
# source_path: LeetCode-Solutions-master/Python/reorder-routes-to-make-all-paths-lead-to-the-city-zero.py
# solution_class: Solution
# submission_id: 85db30ffe46a5c502eb56bf10908d83c82982ba4
# seed: 2834440283

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        lookup, graph = set(), collections.defaultdict(list)
        for u, v in connections:
            lookup.add(u*n+v)
            graph[v].append(u)
            graph[u].append(v) 
        result = 0
        stk = [(-1, 0)]
        while stk:
            parent, u = stk.pop()
            result += (parent*n+u in lookup)
            for v in reversed(graph[u]):
                if v == parent:
                    continue
                stk.append((u, v))
        return result