# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reorder-routes-to-make-all-paths-lead-to-the-city-zero
# source_path: LeetCode-Solutions-master/Python/reorder-routes-to-make-all-paths-lead-to-the-city-zero.py
# solution_class: Solution2
# submission_id: abe1f7aa5a897f26eea3549ee2252d8527a5ba19
# seed: 1799674845

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        def dfs(n, lookup, graph, parent, u):
            result = (parent*n+u in lookup)
            for v in graph[u]:
                if v == parent:
                    continue
                result += dfs(n, lookup, graph, u, v)  
            return result

        lookup, graph = set(), collections.defaultdict(list)
        for u, v in connections:
            lookup.add(u*n+v)
            graph[v].append(u)
            graph[u].append(v) 
        return dfs(n, lookup, graph, -1, 0)