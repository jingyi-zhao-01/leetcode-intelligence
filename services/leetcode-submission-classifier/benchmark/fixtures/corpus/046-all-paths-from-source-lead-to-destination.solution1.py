# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-paths-from-source-lead-to-destination
# source_path: LeetCode-Solutions-master/Python/all-paths-from-source-lead-to-destination.py
# solution_class: Solution
# submission_id: 07dce0f17faf5b10a2cc846aee38370ef769bba6
# seed: 3836386137

# Time:  O(n + e)
# Space: O(n + e)

import collections

class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        UNVISITED, VISITING, DONE = range(3)
        def dfs(children, node, destination, status):
            if status[node] == DONE:
                return True
            if status[node] == VISITING:
                return False
            status[node] = VISITING
            if node not in children and node != destination:
                return False
            if node in children:
                for child in children[node]:
                    if not dfs(children, child, destination, status):
                        return False
            status[node] = DONE
            return True
        
        children = collections.defaultdict(list)
        for parent, child in edges:
            children[parent].append(child)
        return dfs(children, source, destination, [0]*n)