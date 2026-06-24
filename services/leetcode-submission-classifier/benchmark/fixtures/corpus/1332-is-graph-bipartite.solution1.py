# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: is-graph-bipartite
# source_path: LeetCode-Solutions-master/Python/is-graph-bipartite.py
# solution_class: Solution
# submission_id: fa5d5a1168796341a03277a14c6dbfe6996772a9
# seed: 108105890

# Time:  O(|V| + |E|)
# Space: O(|V|)

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        for node in xrange(len(graph)):
            if node in color:
                continue
            stack = [node]
            color[node] = 0
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in color:
                        stack.append(neighbor)
                        color[neighbor] = color[curr] ^ 1
                    elif color[neighbor] == color[curr]:
                        return False
        return True