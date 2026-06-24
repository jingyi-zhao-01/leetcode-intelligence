# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-paths-from-source-to-target
# source_path: LeetCode-Solutions-master/Python/all-paths-from-source-to-target.py
# solution_class: Solution
# submission_id: 7b9dbce0c0d6c055135efe691415d398be3bec0b
# seed: 1584539367

# Time:  O(p + r * n), p is the count of all the possible paths in graph,
#                      r is the count of the result.
# Space: O(n)

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(graph, curr, path, result):
            if curr == len(graph)-1:
                result.append(path[:])
                return
            for node in graph[curr]:
                path.append(node)
                dfs(graph, node, path, result)
                path.pop()

        result = []
        dfs(graph, 0, [0], result)
        return result