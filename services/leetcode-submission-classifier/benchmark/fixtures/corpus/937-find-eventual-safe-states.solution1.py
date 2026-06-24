# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-eventual-safe-states
# source_path: LeetCode-Solutions-master/Python/find-eventual-safe-states.py
# solution_class: Solution
# submission_id: 498d8b9e8fba2ee8ae0d11237309f1fb21a5a80d
# seed: 1047298028

# Time:  O(|V| + |E|)
# Space: O(|V|)

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        WHITE, GRAY, BLACK = range(3)

        def dfs(graph, node, lookup):
            if lookup[node] != WHITE:
                return lookup[node] == BLACK
            lookup[node] = GRAY
            if any(not dfs(graph, child, lookup) for child in graph[node]):
                return False
            lookup[node] = BLACK
            return True

        lookup = [WHITE]*len(graph)
        return filter(lambda node: dfs(graph, node, lookup), xrange(len(graph)))